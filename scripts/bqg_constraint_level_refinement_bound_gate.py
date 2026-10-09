#!/usr/bin/env python3
"""Regression for the constraint-level master-refinement identity."""
from __future__ import annotations
import numpy as np

def herm(rng,n):
    X=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
    return (X+X.conj().T)/2

def iso(rng,nc,nf):
    X=rng.normal(size=(nc,nf))+1j*rng.normal(size=(nc,nf))
    Q,_=np.linalg.qr(X)
    return Q[:,:nf]

def run():
    rng=np.random.default_rng(20261010)
    worst=0.0
    for nf,nc,m in [(3,5,2),(4,7,3),(5,9,5)]:
        for _ in range(40):
            I=iso(rng,nc,nf)
            Cf=[herm(rng,nf) for _ in range(m)]
            Cc=[herm(rng,nc) for _ in range(m)]
            s=float(rng.uniform(0.2,2.0))
            Mf=sum((C@C for C in Cf),np.zeros((nf,nf),complex))
            Mc=sum((C@C for C in Cc),np.zeros((nc,nc),complex))
            R=Mc@I-s*s*I@Mf
            rhs=np.zeros_like(R)
            bound=0.0
            for A,B in zip(Cc,Cf):
                E=A@I-s*I@B
                rhs += A@E+s*E@B
                bound += (np.linalg.norm(A,2)+s*np.linalg.norm(B,2))*np.linalg.norm(E,2)
            assert np.linalg.norm(R-rhs)<1e-9
            nr=np.linalg.norm(R,2)
            assert nr<=bound+1e-9
            worst=max(worst,nr/max(bound,1e-30))
    print("max ||R||/bound =",worst)
    print("CONSTRAINT-LEVEL MASTER REFINEMENT IDENTITY PASS")
    print("PASS")

if __name__=="__main__":
    run()
