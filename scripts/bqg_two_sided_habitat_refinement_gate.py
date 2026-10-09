#!/usr/bin/env python3
"""Regression gate for the two-sided habitat refinement theorem."""
from __future__ import annotations
import numpy as np

def iso(rng,nc,nf):
    X=rng.normal(size=(nc,nf))+1j*rng.normal(size=(nc,nf))
    Q,_=np.linalg.qr(X)
    return Q[:,:nf]

def run():
    rng=np.random.default_rng(20261010)
    worst=0.0
    for _ in range(100):
        n0f,n1f,n0c,n1c,m=3,5,6,8,4
        i0=iso(rng,n0c,n0f)
        i1=iso(rng,n1c,n1f)
        Cf=[]; Cc=[]
        for _a in range(m):
            Cf.append(rng.normal(size=(n1f,n0f))+1j*rng.normal(size=(n1f,n0f)))
            Cc.append(rng.normal(size=(n1c,n0c))+1j*rng.normal(size=(n1c,n0c)))
        Mf=sum((C.conj().T@C for C in Cf),np.zeros((n0f,n0f),complex))
        Mc=sum((C.conj().T@C for C in Cc),np.zeros((n0c,n0c),complex))
        R=Mc@i0-i0@Mf
        rhs=np.zeros_like(R); bound=0.0
        pull=np.zeros((n0f,n0f),complex); pbound=0.0
        for A,B in zip(Cc,Cf):
            E=A@i0-i1@B
            F=A.conj().T@i1-i0@B.conj().T
            rhs += A.conj().T@E+F@B
            bound += np.linalg.norm(A,2)*np.linalg.norm(E,2)+np.linalg.norm(F,2)*np.linalg.norm(B,2)
            pull += B.conj().T@i1.conj().T@E+E.conj().T@i1@B+E.conj().T@E
            pbound += 2*np.linalg.norm(B,2)*np.linalg.norm(E,2)+np.linalg.norm(E,2)**2
        assert np.linalg.norm(R-rhs)<1e-9
        assert np.linalg.norm(R,2)<=bound+1e-9
        D=i0.conj().T@Mc@i0-Mf
        assert np.linalg.norm(D-pull)<1e-9
        assert np.linalg.norm(D,2)<=pbound+1e-9
        worst=max(worst,np.linalg.norm(R,2)/max(bound,1e-30))
    print("max master residual / bound =",worst)
    print("TWO-SIDED HABITAT REFINEMENT PASS")
    print("PASS")

if __name__=="__main__":
    run()
