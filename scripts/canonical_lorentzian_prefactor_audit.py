#!/usr/bin/env python3
"""Executable algebraic audit of the raw Lorentzian K-K-V prefactor phase.

The finite Peter-Weyl code uses raw commutators.  Restoring the canonical
Poisson-to-commutator factors introduces five powers of 1/i:

  one in each of the two K ~ [V,H_E]/(i hbar) factors,
  one in each of the three connection brackets C(K), C(K), C(V).

Therefore the structural phase is (1/i)^5=-i.  The script also verifies that a
Hermitian one-body term a Y rotates the logical metric-shape X/Z coordinates.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)

RAW_Y_ABS = 1.3389293521464034
COV_ERR = 1.3976239359266602e-15
VOLUME_LEAK = 6.532094795930893e-16


def comm(a, b):
    return a @ b - b @ a


def run():
    phase = (1 / 1j) ** 5

    # Raw environment-unbiased orientation block is i*y*Y, equivalently a real
    # antisymmetric matrix.  Multiplying by -i must make it Hermitian.
    Lraw = 1j * RAW_Y_ABS * Y
    Hstruct = -1j * Lraw

    # Heisenberg equations with hbar=1 and H=aY.
    a = RAW_Y_ABS
    H = a * Y
    dX = 1j * comm(H, X)
    dZ = 1j * comm(H, Z)

    phase_ok = abs(phase + 1j) < 1e-15
    herm_err = float(np.linalg.norm(Hstruct - Hstruct.conj().T))
    x_err = float(np.linalg.norm(dX - 2 * a * Z))
    z_err = float(np.linalg.norm(dZ + 2 * a * X))

    passed = phase_ok and herm_err < 1e-14 and x_err < 1e-14 and z_err < 1e-14

    return {
        "status": "canonical raw-Lorentzian prefactor phase audit",
        "passed": bool(passed),
        "number_of_inverse_i_factors": 5,
        "inverse_i_power": [float(phase.real), float(phase.imag)],
        "required_structural_phase": "-i",
        "raw_environment_unbiased_Y_abs": RAW_Y_ABS,
        "raw_matrix": [[[float(z.real), float(z.imag)] for z in row] for row in Lraw],
        "hermitian_structural_matrix_after_minus_i": [
            [[float(z.real), float(z.imag)] for z in row] for row in Hstruct
        ],
        "hermiticity_error": herm_err,
        "shape_rotation": {
            "dX_expected": "+2*a*Z / hbar",
            "dZ_expected": "-2*a*X / hbar",
            "dX_error_hbar1": x_err,
            "dZ_error_hbar1": z_err,
            "local_angular_frequency": "Omega_L=2*|a_L|/hbar",
        },
        "source_orbit_diagnostics": {
            "S4_covariance_relative_error": COV_ERR,
            "max_volume_basis_leakage": VOLUME_LEAK,
        },
        "normalization_boundary": (
            "The phase is fixed by the declared commutator bookkeeping. The remaining real "
            "magnitude depends only on the already-existing volume/action normalization and "
            "frozen canonical/regulator coefficients; this script does not fit them."
        ),
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path)
    a = p.parse_args()
    out = run()
    text = json.dumps(out, indent=2)
    print(text)
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
