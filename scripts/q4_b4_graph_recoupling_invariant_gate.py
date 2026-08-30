#!/usr/bin/env python3
"""Exact B4=(Z2)^4 semidirect S4 graph+recoupling invariant-sector gate.

This extends the local S4 [2,2] recoupling representation to the sixteen Q4
bit-labelled dual nodes. A signed coordinate permutation g=(m,p) acts by

    v -> m XOR p.v

on the 16 node labels and by the same local [2,2] matrix R_p on each local
recoupling carrier. The resulting carrier Hilbert space has dimension 2^16.

Without constructing a 65536 x 65536 dense matrix, the trace of the combined
permutation-tensor action is evaluated through cycle factorization:

    Tr U_(m,p) = product_{cycles c of f_(m,p)} Tr(R_p^|c|).

The [2,2] S4 character is integer-valued, so the primary multiplicity count is
performed with exact integer class arithmetic. Floating recoupling matrices are
retained as an independent scale-aware consistency check rather than being
rounded with an absolute tolerance at characters as large as 2^16.

The gate also constructs an explicit nonzero full-B4 invariant pure vector by
averaging |i0>^tensor16 and verifies invariance under a generating set.

Claim boundary: this is the graph-node + local recoupling carrier only. It does
not yet transform Peter-Weyl edge spins, orientation-dependent Hamiltonian
outputs, or the full physical constraint habitat.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np

import q4_local_s4_singlet_obstruction_gate as LOCAL

TOL = 5e-11


def bit_tuple(v: int) -> tuple[int, int, int, int]:
    return tuple((v >> (3 - i)) & 1 for i in range(4))


def bit_label(bits: tuple[int, ...]) -> int:
    out = 0
    for i, b in enumerate(bits):
        out |= (int(b) & 1) << (3 - i)
    return out


def p_bits(p: tuple[int, ...], bits: tuple[int, ...]) -> tuple[int, ...]:
    # Same leg convention as np.transpose(..., axes=p): new slot i takes old p[i].
    return tuple(bits[p[i]] for i in range(4))


def p_mask(p: tuple[int, ...], mask: int) -> int:
    return bit_label(p_bits(p, bit_tuple(mask)))


def node_map(mask: int, p: tuple[int, ...], v: int) -> int:
    pb = p_bits(p, bit_tuple(v))
    mb = bit_tuple(mask)
    return bit_label(tuple(pb[i] ^ mb[i] for i in range(4)))


def compose_p(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    # p.(q.v) under the frozen axis convention.
    return tuple(q[p[i]] for i in range(4))


def group_product(
    g: tuple[int, tuple[int, ...]], h: tuple[int, tuple[int, ...]]
) -> tuple[int, tuple[int, ...]]:
    m, p = g
    n, q = h
    return m ^ p_mask(p, n), compose_p(p, q)


def cycles(mapping: list[int] | tuple[int, ...]) -> list[int]:
    seen: set[int] = set()
    out: list[int] = []
    for start in range(len(mapping)):
        if start in seen:
            continue
        j = start
        length = 0
        while j not in seen:
            seen.add(j)
            length += 1
            j = mapping[j]
        out.append(length)
    return sorted(out, reverse=True)


def permutation_power(p: tuple[int, ...], power: int) -> tuple[int, ...]:
    """Return p**power for the index-map convention i -> p[i]."""
    out = tuple(range(len(p)))
    for _ in range(power):
        out = tuple(p[out[i]] for i in range(len(p)))
    return out


def s4_22_character(p: tuple[int, ...]) -> int:
    """Exact character of the S4 irrep [2,2], keyed only by cycle type."""
    c = tuple(cycles(p))
    table = {
        (1, 1, 1, 1): 2,
        (2, 1, 1): 0,
        (2, 2): 2,
        (3, 1): -1,
        (4,): 0,
    }
    if c not in table:
        raise AssertionError(f"unexpected S4 cycle type {c} for permutation {p}")
    return table[c]


def kron_power_vec(v: np.ndarray, n: int) -> np.ndarray:
    out = np.asarray([1.0 + 0j])
    for _ in range(n):
        out = np.kron(out, v)
    return out


def site_axis_order(mask: int, p: tuple[int, ...]) -> tuple[int, ...]:
    # output axis new receives input axis old, with new=f(old)
    order = [0] * 16
    for old in range(16):
        new = node_map(mask, p, old)
        order[new] = old
    return tuple(order)


def apply_same_local_matrix(state: np.ndarray, R: np.ndarray) -> np.ndarray:
    T = np.asarray(state, complex).reshape((2,) * 16)
    # Applying R to every tensor factor. Move the contracted output axis back
    # to its original position after each tensordot.
    for axis in range(16):
        T = np.tensordot(R, T, axes=(1, axis))
        T = np.moveaxis(T, 0, axis)
    return T.reshape(-1)


def apply_group(state: np.ndarray, mask: int, p: tuple[int, ...], R: np.ndarray) -> np.ndarray:
    x = apply_same_local_matrix(state, R).reshape((2,) * 16)
    return np.transpose(x, axes=site_axis_order(mask, p)).reshape(-1)


def reduced_one_site(state: np.ndarray, site: int = 0) -> np.ndarray:
    T = np.asarray(state, complex).reshape((2,) * 16)
    A = np.moveaxis(T, site, 0).reshape(2, -1)
    return A @ A.conj().T


def run() -> dict[str, object]:
    local_basis = LOCAL.singlet_basis()
    perms = tuple(itertools.permutations(range(4)))
    reps = {p: LOCAL.rep_matrix(local_basis, p)[0] for p in perms}
    elements = tuple((m, p) for m in range(16) for p in perms)

    # Structural semidirect-product closure and node-action homomorphism.
    max_node_group_error = 0
    max_local_group_error = 0.0
    for g in elements:
        m, p = g
        for h in elements:
            n, q = h
            gh = group_product(g, h)
            for v in range(16):
                lhs = node_map(m, p, node_map(n, q, v))
                rhs = node_map(gh[0], gh[1], v)
                if lhs != rhs:
                    max_node_group_error = 1
                    break
            max_local_group_error = max(
                max_local_group_error,
                float(np.linalg.norm(reps[p] @ reps[q] - reps[gh[1]], 2)),
            )

    # Exact character arithmetic gives the theorem-level multiplicity. The
    # floating matrices provide a separate numerical consistency diagnostic.
    character_rows = []
    exact_char_sum = 0
    numerical_char_sum = 0.0 + 0j
    max_numeric_character_scaled_error = 0.0
    max_numeric_character_absolute_error = 0.0
    cycle_counter: dict[str, int] = {}
    for mask, p in elements:
        mapping = [node_map(mask, p, v) for v in range(16)]
        cyc = cycles(mapping)
        R = reps[p]

        exact_ch = 1
        numeric_ch = 1.0 + 0j
        for L in cyc:
            exact_ch *= s4_22_character(permutation_power(p, L))
            numeric_ch *= np.trace(np.linalg.matrix_power(R, L))

        exact_char_sum += exact_ch
        numerical_char_sum += numeric_ch
        abs_err = float(abs(numeric_ch - exact_ch))
        scaled_err = abs_err / max(1.0, abs(float(exact_ch)))
        max_numeric_character_absolute_error = max(max_numeric_character_absolute_error, abs_err)
        max_numeric_character_scaled_error = max(max_numeric_character_scaled_error, scaled_err)

        key = str(tuple(cyc))
        cycle_counter[key] = cycle_counter.get(key, 0) + 1
        character_rows.append({
            "mask": mask,
            "permutation": list(p),
            "node_cycle_lengths": cyc,
            "exact_character": exact_ch,
            "numerical_character": [float(numeric_ch.real), float(numeric_ch.imag)],
            "numerical_scaled_error": scaled_err,
        })

    multiplicity_divisible = exact_char_sum % len(elements) == 0
    multiplicity = exact_char_sum // len(elements) if multiplicity_divisible else -1
    numerical_multiplicity = numerical_char_sum / len(elements)
    numerical_multiplicity_error = float(abs(numerical_multiplicity - multiplicity))

    # Full group average of the uniform |i0>^16 seed. XOR node permutations do
    # nothing to every term in this uniform orbit, so the 384-element average
    # equals the 24-element S4 average below, but the resulting vector is then
    # verified against generators of both subgroups.
    e0 = np.asarray([1.0, 0.0], complex)
    seed = kron_power_vec(e0, 16)
    avg = np.zeros_like(seed)
    for p in perms:
        avg += kron_power_vec(reps[p] @ e0, 16)
    avg /= len(perms)
    avg_norm2 = float(np.vdot(avg, avg).real)
    psi = avg / math.sqrt(avg_norm2)

    identity = tuple(range(4))
    adjacent_swaps = (
        (1, 0, 2, 3),
        (0, 2, 1, 3),
        (0, 1, 3, 2),
    )
    generator_rows = []
    max_generator_defect = 0.0
    for mask in (1, 2, 4, 8):
        y = apply_group(psi, mask, identity, reps[identity])
        err = float(np.linalg.norm(y - psi))
        max_generator_defect = max(max_generator_defect, err)
        generator_rows.append({"kind": "XOR", "mask": mask, "defect": err})
    for p in adjacent_swaps:
        y = apply_group(psi, 0, p, reps[p])
        err = float(np.linalg.norm(y - psi))
        max_generator_defect = max(max_generator_defect, err)
        generator_rows.append({"kind": "S4_adjacent_swap", "permutation": list(p), "defect": err})

    rho0 = reduced_one_site(psi, 0)
    rho0_err = float(np.linalg.norm(rho0 - 0.5 * np.eye(2), 2))
    ev_rho = np.linalg.eigvalsh(0.5 * (rho0 + rho0.conj().T))
    entropy = float(-sum(x * math.log2(x) for x in ev_rho if x > 1e-15))

    # Independent closed-form norm for this particular uniform seed orbit.
    expected_uniform_norm2 = 10923.0 / 32768.0
    norm2_error = abs(avg_norm2 - expected_uniform_norm2)

    checks = {
        "group_has_384_elements": len(elements) == 384,
        "node_action_semidirect_group_law": max_node_group_error == 0,
        "local_recoupling_group_law_compatible": max_local_group_error < TOL,
        "exact_character_sum_divisible_by_group_order": multiplicity_divisible,
        "numerical_characters_match_exact_scale_aware": max_numeric_character_scaled_error < TOL,
        "numerical_character_average_matches_exact_multiplicity": numerical_multiplicity_error < TOL,
        "full_graph_recoupling_trivial_multiplicity_is_243": multiplicity == 243,
        "uniform_seed_group_average_nonzero": avg_norm2 > 1e-8,
        "uniform_seed_projector_norm_matches_closed_value": norm2_error < TOL,
        "explicit_state_invariant_under_B4_generators": max_generator_defect < 2e-10,
        "explicit_state_local_reduced_density_is_I_over_2": rho0_err < 2e-10,
        "explicit_state_one_site_entropy_is_one_bit": abs(entropy - 1.0) < 2e-10,
    }
    passed = bool(all(checks.values()))

    return {
        "status": "exact B4 graph-node plus local recoupling invariant-sector diagnostic",
        "science_status": "Q4_B4_GRAPH_RECOUPLING_INVARIANT_SECTOR_DIMENSION_243" if passed else "Q4_B4_GRAPH_RECOUPLING_GATE_FAIL",
        "passed": passed,
        "group": "B4=(Z2)^4 semidirect S4 signed coordinate permutations",
        "group_order": len(elements),
        "carrier_hilbert_dimension": 2 ** 16,
        "local_recoupling_irrep": "S4 [2,2]",
        "trivial_sector_multiplicity": multiplicity,
        "trivial_sector_fraction": multiplicity / float(2 ** 16) if multiplicity >= 0 else None,
        "exact_character_sum": exact_char_sum,
        "numerical_character_average": [float(numerical_multiplicity.real), float(numerical_multiplicity.imag)],
        "numerical_character_average_error": numerical_multiplicity_error,
        "max_numeric_character_absolute_error": max_numeric_character_absolute_error,
        "max_numeric_character_scaled_error": max_numeric_character_scaled_error,
        "max_local_group_law_error": max_local_group_error,
        "node_group_law_error_flag": max_node_group_error,
        "node_cycle_structure_counts": cycle_counter,
        "explicit_uniform_seed_group_average_norm2": avg_norm2,
        "explicit_uniform_seed_expected_norm2": expected_uniform_norm2,
        "explicit_state_max_generator_invariance_defect": max_generator_defect,
        "explicit_state_generator_rows": generator_rows,
        "explicit_state_site0_reduced_density": [[[float(z.real), float(z.imag)] for z in row] for row in rho0],
        "explicit_state_site0_entropy_bits": entropy,
        "checks": checks,
        "interpretation": (
            "Including node permutations reduces the diagonal-local S4 invariant multiplicity from 10923 to a 243-dimensional invariant sector in the 2^16 recoupling-carrier space. "
            "A nonzero globally pure invariant state exists and is locally maximally mixed."
        ),
        "next_required_extension": (
            "Lift the same signed-permutation action to the actual Peter-Weyl edge-spin/K labels and graph-changing Hamiltonian image states, then test U_g H_v U_g^{-1} against the appropriately transported node constraint including orientation character."
        ),
        "claim_boundary": (
            "Exact graph-node + local recoupling representation result only. Edge-spin transport, graph-changing output support, orientation-sensitive Hamiltonian covariance, physical constraint kernel, refinement and continuum history are not established by this gate."
        ),
        "character_rows": character_rows,
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
