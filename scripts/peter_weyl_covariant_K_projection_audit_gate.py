#!/usr/bin/env python3
"""Invariant audit for the matrix-covariant Lorentzian K leg.

The historical full-charge C_e(K) run intentionally remains a FAIL because it
used the maximum non-Gauss component of individual fixed-index primitive
branches as a hard criterion.  Such a branch is not separately gauge
invariant.  This audit keeps that diagnostic but replaces it, for physical
pass/fail purposes, with invariant full-operator tests frozen in
PETER_WEYL_COVARIANT_K_PROJECTION_AUDIT.md.

The key independent regression is

  H_E^(all-J internal volume + linear Gauss projection)
      == H_E^(existing safe Peter-Weyl engine)

on the frozen all-j=1/2, all-K=0 input.  This checks that term-by-term linear
projection has not altered the physical Gauss matrix element.  The audit then
requires the complete charged H_E and K sums to preserve the spectator
J=1/2 representation exactly, and the final C_e(K) source to contain only
J=0 plus J=1.

No operator coefficient or tolerance from the old C(K) calculation is fitted.
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
import peter_weyl_covariant_K_leg_gate as CK


def add(dst, src, scale=1.0, tol=1e-11):
    for key, amp in src.items():
        z = dst.get(key, 0j) + scale * amp
        if abs(z) > tol:
            dst[key] = z
        elif key in dst:
            del dst[key]


def project_gauss_branch(branch, tol=1e-11):
    """Linear Gauss projection of one completed primitive branch."""
    spins, tensors, amp = branch
    opts_by_node = []
    for v in PW.VERT:
        ls = PW.local_spins(spins, v)
        opts = []
        for K in PW.allowed_k2_t(*ls):
            c = np.vdot(PW.oriented_intertwiner(v, ls, K), tensors[v])
            if abs(c) > 1e-13:
                opts.append((K, c))
        if not opts:
            return {}
        opts_by_node.append(tuple(opts))

    out = {}
    for choice in itertools.product(*opts_by_node):
        val = amp
        Ks = []
        for K, c in choice:
            Ks.append(K)
            val *= c
        if abs(val) > tol:
            key = (spins, tuple(Ks))
            out[key] = out.get(key, 0j) + val
    return {k:a for k,a in out.items() if abs(a) > tol}


def apply_HE_allJ_then_Gauss(initial, source_v, Jmax2):
    """Same primitive sequences as H_E, but CK's direct-sum-J volume engine."""
    base = PW.initial_factorized_oriented(initial)
    out = {}
    max_internal_volume_sector_leakage = 0.0
    for sign, spec in PW.oriented_specs(source_v):
        v, a, b, c = spec
        for adj in (False, True):
            pref = 0.5 * sign
            for coef, seq0 in PW.T_sequences(v, a, b, c):
                seq = PW.adjoint_sequence(seq0) if adj else seq0
                branches, vleak = CK.apply_sequence_to_branch(base, seq, source_v, Jmax2)
                max_internal_volume_sector_leakage = max(
                    max_internal_volume_sector_leakage, vleak
                )
                for branch in branches:
                    add(out, project_gauss_branch(branch), pref * coef)
    return {k:a for k,a in out.items() if abs(a) > 1e-10}, max_internal_volume_sector_leakage


def sparse_norm2(state):
    return float(sum(abs(a) ** 2 for a in state.values()))


def relative_state_error(a, b):
    keys = set(a) | set(b)
    num = math.sqrt(sum(abs(a.get(k,0j)-b.get(k,0j))**2 for k in keys))
    den = math.sqrt(sparse_norm2(b))
    return num / max(den, 1e-30)


def run():
    JMAX2 = 5
    initial = PW.basis_full_jhalf()[0]

    # Independent uncharged regression using the new all-J volume implementation.
    allj_gauss, allj_vleak = apply_HE_allJ_then_Gauss(initial, 0, JMAX2)
    safe = PW.prune_state(
        PW.apply_H_cached_state({initial:1+0j}, 0, JMAX2), 1e-10
    )
    he_regression = relative_state_error(allj_gauss, safe)
    support_match = set(allj_gauss) == set(safe)

    # Historical exact C(K) calculation. Its own `passed` remains false because
    # it preserves the obsolete per-primitive branch-leak criterion.
    raw = CK.run(0, 1)

    physical_pass = (
        he_regression < 1e-9
        and support_match
        and allj_vleak < 1e-10
        and raw["outer_complete_basis_leakage"] < 1e-10
        and raw["outer_wrong_charge_fraction"] < 1e-18
        and raw["internal_volume_sector_leakage"] < 1e-10
        and raw["HE_wrong_charge_fraction"] < 1e-18
        and raw["K_wrong_charge_fraction"] < 1e-18
        and raw["C_matrix_Frobenius_covariant_state_norm"] > 1e-10
        and raw["C_J1_weight"] > 1e-14
        and raw["C_J_greater_than_1_weight_fraction"] < 1e-18
        and raw["max_spin_reached"] <= 2.5 + 1e-12
    )

    # Preserve the historical diagnostic explicitly: the new gate should not
    # silently erase the reason the old run was red.
    history_preserved = (
        not raw["passed"]
        and raw["complete_charge_basis_leakage"] > 0.5
    )

    return {
        "status": "invariant projection audit for matrix-covariant C_e(K)",
        "passed": bool(physical_pass and history_preserved),
        "historical_raw_CK_passed": bool(raw["passed"]),
        "historical_primitive_branch_projection_diagnostic": raw["complete_charge_basis_leakage"],
        "historical_fail_preserved": bool(history_preserved),
        "allJ_Gauss_HE_support": len(allj_gauss),
        "safe_HE_support": len(safe),
        "allJ_vs_safe_support_identical": bool(support_match),
        "allJ_vs_safe_HE_relative_column_error": he_regression,
        "allJ_internal_volume_sector_leakage": allj_vleak,
        "full_charged_HE_wrong_charge_fraction": raw["HE_wrong_charge_fraction"],
        "full_charged_K_wrong_charge_fraction": raw["K_wrong_charge_fraction"],
        "outer_wrong_charge_fraction": raw["outer_wrong_charge_fraction"],
        "C_matrix_Frobenius_covariant_state_norm": raw["C_matrix_Frobenius_covariant_state_norm"],
        "C_weight_by_source_J": raw["C_weight_by_source_J"],
        "C_J_greater_than_1_weight_fraction": raw["C_J_greater_than_1_weight_fraction"],
        "max_spin_reached": raw["max_spin_reached"],
        "invariant_interpretation": (
            "The all-J internal-volume engine reproduces the independently existing safe Gauss H_E column after linear projection, while the complete charged H_E/K sums preserve J=1/2 and C_e(K) transforms only as source J=0+1. The old max per-primitive non-Gauss branch norm is retained as history but is not an operator covariance defect."
        ),
        "next_use": (
            "If green, C_e(K) is accepted as a finite matrix-covariant Lorentzian brick and the next gate is the traced epsilon^{ijk} product of two K legs and one V leg, which must return a pure source J=0 scalar."
        ),
        "scope_note": "Finite single-edge/single-input amplitude audit; full Lorentzian triple and HDA remain open."
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path)
    a = ap.parse_args()
    out = run(); text = json.dumps(out, indent=2); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
