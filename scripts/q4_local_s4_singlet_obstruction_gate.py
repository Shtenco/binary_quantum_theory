#!/usr/bin/env python3
"""Exact local S4 obstruction for a pure four-spin-1/2 Gauss singlet.

The two-dimensional four-qubit SU(2)-singlet sector carries the irreducible
S4 representation [2,2], not the trivial representation.  Consequently no
nonzero local pure singlet vector can be invariant under every leg
permutation.  This matters for interpreting raw Q4/Hamming-distance covariance
checks built from a fixed K=0 recoupling seed.

The gate constructs the standard K=0/K=1 singlet basis directly in magnetic
space, derives all 24 leg-permutation matrices by overlap, verifies the exact
representation law, reproduces the [2,2] character table on S4 conjugacy
classes, and checks that the full group-average projector vanishes on this
sector.  It also verifies that twirling a generic pure density matrix gives
I/2, as required by Schur's lemma for an irreducible unitary representation.

This is a representation-theoretic diagnostic only.  It does not assert that
the physical background must be mixed: global entanglement between local
[2,2] sectors can still contain an S4 singlet and must be tested separately.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import numpy as np

TOL = 2e-12


def parity(p: tuple[int, ...]) -> int:
    return -1 if sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) % 2 else 1


def compose(g: tuple[int, ...], h: tuple[int, ...]) -> tuple[int, ...]:
    """Permutation corresponding to applying h first, then g, for transpose axes."""
    # np.transpose(np.transpose(T, h), g) = np.transpose(T, tuple(h[g[i]] ...))
    return tuple(h[g[i]] for i in range(4))


def inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    q = [0] * 4
    for i, x in enumerate(p):
        q[x] = i
    return tuple(q)


def cycle_type(p: tuple[int, ...]) -> tuple[int, ...]:
    seen = [False] * 4
    cycles: list[int] = []
    for i in range(4):
        if seen[i]:
            continue
        j = i
        length = 0
        while not seen[j]:
            seen[j] = True
            length += 1
            j = p[j]
        cycles.append(length)
    return tuple(sorted(cycles, reverse=True))


def singlet_basis() -> list[np.ndarray]:
    z = np.asarray([1.0, 0.0], complex)
    o = np.asarray([0.0, 1.0], complex)
    s = (np.kron(z, o) - np.kron(o, z)) / np.sqrt(2.0)
    i0 = np.kron(s, s).reshape(2, 2, 2, 2)

    tp = np.kron(z, z)
    t0 = (np.kron(z, o) + np.kron(o, z)) / np.sqrt(2.0)
    tm = np.kron(o, o)
    i1 = (np.kron(tp, tm) - np.kron(t0, t0) + np.kron(tm, tp)) / np.sqrt(3.0)
    i1 = i1.reshape(2, 2, 2, 2)
    return [i0, i1]


def rep_matrix(basis: list[np.ndarray], p: tuple[int, ...]) -> tuple[np.ndarray, float]:
    R = np.asarray(
        [[np.vdot(A, np.transpose(B, axes=p)) for B in basis] for A in basis],
        complex,
    )
    worst = 0.0
    for j, B in enumerate(basis):
        target = np.transpose(B, axes=p)
        recon = sum((R[i, j] * basis[i] for i in range(2)), np.zeros_like(target))
        worst = max(worst, float(np.linalg.norm(target - recon)))
    return R, worst


def matrix_json(M: np.ndarray) -> list[list[list[float]]]:
    return [[[float(z.real), float(z.imag)] for z in row] for row in np.asarray(M, complex)]


def run() -> dict[str, object]:
    basis = singlet_basis()
    gram = np.asarray([[np.vdot(A, B) for B in basis] for A in basis], complex)
    perms = tuple(itertools.permutations(range(4)))

    reps: dict[tuple[int, ...], np.ndarray] = {}
    rows = []
    max_sector_leak = 0.0
    max_unitarity = 0.0
    for p in perms:
        R, leak = rep_matrix(basis, p)
        reps[p] = R
        max_sector_leak = max(max_sector_leak, leak)
        unit = float(np.linalg.norm(R.conj().T @ R - np.eye(2), 2))
        max_unitarity = max(max_unitarity, unit)
        rows.append({
            "permutation": list(p),
            "cycle_type": list(cycle_type(p)),
            "parity": parity(p),
            "trace": [float(np.trace(R).real), float(np.trace(R).imag)],
            "determinant": [float(np.linalg.det(R).real), float(np.linalg.det(R).imag)],
            "unitarity_defect": unit,
            "singlet_sector_leakage": leak,
            "matrix": matrix_json(R),
        })

    max_group_error = 0.0
    max_inverse_error = 0.0
    for g in perms:
        for h in perms:
            gh = compose(g, h)
            # With the transpose convention above, R_g R_h corresponds to
            # transpose by compose(g,h) as defined.
            max_group_error = max(
                max_group_error,
                float(np.linalg.norm(reps[g] @ reps[h] - reps[gh], 2)),
            )
        max_inverse_error = max(
            max_inverse_error,
            float(np.linalg.norm(reps[inverse(g)] @ reps[g] - np.eye(2), 2)),
        )

    by_class: dict[tuple[int, ...], list[complex]] = {}
    for p in perms:
        by_class.setdefault(cycle_type(p), []).append(np.trace(reps[p]))

    expected_character = {
        (1, 1, 1, 1): 2.0,
        (2, 1, 1): 0.0,
        (3, 1): -1.0,
        (2, 2): 2.0,
        (4,): 0.0,
    }
    class_rows = []
    max_character_error = 0.0
    for typ in sorted(by_class, reverse=True):
        vals = np.asarray(by_class[typ], complex)
        mean = vals.mean()
        spread = float(np.max(np.abs(vals - mean)))
        target = expected_character[typ]
        err = float(abs(mean - target))
        max_character_error = max(max_character_error, spread, err)
        class_rows.append({
            "cycle_type": list(typ),
            "class_size": len(vals),
            "character_mean": [float(mean.real), float(mean.imag)],
            "within_class_spread": spread,
            "expected_[2,2]_character": target,
            "absolute_error": err,
        })

    P_trivial = sum(reps.values()) / len(perms)
    trivial_projector_norm = float(np.linalg.norm(P_trivial, 2))
    trivial_projector_eigenvalues = np.linalg.eigvalsh(0.5 * (P_trivial + P_trivial.conj().T))

    # Generic pure state deliberately not aligned with either recoupling axis.
    psi = np.asarray([1.0, np.exp(0.37j)], complex)
    psi /= np.linalg.norm(psi)
    rho = np.outer(psi, psi.conj())
    rho_twirl = sum(R @ rho @ R.conj().T for R in reps.values()) / len(perms)
    twirl_target = 0.5 * np.eye(2)
    twirl_error = float(np.linalg.norm(rho_twirl - twirl_target, 2))

    # Search for a common invariant vector via stacked (R-I).  The smallest
    # singular value must be strictly nonzero at numerical precision.
    stacked = np.vstack([R - np.eye(2) for R in reps.values()])
    invariant_singular_values = np.linalg.svd(stacked, compute_uv=False)
    invariant_nullity = int(np.sum(invariant_singular_values < 1e-10))
    min_invariance_penalty = float(invariant_singular_values[-1])

    checks = {
        "singlet_basis_orthonormal": bool(np.linalg.norm(gram - np.eye(2), 2) < TOL),
        "all_24_permutations_present": len(perms) == 24,
        "singlet_sector_closed_under_S4": max_sector_leak < TOL,
        "representation_unitary": max_unitarity < TOL,
        "representation_group_law": max_group_error < TOL,
        "inverse_roundtrip": max_inverse_error < TOL,
        "character_matches_irrep_[2,2]": max_character_error < TOL,
        "full_S4_trivial_projector_vanishes": trivial_projector_norm < TOL,
        "no_nonzero_common_invariant_vector": invariant_nullity == 0 and min_invariance_penalty > 1e-6,
        "generic_pure_density_twirl_is_I_over_2": twirl_error < TOL,
    }
    passed = bool(all(checks.values()))

    return {
        "status": "exact local S4 representation obstruction for a pure four-spin-1/2 Gauss singlet",
        "science_status": "LOCAL_PURE_S4_INVARIANT_SINGLET_OBSTRUCTED" if passed else "S4_REPRESENTATION_DIAGNOSTIC_FAIL",
        "passed": passed,
        "singlet_dimension": 2,
        "representation_irrep": "S4 [2,2]",
        "character_by_conjugacy_class": class_rows,
        "maximum_sector_leakage": max_sector_leak,
        "maximum_unitarity_defect": max_unitarity,
        "maximum_group_law_error": max_group_error,
        "maximum_inverse_roundtrip_error": max_inverse_error,
        "trivial_group_average_projector_norm": trivial_projector_norm,
        "trivial_group_average_projector_eigenvalues": [float(x) for x in trivial_projector_eigenvalues],
        "invariant_vector_stacked_singular_values": [float(x) for x in invariant_singular_values],
        "invariant_subspace_dimension": invariant_nullity,
        "generic_pure_density_S4_twirl_error_to_I_over_2": twirl_error,
        "checks": checks,
        "permutation_rows": rows,
        "consequence_for_Q4_diagnostics": (
            "A fixed local K=0 pure singlet chooses a recoupling direction inside the irreducible [2,2] sector. "
            "Therefore equality of raw node-column overlaps for every pair at the same Hamming distance is a stronger assumption than XOR translation covariance and is not implied by local Gauss invariance."
        ),
        "allowed_next_routes": (
            "Test operator covariance with explicit S4 recoupling matrices; or construct an S4-covariant density/background ensemble; "
            "or search for a globally entangled S4-invariant state across multiple local [2,2] sectors."
        ),
        "claim_boundary": (
            "This is a local representation-theory obstruction only. It does not prove physical anisotropy, does not require nature to use a mixed state, "
            "and does not decide whether the full multi-node BCQG background has a global S4-invariant pure sector."
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
