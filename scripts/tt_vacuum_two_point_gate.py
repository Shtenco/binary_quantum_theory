#!/usr/bin/env python3
"""Reduced TT vacuum two-point function and smoothing-spectrum falsifier.

For the exact reduced Euclidean lattice kernel corresponding to the frozen
causal TT transfer,

    K_E(omega,k)=4 sin^2(omega/2)+Omega_k^2,
    Omega_k^2=r^2 sum_i 4 sin^2(k_i/2),

integrating over the Brillouin-zone frequency gives the exact equal-time
Gaussian covariance

    C(k)=int_{-pi}^{pi} d omega/(2 pi) 1/[Z K_E]
        =1/[Z Omega_k sqrt(Omega_k^2+4)].

Hence C(k) ~ 1/(2 Z r |k|) in the infrared.  This is a direct negative
control on identifying the repository's b^-2 observer smoothing defect with a
massless graviton vacuum RMS law.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def omega_sq(kvec: np.ndarray, r: float) -> float:
    return float(r * r * np.sum((2.0 * np.sin(0.5 * kvec)) ** 2))


def equal_time_covariance(kvec: np.ndarray, r: float, Z: float = 1.0) -> float:
    om2 = omega_sq(kvec, r)
    om = math.sqrt(om2)
    if om == 0.0:
        return math.inf
    return 1.0 / (Z * om * math.sqrt(om2 + 4.0))


def numerical_frequency_integral(kvec: np.ndarray, r: float, Z: float = 1.0,
                                 n: int = 200000) -> float:
    # Midpoint periodic rule is exponentially accurate for nonzero mass/gap.
    w = -math.pi + (np.arange(n) + 0.5) * (2.0 * math.pi / n)
    den = 4.0 * np.sin(0.5 * w) ** 2 + omega_sq(kvec, r)
    return float(np.mean(1.0 / (Z * den)))


def run(r: float = 1.0 / math.sqrt(3.0)) -> dict:
    direction = np.array([1.0, 2.0, 3.0])
    direction /= np.linalg.norm(direction)

    qs = np.geomspace(2e-4, 5e-2, 80)
    cov = np.array([equal_time_covariance(q * direction, r) for q in qs])
    slope = float(np.polyfit(np.log(qs[:50]), np.log(cov[:50]), 1)[0])

    # Independent exact-vs-frequency-integration checks away from the singular zero mode.
    checks = []
    max_rel = 0.0
    for q in (0.03, 0.08, 0.2, 0.5):
        kv = q * direction
        exact = equal_time_covariance(kv, r)
        numeric = numerical_frequency_integral(kv, r, n=40000)
        rel = abs(numeric - exact) / exact
        max_rel = max(max_rel, rel)
        checks.append({"q": q, "exact": exact, "numeric": numeric, "relative_error": rel})

    # In 3 spatial dimensions, if P(k)~k^n then the variance of a large smooth
    # block average scales R^{-(3+n)}, so RMS scales R^{-(3+n)/2}.
    n_tt = -1.0
    rms_exponent_3d = (3.0 + n_tt) / 2.0

    # Existing smoothing-defect exponent p_smooth=2.001707 would imply n=2p-3
    # only if it were itself a stationary 3D quantum RMS law.
    p_smooth = 2.001707
    n_from_smoothing_assumption = 2.0 * p_smooth - 3.0

    passed = abs(slope + 1.0) < 2e-4 and max_rel < 2e-8
    return {
        "status": "reduced TT Gaussian vacuum two-point negative control",
        "passed": bool(passed),
        "r": r,
        "exact_equal_time_covariance": (
            "C(k)=1/[Z*Omega_k*sqrt(Omega_k^2+4)], "
            "Omega_k^2=r^2 sum_i 4 sin^2(k_i/2)"
        ),
        "infrared": {
            "analytic_power_spectrum_exponent_n": n_tt,
            "numerical_loglog_slope": slope,
            "C_asymptotic": "1/(2 Z r |k|)",
            "3d_block_RMS_exponent": rms_exponent_3d,
        },
        "frequency_integral_checks": checks,
        "max_exact_vs_numeric_relative_error": max_rel,
        "smoothing_comparison": {
            "observer_smoothing_defect_RMS_exponent": p_smooth,
            "conditional_n_if_misidentified_as_3d_quantum_RMS": n_from_smoothing_assumption,
            "actual_reduced_TT_vacuum_n": n_tt,
            "actual_reduced_TT_vacuum_block_RMS_exponent": rms_exponent_3d,
            "conclusion": (
                "The b^-2.001707 observer smoothing defect is not the Gaussian massless TT vacuum RMS "
                "of the explicit reduced propagator. Promoting it directly to P_foam(k)~k^1.003414 is rejected "
                "by this negative control unless the full interacting/history/RG vacuum changes the IR universality class."
            ),
        },
        "scientific_scope": (
            "Exact for the Gaussian vacuum associated with the reduced free TT lattice kernel. "
            "The full Peter-Weyl/history vacuum remains to be computed and may differ."
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
