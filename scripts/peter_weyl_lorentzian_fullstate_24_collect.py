#!/usr/bin/env python3
"""Collect the 24 exact full-state ordered Lorentzian triple artifacts.

Each worker returns an unweighted ordinary Gauss sparse state and an independently
frozen epsilon coefficient +/-1.  This collector applies those coefficients and
forms the exact raw node operator column

    L_raw |g> = sum_{24 terms} s_abc T_abc |g>.

No logical projection, phase completion or physical real coefficient is applied.
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
        spins=np.zeros((0,10),dtype=np.int16); Ks=np.zeros((0,5),dtype=np.int16); amp=np.zeros((0,),complex)
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    np.savez_compressed(path,spins=spins,Ks=Ks,amp=amp)


def add(dst,src,scale=1.0,tol=TOL):
    for k,a in src.items():
        z=dst.get(k,0j)+scale*a
        if abs(z)>tol: dst[k]=z
        elif k in dst: del dst[k]


def norm2(s): return float(sum(abs(a)**2 for a in s.values()))
def max_spin(s): return max((max(k[0]) for k in s),default=0)/2.0


def run(input_dir):
    d=Path(input_dir); total={}; rows=[]; max_leak=0.0; max_reject=0.0
    missing=[]
    for tag,coef in EXPECTED.items():
        jp=d/f'T_{tag}.json'; sp=d/f'T_{tag}.npz'
        if not jp.exists() or not sp.exists():
            missing.append(tag); continue
        meta=json.loads(jp.read_text(encoding='utf-8'))
        state=load_state(sp)
        if int(meta['epsilon_coefficient'])!=coef:
            raise RuntimeError(f'coefficient mismatch for {tag}: {meta["epsilon_coefficient"]} vs {coef}')
        add(total,state,coef)
        max_leak=max(max_leak,float(meta.get('physical_acceptance_max_leakage',0.0)))
        max_reject=max(max_reject,float(meta.get('nonscalar_rejected_norm',0.0)))
        rows.append({
            'tag':tag,'coefficient':coef,'worker_passed':bool(meta.get('passed',False)),
            'gauss_support':len(state),'gauss_norm':math.sqrt(norm2(state)),
            'gauss_max_spin':max_spin(state),
        })
    checks={
        'all_24_artifacts_present':not missing and len(rows)==24,
        'all_workers_passed':len(rows)==24 and all(x['worker_passed'] for x in rows),
        'physical_leakage':max_leak<1e-8,
        'nonscalar_rejection':max_reject<1e-8,
        'finite_total_norm':math.isfinite(math.sqrt(norm2(total))),
        'single_HL_wall':max_spin(total)<=3.5+1e-12,
    }
    return total,{
        'status':'exact 24-way full-state Lorentzian raw node column collector',
        'passed':all(checks.values()),
        'source_node':0,'Jmax':3.5,
        'missing_tags':missing,
        'ordered_terms':rows,
        'raw_L_support':len(total),
        'raw_L_norm':math.sqrt(norm2(total)),
        'raw_L_max_spin':max_spin(total),
        'max_physical_acceptance_leakage':max_leak,
        'max_nonscalar_rejected_norm':max_reject,
        'checks':checks,
        'phase_completed':False,
        'physical_real_coefficient_applied':False,
        'next_use':'Use this exact Gauss column as the first L layer for distributed EL/LL and as a benchmark for the general state-action adapter.',
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input-dir',type=Path,required=True)
    p.add_argument('--json-output',type=Path,required=True)
    p.add_argument('--state-output',type=Path,required=True)
    a=p.parse_args(); state,out=run(a.input_dir)
    a.json_output.parent.mkdir(parents=True,exist_ok=True)
    a.json_output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    save_state(a.state_output,state)
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if out['passed'] else 1

if __name__=='__main__': raise SystemExit(main())
