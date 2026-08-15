#!/usr/bin/env python3
"""Distributed exact channel worker for the preregistered full geometry commutator.

Computes one of

    EE = E0 E1 - E1 E0
    EL = E0 L1 - E1 L0
    LE = L0 E1 - L1 E0
    LL = L0 L1 - L1 L0

on the frozen all-j=1/2, all-K=0 input.  E is the raw physical sine ordering
H_E^sine; L is the full 24-term raw epsilon-oriented K_sine-K_sine-V node
operator projected exactly back to the general Gauss basis.

The signed physical coefficients are deliberately NOT applied here.  Each raw
channel is saved as a compressed NPZ sparse state so a separate collector can
form the exact weighted [G0,G1] without rerunning the expensive channel.
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
import peter_weyl_euclidean_sine_ordering_gate as SINE
import peter_weyl_lorentzian_gauss_action_gate as LGA
import peter_weyl_lorentzian_logical_projection_gate as LP
import peter_weyl_zeroaware_volume_migration_experiment as ZVM

PRUNE=1e-10
CHANNELS=('EE','EL','LE','LL')
WALLS={
    'EE':{'first_E':5,'second_E':5},
    'EL':{'first_L':7,'second_E':9},
    'LE':{'first_E':5,'second_L':9},
    'LL':{'first_L':7,'second_L':13},
}


def norm2(state):
    return float(sum(abs(a)**2 for a in state.values()))


def add(dst,src,scale=1.0,tol=PRUNE):
    for key,amp in src.items():
        z=dst.get(key,0j)+scale*amp
        if abs(z)>tol:
            dst[key]=z
        elif key in dst:
            del dst[key]


def max_spin(state):
    return max((max(key[0]) for key in state),default=0)/2.0


def E(state,node,jmax2):
    return PW.prune_state(SINE.safe_H_sine(state,node,jmax2),PRUNE)


def L_installed(state,node,jmax2):
    out,diag,rejected2,rows=LGA.apply_L_raw_state_installed(
        state,node,jmax2,PRUNE
    )
    return out,diag,rejected2,rows


def combine_diag(dst,src):
    for k,v in src.items():
        if isinstance(v,(int,float)):
            dst[k]=max(dst.get(k,0.0),float(v))


def apply_one(state,op,node,jmax2,lstack_installed):
    if op=='E':
        out=E(state,node,jmax2)
        return out,{},0.0,[]
    if op=='L':
        if not lstack_installed:
            raise RuntimeError('Lorentzian stack not installed')
        return L_installed(state,node,jmax2)
    raise ValueError(op)


def sequence(initial,left,left_node,right,right_node,channel,lstack_installed):
    walls=WALLS[channel]
    first_key=f'first_{right}'
    second_key=f'second_{left}'
    first,diag1,rej1,rows1=apply_one(
        {initial:1+0j},right,right_node,walls[first_key],lstack_installed
    )
    second,diag2,rej2,rows2=apply_one(
        first,left,left_node,walls[second_key],lstack_installed
    )
    diag={}; combine_diag(diag,diag1); combine_diag(diag,diag2)
    return second,{
        'right_operator':right,
        'right_node':right_node,
        'right_Jmax':walls[first_key]/2,
        'right_output_support':len(first),
        'right_output_norm':math.sqrt(norm2(first)),
        'right_max_spin':max_spin(first),
        'left_operator':left,
        'left_node':left_node,
        'left_Jmax':walls[second_key]/2,
        'final_support':len(second),
        'final_norm':math.sqrt(norm2(second)),
        'final_max_spin':max_spin(second),
        'max_diagnostics':diag,
        'nonscalar_rejected_norm':math.sqrt(max(rej1+rej2,0.0)),
        'right_L_input_columns':len(rows1),
        'left_L_input_columns':len(rows2),
    }


def channel_sequences(channel):
    if channel=='EE':
        return ('E',0,'E',1),('E',1,'E',0)
    if channel=='EL':
        return ('E',0,'L',1),('E',1,'L',0)
    if channel=='LE':
        return ('L',0,'E',1),('L',1,'E',0)
    if channel=='LL':
        return ('L',0,'L',1),('L',1,'L',0)
    raise ValueError(channel)


def save_state_npz(path,state):
    path=Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    rows=sorted(state.items(),key=lambda kv:repr(kv[0]))
    if rows:
        spins=np.asarray([k[0] for k,_ in rows],dtype=np.int16)
        Ks=np.asarray([k[1] for k,_ in rows],dtype=np.int16)
        amp=np.asarray([a for _,a in rows],dtype=np.complex128)
    else:
        spins=np.zeros((0,len(PW.EDGES)),dtype=np.int16)
        Ks=np.zeros((0,len(PW.VERT)),dtype=np.int16)
        amp=np.zeros((0,),dtype=np.complex128)
    np.savez_compressed(path,spins=spins,Ks=Ks,amp=amp)


def run(channel):
    if channel not in CHANNELS:
        raise ValueError(channel)
    ZVM.patch_and_clear()
    initial=PW.basis_full_jhalf()[0]
    need_L='L' in channel
    restore=None; caches={}
    try:
        if need_L:
            restore,caches=LP.install_sine_cached_stack()
        seqA,seqB=channel_sequences(channel)
        A,diagA=sequence(initial,*seqA,channel,need_L)
        B,diagB=sequence(initial,*seqB,channel,need_L)
        C={}; add(C,A,+1); add(C,B,-1)

        maxdiag={}; combine_diag(maxdiag,diagA['max_diagnostics']); combine_diag(maxdiag,diagB['max_diagnostics'])
        max_physical=max(
            float(maxdiag.get('CV_complete_basis_leakage',0.0)),
            float(maxdiag.get('CK_outer_complete_basis_leakage',0.0)),
            float(maxdiag.get('CK_internal_volume_sector_leakage',0.0)),
        )
        reject=max(diagA['nonscalar_rejected_norm'],diagB['nonscalar_rejected_norm'])
        # Relevant pair wall is the second action wall for both directions.
        second_wall=max(diagA['left_Jmax'],diagB['left_Jmax'])
        mspin=max(max_spin(C),diagA['final_max_spin'],diagB['final_max_spin'])
        cache_info={
            name:{'hits':fn.cache_info().hits,'misses':fn.cache_info().misses,'currsize':fn.cache_info().currsize}
            for name,fn in caches.items()
        } if need_L else {}

        checks={
            'both_directional_first_actions_nonzero':diagA['right_output_support']>0 and diagB['right_output_support']>0,
            'both_directional_compositions_completed':diagA['final_support']>=0 and diagB['final_support']>=0,
            'finite_norms':all(math.isfinite(x) for x in [diagA['final_norm'],diagB['final_norm'],math.sqrt(norm2(C))]),
            'physical_basis_volume_leakage':max_physical<1e-8,
            'nonscalar_closure_leakage':reject<1e-8,
            'measured_spin_within_frozen_wall':mspin<=second_wall+1e-12,
        }
        return C,{
            'status':f'preregistered raw {channel} channel of the full signed geometry commutator',
            'passed':all(checks.values()),
            'preregistration':'PETER_WEYL_FULL_GEOMETRY_COMMUTATOR_PREREGISTRATION.md',
            'channel':channel,
            'definition':{
                'EE':'E0E1-E1E0','EL':'E0L1-E1L0','LE':'L0E1-L1E0','LL':'L0L1-L1L0'
            }[channel],
            'input':'all ten links j=1/2; all five K=0',
            'frozen_walls_Jmax':{k:v/2 for k,v in WALLS[channel].items()},
            'direction_A':diagA,
            'direction_B':diagB,
            'commutator_support':len(C),
            'commutator_norm':math.sqrt(norm2(C)),
            'commutator_max_spin':max_spin(C),
            'max_physical_basis_volume_leakage':max_physical,
            'max_nonscalar_rejected_norm':reject,
            'cache_info':cache_info,
            'checks':checks,
            'channel_may_be_exactly_zero':True,
            'signed_physical_weight_applied_here':False,
        }
    finally:
        if restore is not None:
            restore()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--channel',choices=CHANNELS,required=True)
    p.add_argument('--json-output',type=Path,required=True)
    p.add_argument('--state-output',type=Path,required=True)
    a=p.parse_args(); state,out=run(a.channel)
    a.json_output.parent.mkdir(parents=True,exist_ok=True)
    a.json_output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    save_state_npz(a.state_output,state)
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if out['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
