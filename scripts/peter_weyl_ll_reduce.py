#!/usr/bin/env python3
"""Exact raw LL reducer: (L0 L1 - L1 L0)|psi> from two collected NPZ states."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import numpy as np

TOL=1e-10


def load(path):
    z=np.load(path,allow_pickle=False); out={}
    for spins,Ks,amp in zip(z['spins'],z['Ks'],z['amp']):
        out[(tuple(int(x) for x in spins),tuple(int(x) for x in Ks))]=complex(amp)
    return out


def save(path,state):
    rows=sorted(state.items(),key=lambda kv:repr(kv[0]))
    if rows:
        spins=np.asarray([k[0] for k,_ in rows],dtype=np.int16); Ks=np.asarray([k[1] for k,_ in rows],dtype=np.int16); amp=np.asarray([a for _,a in rows],dtype=np.complex128)
    else:
        spins=np.zeros((0,10),dtype=np.int16); Ks=np.zeros((0,5),dtype=np.int16); amp=np.zeros((0,),dtype=np.complex128)
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True); np.savez_compressed(path,spins=spins,Ks=Ks,amp=amp)


def norm2(s): return float(sum(abs(a)**2 for a in s.values()))
def max_spin(s): return max((max(k[0]) for k in s),default=0)/2.0


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--L0L1',type=Path,required=True); p.add_argument('--L1L0',type=Path,required=True)
    p.add_argument('--json-output',type=Path,required=True); p.add_argument('--state-output',type=Path,required=True)
    a=p.parse_args(); A=load(a.L0L1); B=load(a.L1L0); C=dict(A)
    for k,v in B.items():
        z=C.get(k,0j)-v
        if abs(z)>TOL: C[k]=z
        elif k in C: del C[k]
    nA=math.sqrt(norm2(A)); nB=math.sqrt(norm2(B)); nC=math.sqrt(norm2(C))
    out={
        'status':'exact raw LL commutator reducer',
        'passed':all(math.isfinite(x) for x in (nA,nB,nC)) and max_spin(C)<=6.5+1e-12,
        'definition':'C_LL=L0L1-L1L0',
        'L0L1_support':len(A),'L0L1_norm':nA,
        'L1L0_support':len(B),'L1L0_norm':nB,
        'LL_support':len(C),'LL_norm':nC,'LL_max_spin':max_spin(C),
        'signed_geometry_weight_applied_here':False,
        'signed_weight_for_full_geometry':'b^2=(32 i/9)^2=-1024/81',
        'scope':'Raw LL channel only; full geometry collector applies the frozen signed weight.',
    }
    a.json_output.parent.mkdir(parents=True,exist_ok=True); a.json_output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8'); save(a.state_output,C)
    print(json.dumps(out,indent=2,sort_keys=True)); return 0 if out['passed'] else 1

if __name__=='__main__': raise SystemExit(main())
