#!/usr/bin/env python3
"""Actual 32D higher-shell Peter-Weyl master observable.

For the logical P sector and H=H_E,0+H_E,1, spin parity gives P H P=0.
Define for each logical basis vector |i>

    a_i = H |i>
    b_i = H^2 |i>.

Then

    K_ij = <a_i|a_j> = (P H^2 P)_ij
    H4_ij = <b_i|b_j> = (P H^4 P)_ij

and the first denominator-free higher-shell master observable is

    Lambda = K^-1/2 (H4-K^2) K^-1/2.

The earlier spin-parity/master gate proved the block identity only on generic
matrices. This script evaluates Lambda on the actual finite Peter-Weyl habitat.
It is still Euclidean and finite; it is not the final Lorentzian/RG propagator.
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
JMAX2_SECOND_HIT_SAFE = 5  # Jmax=5/2, required by the proven HH reachability wall.


def apply_H_state(state, v=0, w=1):
    out = {}
    AN.sparse_add(out, SINE.safe_H_sine(state, v, JMAX2_SECOND_HIT_SAFE))
    AN.sparse_add(out, SINE.safe_H_sine(state, w, JMAX2_SECOND_HIT_SAFE))
    return out


def logical_basis():
    keys = []
    labels = []
    for env in AN.ENV_STATES:
        for pair in AN.PAIR_STATES:
            keys.append(AN.logical_key(pair[0], pair[1], env))
            labels.append({"environment_K234": list(env), "pair_K01": list(pair)})
    return keys, labels


def gram(images):
    n = len(images)
    K = np.zeros((n, n), dtype=complex)
    for i in range(n):
        for j in range(i, n):
            z = AN.sparse_inner(images[i], images[j])
            K[i, j] = z
            K[j, i] = np.conj(z)
    return (K + K.conj().T) / 2


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


def run():
    AN.ZVM.patch_and_clear()
    keys, labels = logical_basis()

    first = []
    second = []
    first_support = []
    second_support = []
    first_proj_max = 0.0
    second_max_spin = 0.0

    for idx, key in enumerate(keys):
        a = apply_H_state({key: 1.0 + 0j})
        p1 = {k: v for k, v in a.items() if AN.is_all_jhalf(k)}
        first_proj_max = max(first_proj_max, AN.sparse_norm(p1))
        first.append(a)
        first_support.append(len(a))

        b = apply_H_state(a)
        second.append(b)
        second_support.append(len(b))
        if b:
            second_max_spin = max(second_max_spin, max(max(k[0]) / 2 for k in b))
        print(
            f"column {idx+1:02d}/32 first_support={len(a)} second_support={len(b)}",
            flush=True,
        )

    K = gram(first)
    H4 = gram(second)
    M = H4 - K @ K
    M = (M + M.conj().T) / 2

    ek, Uk = np.linalg.eigh(K)
    scale = max(float(np.max(np.abs(ek))), 1.0)
    ktol = 1e-10 * scale
    rank = int(np.sum(ek > ktol))
    if rank != 32:
        raise RuntimeError(f"K is not full rank: rank={rank}")
    Kmh = (Uk * (1.0 / np.sqrt(ek))) @ Uk.conj().T
    Lam = Kmh @ M @ Kmh
    Lam = (Lam + Lam.conj().T) / 2
    el = np.linalg.eigvalsh(Lam).real
    em = np.linalg.eigvalsh(M).real

    pair = pair_partial_trace(Lam)
    pair_analysis = AN.analyze_kernel(pair)
    coeff, _ = AN.pauli_decompose(pair)
    Jrot = pair_analysis["heisenberg_frame"]["coupling_tensor_XYZ"]
    Jrot_real = np.array([[complex(*z).real for z in row] for row in Jrot])
    j_shape = float(0.5 * (Jrot_real[0, 0] + Jrot_real[2, 2]))
    j_orient = float(Jrot_real[1, 1])

    h4_reconstruction = K @ K + M
    h4_error = float(np.linalg.norm(H4 - h4_reconstruction))
    positivity_tol = 5e-8 * max(float(np.max(np.abs(em))), 1.0)

    passed = (
        first_proj_max < 1e-12
        and rank == 32
        and h4_error < 1e-8
        and second_max_spin <= JMAX2_SECOND_HIT_SAFE / 2 + 1e-12
        and float(np.min(em)) > -positivity_tol
        and float(np.min(el)) > -1e-7
        and pair_analysis["hermiticity_error"] < 1e-9
        and pair_analysis["pauli_reconstruction_error"] < 1e-8
    )

    return {
        "status": "actual finite 32D Peter-Weyl higher-shell Lambda gate",
        "passed": bool(passed),
        "basis_labels": labels,
        "support": {
            "first_order_projection_max": first_proj_max,
            "first_support_min": int(min(first_support)),
            "first_support_max": int(max(first_support)),
            "second_support_min": int(min(second_support)),
            "second_support_max": int(max(second_support)),
            "second_max_spin": second_max_spin,
            "Jmax_used": JMAX2_SECOND_HIT_SAFE / 2,
            "regulator_note": "Jmax=5/2 is the proven safe HH wall for all-j=1/2 input.",
        },
        "K": {
            "rank": rank,
            "eigenvalue_min": float(np.min(ek)),
            "eigenvalue_max": float(np.max(ek)),
            "condition_number": float(np.max(ek) / np.min(ek)),
        },
        "higher_shell_positive_matrix": {
            "identity": "M=P H^4 P-K^2",
            "H4_reconstruction_error": h4_error,
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
                np.linalg.norm(Lam - np.trace(Lam).real / 32.0 * np.eye(32))
                / max(np.linalg.norm(Lam), 1e-30)
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
        "interpretation": (
            "This is the first actual denominator-free higher-shell logical master observable. "
            "A non-scalar Lambda identifies genuine next-shell logical dynamics that survives the "
            "two-shell K=A^dagger A normalization. It is not yet a physical TT stiffness until "
            "the Lorentzian/route sectors and recursive spatial RG are included."
        ),
        "scientific_scope": (
            "Finite Euclidean H_E0+H_E1 Peter-Weyl calculation at regulator-safe Jmax=5/2. "
            "No arbitrary energy denominator, mirror-force fit or external data is used."
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
    return 0 if out["passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
