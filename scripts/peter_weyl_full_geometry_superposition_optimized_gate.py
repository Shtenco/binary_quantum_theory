#!/usr/bin/env python3
"""Exact whole-state optimized full signed two-node geometry commutator.

This is a computationally factorized evaluation of the already preregistered
operator

    G_v = a E_v + b L_v,
    a = -2/3,
    b = +32 i / 9,

in structural beta=hbar=1 units, on the frozen all-j=1/2, all-K=0 seed.

Raw channel definitions and frozen walls are unchanged:

    EE = E0 E1 - E1 E0,                  Jmax=5/2 -> 5/2
    EL = E0 L1 - E1 L0,                  Jmax=7/2 -> 9/2
    LE = L0 E1 - L1 E0,                  Jmax=5/2 -> 9/2
    LL = L0 L1 - L1 L0,                  Jmax=7/2 -> 13/2

The only optimization is exact linearity.  Instead of applying a complete
24-term L column separately to every intermediate Gauss basis key, each
24-term epsilon sum is applied directly to the complete sparse Gauss
superposition.  C(V) and C(K_sine) are linear sparse-state operators, and a
reduced executable linearity gate is run before the production calculation.

No sign fitting, coefficient fitting, channel subtraction, channel deletion or
post-result threshold change is performed.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import time
from pathlib import Path

import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_euclidean_sine_ordering_gate as SINE
import peter_weyl_lorentzian_logical_projection_gate as LP
import peter_weyl_lorentzian_superposition_gate as SUP
import peter_weyl_zeroaware_volume_migration_experiment as ZVM

TOL=1e-10
A=-2.0/3.0
B=32.0j/9.0
WEIGHTS={
    'EE':A*A,
    'EL':A*B,
    'LE':A*B,
    'LL':B*B,
}


def add(dst,src,scale=1.0,tol=TOL):
    for k,a in src.items():
        z=dst.get(k,0j)+scale*a
        if abs(z)>tol:
            dst[k]=z
        elif k in dst:
            del dst[k]


def diff(a,b):
    out={}; add(out,a,+1); add(out,b,-1); return out


def norm2(s):
    return float(sum(abs(a)**2 for a in s.values()))


def norm(s):
    return math.sqrt(norm2(s))


def max_spin(s):
    return max((max(k[0]) for k in s),default=0)/2.0


def finite_state(s):
    return all(np.isfinite([z.real,z.imag]).all() for z in s.values())


def E(state,node,jmax2):
    return PW.prune_state(SINE.safe_H_sine(state,node,jmax2),TOL)


def L(state,node,jmax2,label):
    print(f'[L] start {label}: source={node} Jmax={jmax2/2} input_support={len(state)} input_norm={norm(state):.16g}',flush=True)
    t0=time.time()
    restore,caches=LP.install_sine_cached_stack()
    try:
        out,rows,diag,accepted2,rejected2=SUP.epsilon_sum_gauss_from_gauss(
            state,node,jmax2
        )
        cache_info={
            name:{'hits':fn.cache_info().hits,'misses':fn.cache_info().misses,'currsize':fn.cache_info().currsize}
            for name,fn in caches.items()
        }
    finally:
        restore()
    physical=max(
        float(diag.get('CV_complete_basis_leakage',0.0)),
        float(diag.get('CK_outer_complete_basis_leakage',0.0)),
        float(diag.get('CK_internal_volume_sector_leakage',0.0)),
    )
    rejected=math.sqrt(max(rejected2,0.0))
    meta={
        'label':label,'source_node':node,'Jmax':jmax2/2,
        'input_support':len(state),'input_norm':norm(state),
        'output_support':len(out),'output_norm':norm(out),'output_max_spin':max_spin(out),
        'ordered_terms':rows,
        'max_physical_basis_volume_leakage':physical,
        'scalar_accepted_norm_accumulated':math.sqrt(max(accepted2,0.0)),
        'nonscalar_rejected_norm_accumulated':rejected,
        'cache_info':cache_info,
        'elapsed_seconds':time.time()-t0,
        'checks':{
            'finite_output':finite_state(out) and math.isfinite(norm(out)),
            'physical_basis_volume_leakage':physical<1e-8,
            'nonscalar_rejected_norm':rejected<1e-8,
            'spin_within_frozen_wall':max_spin(out)<=jmax2/2+1e-12,
        },
    }
    meta['passed']=all(meta['checks'].values())
    print(f'[L] done {label}: support={len(out)} norm={norm(out):.16g} max_spin={max_spin(out)} elapsed={meta["elapsed_seconds"]:.3f}s pass={meta["passed"]}',flush=True)
    return out,meta


def channel_meta(name,state,Aseq,Bseq,wall,extra=None):
    m={
        'channel':name,'support':len(state),'norm':norm(state),'max_spin':max_spin(state),
        'direction_A':Aseq,'direction_B':Bseq,
        'frozen_pair_wall_Jmax':wall,
        'finite_amplitudes':finite_state(state),
        'signed_weight':[float(WEIGHTS[name].real),float(WEIGHTS[name].imag)],
    }
    if extra: m.update(extra)
    m['passed']=bool(m['finite_amplitudes'] and m['max_spin']<=wall+1e-12)
    return m


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


def relerr(a,b):
    keys=set(a)|set(b)
    num=math.sqrt(sum(abs(a.get(k,0j)-b.get(k,0j))**2 for k in keys))
    return num/max(norm(b),1e-30)


def run():
    t_all=time.time()
    ZVM.patch_and_clear()

    # Executable prerequisite: whole-state ordered-triple linearity.
    print('[preflight] exact Lorentzian superposition linearity',flush=True)
    linearity=SUP.run_linearity_gate(jmax2=5)
    if not linearity.get('passed',False):
        raise RuntimeError('superposition linearity gate failed')

    initial=PW.basis_full_jhalf()[0]
    seed={initial:1+0j}

    # First actions reused by all channels.
    print('[first] Euclidean node images',flush=True)
    E0=E(seed,0,5)
    E1=E(seed,1,5)
    L0,L0meta=L(seed,0,7,'L0_seed')
    L1,L1meta=L(seed,1,7,'L1_seed')

    # EE = E0 E1 - E1 E0.
    print('[channel] EE',flush=True)
    EE_A=E(E1,0,5)
    EE_B=E(E0,1,5)
    EE=diff(EE_A,EE_B)
    EE_meta=channel_meta('EE',EE,
        {'sequence':'E0(E1(seed))','support':len(EE_A),'norm':norm(EE_A),'max_spin':max_spin(EE_A)},
        {'sequence':'E1(E0(seed))','support':len(EE_B),'norm':norm(EE_B),'max_spin':max_spin(EE_B)},
        2.5,
        {'reference_expected_norm':2.879453814704955,'reference_norm_abs_error':abs(norm(EE)-2.879453814704955),
         'reference_expected_support':514,'reference_support_match':len(EE)==514})
    EE_meta['passed']=EE_meta['passed'] and EE_meta['reference_norm_abs_error']<1e-11 and EE_meta['reference_support_match']

    # EL = E0 L1 - E1 L0.  Cheap once first L columns are available.
    print('[channel] EL',flush=True)
    EL_A=E(L1,0,9)
    EL_B=E(L0,1,9)
    EL=diff(EL_A,EL_B)
    EL_meta=channel_meta('EL',EL,
        {'sequence':'E0(L1(seed))','support':len(EL_A),'norm':norm(EL_A),'max_spin':max_spin(EL_A)},
        {'sequence':'E1(L0(seed))','support':len(EL_B),'norm':norm(EL_B),'max_spin':max_spin(EL_B)},
        4.5)

    # LE = L0 E1 - L1 E0: each second L acts once on the complete E superposition.
    print('[channel] LE',flush=True)
    LE_A,LE_A_meta=L(E1,0,9,'L0_on_E1')
    LE_B,LE_B_meta=L(E0,1,9,'L1_on_E0')
    LE=diff(LE_A,LE_B)
    LE_meta=channel_meta('LE',LE,LE_A_meta,LE_B_meta,4.5,
        {'max_physical_basis_volume_leakage':max(LE_A_meta['max_physical_basis_volume_leakage'],LE_B_meta['max_physical_basis_volume_leakage']),
         'max_nonscalar_rejected_norm':max(LE_A_meta['nonscalar_rejected_norm_accumulated'],LE_B_meta['nonscalar_rejected_norm_accumulated'])})
    LE_meta['passed']=LE_meta['passed'] and LE_A_meta['passed'] and LE_B_meta['passed']

    # LL = L0 L1 - L1 L0: each second L acts once on the complete first-L superposition.
    print('[channel] LL',flush=True)
    LL_A,LL_A_meta=L(L1,0,13,'L0_on_L1')
    LL_B,LL_B_meta=L(L0,1,13,'L1_on_L0')
    LL=diff(LL_A,LL_B)
    LL_meta=channel_meta('LL',LL,LL_A_meta,LL_B_meta,6.5,
        {'max_physical_basis_volume_leakage':max(LL_A_meta['max_physical_basis_volume_leakage'],LL_B_meta['max_physical_basis_volume_leakage']),
         'max_nonscalar_rejected_norm':max(LL_A_meta['nonscalar_rejected_norm_accumulated'],LL_B_meta['nonscalar_rejected_norm_accumulated'])})
    LL_meta['passed']=LL_meta['passed'] and LL_A_meta['passed'] and LL_B_meta['passed']

    # Frozen signed assembly [G0,G1].
    signed={}
    for name,state in [('EE',EE),('EL',EL),('LE',LE),('LL',LL)]:
        add(signed,state,WEIGHTS[name])

    signed_meta={
        'support':len(signed),'norm':norm(signed),'max_spin':max_spin(signed),
        'finite_amplitudes':finite_state(signed),
        'weights':{k:[float(v.real),float(v.imag)] for k,v in WEIGHTS.items()},
        'formula':'(4/9) EE + (-64 i/27)(EL+LE) + (-1024/81) LL',
    }

    channels={'EE':EE_meta,'EL':EL_meta,'LE':LE_meta,'LL':LL_meta}
    checks={
        'linearity_preflight':bool(linearity.get('passed',False)),
        'first_L0_passed':bool(L0meta['passed']),
        'first_L1_passed':bool(L1meta['passed']),
        'EE_passed':bool(EE_meta['passed']),
        'EL_passed':bool(EL_meta['passed']),
        'LE_passed':bool(LE_meta['passed']),
        'LL_passed':bool(LL_meta['passed']),
        'signed_state_finite':signed_meta['finite_amplitudes'] and math.isfinite(signed_meta['norm']),
        'no_posthoc_fit':True,
    }

    out={
        'status':'exact whole-state optimized preregistered full signed geometry commutator',
        'passed':all(checks.values()),
        'input':'all ten links j=1/2; all five K=0',
        'physical_structural_units':{'beta':1.0,'hbar':1.0,'a_E':A,'b_L_raw':[B.real,B.imag]},
        'frozen_channel_weights':{k:[float(v.real),float(v.imag)] for k,v in WEIGHTS.items()},
        'linearity_preflight':linearity,
        'first_actions':{
            'E0':{'support':len(E0),'norm':norm(E0),'max_spin':max_spin(E0)},
            'E1':{'support':len(E1),'norm':norm(E1),'max_spin':max_spin(E1)},
            'L0':L0meta,'L1':L1meta,
        },
        'channels':channels,
        'signed_commutator':signed_meta,
        'checks':checks,
        'elapsed_seconds':time.time()-t_all,
        'optimization_statement':'Only exact linear regrouping of sparse-state actions; operator algebra, orientation coefficients, cutoffs and signed physical weights are unchanged.',
    }
    states={'EE':EE,'EL':EL,'LE':LE,'LL':LL,'SIGNED':signed,'L0':L0,'L1':L1}
    return states,out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output-dir',type=Path,default=Path('verification_results/full_geometry_optimized'))
    a=p.parse_args(); states,out=run(); d=a.output_dir; d.mkdir(parents=True,exist_ok=True)
    for name,state in states.items():
        save_state(d/f'{name}.npz',state)
    (d/'RESULT.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if out['passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
