#!/usr/bin/env python3
"""Exact representation-theory carrier for the first internal Peter-Weyl RG step.

The microscopic logical geometry qubit is the full four-spin j=1/2 singlet
space, which carries the two-dimensional S4 irrep [2,2].  Pairing two fine
face spins symmetrically gives the natural coarse face representation j=1.
The four-j=1 gauge-singlet space has dimension three.  This gate proves that
under face permutations it decomposes with multiplicity one as

    H_singlet(j=1) = [4] + [2,2].

Therefore the renormalized two-dimensional logical geometry sector is selected
by tetrahedral symmetry itself; no fitted projector is needed.  The unique
S4 intertwiner from the j=1/2 logical qubit into this j=1 doublet is then
constructed and checked on all 24 permutations.

All spins are stored doubled, following the repository Peter-Weyl convention.
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


PERMS = tuple(itertools.permutations(range(4)))


def local_basis(s2: int):
    ks = PW.allowed_k2_t(s2, s2, s2, s2)
    ts = [PW.intertwiner_tensor_cached((s2, s2, s2, s2), K) for K in ks]
    return ks, ts


def permutation_matrix(s2: int, perm):
    ks, ts = local_basis(s2)
    U = np.zeros((len(ks), len(ks)), dtype=complex)
    for j, T in enumerate(ts):
        Tp = np.transpose(T, axes=perm)
        for i, S in enumerate(ts):
            U[i, j] = np.vdot(S, Tp)
    return U


def cycle_type(p):
    seen = set(); lengths = []
    for i in range(4):
        if i in seen:
            continue
        j = i; n = 0
        while j not in seen:
            seen.add(j); n += 1; j = p[j]
        lengths.append(n)
    return tuple(sorted(lengths, reverse=True))


def characters(s2: int):
    grouped = {}
    for p in PERMS:
        key = cycle_type(p)
        grouped.setdefault(key, []).append(float(np.trace(permutation_matrix(s2, p)).real))
    return {
        str(k): {
            "class_size": len(v),
            "character_mean": float(np.mean(v)),
            "character_spread": float(np.max(v) - np.min(v)),
        }
        for k, v in sorted(grouped.items())
    }


def volume_matrix_j1():
    ks, ts = local_basis(2)
    V = np.zeros((len(ks), len(ks)), dtype=complex)
    for j, T in enumerate(ts):
        VT = PW.apply_volume_tensor(T, (2, 2, 2, 2))
        for i, S in enumerate(ts):
            V[i, j] = np.vdot(S, VT)
    return (V + V.conj().T) / 2


def run():
    # Fine j=1/2 logical representation: K=0,2 and irreducible [2,2].
    k_half, _ = local_basis(1)
    U_half = {p: permutation_matrix(1, p) for p in PERMS}

    # Coarse j=1 singlet representation: K=0,2,4.
    k_one, _ = local_basis(2)
    U_one = {p: permutation_matrix(2, p) for p in PERMS}
    P_triv = sum(U_one.values()) / len(PERMS)
    P_triv = (P_triv + P_triv.conj().T) / 2

    # In this fixed recoupling convention the exact symmetry-adapted vectors are
    # especially simple in the ordered K=(0,2,4) basis.
    v_triv = np.array([math.sqrt(5) / 3.0, 0.0, 2.0 / 3.0], dtype=complex)
    D = np.column_stack([
        np.array([0.0, 1.0, 0.0], dtype=complex),
        np.array([-2.0 / 3.0, 0.0, math.sqrt(5) / 3.0], dtype=complex),
    ])
    P22 = D @ D.conj().T

    projector_error = float(np.linalg.norm(P_triv - np.outer(v_triv, v_triv.conj())))
    completeness_error = float(np.linalg.norm(P_triv + P22 - np.eye(3)))
    doublet_orth_error = float(np.linalg.norm(D.conj().T @ D - np.eye(2)))

    # The unique multiplicity-one S4 intertwiner, up to an overall phase.  A
    # deterministic phase convention maps fine K=0 to coarse K=2.
    W = np.column_stack([
        np.array([0.0, 1.0, 0.0], dtype=complex),
        np.array([2.0 / 3.0, 0.0, -math.sqrt(5) / 3.0], dtype=complex),
    ])
    intertwining = [np.linalg.norm(U_one[p] @ W - W @ U_half[p]) for p in PERMS]
    isometry_error = float(np.linalg.norm(W.conj().T @ W - np.eye(2)))
    range_error = float(np.linalg.norm(W @ W.conj().T - P22))

    # The full j=1 singlet has nontrivial volume structure; the symmetry-selected
    # [2,2] block itself is scalar, while the trivial singlet is the zero-volume
    # channel.  This is useful: the auxiliary state exists but the renormalized
    # logical carrier remains a qubit.
    V = volume_matrix_j1()
    V_doublet = W.conj().T @ V @ W
    v_doublet = float(np.trace(V_doublet).real / 2.0)
    volume_doublet_scalar_error = float(np.linalg.norm(V_doublet - v_doublet * np.eye(2)))
    volume_trivial = float(np.vdot(v_triv, V @ v_triv).real)
    expected_doublet_volume = 3.0 ** 0.25

    # Expected S4 characters by conjugacy class.
    # cycle types: e=(1,1,1,1), transposition=(2,1,1), double transposition=(2,2),
    # 3-cycle=(3,1), 4-cycle=(4,).
    expected_half = {
        "(1, 1, 1, 1)": 2.0,
        "(2, 1, 1)": 0.0,
        "(2, 2)": 2.0,
        "(3, 1)": -1.0,
        "(4,)": 0.0,
    }
    expected_one = {
        "(1, 1, 1, 1)": 3.0,
        "(2, 1, 1)": 1.0,
        "(2, 2)": 3.0,
        "(3, 1)": 0.0,
        "(4,)": 1.0,
    }
    ch_half = characters(1)
    ch_one = characters(2)
    char_error = max(
        [abs(ch_half[k]["character_mean"] - v) for k, v in expected_half.items()]
        + [abs(ch_one[k]["character_mean"] - v) for k, v in expected_one.items()]
    )

    tol = 2e-12
    passed = (
        tuple(k_half) == (0, 2)
        and tuple(k_one) == (0, 2, 4)
        and char_error < tol
        and projector_error < tol
        and completeness_error < tol
        and doublet_orth_error < tol
        and max(intertwining) < tol
        and isometry_error < tol
        and range_error < tol
        and volume_doublet_scalar_error < 2e-8
        and abs(volume_trivial) < 2e-8
        and abs(v_doublet - expected_doublet_volume) < 2e-8
    )

    return {
        "status": "exact S4 representation carrier for j=1/2 -> j=1 internal Peter-Weyl blocking",
        "passed": bool(passed),
        "fine_face_spin": 0.5,
        "coarse_face_spin": 1.0,
        "fine_singlet_K2_basis": list(k_half),
        "coarse_singlet_K2_basis": list(k_one),
        "fine_S4_irrep": "[2,2]",
        "coarse_S4_decomposition": "[4] direct-sum [2,2]",
        "characters_jhalf": ch_half,
        "characters_j1": ch_one,
        "coarse_trivial_vector_K024": [float(x.real) for x in v_triv],
        "coarse_doublet_basis_K024": [[float(z.real) for z in D[:, i]] for i in range(2)],
        "canonical_intertwiner_W_K024_from_fine_K02": [[float(z.real) for z in row] for row in W],
        "projector_error": projector_error,
        "completeness_error": completeness_error,
        "intertwiner_max_error_all_24_permutations": float(max(intertwining)),
        "isometry_error": isometry_error,
        "range_projector_error": range_error,
        "j1_absolute_volume_matrix_K024": [[float(z.real) for z in row] for row in V],
        "trivial_sector_absolute_volume": volume_trivial,
        "doublet_absolute_volume": v_doublet,
        "expected_doublet_absolute_volume_3_quarter": expected_doublet_volume,
        "doublet_volume_scalar_error": volume_doublet_scalar_error,
        "conclusion": (
            "The first symmetric face-spin growth j=1/2 -> j=1 contains a unique multiplicity-one S4 [2,2] doublet. "
            "It is representation-equivalent to the microscopic logical geometry qubit, giving a symmetry-selected 2D coarse carrier and a unique intertwiner up to phase. "
            "This removes projector freedom from the first nontrivial internal RG step."
        ),
        "next": "recompute the denominator-free higher-shell Lambda with all edges j=1 and P equal to this S4 [2,2]^5 logical carrier, then compare the S4-reduced R_aniso to the j=1/2 value",
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
