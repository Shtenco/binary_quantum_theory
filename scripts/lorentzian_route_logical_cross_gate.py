#!/usr/bin/env python3
"""Quantify the signed logical Lorentzian-route cross channel.

Independent upstream gates now freeze, in beta=hbar=1 structural units,

    H_phase = c_L Y,                c_L=1.3389293521464034
    H_L,bare / H_phase = -16/9
    H_corr,full / H_phase = -32/9.

The route-ordering diagnostic is therefore no longer reported only per an open
normalization g_R.  This gate keeps the raw/unit coefficient for regression and
also reports the signed bare-H_L and full-beta=1 correction cross operators.

Expectation-first isotropic route average is scalar and gives zero local cross.
Operator-first gives a nonzero X/Z cross.  This remains a finite logical
regression, not the full graph-changing two-node HDA.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

C_L = 1.3389293521464034
BARE_HL_PHASE_COEFF = -16.0/9.0
FULL_CORR_PHASE_COEFF = -32.0/9.0
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


def summary_for(scale, Cop):
    C = scale * Cop
    c = {k: np.trace(P @ C) / 2.0 for k, P in PAULI.items()}
    return {
        "phase_scale": scale,
        "pauli": {k: zpair(v) for k, v in c.items()},
        "shape_coefficient_norm": float(np.hypot(abs(c["X"]), abs(c["Z"]))),
        "frobenius_norm": float(np.linalg.norm(C)),
    }


def run():
    Hphase = C_L * Y
    Oexp = OMEGA_EXP_I * I
    Oop = OMEGA_OP_I * I + OMEGA_OP_X * X + OMEGA_OP_Z * Z

    Cexp = cross(Hphase, Oexp)
    Cop = cross(Hphase, Oop)
    cop = {k: np.trace(P @ Cop) / 2.0 for k, P in PAULI.items()}

    expected_x = 2.0 * C_L * OMEGA_OP_Z
    expected_z = -2.0 * C_L * OMEGA_OP_X
    raw_shape_norm = float(np.hypot(abs(cop["X"]), abs(cop["Z"])))
    raw_frob = float(np.linalg.norm(Cop))

    bare = summary_for(BARE_HL_PHASE_COEFF, Cop)
    full = summary_for(FULL_CORR_PHASE_COEFF, Cop)

    checks = {
        "expectation_first_cross_zero": float(np.linalg.norm(Cexp)) < 1e-14,
        "operator_first_cross_nonzero": raw_frob > 1e-6,
        "operator_first_cross_hermitian": float(np.linalg.norm(Cop-Cop.conj().T)) < 1e-14,
        "operator_first_no_I": abs(cop["I"]) < 1e-14,
        "operator_first_no_Y": abs(cop["Y"]) < 1e-14,
        "operator_first_X_formula": abs(cop["X"].real-expected_x) < 1e-12 and abs(cop["X"].imag) < 1e-12,
        "operator_first_Z_formula": abs(cop["Z"].real-expected_z) < 1e-12 and abs(cop["Z"].imag) < 1e-12,
        "bare_phase_scale_frozen": abs(bare["phase_scale"] + 16.0/9.0) < 1e-15,
        "full_phase_scale_frozen": abs(full["phase_scale"] + 32.0/9.0) < 1e-15,
        "bare_signed_X": abs(bare["pauli"]["X"][0] + 0.09539108408604444) < 2e-12,
        "bare_signed_Z": abs(bare["pauli"]["Z"][0] + 0.16522220393013332) < 2e-12,
        "full_signed_X": abs(full["pauli"]["X"][0] + 0.19078216817208887) < 2e-12,
        "full_signed_Z": abs(full["pauli"]["Z"][0] + 0.33044440786026663) < 2e-12,
    }

    return {
        "status": "finite signed logical Lorentzian-route ordering regression",
        "passed": all(checks.values()),
        "beta": 1.0,
        "hbar": 1.0,
        "phase_completed_local_coefficient": C_L,
        "frozen_bare_HL_phase_scale": BARE_HL_PHASE_COEFF,
        "frozen_full_correction_phase_scale": FULL_CORR_PHASE_COEFF,
        "expectation_first_route_operator": {"I": OMEGA_EXP_I, "X": 0.0, "Y": 0.0, "Z": 0.0},
        "expectation_first_cross_frobenius_norm": float(np.linalg.norm(Cexp)),
        "operator_first_route_operator": {"I": OMEGA_OP_I, "X": OMEGA_OP_X, "Y": 0.0, "Z": OMEGA_OP_Z},
        "operator_first_cross_identity": "-i[c_L Y, Omega_op] = 2 c_L (Omega_Z X - Omega_X Z)",
        "unit_phase_cross_pauli": coeffs(Cop),
        "unit_phase_cross_shape_coefficient_norm": raw_shape_norm,
        "unit_phase_cross_frobenius_norm": raw_frob,
        "signed_bare_HL_cross": bare,
        "signed_full_beta1_correction_cross": full,
        "checks": checks,
        "interpretation": (
            "The previously open normalization is now fixed upstream. In beta=hbar=1 structural units the operator-first "
            "logical route block predicts a definite negative X/Z cross for both the bare repository H_L and the full beta=1 "
            "Lorentzian correction. The expectation-first isotropic surrogate still erases the same cross exactly."
        ),
        "scope": (
            "Finite logical two-by-two regression using frozen averaged route coefficients and the independently frozen signed "
            "Lorentzian relative normalization. It is not the graph-changing two-node HDA and is not a physical energy/force prediction."
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
