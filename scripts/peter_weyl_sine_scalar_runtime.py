#!/usr/bin/env python3
"""Shared exact reduced runtime for physical sine-ordered Lorentzian scalar DAGs.

One context owns the zero-aware volume convention, sine H_E ordering, rank-0
Wigner--Eckart H_E cache and state caches across MANY ordered triples.  This is
needed for the epsilon-oriented H_L sum; restarting Python for every permutation
would discard the common reduced operator blocks.

The only representation pruning is exact and preregistered:
  after the middle leg retain source J=0,1;
  after the final leg retain source J=0.
No support/amplitude threshold is loosened.
"""
from __future__ import annotations

import functools
import itertools
import math
import numpy as np

import k5_peter_weyl_safe_hda_column as PW
import charged_intertwiner_recoupling_gate as CH
import peter_weyl_covariant_volume_leg_gate as CV
import peter_weyl_covariant_composition_gate as COMP
import peter_weyl_covariant_K_composition_gate as KC
import peter_weyl_covariant_K_composition_cached_gate as CACHE
import peter_weyl_covariant_K_sine_composition_gate as SINEK
import peter_weyl_zeroaware_volume_migration_experiment as ZVM

TOL=1e-11


def freeze(state):
    return tuple(sorted(state.items(),key=lambda kv:repr(kv[0])))


def add(dst,src,scale=1.0,tol=TOL):
    for key,amp in src.items():
        z=dst.get(key,0j)+scale*amp
        if abs(z)>tol: dst[key]=z
        elif key in dst: del dst[key]


def project_allowed_J(branches,source_v,allowed_J2,tol=TOL):
    allowed=frozenset(int(x) for x in allowed_J2)
    out={}
    for spins,tensors,amp in branches:
        other_opts=[]; ok=True
        for u in PW.VERT:
            if u==source_v:
                other_opts.append(((None,1+0j),)); continue
            ls=PW.local_spins(spins,u); opts=[]
            for K in PW.allowed_k2_t(*ls):
                c=np.vdot(PW.oriented_intertwiner(u,ls,K),tensors[u])
                if abs(c)>1e-13: opts.append((K,c))
            if not opts:
                ok=False; break
            other_opts.append(tuple(opts))
        if not ok: continue

        ls0=PW.local_spins(spins,source_v)
        X0=CV.unorient_local(tensors[source_v],ls0,source_v)
        src=[]
        for J2 in sorted(set(CV.all_total_J2(ls0)) & allowed):
            for M2 in PW.m2vals_t(J2):
                for K12,K34 in CH.allowed_charged_labels(tuple(ls0),J2):
                    B=CH.charged_tensor(tuple(ls0),K12,K34,J2,M2)
                    c=np.vdot(B,X0)
                    if abs(c)>1e-13: src.append((J2,M2,K12,K34,c))

        for chosen in itertools.product(*other_opts):
            base=amp; Kother=[]
            for u,(K,c) in enumerate(chosen):
                if u==source_v: Kother.append(-1)
                else:
                    Kother.append(K); base*=c
            for J2,M2,K12,K34,c in src:
                val=base*c
                if abs(val)>tol:
                    key=(spins,tuple(Kother),J2,M2,K12,K34)
                    out[key]=out.get(key,0j)+val
    return {k:a for k,a in out.items() if abs(a)>tol}


class SineScalarRuntime:
    def __init__(self,source_v=0,Jmax2=7):
        self.v=int(source_v); self.Jmax2=int(Jmax2); self._installed=False
        self.diag={'CV_complete_basis_leakage':0.0,'CK_outer_complete_basis_leakage':0.0,
                   'CK_internal_volume_sector_leakage':0.0,'CK_primitive_charge_basis_diagnostic':0.0}

    def __enter__(self):
        ZVM.patch_and_clear()
        self.old_he=KC.CK.apply_HE_complete_key
        self.old_gauss=KC.KG.apply_HE_local
        self.old_k=KC.apply_K_complete_custom
        self.old_inv=COMP.inverse_complete
        self.old_direct=KC.direct_K_covariant

        @functools.lru_cache(maxsize=None)
        def he_reduced(canonical_key,v,Jmax2,charged_nodes):
            return SINEK.complete_HE_sine(canonical_key,v,Jmax2,charged_nodes=charged_nodes)
        self.he_reduced=he_reduced

        def he_wrap(key,v,Jmax2,charged_nodes=(0,1)):
            charged_nodes=tuple(charged_nodes)
            canonical,original=CACHE.canonicalize_scalar_charge_M(key,charged_nodes)
            st,vl,bl=he_reduced(canonical,v,Jmax2,charged_nodes)
            return CACHE.restore_scalar_charge_M(st,charged_nodes,original),vl,bl
        self.he_wrap=he_wrap

        @functools.lru_cache(maxsize=None)
        def k_cache(frozen,v,Jmax2,charged_nodes):
            st,vl,bl=self.old_k(dict(frozen),v,Jmax2,charged_nodes)
            return tuple(st.items()),float(vl),float(bl)
        self.k_cache=k_cache
        def k_wrap(st,v,Jmax2,charged_nodes):
            items,vl,bl=k_cache(freeze(st),v,Jmax2,tuple(charged_nodes)); return dict(items),vl,bl
        self.k_wrap=k_wrap

        @functools.lru_cache(maxsize=None)
        def inv_cache(frozen,v,w,k,j,Jmax2):
            st,leak=self.old_inv(dict(frozen),v,w,k,j,Jmax2); return tuple(st.items()),float(leak)
        self.inv_cache=inv_cache
        def inv_wrap(st,v,w,k,j,Jmax2):
            items,leak=inv_cache(freeze(st),v,w,k,j,Jmax2); return dict(items),leak
        self.inv_wrap=inv_wrap

        @functools.lru_cache(maxsize=None)
        def direct_cache(frozen,v,Jmax2):
            st,vl,bl=self.old_direct(dict(frozen),v,Jmax2); return tuple(st.items()),float(vl),float(bl)
        self.direct_cache=direct_cache
        def direct_wrap(st,v,Jmax2):
            items,vl,bl=direct_cache(freeze(st),v,Jmax2); return dict(items),vl,bl
        self.direct_wrap=direct_wrap

        KC.CK.apply_HE_complete_key=he_wrap
        KC.KG.apply_HE_local=SINEK.gauss_HE_sine_with_historical_K_cutoff
        KC.apply_K_complete_custom=k_wrap
        COMP.inverse_complete=inv_wrap
        KC.direct_K_covariant=direct_wrap
        self._installed=True
        return self

    def __exit__(self,exc_type,exc,tb):
        if self._installed:
            KC.CK.apply_HE_complete_key=self.old_he
            KC.KG.apply_HE_local=self.old_gauss
            KC.apply_K_complete_custom=self.old_k
            COMP.inverse_complete=self.old_inv
            KC.direct_K_covariant=self.old_direct
            self._installed=False
        return False

    def close_allowed(self,st,w,i,k,allowed):
        out={}
        for key,amp in st.items():
            br=KC.CK.branch_from_key(key,amp)
            for hb in PW.apply_hit_branch(br,self.v,w,i,k,self.Jmax2):
                add(out,project_allowed_J([hb],self.v,allowed))
        return out

    def C_K_allowed(self,st,w,i,j,allowed):
        direct,vl0,bl0=self.direct_wrap(st,self.v,self.Jmax2)
        direct={key:amp for key,amp in direct.items() if key[2] in allowed}
        hKh={}; outer=0.0; vl=vl0; bl=bl0
        for k in range(2):
            inv,oleak=self.inv_wrap(st,self.v,w,k,j,self.Jmax2); outer=max(outer,oleak)
            kinv,vli,bli=self.k_wrap(inv,self.v,self.Jmax2,(self.v,w))
            vl=max(vl,vli); bl=max(bl,bli)
            add(hKh,self.close_allowed(kinv,w,i,k,allowed))
        out={}
        if i==j: add(out,direct,+1)
        add(out,hKh,-1)
        self.diag['CK_outer_complete_basis_leakage']=max(self.diag['CK_outer_complete_basis_leakage'],outer)
        self.diag['CK_internal_volume_sector_leakage']=max(self.diag['CK_internal_volume_sector_leakage'],vl)
        self.diag['CK_primitive_charge_basis_diagnostic']=max(self.diag['CK_primitive_charge_basis_diagnostic'],bl)
        return out

    def initial_covariant(self):
        initial=PW.basis_full_jhalf()[0]
        return CV.gauss_to_covariant({initial:1+0j},self.v)

    def ordered_triple(self,a,b,c,psi=None):
        if psi is None: psi=self.initial_covariant()
        total={}; rows=[]
        for i,j,k in itertools.product(range(2),repeat=3):
            s1,lv=COMP.C_volume_component(psi,self.v,c,k,i,self.Jmax2)
            self.diag['CV_complete_basis_leakage']=max(self.diag['CV_complete_basis_leakage'],float(lv))
            s2=self.C_K_allowed(s1,b,j,k,(0,2)) if s1 else {}
            s3=self.C_K_allowed(s2,a,i,j,(0,)) if s2 else {}
            add(total,s3)
            rows.append({'ijk':[i,j,k],'CV':len(s1),'middle_J01':len(s2),'final_J0':len(s3)})
        return total,rows

    def cache_info(self):
        infos={'HE_reduced':self.he_reduced.cache_info(),'K_state':self.k_cache.cache_info(),
               'inverse_state':self.inv_cache.cache_info(),'direct_K_state':self.direct_cache.cache_info()}
        return {n:{'hits':x.hits,'misses':x.misses,'currsize':x.currsize} for n,x in infos.items()}


def state_norm(st): return math.sqrt(sum(abs(a)**2 for a in st.values()))
def max_spin(st): return max((max(k[0]) for k in st),default=0)/2
