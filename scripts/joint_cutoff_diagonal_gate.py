#!/usr/bin/env python3
"""Canonical simultaneous-cutoff gate for the BCQG core candidate.

This gate does not claim a uniform Jmax->infinity theorem. It checks the
power-law diagonal family

    Jmax(epsilon) ~ epsilon^(-alpha)

against the frozen Lorentzian-route composition bounds

    C_cross / D = O(epsilon * Jmax^(13/2))
    C_GG    / D = O(epsilon^2 * Jmax^13).

For a power trajectory the sufficient condition is

    0 < alpha < 2/13.

The canonical candidate choice alpha=1/8 gives

    C_cross / D = O(epsilon^(3/16))
    C_GG    / D = O(epsilon^(3/8)).

The script verifies the analytic exponents and a half-integer-quantized
numerical staircase. Boundary and supercritical alpha values are included as
negative controls.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

ALPHA_CRIT = 2.0 / 13.0
ALPHA_CANON = 1.0 / 8.0


def exponents(alpha: float) -> tuple[float, float]:
    p_cross = 1.0 - 13.0 * alpha / 2.0
    p_gg = 2.0 - 13.0 * alpha
    return p_cross, p_gg


def half_integer_floor(x: float) -> float:
    return max(0.5, math.floor(2.0 * x) / 2.0)


def staircase(alpha: float, levels: int = 18):
    eps = np.array([2.0 ** (-n) for n in range(4, 4 + levels)], dtype=float)
    j = np.array([half_integer_floor(e ** (-alpha)) for e in eps], dtype=float)
    cross = eps * j ** (13.0 / 2.0)
    gg = eps ** 2 * j ** 13.0
    return eps, j, cross, gg


def log_slope(eps: np.ndarray, y: np.ndarray) -> float:
    # Quantization makes the staircase locally flat, so fit the full declared
    # window rather than finite-differencing adjacent points.
    x = np.log(eps)
    z = np.log(y)
    return float(np.polyfit(x, z, 1)[0])


def run(levels: int = 18) -> dict:
    pc, pg = exponents(ALPHA_CANON)
    eps, j, cross, gg = staircase(ALPHA_CANON, levels)
    slope_cross = log_slope(eps, cross)
    slope_gg = log_slope(eps, gg)

    p_boundary = exponents(ALPHA_CRIT)
    p_super = exponents(1.0 / 6.0)

    # Analytic statements are the theorem. The staircase slopes are only a
    # quantized finite-window regression and therefore get loose tolerances.
    checks = {
        "alpha_canonical_below_critical": ALPHA_CANON < ALPHA_CRIT,
        "canonical_cross_exponent_exact": abs(pc - 3.0 / 16.0) < 1e-15,
        "canonical_gg_exponent_exact": abs(pg - 3.0 / 8.0) < 1e-15,
        "canonical_both_positive": pc > 0.0 and pg > 0.0,
        "boundary_is_not_decaying": abs(p_boundary[0]) < 1e-15 and abs(p_boundary[1]) < 1e-15,
        "supercritical_fails": p_super[0] < 0.0 and p_super[1] < 0.0,
        "quantized_cross_decreases": bool(cross[-1] < cross[0]),
        "quantized_gg_decreases": bool(gg[-1] < gg[0]),
        "quantized_cross_slope_positive": slope_cross > 0.0,
        "quantized_gg_slope_positive": slope_gg > 0.0,
    }

    return {
        "status": "conditional_diagonal_certificate",
        "assumed_bounds": {
            "cross_over_D": "O(epsilon * Jmax^(13/2))",
            "geometry_geometry_over_D": "O(epsilon^2 * Jmax^13)",
        },
        "critical_alpha": ALPHA_CRIT,
        "canonical_alpha": ALPHA_CANON,
        "canonical_exponents": {
            "cross": pc,
            "geometry_geometry": pg,
        },
        "negative_controls": {
            "alpha_equal_2_over_13": {
                "cross_exponent": p_boundary[0],
                "geometry_geometry_exponent": p_boundary[1],
            },
            "alpha_1_over_6": {
                "cross_exponent": p_super[0],
                "geometry_geometry_exponent": p_super[1],
            },
        },
        "quantized_staircase": {
            "levels": levels,
            "epsilon_first": float(eps[0]),
            "epsilon_last": float(eps[-1]),
            "Jmax_first": float(j[0]),
            "Jmax_last": float(j[-1]),
            "cross_bound_first": float(cross[0]),
            "cross_bound_last": float(cross[-1]),
            "gg_bound_first": float(gg[0]),
            "gg_bound_last": float(gg[-1]),
            "fitted_cross_exponent": slope_cross,
            "fitted_gg_exponent": slope_gg,
        },
        "checks": checks,
        "passed": all(checks.values()),
        "scope": (
            "This establishes one explicit admissible simultaneous-cutoff path, "
            "conditional on the frozen polynomial norm-growth bounds. It is not "
            "a uniform theorem over arbitrary Jmax(epsilon) trajectories."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--levels", type=int, default=18)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    out = run(args.levels)
    text = json.dumps(out, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
