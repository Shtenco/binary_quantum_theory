#!/usr/bin/env python3
"""V2 six-term cache-sharing PL Lorentzian shard with tetrahedral volume.

Execution grouping is inherited unchanged from pl_lorentzian_group_worker.py.
Only the charged/intermediate volume backend is replaced by the preregistered
four-leg tetrahedral completion.
"""
from __future__ import annotations
import argparse,json,traceback
from pathlib import Path
import pl_lorentzian_group_worker as BASE
from tetrahedral_volume_backend import install_tetrahedral_volume_backend

def run(mode,slot,outdir,source=0):
    with install_tetrahedral_volume_backend():
        out=BASE.run(mode,slot,outdir,source)
    out['operator_version']='tetrahedral-charged-volume-v2'
    out['volume_definition']='V_tet=sqrt(abs((1/4) sum_r (-1)^r q_hat_r)) with production zero-aware spectrum'
    for row in out.get('terms',[]):
        row['operator_version']='tetrahedral-charged-volume-v2'
    # Rewrite the already-emitted per-term metadata with the V2 provenance while
    # preserving their exact amplitudes/states.
    for idx in out.get('indices',[]):
        p=Path(outdir)/f'term_{mode}_{idx}.json'
        if p.exists():
            d=json.loads(p.read_text(encoding='utf-8'));d['operator_version']='tetrahedral-charged-volume-v2';d['volume_definition']=out['volume_definition'];p.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    return out

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--mode',choices=('forward','adjoint'),required=True);p.add_argument('--first-slot',type=int,choices=range(4),required=True);p.add_argument('--source',type=int,default=0);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True)
    try:o=run(a.mode,a.first_slot,a.out_dir,a.source);code=0 if o['passed'] else 1
    except Exception as exc:o={'status':'shard exception','passed':False,'operator_version':'tetrahedral-charged-volume-v2','mode':a.mode,'first_actual_local_slot':a.first_slot,'error_type':type(exc).__name__,'error':str(exc),'traceback':traceback.format_exc()};code=1
    (a.out_dir/f'shard_{a.mode}_{a.first_slot}.json').write_text(json.dumps(o,indent=2,sort_keys=True)+'\n',encoding='utf-8');print(json.dumps(o,indent=2,sort_keys=True));return code
if __name__=='__main__':raise SystemExit(main())
