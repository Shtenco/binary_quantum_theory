#!/usr/bin/env python3
"""Focused invariant equivalence gate for the symmetry-adapted all-J H_E engine.

The current Lorentzian C_e(K) frontier depends on extending H_E to charged
representations.  Internal volume insertions in that extension are evaluated as

    V = direct_sum_J sqrt(|Q_J|).

Before trusting the charged extension, the same all-J volume implementation
must reproduce the independently existing regulator-safe Gauss H_E column on
the frozen all-j=1/2, all-K=0 input.  This script isolates only that question;
it does not recompute C_e(K).

Frozen criterion from PETER_WEYL_COVARIANT_K_PROJECTION_AUDIT.md:

    ||H_E^(allJ/P_G)-H_E^safe|| / ||H_E^safe|| < 1e-9.

Support equality is also required.  On failure the script reports norm overlap,
phase-aligned error, largest coefficient mismatch and whether differences are
confined to tiny amplitudes.  The 1e-9 criterion is not relaxed here.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_covariant_K_projection_audit_gate as AUD


def norm2(s):
    return float(sum(abs(a)**2 for a in s.values()))


def inner(a,b):
    return sum(np.conj(a.get(k,0j))*b.get(k,0j) for k in set(a)|set(b))


def diff_metrics(a,b):
    keys=set(a)|set(b)
    den=math.sqrt(norm2(b))
    diffs={k:a.get(k,0j)-b.get(k,0j) for k in keys}
    err=math.sqrt(sum(abs(z)**2 for z in diffs.values()))/max(den,1e-30)
    ov=inner(b,a)
    nb=math.sqrt(norm2(b)); na=math.sqrt(norm2(a))
    fidelity=abs(ov)**2/max((nb*na)**2,1e-60)
    phase=ov/abs(ov) if abs(ov)>0 else 1+0j
    # Compare after removing one global phase as a diagnostic only.  The actual
    # pass condition still uses the raw frozen column error above.
    aligned={k:a.get(k,0j)*np.conj(phase) for k in keys}
    aligned_err=math.sqrt(sum(abs(aligned[k]-b.get(k,0j))**2 for k in keys))/max(den,1e-30)
    ranked=sorted(keys,key=lambda k:abs(diffs[k]),reverse=True)
    largest=[]
    for k in ranked[:12]:
        aa=a.get(k,0j); bb=b.get(k,0j); dd=aa-bb
        largest.append({
            "max_spin":max(k[0])/2,
            "Ks":list(k[1]),
            "abs_allJ":abs(aa),
            "abs_safe":abs(bb),
            "abs_difference":abs(dd),
            "relative_to_safe_column_norm":abs(dd)/max(den,1e-30),
        })
    only_a=set(a)-set(b); only_b=set(b)-set(a)
    max_only_a=max((abs(a[k]) for k in only_a),default=0.0)
    max_only_b=max((abs(b[k]) for k in only_b),default=0.0)
    return err, aligned_err, fidelity, largest, only_a, only_b, max_only_a, max_only_b


def run():
    JMAX2=5
    initial=PW.basis_full_jhalf()[0]
    allj,vleak=AUD.apply_HE_allJ_then_Gauss(initial,0,JMAX2)
    safe=PW.prune_state(PW.apply_H_cached_state({initial:1+0j},0,JMAX2),1e-10)
    err,aligned_err,fidelity,largest,only_a,only_b,max_only_a,max_only_b=diff_metrics(allj,safe)
    support_equal=set(allj)==set(safe)
    passed=bool(err<1e-9 and support_equal and vleak<1e-10)
    return {
        "status":"focused all-J versus safe Peter-Weyl H_E equivalence audit",
        "passed":passed,
        "frozen_relative_error_threshold":1e-9,
        "allJ_support":len(allj),
        "safe_support":len(safe),
        "support_equal":support_equal,
        "only_allJ_support_count":len(only_a),
        "only_safe_support_count":len(only_b),
        "max_only_allJ_amplitude":max_only_a,
        "max_only_safe_amplitude":max_only_b,
        "allJ_norm":math.sqrt(norm2(allj)),
        "safe_norm":math.sqrt(norm2(safe)),
        "raw_relative_column_error":err,
        "global_phase_aligned_relative_error_diagnostic":aligned_err,
        "column_fidelity_squared":float(fidelity),
        "allJ_internal_volume_sector_leakage":vleak,
        "largest_coefficient_mismatches":largest,
        "verdict_if_fail":(
            "A FAIL is retained.  If the discrepancy is concentrated at the sqrt(machine-epsilon) volume floor, the next experiment must preregister a canonical/high-precision Gauss-volume reference and rerun old Euclidean regressions; the 1e-9 audit is not retroactively weakened."
        ),
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output",type=Path)
    a=ap.parse_args(); out=run(); text=json.dumps(out,indent=2); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(text+"\n",encoding="utf-8")
    return 0 if out["passed"] else 1

if __name__=="__main__":
    raise SystemExit(main())
