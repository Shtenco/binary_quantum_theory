#!/usr/bin/env python3
"""Longitudinal mirror source in the conditional Heisenberg/Goldstone branch.

If the Bell-gluing pseudospin O(3) survives in the IR and a Neel vacuum aligns
with the physical mirror orientation axis Y, write

  N = (pi_x, sqrt(v^2-pi_x^2-pi_z^2), pi_z).

Then the physical mirror scalar Sigma_Y=N_y has no term linear in the two
Goldstone fields. Therefore a static source -Q Sigma_Y has no one-Goldstone
exchange. The leading massless channel is two-Goldstone exchange.

For canonically normalized free massless Goldstones in 3+1 Euclidean spacetime,

  D(tau,r)=1/[4 pi^2 (tau^2+r^2)].

With N_G=2 and H_int=-Q N_y, the quadratic vertex is

  + Q/(2v) (pi_x^2+pi_z^2).

The connected static two-Goldstone potential is

  V_2G(r) = - Q1 Q2 / [32 pi^3 v^2 r^3]

at leading free-Goldstone order. Same charges attract; opposite charges repel.
The force falls as r^-4, so this is not the 1/r potential needed to track
Newtonian gravity at arbitrarily long distance.

This is a conditional low-energy EFT control, not evidence that the accidental
pseudospin symmetry survives the full gravity dynamics.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad


def ny_exact(pi2, v):
    return math.sqrt(max(v * v - pi2, 0.0))


def propagator(tau, r):
    return 1.0 / (4.0 * math.pi**2 * (tau * tau + r * r))


def analytic_D2_integral(r):
    return 1.0 / (32.0 * math.pi**3 * r**3)


def numerical_D2_integral(r):
    val, err = quad(lambda t: propagator(t, r) ** 2, -np.inf, np.inf, epsabs=1e-13, epsrel=1e-12)
    return val, err


def potential(Q1, Q2, v, r, NG=2):
    c1 = Q1 / (2.0 * v)
    c2 = Q2 / (2.0 * v)
    return -c1 * c2 * (2.0 * NG) * analytic_D2_integral(r)


def run():
    v = 1.7
    # Finite-difference derivatives of N_y(pi_x,pi_z) at the vacuum.
    h = 1e-5
    f0 = ny_exact(0.0, v)
    fxp = ny_exact(h * h, v)
    fxm = ny_exact(h * h, v)
    first_x = (fxp - fxm) / (2.0 * h)
    second_x = (fxp - 2.0 * f0 + fxm) / (h * h)
    target_second = -1.0 / v

    integral_rows = []
    max_integral_rel = 0.0
    for r in (0.3, 0.7, 1.0, 2.0, 5.0):
        num, err = numerical_D2_integral(r)
        ana = analytic_D2_integral(r)
        rel = abs(num - ana) / ana
        max_integral_rel = max(max_integral_rel, rel)
        integral_rows.append({"r": r, "numeric": num, "analytic": ana, "relative_error": rel})

    Q = 0.8
    r = 1.3
    same = potential(+Q, +Q, v, r)
    opposite = potential(+Q, -Q, v, r)
    coefficient = 1.0 / (32.0 * math.pi**3)

    # Check r^-3 potential and r^-4 force scaling algebraically.
    V1 = abs(potential(Q, -Q, v, 1.0))
    V2 = abs(potential(Q, -Q, v, 2.0))
    potential_ratio = V1 / V2
    force_ratio_expected = 2.0**4

    passed = (
        abs(first_x) < 1e-14
        and abs(second_x - target_second) < 1e-5
        and max_integral_rel < 2e-10
        and same < 0.0
        and opposite > 0.0
        and abs(opposite + same) < 1e-15
        and abs(potential_ratio - 8.0) < 1e-12
    )

    return {
        "status": "conditional longitudinal mirror Goldstone-source gate",
        "passed": bool(passed),
        "vacuum_parameterization": "N=(pi_x,sqrt(v^2-pi_x^2-pi_z^2),pi_z)",
        "Sigma_Y_expansion": "v-(pi_x^2+pi_z^2)/(2v)+O(pi^4)",
        "one_Goldstone_vertex": 0.0,
        "finite_difference_first_derivative": first_x,
        "finite_difference_second_derivative": second_x,
        "target_second_derivative": target_second,
        "massless_Euclidean_propagator": "D(tau,r)=1/[4*pi^2*(tau^2+r^2)]",
        "D_squared_static_integral": "1/(32*pi^3*r^3)",
        "integral_controls": integral_rows,
        "max_integral_relative_error": max_integral_rel,
        "NG": 2,
        "two_Goldstone_potential": "V_2G=-Q1*Q2/(32*pi^3*v^2*r^3)",
        "dimensionless_coefficient_1_over_32pi3": coefficient,
        "sample_same_charge_potential": same,
        "sample_opposite_charge_potential": opposite,
        "V_r1_over_V_r2_for_r2_equal_2r1": potential_ratio,
        "force_scaling": "F_2G proportional r^-4",
        "force_ratio_F_r1_over_F_2r1": force_ratio_expected,
        "main_result": (
            "A longitudinal mirror source aligned with the Neel vacuum has no one-Goldstone coupling. Exact "
            "Heisenberg/Goldstone symmetry would therefore yield a leading two-Goldstone power-law interaction, "
            "not the previous one-particle 1/r Yukawa potential. Opposite charges repel in this leading free-EFT "
            "control, but the force falls as r^-4."
        ),
        "one_particle_requirement": (
            "A Newton-like long-range 1/r potential still requires a light mirror-odd one-particle pole or a "
            "microscopic source that couples linearly to a transverse Goldstone direction."
        ),
        "scope": (
            "Conditional O(3) nonlinear-sigma-model EFT with canonical free Goldstones. Interactions, velocity, "
            "wavefunction normalization and the survival of the pseudospin symmetry must be derived separately."
        ),
    }


def main():
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
