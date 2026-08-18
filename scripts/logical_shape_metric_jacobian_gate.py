#!/usr/bin/env python3
"""Exact local logical-shape -> tetrahedral metric Jacobian.

For the j=1/2 logical singlet qubit, fixed face-spin norm J_i^2=3/4 and closure
determine all six pairwise face-flux dot products from the two intrinsic-shape
Bloch coordinates X,Z. Around the two regular oriented tetrahedron branches
(X,Z,Y)=(0,0,+/-1), reconstruct the edge Gram metric from face fluxes and
compute the exact two-dimensional metric tangent carried by X,Z.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def face_gram(x: float, z: float) -> np.ndarray:
    r2 = 3.0 / 4.0
    a = -1.0 / 4.0 - z / 2.0
    b = -1.0 / 4.0 + z / 4.0 - math.sqrt(3) * x / 4.0
    c = -1.0 / 4.0 + z / 4.0 + math.sqrt(3) * x / 4.0
    return np.array([[r2, a, b], [a, r2, c], [b, c, r2]], dtype=float)


def edge_metric(x: float, z: float) -> np.ndarray:
    G = face_gram(x, z)
    det = float(np.linalg.det(G))
    if det <= 0:
        raise ValueError("degenerate/non-Euclidean face Gram matrix")
    return 2.0 * math.sqrt(det) * np.linalg.inv(G)


def run(step: float = 1e-6):
    rt3 = math.sqrt(3.0)
    g0_exact = np.array([[2, 1, 1], [1, 2, 1], [1, 1, 2]], dtype=float)
    Mx_exact = np.array([
        [rt3 / 2, 0, rt3 / 2],
        [0, -rt3 / 2, -rt3 / 2],
        [rt3 / 2, -rt3 / 2, 0],
    ])
    Mz_exact = np.array([
        [0.5, 1.0, -0.5],
        [1.0, 0.5, -0.5],
        [-0.5, -0.5, -1.0],
    ])

    g0 = edge_metric(0.0, 0.0)
    Mx_fd = (edge_metric(step, 0.0) - edge_metric(-step, 0.0)) / (2 * step)
    Mz_fd = (edge_metric(0.0, step) - edge_metric(0.0, -step)) / (2 * step)

    gi = np.linalg.inv(g0_exact)
    trace_x = float(np.trace(gi @ Mx_exact))
    trace_z = float(np.trace(gi @ Mz_exact))
    shape_inner = np.array([
        [np.trace(gi @ Mx_exact @ gi @ Mx_exact), np.trace(gi @ Mx_exact @ gi @ Mz_exact)],
        [np.trace(gi @ Mz_exact @ gi @ Mx_exact), np.trace(gi @ Mz_exact @ gi @ Mz_exact)],
    ], dtype=float)

    def vec6(M):
        return np.array([M[0,0], M[1,1], M[2,2], M[0,1], M[0,2], M[1,2]])

    J6 = np.column_stack([vec6(Mx_exact), vec6(Mz_exact)])
    rank = int(np.linalg.matrix_rank(J6, tol=1e-12))

    det0 = float(np.linalg.det(g0_exact))
    det_dx = float((np.linalg.det(edge_metric(step, 0)) - np.linalg.det(edge_metric(-step, 0))) / (2*step))
    det_dz = float((np.linalg.det(edge_metric(0, step)) - np.linalg.det(edge_metric(0, -step))) / (2*step))

    errors = {
        "background_metric": float(np.linalg.norm(g0 - g0_exact)),
        "Mx_finite_difference": float(np.linalg.norm(Mx_fd - Mx_exact)),
        "Mz_finite_difference": float(np.linalg.norm(Mz_fd - Mz_exact)),
        "tracefree_max": max(abs(trace_x), abs(trace_z)),
        "shape_inner_to_3_over_2_identity": float(np.linalg.norm(shape_inner - 1.5 * np.eye(2))),
        "linear_det_change_max": max(abs(det_dx), abs(det_dz)),
    }
    passed = (
        rank == 2
        and errors["background_metric"] < 1e-12
        and errors["Mx_finite_difference"] < 2e-8
        and errors["Mz_finite_difference"] < 2e-8
        and errors["tracefree_max"] < 1e-12
        and errors["shape_inner_to_3_over_2_identity"] < 1e-12
        and errors["linear_det_change_max"] < 2e-8
    )

    return {
        "status": "exact local logical shape-to-metric Jacobian at the regular tetrahedron",
        "passed": bool(passed),
        "background_logical_branches": ["X=0,Z=0,Y=+1", "X=0,Z=0,Y=-1"],
        "background_edge_metric": g0_exact.tolist(),
        "background_det_metric": det0,
        "face_gram_formula": {
            "E1.E2=E3.E4": "-1/4-Z/2",
            "E1.E3=E2.E4": "-1/4+Z/4-sqrt(3)X/4",
            "E1.E4=E2.E3": "-1/4+Z/4+sqrt(3)X/4",
        },
        "metric_reconstruction": "g(X,Z)=2 sqrt(det G(X,Z)) G(X,Z)^-1",
        "M_X": Mx_exact.tolist(),
        "M_Z": Mz_exact.tolist(),
        "metric_tangent_rank": rank,
        "background_covariant_traces": {"X": trace_x, "Z": trace_z},
        "DeWitt_tracefree_shape_inner_matrix": shape_inner.tolist(),
        "normalization": "Tr(g0^-1 M_A g0^-1 M_B)=(3/2) delta_AB",
        "orientation_linear_metric_derivative": 0.0,
        "errors": errors,
        "conclusion": (
            "The intrinsic logical shape doublet (X,Z) maps with rank two to an orthogonal, equal-norm, trace-free tangent of the reconstructed tetrahedral metric. "
            "The two regular orientation branches Y=+/-1 have the same intrinsic metric Jacobian."
        ),
        "scope": "Local tetrahedral geometry at fixed face-spin norm; no external experimental observable is inferred.",
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--step", type=float, default=1e-6)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    out = run(args.step)
    print(json.dumps(out, indent=2))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
