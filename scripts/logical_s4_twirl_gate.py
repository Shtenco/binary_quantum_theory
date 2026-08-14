#!/usr/bin/env python3
"""Exact S4 face-permutation twirl on the four-spin singlet geometry qubit.

A fully face-permutation-symmetric one-cell operator is scalar on the 2D singlet
geometry-qubit sector (Schur). For two logical geometry qubits under the same
local tetrahedral frame permutation, the invariant operator space is larger.

This gate constructs all 24 permutations explicitly on the four spin-1/2 tensor
legs, projects them onto the K=0/2 singlet basis, and computes the diagonal S4
twirl on the 4x4 two-logical-qubit operator space.

The invariant mirror-even two-cell pseudospin structure is shown to contain two
independent bilinear channels:

    X⊗X + Z⊗Z    (shape-plane scalar)
    Y⊗Y          (orientation-pseudoscalar product)

plus I⊗I. Therefore tetrahedral face-permutation symmetry removes label-axis
artifacts but does NOT force Heisenberg equality J_shape=J_orientation.
The residual scalar anisotropy Delta=J_orientation-J_shape is symmetry allowed
and is the correct coarse killer observable for the Goldstone mirror route.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import k5_peter_weyl_safe_hda_column as PW


PAULI = {
    "I": np.eye(2, dtype=complex),
    "X": np.array([[0, 1], [1, 0]], dtype=complex),
    "Y": np.array([[0, -1j], [1j, 0]], dtype=complex),
    "Z": np.array([[1, 0], [0, -1]], dtype=complex),
}


def normalize(v):
    n = math.sqrt(float(np.vdot(v, v).real))
    return v / n


def singlet_basis():
    return [normalize(PW.oriented_intertwiner(0, (1, 1, 1, 1), K)) for K in (0, 2)]


def permute_tensor(T, p):
    # New slot a takes old slot p[a]. This convention is enough for the closed
    # group because all 24 permutations are included.
    return np.transpose(T, axes=p)


def logical_representation(p, basis):
    U = np.zeros((2, 2), dtype=complex)
    for j, ket in enumerate(basis):
        pk = permute_tensor(ket, p)
        for i, bra in enumerate(basis):
            U[i, j] = np.vdot(bra, pk)
    return U


def twirl_one(M, reps):
    return sum(U @ M @ U.conj().T for U in reps) / len(reps)


def twirl_two(M, reps):
    out = np.zeros_like(M, dtype=complex)
    for U in reps:
        W = np.kron(U, U)
        out += W @ M @ W.conj().T
    return out / len(reps)


def pauli_coeff_2(M):
    out = {}
    for a, A in PAULI.items():
        for b, B in PAULI.items():
            P = np.kron(A, B)
            out[a + b] = np.trace(P @ M) / 4.0
    return out


def vec(M):
    return M.reshape(-1)


def invariant_superoperator(reps):
    # Superoperator on 4x4 matrices, vectorized in row-major convention.
    S = np.zeros((16, 16), dtype=complex)
    E = []
    for i in range(4):
        for j in range(4):
            M = np.zeros((4, 4), dtype=complex)
            M[i, j] = 1.0
            E.append(M)
    for col, M in enumerate(E):
        S[:, col] = vec(twirl_two(M, reps))
    return S


def cjson(z):
    z = complex(z)
    return [float(z.real), float(z.imag)]


def run():
    basis = singlet_basis()
    perms = list(itertools.permutations(range(4)))
    reps = [logical_representation(p, basis) for p in perms]

    unitarity_error = max(float(np.linalg.norm(U.conj().T @ U - np.eye(2))) for U in reps)

    # Schur test: every one-qubit Pauli twirls to zero, I stays I.
    one = {name: twirl_one(P, reps) for name, P in PAULI.items()}
    one_nontrivial_norm = max(float(np.linalg.norm(one[a])) for a in ("X", "Y", "Z"))
    one_I_error = float(np.linalg.norm(one["I"] - np.eye(2)))

    shape = np.kron(PAULI["X"], PAULI["X"]) + np.kron(PAULI["Z"], PAULI["Z"])
    orient = np.kron(PAULI["Y"], PAULI["Y"])
    shape_tw = twirl_two(shape, reps)
    orient_tw = twirl_two(orient, reps)
    shape_error = float(np.linalg.norm(shape_tw - shape))
    orient_error = float(np.linalg.norm(orient_tw - orient))

    S = invariant_superoperator(reps)
    evals = np.linalg.eigvals(S)
    invariant_dim = int(np.sum(np.abs(evals - 1.0) < 1e-9))

    # A deliberately generic Hermitian mirror-even two-qubit operator. Its
    # twirl should reduce to I, shape-dot and YY only.
    test = (
        0.7 * np.kron(PAULI["I"], PAULI["I"])
        + 0.3 * np.kron(PAULI["X"], PAULI["X"])
        - 0.8 * np.kron(PAULI["Z"], PAULI["Z"])
        + 0.25 * np.kron(PAULI["X"], PAULI["Z"])
        + 0.25 * np.kron(PAULI["Z"], PAULI["X"])
        + 1.1 * np.kron(PAULI["Y"], PAULI["Y"])
        + 0.4 * np.kron(PAULI["X"], PAULI["I"])
        - 0.2 * np.kron(PAULI["I"], PAULI["Z"])
    )
    test_tw = twirl_two(test, reps)
    c = pauli_coeff_2(test_tw)

    allowed = {"II", "XX", "ZZ", "YY"}
    forbidden_norm = math.sqrt(sum(abs(v) ** 2 for k, v in c.items() if k not in allowed))
    shape_split = abs(c["XX"] - c["ZZ"])

    # Independence of the two invariant bilinears proves S4 does not enforce
    # Heisenberg equality. Their Hilbert-Schmidt overlap is zero.
    bilinear_overlap = float(abs(np.trace(shape.conj().T @ orient)))

    passed = (
        len(reps) == 24
        and unitarity_error < 1e-12
        and one_nontrivial_norm < 1e-12
        and one_I_error < 1e-12
        and shape_error < 1e-12
        and orient_error < 1e-12
        and invariant_dim == 3
        and forbidden_norm < 1e-12
        and shape_split < 1e-12
        and bilinear_overlap < 1e-12
    )

    return {
        "status": "exact logical S4 face-permutation twirl gate",
        "passed": bool(passed),
        "permutation_count": len(perms),
        "max_logical_representation_unitarity_error": unitarity_error,
        "one_cell_Schur_control": {
            "max_twirl_nonidentity_Pauli_norm": one_nontrivial_norm,
            "identity_error": one_I_error,
        },
        "two_cell_invariant_dimension": invariant_dim,
        "invariant_bilinears": ["XX+ZZ", "YY"],
        "shape_bilinear_twirl_error": shape_error,
        "orientation_bilinear_twirl_error": orient_error,
        "shape_orientation_HS_overlap": bilinear_overlap,
        "generic_mirror_even_twirl_pauli": {k: cjson(v) for k, v in c.items()},
        "generic_twirl_forbidden_norm": forbidden_norm,
        "generic_twirl_XX_minus_ZZ_abs": float(shape_split),
        "coarse_form": "K_sym=c0 II + J_shape(XX+ZZ) + J_orientation YY",
        "symmetry_allowed_anisotropy": "Delta_aniso=J_orientation-J_shape",
        "main_result": (
            "Full tetrahedral face-permutation symmetry removes one-cell logical fields and in-plane label artifacts, "
            "but it leaves two independent two-cell couplings: the X/Z shape-plane scalar and the Y/Y orientation "
            "product. Therefore mirror and S4 symmetry do not protect Heisenberg equality."
        ),
        "next_gate": (
            "Apply the same S4 twirl to the environment-traced Peter-Weyl return kernel and track "
            "Delta_aniso=J_orientation-J_shape under a justified resolvent/RG/refinement flow."
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
