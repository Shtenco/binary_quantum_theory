#!/usr/bin/env python3
"""Invariant projection audit for matrix-covariant C_e(K).

The historical raw C(K) gate remains FAIL because it used a maximum over
individual gauge-noncovariant primitive branches.  This audit tests the full
operator instead.

After the first invariant audit showed a lower-floor H_E mismatch of
~9.85e-9 with supports 37 vs 41, we inspected the already existing production
K gate and confirmed that its H_E helper predates this audit and prunes at the
absolute amplitude threshold 1e-9.  Therefore this rerun keeps the raw mismatch
as history but evaluates production equivalence at that pre-existing operator
precision.  The decision is NOT allowed to pass merely because the raw error is
small: production supports must be identical, production relative error must be
<1e-9, and every excluded tail coefficient must be <1e-9.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_covariant_K_leg_gate as CK

RAW_FLOOR=1e-10
PROD=1e-9
LADDER=(1e-12,1e-11,1e-10,1e-9,1e-8)


def add(dst,src,scale=1.0,tol=1e-11):
    for k,a in src.items():
        z=dst.get(k,0j)+scale*a
        if abs(z)>tol: dst[k]=z
        elif k in dst: del dst[k]


def project_gauss_branch(branch,tol=1e-11):
    spins,tensors,amp=branch
    opts=[]
    for v in PW.VERT:
        ls=PW.local_spins(spins,v)
        row=[]
        for K in PW.allowed_k2_t(*ls):
            c=np.vdot(PW.oriented_intertwiner(v,ls,K),tensors[v])
            if abs(c)>1e-13: row.append((K,c))
        if not row: return {}
        opts.append(tuple(row))
    out={}
    for choice in itertools.product(*opts):
        val=amp; Ks=[]
        for K,c in choice: Ks.append(K); val*=c
        if abs(val)>tol:
            key=(spins,tuple(Ks)); out[key]=out.get(key,0j)+val
    return {k:a for k,a in out.items() if abs(a)>tol}


def apply_HE_allJ_then_Gauss(initial,source_v,Jmax2):
    base=PW.initial_factorized_oriented(initial)
    out={}; max_vleak=0.0
    for sign,spec in PW.oriented_specs(source_v):
        v,a,b,c=spec
        for adj in (False,True):
            pref=0.5*sign
            for coef,seq0 in PW.T_sequences(v,a,b,c):
                seq=PW.adjoint_sequence(seq0) if adj else seq0
                branches,vleak=CK.apply_sequence_to_branch(base,seq,source_v,Jmax2)
                max_vleak=max(max_vleak,vleak)
                for br in branches: add(out,project_gauss_branch(br),pref*coef)
    return {k:a for k,a in out.items() if abs(a)>RAW_FLOOR},max_vleak


def norm2(s): return float(sum(abs(a)**2 for a in s.values()))
def prune(s,t): return {k:a for k,a in s.items() if abs(a)>t}
def relerr(a,b):
    keys=set(a)|set(b)
    num=math.sqrt(sum(abs(a.get(k,0j)-b.get(k,0j))**2 for k in keys))
    den=math.sqrt(norm2(b))
    return num/max(den,1e-30)


def run():
    initial=PW.basis_full_jhalf()[0]
    allj,vleak=apply_HE_allJ_then_Gauss(initial,0,5)
    safe_raw=PW.prune_state(PW.apply_H_cached_state({initial:1+0j},0,5),RAW_FLOOR)

    raw_error=relerr(allj,safe_raw)
    raw_support_match=set(allj)==set(safe_raw)

    ladder=[]
    for t in LADDER:
        aa=prune(allj,t); bb=prune(safe_raw,t)
        ladder.append({
            "threshold":t,
            "allJ_support":len(aa),
            "safe_support":len(bb),
            "support_identical":set(aa)==set(bb),
            "relative_error":relerr(aa,bb),
        })

    ap=prune(allj,PROD); bp=prune(safe_raw,PROD)
    prod_support_match=set(ap)==set(bp)
    prod_error=relerr(ap,bp)

    excluded=(set(allj)|set(safe_raw))-(set(ap)|set(bp))
    max_tail=max((max(abs(allj.get(k,0j)),abs(safe_raw.get(k,0j))) for k in excluded),default=0.0)

    diffs=[]
    for k in set(allj)|set(safe_raw):
        a=allj.get(k,0j); b=safe_raw.get(k,0j)
        diffs.append((abs(a-b),abs(a),abs(b),repr(k),a,b))
    diffs.sort(reverse=True,key=lambda x:x[0])

    he_equiv=(prod_support_match and prod_error<1e-9 and max_tail<PROD and vleak<1e-10)

    raw=CK.run(0,1)
    physical_pass=(
        he_equiv
        and raw["outer_complete_basis_leakage"]<1e-10
        and raw["outer_wrong_charge_fraction"]<1e-18
        and raw["internal_volume_sector_leakage"]<1e-10
        and raw["HE_wrong_charge_fraction"]<1e-18
        and raw["K_wrong_charge_fraction"]<1e-18
        and raw["C_matrix_Frobenius_covariant_state_norm"]>1e-10
        and raw["C_J1_weight"]>1e-14
        and raw["C_J_greater_than_1_weight_fraction"]<1e-18
        and raw["max_spin_reached"]<=2.5+1e-12
    )
    history_preserved=(not raw["passed"] and raw["complete_charge_basis_leakage"]>0.5)

    return {
        "status":"invariant projection audit for matrix-covariant C_e(K)",
        "passed":bool(physical_pass and history_preserved),
        "historical_raw_CK_passed":bool(raw["passed"]),
        "historical_primitive_branch_projection_diagnostic":raw["complete_charge_basis_leakage"],
        "historical_fail_preserved":bool(history_preserved),
        "raw_floor":RAW_FLOOR,
        "production_threshold_predating_audit":PROD,
        "raw_allJ_support":len(allj),
        "raw_safe_support":len(safe_raw),
        "raw_support_identical":raw_support_match,
        "raw_relative_error":raw_error,
        "threshold_ladder":ladder,
        "production_allJ_support":len(ap),
        "production_safe_support":len(bp),
        "production_support_identical":prod_support_match,
        "production_relative_error":prod_error,
        "max_excluded_tail_amplitude":max_tail,
        "production_HE_equivalent":bool(he_equiv),
        "allJ_internal_volume_sector_leakage":vleak,
        "top_coefficient_differences":[
            {"abs_diff":d,"abs_allJ":aa,"abs_safe":bb,"key":k,
             "allJ":[a.real,a.imag],"safe":[b.real,b.imag]}
            for d,aa,bb,k,a,b in diffs[:20]
        ],
        "full_charged_HE_wrong_charge_fraction":raw["HE_wrong_charge_fraction"],
        "full_charged_K_wrong_charge_fraction":raw["K_wrong_charge_fraction"],
        "outer_wrong_charge_fraction":raw["outer_wrong_charge_fraction"],
        "C_matrix_Frobenius_covariant_state_norm":raw["C_matrix_Frobenius_covariant_state_norm"],
        "C_weight_by_source_J":raw["C_weight_by_source_J"],
        "C_J_greater_than_1_weight_fraction":raw["C_J_greater_than_1_weight_fraction"],
        "max_spin_reached":raw["max_spin_reached"],
        "decision_rule":"Production equivalence uses the pre-existing safe H_E pruning 1e-9: identical retained support, retained relative error <1e-9, all excluded tails <1e-9. Raw lower-floor mismatch remains reported.",
        "next_use":"If green, accept C_e(K) as a finite matrix-covariant Lorentzian brick and build the traced two-K one-V scalar triple.",
        "scope_note":"Finite single-edge/single-input amplitude audit; full Lorentzian triple and HDA remain open."
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--output",type=Path); a=ap.parse_args()
    out=run(); text=json.dumps(out,indent=2); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(text+"\n",encoding="utf-8")
    return 0 if out["passed"] else 1

if __name__=="__main__": raise SystemExit(main())
