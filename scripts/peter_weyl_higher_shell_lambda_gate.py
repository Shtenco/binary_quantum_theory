#!/usr/bin/env python3
"""Actual 32D higher-shell Peter-Weyl master observable.

The calculation is exact but naturally embarrassingly parallel over the 32
logical basis columns. For each logical basis vector |i> compute

    a_i = H |i>,
    b_i = H^2 |i>,

with H = H_E,0 + H_E,1 and the regulator-safe second-hit wall Jmax=5/2.
After all columns are available,

    K_ij  = <a_i|a_j> = (P H^2 P)_ij,
    H4_ij = <b_i|b_j> = (P H^4 P)_ij,

and

    Lambda = K^-1/2 (H4-K^2) K^-1/2.

Because P H P=0 by exact spin parity, this is also the second block-Lanczos
hopping norm:

    B1^dag B1 = K,
    B2^dag B2 = Lambda.

The column mode serializes the exact sparse states. The assembly mode performs
only inner products and small 32x32 linear algebra; no approximation is added.
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

import peter_weyl_logical_anisotropy_gate as AN
import peter_weyl_euclidean_sine_ordering_gate as SINE

TOL = 1e-11
JMAX2_SECOND_HIT_SAFE = 5
NLOGICAL = 32


def apply_H_state(state, v=0, w=1):
    out = {}
    AN.sparse_add(out, SINE.safe_H_sine(state, v, JMAX2_SECOND_HIT_SAFE))
    AN.sparse_add(out, SINE.safe_H_sine(state, w, JMAX2_SECOND_HIT_SAFE))
    return {k: a for k, a in out.items() if abs(a) > TOL}


def logical_basis():
    keys = []
    labels = []
    for env in AN.ENV_STATES:
        for pair in AN.PAIR_STATES:
            keys.append(AN.logical_key(pair[0], pair[1], env))
            labels.append({"environment_K234": list(env), "pair_K01": list(pair)})
    if len(keys) != NLOGICAL:
        raise RuntimeError(f"expected {NLOGICAL} logical states, got {len(keys)}")
    return keys, labels


def state_to_rows(state):
    rows = []
    for (spins, Ks), amp in state.items():
        rows.append({
            "spins2": list(spins),
            "Ks2": list(Ks),
            "amp": [float(amp.real), float(amp.imag)],
        })
    return rows


def rows_to_state(rows):
    out = {}
    for r in rows:
        key = (tuple(int(x) for x in r["spins2"]), tuple(int(x) for x in r["Ks2"]))
        out[key] = complex(float(r["amp"][0]), float(r["amp"][1]))
    return out


def max_spin(state):
    if not state:
        return 0.0
    return max(max(key[0]) / 2.0 for key in state)


def compute_column(index: int):
    if not 0 <= index < NLOGICAL:
        raise ValueError(f"column must be in [0,{NLOGICAL-1}]")
    AN.ZVM.patch_and_clear()
    keys, labels = logical_basis()
    key = keys[index]
    a = apply_H_state({key: 1.0 + 0j})
    projected = {k: v for k, v in a.items() if AN.is_all_jhalf(k)}
    first_proj = AN.sparse_norm(projected)
    b = apply_H_state(a)
    return {
        "status": "exact Peter-Weyl higher-shell logical column",
        "column": index,
        "label": labels[index],
        "Jmax_used": JMAX2_SECOND_HIT_SAFE / 2,
        "first_order_projection_norm": float(first_proj),
        "first_support": len(a),
        "second_support": len(b),
        "first_max_spin": max_spin(a),
        "second_max_spin": max_spin(b),
        "first_state": state_to_rows(a),
        "second_state": state_to_rows(b),
    }


def sparse_inner(a, b):
    if len(a) > len(b):
        a, b = b, a
        return np.conj(sparse_inner(a, b))
    return sum(np.conj(v) * b.get(k, 0j) for k, v in a.items())


def gram(images):
    n = len(images)
    G = np.zeros((n, n), dtype=complex)
    for i in range(n):
        for j in range(i, n):
            z = sparse_inner(images[i], images[j])
            G[i, j] = z
            G[j, i] = np.conj(z)
    return (G + G.conj().T) / 2


def pair_partial_trace(K32):
    out = np.zeros((4, 4), dtype=complex)
    for e in range(len(AN.ENV_STATES)):
        sl = slice(4 * e, 4 * e + 4)
        out += K32[sl, sl]
    return out / len(AN.ENV_STATES)


def full_pauli_weight_summary(M):
    labels = ("I", "X", "Y", "Z")
    weight_norm2 = {w: 0.0 for w in range(6)}
    largest = []
    dim = M.shape[0]
    for lab in itertools.product(labels, repeat=5):
        P = AN.PAULI[lab[0]]
        for x in lab[1:]:
            P = np.kron(P, AN.PAULI[x])
        c = np.trace(P @ M) / dim
        w = sum(x != "I" for x in lab)
        weight_norm2[w] += float(abs(c) ** 2)
        if w > 0 and abs(c) > 1e-10:
            largest.append((float(abs(c)), "".join(lab), complex(c)))
    largest.sort(reverse=True)
    return {
        "basis_order": "q2,q3,q4,q0,q1",
        "frobenius_coefficient_norm_by_pauli_weight": {
            str(w): math.sqrt(v) for w, v in weight_norm2.items()
        },
        "largest_nonidentity_coefficients": [
            {"label": lab, "coefficient": [float(c.real), float(c.imag)], "abs": a}
            for a, lab, c in largest[:24]
        ],
    }


def matrix_json(M):
    return [
        [[float(z.real), float(z.imag)] for z in row]
        for row in np.asarray(M)
    ]


def hermitian_sqrt(M, name: str, negative_tol: float = 1e-8):
    M = (M + M.conj().T) / 2
    ev, U = np.linalg.eigh(M)
    scale = max(float(np.max(np.abs(ev))), 1.0)
    if float(np.min(ev)) < -negative_tol * scale:
        raise RuntimeError(f"{name} is not PSD: min eigenvalue={float(np.min(ev))}")
    vals = np.sqrt(np.clip(ev, 0.0, None))
    S = (U * vals) @ U.conj().T
    return (S + S.conj().T) / 2, ev


def assemble(directory: Path):
    files = sorted(directory.glob("column_*.json"))
    cols = {}
    for path in files:
        d = json.loads(path.read_text(encoding="utf-8"))
        idx = int(d["column"])
        if idx in cols:
            raise RuntimeError(f"duplicate column {idx}")
        cols[idx] = d
    missing = [i for i in range(NLOGICAL) if i not in cols]
    if missing:
        raise RuntimeError(f"missing columns: {missing}")

    ordered = [cols[i] for i in range(NLOGICAL)]
    first = [rows_to_state(d["first_state"]) for d in ordered]
    second = [rows_to_state(d["second_state"]) for d in ordered]

    K = gram(first)
    H4 = gram(second)
    M = H4 - K @ K
    M = (M + M.conj().T) / 2

    ek, Uk = np.linalg.eigh(K)
    kscale = max(float(np.max(np.abs(ek))), 1.0)
    ktol = 1e-10 * kscale
    rank = int(np.sum(ek > ktol))
    if rank != NLOGICAL:
        raise RuntimeError(f"K is not full rank: rank={rank}")

    Kmh = (Uk * (1.0 / np.sqrt(ek))) @ Uk.conj().T
    Lam = Kmh @ M @ Kmh
    Lam = (Lam + Lam.conj().T) / 2
    em = np.linalg.eigvalsh(M).real
    el = np.linalg.eigvalsh(Lam).real

    B1, _ = hermitian_sqrt(K, "K", negative_tol=1e-10)
    B2, _ = hermitian_sqrt(Lam, "Lambda", negative_tol=2e-7)

    pair = pair_partial_trace(Lam)
    pair_analysis = AN.analyze_kernel(pair)
    coeff, _ = AN.pauli_decompose(pair)
    Jrot = pair_analysis["heisenberg_frame"]["coupling_tensor_XYZ"]
    Jrot_real = np.array([[complex(*z).real for z in row] for row in Jrot])
    j_shape = float(0.5 * (Jrot_real[0, 0] + Jrot_real[2, 2]))
    j_orient = float(Jrot_real[1, 1])

    first_proj_max = max(float(d["first_order_projection_norm"]) for d in ordered)
    second_max = max(float(d["second_max_spin"]) for d in ordered)
    mscale = max(float(np.max(np.abs(em))), 1.0)
    positivity_tol = 5e-8 * mscale

    b1_err = float(np.linalg.norm(B1.conj().T @ B1 - K))
    b2_err = float(np.linalg.norm(B2.conj().T @ B2 - Lam))
    h4_reconstruction = float(np.linalg.norm(H4 - (K @ K + M)))

    passed = (
        first_proj_max < 1e-12
        and rank == NLOGICAL
        and second_max <= JMAX2_SECOND_HIT_SAFE / 2 + 1e-12
        and float(np.min(em)) > -positivity_tol
        and float(np.min(el)) > -2e-7 * max(float(np.max(np.abs(el))), 1.0)
        and pair_analysis["hermiticity_error"] < 1e-9
        and pair_analysis["pauli_reconstruction_error"] < 1e-8
        and b1_err < 1e-8
        and b2_err < 1e-7
    )

    return {
        "status": "actual finite 32D Peter-Weyl higher-shell Lambda / block-Lanczos gate",
        "passed": bool(passed),
        "column_count": len(ordered),
        "support": {
            "first_order_projection_max": first_proj_max,
            "first_support_min": min(int(d["first_support"]) for d in ordered),
            "first_support_max": max(int(d["first_support"]) for d in ordered),
            "second_support_min": min(int(d["second_support"]) for d in ordered),
            "second_support_max": max(int(d["second_support"]) for d in ordered),
            "second_max_spin": second_max,
            "Jmax_used": JMAX2_SECOND_HIT_SAFE / 2,
            "regulator_note": "Jmax=5/2 is the proven safe Euclidean second-hit wall for all-j=1/2 input.",
        },
        "K": {
            "rank": rank,
            "eigenvalue_min": float(np.min(ek)),
            "eigenvalue_max": float(np.max(ek)),
            "condition_number": float(np.max(ek) / np.min(ek)),
        },
        "higher_shell_positive_matrix": {
            "identity": "M=P H^4 P-K^2",
            "H4_reconstruction_error": h4_reconstruction,
            "eigenvalue_min": float(np.min(em)),
            "eigenvalue_max": float(np.max(em)),
        },
        "Lambda": {
            "definition": "K^-1/2 (P H^4 P-K^2) K^-1/2",
            "eigenvalues": [float(x) for x in el],
            "eigenvalue_min": float(np.min(el)),
            "eigenvalue_max": float(np.max(el)),
            "trace": float(np.trace(Lam).real),
            "distance_to_scalar_identity_relative": float(
                np.linalg.norm(Lam - np.trace(Lam).real / NLOGICAL * np.eye(NLOGICAL))
                / max(np.linalg.norm(Lam), 1e-30)
            ),
        },
        "block_lanczos": {
            "B1_definition": "sqrt(K)",
            "B2_definition": "sqrt(Lambda)",
            "B1_reconstruction_error": b1_err,
            "B2_reconstruction_error": b2_err,
            "continued_fraction": (
                "G0(z)=[zI-B1^dag [zI-B2^dag G2(z) B2]^-1 B1]^-1 "
                "for the parity-odd chain with vanishing diagonal Lanczos blocks, recursively continued."
            ),
        },
        "pair_partial_trace_01": {
            **pair_analysis,
            "S4_shape_coupling_after_B_rotation": j_shape,
            "orientation_coupling_after_B_rotation": j_orient,
            "Delta_orient_minus_shape": j_orient - j_shape,
            "raw_pauli_coefficients": {k: [float(v.real), float(v.imag)] for k, v in coeff.items()},
        },
        "full_5qubit_pauli_summary": full_pauli_weight_summary(Lam),
        "matrices_common_logical_basis": {
            "basis_order": "environment K234 major, pair K01 minor; equivalent qubit order q2,q3,q4,q0,q1",
            "K": matrix_json(K),
            "Lambda": matrix_json(Lam),
            "B1": matrix_json(B1),
            "B2": matrix_json(B2),
        },
        "interpretation": (
            "Lambda is the denominator-free higher-shell logical observable and the squared second block-Lanczos hopping. "
            "A non-scalar Lambda is genuine next-shell logical dynamics that survives two-shell K normalization."
        ),
        "scientific_scope": (
            "Finite Euclidean H_E0+H_E1 Peter-Weyl calculation at regulator-safe Jmax=5/2. "
            "No arbitrary energy denominator, external data or per-observable fit is used."
        ),
    }


def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--column", type=int)
    mode.add_argument("--assemble-dir", type=Path)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    if args.column is not None:
        out = compute_column(args.column)
        write_json(args.output, out)
        print(json.dumps({
            "column": out["column"],
            "first_support": out["first_support"],
            "second_support": out["second_support"],
            "second_max_spin": out["second_max_spin"],
        }, indent=2))
        return 0

    out = assemble(args.assemble_dir)
    write_json(args.output, out)
    print(json.dumps({
        "passed": out["passed"],
        "K": out["K"],
        "Lambda": out["Lambda"],
        "block_lanczos": out["block_lanczos"],
        "pair_Delta": out["pair_partial_trace_01"]["Delta_orient_minus_shape"],
    }, indent=2))
    return 0 if out["passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
