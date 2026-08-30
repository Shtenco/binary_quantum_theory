#!/usr/bin/env python3
"""Exact diagonal-S4 pure invariant from two local [2,2] singlet carriers.

The companion local obstruction gate proves that one four-spin-1/2 Gauss
singlet carrier transforms as the irreducible S4 [2,2] representation and has
no nonzero local invariant vector.  This gate proves the constructive next
statement: [2,2] tensor [2,2] contains the trivial representation exactly once.

It builds the diagonal group projector

    P2 = (1/24) sum_g R_g tensor R_g

from the independently constructed local recoupling representation, verifies
that P2 is a rank-one orthogonal projector, and checks the explicit normalized
state vec(I_2)/sqrt(2) against all 24 diagonal group actions.  Its one-carrier
reduced density matrix is I/2, so the global invariant is locally maximally
mixed while remaining globally pure.

This is an internal recoupling-sector construction.  It does not yet include
how the same global S4 element permutes graph nodes/edges in the full 16-cell.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import numpy as np

import q4_local_s4_singlet_obstruction_gate as LOCAL

TOL = 3e-12


def multiplicity_formula(N: int) -> int:
    # Character [2,2] on S4 classes:
    # sizes (1,6,8,3,6), chars (2,0,-1,2,0).
    num = 2 ** (N + 2) + 8 * ((-1) ** N)
    if num % 24:
        raise RuntimeError("character multiplicity failed integrality")
    return num // 24


def matrix_json(M: np.ndarray) -> list[list[list[float]]]:
    return [[[float(z.real), float(z.imag)] for z in row] for row in np.asarray(M, complex)]


def run() -> dict[str, object]:
    basis = LOCAL.singlet_basis()
    perms = tuple(itertools.permutations(range(4)))
    reps = {p: LOCAL.rep_matrix(basis, p)[0] for p in perms}

    diagonal_reps = {p: np.kron(R, R) for p, R in reps.items()}
    P2 = sum(diagonal_reps.values()) / len(perms)
    P2h = 0.5 * (P2 + P2.conj().T)
    evals = np.linalg.eigvalsh(P2h)

    herm_def = float(np.linalg.norm(P2 - P2.conj().T, 2))
    idem_def = float(np.linalg.norm(P2 @ P2 - P2, 2))
    rank = int(np.sum(evals > 1e-10))
    trace = float(np.trace(P2h).real)

    # In the real orthogonal recoupling basis, vec(I)/sqrt(2) is invariant
    # under R tensor R because R R^T = I.  We nevertheless verify all 24.
    psi = np.asarray([1.0, 0.0, 0.0, 1.0], complex) / np.sqrt(2.0)
    max_state_defect = max(float(np.linalg.norm(U @ psi - psi)) for U in diagonal_reps.values())
    projector_state_defect = float(np.linalg.norm(P2 @ psi - psi))

    # Compare the unique projector with |psi><psi| without choosing a phase.
    rho = np.outer(psi, psi.conj())
    projector_match = float(np.linalg.norm(P2h - rho, 2))

    # Reduced density of first carrier.
    A = psi.reshape(2, 2)
    rho_A = A @ A.conj().T
    rho_B = A.T @ A.conj()
    red_A_error = float(np.linalg.norm(rho_A - 0.5 * np.eye(2), 2))
    red_B_error = float(np.linalg.norm(rho_B - 0.5 * np.eye(2), 2))
    entropy_A = float(-sum(x * np.log2(x) for x in np.linalg.eigvalsh(rho_A) if x > 1e-15))

    multiplicities = {str(N): multiplicity_formula(N) for N in range(1, 17)}
    expected_small = {"1": 0, "2": 1, "3": 1, "4": 3, "5": 5, "6": 11}

    # Direct character trace of P2 independently confirms rank/multiplicity.
    character_sq_average = float(sum((np.trace(R) ** 2).real for R in reps.values()) / len(perms))

    checks = {
        "P2_Hermitian": herm_def < TOL,
        "P2_idempotent": idem_def < TOL,
        "P2_rank_one": rank == 1 and abs(trace - 1.0) < TOL,
        "character_multiplicity_two_is_one": abs(character_sq_average - 1.0) < TOL and multiplicities["2"] == 1,
        "explicit_vecI_state_invariant_under_all_24": max_state_defect < TOL,
        "explicit_state_is_projector_image": projector_state_defect < TOL,
        "unique_projector_equals_explicit_state_density": projector_match < TOL,
        "local_reduced_density_A_is_I_over_2": red_A_error < TOL,
        "local_reduced_density_B_is_I_over_2": red_B_error < TOL,
        "entanglement_entropy_one_bit": abs(entropy_A - 1.0) < TOL,
        "multiplicity_formula_small_values": all(multiplicities[k] == v for k, v in expected_small.items()),
        "sixteen_carrier_diagonal_invariant_multiplicity": multiplicities["16"] == 10923,
    }
    passed = bool(all(checks.values()))

    return {
        "status": "exact two-carrier diagonal-S4 globally pure invariant construction",
        "science_status": "TWO_LOCAL_[2,2]_CARRIERS_HAVE_UNIQUE_DIAGONAL_S4_PURE_SINGLET" if passed else "TWO_BLOCK_S4_CONSTRUCTION_FAIL",
        "passed": passed,
        "local_representation": "S4 [2,2]",
        "two_carrier_dimension": 4,
        "diagonal_trivial_multiplicity": rank,
        "P2_eigenvalues": [float(x) for x in evals],
        "P2_trace": trace,
        "P2_Hermiticity_defect": herm_def,
        "P2_idempotence_defect": idem_def,
        "character_squared_group_average": character_sq_average,
        "explicit_invariant_state_basis_order": ["i0⊗i0", "i0⊗i1", "i1⊗i0", "i1⊗i1"],
        "explicit_invariant_state": [[float(z.real), float(z.imag)] for z in psi],
        "max_all_24_state_invariance_defect": max_state_defect,
        "projector_to_explicit_state_defect": projector_match,
        "first_carrier_reduced_density": matrix_json(rho_A),
        "second_carrier_reduced_density": matrix_json(rho_B),
        "single_carrier_entanglement_entropy_bits": entropy_A,
        "diagonal_S4_trivial_multiplicity_N_1_to_16": multiplicities,
        "multiplicity_closed_form": "m_N=(2^(N-1)+(-1)^N)/3",
        "checks": checks,
        "physical_interpretation": (
            "Local pure S4 invariance is obstructed, but two recoupling carriers can restore diagonal S4 exactly through entanglement. "
            "The invariant state is globally pure and each local carrier is maximally mixed."
        ),
        "claim_boundary": (
            "This proves only diagonal S4 invariance in the tensor product of two local recoupling [2,2] carriers. "
            "The full BCQG 16-cell symmetry also permutes nodes, links, orientations and Hamiltonian support; that graph action is not included here. "
            "Therefore this is a constructive representation prerequisite, not yet the physical homogeneous/isotropic BCQG background."
        ),
    }


def main() -> int:
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
