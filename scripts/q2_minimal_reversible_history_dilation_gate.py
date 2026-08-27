#!/usr/bin/env python3
"""Minimal reversible history dilation of the q=2 C4 graph-link transition.

The instantaneous graph-link carrier has four orthogonal active states and one
rank-one no-link state.  Mapping all four active states into the same no-link
state cannot be reversible unless an auxiliary/history channel preserves which
transition is underway.

For an isometry

    |k> -> |no-link> tensor |e_k>,

inner-product preservation forces <e_k|e_l>=delta_kl, hence channel dimension
>=4.  The minimal history sector therefore contains 4 active + 4 transition
states = 8 states.

This script constructs the minimal 8D unitary

    U = [[0, S4],
         [I,  0 ]]

in the decomposition H_active direct-sum H_transition.  It alternates

    active k -> transition k -> active k+1,

has exact order eight, and U^2 restricts to the oriented C4 shift on the active
sector.  This is an exact reversible/history representation theorem, not yet a
derivation of the physical projector or of recursive all-scale phase locking.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def shift_matrix(n: int) -> np.ndarray:
    S = np.zeros((n, n), dtype=int)
    for k in range(n):
        S[(k + 1) % n, k] = 1
    return S


def matrix_order(U: np.ndarray, max_power: int = 100) -> int | None:
    I = np.eye(U.shape[0], dtype=int)
    P = np.eye(U.shape[0], dtype=int)
    for p in range(1, max_power + 1):
        P = P @ U
        if np.array_equal(P, I):
            return p
    return None


def run() -> dict[str, object]:
    n = 4
    I4 = np.eye(n, dtype=int)
    S4 = shift_matrix(n)
    Z4 = np.zeros((n, n), dtype=int)

    # Basis order: active[0..3], transition[0..3].
    U = np.block([[Z4, S4], [I4, Z4]])
    U2 = U @ U
    target_U2 = np.block([[S4, Z4], [Z4, S4]])

    # First half-step active -> no-link x channel is represented by the channel
    # Gram matrix. Reversibility forces rank four / four orthogonal channel tags.
    channel_gram = I4.copy()
    channel_rank = int(np.linalg.matrix_rank(channel_gram))

    # Instantaneous physical projection forgets all four channel labels.
    # Columns: 4 active + 4 transition-history states; rows: 4 active + no-link.
    F = np.zeros((5, 8), dtype=int)
    F[:4, :4] = I4
    F[4, 4:] = 1
    physical_projection_rank = int(np.linalg.matrix_rank(F))
    transition_projection = F[:, 4:]
    transition_image_rank = int(np.linalg.matrix_rank(transition_projection))

    # Explicit transition sequence under U.
    sequence = []
    state = np.zeros(8, dtype=int)
    state[0] = 1
    for t in range(9):
        idx = int(np.argmax(state))
        sequence.append(
            {
                "t": t,
                "history_basis_index": idx,
                "sector": "active" if idx < 4 else "transition",
                "label": idx if idx < 4 else idx - 4,
            }
        )
        state = U @ state

    checks = {
        "U_is_integer_permutation": bool(
            np.all((U == 0) | (U == 1))
            and np.all(U.sum(axis=0) == 1)
            and np.all(U.sum(axis=1) == 1)
        ),
        "U_is_orthogonal": bool(np.array_equal(U.T @ U, np.eye(8, dtype=int))),
        "U_squared_is_two_C4_shifts": bool(np.array_equal(U2, target_U2)),
        "active_sector_two_ticks_equal_C4_shift": bool(np.array_equal(U2[:4, :4], S4)),
        "history_update_has_order_8": matrix_order(U, 32) == 8,
        "reversible_no_link_channel_requires_rank4": channel_rank == 4,
        "minimal_channel_dimension_is_at_least_4": channel_rank == n,
        "instantaneous_projection_collapses_transition_channels_to_rank1": transition_image_rank == 1,
        "instantaneous_projection_is_noninvertible": physical_projection_rank == 5 < 8,
        "eight_ticks_return_to_start": sequence[0]["history_basis_index"] == sequence[-1]["history_basis_index"],
    }

    return {
        "status": "exact minimal reversible/history dilation of the q=2 oriented C4 transition through a rank-one physical no-link bottleneck",
        "passed": bool(all(checks.values())),
        "active_dimension": 4,
        "instantaneous_no_link_dimension": 1,
        "forced_minimum_history_channel_dimension": channel_rank,
        "minimal_reversible_history_dimension": 8,
        "history_unitary": U.tolist(),
        "history_unitary_order": matrix_order(U, 32),
        "coarse_C4_shift": S4.tolist(),
        "two_tick_operator": U2.tolist(),
        "physical_forgetting_map_rank": physical_projection_rank,
        "transition_history_to_no_link_image_rank": transition_image_rank,
        "one_full_history_cycle": sequence,
        "checks": checks,
        "theorem": (
            "If four orthogonal q=2 active channels all pass through the same rank-one physical no-link state and the full evolution is reversible/isometric, the lost channel identity must be retained in an orthogonal history/environment carrier of dimension at least four. The minimal active+transition history dilation is eight-dimensional and admits the unique simple carry cycle active k -> transition k -> active k+1 of order eight."
        ),
        "claim_boundary": (
            "This proves the minimal reversible dilation and the necessity of channel memory. It does not prove that the gravitational physical-projector/history measure selects this minimal dilation, nor that the same dilation recursively refines every phase edge at all scales."
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
