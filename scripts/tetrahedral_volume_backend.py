#!/usr/bin/env python3
"""Tetrahedrally covariant four-leg volume completion on charged sectors.

The historical magnetic/covariant implementation used q_123 on the first three
local legs.  On a Gauss J=0 four-valent intertwiner this is sufficient (up to an
overall orientation/sign normalization), but a Thiemann word inserts V after
holonomy hits where the source is charged and total J need not vanish.  There a
fixed q_123 extension selects a preferred fourth leg.

Define instead the normalized oriented tetrahedral grasping

  Q_tet = (1/4) sum_{r=0}^3 (-1)^r q_{all legs except r}

in the canonical local-slot orientation.  The vertex orientation multiplies all
four terms by one common sign and therefore drops out of V=sqrt(abs(Q_tet)).
The factor 1/4 preserves the already frozen Gauss-sector absolute-volume
normalization: on J=0, Q_tet is +/- q_123 and hence V_tet=V_123.

The implementation works blockwise in exact total-(J,M) recoupling sectors and
uses the same zero-aware spectral functional calculus as the v1.2 production
volume.  It never constructs the exponentially larger global spin-network
Hilbert space.
"""
from __future__ import annotations
import functools,itertools
from contextlib import contextmanager
import numpy as np
import k5_peter_weyl_safe_hda_column as PW
import charged_intertwiner_recoupling_gate as CH
import peter_weyl_covariant_volume_leg_gate as CV
import peter_weyl_covariant_K_leg_gate as CK
import peter_weyl_lorentzian_K_block_gate as KG
import peter_weyl_zeroaware_volume_migration_experiment as ZVM

NORM=0.25

def apply_q_tetra(T,spins_local):
    spins_local=tuple(spins_local);mats=[PW.spin_mats_cached(s) for s in spins_local]
    Y=np.zeros_like(T,dtype=complex)
    for omitted in range(4):
        tri=tuple(r for r in range(4) if r!=omitted);pref=NORM*((-1)**omitted)
        for a,b,c in itertools.product(range(3),repeat=3):
            e=PW.EPS3[a,b,c]
            if not e:continue
            X=T
            # Axis applications commute across distinct legs. Reverse order only
            # avoids any accidental interpretation as same-leg operator order.
            for leg,axis in reversed(tuple(zip(tri,(a,b,c)))):
                X=PW.apply_axis_np(X,leg,mats[leg][axis])
            Y += pref*e*X
    return Y

@functools.lru_cache(maxsize=None)
def tetra_q_block(spins_local,J2,M2):
    spins_local=tuple(spins_local);labels=CH.allowed_charged_labels(spins_local,J2)
    basis=[CH.charged_tensor(spins_local,a,b,J2,M2) for a,b in labels]
    Q=np.zeros((len(labels),len(labels)),complex);max_abs=0.0;max_rel=0.0
    for j,B in enumerate(basis):
        QB=apply_q_tetra(B,spins_local)
        coeff=np.asarray([np.vdot(A,QB) for A in basis],complex)
        recon=sum((c*A for c,A in zip(coeff,basis)),np.zeros_like(QB))
        Q[:,j]=coeff;err=float(np.linalg.norm(QB-recon));rel=err/max(float(np.linalg.norm(QB)),1e-30)
        max_abs=max(max_abs,err);max_rel=max(max_rel,rel)
    return 0.5*(Q+Q.conj().T),max_abs,max_rel

@functools.lru_cache(maxsize=None)
def tetra_volume_block_general(spins_local,J2):
    spins_local=tuple(spins_local);blocks=[]
    for M2 in PW.m2vals_t(J2):blocks.append(tetra_q_block(spins_local,J2,M2)[0])
    Q=sum(blocks)/len(blocks);Q=0.5*(Q+Q.conj().T)
    return ZVM.zeroaware_sqrt_abs(Q)[0]

def tetra_charged_volume(spins_local):
    return tetra_volume_block_general(tuple(spins_local),1)

def apply_tetra_volume_tensor(T,spins_local):
    """Apply V_tet to an arbitrary local magnetic tensor via complete J blocks."""
    spins_local=tuple(spins_local);Y=np.zeros_like(T,dtype=complex);recon=np.zeros_like(T,dtype=complex)
    for J2 in CV.all_total_J2(spins_local):
        labels=CH.allowed_charged_labels(spins_local,J2)
        if not labels:continue
        V=tetra_volume_block_general(spins_local,J2)
        for M2 in PW.m2vals_t(J2):
            basis=[CH.charged_tensor(spins_local,a,b,J2,M2) for a,b in labels]
            coeff=np.asarray([np.vdot(B,T) for B in basis],complex)
            for c,B in zip(coeff,basis):recon+=c*B
            out=V@coeff
            for c,B in zip(out,basis):Y+=c*B
    return Y

def clear_tetra_caches():
    tetra_q_block.cache_clear();tetra_volume_block_general.cache_clear()

@contextmanager
def install_tetrahedral_volume_backend():
    """Install only the volume extension; restore every historical function on exit."""
    old_apply=PW.apply_volume_tensor
    old_charged=CV.canonical_charged_volume
    old_general=CK.canonical_volume_block_general
    # Ensure the common spectral zero convention is active before replacing the
    # q-construction itself.
    ZVM.patch_and_clear();clear_tetra_caches()
    PW.apply_volume_tensor=apply_tetra_volume_tensor
    CV.canonical_charged_volume=tetra_charged_volume
    CK.canonical_volume_block_general=tetra_volume_block_general
    for obj in (getattr(KG,'local_volume_column',None),getattr(PW,'apply_H_cached',None),
                getattr(PW,'apply_H_cached_state',None),getattr(CK,'HE_complete_cached',None)):
        if hasattr(obj,'cache_clear'):obj.cache_clear()
    try:
        yield
    finally:
        PW.apply_volume_tensor=old_apply
        CV.canonical_charged_volume=old_charged
        CK.canonical_volume_block_general=old_general
        for obj in (getattr(KG,'local_volume_column',None),getattr(PW,'apply_H_cached',None),
                    getattr(PW,'apply_H_cached_state',None),getattr(CK,'HE_complete_cached',None)):
            if hasattr(obj,'cache_clear'):obj.cache_clear()
        clear_tetra_caches()
