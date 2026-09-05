#!/usr/bin/env python3
"""Globally grouped outer-edge continuation for one raw Lorentzian boundary column.

Consumes the certified 12-prefix middle packet for one source/input and computes
one fixed outer edge ``a`` contribution to

    H_L^raw ~ sum epsilon_{abc} Tr_aux[C_a(K) C_b(K) C_c(V)].

For fixed ``a,i,j`` the final operator C_a(K)_{ij} is common to every surviving
prefix and auxiliary k-path. Therefore, before the expensive outer hit, we use
only linearity:

    sum_{b,c,k} s_{abc} C_a(K)_{ij} Xi_bc^{ijk}
      = C_a(K)_{ij} [sum_{b,c,k} s_{abc} Xi_bc^{ijk}].

The inner sum is accumulated with NO tolerance pruning (IEEE-exact zeros only).
The frozen scalar-channel selection J2 in {0,2}, Jmax, ordering and C(K)
implementation are unchanged. This reduces the outer work to at most four
C(K) calls per outer edge, hence at most sixteen for the complete first column.

Because numerical sparse implementations can contain internal thresholding, the
result is emitted as an accelerated microscopic packet with an explicit
``production_equivalence_required`` flag. A later independent sparse-equivalence
comparison is required before using this execution mode as a production
replacement for the frozen reference evaluation.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import peter_weyl_lorentzian_epsilon_logical_return_gate as FULL
import peter_weyl_lorentzian_middle_prefix_gate as MID
import peter_weyl_lorentzian_pruned_prefix_worker as PLAN
import peter_weyl_zeroaware_volume_migration_experiment as ZVM


def decode_state(rows):
    out = {}
    for r in rows:
        key = (
            tuple(int(x) for x in r["spins"]),
            tuple(int(x) for x in r["Kother"]),
            int(r["J2"]), int(r["M2"]), int(r["K12"]), int(r["K34"]),
        )
        out[key] = out.get(key, 0j) + complex(float(r["amp"][0]), float(r["amp"][1]))
    return out


def add_no_prune(dst, src, scale=1.0):
    s = complex(scale)
    for key, amp in src.items():
        dst[key] = dst.get(key, 0j) + s * complex(amp)
    # Removing only an IEEE-exact zero is algebraically harmless.
    for key in [k for k, z in dst.items() if z == 0j]:
        del dst[key]


def scalar_channel(state):
    return {k: z for k, z in state.items() if int(k[2]) in (0, 2)}


def norm(state):
    return math.sqrt(sum(abs(z) ** 2 for z in state.values()))


def load_prefixes(prefix_dir: Path):
    summary_path = prefix_dir / "middle_prefix_summary.json"
    if not summary_path.exists():
        raise RuntimeError(f"missing {summary_path}")
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    if summary.get("schema") != "BQG_LORENTZIAN_ALL_MIDDLE_PREFIXES_V1" or not summary.get("passed", False):
        raise RuntimeError("invalid all-middle-prefix summary")
    prefixes = []
    for idx in range(12):
        p = prefix_dir / f"prefix_{idx}.json"
        if not p.exists():
            raise RuntimeError(f"missing prefix artifact {p}")
        d = json.loads(p.read_text(encoding="utf-8"))
        if not d.get("passed", False):
            raise RuntimeError(f"prefix {idx} failed its microscopic integrity gate")
        if int(d["ordered_pair"]["pair_index"]) != idx:
            raise RuntimeError(f"prefix index mismatch in {p}")
        prefixes.append(d)
    return summary, prefixes


def run(prefix_dir: Path, outer_a: int):
    ZVM.patch_and_clear()
    summary, prefixes = load_prefixes(prefix_dir)
    source = int(summary["source_node"])
    input_index = int(summary["input_logical_basis_index"])
    outer_a = int(outer_a)
    neighbors = tuple(FULL.RAW.PW.NEIG[source])
    if outer_a not in neighbors:
        raise ValueError(f"outer edge {outer_a} not incident on source {source}: {neighbors}")

    basis = FULL.RAW.PW.basis_full_jhalf()
    if len(basis) != 32 or not (0 <= input_index < 32):
        raise RuntimeError("frozen 32D all-j=1/2 boundary basis unavailable")
    expected_pairs = MID.ordered_pairs(source)
    if len(expected_pairs) != 12:
        raise RuntimeError("expected twelve ordered middle prefixes")

    common_ok = True
    for idx, p in enumerate(prefixes):
        pair = (int(p["ordered_pair"]["b"]), int(p["ordered_pair"]["c"]))
        common_ok &= pair == expected_pairs[idx]
        common_ok &= int(p["source_node"]) == source
        common_ok &= int(p["input_logical_basis_index"]) == input_index
        common_ok &= abs(float(p["Jmax"]) - float(summary["Jmax"])) < 1e-15

    total = {}
    grouped_rows = []
    outer_calls = 0
    max_spin = 0.0
    diagmax = {
        "CK_outer_complete_basis_leakage": 0.0,
        "CK_internal_volume_sector_leakage": 0.0,
        "CK_complete_charge_basis_leakage": 0.0,
    }
    accounted_triples = []
    relevant_prefix_indices = []

    # Build the exact six ordered epsilon triples whose first edge is outer_a.
    for idx, p in enumerate(prefixes):
        b = int(p["ordered_pair"]["b"])
        c = int(p["ordered_pair"]["c"])
        rows = [r for r in PLAN.epsilon_outer_terms(source, b, c) if int(r["a"]) == outer_a]
        if len(rows) > 1:
            raise RuntimeError(f"prefix {(b,c)} contributes duplicate outer-a rows")
        if rows:
            accounted_triples.append(tuple(int(x) for x in rows[0]["ordered_edges"]))
            relevant_prefix_indices.append(idx)

    old, caches = FULL.install_sine_ordering()
    try:
        for i in range(2):
            for j in range(2):
                grouped = {}
                contributors = []
                for idx, p in enumerate(prefixes):
                    b = int(p["ordered_pair"]["b"])
                    c = int(p["ordered_pair"]["c"])
                    rows = [r for r in PLAN.epsilon_outer_terms(source, b, c) if int(r["a"]) == outer_a]
                    if not rows:
                        continue
                    row = rows[0]
                    sign = int(row["sign"])
                    lookup = {tuple(int(x) for x in q["indices"]): q for q in p["paths"]}
                    if set(lookup) != {(ii, jj, kk) for ii in range(2) for jj in range(2) for kk in range(2)}:
                        raise RuntimeError(f"prefix {idx} does not contain all eight auxiliary paths")
                    before = norm(grouped)
                    path_support = 0
                    path_norm2 = 0.0
                    for k in range(2):
                        s = decode_state(lookup[(i, j, k)]["middle_state"])
                        q = scalar_channel(s)
                        path_support += len(q)
                        path_norm2 += norm(q) ** 2
                        add_no_prune(grouped, q, scale=sign)
                        max_spin = max(max_spin, FULL.max_spin(s), FULL.max_spin(q))
                    contributors.append({
                        "prefix_index": idx,
                        "ordered_edges": [outer_a, b, c],
                        "sign": sign,
                        "prefix_zero_pathwise": bool(p["prefix_zero_pathwise"]),
                        "scalar_input_support_sum": path_support,
                        "scalar_input_quadrature_norm": math.sqrt(path_norm2),
                        "grouped_norm_before": before,
                        "grouped_norm_after": norm(grouped),
                    })
                if grouped:
                    s3, d3 = FULL.RAW.KCOMP.C_K_component(grouped, source, outer_a, i, j, FULL.JMAX2)
                    FULL.update_diag(diagmax, d3)
                    outer_calls += 1
                else:
                    s3 = {}
                FULL.add(total, s3)
                max_spin = max(max_spin, FULL.max_spin(grouped), FULL.max_spin(s3))
                grouped_rows.append({
                    "indices_ij": [i, j],
                    "grouped_pre_outer_support": len(grouped),
                    "grouped_pre_outer_norm": norm(grouped),
                    "outer_support": len(s3),
                    "outer_norm": FULL.norm(s3),
                    "contributors": contributors,
                })
        cache_info = {
            name: {"hits": fun.cache_info().hits, "misses": fun.cache_info().misses, "currsize": fun.cache_info().currsize}
            for name, fun in caches.items()
        }
    finally:
        FULL.restore_ordering(old)

    sd = FULL.scalar_diagnostics(total)
    conv = PLAN.convention_descriptor(source)
    hab = PLAN.habitat_descriptor(source)
    hard = {
        "all_12_prefixes_loaded_with_common_provenance": bool(common_ok),
        "six_ordered_triples_accounted_for_outer_edge": len(accounted_triples) == 6 and len(set(accounted_triples)) == 6,
        "exactly_six_relevant_prefixes_for_outer_edge": len(relevant_prefix_indices) == 6 and len(set(relevant_prefix_indices)) == 6,
        "exactly_four_ij_channels": len(grouped_rows) == 4,
        "outer_CK_call_count_at_most_four": outer_calls <= 4,
        "no_pre_outer_tolerance_pruning": True,
        "outer_CK_complete_basis_leakage_below_1e-9": diagmax["CK_outer_complete_basis_leakage"] < 1e-9,
        "outer_CK_internal_volume_sector_leakage_below_1e-9": diagmax["CK_internal_volume_sector_leakage"] < 1e-9,
        "signed_outer_edge_output_scalar_within_frozen_threshold": FULL.scalar_ok(sd),
        "spin_cutoff_respected": max_spin <= FULL.JMAX2 / 2 + 1e-12,
    }
    return {
        "schema": "BQG_LORENTZIAN_GLOBAL_OUTER_EDGE_V1",
        "passed": bool(all(hard.values())),
        "science_status": "OUTER_EDGE_ZERO" if not total else "OUTER_EDGE_NONZERO",
        "execution_mode": "global_signed_prefix_k_grouping_by_fixed_aij_v1",
        "production_equivalence_required": True,
        "source_node": source,
        "input_logical_basis_index": input_index,
        "input_K_labels": list(basis[input_index][1]),
        "outer_a": outer_a,
        "Jmax": FULL.JMAX2 / 2,
        "accounted_ordered_triples": [list(x) for x in sorted(accounted_triples)],
        "relevant_prefix_indices": relevant_prefix_indices,
        "outer_CK_call_count": outer_calls,
        "naive_ungrouped_outer_call_count_for_same_a": 48,
        "grouped_ij": grouped_rows,
        "outgoing_support": len(total),
        "outgoing_norm": FULL.norm(total),
        "scalar_diagnostics": sd,
        "max_spin_reached": max_spin,
        "max_diagnostics": diagmax,
        "hard_integrity_checks": hard,
        "runtime_exact_cache": cache_info,
        "habitat_descriptor": hab,
        "habitat_hash": PLAN.canonical_hash(hab),
        "boundary_domain_hash": PLAN.boundary_domain_hash(basis),
        "convention_descriptor": conv,
        "convention_hash": PLAN.canonical_hash(conv),
        "state": PLAN.encode_state(total),
        "claim_boundary": "Accelerated algebraically grouped contribution for one outer edge of one raw Lorentzian boundary column. It is not P_phys, not an HDA certificate, and must pass an independent sparse-equivalence gate before replacing the frozen production evaluator.",
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--prefix-dir", type=Path, required=True)
    ap.add_argument("--outer-a", type=int, required=True)
    ap.add_argument("--output", type=Path, required=True)
    a = ap.parse_args()
    out = run(a.prefix_dir, a.outer_a)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in out.items() if k not in ("state", "grouped_ij")}, indent=2))
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
