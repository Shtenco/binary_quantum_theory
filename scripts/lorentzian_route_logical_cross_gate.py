#!/usr/bin/env python3
"""Quantify the logical Lorentzian-route cross channel for two route orderings.

Inputs already frozen by independent calculations:

  H_L,phase / g_R = c_L Y, c_L=1.3389293521464034

Expectation-first isotropic route average:

  Omega_exp = 0.8598466001022401 I

Operator-first isotropic square-root diagnostic:

  Omega_op ~= 0.8197716816 I -0.0347058975 X +0.0200374593 Z.

This gate computes the Hermitian cross generator

  C = -i [H_L, Omega].

For expectation-first averaging C=0 exactly at the quoted logical level.
For operator-first ordering C lies in the X/Z shape plane and is nonzero.

This is a finite ordering discriminator, not a full HDA result. The fixed-cutoff
composition theorem can still suppress such a finite cross coefficient by the
regulator scaling; the purpose here is to freeze the coefficient that a future
full two-node Lorentzian HDA test must reproduce if operator-first route
ordering is chosen.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

C_L = 1.3389293521464034
OMEGA_EXP_I = 0.8598466001022401
OMEGA_OP_I = 0.8197716816
OMEGA_OP_X = -0.0347058975
OMEGA_OP_Z = 0.0200374593

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = {"I": I, "X": X, "Y": Y, "Z": Z}


def zpair(z):
    z = complex(z)
    return [float(z.real), float(z.imag)]


def coeffs(M):
    return {k: zpair(np.trace(P @ M) / 2.0) for k, P in PAULI.items()}


def cross(H, O):
    return -1j * (H @ O - O @ H)


def run():
    H = C_L * Y
    Oexp = OMEGA_EXP_I * I
    Oop = OMEGA_OP_I * I + OMEGA_OP_X * X + OMEGA_OP_Z * Z

    Cexp = cross(H, Oexp)
    Cop = cross(H, Oop)
    cop = {k: np.trace(P @ Cop) / 2.0 for k, P in PAULI.items()}

    expected_x = 2.0 * C_L * OMEGA_OP_Z
    expected_z = -2.0 * C_L * OMEGA_OP_X
    shape_norm = float(np.hypot(abs(cop["X"]), abs(cop["Z"])))
    frob = float(np.linalg.norm(Cop))

    checks = {
        "expectation_first_cross_zero": float(np.linalg.norm(Cexp)) < 1e-14,
        "operator_first_cross_nonzero": frob > 1e-6,
        "operator_first_cross_hermitian": float(np.linalg.norm(Cop-Cop.conj().T)) < 1e-14,
        "operator_first_no_I": abs(cop["I"]) < 1e-14,
        "operator_first_no_Y": abs(cop["Y"]) < 1e-14,
        "operator_first_X_formula": abs(cop["X"].real-expected_x) < 1e-12 and abs(cop["X"].imag) < 1e-12,
        "operator_first_Z_formula": abs(cop["Z"].real-expected_z) < 1e-12 and abs(cop["Z"].imag) < 1e-12,
    }

    return {
        "status": "finite logical Lorentzian-route ordering discriminator",
        "passed": all(checks.values()),
        "lorentzian_phase_completed_coefficient_per_gR": C_L,
        "expectation_first_route_operator": {"I": OMEGA_EXP_I, "X": 0.0, "Y": 0.0, "Z": 0.0},
        "expectation_first_cross_frobenius_norm_per_abs_gR": float(np.linalg.norm(Cexp)),
        "operator_first_route_operator": {"I": OMEGA_OP_I, "X": OMEGA_OP_X, "Y": 0.0, "Z": OMEGA_OP_Z},
        "operator_first_cross_identity": "-i[c_L Y, Omega_op] = 2 c_L (Omega_Z X - Omega_X Z)",
        "operator_first_cross_pauli_per_gR": coeffs(Cop),
        "operator_first_cross_shape_coefficient_norm_per_abs_gR": shape_norm,
        "operator_first_cross_frobenius_norm_per_abs_gR": frob,
        "checks": checks,
        "interpretation": (
            "Expectation-first isotropic averaging erases this local logical cross, "
            "whereas operator-first square-root ordering produces a finite X/Z shape "
            "cross coefficient. A full route/HDA calculation must therefore select "
            "the ordering dynamically/algebraically rather than treating them as "
            "interchangeable."
        ),
        "scope": (
            "Finite logical two-by-two diagnostic using previously frozen averaged "
            "route coefficients. It is not a two-node HDA closure calculation and "
            "does not include the still-open real Lorentzian normalization g_R."
        ),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    out = run()
    text = json.dumps(out, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
