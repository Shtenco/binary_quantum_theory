#!/usr/bin/env python3
"""Finite Euclidean EPRL-type simplicity-map control at gamma=1/3.

This is deliberately a small-spin diagnostic, not a production spin-foam code.
For boundary j=3/2 and gamma=1/3 the standard 0<gamma<1 embedding uses
j_plus=1 and j_minus=1/2.  Four-valent SU(2) intertwiners are embedded leg by
leg with Clebsch-Gordan coefficients, projected to separate + and - invariant
subspaces, and contracted through the two SU(2) 15j tensors.

Two choices are reported:
  * raw group-averaged simplicity/fusion map;
  * locally isometrized map F(F^dag F)^(-1/2), as a normalization-sensitivity
    control rather than a claim that this is the unique EPRL prescription.

The goal is to quantify how much simplicity changes the bare BF vertex at the
smallest convenient admissible spin and how strongly normalization choices
matter before the large-spin universality limit.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from functools import lru_cache
from pathlib import Path

import numpy as np
import sympy as sp
from sympy.physics.wigner import clebsch_gordan


def mvals(j):
    return np.array([j-r for r in range(int(round(2*j))+1)],dtype=float)


@lru_cache(None)
def cg(j1_2,j2_2,J_2,m1_2,m2_2,M_2):
    args=[sp.Rational(x,2) for x in (j1_2,j2_2,J_2,m1_2,m2_2,M_2)]
    return complex(clebsch_gordan(*args).evalf())


def CG(j1,j2,J,m1,m2,M):
    return cg(*(int(round(2*x)) for x in (j1,j2,J,m1,m2,M)))


def intertwiner_tensor(j,k):
    ms=mvals(j); km=mvals(k); d=len(ms)
    T=np.zeros((d,d,d,d),complex)
    for inds in itertools.product(range(d),repeat=4):
        m1,m2,m3,m4=(ms[q] for q in inds); val=0j
        for m in km:
            val+=((-1)**int(round(k-m)))/math.sqrt(2*k+1)*CG(j,j,k,m1,m2,m)*CG(j,j,k,m3,m4,-m)
        T[inds]=val
    return T


def epsilon_j(j):
    ms=mvals(j); E=np.zeros((len(ms),len(ms)),complex)
    for i,m in enumerate(ms):
        q=int(np.flatnonzero(np.isclose(ms,-m))[0]); E[i,q]=(-1)**int(round(j-m))
    return E


def apply_axis(T,axis,M):
    A=np.moveaxis(T,axis,0); B=np.tensordot(M,A,axes=(1,0)); return np.moveaxis(B,0,axis)


def vertex_tensor(j):
    ks=list(range(int(round(2*j))+1)); I=[intertwiner_tensor(j,float(k)) for k in ks]; E=epsilon_j(j)
    cache={}
    for v in range(5):
        neigh=[w for w in range(5) if w!=v]
        for q,T0 in enumerate(I):
            T=T0.copy()
            for ax,w in enumerate(neigh):
                if w<v: T=apply_axis(T,ax,E)
            cache[(v,q)]=T
    V=np.zeros((len(ks),)*5,complex)
    for ios in itertools.product(range(len(ks)),repeat=5):
        T=[cache[(v,ios[v])] for v in range(5)]
        V[ios]=np.einsum('abcd,aefg,behi,cfhj,dgij->',*T,optimize=True)
    return V


def fusion_coefficients(j=1.5,jp=1.0,jm=0.5):
    parent=[intertwiner_tensor(j,float(k)) for k in range(int(2*j)+1)]
    plus=[intertwiner_tensor(jp,float(k)) for k in range(int(2*jp)+1)]
    minus=[intertwiner_tensor(jm,float(k)) for k in range(int(2*jm)+1)]
    ms=mvals(j); mps=mvals(jp); mms=mvals(jm)
    yopts=[]
    for m in ms:
        opts=[]
        for ip,mp in enumerate(mps):
            for im,mm in enumerate(mms):
                if abs(mp+mm-m)<1e-12:
                    c=CG(jp,jm,j,mp,mm,m)
                    if abs(c)>1e-14: opts.append((ip,im,c))
        yopts.append(opts)
    f=np.zeros((len(parent),len(plus),len(minus)),complex)
    for ki,Ipar in enumerate(parent):
        mapped=np.zeros((len(mps),len(mms))*4,complex)
        for inds in itertools.product(range(len(ms)),repeat=4):
            amp=Ipar[inds]
            if abs(amp)<1e-14: continue
            for opts in itertools.product(*(yopts[q] for q in inds)):
                ix=[]; a=amp
                for ip,im,c in opts: ix.extend([ip,im]); a*=c
                mapped[tuple(ix)]+=a
        for a,Ip in enumerate(plus):
            for b,Im in enumerate(minus):
                val=0j
                for pidx in itertools.product(range(len(mps)),repeat=4):
                    ap=np.conj(Ip[pidx])
                    if abs(ap)<1e-14: continue
                    for midx in itertools.product(range(len(mms)),repeat=4):
                        am=np.conj(Im[midx])
                        if abs(am)<1e-14: continue
                        ix=(pidx[0],midx[0],pidx[1],midx[1],pidx[2],midx[2],pidx[3],midx[3])
                        val+=ap*am*mapped[ix]
                f[ki,a,b]=val
    return f


def eprl_vertex(f,Vp,Vm):
    return np.einsum('ABCDE,abcde,iAa,jBb,kCc,lDd,mEe->ijklm',Vp,Vm,f,f,f,f,f,optimize=True)


def reduced_one(psi,d=4):
    T=psi.reshape((d,)*5); A=T.reshape(d,-1); return A@A.conj().T


def entropy(rho):
    e=np.linalg.eigvalsh(rho); e=e[e>1e-14]; return float(-np.sum(e*np.log2(e)))


def diagnostics(A,bf):
    p=A.reshape(-1); n=float(np.vdot(p,p).real); p=p/math.sqrt(n)
    b=bf.reshape(-1); b=b/np.linalg.norm(b)
    rho=reduced_one(p,4); eig=np.linalg.eigvalsh(rho)
    return {"norm_squared":n,"nonzero_components":int(np.sum(np.abs(A)>1e-12)),"fidelity_to_bare_SU2_j3over2_15j":float(abs(np.vdot(b,p))**2),"one_tetra_reduced_eigenvalues":eig.tolist(),"one_tetra_entropy_bits":entropy(rho),"one_to_four_Schmidt_condition":float(math.sqrt(eig.max()/eig.min()))}


def run():
    gamma=1/3; j=1.5; jp=1.0; jm=0.5
    f=fusion_coefficients(j,jp,jm)
    M=f.reshape(4,6).T; G=M.conj().T@M; ge=np.linalg.eigvalsh(G)
    w,V=np.linalg.eigh(G); Miso=M@(V@np.diag(1/np.sqrt(w))@V.conj().T); fiso=Miso.T.reshape(4,3,2)
    Vp=vertex_tensor(jp); Vm=vertex_tensor(jm); bf=vertex_tensor(j)
    raw=eprl_vertex(f,Vp,Vm); iso=eprl_vertex(fiso,Vp,Vm)
    ph=raw.reshape(-1)/np.linalg.norm(raw); qi=iso.reshape(-1)/np.linalg.norm(iso)
    rawd=diagnostics(raw,bf); isod=diagnostics(iso,bf)
    cross=float(abs(np.vdot(ph,qi))**2)
    passed=(np.min(ge)>0 and np.linalg.norm(Miso.conj().T@Miso-np.eye(4))<1e-11 and rawd["fidelity_to_bare_SU2_j3over2_15j"]<0.99 and cross<0.99)
    return {"status":"finite Euclidean EPRL-type simplicity versus BF control","passed":bool(passed),"parameters":{"gamma":gamma,"boundary_j":j,"j_plus":jp,"j_minus":jm},"raw_fusion_Gram_eigenvalues":ge.tolist(),"raw_fusion_condition":float(math.sqrt(ge.max()/ge.min())),"isometrized_fusion_error":float(np.linalg.norm(Miso.conj().T@Miso-np.eye(4))),"raw_simplicity_vertex":rawd,"isometrized_simplicity_vertex":isod,"raw_vs_isometrized_vertex_fidelity":cross,"scope_note":"This uses the standard gamma<1 highest-spin leg embedding and explicit projection to separate plus/minus invariant sectors. It is a finite small-spin normalization-sensitivity control, not a claim that one edge-amplitude convention is the unique EPRL measure and not a Lorentzian continuum test."}


def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--output",type=Path); a=ap.parse_args(); out=run(); txt=json.dumps(out,indent=2); print(txt)
    if a.output: a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(txt+"\n",encoding="utf-8")
    return 0 if out["passed"] else 1

if __name__=="__main__": raise SystemExit(main())
