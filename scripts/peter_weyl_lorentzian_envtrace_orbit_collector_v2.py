#!/usr/bin/env python3
"""V2 provenance-locked S4 env-trace collector for corrected raw one-body L.

Requires all input environment blocks to have tetrahedral charged-volume V2
provenance, then delegates the exact S4 sign-twirl algebra to the historical
collector.  No historical coefficient is imposed as a target.
"""
from __future__ import annotations
import argparse,json,traceback
from pathlib import Path
import peter_weyl_lorentzian_envtrace_orbit_collector as OLD
VERSION='tetrahedral-charged-volume-v2'

def preflight(root):
    rows=[]
    for p in Path(root).rglob('block_*.json'):
        d=json.loads(p.read_text(encoding='utf-8'));rows.append((p,d))
    if len(rows)!=8:raise RuntimeError(f'need exactly 8 corrected block files (123/132 x 4 env batches), got {len(rows)}')
    bad=[str(p) for p,d in rows if d.get('operator_version')!=VERSION]
    if bad:raise RuntimeError(f'non-V2 envtrace inputs: {bad}')
    triples={tuple(d['ordered_edges']) for _,d in rows}
    if triples!={(1,2,3),(1,3,2)}:raise RuntimeError(f'wrong triple set {triples}')
    return rows

def run(root):
    preflight(root);out=OLD.run(Path(root));out['operator_version']=VERSION;out['science_status']='CORRECTED_K5_ONEBODY_RAW_V2';out['historical_fixed_q123_coefficient_for_comparison']=[0.0,1.3389293521464034]
    new=complex(*out['onebody_Y_coefficient_raw']);old=1j*1.3389293521464034
    out['relative_change_vs_historical_fixed_q123']=float(abs(new-old)/max(abs(old),1e-30))
    out['comparison_is_diagnostic_not_acceptance']=True
    return out

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    try:o=run(a.root);code=0 if o['passed'] else 1
    except Exception as exc:o={'status':'V2 envtrace collector exception','passed':False,'operator_version':VERSION,'error_type':type(exc).__name__,'error':str(exc),'traceback':traceback.format_exc()};code=1
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8');print(json.dumps(o,indent=2));return code
if __name__=='__main__':raise SystemExit(main())
