#!/usr/bin/env python3
"""Exact S5 automorphism representation on the 32D fully-active K5 carrier.

Implements K5_S5_CARRIER_SYMMETRY_PREREGISTRATION.md.  The five local
four-valent j=1/2 Gauss-singlet carriers are transported under every K5 vertex
permutation by the induced permutation of their four ordered legs.  No fitted
basis transformation or target-state phase is used.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import numpy as np

from five_tetrahedron_vertex_gate import vertex_tensor

TOL = 3e-12
PERMS5 = tuple(itertools.permutations(range(5)))


def local_basis() -> list[np.ndarray]:
    z = np.asarray([1.0, 0.0], complex)
    o = np.asarray([0.0, 1.0], complex)
    s = (np.kron(z, o) - np.kron(o, z)) / np.sqrt(2.0)
    i0 = np.kron(s, s).reshape(2, 2, 2, 2)
    tp = np.kron(z, z)
    t0 = (np.kron(z, o) + np.kron(o, z)) / np.sqrt(2.0)
    tm = np.kron(o, o)
    i1 = (np.kron(tp, tm) - np.kron(t0, t0) + np.kron(tm, tp)).reshape(2, 2, 2, 2) / np.sqrt(3.0)
    return [i0, i1]


LOCAL = local_basis()


def local_rep(p: tuple[int, ...]) -> np.ndarray:
    return np.asarray(
        [[np.vdot(a, np.transpose(b, axes=p)) for b in LOCAL] for a in LOCAL],
        complex,
    )


def compose(g: tuple[int, ...], h: tuple[int, ...]) -> tuple[int, ...]:
    """Apply h first and then g on K5 vertex labels."""
    return tuple(g[h[v]] for v in range(5))


def inverse(g: tuple[int, ...]) -> tuple[int, ...]:
    q = [0] * 5
    for v, w in enumerate(g):
        q[w] = v
    return tuple(q)


def parity(g: tuple[int, ...]) -> int:
    return -1 if sum(g[i] > g[j] for i in range(5) for j in range(i + 1, 5)) % 2 else 1


def cycle_type(g: tuple[int, ...]) -> tuple[int, ...]:
    seen: set[int] = set()
    out: list[int] = []
    for start in range(5):
        if start in seen:
            continue
        j = start
        n = 0
        while j not in seen:
            seen.add(j)
            n += 1
            j = g[j]
        out.append(n)
    return tuple(sorted(out, reverse=True))


def induced_local_axis_perm(g: tuple[int, ...], v: int) -> tuple[int, ...]:
    old_neigh = [w for w in range(5) if w != v]
    new_v = g[v]
    new_neigh = [w for w in range(5) if w != new_v]
    inv = inverse(g)
    # New local slot n' receives the old slot attached to g^{-1}(n').
    return tuple(old_neigh.index(inv[nnew]) for nnew in new_neigh)


def bit_index(bits: tuple[int, ...]) -> int:
    return int(np.ravel_multi_index(bits, (2, 2, 2, 2, 2)))


def global_rep(g: tuple[int, ...]) -> np.ndarray:
    local = {v: local_rep(induced_local_axis_perm(g, v)) for v in range(5)}
    U = np.zeros((32, 32), complex)
    for old_bits in itertools.product((0, 1), repeat=5):
        col = bit_index(old_bits)
        for new_bits in itertools.product((0, 1), repeat=5):
            amp = 1.0 + 0j
            for v in range(5):
                amp *= local[v][new_bits[g[v]], old_bits[v]]
            if abs(amp) > 1e-15:
                U[bit_index(new_bits), col] = amp
    return U


def matrix_rank_projector(P: np.ndarray) -> int:
    ev = np.linalg.eigvalsh(0.5 * (P + P.conj().T))
    return int(np.sum(ev > 0.5))


def run() -> dict[str, object]:
    U = {g: global_rep(g) for g in PERMS5}
    identity = tuple(range(5))
    I32 = np.eye(32)

    max_unitarity = max(float(np.linalg.norm(M.conj().T @ M - I32, 2)) for M in U.values())
    identity_error = float(np.linalg.norm(U[identity] - I32, 2))

    generators = (
        (1, 0, 2, 3, 4),
        (0, 2, 1, 3, 4),
        (0, 1, 3, 2, 4),
        (0, 1, 2, 4, 3),
    )
    max_generator_composition_error = 0.0
    for g in PERMS5:
        for s in generators:
            max_generator_composition_error = max(
                max_generator_composition_error,
                float(np.linalg.norm(U[s] @ U[g] - U[compose(s, g)], 2)),
                float(np.linalg.norm(U[g] @ U[s] - U[compose(g, s)], 2)),
            )

    coxeter_errors = []
    for i, s in enumerate(generators):
        coxeter_errors.append(float(np.linalg.norm(U[s] @ U[s] - I32, 2)))
        for j, t in enumerate(generators):
            if abs(i - j) > 1:
                coxeter_errors.append(float(np.linalg.norm(U[s] @ U[t] - U[t] @ U[s], 2)))
        if i + 1 < len(generators):
            t = generators[i + 1]
            coxeter_errors.append(float(np.linalg.norm(U[s] @ U[t] @ U[s] - U[t] @ U[s] @ U[t], 2)))
    max_coxeter_error = max(coxeter_errors)

    expected_char = {
        (1, 1, 1, 1, 1): 32.0,
        (2, 1, 1, 1): 0.0,
        (2, 2, 1): 8.0,
        (3, 1, 1): 2.0,
        (3, 2): 0.0,
        (4, 1): 0.0,
        (5,): 2.0,
    }
    character_rows = []
    max_character_error = 0.0
    for typ, target in expected_char.items():
        gs = [g for g in PERMS5 if cycle_type(g) == typ]
        vals = np.asarray([np.trace(U[g]) for g in gs], complex)
        mean = vals.mean()
        spread = float(np.max(np.abs(vals - mean)))
        err = max(spread, float(abs(mean - target)))
        max_character_error = max(max_character_error, err)
        character_rows.append({
            "cycle_type": list(typ),
            "class_size": len(gs),
            "character_mean": [float(mean.real), float(mean.imag)],
            "expected_character": target,
            "max_error": err,
        })

    char_sum = sum(np.trace(U[g]) for g in PERMS5)
    sign_char_sum = sum(parity(g) * np.trace(U[g]) for g in PERMS5)
    trivial_mult = float((char_sum / 120.0).real)
    alternating_mult = float((sign_char_sum / 120.0).real)

    P_triv = sum(U.values()) / 120.0
    P_alt = sum(parity(g) * U[g] for g in PERMS5) / 120.0
    triv_rank = matrix_rank_projector(P_triv)
    alt_rank = matrix_rank_projector(P_alt)
    projector_herm = max(
        float(np.linalg.norm(P_triv - P_triv.conj().T, 2)),
        float(np.linalg.norm(P_alt - P_alt.conj().T, 2)),
    )
    projector_idem = max(
        float(np.linalg.norm(P_triv @ P_triv - P_triv, 2)),
        float(np.linalg.norm(P_alt @ P_alt - P_alt, 2)),
    )
    projector_orth = float(np.linalg.norm(P_triv @ P_alt, 2))

    V = np.asarray(vertex_tensor(), complex).reshape(-1)
    V /= np.linalg.norm(V)
    max_vertex_alternating_defect = max(float(np.linalg.norm(U[g] @ V - parity(g) * V)) for g in PERMS5)
    vertex_alt_projector_error = float(np.linalg.norm(P_alt @ V - V))
    vertex_trivial_projection_norm = float(np.linalg.norm(P_triv @ V))

    # Explicitly expose the second independent alternating direction; this is
    # a diagnostic proving that symmetry does not uniquely select V5.
    ev, vec = np.linalg.eigh(0.5 * (P_alt + P_alt.conj().T))
    Qalt = vec[:, ev > 0.5]
    coeff = Qalt.conj().T @ V
    second = Qalt.copy()
    # Kernel of <V| inside the rank-two alternating space.
    if Qalt.shape[1] == 2:
        c = coeff / max(np.linalg.norm(coeff), 1e-30)
        orth_coeff = np.asarray([-np.conj(c[1]), np.conj(c[0])], complex)
        V2 = Qalt @ orth_coeff
        V2 /= np.linalg.norm(V2)
        second_alt_overlap_with_V = float(abs(np.vdot(V, V2)))
        second_alt_projector_error = float(np.linalg.norm(P_alt @ V2 - V2))
    else:
        second_alt_overlap_with_V = float("nan")
        second_alt_projector_error = float("nan")

    checks = {
        "all_120_S5_actions_unitary": bool(max_unitarity < TOL),
        "identity_is_I32": bool(identity_error < TOL),
        "generator_composition_matches_group_product_for_all_elements": bool(max_generator_composition_error < TOL),
        "adjacent_generators_obey_S5_Coxeter_relations": bool(max_coxeter_error < TOL),
        "characters_match_preregistered_class_values": bool(max_character_error < TOL),
        "trivial_multiplicity_is_two": bool(abs(trivial_mult - 2.0) < TOL),
        "alternating_multiplicity_is_two": bool(abs(alternating_mult - 2.0) < TOL),
        "trivial_and_alternating_projectors_are_rank_two": bool(triv_rank == 2 and alt_rank == 2),
        "sector_projectors_are_Hermitian_idempotent_orthogonal": bool(max(projector_herm, projector_idem, projector_orth) < TOL),
        "five_tetrahedron_vertex_transforms_as_orientation_sign": bool(max_vertex_alternating_defect < TOL),
        "five_tetrahedron_vertex_is_in_alternating_not_trivial_sector": bool(vertex_alt_projector_error < TOL and vertex_trivial_projection_norm < TOL),
        "second_independent_alternating_direction_exists": bool(alt_rank == 2 and second_alt_overlap_with_V < TOL and second_alt_projector_error < TOL),
    }
    passed = bool(all(checks.values()))

    return {
        "status": "exact S5 automorphism representation on the K5 fully-active j=1/2 recoupling carrier",
        "science_status": "K5_S5_CARRIER_EXACT_V5_ALTERNATING_NONUNIQUE" if passed else "K5_S5_CARRIER_GATE_FAIL",
        "passed": passed,
        "carrier_dimension": 32,
        "group_order": 120,
        "max_unitarity_defect": max_unitarity,
        "identity_error": identity_error,
        "max_generator_composition_error": max_generator_composition_error,
        "max_Coxeter_relation_error": max_coxeter_error,
        "character_by_class": character_rows,
        "max_character_error": max_character_error,
        "trivial_multiplicity": trivial_mult,
        "alternating_multiplicity": alternating_mult,
        "trivial_projector_rank": triv_rank,
        "alternating_projector_rank": alt_rank,
        "projector_Hermiticity_error": projector_herm,
        "projector_idempotence_error": projector_idem,
        "trivial_alternating_projector_overlap_norm": projector_orth,
        "V5_max_alternating_transformation_defect": max_vertex_alternating_defect,
        "V5_alternating_projector_error": vertex_alt_projector_error,
        "V5_trivial_projection_norm": vertex_trivial_projection_norm,
        "second_alternating_direction_overlap_with_V5": second_alt_overlap_with_V,
        "second_alternating_direction_projector_error": second_alt_projector_error,
        "checks": checks,
        "interpretation": (
            "The fully-active K5 carrier has an exact S5 automorphism representation. The independent oriented five-tetrahedron vertex is an alternating/pseudoscalar state under odd vertex permutations, not a trivial scalar. "
            "Because the alternating irrep occurs twice, automorphism symmetry alone does not uniquely select V5; additional shape/constraint dynamics are mathematically necessary for uniqueness."
        ),
        "next_required_gate": (
            "Lift the S5 action from the fixed all-j=1/2 carrier to general graph-changing Peter-Weyl state keys, including edge-spin relabelling and local recoupling transport, then directly test covariance of the safe Jmax=5/2 Hamiltonian images."
        ),
        "claim_boundary": (
            "Finite 32D carrier theorem only. It does not establish graph-changing Hamiltonian covariance, HDA closure, uniqueness of V5, Q4-K5 global equivalence, a physical projector or continuum dynamics."
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
