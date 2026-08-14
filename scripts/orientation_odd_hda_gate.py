#!/usr/bin/env python3
"""Orientation-odd gravity construction gate.

This gate tests three candidate ways to turn the project orientation bit chi=+/-1
into a gravitationally relevant sector without confusing mirror orientation with
negative energy.

1. Pure Hamiltonian sign/rescaling:
      H_chi[N] = s_chi H_GR[N].
   HDA gives {H_chi[N],H_chi[M]} = s_chi^2 D[beta].
   With the same D and lapse normalization, closure requires s_chi^2=1.
   s=-1 is only reversal of normal/time orientation (N->-N), not antigravity.

2. Metric sign flip:
   A negative coefficient in front of the Einstein-Hilbert kinetic term would
   make an effective Newton coupling negative, but also flips the graviton
   kinetic sign. This is a ghost/stability failure rather than a healthy
   antigravity branch.

3. Healthy mirror-odd matter mediator:
   Introduce two pseudoscalar canonical fields, sigma (orientation order
   parameter) and phi (mediator), with positive kinetic terms and a bounded
   mirror-even potential
       U = 1/2 mu^2 phi^2 + lambda/4 phi^4
           + g phi sigma + kappa/4 (sigma^2-v^2)^2.
   Mirror acts as (phi,sigma)->(-phi,-sigma). The local potential terms cancel
   from the H-H bracket, leaving the standard diffeomorphism generator.

A coarse object can carry orientation charge Q_chi = eta m chi. Exchange of a
canonical scalar/pseudoscalar mediator then gives a Yukawa force. Opposite
orientation charges repel without negative kinetic energy:
    U12 = -G_T m1 m2/r
          - alpha G_T m1 m2 chi1 chi2 exp(-m_phi r)/r.
The opposite-chi branch is repulsive relative to tensor gravity when
    alpha (1+x) exp(-x) > 1,  x=m_phi r.

This is an antigravity-like fifth-force construction, not yet a reversal of the
metric g00 itself and not yet embedded into the microscopic Peter-Weyl HDA.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def spectral_derivative(f: np.ndarray) -> np.ndarray:
    L = len(f)
    k = np.fft.fftfreq(L, d=1.0 / L)
    return np.fft.ifft(1j * k * np.fft.fft(f)).real


def field(x: np.ndarray, terms):
    out = np.zeros_like(x, dtype=float)
    for k, a, b in terms:
        out += a * np.sin(k * x) + b * np.cos(k * x)
    return out


def scalar_hda_gate(L: int = 512):
    x = 2 * np.pi * np.arange(L) / L
    phi = field(x, [(1, .20, .10), (2, -.10, .05), (3, .04, .02)])
    pphi = field(x, [(1, .15, -.07), (2, .03, .04)])
    sigma = .80 + field(x, [(1, .12, -.03), (2, .04, .02)])
    psigma = field(x, [(1, -.06, .09), (3, .025, -.01)])
    N = 1.0 + field(x, [(1, .04, .02), (2, .01, -.01)])
    M = .9 + field(x, [(1, -.03, .05), (3, .01, .02)])

    mu, lam, g, kappa, v = .7, .2, .25, .4, .9
    dphi = spectral_derivative(phi)
    dsigma = spectral_derivative(sigma)
    dN = spectral_derivative(N)
    dM = spectral_derivative(M)

    U_phi = mu * mu * phi + lam * phi**3 + g * sigma
    U_sigma = g * phi + kappa * sigma * (sigma**2 - v**2)

    dHN_phi = -spectral_derivative(N * dphi) + N * U_phi
    dHM_phi = -spectral_derivative(M * dphi) + M * U_phi
    dHN_sigma = -spectral_derivative(N * dsigma) + N * U_sigma
    dHM_sigma = -spectral_derivative(M * dsigma) + M * U_sigma

    dx = 2 * np.pi / L
    bracket = np.sum(
        dHN_phi * (M * pphi) - (N * pphi) * dHM_phi
        + dHN_sigma * (M * psigma) - (N * psigma) * dHM_sigma
    ) * dx
    beta = N * dM - M * dN
    D = np.sum(beta * (pphi * dphi + psigma * dsigma)) * dx
    abs_error = float(abs(bracket - D))
    rel_error = abs_error / max(abs(float(D)), 1e-30)

    return {
        "L": L,
        "bracket": float(bracket),
        "D_target": float(D),
        "absolute_error": abs_error,
        "relative_error": float(rel_error),
        "passed": bool(rel_error < 1e-10),
        "identity": "{H_matter[N],H_matter[M]} = D_matter[N dM - M dN]",
        "potential_note": "All local mirror-even potential derivatives cancel from the antisymmetric bracket.",
    }


def rescaling_no_go():
    rows = []
    for s in (-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5):
        hda_factor = s * s
        rows.append({
            "s": s,
            "HDA_D_factor": hda_factor,
            "target_defect": abs(hda_factor - 1.0),
            "same_HDA_normalization": abs(hda_factor - 1.0) < 1e-15,
            "interpretation": (
                "time/normal orientation reversal only"
                if s == -1.0 else
                "ordinary branch"
                if s == 1.0 else
                "deformed HDA normalization"
            ),
        })
    return {
        "rows": rows,
        "result": "Same HDA normalization forces s^2=1; s=-1 is N->-N, not static antigravity.",
    }


def yukawa_gate():
    xs = [0.0, 0.1, 0.5, 1.0, 2.0, 5.0]
    rows = []
    for x in xs:
        alpha_crit = math.exp(x) / (1.0 + x)
        rows.append({
            "x_mphi_r": x,
            "alpha_screening_threshold": alpha_crit,
            "alpha_repulsion_condition": f"alpha > {alpha_crit:.12g}",
        })

    alpha_demo = 2.0
    x_demo = 0.1
    scalar_over_tensor = alpha_demo * (1.0 + x_demo) * math.exp(-x_demo)
    opposite_net_outward_over_tensor = scalar_over_tensor - 1.0
    same_total_inward_over_tensor = 1.0 + scalar_over_tensor
    opposite_over_same_measured = opposite_net_outward_over_tensor / same_total_inward_over_tensor

    return {
        "potential": "U=-G_T m1 m2/r - alpha G_T m1 m2 chi1 chi2 exp(-mphi r)/r",
        "force_ratio_scalar_to_tensor": "alpha*(1+x)*exp(-x), x=mphi*r",
        "thresholds": rows,
        "demo": {
            "alpha": alpha_demo,
            "x": x_demo,
            "scalar_over_tensor": scalar_over_tensor,
            "opposite_chi_net_outward_over_bare_tensor_gravity": opposite_net_outward_over_tensor,
            "same_chi_total_inward_over_bare_tensor_gravity": same_total_inward_over_tensor,
            "opposite_repulsion_over_same_sector_measured_attraction": opposite_over_same_measured,
        },
        "massless_limit": {
            "screening": "alpha=1",
            "repulsion": "alpha>1",
            "same_sector": "extra attraction",
            "opposite_sector": "repulsion if alpha>1",
        },
    }


def stability_gate():
    mu2 = 0.7**2
    lam = 0.2
    kappa = 0.4
    bounded_large_field = (mu2 > 0.0 and lam > 0.0 and kappa > 0.0)

    return {
        "canonical_phi_kinetic_sign": +1,
        "canonical_sigma_kinetic_sign": +1,
        "mu_squared": mu2,
        "lambda_phi4": lam,
        "kappa_sigma4": kappa,
        "bounded_at_large_field": bool(bounded_large_field),
        "negative_EH_coefficient_branch": {
            "effective_G_sign_flip_possible": True,
            "graviton_kinetic_sign": -1,
            "healthy": False,
            "reason": "A negative Einstein-Hilbert coefficient is a graviton ghost relative to positive-energy matter.",
        },
        "passed": bool(bounded_large_field),
    }


def run(L: int = 512):
    scalar_hda = scalar_hda_gate(L)
    rescale = rescaling_no_go()
    yukawa = yukawa_gate()
    stability = stability_gate()

    passed = (
        scalar_hda["passed"]
        and stability["passed"]
        and abs(yukawa["thresholds"][0]["alpha_screening_threshold"] - 1.0) < 1e-15
        and any(r["s"] == -1.0 and r["same_HDA_normalization"] for r in rescale["rows"])
    )

    return {
        "status": "orientation-odd HDA construction and healthy mirror-force gate",
        "passed": bool(passed),
        "mirror_order_parameter": "chi=sign(sigma)=+/-1, coarse-grained from the microscopic oriented Y_L/Q coordinate",
        "candidate_action": (
            "S=int sqrt(-g)[Mpl^2 R/2 - (dphi)^2/2 - (dsigma)^2/2 - U(phi,sigma)], "
            "U=mu^2 phi^2/2 + lambda phi^4/4 + g phi sigma + kappa(sigma^2-v^2)^2/4"
        ),
        "mirror_symmetry": "(phi,sigma)->(-phi,-sigma)",
        "rescaling_no_go": rescale,
        "metric_sign_flip_stability": stability["negative_EH_coefficient_branch"],
        "healthy_field_stability": stability,
        "canonical_matter_HDA": scalar_hda,
        "mirror_force": yukawa,
        "main_result": (
            "A healthy orientation-dependent repulsive interaction exists at the continuum candidate level "
            "without negative energy: opposite chi charges repel through a positive-kinetic mediator when "
            "alpha(1+mphi*r)exp(-mphi*r)>1. This is a fifth-force/multi-sector effect, not yet a sign flip of g00."
        ),
        "microscopic_bottleneck": (
            "Derive sigma/phi and their charge eta from the Peter-Weyl/route operators, then embed their "
            "Hamiltonian into the quantum geometry x route HDA and re-run the off-shell closure gate."
        ),
        "scope_note": (
            "The numerical HDA check is a continuum canonical two-pseudoscalar matter-sector control on a periodic "
            "spectral grid. General covariance motivates total GR+matter first-class closure, but the microscopic "
            "CIMFIG/Peter-Weyl quantum HDA with this new sector is not yet proved."
        ),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--L", type=int, default=512)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    out = run(args.L)
    text = json.dumps(out, indent=2, ensure_ascii=False)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
