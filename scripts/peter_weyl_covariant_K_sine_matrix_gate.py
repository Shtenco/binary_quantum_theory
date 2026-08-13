#!/usr/bin/env python3
"""Exact shared-matrix state-to-state C_e(K_sine) gate.

This is a runtime-equivalent implementation of the physical sine-ordered
composition test.  It changes neither the operator nor any cutoff/projection.
The only algebraic optimization is common-subexpression elimination across the
four auxiliary 2x2 components:

    C_ij(K) = delta_ij K - sum_k h_ik K h^-1_kj.

For one input state, direct K is computed once.  For each pair (k,j), the
h^-1 branch and K action are computed once and then closed for both i=0,1.
Thus the full matrix uses 1 direct K + 4 conjugated K evaluations instead of
4 direct K + 8 conjugated K evaluations in the component-wise reference.

Both engines use H_E^sine=(T-T^dagger)/(2i), the same zero-aware volume,
complete charged projections, Jmax walls and acceptance thresholds.
"""
from __future__ import annotations

import argparse
import functools
import json
import math
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_covariant_volume_leg_gate as CV
import peter_weyl_covariant_composition_gate as COMP
import peter_weyl_covariant_K_composition_gate as KC
import peter_weyl_covariant_K_sine_composition_gate as SINEAD

TOL=1e-11


def freeze_state(state):
    return tuple(sorted(state.items(),key=lambda kv:repr(kv[0])))


@functools.lru_cache(maxsize=None)
def HE_key_cached(key,source_v,Jmax2,charged_nodes):
    out,vleak,bleak=SINEAD.complete_HE_sine(
        key,source_v,Jmax2,tuple(charged_nodes)
    )
    return tuple(out.items()),float(vleak),float(bleak)


def apply_HE(state,source_v,Jmax2,charged_nodes):
    out={}; max_v=0.0; max_b=0.0
    charged_nodes=tuple(charged_nodes)
    for key,amp in state.items():
        items,vleak,bleak=HE_key_cached(key,source_v,Jmax2,charged_nodes)
        max_v=max(max_v,vleak); max_b=max(max_b,bleak)
        COMP.add(out,dict(items),amp)
    return out,max_v,max_b


@functools.lru_cache(maxsize=None)
def K_state_cached(frozen,source_v,Jmax2,charged_nodes):
    state=dict(frozen)
    charged_nodes=tuple(charged_nodes)
    HE,v1,b1=apply_HE(state,source_v,Jmax2,charged_nodes)
    VH=KC.CK.apply_volume_complete_state(HE,source_v)
    Vstate=KC.CK.apply_volume_complete_state(state,source_v)
    HV,v2,b2=apply_HE(Vstate,source_v,Jmax2,charged_nodes)
    out={}; COMP.add(out,VH,+1); COMP.add(out,HV,-1)
    return tuple(out.items()),max(v1,v2),max(b1,b2)


def apply_K(state,source_v,Jmax2,charged_nodes):
    items,vleak,bleak=K_state_cached(
        freeze_state(state),source_v,Jmax2,tuple(charged_nodes)
    )
    return dict(items),vleak,bleak


def direct_K_covariant(state_cov,source_v,Jmax2):
    complete=COMP.covariant_to_complete(state_cov,source_v)
    K,vleak,bleak=apply_K(complete,source_v,Jmax2,(source_v,))
    return COMP.complete_to_covariant(K,source_v),vleak,bleak


def C_K_matrix(state_cov,source_v,target_v,Jmax2):
    direct,v0,b0=direct_K_covariant(state_cov,source_v,Jmax2)
    hKh=[[{} for _ in range(2)] for _ in range(2)]
    max_outer=0.0; max_v=float(v0); max_b=float(b0)

    # hKh_ij = sum_k h_ik K h^-1_kj.  For fixed (k,j), h^-1 and K are
    # independent of i and are reused exactly for both output indices.
    for j in range(2):
        for k in range(2):
            inv,oleak=COMP.inverse_complete(
                state_cov,source_v,target_v,k,j,Jmax2
            )
            max_outer=max(max_outer,float(oleak))
            Kinv,vleak,bleak=apply_K(
                inv,source_v,Jmax2,(source_v,target_v)
            )
            max_v=max(max_v,float(vleak)); max_b=max(max_b,float(bleak))
            for i in range(2):
                COMP.add(
                    hKh[i][j],
                    COMP.close_complete(Kinv,source_v,target_v,i,k,Jmax2)
                )

    out=[[{} for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            if i==j:
                COMP.add(out[i][j],direct,+1)
            COMP.add(out[i][j],hKh[i][j],-1)
    return out,{
        'outer_complete_basis_leakage':max_outer,
        'internal_volume_sector_leakage':max_v,
        'complete_charge_basis_leakage':max_b,
    }


def matrix_norm(matrix):
    return math.sqrt(sum(COMP.norm2(s) for row in matrix for s in row))


def weight_by_J(matrix):
    out={}
    for row in matrix:
        for state in row:
            for key,amp in state.items():
                J2=key[2]
                out[J2]=out.get(J2,0.0)+abs(amp)**2
    return {str(J2/2):float(x) for J2,x in sorted(out.items())}


def run(source_v=0,target_v=1):
    import peter_weyl_zeroaware_volume_migration_experiment as ZVM
    ZVM.patch_and_clear()
    HE_key_cached.cache_clear(); K_state_cached.cache_clear()

    old_complete=KC.CK.apply_HE_complete_key
    old_gauss=KC.KG.apply_HE_local
    KC.CK.apply_HE_complete_key=SINEAD.complete_HE_sine
    KC.KG.apply_HE_local=SINEAD.gauss_HE_sine_with_historical_K_cutoff
    if hasattr(KC.CK.HE_complete_cached,'cache_clear'):
        KC.CK.HE_complete_cached.cache_clear()
    try:
        initial=PW.basis_full_jhalf()[0]
        gauss_cov=CV.gauss_to_covariant({initial:1+0j},source_v)

        # Independent historical component-wise reference, but with the same
        # physical sine ordering patched into both representations.
        ref,refdiag=KC.reference_CK_matrix(initial,source_v,target_v,5)
        got,diag=C_K_matrix(gauss_cov,source_v,target_v,5)
        errors=[]; supports=[]
        for i in range(2):
            for j in range(2):
                errors.append(COMP.relerr(got[i][j],ref[i][j]))
                supports.append((len(got[i][j]),len(ref[i][j])))

        CVref=COMP.reference_CV_matrix(initial,source_v,target_v,3)
        J1state,J1key,J1amp=COMP.choose_J1_basis_state(CVref)
        second_target=next(w for w in PW.NEIG[source_v] if w!=target_v)
        second,diag2=C_K_matrix(J1state,source_v,second_target,7)
        weights=weight_by_J(second)
        total=sum(weights.values())
        forbidden=sum(
            x for J,x in ((float(k),v) for k,v in weights.items())
            if J>2.0+1e-15
        )
        scalar_relevant=sum(
            x for J,x in ((float(k),v) for k,v in weights.items())
            if J in (0.0,1.0)
        )
        second_norm=matrix_norm(second)
        max_spin=max(
            (max(key[0]) for row in second for state in row for key in state),
            default=0
        )/2

        passed=(
            max(errors,default=0.0)<1e-9
            and all(a==b for a,b in supports)
            and max(diag.values(),default=0.0)<1e-10
            and refdiag['outer_wrong_charge_fraction']<1e-18
            and refdiag['HE_wrong_charge_fraction']<1e-18
            and refdiag['K_wrong_charge_fraction']<1e-18
            and second_norm>1e-10
            and forbidden/max(total,1e-30)<1e-18
            and scalar_relevant>1e-14
            and max(diag2.values(),default=0.0)<1e-10
            and max_spin<=3.5+1e-12
        )
        hi=HE_key_cached.cache_info(); ki=K_state_cached.cache_info()
        return {
            'status':'exact shared-matrix C_e(K_sine) state-to-state gate',
            'passed':bool(passed),
            'euclidean_ordering':'sine-Hermitian (T-T^dagger)/(2i)',
            'K_definition':'K_sine=[V,H_E^sine]',
            'gauss_HE_cutoff':1e-9,
            'reference_edge':[source_v,target_v],
            'matrix_vs_component_reference_relative_errors':errors,
            'matrix_vs_component_reference_support_pairs':supports,
            'gauss_diagnostics':diag,
            'independent_reference_diagnostics':refdiag,
            'selected_J1_basis_key':repr(J1key),
            'selected_J1_reference_amplitude':[J1amp.real,J1amp.imag],
            'second_edge':[source_v,second_target],
            'second_CK_matrix_norm':second_norm,
            'second_CK_weight_by_source_J':weights,
            'second_CK_forbidden_J_gt_2_fraction':forbidden/max(total,1e-30),
            'second_CK_scalar_relevant_J01_weight':scalar_relevant,
            'second_CK_diagnostics':diag2,
            'second_CK_max_spin_reached':max_spin,
            'HE_key_cache':{'hits':hi.hits,'misses':hi.misses,'currsize':hi.currsize},
            'K_state_cache':{'hits':ki.hits,'misses':ki.misses,'currsize':ki.currsize},
            'exact_runtime_reduction':'full 2x2 matrix uses one direct K and four conjugated K evaluations per source state instead of four plus eight',
            'physics_changed':False,
            'next_use':'If PASS, use the same matrix engine inside the scalar K_sine-K_sine-V trace at Jmax=7/2.',
            'scope_note':'Exact runtime-equivalent composition gate; no K-K-V, H_L or HDA claim yet.',
        }
    finally:
        KC.CK.apply_HE_complete_key=old_complete
        KC.KG.apply_HE_local=old_gauss
        if hasattr(KC.CK.HE_complete_cached,'cache_clear'):
            KC.CK.HE_complete_cached.cache_clear()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--v',type=int,default=0)
    ap.add_argument('--w',type=int,default=1)
    ap.add_argument('--output',type=Path)
    a=ap.parse_args(); out=run(a.v,a.w); text=json.dumps(out,indent=2); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out.get('passed',False) else 1

if __name__=='__main__':
    raise SystemExit(main())
