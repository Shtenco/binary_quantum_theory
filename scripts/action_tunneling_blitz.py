#!/usr/bin/env python3
"""Dependency-free dimensional and WKB checks for the proposed action."""

from __future__ import annotations

import argparse
import json
import math


HBAR = 1.054_571_817e-34  # J s
C = 299_792_458.0  # m/s
G = 6.674_30e-11  # m^3 kg^-1 s^-2
EV = 1.602_176_634e-19  # J
PROTON_MASS = 1.672_621_925_95e-27  # kg


def calculate(delta_t: float, width: float, barrier_ev: float,
              energy_ev: float, mass: float) -> dict[str, float | bool]:
    if delta_t < 0 or width <= 0 or mass <= 0 or barrier_ev <= energy_ev:
        raise ValueError("require delta_t >= 0, width/mass > 0 and barrier > energy")
    planck_length = math.sqrt(HBAR * G / C ** 3)
    planck_time = planck_length / C
    foam_coefficient = HBAR / planck_length ** 2
    gravity_coefficient = C ** 3 / G
    wkb_exponent = (2.0 * width / HBAR) * math.sqrt(
        2.0 * mass * (barrier_ev - energy_ev) * EV
    )
    transmission = math.exp(-wkb_exponent)
    phase_radians = delta_t / planck_time
    return {
        "planck_length_m": planck_length,
        "planck_time_s": planck_time,
        "hbar_over_lp_squared": foam_coefficient,
        "c_cubed_over_G": gravity_coefficient,
        "coefficient_relative_error": abs(foam_coefficient / gravity_coefficient - 1.0),
        "wkb_exponent": wkb_exponent,
        "wkb_transmission_probability": transmission,
        "phase_radians": phase_radians,
        "phase_cycles": phase_radians / (2.0 * math.pi),
        "phase_factor_modulus_squared": 1.0,
        "tunneling_probability_after_pure_phase": transmission,
        "pure_phase_enhances_tunneling": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--delta-t", type=float, default=1e-15, help="time fluctuation, s")
    parser.add_argument("--width", type=float, default=5e-15, help="barrier width, m")
    parser.add_argument("--barrier-ev", type=float, default=100e3)
    parser.add_argument("--energy-ev", type=float, default=10e3)
    parser.add_argument("--mass", type=float, default=PROTON_MASS, help="particle mass, kg")
    args = parser.parse_args()
    try:
        result = calculate(args.delta_t, args.width, args.barrier_ev,
                           args.energy_ev, args.mass)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
