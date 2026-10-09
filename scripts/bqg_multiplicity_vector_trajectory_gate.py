#!/usr/bin/env python3
"""Regression for the multiplicity-vector trajectory theorem."""
from __future__ import annotations
import numpy as np

def run():
    rng=np.random.default_rng(20261010)
    worst=0.0
    for m in (1,2,3,5):
        for _ in range(50):
            v=rng.normal(size=m)+1j*rng.normal(size=m)
            u=rng.normal(size=m)+1j*rng.normal(size=m)
            v/=np.linalg.norm(v); u/=np.linalg.norm(u)
            Pblock=np.kron(np.outer(v,v.conj()),np.eye(2))
            Pmaster=np.kron(np.outer(u,u.conj()),np.eye(2))
            F=abs(np.vdot(u,v))**2
            tr=float(np.trace(Pblock@Pmaster).real/2)
            chi=np.linalg.norm(Pblock-Pmaster,2)
            target=np.sqrt(max(0.0,1-F))
            assert abs(F-tr)<1e-12
            assert abs(chi-target)<1e-11
            worst=max(worst,abs(chi-target))
    print("max projector-angle identity error =",worst)
    print("MULTIPLICITY VECTOR TRAJECTORY PASS")
    print("PASS")

if __name__=="__main__":
    run()
