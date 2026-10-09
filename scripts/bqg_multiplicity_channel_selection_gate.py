#!/usr/bin/env python3
"""Regression gate for multiplicity-channel spectral selection stability."""
from __future__ import annotations
import numpy as np

def projector_for_index(A, idx):
    w,U=np.linalg.eigh((A+A.conj().T)/2)
    v=U[:,idx:idx+1]
    return w, v@v.conj().T

def run():
    rng=np.random.default_rng(20261009)
    worst=0.0
    trials=0
    for n in (2,3,4,5):
        for _ in range(100):
            vals=np.sort(rng.uniform(0.0,5.0,n))
            if np.min(np.diff(vals))<0.2:
                continue
            Q,_=np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))
            A=(Q*vals)@Q.conj().T
            idx=int(rng.integers(n))
            gap=min(abs(vals[idx]-vals[k]) for k in range(n) if k!=idx)
            X=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
            E=(X+X.conj().T)/2
            E*=0.1*gap/max(np.linalg.norm(E,2),1e-30)
            w,P=projector_for_index(A,idx)
            wt,Ut=np.linalg.eigh(A+E)
            # match perturbed eigenvalue nearest the original isolated value
            k=int(np.argmin(abs(wt-w[idx])))
            v=Ut[:,k:k+1]; Pt=v@v.conj().T
            lhs=np.linalg.norm(Pt-P,2)
            rhs=2*np.linalg.norm(E,2)/gap
            assert lhs<=rhs+1e-10,(n,lhs,rhs)
            worst=max(worst,lhs/max(rhs,1e-30)); trials+=1
    print("trials =",trials)
    print("max lhs/rhs =",worst)
    print("MULTIPLICITY CHANNEL STABILITY PASS")
    print("PASS")

if __name__=="__main__":
    run()
