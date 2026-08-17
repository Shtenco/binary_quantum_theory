#!/usr/bin/env python3
"""Exact representation bridge: q=2 active labels + graph absence -> j=1/2 link.

A frozen q=2 cell has four route states.  Four states alone admit the existing
SO(5) spinor quantum-link algebra, but under SU(2)_L x SU(2)_R that spinor is
(2,1) + (1,2), not the Peter-Weyl j=1/2 bi-doublet (2,2).

The graph-changing Hilbert space already contains a natural additional state:
an absent/cylindrically deleted j=0 link.  Adding this single no-link state to
the four active q=2 states gives the existing five-state SO(5) vector quantum
link, which decomposes exactly as

    5 = (2,2) + (1,1).

The four-dimensional active projector therefore carries j_L=j_R=1/2 and the
singlet is the no-link state.  Every fundamental transporter component toggles
between the active q=2 sector and the no-link singlet.

This gate also records the strict four-state-only obstruction and checks that
the q=2 Hamming adjacency already belongs to the compatible SO(5) spinor
operator algebra.  No dynamical selection of the SO(5) completion is claimed.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

import su2_quantum_link_two_qubit_gate as SPINOR
import su2_quantum_link_vector5_gate as VECTOR


def projector_from_casimir(C: np.ndarray) -> np.ndarray:
    return (4.0 / 3.0) * C


def run() -> dict[str, object]:
    # ---- Four-state q=2 Hilbert: exact obstruction to a (2,2) active link. ----
    L4, R4, _ = SPINOR.build()
    CL4 = sum(x @ x for x in L4)
    CR4 = sum(x @ x for x in R4)
    PL4 = projector_from_casimir(CL4)
    PR4 = projector_from_casimir(CR4)

    # In the spinor4 representation the left/right doublet sectors are
    # complementary: (2,1) + (1,2).  Therefore no state carries both endpoint
    # spin-1/2 Casimirs simultaneously.
    spinor_overlap = float(np.linalg.norm(PL4 @ PR4))
    spinor_completeness = float(np.linalg.norm(PL4 + PR4 - np.eye(4)))

    # The q=2 Hamming adjacency A_Q2 = X⊗I + I⊗X is nevertheless already inside
    # the same SO(5) spinor operator algebra.
    A_q2 = np.kron(SPINOR.X, SPINOR.I) + np.kron(SPINOR.I, SPINOR.X)
    A_so5 = 2.0 * (SPINOR.Mab(1, 2) + SPINOR.Mab(3, 4))
    adjacency_embedding_error = float(np.linalg.norm(A_q2 - A_so5))

    # ---- Add the already-available graph-absence state: vector5. ----
    L5, R5, _ = VECTOR.build()
    CL5 = sum(x @ x for x in L5)
    CR5 = sum(x @ x for x in R5)
    PgL = projector_from_casimir(CL5)
    PgR = projector_from_casimir(CR5)
    Pg = 0.5 * (PgL + PgR)
    Ps = np.eye(5) - Pg

    active_rank = int(round(float(np.trace(Pg).real)))
    singlet_rank = int(round(float(np.trace(Ps).real)))
    endpoint_projector_match = float(np.linalg.norm(PgL - PgR))
    active_left_casimir_error = float(np.linalg.norm(Pg @ CL5 @ Pg - 0.75 * Pg))
    active_right_casimir_error = float(np.linalg.norm(Pg @ CR5 @ Pg - 0.75 * Pg))
    singlet_casimir_error = float(np.linalg.norm(Ps @ CL5 @ Ps) + np.linalg.norm(Ps @ CR5 @ Ps))

    # Standard vector5 basis: the first four directions span the active
    # bi-doublet, the fifth direction is the gauge singlet/no-link state.
    basis = np.eye(5, dtype=complex)
    active_basis_errors = [float(np.linalg.norm(Pg @ basis[:, i] - basis[:, i])) for i in range(4)]
    no_link_error = float(np.linalg.norm(Ps @ basis[:, 4] - basis[:, 4]))

    # Four transporter components U_alpha=M_{alpha,4}, alpha=0..3.  Acting on
    # the no-link state produces four orthonormal active states and they have no
    # active->active or singlet->singlet blocks.
    components = [VECTOR.M(a, 4) for a in range(4)]
    vacuum = basis[:, 4]
    created = np.column_stack([Pg @ u @ vacuum for u in components])
    created_gram = created.conj().T @ created
    creation_orthonormal_error = float(np.linalg.norm(created_gram - np.eye(4)))
    active_active = max(float(np.linalg.norm(Pg @ u @ Pg)) for u in components)
    singlet_singlet = max(float(np.linalg.norm(Ps @ u @ Ps)) for u in components)
    active_singlet_norms = [float(np.linalg.norm(Pg @ u @ Ps)) for u in components]
    singlet_active_norms = [float(np.linalg.norm(Ps @ u @ Pg)) for u in components]

    checks = {
        "q2_hilbert_dimension_is_4": A_q2.shape == (4, 4),
        "q2_adjacency_embeds_exactly_in_spinor_so5": adjacency_embedding_error < 1e-12,
        "four_state_left_right_doublets_are_complementary": spinor_overlap < 1e-12 and spinor_completeness < 1e-12,
        "four_state_only_has_no_bidoublet": int(round(np.trace(PL4 @ PR4).real)) == 0,
        "vector5_active_rank_is_4": active_rank == 4,
        "vector5_no_link_rank_is_1": singlet_rank == 1,
        "active_left_right_projectors_match": endpoint_projector_match < 1e-12,
        "active_sector_has_jL_jR_half": active_left_casimir_error < 1e-12 and active_right_casimir_error < 1e-12,
        "no_link_is_endpoint_singlet": singlet_casimir_error < 1e-12,
        "first_four_basis_states_are_active": max(active_basis_errors) < 1e-12,
        "fifth_basis_state_is_no_link": no_link_error < 1e-12,
        "transporter_creates_orthonormal_active_basis_from_no_link": creation_orthonormal_error < 1e-12,
        "transporter_has_no_diagonal_sector_blocks": active_active < 1e-12 and singlet_singlet < 1e-12,
        "transporter_toggles_both_directions_with_unit_norm": all(abs(x - 1.0) < 1e-12 for x in active_singlet_norms + singlet_active_norms),
    }

    return {
        "status": "exact q=2 active-route plus graph-absence representation bridge to an SU(2)_L x SU(2)_R j=1/2 link",
        "passed": bool(all(checks.values())),
        "q2_active_labels": [[0, 0], [0, 1], [1, 0], [1, 1]],
        "four_state_spinor_decomposition": "(2,1) + (1,2)",
        "four_state_left_casimir_spectrum": np.linalg.eigvalsh(CL4).tolist(),
        "four_state_right_casimir_spectrum": np.linalg.eigvalsh(CR4).tolist(),
        "four_state_bidoublet_projector_overlap_norm": spinor_overlap,
        "q2_hamming_adjacency_so5_embedding_error": adjacency_embedding_error,
        "five_state_decomposition": "(2,2) + (1,1)",
        "active_q2_sector_rank": active_rank,
        "no_link_singlet_rank": singlet_rank,
        "endpoint_projector_match_error": endpoint_projector_match,
        "active_left_casimir_error": active_left_casimir_error,
        "active_right_casimir_error": active_right_casimir_error,
        "no_link_casimir_error": singlet_casimir_error,
        "transporter_creation_gram": created_gram.real.tolist(),
        "transporter_creation_orthonormal_error": creation_orthonormal_error,
        "checks": checks,
        "interpretation": (
            "The missing state needed to turn the four q=2 active labels into a Peter-Weyl j=1/2 bi-doublet is naturally supplied by the graph-changing no-link/j=0 state already present in the cylindrical Hilbert space. "
            "This removes a finite-dimensional representation mismatch without adding a new fundamental local label."
        ),
        "claim_boundary": (
            "Exact kinematic representation theorem only. It does not derive the SO(5) transporter coefficients from the frozen rewrite Hamiltonian, prove dynamical attraction to the active geometric sector, or derive higher-j Peter-Weyl representation growth under blocking."
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
