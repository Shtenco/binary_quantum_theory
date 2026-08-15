#!/usr/bin/env python3
"""Generic operator-first route blocks on the Peter-Weyl Gauss basis.

For fixed edge spins and fixed intertwiners away from route nodes (0,1), the
route metric acts on the complete finite block

    K0 in allowed_K(node0)  x  K1 in allowed_K(node1).

This module constructs exact matrix-valued flux Gram operators Q^{ab} on that
block, forms the shared two-node metric

    Q_shared=1/2(Q0 tensor I + I tensor Q1),

and applies the positive operator-first route normal using the exact sparse
Fourier engine in operator_route_sparse_fourier.py.

It is designed for spin-changed states produced by H_E and H_L.  No geometry
expectation value is taken before the spectral square root.
"""
from __future__ import annotations

import functools
import math
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import k5_peter_weyl_safe_hda_column as PW
import operator_route_sparse_fourier as SF

ROUTE_NODES=(0,1)
LOCAL_ROUTE_LEGS=(1,2)
TOL=1e-14


def normalize(v):
    n=math.sqrt(float(np.vdot(v,v).real))
    if n<1e-15:
        raise RuntimeError('zero-norm intertwiner')
    return v/n


def apply_dot(T,leg_a,leg_b,ls):
    out=np.zeros_like(T,dtype=complex)
    ma=PW.spin_mats_cached(ls[leg_a]); mb=PW.spin_mats_cached(ls[leg_b])
    for c in range(3):
        tmp=PW.apply_axis_np(T,leg_b,mb[c])
        tmp=PW.apply_axis_np(tmp,leg_a,ma[c])
        out+=tmp
    return out


@functools.lru_cache(maxsize=None)
def local_flux_gram(spins,vertex):
    spins=tuple(spins)
    ls=PW.local_spins(spins,vertex)
    allowed=tuple(PW.allowed_k2_t(*ls))
    basis=tuple(normalize(PW.oriented_intertwiner(vertex,ls,K)) for K in allowed)
    Q=[[np.zeros((len(allowed),len(allowed)),complex) for _ in range(2)] for _ in range(2)]
    legs=LOCAL_ROUTE_LEGS
    for a,la in enumerate(legs):
        for b,lb in enumerate(legs):
            for j,ket in enumerate(basis):
                acted=apply_dot(ket,la,lb,ls)
                for i,bra in enumerate(basis):
                    Q[a][b][i,j]=np.vdot(bra,acted)
            Q[a][b]=0.5*(Q[a][b]+Q[a][b].conj().T)
    return allowed,tuple(tuple(Q[a][b] for b in range(2)) for a in range(2))


def sector_id(key):
    spins,Ks=key
    rest=tuple(Ks[v] for v in PW.VERT if v not in ROUTE_NODES)
    return tuple(spins),rest


@functools.lru_cache(maxsize=None)
def sector_basis(sector):
    spins,rest=sector
    a0,_=local_flux_gram(spins,0)
    a1,_=local_flux_gram(spins,1)
    rest_vertices=tuple(v for v in PW.VERT if v not in ROUTE_NODES)
    keys=[]
    for K0 in a0:
        for K1 in a1:
            Ks=[None]*len(PW.VERT)
            Ks[0]=K0; Ks[1]=K1
            for v,k in zip(rest_vertices,rest):
                Ks[v]=k
            key=(tuple(spins),tuple(Ks))
            # Other fixed intertwiners must be admissible for this spin sector.
            ok=all(Ks[v] in PW.allowed_k2_t(*PW.local_spins(spins,v)) for v in PW.VERT)
            if not ok:
                raise RuntimeError(f'inadmissible sector basis key {key}')
            keys.append(key)
    return tuple(keys)


@functools.lru_cache(maxsize=None)
def shared_Q(sector):
    spins,_=sector
    a0,q0=local_flux_gram(spins,0)
    a1,q1=local_flux_gram(spins,1)
    I0=np.eye(len(a0),dtype=complex); I1=np.eye(len(a1),dtype=complex)
    Q=[[None,None],[None,None]]
    for a in range(2):
        for b in range(2):
            A=0.5*(np.kron(q0[a][b],I1)+np.kron(I0,q1[a][b]))
            Q[a][b]=0.5*(A+A.conj().T)
    return tuple(tuple(Q[a][b] for b in range(2)) for a in range(2))


def sector_index(sector):
    return {k:i for i,k in enumerate(sector_basis(sector))}


def pack_global(state):
    """Global {gauss_key:{mode:amp}} -> {sector:{mode:vector}}."""
    grouped={}
    for key,modes in state.items():
        sec=sector_id(key)
        if sec not in grouped:
            grouped[sec]={}
        basis=sector_basis(sec)
        idx={k:i for i,k in enumerate(basis)}
        if key not in idx:
            raise RuntimeError(f'key missing from its completed route sector: {key}')
        i=idx[key]
        for mode,amp in modes.items():
            vec=grouped[sec].get(mode,np.zeros(len(basis),complex))
            vec=vec.copy(); vec[i]+=amp
            if np.linalg.norm(vec)>TOL:
                grouped[sec][mode]=vec
            elif mode in grouped[sec]:
                del grouped[sec][mode]
    return grouped


def unpack_global(grouped,tol=TOL):
    out={}
    for sec,modes in grouped.items():
        basis=sector_basis(sec)
        for mode,vec in modes.items():
            for i,amp in enumerate(vec):
                if abs(amp)<=tol:
                    continue
                key=basis[i]
                out.setdefault(key,{})[mode]=out.setdefault(key,{}).get(mode,0j)+amp
    return out


def route_apply_global(lapse,state,epsilon,tol=TOL):
    grouped=pack_global(state)
    gout={}
    for sec,psi in grouped.items():
        gout[sec]=SF.route_apply(shared_Q(sec),lapse,psi,epsilon,tol)
    return unpack_global(gout,tol)


def route_target_global(N,M,state,epsilon,tol=TOL):
    grouped=pack_global(state)
    gout={}
    for sec,psi in grouped.items():
        gout[sec]=SF.route_target(shared_Q(sec),N,M,psi,epsilon,tol)
    return unpack_global(gout,tol)


def add_global(dst,src,scale=1.0,tol=TOL):
    for key,modes in src.items():
        for mode,amp in modes.items():
            d=dst.setdefault(key,{})
            z=d.get(mode,0j)+scale*amp
            if abs(z)>tol:
                d[mode]=z
            elif mode in d:
                del d[mode]
        if not dst.get(key):
            dst.pop(key,None)
    return dst


def route_commutator_global(N,M,state,epsilon,tol=TOL):
    RM=route_apply_global(M,state,epsilon,tol)
    RN=route_apply_global(N,state,epsilon,tol)
    NRM=route_apply_global(N,RM,epsilon,tol)
    MRN=route_apply_global(M,RN,epsilon,tol)
    out={}
    add_global(out,NRM,+1,tol); add_global(out,MRN,-1,tol)
    return out


def global_norm2(state):
    return float(sum(abs(a)**2 for modes in state.values() for a in modes.values()))


def relative_defect(a,b,sign=+1,tol=TOL):
    x={k:dict(v) for k,v in a.items()}
    add_global(x,b,sign,tol)
    return math.sqrt(global_norm2(x))/max(math.sqrt(global_norm2(b)),1e-30)


def carrier_global_state(key,carrier):
    return {key:{(int(carrier),int(carrier-1)):1+0j}}


def sector_min_symbol_eigenvalue(sector,modes):
    Q=shared_Q(sector)
    m=math.inf
    for k in modes:
        A=(k[0]*k[0]*Q[0][0]
           +k[0]*k[1]*(Q[0][1]+Q[1][0])
           +k[1]*k[1]*Q[1][1])
        m=min(m,float(np.linalg.eigvalsh(0.5*(A+A.conj().T)).min()))
    return m
