#!/usr/bin/env python3
"""Exact scalar-channel accelerator for the physical sine-ordered K-K-V triple.

This is an alternative evaluator for the same structural object as
peter_weyl_lorentzian_sine_ordered_triple_gate.py, but moves already-proved
SU(2) selection pruning INTO the final charged projection instead of first
constructing forbidden J sectors and deleting them afterwards.

Right-to-left action on an initial source J=0 state:
  C(V) -> J=0,1;
  middle C(K_sine) -> only J=0,1 need be retained because the last rank-(0+1)
  operator cannot couple J=2 to final J=0;
  final C(K_sine) -> retain J=0 only.

No allowed scalar amplitude is approximated or threshold-adjusted.  The full
unrestricted reference triple remains the independent equivalence target.
"""
from __future__ import annotations

import argparse
import functools
import itertools
import json
import math
from pathlib import Path

import k5_peter_weyl_safe_hda_column as PW
import charged_intertwiner_recoupling_gate as CH
import peter_weyl_covariant_volume_leg_gate as CV
import peter_weyl_covariant_composition_gate as COMP
import peter_weyl_covariant_K_composition_gate as KC
import peter_weyl_covariant_K_composition_cached_gate as CACHE
import peter_weyl_covariant_K_sine_composition_gate as SINEK
import peter_weyl_zeroaware_volume_migration_experiment as ZVM

JMAX2=7
TOL=1e-11


def freeze(state):
    return tuple(sorted(state.items(),key=lambda kv:repr(kv[0])))


def project_allowed_J(branches,source_v,allowed_J2,tol=TOL):
    allowed_J2=frozenset(int(x) for x in allowed_J2)
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
        src_opts=[]
        possible=set(CV.all_total_J2(ls0)) & allowed_J2
        for J2 in sorted(possible):
            for M2 in PW.m2vals_t(J2):
                for K12,K34 in CH.allowed_charged_labels(tuple(ls0),J2):
                    B=CH.charged_tensor(tuple(ls0),K12,K34,J2,M2)
                    c=np.vdot(B,X0)
                    if abs(c)>1e-13:
                        src_opts.append((J2,M2,K12,K34,c))

        for chosen in itertools.product(*other_opts):
            base=amp; Kother=[]
            for u,(K,c) in enumerate(chosen):
                if u==source_v: Kother.append(-1)
                else:
                    Kother.append(K); base*=c
            for J2,M2,K12,K34,cs in src_opts:
                val=base*cs
                if abs(val)>tol:
                    key=(spins,tuple(Kother),J2,M2,K12,K34)
                    out[key]=out.get(key,0j)+val
    return {k:a for k,a in out.items() if abs(a)>tol}


def run(source_v=0,a=None,b=None,c=None):
    ZVM.patch_and_clear()
    neigh=PW.NEIG[source_v]
    if a is None or b is None or c is None:
        a,b,c=neigh[:3]
    if len({a,b,c})!=3 or any(x not in neigh for x in (a,b,c)):
        raise ValueError('a,b,c must be distinct neighbors of source_v')

    old_he=KC.CK.apply_HE_complete_key
    old_gauss=KC.KG.apply_HE_local
    old_k=KC.apply_K_complete_custom
    old_inv=COMP.inverse_complete
    old_direct=KC.direct_K_covariant

    @functools.lru_cache(maxsize=None)
    def he_reduced(canonical_key,v,Jmax2,charged_nodes):
        return SINEK.complete_HE_sine(canonical_key,v,Jmax2,charged_nodes=charged_nodes)
    def he_wrap(key,v,Jmax2,charged_nodes=(0,1)):
        charged_nodes=tuple(charged_nodes)
        canonical,original=CACHE.canonicalize_scalar_charge_M(key,charged_nodes)
        st,vl,bl=he_reduced(canonical,v,Jmax2,charged_nodes)
        return CACHE.restore_scalar_charge_M(st,charged_nodes,original),vl,bl

    @functools.lru_cache(maxsize=None)
    def k_cache(frozen,v,Jmax2,charged_nodes):
        st,vl,bl=old_k(dict(frozen),v,Jmax2,charged_nodes)
        return tuple(st.items()),float(vl),float(bl)
    def k_wrap(st,v,Jmax2,charged_nodes):
        items,vl,bl=k_cache(freeze(st),v,Jmax2,tuple(charged_nodes))
        return dict(items),vl,bl

    @functools.lru_cache(maxsize=None)
    def inv_cache(frozen,v,w,k,j,Jmax2):
        st,leak=old_inv(dict(frozen),v,w,k,j,Jmax2)
        return tuple(st.items()),float(leak)
    def inv_wrap(st,v,w,k,j,Jmax2):
        items,leak=inv_cache(freeze(st),v,w,k,j,Jmax2)
        return dict(items),leak

    @functools.lru_cache(maxsize=None)
    def direct_cache(frozen,v,Jmax2):
        st,vl,bl=old_direct(dict(frozen),v,Jmax2)
        return tuple(st.items()),float(vl),float(bl)
    def direct_wrap(st,v,Jmax2):
        items,vl,bl=direct_cache(freeze(st),v,Jmax2)
        return dict(items),vl,bl

    def close_allowed(st,v,w,i,k,Jmax2,allowed):
        out={}
        for key,amp in st.items():
            br=KC.CK.branch_from_key(key,amp)
            for hb in PW.apply_hit_branch(br,v,w,i,k,Jmax2):
                COMP.add(out,project_allowed_J([hb],v,allowed))
        return out

    def C_K_allowed(st,v,w,i,j,Jmax2,allowed):
        direct,vl0,bl0=direct_wrap(st,v,Jmax2)
        direct={key:amp for key,amp in direct.items() if key[2] in allowed}
        hKh={}; outer=0.0; vl=vl0; bl=bl0
        for k in range(2):
            inv,oleak=inv_wrap(st,v,w,k,j,Jmax2); outer=max(outer,oleak)
            kinv,vli,bli=k_wrap(inv,v,Jmax2,(v,w))
            vl=max(vl,vli); bl=max(bl,bli)
            COMP.add(hKh,close_allowed(kinv,v,w,i,k,Jmax2,allowed))
        out={}
        if i==j: COMP.add(out,direct,+1)
        COMP.add(out,hKh,-1)
        return out,{'outer':outer,'volume':vl,'primitive_charge':bl}

    KC.CK.apply_HE_complete_key=he_wrap
    KC.KG.apply_HE_local=SINEK.gauss_HE_sine_with_historical_K_cutoff
    KC.apply_K_complete_custom=k_wrap
    COMP.inverse_complete=inv_wrap
    KC.direct_K_covariant=direct_wrap
    try:
        initial=PW.basis_full_jhalf()[0]
        psi=CV.gauss_to_covariant({initial:1+0j},source_v)
        total={}; diag={'CV':0.0,'outer':0.0,'volume':0.0,'primitive_charge':0.0}
        rows=[]
        for i,j,k in itertools.product(range(2),repeat=3):
            s1,lv=COMP.C_volume_component(psi,source_v,c,k,i,JMAX2)
            diag['CV']=max(diag['CV'],float(lv))
            s2,d2=C_K_allowed(s1,source_v,b,j,k,JMAX2,(0,2)) if s1 else ({},{})
            if d2:
                for q in ('outer','volume','primitive_charge'): diag[q]=max(diag[q],d2[q])
            s3,d3=C_K_allowed(s2,source_v,a,i,j,JMAX2,(0,)) if s2 else ({},{})
            if d3:
                for q in ('outer','volume','primitive_charge'): diag[q]=max(diag[q],d3[q])
            COMP.add(total,s3)
            rows.append({'ijk':[i,j,k],'CV':len(s1),'mid_J01':len(s2),'final_J0':len(s3)})
        infos={
            'HE_reduced':he_reduced.cache_info(),
            'K_state':k_cache.cache_info(),
            'inverse_state':inv_cache.cache_info(),
            'direct_K_state':direct_cache.cache_info(),
        }
    finally:
        KC.CK.apply_HE_complete_key=old_he
        KC.KG.apply_HE_local=old_gauss
        KC.apply_K_complete_custom=old_k
        COMP.inverse_complete=old_inv
        KC.direct_K_covariant=old_direct

    norm=math.sqrt(sum(abs(x)**2 for x in total.values()))
    support=len(total)
    badJ=sum(abs(amp)**2 for key,amp in total.items() if key[2]!=0)
    maxspin=max((max(key[0]) for key in total),default=0)/2
    passed=(support>0 and norm>1e-10 and badJ<1e-20 and diag['CV']<1e-9
            and diag['outer']<1e-9 and diag['volume']<1e-9 and maxspin<=3.5+1e-12)
    return {
        'status':'exact SU(2)-channel-pruned physical sine K-K-V triple accelerator',
        'passed':bool(passed),
        'source_node':source_v,'ordered_edges':[a,b,c],'Jmax':3.5,
        'output_support':support,'output_norm':norm,'forbidden_final_J_weight':badJ,
        'max_spin_reached':maxspin,'diagnostics':diag,'path_supports':rows,
        'historical_primitive_charge_basis_diagnostic':{
            'value':diag['primitive_charge'],'hard_acceptance':False,
            'reason':'same primitive pre-sum diagnostic already classified by enforced C(K_sine) invariant audit'},
        'exact_selection_pruning':{
            'middle_allowed_J':[0,1],
            'final_allowed_J':[0],
            'reason':'rank-(0+1) final leg cannot couple J=2 to scalar J=0'},
        'runtime_cache':{n:{'hits':x.hits,'misses':x.misses,'currsize':x.currsize} for n,x in infos.items()},
        'reference_requirement':'Must match the unrestricted sine ordered triple on common output amplitudes before replacing it as the production evaluator.',
        'scope_note':'Accelerated one ordered triple, not yet the full epsilon-oriented H_L.'
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--v',type=int,default=0); ap.add_argument('--a',type=int)
    ap.add_argument('--b',type=int); ap.add_argument('--c',type=int); ap.add_argument('--output',type=Path)
    x=ap.parse_args(); out=run(x.v,x.a,x.b,x.c); text=json.dumps(out,indent=2); print(text)
    if x.output:
        x.output.parent.mkdir(parents=True,exist_ok=True); x.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__=='__main__': raise SystemExit(main())
