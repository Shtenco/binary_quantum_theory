#!/usr/bin/env python3
"""Finite graviton-helicity qubit and conditional foam/resonance gate."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp

FROZEN_DELTA_G_EXPONENT = 2.001707


def _kron_on(op: np.ndarray, site: int, n: int = 4) -> np.ndarray:
    eye = np.eye(2, dtype=complex)
    out = np.array([[1.0 + 0.0j]])
    for i in range(n):
        out = np.kron(out, op if i == site else eye)
    return out


def spin2_from_four_qubits() -> dict:
    sx = np.array([[0, 1], [1, 0]], dtype=complex) / 2.0
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex) / 2.0
    sz = np.array([[1, 0], [0, -1]], dtype=complex) / 2.0
    Jx = sum(_kron_on(sx, i) for i in range(4))
    Jy = sum(_kron_on(sy, i) for i in range(4))
    Jz = sum(_kron_on(sz, i) for i in range(4))
    J2 = Jx @ Jx + Jy @ Jy + Jz @ Jz

    evals, evecs = np.linalg.eigh(J2)
    expected = {0.0: 2, 2.0: 9, 6.0: 5}
    observed = {0.0: 0, 2.0: 0, 6.0: 0}
    for value in evals:
        target = min(observed, key=lambda x: abs(float(value) - x))
        observed[target] += 1

    plus2 = np.zeros(16, dtype=complex)
    minus2 = np.zeros(16, dtype=complex)
    plus2[0] = 1.0
    minus2[-1] = 1.0

    j2_mask = np.abs(evals - 6.0) < 1e-9
    P2 = evecs[:, j2_mask] @ evecs[:, j2_mask].conj().T
    plus_leak = float(np.linalg.norm((np.eye(16) - P2) @ plus2))
    minus_leak = float(np.linalg.norm((np.eye(16) - P2) @ minus2))

    j2_plus = float(np.vdot(plus2, J2 @ plus2).real)
    j2_minus = float(np.vdot(minus2, J2 @ minus2).real)
    m_plus = float(np.vdot(plus2, Jz @ plus2).real)
    m_minus = float(np.vdot(minus2, Jz @ minus2).real)
    linear_plus = (plus2 + minus2) / np.sqrt(2.0)
    linear_cross = (plus2 - minus2) / (1j * np.sqrt(2.0))
    overlap = abs(complex(np.vdot(linear_plus, linear_cross)))

    passed = (
        observed == expected
        and abs(j2_plus - 6.0) < 1e-12
        and abs(j2_minus - 6.0) < 1e-12
        and abs(m_plus - 2.0) < 1e-12
        and abs(m_minus + 2.0) < 1e-12
        and plus_leak < 1e-12
        and minus_leak < 1e-12
        and overlap < 1e-12
    )
    return {
        "passed": bool(passed),
        "decomposition": "(1/2)^4 = 2xj0 + 3xj1 + 1xj2",
        "J2_eigenvalue_multiplicities": observed,
        "j2_irrep_dimension": 5,
        "helicity_code_dimension": 2,
        "helicity_basis": ["m=+2", "m=-2"],
        "plus2_J2": j2_plus,
        "minus2_J2": j2_minus,
        "plus2_Jz": m_plus,
        "minus2_Jz": m_minus,
        "j2_projector_leakage": {"plus2": plus_leak, "minus2": minus_leak},
        "linear_polarization_overlap_abs": overlap,
        "interpretation": "four spin-1/2 qubits are the minimum microscopic set that can carry a j=2 collective sector; physical massless +/-2 helicities form a logical polarization qubit",
    }


def hyperuniform_inference(p: float = FROZEN_DELTA_G_EXPONENT) -> dict:
    n = 2.0 * p - 3.0
    return {
        "conditional": True,
        "input_rms_exponent_p": p,
        "inferred_low_k_power_n": n,
        "relation": "RMS(delta_g_R) ~ R^{-(3+n)/2}; n=2p-3",
        "white_noise_reference_n": 0.0,
        "white_noise_rms_exponent": 1.5,
        "hyperuniform_if_interpreted_as_variance": bool(n > 0.0),
        "interpretation": f"if the frozen delta-g exponent is a quantum RMS exponent, then P_delta_g(k) ~ k^{n:.6f} at low k",
    }


def floquet_growth(omega: float, drive: float, modulation: float) -> float:
    period = 2.0 * np.pi / drive

    def rhs(t: float, y: np.ndarray) -> np.ndarray:
        M = y.reshape(2, 2)
        A = np.array([[0.0, 1.0], [-omega**2 * (1.0 + modulation * np.cos(drive * t)), 0.0]])
        return (A @ M).reshape(-1)

    sol = solve_ivp(rhs, (0.0, period), np.eye(2).reshape(-1), method="DOP853", rtol=2e-11, atol=1e-13)
    M = sol.y[:, -1].reshape(2, 2)
    eig = np.linalg.eigvals(M)
    raw = float(np.max(np.log(np.abs(eig))) / period)
    return max(0.0, raw)


def parametric_resonance_gate() -> dict:
    omega = 1.0
    modulation = 0.02
    mu_numeric = floquet_growth(omega, 2.0 * omega, modulation)
    mu_leading = abs(modulation) * omega / 4.0
    below = floquet_growth(omega, 1.8 * omega, modulation)
    above = floquet_growth(omega, 2.2 * omega, modulation)
    edge_lo = floquet_growth(omega, 1.99 * omega, modulation)
    edge_hi = floquet_growth(omega, 2.01 * omega, modulation)
    rel = abs(mu_numeric - mu_leading) / mu_leading
    passed = rel < 0.01 and mu_numeric > 1e-4 and below < 1e-8 and above < 1e-8 and edge_lo < mu_numeric and edge_hi < mu_numeric
    return {
        "passed": bool(passed),
        "model_equation": "qddot + omega_I^2 [1 + xi*h*cos(Omega_GW*t)] q = 0",
        "vacuum_channel": "parametric squeezing / pair excitation",
        "resonance_condition": "Omega_GW ~= 2 omega_I",
        "test_omega_I": omega,
        "test_modulation_xi_h": modulation,
        "floquet_mu_numeric": mu_numeric,
        "floquet_mu_leading": mu_leading,
        "relative_error_to_small_modulation_formula": rel,
        "leading_band_halfwidth_in_Omega": abs(modulation) * omega / 2.0,
        "off_resonance_growth": {"Omega=1.8omega": below, "Omega=2.2omega": above},
        "near_band_edge_growth": {"Omega=1.99omega": edge_lo, "Omega=2.01omega": edge_hi},
        "physical_formula": "mu ~= |xi*h| omega_I / 4",
        "scope": "resonance is conditional on a nonzero TT metric coupling xi; the gate does not establish an infoton or derive xi",
    }


def illustrative_scale() -> dict:
    h = 1e-21
    f_gw = 100.0
    f_mode = f_gw / 2.0
    omega_mode = 2.0 * np.pi * f_mode
    mu = h * omega_mode / 4.0
    seconds_per_year = 365.25 * 24.0 * 3600.0
    return {
        "illustrative_not_model_prediction": True,
        "assumed_strain_h": h,
        "assumed_GW_frequency_Hz": f_gw,
        "parametric_resonant_mode_frequency_Hz": f_mode,
        "assumed_dimensionless_coupling_xi": 1.0,
        "growth_rate_per_second": mu,
        "e_fold_time_years": 1.0 / mu / seconds_per_year,
    }


def run() -> dict:
    spin = spin2_from_four_qubits()
    resonance = parametric_resonance_gate()
    return {
        "status": "graviton helicity qubit + conditional foam/resonance bridge",
        "passed_finite_gates": bool(spin["passed"] and resonance["passed"]),
        "graviton_qubit": spin,
        "foam_IR_inference": hyperuniform_inference(),
        "GW_information_mode_resonance": resonance,
        "illustrative_scale": illustrative_scale(),
        "candidate_infoton_definition": "project-local route/information-sector bosonic collective mode; binary polarization does not by itself determine Lorentz spin",
        "mode_hilbert_space": "Fock occupation x C^2 polarization/helicity",
        "not_claimed": ["new experimentally observed particle", "vacuum energy extraction", "proof that all quantum foam is caused by gravitational waves", "derived infoton-graviton coupling xi"],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    out = run()
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed_finite_gates"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
