#!/usr/bin/env python3
"""Generic exact collector for a 24-way full-state Lorentzian node column.

Unlike the historical source-0 collector, the expected orientation table is
generated from PW.NEIG[source] using the production epsilon convention. This is
needed for source node 1, whose ordered neighbors are (0,2,3,4).
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

TOL=1e-10


def parity(base,perm):
    idx=[base.index(x) for x in perm]
    inv=sum(idx[i]>idx[j] for i in range(3) for j in range(i+1,3))
    return -1 if inv%2 else 1


def expected(source):
    neigh=PW.NEIG[source]; out={}
    for r,omit in enumerate(neigh):
        base=tuple(x for x in neigh if x!=omit); face=(-1)**r
        for perm in itertools.permutations(base):
            out[''.join(str(x) for x in perm)]=face*parity(base,perm)
    if len(out)!=24:
        raise RuntimeError(f'expected 24 distinct terms, got {len(out)}')
    return out


def load_state(path):
    z=np.load(path,allow_pickle=False); out={}
    for spins,Ks,amp in zip(z['spins'],z['Ks'],z['amp']):
        out[(tuple(int(x) for x in spins),tuple(int(x) for x in Ks))]=complex(amp)
    return out


def save_state(path,state):
    rows=sorted(state.items(),key=lambda kv:repr(kv[0]))
    if rows:
        spins=np.asarray([k[0] for k,_ in rows],dtype=np.int16); Ks=np.asarray([k[1] for k,_ in rows],dtype=np.int16); amp=np.asarray([a for _,a in rows],dtype=np.complex128)
    else:
        spins=np.zeros((0,len(PW.EDGES)),dtype=np.int16); Ks=np.zeros((0,len(PW.VERT)),dtype=np.int16); amp=np.zeros((0,),dtype=np.complex128)
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True); np.savez_compressed(path,spins=spins,Ks=Ks,amp=amp)


def add(dst,src,scale=1.0):
    for k,a in src.items():
        z=dst.get(k,0j)+scale*a
        if abs(z)>TOL: dst[k]=z
        elif k in dst: del dst[k]


def norm2(s): return float(sum(abs(a)**2 for a in s.values()))
def max_spin(s): return max((max(k[0]) for k in s),default=0)/2.0


def run(input_dir,source):
    d=Path(input_dir); E=expected(source); total={}; rows=[]; missing=[]; max_leak=0.0; max_reject=0.0
    for tag,coef in E.items():
        jp=d/f'T_{tag}.json'; sp=d/f'T_{tag}.npz'
        if not jp.exists() or not sp.exists():
            missing.append(tag); continue
        meta=json.loads(jp.read_text(encoding='utf-8')); st=load_state(sp)
        if int(meta['epsilon_coefficient'])!=coef: raise RuntimeError(f'coefficient mismatch {tag}')
        if int(meta['source_node'])!=source: raise RuntimeError(f'source mismatch {tag}')
        add(total,st,coef)
        max_leak=max(max_leak,float(meta.get('physical_acceptance_max_leakage',0.0)))
        max_reject=max(max_reject,float(meta.get('nonscalar_rejected_norm',0.0)))
        rows.append({'tag':tag,'coefficient':coef,'worker_passed':bool(meta.get('passed',False)),'support':len(st),'norm':math.sqrt(norm2(st)),'exact_zero':bool(meta.get('exact_zero_ordered_term',False))})
    checks={
        'all_24_present':not missing and len(rows)==24,
        'all_workers_passed':len(rows)==24 and all(x['worker_passed'] for x in rows),
        'physical_leakage':max_leak<1e-8,
        'nonscalar_rejection':max_reject<1e-8,
        'finite_total_norm':math.isfinite(math.sqrt(norm2(total))),
        'single_HL_wall':max_spin(total)<=3.5+1e-12,
    }
    return total,{
        'status':'exact generic 24-way full-state Lorentzian raw node column collector',
        'passed':all(checks.values()),'source_node':source,'neighbor_order':list(PW.NEIG[source]),'Jmax':3.5,
        'expected_orientation_table':E,'missing_tags':missing,'ordered_terms':rows,
        'raw_L_support':len(total),'raw_L_norm':math.sqrt(norm2(total)),'raw_L_max_spin':max_spin(total),
        'max_physical_acceptance_leakage':max_leak,'max_nonscalar_rejected_norm':max_reject,'checks':checks,
        'phase_completed':False,'physical_real_coefficient_applied':False,
    }


def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--input-dir',type=Path,required=True); p.add_argument('--source',type=int,required=True)
    p.add_argument('--json-output',type=Path,required=True); p.add_argument('--state-output',type=Path,required=True)
    a=p.parse_args(); state,out=run(a.input_dir,a.source)
    a.json_output.parent.mkdir(parents=True,exist_ok=True); a.json_output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8'); save_state(a.state_output,state)
    print(json.dumps(out,indent=2,sort_keys=True)); return 0 if out['passed'] else 1

if __name__=='__main__': raise SystemExit(main())
