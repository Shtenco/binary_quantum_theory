#!/usr/bin/env python3
"""V2 exact PL Lorentzian ordered-term worker with tetrahedral charged volume.

All algebra, PL epsilon signs, cutoffs, scalar projection and acceptance logic
come from pl_lorentzian_triple_worker.py.  The only physical change is the
preregistered charged/intermediate volume completion installed by
``tetrahedral_volume_backend``.
"""
from __future__ import annotations
import argparse,json,traceback
from pathlib import Path
import pl_lorentzian_triple_worker as BASE
from tetrahedral_volume_backend import install_tetrahedral_volume_backend
from pl_dual_complex import DualComplex,seed_16cell_boundary

def run(index,mode='forward',source=0):
    with install_tetrahedral_volume_backend():
        state,out=BASE.run(index,mode,source)
    out['operator_version']='tetrahedral-charged-volume-v2'
    out['supersedes']='fixed-q123 charged extension before any complete PL Lorentzian science result'
    out['volume_definition']='V_tet=sqrt(abs((1/4) sum_r (-1)^r q_hat_r)) with production zero-aware spectrum'
    return state,out

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--index',type=int,required=True);p.add_argument('--mode',choices=('forward','adjoint'),required=True);p.add_argument('--source',type=int,default=0);p.add_argument('--json-output',type=Path,required=True);p.add_argument('--state-output',type=Path,required=True);a=p.parse_args()
    try:state,out=run(a.index,a.mode,a.source);code=0 if out['passed'] else 1
    except Exception as exc:state={};out={'status':'worker exception','passed':False,'operator_version':'tetrahedral-charged-volume-v2','mode':a.mode,'index':a.index,'error_type':type(exc).__name__,'error':str(exc),'traceback':traceback.format_exc()};code=1
    D=DualComplex(seed_16cell_boundary());BASE.save_state(a.state_output,state,len(D.dual_edges()),D.n_tets);a.json_output.parent.mkdir(parents=True,exist_ok=True);a.json_output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8');print(json.dumps(out,indent=2,sort_keys=True));return code
if __name__=='__main__':raise SystemExit(main())
