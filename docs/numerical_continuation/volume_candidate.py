"""Experimental regular-tetrahedron orientation prescription, not production.

Q=-sum_r (-1)^r Q_(omit r)/4, V=sqrt(abs(Q)).
The 1/4 fixes the old Gauss normalization, not a physical prefactor.
"""
import sys, functools, itertools
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))
import k5_peter_weyl_safe_hda_column as P
import charged_intertwiner_recoupling_gate as CH
import peter_weyl_covariant_K_leg_gate as CK
import peter_weyl_covariant_volume_leg_gate as CV
import peter_weyl_zeroaware_volume_migration_experiment as Z

@functools.lru_cache(None)
def qmatrix(spins):
    dims=tuple(s+1 for s in spins); n=int(np.prod(dims))
    Q=np.zeros((n,n),complex)
    for omit in range(4):
        triple=tuple(x for x in range(4) if x!=omit)
        for xyz in itertools.permutations(range(3)):
            factors=[np.eye(d) for d in dims]
            for leg,a in zip(triple,xyz): factors[leg]=P.spin_mats_cached(spins[leg])[a]
            T=factors[0]
            for F in factors[1:]: T=np.kron(T,F)
            Q+=((-1)**(omit+1)/4)*P.EPS3[xyz]*T
    return (Q+Q.conj().T)/2

@functools.lru_cache(None)
def volume(spins):
    return Z.zeroaware_sqrt_abs(qmatrix(tuple(spins)))[0]

def apply_volume(T, spins):
    return (volume(tuple(spins))@T.reshape(-1)).reshape(T.shape)

@functools.lru_cache(None)
def reduced(spins,J):
    labels=CH.allowed_charged_labels(spins,J)
    B=np.column_stack([CH.charged_tensor(spins,a,b,J,J).reshape(-1) for a,b in labels])
    Q=B.conj().T@qmatrix(spins)@B
    return Z.zeroaware_sqrt_abs(Q)[0]

def install():
    Z.patch_and_clear()
    P.apply_volume_tensor=apply_volume
    CK.canonical_volume_block_general=reduced
    CV.canonical_charged_volume=lambda spins: reduced(tuple(spins),1)
    import peter_weyl_lorentzian_K_block_gate as KG
    for obj in (P.T_cached,KG.local_volume_column,getattr(P,'apply_H_cached',None),getattr(P,'apply_H_cached_state',None),CK.HE_complete_cached):
        if hasattr(obj,'cache_clear'): obj.cache_clear()
