#!/usr/bin/env python3
"""Safe-cutoff diagonal-environment blocks for one ordered Lorentzian triple.

For source node 0, each of the other four logical K5 nodes is allowed to be in
K=0 or K=2.  For a requested batch of environment bitstrings e=0..15, compute

  M_abc(e)_{f q}
    = <K_f,e| Tr_aux[C_a(K) C_b(K) C_c(V)] |K_q,e>

with source K_q,K_f in {0,2}.  The environment is diagonal because the target
observable is the true one-body partial trace, not a frozen-boundary matrix.

The contraction is the same exact safe Jmax=7/2 meet-in-the-middle contraction
used by peter_weyl_lorentzian_ordered_mitm_param_gate.py.  Expensive sine-stack
caches are kept alive across all environments in the batch.

This file computes structural raw amplitudes only.  It does not insert the final
canonical kappa/beta/hbar/i prefactor and does not claim a Hermitian physical H_L.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import numpy as np

import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_lorentzian_logical_projection_gate as LP

PAULI={
    'I':np.eye(2,dtype=complex),
    'X':np.array([[0,1],[1,0]],complex),
    'Y':np.array([[0,-1j],[1j,0]],complex),
    'Z':np.array([[1,0],[0,-1]],complex),
}


def inner(a,b):
    if len(a)>len(b):
        return np.conj(inner(b,a))
    return sum(np.conj(v)*b.get(k,0j) for k,v in a.items())


def cp(z):
    z=complex(z)
    return [float(z.real),float(z.imag)]


def env_Ks(env_index:int, source:int=0):
    Ks=[0]*len(PW.VERT)
    bit=0
    for v in PW.VERT:
        if v==source:
            continue
        Ks[v]=2 if ((env_index>>bit)&1) else 0
        bit+=1
    return Ks


def logical_covariant(env_index:int, source_K:int, source:int=0):
    spins=(1,)*len(PW.EDGES)
    Ks=env_Ks(env_index,source)
    Ks[source]=source_K
    key=(spins,tuple(Ks))
    return LP.CV.gauss_to_covariant({key:1+0j},source)


def matrix_for_env(a,b,c,env_index,source,jmax2):
    logical=[logical_covariant(env_index,K,source) for K in (0,2)]
    back={}
    max_outer=max_vol=max_charge=max_cv=0.0

    # Backward first C(K), using C(K)_ij^dagger=-C(K)_ji.
    for f in range(2):
        for j,i in itertools.product(range(2),repeat=2):
            s,d=LP.RAW.KCOMP.C_K_component(logical[f],source,a,j,i,jmax2)
            back[(f,j,i)]=s
            max_outer=max(max_outer,float(d['outer_complete_basis_leakage']))
            max_vol=max(max_vol,float(d['internal_volume_sector_leakage']))
            max_charge=max(max_charge,float(d['complete_charge_basis_leakage']))

    M=np.zeros((2,2),complex)
    for q in range(2):
        for i,j,k in itertools.product(range(2),repeat=3):
            s1,lv=LP.RAW.COMP.C_volume_component(logical[q],source,c,k,i,jmax2)
            max_cv=max(max_cv,float(lv))
            if s1:
                s2,d=LP.RAW.KCOMP.C_K_component(s1,source,b,j,k,jmax2)
                max_outer=max(max_outer,float(d['outer_complete_basis_leakage']))
                max_vol=max(max_vol,float(d['internal_volume_sector_leakage']))
                max_charge=max(max_charge,float(d['complete_charge_basis_leakage']))
                # Same scalar-source closure filter as the validated ordered MITM gate.
                s2={key:amp for key,amp in s2.items() if key[2] in (0,2)}
            else:
                s2={}
            if s2:
                for f in range(2):
                    M[f,q] -= inner(back[(f,j,i)],s2)

    physical=max(max_cv,max_outer,max_vol)
    coeff={name:cp(np.trace(P@M)/2.0) for name,P in PAULI.items()}
    return M,physical,max_charge,coeff


def run(a,b,c,env_start,env_stop,coefficient=1,source=0,jmax2=7):
    neigh=PW.NEIG[source]
    if len({a,b,c})!=3 or any(x not in neigh for x in (a,b,c)):
        raise ValueError(f'(a,b,c) must be distinct neighbors of source {source}: {neigh}')
    if not (0<=env_start<env_stop<=16):
        raise ValueError('require 0 <= env_start < env_stop <= 16')

    LP.JMAX2=jmax2
    restore,_=LP.install_sine_cached_stack()
    rows=[]
    total=np.zeros((2,2),complex)
    max_physical=max_charge=0.0
    try:
        for e in range(env_start,env_stop):
            M,physical,charge,coeff=matrix_for_env(a,b,c,e,source,jmax2)
            total+=M
            max_physical=max(max_physical,physical)
            max_charge=max(max_charge,charge)
            rows.append({
                'environment_index':e,
                'environment_Ks':env_Ks(e,source),
                'logical_2x2_matrix':[[cp(M[r,s]) for s in range(2)] for r in range(2)],
                'frobenius_norm':float(np.linalg.norm(M)),
                'pauli_coefficients':coeff,
                'physical_acceptance_max_leakage':physical,
                'historical_charge_diagnostic':charge,
            })
    finally:
        restore()

    summed_coeff={name:cp(np.trace(P@total)/2.0) for name,P in PAULI.items()}
    passed=bool(max_physical<1e-8 and np.all(np.isfinite(total)) and len(rows)==env_stop-env_start)
    return {
        'status':'safe Lorentzian diagonal-environment trace block',
        'passed':passed,
        'source_node':source,
        'ordered_edges':[a,b,c],
        'epsilon_coefficient':int(coefficient),
        'Jmax':jmax2/2,
        'environment_start':env_start,
        'environment_stop':env_stop,
        'environment_count':len(rows),
        'environment_indices':[r['environment_index'] for r in rows],
        'environment_sum_matrix':[[cp(total[r,s]) for s in range(2)] for r in range(2)],
        'environment_sum_pauli':summed_coeff,
        'max_physical_basis_volume_leakage':max_physical,
        'historical_charge_diagnostic_max':max_charge,
        'historical_charge_is_hard_acceptance':False,
        'environments':rows,
        'scope':'Diagonal logical-environment contribution to one ordered raw Lorentzian triple only; not yet averaged over all 16 environments or epsilon-assembled.',
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--a',type=int,required=True)
    p.add_argument('--b',type=int,required=True)
    p.add_argument('--c',type=int,required=True)
    p.add_argument('--coefficient',type=int,required=True)
    p.add_argument('--env-start',type=int,required=True)
    p.add_argument('--env-stop',type=int,required=True)
    p.add_argument('--output',type=Path)
    x=p.parse_args()
    o=run(x.a,x.b,x.c,x.env_start,x.env_stop,x.coefficient)
    t=json.dumps(o,indent=2)
    print(t)
    if x.output:
        x.output.parent.mkdir(parents=True,exist_ok=True)
        x.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
