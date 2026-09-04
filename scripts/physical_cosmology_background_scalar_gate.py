#!/usr/bin/env python3
"""Reference gate for background/scalar cosmology and lensing-dynamics closure.

This gate does NOT invent BQG dark matter or dark energy. It freezes the map that a future
physical connected-history effective action Gamma[g,A] must satisfy:

* rho_hist(a) -> w_hist(a) through covariant background conservation;
* pressureless a^-3 and constant vacuum density are recovered as w=0 and w=-1 controls;
* scalar dynamics is parameterized by the Newtonian potential Psi and Weyl potential
  (Phi+Psi)/2, so growth/dynamics and gravitational lensing cannot be fitted independently;
* the no-slip DM-like reference has the same enhancement in dynamical and lensing masses;
* a deliberately split lensing response is retained as a negative control.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

TOL = 2e-5


def infer_w_from_rho(a: np.ndarray, rho: np.ndarray) -> np.ndarray:
    if np.any(a <= 0) or np.any(rho <= 0):
        raise ValueError("a and rho must be positive")
    ln_a = np.log(a)
    ln_rho = np.log(rho)
    dlnrho_dln_a = np.gradient(ln_rho, ln_a, edge_order=2)
    return -1.0 - dlnrho_dln_a / 3.0


def pressure_from_conservation(a: np.ndarray, rho: np.ndarray) -> np.ndarray:
    return infer_w_from_rho(a, rho) * rho


def conservation_residual(a: np.ndarray, rho: np.ndarray, p: np.ndarray) -> np.ndarray:
    ln_a = np.log(a)
    drho_dln_a = np.gradient(rho, ln_a, edge_order=2)
    scale = np.maximum(np.abs(rho), 1e-30)
    return (drho_dln_a + 3.0 * (rho + p)) / scale


def scalar_response(mu: float, sigma: float) -> dict:
    if mu <= 0 or sigma <= 0:
        raise ValueError("mu and sigma must be positive in this reference gate")
    # Definitions:
    # -k^2 Psi = 4 pi G a^2 mu rho Delta
    # -k^2 (Phi+Psi) = 8 pi G a^2 Sigma rho Delta
    eta = 2.0 * sigma / mu - 1.0  # Phi/Psi
    lensing_to_dynamical_mass = sigma / mu
    return {
        "mu": mu,
        "Sigma": sigma,
        "eta_Phi_over_Psi": eta,
        "M_lens_over_M_dyn": lensing_to_dynamical_mass,
    }


def run_gate() -> dict:
    # Log grid makes power-law differentiation especially clean.
    a = np.geomspace(0.08, 1.0, 501)

    rho_m = a ** -3.0
    rho_v = np.ones_like(a)
    rho_r = a ** -4.0

    w_m = infer_w_from_rho(a, rho_m)
    w_v = infer_w_from_rho(a, rho_v)
    w_r = infer_w_from_rho(a, rho_r)

    sl = slice(3, -3)
    matter_w_error = float(np.max(np.abs(w_m[sl] - 0.0)))
    vacuum_w_error = float(np.max(np.abs(w_v[sl] + 1.0)))
    radiation_w_error = float(np.max(np.abs(w_r[sl] - 1.0 / 3.0)))

    # Slowly evolving synthetic reference. This is not a fit or BQG prediction.
    w0, wa = -0.94, 0.11
    rho_cpl = a ** (-3.0 * (1.0 + w0 + wa)) * np.exp(-3.0 * wa * (1.0 - a))
    w_cpl_expected = w0 + wa * (1.0 - a)
    w_cpl = infer_w_from_rho(a, rho_cpl)
    cpl_w_error = float(np.max(np.abs(w_cpl[sl] - w_cpl_expected[sl])))

    p_cpl = pressure_from_conservation(a, rho_cpl)
    conservation_error = float(np.max(np.abs(conservation_residual(a, rho_cpl, p_cpl)[sl])))

    # Scalar/lensing closure controls.
    # A DM-like no-slip enhancement can be represented phenomenologically by mu=Sigma>1.
    no_slip = scalar_response(mu=1.65, sigma=1.65)
    no_slip_eta_error = abs(no_slip["eta_Phi_over_Psi"] - 1.0)
    no_slip_mass_error = abs(no_slip["M_lens_over_M_dyn"] - 1.0)

    # Negative control: dynamics and lensing are independently enhanced.
    split = scalar_response(mu=1.65, sigma=1.15)
    split_mass_mismatch = abs(split["M_lens_over_M_dyn"] - 1.0)
    split_slip_mismatch = abs(split["eta_Phi_over_Psi"] - 1.0)

    # Null history sector must not manufacture an extra cosmological component.
    rho_hist_null = np.zeros_like(a)
    null_extra_density = float(np.max(np.abs(rho_hist_null)))

    # Synthetic positive Friedmann reference with a history component. The numbers are
    # arbitrary and used only to verify that the map is algebraically well behaved.
    om_b, om_r, om_hist = 0.05, 8e-5, 0.25
    h2 = om_b * a ** -3 + om_r * a ** -4 + om_hist * a ** -3 + (1 - om_b - om_r - om_hist)
    friedmann_positive = bool(np.all(np.isfinite(h2)) and np.all(h2 > 0))

    passed = all(
        [
            matter_w_error < TOL,
            vacuum_w_error < TOL,
            radiation_w_error < TOL,
            cpl_w_error < 2e-4,
            conservation_error < 2e-3,
            no_slip_eta_error < 1e-12,
            no_slip_mass_error < 1e-12,
            split_mass_mismatch > 0.1,
            split_slip_mismatch > 0.1,
            null_extra_density == 0.0,
            friedmann_positive,
        ]
    )

    return {
        "schema_version": 1,
        "passed": passed,
        "status": "tested_finite_reference" if passed else "failed_reference",
        "background_controls": {
            "matter_a^-3_w_error": matter_w_error,
            "vacuum_constant_w_error": vacuum_w_error,
            "radiation_a^-4_w_error": radiation_w_error,
            "evolving_reference_w_error": cpl_w_error,
            "continuity_residual": conservation_error,
            "null_history_extra_density": null_extra_density,
            "synthetic_friedmann_positive": friedmann_positive,
        },
        "scalar_lensing_controls": {
            "no_slip_reference": no_slip,
            "no_slip_eta_error": no_slip_eta_error,
            "no_slip_lensing_dynamics_mass_error": no_slip_mass_error,
            "split_negative_control": split,
            "split_lensing_dynamics_mass_mismatch": split_mass_mismatch,
            "split_gravitational_slip_mismatch": split_slip_mismatch,
        },
        "required_future_outputs": [
            "rho_hist(a) and p_hist(a) derived from Gamma_FLRW, not selected from a fitted w(a)",
            "physical scalar Hessian/kernel giving Psi, Phi, stability and growth",
            "effective sound speed and anisotropic stress of any DM-like history component",
            "the same Weyl potential (Phi+Psi)/2 for lensing deflection and optical phase",
            "joint lensing + dynamics + CMB/large-scale-structure comparison with one frozen theory output",
        ],
        "scientific_boundary": (
            "Passing this gate validates only the cosmological bookkeeping and cross-observable "
            "consistency map. It does not show that BQG generates rho~a^-3, rho=const, a viable "
            "dark sector, or the observed lensing signal. Those remain open until derived from "
            "the theory-specific physical projector/history and connected effective action."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    result = run_gate()
    text = json.dumps(result, indent=2, ensure_ascii=False)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
