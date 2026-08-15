#!/usr/bin/env python3
"""Exact sparse-Fourier engine for the operator-first route-normal constraint.

For the frozen HDA probes, N and M contain only constant and first harmonic
sin/cos modes and the WKB state starts on one Fourier carrier.  FFT grids are
therefore unnecessary: multiplication is finite convolution in Fourier space.

This module works for an arbitrary finite geometry block Q^{ab} (matrix-valued):

    Omega(k) = sqrt_operator(Q^{ab} k_a k_b) / epsilon,
    R[N]     = 1/2 {N,Omega}.

It also constructs the matrix-valued half-density diffeomorphism target exactly
in the same sparse Fourier representation.

Fourier convention:

    f(x)=sum_k f_k exp(i k.x),
    d_a f_k = i k_a f_k / epsilon.
"""
from __future__ import annotations

import math
from collections import defaultdict

import numpy as np

Mode=tuple[int,int]


def sqrt_psd(A,tol=1e-9):
    H=0.5*(A+A.conj().T)
    vals,U=np.linalg.eigh(H)
    if vals.min() < -tol:
        raise RuntimeError(f'route symbol not positive semidefinite: {vals}')
    vals=np.maximum(vals,0.0)
    return (U*np.sqrt(vals))@U.conj().T


def add_mode_dict(dst,src,scale=1.0,tol=1e-14):
    for k,v in src.items():
        z=dst.get(k,0)+scale*v
        if np.linalg.norm(z)>tol:
            dst[k]=z
        elif k in dst:
            del dst[k]
    return dst


def scalar_convolve(a,b,tol=1e-15):
    out=defaultdict(complex)
    for ka,va in a.items():
        for kb,vb in b.items():
            k=(ka[0]+kb[0],ka[1]+kb[1])
            out[k]+=va*vb
    return {k:v for k,v in out.items() if abs(v)>tol}


def scalar_derivative(a,axis,epsilon,tol=1e-15):
    out={}
    for k,v in a.items():
        z=(1j*k[axis]/epsilon)*v
        if abs(z)>tol:
            out[k]=z
    return out


def scalar_times_vector(a,psi,tol=1e-14):
    out={}
    for ka,va in a.items():
        for kb,vb in psi.items():
            k=(ka[0]+kb[0],ka[1]+kb[1])
            z=out.get(k,np.zeros_like(vb))+va*vb
            if np.linalg.norm(z)>tol:
                out[k]=z
            elif k in out:
                del out[k]
    return out


def matrix_times_vector(A_modes,psi,tol=1e-14):
    out={}
    for ka,A in A_modes.items():
        for kb,v in psi.items():
            k=(ka[0]+kb[0],ka[1]+kb[1])
            z=out.get(k,np.zeros(A.shape[0],complex))+A@v
            if np.linalg.norm(z)>tol:
                out[k]=z
            elif k in out:
                del out[k]
    return out


def vector_derivative(psi,axis,epsilon,tol=1e-14):
    out={}
    for k,v in psi.items():
        z=(1j*k[axis]/epsilon)*v
        if np.linalg.norm(z)>tol:
            out[k]=z
    return out


def matrix_derivative(A_modes,axis,epsilon,tol=1e-14):
    out={}
    for k,A in A_modes.items():
        z=(1j*k[axis]/epsilon)*A
        if np.linalg.norm(z)>tol:
            out[k]=z
    return out


def omega_matrix(Q,mode,epsilon):
    k0,k1=mode
    A=(k0*k0*Q[0][0]
       +k0*k1*(Q[0][1]+Q[1][0])
       +k1*k1*Q[1][1])
    return sqrt_psd(A)/epsilon


def omega_apply(Q,psi,epsilon,tol=1e-14,cache=None):
    out={}
    if cache is None:
        cache={}
    for k,v in psi.items():
        if k not in cache:
            cache[k]=omega_matrix(Q,k,epsilon)
        z=cache[k]@v
        if np.linalg.norm(z)>tol:
            out[k]=z
    return out


def route_apply(Q,lapse,psi,epsilon,tol=1e-14,cache=None):
    if cache is None:
        cache={}
    Om=omega_apply(Q,psi,epsilon,tol,cache)
    left=scalar_times_vector(lapse,Om,tol)
    Npsi=scalar_times_vector(lapse,psi,tol)
    right=omega_apply(Q,Npsi,epsilon,tol,cache)
    out={}
    add_mode_dict(out,left,0.5,tol)
    add_mode_dict(out,right,0.5,tol)
    return out


def oneform_modes(N,M,epsilon):
    out=[]
    for b in range(2):
        NdM=scalar_convolve(N,scalar_derivative(M,b,epsilon))
        MdN=scalar_convolve(M,scalar_derivative(N,b,epsilon))
        x=dict(NdM)
        for k,v in MdN.items():
            x[k]=x.get(k,0j)-v
            if abs(x[k])<1e-15:
                del x[k]
        out.append(x)
    return out


def beta_matrix_modes(Q,N,M,epsilon,tol=1e-14):
    one=oneform_modes(N,M,epsilon)
    beta=[{},{}]
    d=Q[0][0].shape[0]
    for a in range(2):
        modes=set(one[0])|set(one[1])
        for k in modes:
            A=np.zeros((d,d),complex)
            for b in range(2):
                A+=Q[a][b]*one[b].get(k,0j)
            if np.linalg.norm(A)>tol:
                beta[a][k]=A
    return beta


def route_target(Q,N,M,psi,epsilon,tol=1e-14):
    beta=beta_matrix_modes(Q,N,M,epsilon,tol)
    out={}
    for a in range(2):
        term=matrix_times_vector(beta[a],vector_derivative(psi,a,epsilon,tol),tol)
        add_mode_dict(out,term,+1,tol)
    div={}
    for a in range(2):
        dA=matrix_derivative(beta[a],a,epsilon,tol)
        for k,A in dA.items():
            z=div.get(k,np.zeros_like(A))+A
            if np.linalg.norm(z)>tol:
                div[k]=z
            elif k in div:
                del div[k]
    add_mode_dict(out,matrix_times_vector(div,psi,tol),0.5,tol)
    return out


def route_commutator(Q,N,M,psi,epsilon,tol=1e-14):
    cache={}
    RM=route_apply(Q,M,psi,epsilon,tol,cache)
    RN=route_apply(Q,N,psi,epsilon,tol,cache)
    NRM=route_apply(Q,N,RM,epsilon,tol,cache)
    MRN=route_apply(Q,M,RN,epsilon,tol,cache)
    out=dict(NRM)
    add_mode_dict(out,MRN,-1,tol)
    return out


def vector_mode_norm2(psi):
    return float(sum(np.vdot(v,v).real for v in psi.values()))


def relative_defect(a,b,sign=+1):
    # ||a + sign*b|| / ||b||
    x=dict(a)
    add_mode_dict(x,b,sign)
    return math.sqrt(vector_mode_norm2(x))/max(math.sqrt(vector_mode_norm2(b)),1e-30)


def frozen_lapses(epsilon):
    # N=0.9+eps*(0.13 sin y + 0.07 cos z)
    # M=1.1+eps*(0.11 cos y + 0.09 sin z)
    N={
        (0,0):0.9+0j,
        (1,0):-0.5j*0.13*epsilon,
        (-1,0):+0.5j*0.13*epsilon,
        (0,1):0.5*0.07*epsilon,
        (0,-1):0.5*0.07*epsilon,
    }
    M={
        (0,0):1.1+0j,
        (1,0):0.5*0.11*epsilon,
        (-1,0):0.5*0.11*epsilon,
        (0,1):-0.5j*0.09*epsilon,
        (0,-1):+0.5j*0.09*epsilon,
    }
    return N,M


def carrier_state(d,carrier,index=0):
    v=np.zeros(d,complex); v[index]=1.0
    return {(int(carrier),int(carrier-1)):v}
