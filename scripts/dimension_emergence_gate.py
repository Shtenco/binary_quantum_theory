#!/usr/bin/env python3
"""Dimension-blind controls and a minimal binary causal-diamond null model.

This script is intentionally a falsification harness.  It does not assume four
spacetime dimensions when estimating dimension.  First it checks the heat-kernel
spectral-dimension estimator on periodic lattices of known dimension.  It then
applies the same logic to the least-structured binary reconvergent causal rule:

    one edge -> two alternative two-step paths -> reconvergence.

The latter is a null model for causal confluence, not the final CIMFIG rule set.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.linalg import eigvalsh


def torus_heat_return(length: int, dimension: int, times: np.ndarray) -> np.ndarray:
    """Exact normalized heat trace of a periodic nearest-neighbour lattice."""
    n = np.arange(length, dtype=float)
    lam1 = 2.0 - 2.0 * np.cos(2.0 * np.pi * n / length)
    p1 = np.array([np.exp(-t * lam1).mean() for t in times])
    return p1 ** dimension


def spectral_dimension(times: np.ndarray, heat_return: np.ndarray) -> np.ndarray:
    return -2.0 * np.gradient(np.log(heat_return), np.log(times))


def diamond_graph(generations: int, branches: int = 2) -> sparse.csr_matrix:
    """Hierarchical reconvergent graph with no coordinates or target dimension."""
    if generations < 1 or branches < 1:
        raise ValueError("generations and branches must be positive")
    edges = [(0, 1)]
    next_id = 2
    for _ in range(generations):
        new_edges: list[tuple[int, int]] = []
        for u, v in edges:
            mids = list(range(next_id, next_id + branches))
            next_id += branches
            for m in mids:
                new_edges.append((u, m))
                new_edges.append((m, v))
        edges = new_edges

    rows: list[int] = []
    cols: list[int] = []
    for u, v in edges:
        rows.extend((u, v))
        cols.extend((v, u))
    data = np.ones(len(rows), dtype=float)
    return sparse.csr_matrix((data, (rows, cols)), shape=(next_id, next_id))


def normalized_laplacian_dense(adjacency: sparse.csr_matrix) -> np.ndarray:
    degree = np.asarray(adjacency.sum(axis=1)).ravel()
    invsqrt = np.zeros_like(degree)
    mask = degree > 0
    invsqrt[mask] = 1.0 / np.sqrt(degree[mask])
    D = sparse.diags(invsqrt)
    return (sparse.eye(adjacency.shape[0]) - D @ adjacency @ D).toarray()


def window_mean(times: np.ndarray, values: np.ndarray, lo: float, hi: float) -> tuple[float, float]:
    mask = (times >= lo) & (times <= hi)
    if not np.any(mask):
        raise ValueError("empty averaging window")
    return float(values[mask].mean()), float(values[mask].std())


def run(max_generation: int = 5) -> dict[str, object]:
    # Independent calibration.  The estimator is not told the answer after the
    # heat trace is constructed.
    control_times = np.geomspace(0.5, 12.0, 120)
    controls = []
    for d, L in ((1, 128), (2, 64), (3, 32), (4, 24)):
        p = torus_heat_return(L, d, control_times)
        ds = spectral_dimension(control_times, p)
        mean, std = window_mean(control_times, ds, 5.0, 10.0)
        controls.append({
            "true_dimension": d,
            "torus_length": L,
            "spectral_dimension_mean_t5_t10": mean,
            "spectral_dimension_std_t5_t10": std,
            "relative_error": abs(mean - d) / d,
        })

    rows = []
    previous_nodes = None
    last_eigenvalues = None
    for g in range(2, max_generation + 1):
        A = diamond_graph(g, branches=2)
        nodes = int(A.shape[0])
        diameter = 2 ** g
        dH_step = None
        if previous_nodes is not None:
            dH_step = math.log(nodes / previous_nodes, 2.0)
        previous_nodes = nodes

        # Dense diagonalisation is deliberate here: the largest default graph
        # has only 684 vertices and we want an independent complete heat trace.
        vals = eigvalsh(normalized_laplacian_dense(A))
        last_eigenvalues = vals
        rows.append({
            "generation": g,
            "nodes": nodes,
            "diameter": diameter,
            "effective_volume_dimension": dH_step,
            "spectral_gap": float(vals[1]),
        })

    if last_eigenvalues is None:
        raise RuntimeError("no diamond graph generated")
    diamond_times = np.geomspace(0.5, 40.0, 160)
    heat = np.array([np.exp(-t * last_eigenvalues).mean() for t in diamond_times])
    ds = spectral_dimension(diamond_times, heat)
    ds_mean, ds_std = window_mean(diamond_times, ds, 6.0, 12.0)

    # The target is deliberately evaluated, not used in construction.
    final_dH = float(rows[-1]["effective_volume_dimension"])
    passes_4d = abs(final_dH - 4.0) < 0.25 and abs(ds_mean - 4.0) < 0.25

    return {
        "status": "null-model falsification harness",
        "controls": controls,
        "minimal_binary_diamond": {
            "rule": "one edge -> two alternative two-step paths -> reconvergence",
            "coordinates_used": False,
            "target_dimension_used_in_rule": False,
            "rows": rows,
            "spectral_dimension_mean_t6_t12": ds_mean,
            "spectral_dimension_std_t6_t12": ds_std,
            "passes_4d_gate": passes_4d,
            "conclusion": "minimal binary reconvergence tends to an approximately two-dimensional geometry, not four-dimensional geometry",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-generation", type=int, default=5)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_generation < 3 or args.max_generation > 5:
        parser.error("use 3 <= max-generation <= 5 (dense heat-trace control)")
    result = run(args.max_generation)
    text = json.dumps(result, ensure_ascii=False, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
