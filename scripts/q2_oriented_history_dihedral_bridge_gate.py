#!/usr/bin/env python3
"""Exact oriented-history dihedral bridge: winding, conjugation and geometry Y.

For an oriented cyclic history carrier, let T be one forward history step and R
reverse orientation.  The defining relation

    R T R = T^{-1}

is the finite dihedral analogue of the universal-cover history group

    Z semidirect_{n -> -n} Z2 = D_infinity.

On a phase character T -> exp(i theta), R exchanges theta <-> -theta, hence
complex conjugation.  The Hermitian history current

    C_h = (T - T^dagger)/(2 i)

has eigenvalue sin(theta) (up to the shift convention) and is reflection odd.
The q=2 tetrahedral geometry orientation operator Y is also reflection odd, so

    H_lock = Y tensor C_h

is invariant under the diagonal reflection Z tensor R, where Z Y Z = -Y.

This is exact group/representation theory.  It proves the allowed invariant
bridge between the winding-character phase and geometry orientation; it does
not prove that the microscopic Hamiltonian constraint has a nonzero coefficient
multiplying H_lock.  That coefficient is measured separately by the production
Peter-Weyl history-current gate.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def shift(N: int) -> np.ndarray:
    T = np.zeros((N, N), complex)
    for n in range(N):
        T[(n + 1) % N, n] = 1.0
    return T


def reflection(N: int) -> np.ndarray:
    R = np.zeros((N, N), complex)
    for n in range(N):
        R[(-n) % N, n] = 1.0
    return R


def fourier_state(N: int, k: int) -> np.ndarray:
    # With T|n>=|n+1>, this convention gives T|k>=exp(-2 pi i k/N)|k>.
    n = np.arange(N)
    v = np.exp(2j * np.pi * k * n / N) / np.sqrt(N)
    return v


def relerr(A, B):
    return float(np.linalg.norm(A - B) / max(np.linalg.norm(B), 1e-30))


def run(Ns=(4, 8, 16, 32)):
    Y = np.array([[0, -1j], [1j, 0]], complex)
    Z = np.array([[1, 0], [0, -1]], complex)
    per_N = {}
    worst = 0.0

    for N in Ns:
        T = shift(N)
        R = reflection(N)
        I = np.eye(N, dtype=complex)
        C = (T - T.conj().T) / (2j)

        group_checks = {
            "T_unitary": relerr(T.conj().T @ T, I),
            "R_involution": relerr(R @ R, I),
            "RTR_equals_Tdagger": relerr(R @ T @ R, T.conj().T),
            "current_reflection_odd": relerr(R @ C @ R, -C),
        }

        J = np.kron(Z, R)
        Hlock = np.kron(Y, C)
        joint_err = relerr(J @ Hlock @ J.conj().T, Hlock)

        spectral = []
        conj_errors = []
        for k in range(N):
            v = fourier_state(N, k)
            lam_T = np.vdot(v, T @ v)
            lam_C = np.vdot(v, C @ v)
            expected_T = np.exp(-2j * np.pi * k / N)
            expected_C = -np.sin(2 * np.pi * k / N)
            kbar = (-k) % N
            vb = fourier_state(N, kbar)
            phase = np.vdot(vb, R @ v)
            mapped = R @ v
            # Compare rays, removing the irrelevant unit phase.
            if abs(phase) > 1e-15:
                mapped = mapped / phase
            cerr = float(np.linalg.norm(mapped - vb))
            conj_errors.append(cerr)
            spectral.append({
                "k": k,
                "theta": float(2 * np.pi * k / N),
                "T_character": [float(lam_T.real), float(lam_T.imag)],
                "T_expected": [float(expected_T.real), float(expected_T.imag)],
                "current_eigenvalue": float(lam_C.real),
                "current_expected": float(expected_C),
                "reflection_partner_k": kbar,
            })

        spectral_T_err = max(
            abs(complex(*s["T_character"]) - complex(*s["T_expected"]))
            for s in spectral
        )
        current_err = max(abs(s["current_eigenvalue"] - s["current_expected"]) for s in spectral)
        vals = list(group_checks.values()) + [joint_err, max(conj_errors), spectral_T_err, current_err]
        worst = max(worst, *vals)
        per_N[str(N)] = {
            "group_errors": group_checks,
            "diagonal_lock_invariance_error": joint_err,
            "reflection_character_pairing_max_error": max(conj_errors),
            "character_spectrum_max_error": float(spectral_T_err),
            "current_sine_spectrum_max_error": float(current_err),
            "spectral_table": spectral,
        }

    geometry_odd = relerr(Z @ Y @ Z, -Y)
    worst = max(worst, geometry_odd)
    passed = worst < 1e-12

    return {
        "status": "exact oriented-history dihedral winding/phase/orientation bridge",
        "passed": bool(passed),
        "finite_carriers": list(Ns),
        "geometry_reflection_odd_error": geometry_odd,
        "max_exact_gate_error": worst,
        "finite_group_relation": "D_N=<T,R | T^N=1, R^2=1, R T R=T^{-1}>",
        "universal_cover_relation": "D_infinity=Z semidirect Z2 with R w R=-w",
        "pontryagin_dual_statement": "Z-hat = U(1); T-character exp(i theta) is exchanged with exp(-i theta) by orientation reversal",
        "history_current": "C_h=(T-T^dagger)/(2i), reflection odd, character eigenvalue proportional to sin(theta)",
        "geometry_orientation": "Y_L is reflection/sign-character odd",
        "invariant_locking_channel": "Y_L tensor C_h is invariant under simultaneous geometry/history reversal",
        "per_N": per_N,
        "claim_boundary": (
            "Exact finite representation-theory controls plus the standard universal-cover group identity. "
            "This proves that a geometry-orientation/history-current locking operator is symmetry-consistent and that history reversal implements phase conjugation. "
            "It does not prove a nonzero microscopic coupling, physical time, physical projector, continuum gauge dynamics, photon, or experimental observable."
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
