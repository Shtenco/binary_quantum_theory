#!/usr/bin/env python3
"""Check emergence of mass-independent free fall from sine kinematics."""

from __future__ import annotations

import argparse
import json
import math


HBAR = 1.054_571_817e-34


def lattice_acceleration(momentum: float, mass: float, spacing: float,
                         potential_gradient: float) -> float:
    if mass <= 0.0 or spacing <= 0.0:
        raise ValueError("mass and spacing must be positive")
    # H=(hbar^2/ma^2)[1-cos(pa/hbar)]+m Phi.
    return -math.cos(momentum * spacing / HBAR) * potential_gradient


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ka", type=float, default=0.1,
                        help="dimensionless momentum p*a/hbar")
    parser.add_argument("--gradient", type=float, default=9.81,
                        help="potential gradient in m/s^2")
    args = parser.parse_args()
    if not math.isfinite(args.ka) or not math.isfinite(args.gradient):
        parser.error("arguments must be finite")
    spacing = 1e-35
    masses = (9.109_383_7139e-31, 1.672_621_925_95e-27)
    accelerations = [
        lattice_acceleration(args.ka * HBAR / spacing, mass, spacing, args.gradient)
        for mass in masses
    ]
    continuum = -args.gradient
    expected = -math.cos(args.ka) * args.gradient
    result = {
        "dimensionless_ka": args.ka,
        "accelerations_m_per_s2": accelerations,
        "mass_independence_error": abs(accelerations[0] - accelerations[1]),
        "exact_sine_acceleration": expected,
        "continuum_acceleration": continuum,
        "relative_lattice_correction": abs(expected / continuum - 1.0)
        if continuum else 0.0,
        "mass_cancels_at_fixed_ka": accelerations[0] == accelerations[1],
        "interpretation": "WEP is recovered as ka -> 0; fixed ka is not fixed velocity",
    }
    print(json.dumps(result, indent=2))
    return 0 if result["mass_independence_error"] < 1e-14 else 1


if __name__ == "__main__":
    raise SystemExit(main())
