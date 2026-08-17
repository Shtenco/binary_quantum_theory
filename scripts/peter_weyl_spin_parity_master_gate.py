#!/usr/bin/env python3
"""Exact support grading + two-shell master-constraint control for Euclidean Peter-Weyl H_E.

This gate proves/checks three sharply separated statements.

(1) Every primitive Euclidean T-sequence in the existing K5 implementation has
    an odd number of fundamental path hits (five) and flips exactly three edge
    spin-parity bits. Therefore the doubled-spin grading

        Pi |{s_e}> = (-1)^(sum_e s_e) |{s_e}>,  s_e=2j_e,

    anticommutes with H_E at support level: {Pi,H_E}=0.

(2) For P H_E P=0 and A=Q H_E P, the minimal two-shell master resolvent with
    M_Q=AA^dagger gives

        A^dagger(AA^dagger+mu^2 I)^-1 A
        = K(K+mu^2 I)^-1, K=A^dagger A,

    which tends to identity on full-rank P as mu->0. Raw return-amplitude
    anisotropy therefore does not by itself survive this normalization.

(3) With the parity-compatible next even shell R and C=R H_E Q,

        P H_E^4 P - K^2 = A^dagger C^dagger C A >= 0.

    The normalized higher-shell leakage matrix

        Lambda=K^-1/2 (P H_E^4 P-K^2) K^-1/2

    is the next denominator-free positive observable. This gate checks the block
    identity on a generic finite matrix control; it does NOT compute Lambda for
    the full Peter-Weyl dynamics yet.
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

CANONICAL_COEFF = {
    "II": 9.04524203998966,
    "IX": +0.08054446950018196,
    "IZ": +0.04650237114766842,
    "XI": +0.08054446950018226,
    "ZI": +0.04650237114766753,
    "XX": +0.45691119919191336,
    "YY": +2.18199564892363,
    "ZZ": +0.6560148247263502,
    "XZ": -0.17242879769840605,
    "ZX": -0.17242879769840608,
}


def path_signature(seq):
    parity = {e: 0 for e in PW.EDGES}
    hits = 0
    for op in seq:
        if op[0] != "P":
            continue
        path = tuple(op[1])
        for x, y in zip(path[:-1], path[1:]):
            e = tuple(sorted((x, y)))
            parity[e] ^= 1
            hits += 1
    odd_edges = tuple(sorted(e for e, p in parity.items() if p))
    return hits, odd_edges


def support_grading_audit():
    rows = []
    all_ok = True
    for v in PW.VERT:
        for sign, spec in PW.oriented_specs(v):
            for coef, seq in PW.T_sequences(*spec):
                hits, odd = path_signature(seq)
                ahits, aodd = path_signature(PW.adjoint_sequence(seq))
                ok = (hits % 2 == 1 and hits == 5 and len(odd) == 3 and ahits == hits and aodd == odd)
                all_ok &= ok
                rows.append({
                    "node": v,
                    "spec": list(spec),
                    "orientation_sign": sign,
                    "sequence_coefficient": coef,
                    "fundamental_segment_hits": hits,
                    "odd_edge_count": len(odd),
                    "odd_edges": [list(e) for e in odd],
                    "adjoint_same_signature": bool(ahits == hits and aodd == odd),
                    "passed": bool(ok),
                })
    return {
        "passed": bool(all_ok),
        "sequence_count": len(rows),
        "all_sequences_have_five_hits": all(r["fundamental_segment_hits"] == 5 for r in rows),
        "all_sequences_flip_three_edge_parities": all(r["odd_edge_count"] == 3 for r in rows),
        "all_adjoint_signatures_match": all(r["adjoint_same_signature"] for r in rows),
        "grading": "Pi=(-1)^(sum_e 2j_e)",
        "conclusion": "Every primitive H_E sequence flips Pi, hence {Pi,H_E}=0 at support level.",
    }


def canonical_K():
    K = np.zeros((4, 4), dtype=complex)
    for lab, c in CANONICAL_COEFF.items():
        K += c * np.kron(PAULI[lab[0]], PAULI[lab[1]])
    return (K + K.conj().T) / 2


def pauli_coeff(K):
    out = {}
    for a, A in PAULI.items():
        for b, B in PAULI.items():
            out[a + b] = np.trace(np.kron(A, B) @ K) / 4.0
    return out


def delta_aniso(K):
    c = pauli_coeff(K)
    return float((c["YY"] + 0.5 * (c["XX"] + c["ZZ"])).real)


def two_shell_master_control():
    K = canonical_K()
    ev, U = np.linalg.eigh(K)
    sqrtK = (U * np.sqrt(ev)) @ U.conj().T

    rng = np.random.default_rng(20260814)
    X = rng.normal(size=(7, 4)) + 1j * rng.normal(size=(7, 4))
    Qiso, _ = np.linalg.qr(X)
    A = Qiso[:, :4] @ sqrtK

    K_from_A = A.conj().T @ A
    k_error = float(np.linalg.norm(K_from_A - K))

    mu_rows = []
    identity_errors = []
    for mu in (3.0, 1.0, 0.3, 0.1, 0.03, 0.01, 0.003, 0.001):
        left = A.conj().T @ np.linalg.inv(A @ A.conj().T + (mu * mu) * np.eye(A.shape[0])) @ A
        right = K @ np.linalg.inv(K + (mu * mu) * np.eye(4))
        identity_err = float(np.linalg.norm(left - right))
        identity_errors.append(identity_err)
        c = pauli_coeff(right)
        c0 = float(c["II"].real)
        d = delta_aniso(right)
        mu_rows.append({
            "mu": mu,
            "matrix_identity_error": identity_err,
            "distance_to_identity": float(np.linalg.norm(right - np.eye(4))),
            "Delta_aniso": d,
            "II": c0,
            "Delta_over_II": d / c0,
        })

    invK_delta = delta_aniso(np.linalg.inv(K))
    return {
        "passed": bool(
            np.min(ev) > 1e-10
            and k_error < 1e-10
            and max(identity_errors) < 1e-9
            and mu_rows[-1]["distance_to_identity"] < 1e-6
            and abs(mu_rows[-1]["Delta_over_II"]) < 1e-6
        ),
        "canonical_K_eigenvalues": [float(x) for x in ev],
        "canonical_K_condition_number": float(np.max(ev) / np.min(ev)),
        "A_dagger_A_reconstruction_error": k_error,
        "mu_scan": mu_rows,
        "small_mu_expansion": {
            "formula": "K(K+mu^2 I)^-1 = I - mu^2 K^-1 + O(mu^4)",
            "minus_Delta_of_K_inverse": float(-invK_delta),
        },
        "conclusion": "For the full-rank canonical K, the minimal two-shell master normalization tends to identity as mu->0.",
    }


def higher_shell_block_identity():
    rng = np.random.default_rng(7331)
    p, q, r = 4, 7, 5

    K = canonical_K()
    ev, U = np.linalg.eigh(K)
    sqrtK = (U * np.sqrt(ev)) @ U.conj().T
    X = rng.normal(size=(q, p)) + 1j * rng.normal(size=(q, p))
    Qiso, _ = np.linalg.qr(X)
    A = Qiso[:, :p] @ sqrtK
    C = (rng.normal(size=(r, q)) + 1j * rng.normal(size=(r, q))) / math.sqrt(2 * q)

    H = np.zeros((p + q + r, p + q + r), dtype=complex)
    Ps = slice(0, p)
    Qs = slice(p, p + q)
    Rs = slice(p + q, p + q + r)
    H[Qs, Ps] = A
    H[Ps, Qs] = A.conj().T
    H[Rs, Qs] = C
    H[Qs, Rs] = C.conj().T

    H2 = H @ H
    H4 = H2 @ H2
    K0 = A.conj().T @ A
    lhs = H4[Ps, Ps] - K0 @ K0
    rhs = A.conj().T @ C.conj().T @ C @ A
    block_error = float(np.linalg.norm(lhs - rhs))

    ek, Uk = np.linalg.eigh(K0)
    Kmh = (Uk * (1.0 / np.sqrt(ek))) @ Uk.conj().T
    Lam = Kmh @ lhs @ Kmh
    Lam = (Lam + Lam.conj().T) / 2
    lev = np.linalg.eigvalsh(Lam).real

    return {
        "passed": bool(block_error < 1e-9 and np.min(lev) > -1e-9),
        "block_identity_error": block_error,
        "Lambda_eigenvalues": [float(x) for x in lev],
        "Lambda_min_eigenvalue": float(np.min(lev)),
        "identity": "P H^4 P-K^2 = A^dagger C^dagger C A",
        "next_model_observable": "Lambda=K^-1/2 (P H_E^4 P-K^2) K^-1/2",
        "scope": "This block test proves the algebraic target; the actual Peter-Weyl Lambda still has to be computed.",
    }


def run():
    support = support_grading_audit()
    two = two_shell_master_control()
    higher = higher_shell_block_identity()
    passed = support["passed"] and two["passed"] and higher["passed"]
    return {
        "status": "Peter-Weyl spin-parity and master-constraint gate",
        "passed": bool(passed),
        "support_grading": support,
        "two_shell_master_control": two,
        "higher_shell_identity": higher,
        "frontier": (
            "Raw K=A^dagger A anisotropy is not yet a physical infrared anisotropy. "
            "Because H_E is spin-parity odd, the first nontrivial normalized Euclidean source is second-hit leakage "
            "C from the odd one-hit sector into nonlogical even states. Compute Lambda on the actual Peter-Weyl habitat next."
        ),
        "scientific_scope": (
            "Finite candidate-model algebra only. This gate establishes support grading, a two-shell master normalization "
            "identity and a higher-shell positive block identity. It does not establish extra particle content, a new "
            "interaction, a physical mass scale, or the full Lorentzian/route/matter master constraint."
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
