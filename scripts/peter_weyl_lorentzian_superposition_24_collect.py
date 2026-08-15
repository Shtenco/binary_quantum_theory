#!/usr/bin/env python3
"""Exact collector for sharded 24-term Lorentzian superposition workers.

Expected worker files:

    T_<tag>_S<shard>.json/.npz

for all 24 orientation tags and `shard=0..shard_count-1`.

The collector first sums shards for each ordered triple with coefficient +1,
then applies the frozen epsilon orientation coefficient +/-1 and sums all 24
triples.  This order is exactly equivalent by linearity.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

EXPECTED={
 '234':+1,'243':-1,'324':-1,'342':+1,'423':+1,'432':-1,
 '134':-1,'143':+1,'314':+1,'341':-1,'413':-1,'431':+1,
 '124':+1,'142':-1,'214':-1,'241':+1,'412':+1,'421':-1,
 '123':-1,'132':+1,'213':+1,'231':-1,'312':-1,'321':+1,
}
TOL=1e-10


def load_state(path):
    z=np.load(path,allow_pickle=False)
    out={}
    for spins,Ks,amp in zip(z['spins'],z['Ks'],z['amp']):
        out[(tuple(int(x) for x in spins),tuple(int(x) for x in Ks))]=complex(amp)
    return out


def save_state(path,state):
    rows=sorted(state.items(),key=lambda kv:repr(kv[0]))
    if rows:
        spins=np.asarray([k[0] for k,_ in rows],dtype=np.int16)
        Ks=np.asarray([k[1] for k,_ in rows],dtype=np.int16)
        amp=np.asarray([a for _,a in rows],dtype=np.complex128)
    else:
        spins=np.zeros((0,10),dtype=np.int16); Ks=np.zeros((0,5),dtype=np.int16); amp=np.zeros((0,),dtype=np.complex128)
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    np.savez_compressed(path,spins=spins,Ks=Ks,amp=amp)


def add(dst,src,scale=1.0,tol=TOL):
    for k,a in src.items():
        z=dst.get(k,0j)+scale*a
        if abs(z)>tol: dst[k]=z
        elif k in dst: del dst[k]


def norm2(s): return float(sum(abs(a)**2 for a in s.values()))
def max_spin(s): return max((max(k[0]) for k in s),default=0)/2.0


def run(input_dir,source,jmax2,shard_count):
    d=Path(input_dir); total={}; term_rows=[]; missing=[]; max_leak=0.0; max_reject=0.0
    for tag,coef in EXPECTED.items():
        term={}; shard_rows=[]
        for s in range(shard_count):
            jp=d/f'T_{tag}_S{s}.json'; sp=d/f'T_{tag}_S{s}.npz'
            if not jp.exists() or not sp.exists():
                missing.append(f'{tag}:S{s}'); continue
            meta=json.loads(jp.read_text(encoding='utf-8')); st=load_state(sp)
            if int(meta['epsilon_coefficient'])!=coef:
                raise RuntimeError(f'coefficient mismatch {tag}: {meta["epsilon_coefficient"]} != {coef}')
            if int(meta['source_node'])!=source:
                raise RuntimeError(f'source mismatch {tag}: {meta["source_node"]} != {source}')
            add(term,st,+1)
            max_leak=max(max_leak,float(meta.get('max_physical_basis_volume_leakage',0.0)))
            max_reject=max(max_reject,float(meta.get('nonscalar_rejected_norm',0.0)))
            shard_rows.append({'shard':s,'passed':bool(meta.get('passed',False)),'support':len(st),'norm':math.sqrt(norm2(st))})
        add(total,term,coef)
        term_rows.append({'tag':tag,'coefficient':coef,'shards':shard_rows,'unweighted_support':len(term),'unweighted_norm':math.sqrt(norm2(term))})

    all_workers=[x for t in term_rows for x in t['shards']]
    checks={
        'all_artifacts_present':not missing and len(all_workers)==24*shard_count,
        'all_workers_passed':len(all_workers)==24*shard_count and all(x['passed'] for x in all_workers),
        'physical_leakage':max_leak<1e-8,
        'nonscalar_rejection':max_reject<1e-8,
        'finite_total_norm':math.isfinite(math.sqrt(norm2(total))),
        'output_spin_within_wall':max_spin(total)<=jmax2/2+1e-12,
    }
    return total,{
        'status':'exact sharded 24-term Lorentzian superposition collector',
        'passed':all(checks.values()),
        'source_node':source,'Jmax':jmax2/2,'shard_count':shard_count,
        'missing':missing,'ordered_terms':term_rows,
        'raw_L_support':len(total),'raw_L_norm':math.sqrt(norm2(total)),'raw_L_max_spin':max_spin(total),
        'max_physical_basis_volume_leakage':max_leak,'max_nonscalar_rejected_norm':max_reject,
        'checks':checks,'phase_completed':False,'physical_real_coefficient_applied':False,
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input-dir',type=Path,required=True); p.add_argument('--source',type=int,required=True)
    p.add_argument('--jmax2',type=int,required=True); p.add_argument('--shard-count',type=int,default=1)
    p.add_argument('--json-output',type=Path,required=True); p.add_argument('--state-output',type=Path,required=True)
    a=p.parse_args(); state,out=run(a.input_dir,a.source,a.jmax2,a.shard_count)
    a.json_output.parent.mkdir(parents=True,exist_ok=True)
    a.json_output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    save_state(a.state_output,state)
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if out['passed'] else 1

if __name__=='__main__': raise SystemExit(main())
