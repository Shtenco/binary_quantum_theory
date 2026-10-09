#!/usr/bin/env python3
"""Exact finite counterexample: same physical projector, different causal graph."""
from __future__ import annotations

import numpy as np


def projector_zero(M, tol=1e-12):
    w,U = np.linalg.eigh(M)
    z = np.abs(w) < tol
    return w, U[:,z] @ U[:,z].conj().T


def first_order(M, i, j, maxn=8, tol=1e-12):
    P=np.eye(M.shape[0])
    for n in range(maxn+1):
        if abs(P[j,i]) > tol:
            return n
        P=P@M
    return None


def run():
    M_path=np.array([
        [1.,-1.,0.],
        [-1.,2.,-1.],
        [0.,-1.,1.],
    ])

    M_complete=np.array([
        [2.,-1.,-1.],
        [-1.,2.,-1.],
        [-1.,-1.,2.],
    ])

    wp,Pp=projector_zero(M_path)
    wc,Pc=projector_zero(M_complete)

    assert np.min(wp)>-1e-12
    assert np.min(wc)>-1e-12
    assert np.linalg.norm(Pp-Pc) < 1e-12

    expected=np.ones((3,3))/3
    assert np.linalg.norm(Pp-expected) < 1e-12

    dp=first_order(M_path,0,2)
    dc=first_order(M_complete,0,2)

    assert dp == 2
    assert dc == 1
    assert abs(Pp[2,0]-Pc[2,0]) < 1e-12
    assert abs(Pp[2,0]-1/3) < 1e-12

    print("spec(path) =", wp)
    print("spec(complete) =", wc)
    print("||P_path-P_complete|| =", np.linalg.norm(Pp-Pc))
    print("P_phys[3,1] =", Pp[2,0])
    print("d_M path(1,3) =", dp)
    print("d_M complete(1,3) =", dc)
    print("SAME PROJECTOR / DIFFERENT CAUSAL ORDER")
    print("NO-GO PASS")


if __name__=="__main__":
    run()
