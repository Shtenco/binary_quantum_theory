#!/usr/bin/env python3
"""Regression for scale-free refinement residual invariance."""
from __future__ import annotations
import numpy as np

def zero_data(M,tol=1e-10):
    w,U=np.linalg.eigh((M+M.conj().T)/2)
    z=np.abs(w)<tol*max(np.max(np.abs(w)),1.0)
    P=U[:,z]@U[:,z].conj().T
    pos=w[~z]
    return P,float(np.min(pos))

def eps_grid(Mf,Mc,Iota):
    Pf,df=zero_data(Mf); Pc,dc=zero_data(Mc)
    rs=np.logspace(-3,3,2000)
    vals=[]
    for r in rs:
        vals.append(np.linalg.norm(Mc@Iota-r*Iota@Mf,2)/min(dc,r*df))
    return min(vals),np.linalg.norm(Pc@Iota-Iota@Pf,2)

def run():
    rng=np.random.default_rng(20261010)
    worst=0.0
    for _ in range(30):
        nf,nc=5,8
        X=rng.normal(size=(nf,nf-1))+1j*rng.normal(size=(nf,nf-1))
        Q,_=np.linalg.qr(X)
        vf=rng.uniform(0.5,3,nf-1)
        Mf=(Q*vf)@Q.conj().T
        Y=rng.normal(size=(nc,nc-1))+1j*rng.normal(size=(nc,nc-1))
        Qc,_=np.linalg.qr(Y)
        vc=rng.uniform(0.5,3,nc-1)
        Mc=(Qc*vc)@Qc.conj().T
        Z=rng.normal(size=(nc,nf))+1j*rng.normal(size=(nc,nf))
        Iota,_=np.linalg.qr(Z); Iota=Iota[:,:nf]

        e,lhs=eps_grid(Mf,Mc,Iota)
        assert lhs<=e+5e-3

        a=float(rng.uniform(0.2,5)); b=float(rng.uniform(0.2,5))
        e2,_=eps_grid(a*Mf,b*Mc,Iota)
        rel=abs(e-e2)/max(e,1e-12)
        worst=max(worst,rel)
        assert rel<2e-2
    print("max scale-invariance grid error =",worst)
    print("SCALE-FREE REFINEMENT BOUND PASS")
    print("PASS")

if __name__=="__main__":
    run()
