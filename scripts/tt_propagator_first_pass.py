#!/usr/bin/env python3
"""First physicalization pass: exact reduced TT transfer propagator and quartic pole.

This script uses the frozen symplectic causal TT transfer already present in
bcqg_unified_verification.py:

    khat^2 = sum_i [2 sin(k_i/2)]^2
    lambda = r^2 khat^2
    cos(omega) = 1 - lambda/2

equivalently

    4 sin^2(omega/2) = r^2 sum_i 4 sin^2(k_i/2).

The resulting free two-polarization connected propagator is fixed up to the
overall wave-function/action normalization Z_T:

    G_AB(omega,k) = delta_AB / [ Z_T K(omega,k) ]

    K = 4 sin^2(omega/2) - r^2 sum_i 4 sin^2(k_i/2) + i0.

The script extracts the O(k^4) pole correction.  It deliberately distinguishes
the rotational scalar projection from the cubic-lattice anisotropy.  Therefore
the isotropic coefficient reported here is a *bare reduced-transfer* coefficient,
not yet the physical eta_2 of the full Peter-Weyl/history/RG theory.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def unit(v):
    x = np.asarray(v, dtype=float)
    n = float(np.linalg.norm(x))
    if n <= 0:
        raise ValueError("direction must be nonzero")
    return x / n


def pole_omega(q: float, n: np.ndarray, r2: float) -> float:
    kh2 = float(np.sum((2.0 * np.sin(0.5 * q * n)) ** 2))
    arg = 0.5 * math.sqrt(max(0.0, r2 * kh2))
    if arg > 1.0:
        raise ValueError("outside stable transfer band")
    return 2.0 * math.asin(arg)


def eta_direction(n: np.ndarray, r2: float) -> float:
    """omega^2 = r^2 q^2 [1 + eta(n) q^2 + O(q^4)]."""
    return float((r2 - np.sum(n**4)) / 12.0)


def numerical_eta(n: np.ndarray, r2: float) -> float:
    qs = np.geomspace(1e-4, 8e-2, 80)
    ys = np.array([
        pole_omega(float(q), n, r2) ** 2 / (r2 * q * q) - 1.0
        for q in qs
    ])
    X = np.column_stack([qs**2, qs**4])
    return float(np.linalg.lstsq(X, ys, rcond=None)[0][0])


def run(r: float = 1.0 / math.sqrt(3.0)) -> dict:
    if not (0.0 < r <= 1.0):
        raise ValueError("require 0 < r <= 1")
    r2 = r * r

    dirs = {
        "axial": unit([1, 0, 0]),
        "face_diagonal": unit([1, 1, 0]),
        "body_diagonal": unit([1, 1, 1]),
        "generic_123": unit([1, 2, 3]),
    }

    directional = {}
    max_fit_err = 0.0
    for name, n in dirs.items():
        analytic = eta_direction(n, r2)
        fitted = numerical_eta(n, r2)
        max_fit_err = max(max_fit_err, abs(analytic - fitted))
        directional[name] = {
            "direction": n.tolist(),
            "sum_n_i^4": float(np.sum(n**4)),
            "eta4_directional_analytic": analytic,
            "eta4_directional_numeric_fit": fitted,
            "absolute_fit_error": abs(analytic - fitted),
        }

    # In 3 spatial dimensions <sum_i n_i^4>_S2 = 3/5.
    eta_iso = (r2 - 3.0 / 5.0) / 12.0
    zeta_cubic = -1.0 / 12.0

    # Quartic pole:
    # omega^2 = r^2 k^2
    # + r^2[(r^2-3/5) k^4/12 - Q4_cubic/12] + O(k^6),
    # Q4_cubic = sum_i k_i^4 - (3/5)(k^2)^2.
    passed = max_fit_err < 2e-8

    return {
        "status": "exact reduced causal-TT free propagator first pass",
        "passed": passed,
        "frozen_source_relation": {
            "r": r,
            "r_squared": r2,
            "kernel": "K=4 sin^2(omega/2)-r^2 sum_i 4 sin^2(k_i/2)",
            "propagator": "G_TT_AB=delta_AB/[Z_T*(K+i0)]",
            "two_polarizations": True,
            "overall_Z_T_fixed_here": False,
        },
        "small_momentum_pole": {
            "formula": (
                "omega^2=r^2 k^2 + r^2[(r^2-3/5)k^4/12 "
                "-(sum_i k_i^4-(3/5)(k^2)^2)/12] + O(k^6)"
            ),
            "bare_isotropic_eta2": eta_iso,
            "bare_cubic_anisotropy_zeta4": zeta_cubic,
            "A4_times_Ep2_per_lambda_if_scalar_survives_RG": 8.0 * math.pi * eta_iso,
            "definition": (
                "omega^2=r^2 k^2[1+eta2_iso k^2] "
                "+r^2*zeta4*(sum_i k_i^4-3(k^2)^2/5)+O(k^6)"
            ),
        },
        "directional_checks": directional,
        "max_analytic_numeric_eta_error": max_fit_err,
        "lambda_R_eff_status": (
            "NOT determined by this transfer. The repository growth-composition "
            "axiom fixes phase linearity but leaves one overall slope/action normalization."
        ),
        "physical_eta2_status": (
            "NOT YET. eta2_iso above is the bare reduced-transfer scalar projection. "
            "The full physical eta2 requires the same frozen Peter-Weyl/history measure, "
            "constrained TT observable map and RG/blocking used to derive lambda_R_eff; "
            "the cubic anisotropy must also be shown to flow away or retained as a separate prediction."
        ),
        "next_gate": (
            "Construct G_TT from the full constrained microscopic/effective Hessian or history "
            "two-point function, fit simultaneously the isotropic k^4 invariant and cubic "
            "anisotropy, and derive/fix the remaining overall action slope."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--r", type=float, default=1.0 / math.sqrt(3.0))
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    out = run(args.r)
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
