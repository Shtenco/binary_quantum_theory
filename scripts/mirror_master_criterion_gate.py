#!/usr/bin/env python3
"""Dimensionless master criterion for the healthy mirror-force branch.

Using the regular-seed Hodge normalization

    Z_sigma = (2 sqrt(2)/3) J/ell,

define natural dimensionless microscopic ratios

    g_*     = G J/ell,
    j_sigma = J ell/(hbar c_sigma),
    R       = r/ell,
    Delta_sigma = delta_sigma J.

Then

    alpha = 3 beta_m^2/(8 sqrt(2) pi g_*),
    x = m_sigma r = delta_sigma j_sigma R,

and opposite-chi repulsion requires

    beta_m^2 > (8 sqrt(2) pi/3) g_* exp(x)/(1+x).

This gate verifies equivalence of the original and reduced criteria and emits
range requirements. It does not supply the microscopic beta_m, g_* or j_sigma.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


C_HODGE = 2.0 * math.sqrt(2.0) / 3.0
C_BETA = 8.0 * math.sqrt(2.0) * math.pi / 3.0


def alpha_from_beta_gstar(beta_m, gstar):
    return 3.0 * beta_m * beta_m / (8.0 * math.sqrt(2.0) * math.pi * gstar)


def x_from_gap(delta_sigma, jsigma, R):
    return delta_sigma * jsigma * R


def beta_crit(gstar, x):
    return math.sqrt(C_BETA * gstar * math.exp(x) / (1.0 + x))


def original_force_ratio(alpha, x):
    return alpha * (1.0 + x) * math.exp(-x)


def run():
    # Deterministic equivalence controls over a broad parameter grid.
    cases = []
    max_equivalence_error = 0.0
    for gstar in (1e-6, 1e-3, 0.1, 1.0, 10.0):
        for beta in (0.01, 0.1, 0.5, 1.0, 3.0):
            for x in (0.0, 0.1, 0.5, 1.0, 2.0):
                alpha = alpha_from_beta_gstar(beta, gstar)
                ratio = original_force_ratio(alpha, x)
                bcrit = beta_crit(gstar, x)
                pass_original = ratio > 1.0
                pass_master = abs(beta) > bcrit
                err = 0.0 if pass_original == pass_master else 1.0
                max_equivalence_error = max(max_equivalence_error, err)
                cases.append({
                    "gstar": gstar,
                    "beta_m": beta,
                    "x": x,
                    "alpha": alpha,
                    "force_ratio": ratio,
                    "beta_crit": bcrit,
                    "repulsive": pass_original,
                })

    # Deep ordered finite-seed odd spectral gap from the symmetry-resolved gate.
    delta_deep = 7.9700878769645
    delta_soft_checked = 5.58410566853
    range_table = []
    for R in (1.0, 1e3, 1e6, 1e9, 1e12):
        range_table.append({
            "R_equals_r_over_ell": R,
            "jsigma_max_for_x_le_1_deep_seed": 1.0 / (delta_deep * R),
            "jsigma_max_for_x_le_1_softest_checked_seed": 1.0 / (delta_soft_checked * R),
        })

    # Algebraic dimensional reduction control from the Hodge Z_sigma.
    # Set ell=1 and J arbitrary: gstar=GJ/ell. The two alpha formulas must agree.
    max_alpha_reduction_error = 0.0
    for G, J, ell, beta in (
        (0.03, 2.0, 0.7, 0.4),
        (1.2, 0.5, 3.0, 1.1),
        (2e-4, 7.0, 0.02, 0.08),
    ):
        Z = C_HODGE * J / ell
        alpha_full = beta * beta / (4.0 * math.pi * G * Z)
        gstar = G * J / ell
        alpha_reduced = alpha_from_beta_gstar(beta, gstar)
        max_alpha_reduction_error = max(max_alpha_reduction_error, abs(alpha_full - alpha_reduced))

    passed = max_equivalence_error == 0.0 and max_alpha_reduction_error < 1e-12

    return {
        "status": "dimensionless mirror-force master criterion gate",
        "passed": bool(passed),
        "definitions": {
            "gstar": "G*J/ell",
            "jsigma": "J*ell/(hbar*c_sigma)",
            "R": "r/ell",
            "delta_sigma": "Delta_sigma/J",
            "x": "delta_sigma*jsigma*R",
        },
        "hodge_normalization": "Z_sigma=(2*sqrt(2)/3)*J/ell",
        "alpha_reduced": "alpha=3*beta_m^2/(8*sqrt(2)*pi*gstar)",
        "master_repulsion_criterion": (
            "beta_m^2 > (8*sqrt(2)*pi/3)*gstar*exp(x)/(1+x), "
            "x=delta_sigma*jsigma*R"
        ),
        "range_criterion": "x<=1 implies jsigma<=1/(delta_sigma*R)",
        "max_boolean_equivalence_error": max_equivalence_error,
        "max_alpha_reduction_error": max_alpha_reduction_error,
        "range_table": range_table,
        "sample_cases": cases[:15],
        "scope": (
            "This removes alpha as an independent phenomenological parameter once beta_m, gstar and the "
            "sigma gap/speed ratio are known. It does not derive those microscopic quantities."
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
