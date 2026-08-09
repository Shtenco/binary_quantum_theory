#!/usr/bin/env python3
"""Coordinate-free local manifold-dimension gate from vertex-link homology.

The physical use case is a coarse simplicial/hypergraph complex produced by a
frozen microscopic rule.  A combinatorial D-manifold has vertex links with the
homology of S^(D-1).  This script provides a JSON-input mode for maximal
simplices and self-tests the implementation on periodic Freudenthal
triangulations in dimensions 2, 3 and 4.

Homology is computed over GF(2); passing this gate is necessary, not sufficient,
for a genuine PL manifold.
"""

from __future__ import annotations

import argparse
import collections
import itertools
import json
from pathlib import Path

import numpy as np


def gf2_rank(matrix: np.ndarray) -> int:
    A = np.asarray(matrix, dtype=np.uint8).copy() & 1
    m, n = A.shape
    rank = 0
    col = 0
    while rank < m and col < n:
        pivots = np.flatnonzero(A[rank:, col])
        if len(pivots) == 0:
            col += 1
            continue
        pivot = rank + int(pivots[0])
        if pivot != rank:
            A[[rank, pivot]] = A[[pivot, rank]]
        for row in range(m):
            if row != rank and A[row, col]:
                A[row] ^= A[rank]
        rank += 1
        col += 1
    return rank


def all_faces(maximal_simplices: list[tuple[int, ...]]) -> dict[int, set[tuple[int, ...]]]:
    faces: dict[int, set[tuple[int, ...]]] = collections.defaultdict(set)
    for simplex in maximal_simplices:
        for size in range(1, len(simplex) + 1):
            for face in itertools.combinations(simplex, size):
                faces[size - 1].add(tuple(face))
    return faces


def betti_numbers(maximal_simplices: list[tuple[int, ...]]) -> list[int]:
    faces = all_faces(maximal_simplices)
    if not faces:
        return []
    max_dimension = max(faces)
    boundary_rank: dict[int, int] = {}

    for k in range(1, max_dimension + 1):
        rows = sorted(faces[k - 1])
        cols = sorted(faces[k])
        row_index = {face: i for i, face in enumerate(rows)}
        B = np.zeros((len(rows), len(cols)), dtype=np.uint8)
        for j, simplex in enumerate(cols):
            for face in itertools.combinations(simplex, k):
                B[row_index[tuple(face)], j] = 1
        boundary_rank[k] = gf2_rank(B)

    betti = []
    for k in range(max_dimension + 1):
        n_k = len(faces[k])
        rank_k = boundary_rank.get(k, 0)
        rank_k1 = boundary_rank.get(k + 1, 0)
        betti.append(int(n_k - rank_k - rank_k1))
    return betti


def vertex_link(maximal_simplices: list[tuple[int, ...]], vertex: int) -> list[tuple[int, ...]]:
    candidates: set[tuple[int, ...]] = set()
    for simplex in maximal_simplices:
        if vertex in simplex:
            reduced = tuple(x for x in simplex if x != vertex)
            if reduced:
                candidates.add(tuple(sorted(reduced)))

    items = list(candidates)
    sets = [set(x) for x in items]
    maximal = []
    for i, simplex in enumerate(items):
        si = sets[i]
        if not any(i != j and si < sets[j] for j in range(len(items))):
            maximal.append(simplex)
    return sorted(maximal)


def infer_sphere_dimension(betti: list[int]) -> int | None:
    """Infer m for a homology S^m, m>=1, from Betti numbers over GF(2)."""
    if len(betti) < 2:
        return None
    m = len(betti) - 1
    target = [0] * (m + 1)
    target[0] = 1
    target[m] = 1
    return m if betti == target else None


def analyze(maximal_simplices: list[tuple[int, ...]]) -> dict[str, object]:
    vertices = sorted(set(itertools.chain.from_iterable(maximal_simplices)))
    rows = []
    inferred = []
    for vertex in vertices:
        link = vertex_link(maximal_simplices, vertex)
        betti = betti_numbers(link)
        sphere_dim = infer_sphere_dimension(betti)
        local_dim = None if sphere_dim is None else sphere_dim + 1
        inferred.append(local_dim)
        rows.append({
            "vertex": int(vertex),
            "link_betti_GF2": betti,
            "inferred_local_dimension": local_dim,
        })

    counts = collections.Counter(inferred)
    finite_dims = [d for d in inferred if d is not None]
    dominant = None
    if finite_dims:
        dominant = collections.Counter(finite_dims).most_common(1)[0][0]
    defects = sum(d != dominant for d in inferred) if dominant is not None else len(inferred)

    return {
        "vertices": len(vertices),
        "maximal_simplices": len(maximal_simplices),
        "dominant_local_dimension": dominant,
        "manifold_link_defect_fraction": defects / max(len(vertices), 1),
        "dimension_counts": {str(k): int(v) for k, v in counts.items()},
        "vertex_rows": rows,
        "scope_note": "GF(2) homology-sphere links are a necessary local manifold test, not a complete PL-manifold recognition theorem",
    }


def vertex_id(coord: np.ndarray, length: int, dimension: int) -> int:
    value = 0
    for axis in range(dimension):
        value += int(coord[axis] % length) * (length ** axis)
    return value


def freudenthal_torus(length: int, dimension: int) -> list[tuple[int, ...]]:
    maximal: set[tuple[int, ...]] = set()
    for base_tuple in itertools.product(range(length), repeat=dimension):
        base = np.asarray(base_tuple, dtype=int)
        for permutation in itertools.permutations(range(dimension)):
            points = [base.copy()]
            current = base.copy()
            for axis in permutation:
                current = current.copy()
                current[axis] += 1
                points.append(current.copy())
            simplex = tuple(sorted(vertex_id(p, length, dimension) for p in points))
            if len(set(simplex)) == dimension + 1:
                maximal.add(simplex)
    return sorted(maximal)


def self_test() -> dict[str, object]:
    controls = []
    all_passed = True
    for dimension in (2, 3, 4):
        simplices = freudenthal_torus(3, dimension)
        result = analyze(simplices)
        passed = (
            result["dominant_local_dimension"] == dimension
            and result["manifold_link_defect_fraction"] == 0.0
        )
        all_passed &= bool(passed)
        controls.append({
            "true_dimension": dimension,
            "vertices": result["vertices"],
            "maximal_simplices": result["maximal_simplices"],
            "inferred_dimension": result["dominant_local_dimension"],
            "defect_fraction": result["manifold_link_defect_fraction"],
            "passed": passed,
        })
    return {"controls": controls, "all_passed": all_passed}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        help="JSON file containing {'maximal_simplices': [[...], ...]}",
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.input:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        raw = payload.get("maximal_simplices")
        if not isinstance(raw, list):
            parser.error("input JSON must contain a list 'maximal_simplices'")
        simplices = [tuple(sorted(int(x) for x in simplex)) for simplex in raw]
        result = {"mode": "input", "analysis": analyze(simplices)}
    else:
        result = {"mode": "self-test", **self_test()}

    text = json.dumps(result, ensure_ascii=False, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")

    if result.get("mode") == "self-test" and not result.get("all_passed", False):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
