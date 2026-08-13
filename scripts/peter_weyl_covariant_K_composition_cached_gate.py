#!/usr/bin/env python3
"""Runtime-equivalent cached wrapper for the generalized C_e(K) gate.

The physics implementation remains in peter_weyl_covariant_K_composition_gate.
This wrapper changes only repeated evaluation of deterministic sparse-state
functions. Cache keys contain the complete discrete labels and exact complex
amplitudes; no rounding, pruning, fitting or representation reduction occurs.

Additional exact acceleration
-----------------------------
H_E is an SU(2) scalar.  In an explicit |J,M,K12,K34> charged basis its reduced
matrix element is independent of M and H_E preserves J,M at every charged
endpoint.  Therefore all magnetic copies of the SAME charged reduced state are
computed once at highest weight M=J and the output labels are relabelled back
to the original M values.  This is the rank-0 Wigner--Eckart identity, not a
physical approximation.  Any output that violates the required J,M preservation
raises immediately instead of being silently projected.
"""
from __future__ import annotations

import argparse
import functools
import json
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import peter_weyl_covariant_K_composition_gate as CKCOMP


def freeze_state(state):
    return tuple(sorted(state.items(),key=lambda kv:repr(kv[0])))


def canonicalize_scalar_charge_M(key,charged_nodes):
    spins,labels=key
    labs=list(labels)
    original={}
    for v in charged_nodes:
        lab=labs[v]
        if lab[0] != 'C':
            raise ValueError(f'charged node {v} lacks explicit C label')
        _,J2,M2,K12,K34=lab
        original[v]=(int(J2),int(M2))
        labs[v]=CKCOMP.CK.label_charge(J2,J2,K12,K34)
    return (spins,tuple(labs)),original


def restore_scalar_charge_M(state,charged_nodes,original):
    out={}
    for key,amp in state.items():
        spins,labels=key
        labs=list(labels)
        for v in charged_nodes:
            lab=labs[v]
            if lab[0] != 'C':
                raise RuntimeError('scalar H_E lost charged endpoint label')
            _,J2,M2,K12,K34=lab
            Jin,Min=original[v]
            if int(J2) != Jin or int(M2) != Jin:
                raise RuntimeError(
                    f'scalar H_E violated canonical J,M preservation at node {v}: '
                    f'input J2={Jin}, canonical M2={Jin}, output={(J2,M2)}'
                )
            labs[v]=CKCOMP.CK.label_charge(J2,Min,K12,K34)
        ko=(spins,tuple(labs))
        out[ko]=out.get(ko,0j)+amp
    return out


def run(v=0,w=1):
    original_he=CKCOMP.CK.apply_HE_complete_key
    original_k=CKCOMP.apply_K_complete_custom
    original_inv=CKCOMP.COMP.inverse_complete
    original_direct=CKCOMP.direct_K_covariant
    original_close=CKCOMP.COMP.close_complete

    @functools.lru_cache(maxsize=None)
    def cached_he_reduced(canonical_key,source_v,Jmax2,charged_nodes):
        return original_he(
            canonical_key,source_v,Jmax2,charged_nodes=tuple(charged_nodes)
        )

    he_calls={'magnetic_requests':0,'reduced_requests':0}

    def reduced_he(key,source_v,Jmax2,charged_nodes=(0,1)):
        charged_nodes=tuple(charged_nodes)
        he_calls['magnetic_requests'] += 1
        canonical,original=canonicalize_scalar_charge_M(key,charged_nodes)
        before=cached_he_reduced.cache_info().misses
        state,vleak,bleak=cached_he_reduced(
            canonical,source_v,Jmax2,charged_nodes
        )
        after=cached_he_reduced.cache_info().misses
        he_calls['reduced_requests'] += int(after>before)
        return restore_scalar_charge_M(state,charged_nodes,original),vleak,bleak

    @functools.lru_cache(maxsize=None)
    def cached_k_frozen(frozen,source_v,Jmax2,charged_nodes):
        out,vleak,bleak=original_k(dict(frozen),source_v,Jmax2,tuple(charged_nodes))
        return tuple(out.items()),float(vleak),float(bleak)

    def cached_k(state,source_v,Jmax2,charged_nodes):
        items,vleak,bleak=cached_k_frozen(
            freeze_state(state),source_v,Jmax2,tuple(charged_nodes)
        )
        return dict(items),vleak,bleak

    @functools.lru_cache(maxsize=None)
    def cached_inv_frozen(frozen,source_v,target_v,k,j,Jmax2):
        out,leak=original_inv(dict(frozen),source_v,target_v,k,j,Jmax2)
        return tuple(out.items()),float(leak)

    def cached_inv(state,source_v,target_v,k,j,Jmax2):
        items,leak=cached_inv_frozen(
            freeze_state(state),source_v,target_v,k,j,Jmax2
        )
        return dict(items),leak

    @functools.lru_cache(maxsize=None)
    def cached_direct_frozen(frozen,source_v,Jmax2):
        out,vleak,bleak=original_direct(dict(frozen),source_v,Jmax2)
        return tuple(out.items()),float(vleak),float(bleak)

    def cached_direct(state,source_v,Jmax2):
        items,vleak,bleak=cached_direct_frozen(
            freeze_state(state),source_v,Jmax2
        )
        return dict(items),vleak,bleak

    @functools.lru_cache(maxsize=None)
    def cached_close_frozen(frozen,source_v,target_v,i,k,Jmax2):
        out=original_close(dict(frozen),source_v,target_v,i,k,Jmax2)
        return tuple(out.items())

    def cached_close(state,source_v,target_v,i,k,Jmax2):
        return dict(cached_close_frozen(
            freeze_state(state),source_v,target_v,i,k,Jmax2
        ))

    CKCOMP.CK.apply_HE_complete_key=reduced_he
    CKCOMP.apply_K_complete_custom=cached_k
    CKCOMP.COMP.inverse_complete=cached_inv
    CKCOMP.direct_K_covariant=cached_direct
    CKCOMP.COMP.close_complete=cached_close
    try:
        out=CKCOMP.run(v,w)
        hi=cached_he_reduced.cache_info(); ki=cached_k_frozen.cache_info()
        ii=cached_inv_frozen.cache_info(); di=cached_direct_frozen.cache_info()
        ci=cached_close_frozen.cache_info()
    finally:
        CKCOMP.CK.apply_HE_complete_key=original_he
        CKCOMP.apply_K_complete_custom=original_k
        CKCOMP.COMP.inverse_complete=original_inv
        CKCOMP.direct_K_covariant=original_direct
        CKCOMP.COMP.close_complete=original_close

    out['runtime_memoization']={
        'scalar_HE_reduced_highest_weight_cache':{
            'hits':hi.hits,'misses':hi.misses,'currsize':hi.currsize,
            'magnetic_requests':he_calls['magnetic_requests'],
            'distinct_reduced_requests':he_calls['reduced_requests'],
            'rule':'rank-0 Wigner-Eckart: fixed charged J,K labels are M-independent and preserve J,M',
        },
        'apply_K_complete_state':{'hits':ki.hits,'misses':ki.misses,'currsize':ki.currsize},
        'inverse_complete_state':{'hits':ii.hits,'misses':ii.misses,'currsize':ii.currsize},
        'direct_K_covariant_state':{'hits':di.hits,'misses':di.misses,'currsize':di.currsize},
        'close_complete_state':{'hits':ci.hits,'misses':ci.misses,'currsize':ci.currsize},
        'cache_keys_use_full_exact_sparse_states':True,
        'magnetic_reduction_is_exact_SU2_scalar_identity':True,
        'physics_changed':False,
    }
    return out


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--v',type=int,default=0)
    ap.add_argument('--w',type=int,default=1)
    ap.add_argument('--output',type=Path)
    a=ap.parse_args(); out=run(a.v,a.w); text=json.dumps(out,indent=2); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out.get('passed',False) else 1

if __name__=='__main__':
    raise SystemExit(main())
