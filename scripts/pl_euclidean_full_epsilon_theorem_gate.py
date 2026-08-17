#!/usr/bin/env python3
"""Exact combinatorial certificate for full-epsilon PL Euclidean covariance.

No floating point or GR target is used.  The gate checks:
1. the S4 alternating-character reindexing identity exhaustively;
2. exact 16-cell dual-edge and plaquette-path covariance for all 24 local slot
   permutations, all 16 dual nodes, and all ordered r != s face pairs;
3. the historical 12 cyclic representatives are exactly one parity class of
   the six permutations of the non-omitted slots, explaining why a factor 1/2
   makes the 24-term normalization collapse to the old normalization when the
   omitted anti-cyclic terms are exact negatives.
"""
from __future__ import annotations

import argparse
import itertools
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from pl_dual_complex import DualComplex, seed_16cell_boundary


def parity(p):
    return -1 if sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2 else 1


def compose(h, p):
    return tuple(h[x] for x in p)


def inv(h):
    q = [0] * len(h)
    for i, x in enumerate(h):
        q[x] = i
    return tuple(q)


def map_node(v, h):
    bits = [(v >> (3 - i)) & 1 for i in range(4)]
    nb = [0] * 4
    for i in range(4):
        nb[h[i]] = bits[i]
    out = 0
    for i, b in enumerate(nb):
        out |= b << (3 - i)
    return out


def run():
    S4 = tuple(itertools.permutations(range(4)))

    # Character/reindex theorem: sgn(h^-1 q) = sgn(h) sgn(q).
    reindex_fail = []
    for h in S4:
        hi = inv(h)
        for q in S4:
            lhs = parity(compose(hi, q))
            rhs = parity(h) * parity(q)
            if lhs != rhs:
                reindex_fail.append((h, q, lhs, rhs))

    D = DualComplex(seed_16cell_boundary())

    # Graph/plaquette exact covariance for full local S4, not just order-8 H.
    neighbor_fail = []
    path_fail = []
    edge_orientation_reversals = []
    edges = D.dual_edges()
    edge_set = set(edges)

    for h in S4:
        for v in range(D.n_tets):
            for r in range(4):
                lhs = map_node(D.neighbor[(v, r)], h)
                rhs = D.neighbor[(map_node(v, h), h[r])]
                if lhs != rhs:
                    neighbor_fail.append((h, v, r, lhs, rhs))
            for r in range(4):
                for s in range(4):
                    if r == s:
                        continue
                    p = D.plaquette_path(v, r, s)
                    mapped = tuple(map_node(x, h) for x in p)
                    target = D.plaquette_path(map_node(v, h), h[r], h[s])
                    if mapped != target:
                        path_fail.append((h, v, r, s, mapped, target))

        rev = 0
        mapped_edges = set()
        for a, b in edges:
            aa, bb = map_node(a, h), map_node(b, h)
            if (a < b) != (aa < bb):
                rev += 1
            mapped_edges.add(tuple(sorted((aa, bb))))
        if mapped_edges != edge_set or rev:
            edge_orientation_reversals.append((h, rev, len(mapped_edges), len(edge_set)))

    # Old 12 representatives are the three even permutations of the remaining
    # triad for each fixed omitted slot relative to its sorted order.
    cyclic_rows = []
    cyclic_ok = True
    for d in range(4):
        tri = tuple(x for x in range(4) if x != d)
        cyclic = (tri, (tri[1], tri[2], tri[0]), (tri[2], tri[0], tri[1]))
        anti = tuple(p for p in itertools.permutations(tri) if p not in cyclic)
        signs_c = [parity((d,) + p) for p in cyclic]
        signs_a = [parity((d,) + p) for p in anti]
        expected = (-1) ** d
        row_ok = all(x == expected for x in signs_c) and all(x == -expected for x in signs_a)
        cyclic_ok = cyclic_ok and row_ok
        cyclic_rows.append(
            {
                "omitted_slot": d,
                "cyclic": [list(x) for x in cyclic],
                "anti_cyclic": [list(x) for x in anti],
                "cyclic_signs": signs_c,
                "anti_cyclic_signs": signs_a,
                "historical_local_sign": expected,
                "passed": row_ok,
            }
        )

    checks = {
        "S4_order_24": len(S4) == 24,
        "alternating_reindex_identity_exact": len(reindex_fail) == 0,
        "16cell_neighbor_slot_covariance_full_S4": len(neighbor_fail) == 0,
        "16cell_plaquette_path_covariance_full_S4": len(path_fail) == 0,
        "16cell_dual_edge_orientation_preserved_full_S4": len(edge_orientation_reversals) == 0,
        "historical_12_are_cyclic_parity_half_of_full24": bool(cyclic_ok),
    }

    return {
        "status": "exact combinatorial full-epsilon PL Euclidean covariance theorem",
        "passed": bool(all(checks.values())),
        "science_status": "EXACT_STRUCTURAL_THEOREM",
        "checks": checks,
        "S4_order": len(S4),
        "reindex_cases_checked": len(S4) * len(S4),
        "neighbor_cases_checked": len(S4) * D.n_tets * 4,
        "plaquette_cases_checked": len(S4) * D.n_tets * 4 * 3,
        "dual_edges": len(edges),
        "reindex_failures": reindex_fail[:4],
        "neighbor_failures": neighbor_fail[:4],
        "plaquette_failures": path_fail[:4],
        "edge_orientation_failures": edge_orientation_reversals[:4],
        "cyclic_rows": cyclic_rows,
        "theorem": "If U_h T_p U_h^-1 = T_{h.p}, then E24=(1/2)sum_p sgn(p)T_p obeys U_h E24 U_h^-1=sgn(h)E24 exactly.",
        "scope_note": "This proves the alternating/reindex and PL path combinatorics. The heavy Peter-Weyl full24 gate independently checks that the implemented elementary words realize the assumed covariance.",
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path)
    a = ap.parse_args()
    out = run()
    text = json.dumps(out, indent=2, sort_keys=True)
    print(text)
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
