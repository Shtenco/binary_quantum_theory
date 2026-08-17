#!/usr/bin/env python3
"""Translate frozen microscopic gravity coefficients into physical observables.

This is a scale/prediction *translator*, not a fit and not evidence that the
input coefficients have already been derived.  The two theory inputs are

  lambda_R_eff : coefficient of sum_h Atilde_h delta_h in S_eff / hbar
  eta2         : leading dimensionless TT dispersion coefficient

with conventions

  lambda_R_eff = a_*^2 / (8 pi l_P^2)

  omega^2 = c^2 k^2 [1 + eta2 (k a_*)^2 + O((k a_*)^4)]

and the LVK modified-dispersion convention

  E^2 = p^2 c^2 + A_4 p^4 c^4 + ...

so

  A_4 = eta2 a_*^2 / (hbar c)^2.

The flat-space phase estimate is only a diagnostic.  A catalog comparison must
use the cosmological propagation integral of the selected LVK analysis.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from scipy.constants import G, c, hbar, electron_volt, parsec


def translate(lambda_r_eff: float, eta2: float, frequency_hz: float,
              distance_mpc: float) -> dict:
    if lambda_r_eff <= 0:
        raise ValueError("lambda_R_eff must be positive for a healthy positive Newton normalization")

    l_p = math.sqrt(hbar * G / c**3)
    e_p_joule = hbar * c / l_p
    e_p_ev = e_p_joule / electron_volt

    a_over_lp = math.sqrt(8.0 * math.pi * lambda_r_eff)
    a_m = a_over_lp * l_p

    # LVK A_4 in inverse energy squared.  a/(hbar c) has units 1/J.
    a4_joule_m2 = eta2 * (a_m / (hbar * c))**2
    a4_ev_m2 = a4_joule_m2 * electron_volt**2

    omega = 2.0 * math.pi * frequency_hz
    k = omega / c
    ka = k * a_m
    delta_v_over_c = 1.5 * eta2 * ka**2

    distance_m = distance_mpc * 1.0e6 * parsec
    flat_phase_shift = -0.5 * eta2 * distance_m * omega**3 * a_m**2 / c**3

    return {
        "status": "physical scale/prediction translation from frozen theory inputs",
        "inputs_are_theory_outputs_not_fit_parameters": True,
        "lambda_R_eff": lambda_r_eff,
        "eta2": eta2,
        "constants": {
            "Planck_length_m": l_p,
            "Planck_energy_eV": e_p_ev,
        },
        "scale": {
            "a_over_lP": a_over_lp,
            "a_star_m": a_m,
            "identity": "a_star/lP = sqrt(8*pi*lambda_R_eff)",
        },
        "LVK_modified_dispersion": {
            "alpha": 4,
            "A4_eV^-2": a4_ev_m2,
            "identity": "A4 = eta2*a_star^2/(hbar*c)^2 = 8*pi*eta2*lambda_R_eff/E_P^2",
        },
        "flat_space_diagnostic": {
            "frequency_Hz": frequency_hz,
            "distance_Mpc": distance_mpc,
            "k_a": ka,
            "delta_v_over_c_leading": delta_v_over_c,
            "phase_shift_rad_leading": flat_phase_shift,
            "warning": "Use the selected LVK cosmological propagation integral for real catalog inference.",
        },
        "scientific_scope": (
            "This script performs no parameter estimation.  Its output becomes a prediction only when "
            "lambda_R_eff and eta2 were independently derived from a frozen microscopic commit and "
            "preregistered before opening the external comparison posterior."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--lambda-r-eff", type=float, required=True)
    ap.add_argument("--eta2", type=float, required=True)
    ap.add_argument("--frequency-hz", type=float, default=100.0)
    ap.add_argument("--distance-mpc", type=float, default=1000.0)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    out = translate(args.lambda_r_eff, args.eta2, args.frequency_hz, args.distance_mpc)
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
