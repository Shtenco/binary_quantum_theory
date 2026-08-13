#!/usr/bin/env python3
from __future__ import annotations
import json, math, sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_covariant_K_projection_audit_gate as AUD

THRESHOLDS=(1e-12,1e-11,1e-10,1e-9,1e-8)
PROD=1e-9

def norm2(s): return float(sum(abs(a)**2 for a in s.values()))
def relerr(a,b):
    keys=set(a)|set(b)
    num=math.sqrt(sum(abs(a.get(k,0j)-b.get(k,0j))**2 for k in keys))
    den=math.sqrt(norm2(b))
    return num/max(den,1e-30)
def prune(s,t): return {k:a for k,a in s.items() if abs(a)>t}

def run():
    initial=PW.basis_full_jhalf()[0]
    allj,_=AUD.apply_HE_allJ_then_Gauss(initial,0,5)
    # Build the independently existing safe column with the same low diagnostic floor.
    safe=PW.prune_state(PW.apply_H_cached_state({initial:1+0j},0,5),1e-12)
    keys=set(allj)|set(safe)
    diffs=[]
    for k in keys:
        a=allj.get(k,0j); b=safe.get(k,0j)
        diffs.append((abs(a-b),abs(a),abs(b),repr(k),a,b))
    diffs.sort(reverse=True,key=lambda x:x[0])
    ladder=[]
    for t in THRESHOLDS:
        aa=prune(allj,t); bb=prune(safe,t)
        ladder.append({"threshold":t,"allJ_support":len(aa),"safe_support":len(bb),"support_identical":set(aa)==set(bb),"relative_error":relerr(aa,bb)})
    ap=prune(allj,PROD); bp=prune(safe,PROD)
    low_extra=[]
    for k in (set(allj)|set(safe))-(set(ap)|set(bp)):
        low_extra.append(max(abs(allj.get(k,0j)),abs(safe.get(k,0j))))
    max_tail=max(low_extra,default=0.0)
    passed=(set(ap)==set(bp) and relerr(ap,bp)<1e-9 and max_tail<PROD)
    return {
      "status":"H_E support-tail numerical audit",
      "passed":bool(passed),
      "production_threshold":PROD,
      "raw_allJ_support":len(allj),"raw_safe_support":len(safe),
      "raw_relative_error":relerr(allj,safe),
      "threshold_ladder":ladder,
      "production_support_identical":set(ap)==set(bp),
      "production_relative_error":relerr(ap,bp),
      "max_excluded_tail_amplitude":max_tail,
      "top_differences":[{"abs_diff":d,"abs_allJ":aa,"abs_safe":bb,"key":k,"allJ":[a.real,a.imag],"safe":[b.real,b.imag]} for d,aa,bb,k,a,b in diffs[:20]],
      "decision_rule":"PASS only if supports at predating 1e-9 production pruning are identical, retained relative error <1e-9, and all excluded tail amplitudes are <1e-9."
    }

def main():
    out=run(); print(json.dumps(out,indent=2)); return 0 if out['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
