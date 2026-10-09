#!/usr/bin/env python3
"""Regression gate for the BQG refinement-projector stability theorem."""
from __future__ import annotations

import numpy as np


def zero_projector(M, tol=1e-10):
    w,U=np.linalg.eigh((M+M.conj().T)/2)
    scale=max(float(np.max(np.abs(w))),1.0)
    z=np.abs(w)<tol*scale
    P=U[:,z]@U[:,z].conj().T
    pos=w[~z]
    gap=float(np.min(pos)) if len(pos) else np.inf
    return P,gap


def random_psd_with_kernel(rng,n,k):
    X=rng.normal(size=(n,n-k))+1j*rng.normal(size=(n,n-k))
    Q,_=np.linalg.qr(X)
    vals=rng.uniform(0.4,3.0,n-k)
    M=(Q*vals)@Q.conj().T
    return (M+M.conj().T)/2


def random_isometry(rng,nfine,ncoarse):
    X=rng.normal(size=(nfine,ncoarse))+1j*rng.normal(size=(nfine,ncoarse))
    Q,_=np.linalg.qr(X)
    return Q[:,:ncoarse]


def one_trial(rng,nc,nf,kc,kf):
    Md=random_psd_with_kernel(rng,nc,kc)
    Mf=random_psd_with_kernel(rng,nf,kf)
    Iota=random_isometry(rng,nf,nc)

    Pd,gd=zero_projector(Md)
    Pf,gf=zero_projector(Mf)

    R=Mf@Iota-Iota@Md
    lhs=np.linalg.norm(Pf@Iota-Iota@Pd,2)
    rhs=np.linalg.norm(R,2)/min(gd,gf)

    leak_phys=np.linalg.norm((np.eye(nf)-Pf)@Iota@Pd,2)
    leak_unphys=np.linalg.norm(Pf@Iota@(np.eye(nc)-Pd),2)

    assert leak_phys <= np.linalg.norm(R,2)/gf + 1e-8
    assert leak_unphys <= np.linalg.norm(R,2)/gd + 1e-8
    assert lhs <= rhs + 1e-8
    return lhs,rhs


def exact_intertwining_control(rng):
    # Construct Mf so that a chosen coarse block is exactly embedded.
    nc,nf=5,8
    Md=random_psd_with_kernel(rng,nc,1)
    Iota=random_isometry(rng,nf,nc)
    Qfull,_=np.linalg.qr(np.column_stack([
        Iota,
        rng.normal(size=(nf,nf-nc))+1j*rng.normal(size=(nf,nf-nc))
    ]))
    Iota=Qfull[:,:nc]
    J=Qfull[:,nc:]
    extra=np.diag(np.linspace(1.2,2.0,nf-nc))
    Mf=Iota@Md@Iota.conj().T + J@extra@J.conj().T
    Pf,gf=zero_projector(Mf)
    Pd,gd=zero_projector(Md)
    R=Mf@Iota-Iota@Md
    assert np.linalg.norm(R)<1e-10
    assert np.linalg.norm(Pf@Iota-Iota@Pd)<1e-9


def run():
    rng=np.random.default_rng(20261009)
    ratios=[]
    for nc,nf,kc,kf in [
        (4,7,1,1),(5,8,1,2),(6,10,2,1),(7,11,2,3)
    ]:
        for _ in range(20):
            lhs,rhs=one_trial(rng,nc,nf,kc,kf)
            ratios.append(lhs/rhs if rhs>1e-14 else 0.0)

    exact_intertwining_control(rng)

    print("random trials =",len(ratios))
    print("max observed lhs/rhs =",max(ratios))
    print("PROJECTOR INTERTWINING BOUND PASS")
    print("EXACT R=0 COROLLARY PASS")
    print("PASS")


if __name__=="__main__":
    run()
