#!/usr/bin/env python3
"""Extract the Lorentzian ordered-triple geometry-orientation current.

This gate does not recompute the expensive Peter-Weyl environment trace.  It
consumes the already-frozen successful production evidence and asks a new,
pre-registered operator-identification question:

Does the local geometry pseudoscalar Y live in the reversal-odd part of an
ordered Lorentzian triple pair 123 <-> 132?

The input orbit artifact contains the exact environment-averaged 2x2 source
blocks T123 and T132, together with an S4 covariance reconstruction and the
full 24-term sign-twirled one-body operator.  We decompose both blocks in the
Pauli basis and form

    cY_even = (cY_123 + cY_132)/2,
    cY_odd  = (cY_132 - cY_123)/2.

For the raw operator the Y coefficients are anti-Hermitian (pure imaginary).
The unique minimal Hermitian phase completion

    H_phase = -i/2 (L_raw - L_raw^dagger)

maps the imaginary coefficient i a to the real coefficient a.  The gate also
checks the frozen beta=hbar=1 signed repository normalization.

A pass proves a finite ordered-triple reflection current coupled to the q=2
geometry pseudoscalar.  It does NOT yet prove that this discrete ordered-triple
reflection is the full universal-cover winding translation character, nor that
the resulting constraint-history label is physical time.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

PAULI = {
    "I": np.eye(2, dtype=complex),
    "X": np.array([[0, 1], [1, 0]], complex),
    "Y": np.array([[0, -1j], [1j, 0]], complex),
    "Z": np.array([[1, 0], [0, -1]], complex),
}


def decode_matrix(rows):
    return np.array([[complex(*z) for z in row] for row in rows], dtype=complex)


def pauli(M):
    return {k: np.trace(P.conj().T @ M) / 2.0 for k, P in PAULI.items()}


def cpair(z):
    z = complex(z)
    return [float(z.real), float(z.imag)]


def run(orbit_path: Path, herm_path: Path, sign_path: Path):
    orbit = json.loads(orbit_path.read_text(encoding="utf-8"))
    herm = json.loads(herm_path.read_text(encoding="utf-8"))
    sign = json.loads(sign_path.read_text(encoding="utf-8"))

    T123 = decode_matrix(orbit["T123_environment_average"])
    T132 = decode_matrix(orbit["T132_environment_average"])
    p123 = pauli(T123)
    p132 = pauli(T132)

    y123 = p123["Y"]
    y132 = p132["Y"]
    y_even = 0.5 * (y123 + y132)
    y_odd = 0.5 * (y132 - y123)

    # Reflection-odd raw Y amplitude is pure imaginary.  Minimal Hermitian
    # phase projection sends i*a -> a.
    completed_pair_y = float(y_odd.imag)

    full_raw_y = complex(*orbit["onebody_Y_coefficient_raw"])
    full_completed_y = float(full_raw_y.imag)
    full_signed_corr = float(sign["local_full_correction_coefficient"])
    full_signed_bare = float(sign["local_bare_HL_coefficient"])

    expected_full_completed = float(herm["environment_unbiased_onebody_signed_Y"]) / (-32.0 / 9.0)
    expected_full_signed = (-32.0 / 9.0) * full_completed_y
    expected_bare_signed = (-16.0 / 9.0) * full_completed_y

    # The source orbit file already states that T132 is reconstructed by S4
    # covariance; keep that as an independent control rather than assuming the
    # two matrices are hand-selected reversal partners.
    cov_err = float(orbit["T132_covariance_relative_error"])
    leakage = float(orbit["max_physical_basis_volume_leakage"])

    even_ratio = float(abs(y_even) / max(abs(y_odd), 1e-30))
    real_leak_ratio = float(max(abs(y123.real), abs(y132.real)) / max(abs(y_odd), 1e-30))

    checks = {
        "orbit_source_passed": bool(orbit.get("passed")),
        "hermitian_completion_passed": bool(herm.get("passed")),
        "repo_sign_passed": bool(sign.get("passed")),
        "ordered_pair_Y_is_nonzero": bool(abs(y_odd) > 1e-6),
        "ordered_pair_Y_even_cancels": bool(even_ratio < 1e-12),
        "ordered_pair_Y_is_raw_antihermitian": bool(real_leak_ratio < 1e-12),
        "T132_S4_covariance": bool(cov_err < 1e-12),
        "volume_leakage_control": bool(leakage < 1e-12),
        "full_orbit_Y_is_nonzero": bool(abs(full_raw_y) > 1e-3),
        "full_orbit_Y_is_raw_antihermitian": bool(abs(full_raw_y.real) < 1e-12 * abs(full_raw_y.imag)),
        "minimal_Hermitian_completion_consistent": bool(abs(full_completed_y - expected_full_completed) < 1e-12),
        "signed_full_normalization_consistent": bool(abs(full_signed_corr - expected_full_signed) < 1e-12),
        "signed_bare_normalization_consistent": bool(abs(full_signed_bare - expected_bare_signed) < 1e-12),
        "no_fit_used": bool(sign.get("fitting_used") is False),
    }

    return {
        "status": "finite Lorentzian ordered-history geometry-Y current extractor",
        "passed": bool(all(checks.values())),
        "source_node": int(orbit["source_node"]) if "source_node" in orbit else 0,
        "ordered_pair": ["123", "132"],
        "T123_pauli": {k: cpair(v) for k, v in p123.items()},
        "T132_pauli": {k: cpair(v) for k, v in p132.items()},
        "Y_pair": {
            "cY_123_raw": cpair(y123),
            "cY_132_raw": cpair(y132),
            "cY_even_raw": cpair(y_even),
            "cY_odd_raw": cpair(y_odd),
            "odd_over_even_inverse_ratio": float(abs(y_odd) / max(abs(y_even), 1e-30)),
            "even_over_odd_ratio": even_ratio,
            "real_leak_over_odd_ratio": real_leak_ratio,
            "minimal_Hermitian_completed_pair_Y": completed_pair_y,
        },
        "full_24term_environment_unbiased": {
            "raw_Y": cpair(full_raw_y),
            "minimal_Hermitian_completed_Y_before_repo_prefactor": full_completed_y,
            "signed_full_beta1_hbar1_Y": full_signed_corr,
            "signed_bare_HL_beta1_hbar1_Y": full_signed_bare,
        },
        "controls": {
            "T132_covariance_relative_error": cov_err,
            "max_physical_basis_volume_leakage": leakage,
        },
        "checks": checks,
        "decision": (
            "NONZERO_LORENTZIAN_ORDERED_TRIPLE_REFLECTION_ODD_Y_CURRENT"
            if all(checks.values())
            else "GATE_FAILED"
        ),
        "interpretation": (
            "The existing Lorentzian Peter-Weyl candidate has a nonzero q=2 geometry-pseudoscalar Y amplitude in the reversal-odd part of the ordered 123<->132 triple pair, and that anti-Hermitian raw phase survives the unique minimal Hermitian projection as a real Y coefficient."
        ),
        "claim_boundary": (
            "FINITE_PASS on frozen finite-cutoff production evidence. This establishes an ordered-triple reflection current, not yet a universal-cover winding-character spectral decomposition. It does not identify constraint history with physical time, derive the physical rigging map, continuum U(1) dynamics, alpha, masses, or an experimental observable."
        ),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--orbit", type=Path, default=Path("verification_results/PETER_WEYL_LORENTZIAN_ENVTRACE_ORBIT.json"))
    ap.add_argument("--hermitian", type=Path, default=Path("verification_results/LORENTZIAN_HERMITIAN_COMPLETION.json"))
    ap.add_argument("--sign", type=Path, default=Path("verification_results/LORENTZIAN_REPO_SIGN.json"))
    ap.add_argument("--output", type=Path)
    a = ap.parse_args()
    out = run(a.orbit, a.hermitian, a.sign)
    txt = json.dumps(out, indent=2)
    print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(txt + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
