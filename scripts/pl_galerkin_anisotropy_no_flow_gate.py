#!/usr/bin/env python3
"""Actual recursive-PL Galerkin no-flow gate for the higher-shell anisotropy.

This is a deliberately narrow falsification/control calculation.

Take the canonical 16-cell spatial completion and exactly the same global
barycentric subdivision used by ``bcqg_global_manifold_gate.py``.  Let L_g be
the combinatorial Laplacian of the tetrahedron dual graph at generation g and
let P_g inject one normalized block-constant degree of freedom per parent
tetrahedron into its 24 barycentric children.

For a separable geometry-only coarse graining

    K_fine = L_{g+1} tensor J_internal,
    P_full = P_g tensor I_internal,

Galerkin projection gives

    K_coarse = (P_g^T L_{g+1} P_g) tensor J_internal.

Therefore no geometry-only linear projection can change ratios among internal
S4 couplings.  This gate additionally checks on the *actual* recursive PL
complex that

    P_g^T L_{g+1} P_g = (1/4) L_g

for g=0->1 and 1->2, to machine precision.  Hence the completed higher-shell
S4 seed R_aniso is exactly stationary in this separable control ansatz.

This is NOT the physical Peter-Weyl RG.  Its purpose is to prove that any real
flow of R_aniso must come from non-separable internal recoupling/dynamics, not
from spatial barycentric smoothing by itself.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.sparse import coo_matrix

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from bcqg_global_manifold_gate import cross_polytope_boundary_4


C0 = 12.860443113390883
J_SHAPE = -0.3629900150598623
J_ORIENT = 0.7912767588958898
R_ANISO = (J_ORIENT - J_SHAPE) / C0
CHILDREN_PER_TET = math.factorial(4)  # barycentric top-simplex chains


def barycentric_subdivision_with_parent(tets):
    """Same subdivision semantics as bcqg_global_manifold_gate + parent map."""
    faces = set()
    for tet in tets:
        for size in range(1, 5):
            faces.update(tuple(sorted(f)) for f in itertools.combinations(tet, size))
    fid = {f: i for i, f in enumerate(sorted(faces, key=lambda x: (len(x), x)))}

    parent = {}
    for ti, tet in enumerate(tets):
        for perm in itertools.permutations(tet):
            prefix = []
            chain = []
            for vertex in perm:
                prefix.append(vertex)
                chain.append(fid[tuple(sorted(prefix))])
            child = tuple(sorted(chain))
            old = parent.get(child)
            if old is not None and old != ti:
                raise RuntimeError("top-dimensional barycentric child has two parents")
            parent[child] = ti

    children = sorted(parent)
    return children, [parent[c] for c in children]


def dual_edges(tets):
    faces = defaultdict(list)
    for ti, tet in enumerate(tets):
        for f in itertools.combinations(tet, 3):
            faces[tuple(sorted(f))].append(ti)
    if any(len(v) != 2 for v in faces.values()):
        raise RuntimeError("non-closed triangular face incidence")
    return sorted(tuple(v) for v in faces.values())


def laplacian(n, edges):
    degree = np.zeros(n, dtype=float)
    row, col, data = [], [], []
    for a, b in edges:
        degree[a] += 1.0
        degree[b] += 1.0
        row.extend((a, b))
        col.extend((b, a))
        data.extend((-1.0, -1.0))
    row.extend(range(n))
    col.extend(range(n))
    data.extend(degree.tolist())
    return coo_matrix((data, (row, col)), shape=(n, n)).tocsr()


def frob_sparse(A):
    return float(np.sqrt(A.multiply(A).sum()))


def one_step(tets, generation):
    fine, parent = barycentric_subdivision_with_parent(tets)
    n_coarse, n_fine = len(tets), len(fine)
    counts = np.bincount(parent, minlength=n_coarse)
    if not np.all(counts == CHILDREN_PER_TET):
        raise RuntimeError(f"unexpected child counts: {counts.tolist()}")

    Lc = laplacian(n_coarse, dual_edges(tets))
    Lf = laplacian(n_fine, dual_edges(fine))

    rows = np.arange(n_fine)
    cols = np.asarray(parent, dtype=int)
    vals = np.full(n_fine, 1.0 / math.sqrt(CHILDREN_PER_TET))
    P = coo_matrix((vals, (rows, cols)), shape=(n_fine, n_coarse)).tocsr()

    Leff = (P.T @ Lf @ P).tocsr()
    denom = float(Lc.multiply(Lc).sum())
    scale = float(Leff.multiply(Lc).sum() / denom)
    residual = frob_sparse(Leff - scale * Lc) / max(frob_sparse(Leff), 1e-30)

    # Cross-boundary fine dual edges per coarse dual edge.  This makes the 1/4
    # factor transparent: 6 crossing child edges / 24 normalization.
    crossing = defaultdict(int)
    for a, b in dual_edges(fine):
        pa, pb = parent[a], parent[b]
        if pa != pb:
            crossing[tuple(sorted((pa, pb)))] += 1
    coarse_edges = dual_edges(tets)
    cross_counts = [crossing[e] for e in coarse_edges]

    c0_out = scale * C0
    js_out = scale * J_SHAPE
    jo_out = scale * J_ORIENT
    r_out = (jo_out - js_out) / c0_out

    return {
        "generation_in": generation,
        "generation_out": generation + 1,
        "coarse_tetrahedra": n_coarse,
        "fine_tetrahedra": n_fine,
        "children_per_parent": int(counts[0]),
        "coarse_dual_edges": len(coarse_edges),
        "fine_dual_edges": len(dual_edges(fine)),
        "crossing_fine_edges_per_coarse_edge_min": int(min(cross_counts)),
        "crossing_fine_edges_per_coarse_edge_max": int(max(cross_counts)),
        "galerkin_scale": scale,
        "target_scale_one_quarter": 0.25,
        "laplacian_relative_residual": residual,
        "couplings_in": {
            "c0": C0,
            "J_shape": J_SHAPE,
            "J_orient": J_ORIENT,
            "R_aniso": R_ANISO,
        },
        "couplings_after_geometry_only_projection": {
            "c0": c0_out,
            "J_shape": js_out,
            "J_orient": jo_out,
            "R_aniso": r_out,
        },
        "R_aniso_change": r_out - R_ANISO,
        "fine_tets": fine,
    }


def run(refinements=2):
    if refinements < 1:
        raise ValueError("refinements must be >=1")
    tets = cross_polytope_boundary_4()
    rows = []
    for g in range(refinements):
        row = one_step(tets, g)
        tets = row.pop("fine_tets")
        rows.append(row)

    tol = 2e-12
    passed = all(
        abs(r["galerkin_scale"] - 0.25) < tol
        and r["laplacian_relative_residual"] < tol
        and r["crossing_fine_edges_per_coarse_edge_min"] == 6
        and r["crossing_fine_edges_per_coarse_edge_max"] == 6
        and abs(r["R_aniso_change"]) < tol
        for r in rows
    )
    return {
        "status": "recursive PL geometry-only Galerkin anisotropy no-flow control",
        "passed": bool(passed),
        "spatial_complex": "16-cell boundary with canonical global barycentric subdivision",
        "projection": "normalized block-constant P0: each parent -> 24 children with amplitude 1/sqrt(24)",
        "exact_factorization": "(P tensor I)^T (L_fine tensor J) (P tensor I) = (P^T L_fine P) tensor J",
        "checked_PL_identity": "P^T L_{g+1} P = (1/4) L_g",
        "local_R_aniso": R_ANISO,
        "steps": rows,
        "conclusion": (
            "Within the separable geometry-only Galerkin ansatz, barycentric PL smoothing rescales all internal S4 pair couplings by the same factor and leaves R_aniso exactly unchanged. "
            "Therefore any nontrivial RG beta function for R_aniso must originate in internal Peter-Weyl recoupling/non-separable block dynamics (or another explicitly derived coupling between geometry and internal channels), not in spatial averaging alone."
        ),
        "scope_note": (
            "This is a no-flow control theorem for a separable linear blocking map, not the physical quantum RG and not evidence that R_aniso survives in the infrared."
        ),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--refinements", type=int, default=2)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    out = run(args.refinements)
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
