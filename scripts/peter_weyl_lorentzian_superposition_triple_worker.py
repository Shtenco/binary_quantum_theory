#!/usr/bin/env python3
"""Exact ordered Lorentzian triple worker on an arbitrary Gauss NPZ state.

Loads a sparse ordinary-Gauss state, optionally selects a deterministic linear
shard, applies one production physical-sine ordered triple to the whole shard,
and writes the exact ordinary-Gauss output as NPZ.

This worker relies on peter_weyl_lorentzian_superposition_gate.py, whose
linearity gate must pass before this path is promoted for the full LL run.
Sharding is strictly linear resource partitioning; physics and coefficients are
unchanged.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_lorentzian_logical_projection_gate as LP
import peter_weyl_lorentzian_superposition_gate as SUP

TOL=1e-10


def load_state(path):
    z=np.load(path,allow_pickle=False)
    out={}
    for spins,Ks,amp in zip(z['spins'],z['Ks'],z['amp']):
        key=(tuple(int(x) for x in spins),tuple(int(x) for x in Ks))
        c=complex(amp)
        if abs(c)>TOL:
            out[key]=c
    return out


def save_state(path,state):
    rows=sorted(state.items(),key=lambda kv:repr(kv[0]))
    if rows:
        spins=np.asarray([k[0] for k,_ in rows],dtype=np.int16)
        Ks=np.asarray([k[1] for k,_ in rows],dtype=np.int16)
        amp=np.asarray([a for _,a in rows],dtype=np.complex128)
    else:
        spins=np.zeros((0,len(PW.EDGES)),dtype=np.int16)
        Ks=np.zeros((0,len(PW.VERT)),dtype=np.int16)
        amp=np.zeros((0,),dtype=np.complex128)
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    np.savez_compressed(path,spins=spins,Ks=Ks,amp=amp)


def norm2(state):
    return float(sum(abs(a)**2 for a in state.values()))


def max_spin(state):
    return max((max(k[0]) for k in state),default=0)/2.0


def shard_state(state,index,count):
    if count<1 or not 0<=index<count:
        raise ValueError('invalid shard index/count')
    rows=sorted(state.items(),key=lambda kv:repr(kv[0]))
    return {k:a for n,(k,a) in enumerate(rows) if n%count==index}


def run(input_path,source,a,b,c,coefficient,jmax2,shard_index=0,shard_count=1):
    if coefficient not in (-1,1):
        raise ValueError('coefficient must be +/-1')
    state=load_state(input_path)
    piece=shard_state(state,shard_index,shard_count)
    restore,caches=LP.install_sine_cached_stack()
    try:
        out,diag,accepted2,rejected2=SUP.ordered_triple_gauss_from_gauss(
            piece,source,a,b,c,jmax2
        )
        physical=max(
            float(diag.get('CV_complete_basis_leakage',0.0)),
            float(diag.get('CK_outer_complete_basis_leakage',0.0)),
            float(diag.get('CK_internal_volume_sector_leakage',0.0)),
        )
        cache_info={
            name:{'hits':fn.cache_info().hits,'misses':fn.cache_info().misses,'currsize':fn.cache_info().currsize}
            for name,fn in caches.items()
        }
    finally:
        restore()

    nout=math.sqrt(norm2(out))
    reject=math.sqrt(max(rejected2,0.0))
    checks={
        'input_loaded':len(state)>0,
        'shard_nonempty':len(piece)>0,
        'finite_output_norm':math.isfinite(nout),
        'finite_output_amplitudes':all(np.isfinite([z.real,z.imag]).all() for z in out.values()),
        'physical_basis_volume_leakage':physical<1e-8,
        'nonscalar_rejected_norm':reject<1e-8,
        'output_spin_within_wall':max_spin(out)<=jmax2/2+1e-12,
    }
    return out,{
        'status':'exact ordered Lorentzian triple on a Gauss superposition shard',
        'passed':all(checks.values()),
        'input_file':str(input_path),
        'input_support':len(state),
        'input_norm':math.sqrt(norm2(state)),
        'shard_index':shard_index,
        'shard_count':shard_count,
        'shard_support':len(piece),
        'shard_norm':math.sqrt(norm2(piece)),
        'source_node':source,
        'ordered_edges':[a,b,c],
        'epsilon_coefficient':coefficient,
        'Jmax':jmax2/2,
        'output_support':len(out),
        'output_norm':nout,
        'output_max_spin':max_spin(out),
        'scalar_accepted_norm':math.sqrt(max(accepted2,0.0)),
        'nonscalar_rejected_norm':reject,
        'max_physical_basis_volume_leakage':physical,
        'cache_info':cache_info,
        'checks':checks,
        'weighted_here':False,
        'scope':'One exact linear shard of one ordered triple; collectors perform shard sum and epsilon-oriented 24-term sum.',
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--source',type=int,required=True)
    p.add_argument('--a',type=int,required=True); p.add_argument('--b',type=int,required=True); p.add_argument('--c',type=int,required=True)
    p.add_argument('--coefficient',type=int,required=True)
    p.add_argument('--jmax2',type=int,required=True)
    p.add_argument('--shard-index',type=int,default=0); p.add_argument('--shard-count',type=int,default=1)
    p.add_argument('--json-output',type=Path,required=True); p.add_argument('--state-output',type=Path,required=True)
    x=p.parse_args(); state,out=run(x.input,x.source,x.a,x.b,x.c,x.coefficient,x.jmax2,x.shard_index,x.shard_count)
    x.json_output.parent.mkdir(parents=True,exist_ok=True)
    x.json_output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    save_state(x.state_output,state)
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if out['passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
