#!/usr/bin/env python3
"""Exact local Q4 ↔ K5 four-valent singlet-carrier compatibility gate.

This implements Q4_K5_LOCAL_CARRIER_BRIDGE_PREREGISTRATION.md.  It compares
an explicit Q4 four-spin-1/2 singlet basis against the canonical K5
Peter-Weyl K=0,2 intertwiner basis without fitting any basis transformation.

A PASS is local representation compatibility only; Q4 and K5 remain distinct
global graphs and no B4 covariance of the K5 Hamiltonian is claimed.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import numpy as np

import k5_peter_weyl_safe_hda_column as PW

TOL = 2e-12
PERMS = tuple(itertools.permutations(range(4)))


def explicit_q4_basis() -> list[np.ndarray]:
    z = np.asarray([1.0, 0.0], complex)
    o = np.asarray([0.0, 1.0], complex)
    s = (np.kron(z, o) - np.kron(o, z)) / np.sqrt(2.0)
    i0 = np.kron(s, s).reshape(2, 2, 2, 2)

    tp = np.kron(z, z)
    t0 = (np.kron(z, o) + np.kron(o, z)) / np.sqrt(2.0)
    tm = np.kron(o, o)
    i1 = (
        np.kron(tp, tm) - np.kron(t0, t0) + np.kron(tm, tp)
    ).reshape(2, 2, 2, 2) / np.sqrt(3.0)
    return [i0, i1]


def k5_basis() -> list[np.ndarray]:
    return [
        PW.intertwiner_tensor_cached((1, 1, 1, 1), 0),
        PW.intertwiner_tensor_cached((1, 1, 1, 1), 2),
    ]


def gram(basis: list[np.ndarray]) -> np.ndarray:
    return np.asarray([[np.vdot(a, b) for b in basis] for a in basis], complex)


def rep_matrix(basis: list[np.ndarray], p: tuple[int, ...]) -> np.ndarray:
    return np.asarray(
        [[np.vdot(a, np.transpose(b, axes=p)) for b in basis] for a in basis],
        complex,
    )


def compose(g: tuple[int, ...], h: tuple[int, ...]) -> tuple[int, ...]:
    # np.transpose(np.transpose(T,h),g) = np.transpose(T, compose(g,h)).
    return tuple(h[g[i]] for i in range(4))


def cycle_type(p: tuple[int, ...]) -> tuple[int, ...]:
    seen: set[int] = set()
    out: list[int] = []
    for i in range(4):
        if i in seen:
            continue
        j = i
        n = 0
        while j not in seen:
            seen.add(j)
            n += 1
            j = p[j]
        out.append(n)
    return tuple(sorted(out, reverse=True))


def matrix_json(M: np.ndarray) -> list[list[list[float]]]:
    return [[[float(z.real), float(z.imag)] for z in row] for row in np.asarray(M, complex)]


def restricted_volume(basis: list[np.ndarray]) -> np.ndarray:
    out = np.zeros((2, 2), complex)
    for j, b in enumerate(basis):
        vb = PW.apply_volume_tensor(b, (1, 1, 1, 1))
        for i, a in enumerate(basis):
            out[i, j] = np.vdot(a, vb)
    return 0.5 * (out + out.conj().T)


def run() -> dict[str, object]:
    q4 = explicit_q4_basis()
    k5 = k5_basis()

    Gq = gram(q4)
    Gk = gram(k5)
    overlap = np.asarray([[np.vdot(a, b) for b in k5] for a in q4], complex)
    raw_overlap_error = float(np.linalg.norm(overlap - np.eye(2), 2))

    Rq = {p: rep_matrix(q4, p) for p in PERMS}
    Rk = {p: rep_matrix(k5, p) for p in PERMS}

    max_rep_bridge_error = 0.0
    max_q4_unitarity = 0.0
    max_k5_unitarity = 0.0
    max_q4_group_error = 0.0
    max_k5_group_error = 0.0
    permutation_rows = []
    for p in PERMS:
        bridge = float(np.linalg.norm(Rq[p] - Rk[p], 2))
        uq = float(np.linalg.norm(Rq[p].conj().T @ Rq[p] - np.eye(2), 2))
        uk = float(np.linalg.norm(Rk[p].conj().T @ Rk[p] - np.eye(2), 2))
        max_rep_bridge_error = max(max_rep_bridge_error, bridge)
        max_q4_unitarity = max(max_q4_unitarity, uq)
        max_k5_unitarity = max(max_k5_unitarity, uk)
        permutation_rows.append({
            "permutation": list(p),
            "cycle_type": list(cycle_type(p)),
            "Q4_matrix": matrix_json(Rq[p]),
            "K5_matrix": matrix_json(Rk[p]),
            "bridge_operator_norm_error": bridge,
        })

    for g in PERMS:
        for h in PERMS:
            gh = compose(g, h)
            max_q4_group_error = max(
                max_q4_group_error,
                float(np.linalg.norm(Rq[g] @ Rq[h] - Rq[gh], 2)),
            )
            max_k5_group_error = max(
                max_k5_group_error,
                float(np.linalg.norm(Rk[g] @ Rk[h] - Rk[gh], 2)),
            )

    expected_character = {
        (1, 1, 1, 1): 2.0,
        (2, 1, 1): 0.0,
        (2, 2): 2.0,
        (3, 1): -1.0,
        (4,): 0.0,
    }
    character_rows = []
    max_character_error = 0.0
    for typ, target in expected_character.items():
        ps = [p for p in PERMS if cycle_type(p) == typ]
        qvals = np.asarray([np.trace(Rq[p]) for p in ps], complex)
        kvals = np.asarray([np.trace(Rk[p]) for p in ps], complex)
        qmean = qvals.mean()
        kmean = kvals.mean()
        err = max(
            float(abs(qmean - target)),
            float(abs(kmean - target)),
            float(np.max(np.abs(qvals - qmean))),
            float(np.max(np.abs(kvals - kmean))),
        )
        max_character_error = max(max_character_error, err)
        character_rows.append({
            "cycle_type": list(typ),
            "class_size": len(ps),
            "expected_[2,2]_character": target,
            "Q4_character_mean": [float(qmean.real), float(qmean.imag)],
            "K5_character_mean": [float(kmean.real), float(kmean.imag)],
            "max_class_error": err,
        })

    Pq = sum(Rq.values()) / len(PERMS)
    Pk = sum(Rk.values()) / len(PERMS)
    q4_trivial_norm = float(np.linalg.norm(Pq, 2))
    k5_trivial_norm = float(np.linalg.norm(Pk, 2))
    projector_bridge_error = float(np.linalg.norm(Pq - Pk, 2))

    Vq = restricted_volume(q4)
    Vk = restricted_volume(k5)
    volume_bridge_error = float(np.linalg.norm(Vq - Vk, 2))
    vscalar = float(np.trace(Vk).real / 2.0)
    volume_scalar_error = float(np.linalg.norm(Vk - vscalar * np.eye(2), 2))
    volume_scale = max(abs(vscalar), 1e-30)
    volume_bridge_relative = volume_bridge_error / volume_scale
    volume_scalar_relative = volume_scalar_error / volume_scale

    checks = {
        "Q4_basis_orthonormal_dimension_two": bool(len(q4) == 2 and np.linalg.norm(Gq - np.eye(2), 2) < TOL),
        "K5_basis_orthonormal_dimension_two": bool(len(k5) == 2 and np.linalg.norm(Gk - np.eye(2), 2) < TOL),
        "raw_basis_overlap_is_identity_without_fit": bool(raw_overlap_error < TOL),
        "all_24_induced_S4_matrices_identical": bool(max_rep_bridge_error < TOL),
        "both_representations_unitary": bool(max(max_q4_unitarity, max_k5_unitarity) < TOL),
        "both_representations_obey_same_group_law": bool(max(max_q4_group_error, max_k5_group_error) < TOL),
        "both_characters_equal_irrep_[2,2]": bool(max_character_error < TOL),
        "both_local_trivial_projectors_vanish": bool(max(q4_trivial_norm, k5_trivial_norm, projector_bridge_error) < TOL),
        "absolute_volume_matrices_match": bool(volume_bridge_relative < TOL),
        "jhalf_absolute_volume_is_scalar_on_[2,2]": bool(volume_scalar_relative < TOL),
    }
    passed = bool(all(checks.values()))

    return {
        "status": "exact local Q4-K5 four-valent carrier compatibility theorem",
        "science_status": "Q4_K5_LOCAL_[2,2]_CARRIER_IDENTICAL" if passed else "Q4_K5_LOCAL_CARRIER_BRIDGE_FAIL",
        "passed": passed,
        "Q4_graph_scope": "16-node Q4 background; only one four-valent local carrier is used here",
        "K5_graph_scope": "five-node K5 4-simplex laboratory; only one four-valent local carrier is used here",
        "global_graph_isomorphism_claimed": False,
        "raw_overlap_Q4_i01_vs_K5_K02": matrix_json(overlap),
        "raw_overlap_operator_norm_error_to_identity": raw_overlap_error,
        "max_S4_representation_bridge_error": max_rep_bridge_error,
        "max_Q4_unitarity_defect": max_q4_unitarity,
        "max_K5_unitarity_defect": max_k5_unitarity,
        "max_Q4_group_law_error": max_q4_group_error,
        "max_K5_group_law_error": max_k5_group_error,
        "character_by_class": character_rows,
        "max_character_error": max_character_error,
        "Q4_trivial_projector_norm": q4_trivial_norm,
        "K5_trivial_projector_norm": k5_trivial_norm,
        "trivial_projector_bridge_error": projector_bridge_error,
        "Q4_absolute_volume_matrix": matrix_json(Vq),
        "K5_absolute_volume_matrix": matrix_json(Vk),
        "absolute_volume_scalar": vscalar,
        "absolute_volume_bridge_relative_error": volume_bridge_relative,
        "absolute_volume_scalar_relative_error": volume_scalar_relative,
        "permutation_rows": permutation_rows,
        "checks": checks,
        "theorem": (
            "With the frozen leg order and without any fitted basis rotation or phase, the explicit Q4 four-spin-1/2 singlet basis (i0,i1) is identical to the canonical K5 Peter-Weyl (K=0,K=2) basis. "
            "All 24 leg permutations therefore realize the same S4 [2,2] matrices and the same local pure-S4-invariant obstruction in both graph contexts."
        ),
        "next_required_bridge": (
            "Construct and preregister an incidence/frame transport layer that embeds a chosen local four-valent Q4 neighbourhood into a K5 tetrahedral constraint patch while keeping global Q4 and K5 graph data distinct. "
            "Only after that layer is explicit may Hamiltonian covariance be tested."
        ),
        "claim_boundary": (
            "Local carrier identity only. Q4 and K5 are not asserted to be globally isomorphic; XOR translations, K5 node permutations, graph-changing Hamiltonian covariance, HDA closure, master-kernel stability and continuum dynamics are not established here."
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
