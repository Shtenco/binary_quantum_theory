#!/usr/bin/env python3
"""Mirror-force normalization and source-selection gate.

This gate narrows the healthy mirror-force branch after the 16-cell staggered
order parameter Sigma has been derived.

For a dimensionless coarse pseudoscalar sigma with continuum kinetic term

    L_sigma = Z_sigma/2 * (partial sigma)^2 - ...

and a point-particle/source coupling

    L_int = - beta_m * m * chi * sigma,

the canonically normalized field phi_c=sqrt(Z_sigma)*sigma has source charge

g_m = beta_m*m/sqrt(Z_sigma).

Tree-level exchange gives

    V_sigma(r) = - beta_1 beta_2 m1 m2 chi1 chi2
                 exp(-m_sigma r)/(4*pi*Z_sigma*r).

Compared with tensor gravity V_G=-G*m1*m2/r, the long-range strength is

    alpha = beta_m^2/(4*pi*G*Z_sigma)

for equal source normalizations.

The already-derived pure orientation defect is mirror symmetric: its energy is
8J in either Sigma=+1 or Sigma=-1 vacuum. Therefore it has zero linear mirror
source coefficient in the minimal geometry-only model. A nonzero beta_m must
come from an additional matter-sensitive operator, e.g. the candidate axial
coupling Y_L J5^0, rather than from positive rest energy alone.

No SI prediction is made because G*Z_sigma and the matter coupling beta_m are
not yet fixed by the microscopic theory.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def alpha_from(beta_m: float, GZ: float) -> float:
    return beta_m * beta_m / (4.0 * math.pi * GZ)


def beta_required(alpha: float, GZ: float) -> float:
    return math.sqrt(4.0 * math.pi * GZ * alpha)


def run():
    # Exact geometry-only source-selection control from the 16-cell gate.
    E_defect_plus_over_J = 8.0
    E_defect_minus_over_J = 8.0
    odd_energy_split_over_J = 0.5 * (E_defect_plus_over_J - E_defect_minus_over_J)
    beta_geometry_only = odd_energy_split_over_J / max(
        0.5 * (E_defect_plus_over_J + E_defect_minus_over_J), 1e-30
    )

    # Dimensionless normalization controls. GZ is deliberately arbitrary here;
    # these rows verify only the algebraic mapping and threshold inversion.
    GZ_control = 1.0 / (4.0 * math.pi)
    alpha_rows = []
    for beta in (0.0, 0.5, 1.0, 2.0):
        a = alpha_from(beta, GZ_control)
        b_back = beta_required(a, GZ_control)
        alpha_rows.append({
            "beta_m": beta,
            "G_times_Zsigma": GZ_control,
            "alpha": a,
            "beta_roundtrip": b_back,
            "roundtrip_error": abs(beta - b_back),
        })

    # Yukawa screening thresholds already used by the force gate, now mapped to
    # the beta_m required once G*Z_sigma is known.
    threshold_rows = []
    for x in (0.0, 0.1, 0.5, 1.0, 2.0):
        alpha_crit = math.exp(x) / (1.0 + x)
        threshold_rows.append({
            "x_m_sigma_r": x,
            "alpha_crit": alpha_crit,
            "beta_crit_at_control_GZ": beta_required(alpha_crit, GZ_control),
        })

    # Candidate axial source: beta_m = lambda_5 * (Q5/m). This is symbolic; the
    # finite gate simply records the source selection rule and a normalized toy
    # consistency point, not a physical value of lambda_5 or Q5.
    lambda5 = 0.3
    q5_over_m = 0.4
    beta_axial_demo = lambda5 * q5_over_m
    alpha_axial_demo = alpha_from(beta_axial_demo, GZ_control)

    passed = (
        abs(odd_energy_split_over_J) < 1e-15
        and abs(beta_geometry_only) < 1e-15
        and max(r["roundtrip_error"] for r in alpha_rows) < 1e-15
        and abs(alpha_from(1.0, GZ_control) - 1.0) < 1e-15
    )

    return {
        "status": "mirror-force normalization and source-selection gate",
        "passed": bool(passed),
        "exact_strength_formula": "alpha=beta_m^2/(4*pi*G*Z_sigma)",
        "canonical_field": "phi_c=sqrt(Z_sigma)*sigma",
        "source_charge": "g_m=beta_m*m*chi/sqrt(Z_sigma)",
        "geometry_only_defect": {
            "E_defect_in_Sigma_plus_over_J": E_defect_plus_over_J,
            "E_defect_in_Sigma_minus_over_J": E_defect_minus_over_J,
            "mirror_odd_energy_split_over_J": odd_energy_split_over_J,
            "beta_geometry_only": beta_geometry_only,
            "conclusion": "The minimal pure geometry defect has no linear mirror charge."
        },
        "normalization_controls": alpha_rows,
        "screening_threshold_mapping": threshold_rows,
        "candidate_matter_source": {
            "operator": "lambda_5 * sigma * J5^0",
            "beta_m": "lambda_5 * (Q5/m)",
            "demo_lambda5": lambda5,
            "demo_Q5_over_m": q5_over_m,
            "demo_beta_m": beta_axial_demo,
            "demo_alpha_at_control_GZ": alpha_axial_demo,
            "scope": "Algebraic normalization example only; not a physical parameter fit."
        },
        "scale_bottleneck": (
            "A first-principles alpha needs both the continuum stiffness Z_sigma of the derived staggered mode "
            "and a microscopic matter coupling beta_m. HDA closure fixes the constraint structure but not this "
            "overall physical normalization or Newton scale."
        ),
        "falsifier": (
            "If all allowed microscopic matter operators give beta_m=0, the derived mirror order cannot mediate "
            "a composition-dependent fifth force even though Sigma itself exists."
        )
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
