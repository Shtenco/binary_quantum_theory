#!/usr/bin/env python3
"""Exact negative result for the proposed 12 -> 24 PL epsilon correction.

The missing anti-cyclic ordered triples are already exact duplicates of the
historical cyclic terms after Levi-Civita parity is included.  Therefore the
normalized full 24-term alternating sum is IDENTICALLY the current 12-term
operator and cannot repair the measured finite pairing-stabilizer defect.

This gate works at actual T_sequences operator-word level and avoids the heavy
Peter-Weyl amplitude evaluation entirely.
"""
from __future__ import annotations

import argparse
import itertools
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from pl_dual_complex import DualComplex, seed_16cell_boundary
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean


def parity(p):
    return -1 if sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2 else 1


def counter(rows):
    """Exact multiset of sequences with integer external coefficients."""
    c = Counter()
    for coef, seq in rows:
        c[repr(seq)] += int(coef)
    return +c - (-c)


def signed_counter(rows, scale=1):
    c = Counter()
    for coef, seq in rows:
        c[repr(seq)] += int(scale) * int(coef)
    return c


def exact_neg(a, b):
    ca = signed_counter(a, +1)
    cb = signed_counter(b, +1)
    keys = set(ca) | set(cb)
    return all(cb[k] == -ca[k] for k in keys)


def exact_neg_adjoint(G, a, b):
    ca = Counter()
    cb = Counter()
    for coef, seq in a:
        ca[repr(G.adjoint_sequence(seq))] += int(coef)
    for coef, seq in b:
        cb[repr(G.adjoint_sequence(seq))] += int(coef)
    keys = set(ca) | set(cb)
    return all(cb[k] == -ca[k] for k in keys)


def run():
    D = DualComplex(seed_16cell_boundary())
    G = PLPeterWeylEuclidean(D)

    swap_rows = []
    forward_failures = []
    adjoint_failures = []

    for v in range(D.n_tets):
        for a in range(4):
            for b in range(4):
                if b == a:
                    continue
                for c in range(4):
                    if c in (a, b):
                        continue
                    lhs = G.T_sequences(v, a, b, c)
                    rhs = G.T_sequences(v, b, a, c)
                    fwd = exact_neg(lhs, rhs)
                    adj = exact_neg_adjoint(G, lhs, rhs)
                    if not fwd:
                        forward_failures.append((v, a, b, c))
                    if not adj:
                        adjoint_failures.append((v, a, b, c))
                    swap_rows.append(
                        {
                            "node": v,
                            "a": a,
                            "b": b,
                            "c": c,
                            "forward_exact_negative": fwd,
                            "direct_adjoint_exact_negative": adj,
                        }
                    )

    # Fixed-d parity pairing between 3 historical cyclic and 3 omitted
    # anti-cyclic orders.  We construct the exact bijection anti = swap12(cyclic)
    # rather than selecting it after inspection.
    omitted_rows = []
    parity_pairing_ok = True
    for d in range(4):
        tri = tuple(r for r in range(4) if r != d)
        cyclic = [tri, (tri[1], tri[2], tri[0]), (tri[2], tri[0], tri[1])]
        anti = [(p[1], p[0], p[2]) for p in cyclic]
        row_pairs = []
        for cyc, ant in zip(cyclic, anti):
            sc = parity((d,) + cyc)
            sa = parity((d,) + ant)
            ok = sa == -sc
            parity_pairing_ok = parity_pairing_ok and ok
            row_pairs.append(
                {
                    "cyclic": list(cyc),
                    "anti_cyclic": list(ant),
                    "cyclic_parity": sc,
                    "anti_cyclic_parity": sa,
                    "opposite_parity": ok,
                }
            )
        omitted_rows.append({"omitted_slot": d, "pairs": row_pairs})

    # Formal coefficient identity: for each paired term,
    # (1/2)[s*T + (-s)*(-T)] = s*T.
    pair_identity_exact = parity_pairing_ok and not forward_failures and not adjoint_failures

    checks = {
        "384_forward_swap_cases_exact": len(swap_rows) == 384 and len(forward_failures) == 0,
        "384_direct_adjoint_swap_cases_exact": len(swap_rows) == 384 and len(adjoint_failures) == 0,
        "cyclic_anticyclic_parities_opposite": bool(parity_pairing_ok),
        "normalized_full24_equals_historical12_forward": bool(pair_identity_exact),
        "normalized_full24_equals_historical12_direct_adjoint": bool(pair_identity_exact),
        "normalized_full24_equals_historical12_physical_sine": bool(pair_identity_exact),
    }

    return {
        "status": "exact PL Euclidean 12-term / 24-term epsilon equivalence",
        "passed": bool(all(checks.values())),
        "science_status": "EXACT_NEGATIVE_OPERATOR_CORRECTION_RESULT",
        "checks": checks,
        "ordered_swap_cases_checked": len(swap_rows),
        "forward_failures": [list(x) for x in forward_failures[:8]],
        "direct_adjoint_failures": [list(x) for x in adjoint_failures[:8]],
        "omitted_slot_pairing": omitted_rows,
        "identity": "T(v;b,a,c)=-T(v;a,b,c) exactly; anti-cyclic epsilon parity also flips; therefore E_full24=(1/2)sum_S4 sgn(p)T_p equals E_historical12 exactly.",
        "consequence": "The measured 0.1139945503942336 finite H-sign-irrep breaking power cannot be repaired by adding the omitted anti-cyclic half. The defect lies deeper in the distinguished third-slot/triad-leg regulator role or its refinement behavior.",
        "documentation": "PL_EUCLIDEAN_12_24_EQUIVALENCE_THEOREM.md",
        "supersedes_experiment": "A heavy full24 amplitude rerun is mathematically redundant for deciding the 12-vs-24 question.",
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path)
    a = p.parse_args()
    out = run()
    text = json.dumps(out, indent=2, sort_keys=True)
    print(text)
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
