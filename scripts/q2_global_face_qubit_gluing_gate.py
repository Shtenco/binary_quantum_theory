#!/usr/bin/env python3
"""Exact global gluing of the q=2 tetrahedral carrier on the 16-cell boundary.

The selected q=2 PL completion is the boundary of the four-dimensional
cross-polytope.  Each tetrahedral facet contains one signed vertex from each of
four coordinate axes.  Its four triangular faces are therefore canonically
labelled by the omitted axis.  We identify those four face colours with the
four frozen q=2 route labels 00,01,10,11.

This gate proves purely combinatorially that:
- every triangular face is shared by exactly two tetrahedra;
- both incident tetrahedra assign the same q=2 carrier label to that face;
- the dual graph of the 16 tetrahedra is exactly the four-dimensional cube Q4;
- neighboring tetrahedra differ by one sign bit and hence have opposite parity
  orientation;
- the local Walsh-character tetrahedral flux frame can therefore be glued with
  opposite outward flux across every shared face.

This is an exact kinematic gluing theorem for the selected PL completion.  It
does not prove that the microscopic dynamics uniquely selects that completion
or its semiclassical measure.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from collections import defaultdict
from pathlib import Path

import numpy as np

ROUTE_LABELS = {
    0: (0, 0),
    1: (0, 1),
    2: (1, 0),
    3: (1, 1),
}


def walsh(mask: int, bits: tuple[int, int]) -> int:
    parity = ((mask & 1) * bits[0] + ((mask >> 1) & 1) * bits[1]) & 1
    return 1 if parity == 0 else -1


def local_fluxes() -> dict[int, np.ndarray]:
    return {
        axis: np.array([walsh(m, ROUTE_LABELS[axis]) for m in (1, 2, 3)], float) / math.sqrt(3.0)
        for axis in range(4)
    }


def tetrahedra() -> list[tuple[int, int, int, int]]:
    """Sign vectors of the 16 facets; bit 1 means the negative axis vertex."""
    return list(itertools.product((0, 1), repeat=4))


def face_key(signs: tuple[int, ...], omitted_axis: int) -> tuple[tuple[int, int], ...]:
    return tuple((axis, signs[axis]) for axis in range(4) if axis != omitted_axis)


def hamming(a: tuple[int, ...], b: tuple[int, ...]) -> int:
    return sum(x != y for x, y in zip(a, b))


def run() -> dict[str, object]:
    cells = tetrahedra()
    flux = local_fluxes()
    incidence: dict[tuple, list[tuple[tuple[int, ...], int]]] = defaultdict(list)
    for cell in cells:
        for omitted in range(4):
            incidence[face_key(cell, omitted)].append((cell, omitted))

    shared_faces = []
    dual_edges = set()
    max_flux_mismatch = 0.0
    for key, entries in incidence.items():
        if len(entries) != 2:
            continue
        (a, ca), (b, cb) = entries
        dual_edges.add(tuple(sorted((a, b))))
        same_colour = ca == cb
        # Orientation parity on the cross-polytope boundary is bipartite up to
        # one global sign.  Adjacent cells differ in the omitted sign bit.
        pa = -1 if sum(a) % 2 else 1
        pb = -1 if sum(b) % 2 else 1
        fa = pa * flux[ca]
        fb = pb * flux[cb]
        mismatch = float(np.linalg.norm(fa + fb))
        max_flux_mismatch = max(max_flux_mismatch, mismatch)
        shared_faces.append({
            "omitted_axis": ca,
            "route_label": list(ROUTE_LABELS[ca]),
            "cells": [list(a), list(b)],
            "same_face_colour": bool(same_colour),
            "hamming_distance": hamming(a, b),
            "orientation_product": pa * pb,
            "outward_flux_sum_norm": mismatch,
        })

    degrees = {cell: 0 for cell in cells}
    for a, b in dual_edges:
        degrees[a] += 1
        degrees[b] += 1

    expected_q4_edges = {
        tuple(sorted((a, b)))
        for a, b in itertools.combinations(cells, 2)
        if hamming(a, b) == 1
    }

    local_gram = np.array([flux[i] for i in range(4)]) @ np.array([flux[i] for i in range(4)]).T
    target_gram = np.full((4, 4), -1.0 / 3.0)
    np.fill_diagonal(target_gram, 1.0)

    checks = {
        "sixteen_tetrahedra": len(cells) == 16,
        "thirty_two_triangle_faces": len(incidence) == 32,
        "each_face_two_sided": all(len(v) == 2 for v in incidence.values()),
        "four_faces_per_tetrahedron": all(degrees[c] == 4 for c in cells),
        "dual_graph_exact_Q4": dual_edges == expected_q4_edges and len(dual_edges) == 32,
        "shared_face_has_same_q2_label": all(r["same_face_colour"] for r in shared_faces),
        "neighbors_flip_exactly_one_sign_bit": all(r["hamming_distance"] == 1 for r in shared_faces),
        "neighbor_orientation_opposite": all(r["orientation_product"] == -1 for r in shared_faces),
        "outward_flux_cancels_on_shared_face": max_flux_mismatch < 1e-14,
        "local_flux_frame_remains_regular_tetrahedron": float(np.linalg.norm(local_gram - target_gram)) < 1e-14,
    }

    return {
        "status": "exact q=2 tetrahedral face-qubit carrier gluing on selected 16-cell PL completion",
        "passed": bool(all(checks.values())),
        "tetrahedra": len(cells),
        "triangular_faces": len(incidence),
        "dual_edges": len(dual_edges),
        "dual_graph": "Q4",
        "route_face_colouring": {str(k): list(v) for k, v in ROUTE_LABELS.items()},
        "maximum_shared_outward_flux_sum_norm": max_flux_mismatch,
        "checks": checks,
        "claim_boundary": (
            "Exact global kinematic compatibility of the local q=2 Walsh tetrahedral carrier with the selected 16-cell completion. "
            "Dynamical uniqueness/selection of this PL phase and a physical coarse-state measure remain open."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    out = run()
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
