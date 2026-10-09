#!/usr/bin/env python3
"""Regression gate for the canonical selected-channel intertwiner theorem."""
from __future__ import annotations
import itertools
import numpy as np
import peter_weyl_j1_s4_block_gate as J1

PERMS=tuple(itertools.permutations(range(4)))

def run():
    # Use the known j=1/2 and j=1 [2,2] copies.
    reps_f=[J1.permutation_matrix(1,p) for p in PERMS]
    reps_c_full=[J1.permutation_matrix(2,p) for p in PERMS]

    # Canonical j=1 [2,2] embedding already registered in the repository.
    W=np.column_stack([
        np.array([0.0,1.0,0.0],complex),
        np.array([2/3,0.0,-np.sqrt(5)/3],complex),
    ])
    reps_c=[W.conj().T@U@W for U in reps_c_full]

    rng=np.random.default_rng(20261010)
    X=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
    Y=np.zeros((2,2),complex)
    for Uf,Uc in zip(reps_f,reps_c):
        Y += Uc@X@Uf.conj().T
    Y/=24

    gram=Y.conj().T@Y
    alpha=float(np.trace(gram).real/2)
    assert alpha>1e-12
    Iota=Y/np.sqrt(alpha)

    assert np.linalg.norm(Iota.conj().T@Iota-np.eye(2))<1e-10
    err=max(np.linalg.norm(Uc@Iota-Iota@Uf) for Uf,Uc in zip(reps_f,reps_c))
    assert err<1e-10

    print("alpha =",alpha)
    print("isometry_error =",np.linalg.norm(Iota.conj().T@Iota-np.eye(2)))
    print("max_intertwiner_error =",err)
    print("CANONICAL SELECTED-CHANNEL INTERTWINER PASS")
    print("PASS")

if __name__=="__main__":
    run()
