#!/usr/bin/env python3
"""Show that the additive growth/composition law fixes phase linearity but not slope."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def run(M: int = 8) -> dict:
    if M < 2:
        raise ValueError("M must be >=2")
    values = [n for n in range(-M, M + 1) if n != 0]
    vi = {n: i for i, n in enumerate(values)}
    rows = []
    for n in range(-M, M + 1):
        for m in range(-M, M + 1):
            r = n + m
            if r < -M or r > M:
                continue
            row = np.zeros(len(values))
            if r != 0:
                row[vi[r]] += 1
            if n != 0:
                row[vi[n]] -= 1
            if m != 0:
                row[vi[m]] -= 1
            if np.linalg.norm(row) > 0:
                rows.append(row)
    A = np.vstack(rows)
    _, s, vh = np.linalg.svd(A, full_matrices=False)
    rank = int(np.sum(s > 1e-11))
    null_dim = len(values) - rank
    null = vh[-1]
    linear = np.asarray(values, float)
    linear /= np.linalg.norm(linear)
    alignment = float(abs(null @ linear))

    slopes = [0.1, 0.5, 1.0, math.sqrt(2.0), math.pi]
    residuals = {}
    for slope in slopes:
        f = slope * np.asarray(values, float)
        residuals[str(slope)] = float(np.linalg.norm(A @ f))

    passed = null_dim == 1 and alignment > 1 - 1e-12 and max(residuals.values()) < 1e-12
    return {
        "status": "exact finite additive-phase normalization no-go",
        "passed": passed,
        "M": M,
        "equation_matrix_shape": list(A.shape),
        "rank": rank,
        "null_dimension": null_dim,
        "linear_null_alignment": alignment,
        "tested_arbitrary_slope_residuals": residuals,
        "derived_statement": "composition fixes f(n)=s*n but leaves one arbitrary real slope s",
        "physical_implication": (
            "The growth/composition axiom alone cannot determine the absolute microscopic "
            "action/phase normalization and therefore cannot by itself determine lambda_R_eff."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--M", type=int, default=8)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    out = run(args.M)
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
