#!/usr/bin/env python3
"""Exact q=2 causal-volume dimension-three fixed-point gate.

This gate uses only the already-derived local selector q=2 and the frozen route
rewrite used by the geometrogenesis harness:

  * B = 2^q route midpoints per active causal edge;
  * every active edge becomes 2B active child edges;
  * causal depth/length doubles per generation.

The number of vertices after g generations is therefore exactly

    N_g = 2 + B * ((2B)^g - 1)/(2B - 1).

Define the one-step causal-volume exponent

    d_g = log_2(N_g/N_{g-1}).

For q=2, B=4 and N_g=(4*8^g+10)/7.  Hence d_g increases monotonically
to log_2(8)=3.  This is an exact asymptotic statement about the frozen causal
volume scaling.  It is not by itself a theorem about spectral dimension of an
arbitrary graph metric; the independent PL-link and spectral gates remain
separate cross-checks.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def n_vertices(g: int, q: int) -> int:
    B = 1 << q
    return 2 + B * (((2 * B) ** g - 1) // (2 * B - 1))


def step_dimension(g: int, q: int) -> float:
    return math.log(n_vertices(g, q) / n_vertices(g - 1, q), 2.0)


def run(q: int = 2, max_generation: int = 10):
    if q != 2:
        raise ValueError("canonical gate is frozen to independently derived q=2")
    if max_generation < 3:
        raise ValueError("max_generation must be >=3")

    B = 1 << q
    d_star = math.log(2 * B, 2.0)
    rows = []
    ds = []
    for g in range(2, max_generation + 1):
        d = step_dimension(g, q)
        ds.append(d)
        rows.append({
            "generation": g,
            "vertices": n_vertices(g, q),
            "causal_length_scale": 2 ** g,
            "step_dimension": d,
            "defect_to_three": 3.0 - d,
        })

    monotone = all(ds[i + 1] > ds[i] for i in range(len(ds) - 1))
    below = all(d < 3.0 for d in ds)

    # Exact q=2 formula:
    # d_g = 3 + log2(1 - 35/(16*8^(g-1)+40)).
    closed_form_residual = 0.0
    for row in rows:
        g = row["generation"]
        d_cf = 3.0 + math.log(1.0 - 35.0 / (16.0 * (8.0 ** (g - 1)) + 40.0), 2.0)
        closed_form_residual = max(closed_form_residual, abs(d_cf - row["step_dimension"]))

    passed = (
        abs(d_star - 3.0) < 1e-15
        and monotone
        and below
        and closed_form_residual < 1e-14
        and rows[-1]["defect_to_three"] < 3e-8
    )

    return {
        "status": "exact q=2 causal-volume dimension-three fixed-point closure",
        "passed": passed,
        "q": q,
        "routes_B": B,
        "active_edge_growth_per_generation": 2 * B,
        "causal_length_growth_per_generation": 2,
        "exact_fixed_point_dimension": d_star,
        "exact_vertex_count_formula": "N_g = 2 + B*((2B)^g-1)/(2B-1); for q=2: N_g=(4*8^g+10)/7",
        "exact_step_formula_q2": "d_g = 3 + log2(1 - 35/(16*8^(g-1)+40))",
        "rows": rows,
        "checks": {
            "monotone_increase_to_three": monotone,
            "all_finite_steps_below_three": below,
            "closed_form_residual": closed_form_residual,
        },
        "scope": (
            "Exact causal-volume scaling for the frozen q=2 route rewrite. "
            "Topological dimension is independently fixed by the S2-link/S3 PL-manifold gate; "
            "spectral dimension and z are independent numerical cross-checks."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-generation", type=int, default=10)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    out = run(max_generation=args.max_generation)
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
