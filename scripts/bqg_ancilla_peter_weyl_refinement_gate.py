#!/usr/bin/env python3
"""Regression gate for the ancilla-assisted Peter-Weyl refinement theorem."""
from __future__ import annotations
import numpy as np
from q2_symmetric_block_peter_weyl_growth_gate import spin_matrices_from_symmetric_n

# Use the same occupation-order convention as the old and new spin bases.
S=spin_matrices_from_symmetric_n(1)

def inclusion(n:int):
    # codomain basis: old occupation k=0..n, ancilla a=0,1
    J=np.zeros(((n+1)*2,n+2),complex)
    for k in range(n+2):
        if k<=n:
            J[2*k+0,k]=np.sqrt((n+1-k)/(n+1))
        if k>=1:
            J[2*(k-1)+1,k]=np.sqrt(k/(n+1))
    return J

def run():
    worst_iso=0.0; worst_int=0.0
    for n in range(1,9):
        J=inclusion(n)
        old=spin_matrices_from_symmetric_n(n)
        new=spin_matrices_from_symmetric_n(n+1)
        iso=np.linalg.norm(J.conj().T@J-np.eye(n+2))
        worst_iso=max(worst_iso,float(iso))
        for a in range(3):
            total=np.kron(old[a],np.eye(2))+np.kron(np.eye(n+1),S[a])
            err=np.linalg.norm(total@J-J@new[a])
            worst_int=max(worst_int,float(err))
            assert err<1e-11,(n,a,err)
        assert iso<1e-12
    print("max isometry error =",worst_iso)
    print("max SU2 intertwiner error =",worst_int)
    print("ANCILLA-ASSISTED PETER-WEYL REFINEMENT PASS")
    print("PASS")

if __name__=="__main__":
    run()
