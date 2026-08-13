#!/usr/bin/env python3
"""State-to-state composition gate for C_e(K)=h[h^-1,K].

The existing peter_weyl_covariant_K_leg_gate constructs C_e(K) on one Gauss
input.  The Lorentzian triple needs C_e(K) to act after another covariant leg,
when the source is already in an explicit total-J sector.

This module keeps that source representation explicit throughout:

* direct K=[V,H_E] on a covariant input projects only the source in all J and
  every other node to Gauss;
* after h^-1 on edge (v,w), both v and w are retained in complete all-J bases;
* K acts before any premature J=1/2 projection;
* the forward h closes w and only then the final state is projected to the
  one-source covariant representation.

The first acceptance test is equivalence with the previously independent C(K)
column on the frozen Gauss input.  The second applies the generalized operator
to a genuine source-J=1 state from C(V), requiring only J_out=0,1,2 as dictated
by a rank-(0+1) fundamental matrix operator.  No H_L coefficient is fitted.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_covariant_volume_leg_gate as CV
import peter_weyl_covariant_K_leg_gate as CK
import peter_weyl_lorentzian_K_block_gate as KG
import peter_weyl_covariant_composition_gate as COMP

TOL=1e-11


def apply_HE_complete_state_custom(state,source_v,Jmax2,charged_nodes):
    out={}; max_v=0.0; max_b=0.0
    for key,amp in state.items():
        part,vleak,bleak=CK.apply_HE_complete_key(
            key,source_v,Jmax2,charged_nodes=tuple(charged_nodes)
        )
        max_v=max(max_v,vleak); max_b=max(max_b,bleak)
        COMP.add(out,part,amp)
    return out,max_v,max_b


def apply_K_complete_custom(state,source_v,Jmax2,charged_nodes):
    HE,v1,b1=apply_HE_complete_state_custom(
        state,source_v,Jmax2,charged_nodes
    )
    VH=CK.apply_volume_complete_state(HE,source_v)
    Vstate=CK.apply_volume_complete_state(state,source_v)
    HV,v2,b2=apply_HE_complete_state_custom(
        Vstate,source_v,Jmax2,charged_nodes
    )
    out={}; COMP.add(out,VH,+1); COMP.add(out,HV,-1)
    return out,max(v1,v2),max(b1,b2)


def direct_K_covariant(state_cov,source_v,Jmax2):
    complete=COMP.covariant_to_complete(state_cov,source_v)
    K,vleak,bleak=apply_K_complete_custom(
        complete,source_v,Jmax2,(source_v,)
    )
    return COMP.complete_to_covariant(K,source_v),vleak,bleak


def C_K_component(state_cov,source_v,target_v,i,j,Jmax2):
    direct,v0,b0=direct_K_covariant(state_cov,source_v,Jmax2)
    hKh={}; max_outer=0.0; max_v=v0; max_b=b0
    for k in range(2):
        inv,oleak=COMP.inverse_complete(
            state_cov,source_v,target_v,k,j,Jmax2
        )
        max_outer=max(max_outer,oleak)
        Kinv,vleak,bleak=apply_K_complete_custom(
            inv,source_v,Jmax2,(source_v,target_v)
        )
        max_v=max(max_v,vleak); max_b=max(max_b,bleak)
        COMP.add(
            hKh,
            COMP.close_complete(Kinv,source_v,target_v,i,k,Jmax2)
        )
    out={}
    if i==j:
        COMP.add(out,direct,+1)
    COMP.add(out,hKh,-1)
    return out,{
        'outer_complete_basis_leakage':max_outer,
        'internal_volume_sector_leakage':max_v,
        'complete_charge_basis_leakage':max_b,
    }


def reference_CK_matrix(initial,source_v,target_v,Jmax2=5):
    Kgauss=KG.apply_K_local({initial:1+0j},source_v,Jmax2)
    Kcov=CV.gauss_to_covariant(Kgauss,source_v)
    C=[[{} for _ in range(2)] for _ in range(2)]
    diagmax={
        'outer_complete_basis_leakage':0.0,
        'outer_wrong_charge_fraction':0.0,
        'internal_volume_sector_leakage':0.0,
        'complete_charge_basis_leakage':0.0,
        'HE_wrong_charge_fraction':0.0,
        'K_wrong_charge_fraction':0.0,
    }
    for i in range(2):
        for j in range(2):
            hKh,diag,_=CK.covariant_K_leg(
                initial,source_v,target_v,i,j,Jmax2
            )
            for name in diagmax:
                diagmax[name]=max(diagmax[name],diag[name])
            out={}
            if i==j:
                COMP.add(out,Kcov,+1)
            COMP.add(out,hKh,-1)
            C[i][j]=out
    return C,diagmax


def combined_weight_by_J(matrix):
    out={}
    for row in matrix:
        for state in row:
            for key,amp in state.items():
                J2=key[2]
                out[J2]=out.get(J2,0.0)+abs(amp)**2
    return {str(J2/2):float(x) for J2,x in sorted(out.items())}


def matrix_norm(matrix):
    return math.sqrt(sum(COMP.norm2(s) for row in matrix for s in row))


def run(source_v=0,target_v=1):
    # The research branch uses the preregistered zero-aware Q-nullspace
    # convention.  Applying it here makes this file independently executable;
    # it does not alter any frozen H_E/C(K) threshold.
    import peter_weyl_zeroaware_volume_migration_experiment as ZVM
    ZVM.patch_and_clear()

    initial=PW.basis_full_jhalf()[0]
    gauss_cov=CV.gauss_to_covariant({initial:1+0j},source_v)
    ref,refdiag=reference_CK_matrix(initial,source_v,target_v,5)
    got=[[{} for _ in range(2)] for _ in range(2)]
    errors=[]; supports=[]
    maxdiag={
        'outer_complete_basis_leakage':0.0,
        'internal_volume_sector_leakage':0.0,
        'complete_charge_basis_leakage':0.0,
    }
    for i in range(2):
        for j in range(2):
            state,diag=C_K_component(
                gauss_cov,source_v,target_v,i,j,5
            )
            got[i][j]=state
            errors.append(COMP.relerr(state,ref[i][j]))
            supports.append((len(state),len(ref[i][j])))
            for name in maxdiag:
                maxdiag[name]=max(maxdiag[name],diag[name])

    # Obtain a real non-Gauss J=1 source from the independently existing C(V)
    # column, then act with C(K) along a different radial edge.  Jmax=7/2 is
    # the sufficient single-H_L wall from the hit-depth preregistration.
    CVref=COMP.reference_CV_matrix(initial,source_v,target_v,3)
    J1state,J1key,J1amp=COMP.choose_J1_basis_state(CVref)
    second_target=next(w for w in PW.NEIG[source_v] if w!=target_v)
    second=[[{} for _ in range(2)] for _ in range(2)]
    maxdiag2={name:0.0 for name in maxdiag}
    for i in range(2):
        for j in range(2):
            state,diag=C_K_component(
                J1state,source_v,second_target,i,j,7
            )
            second[i][j]=state
            for name in maxdiag2:
                maxdiag2[name]=max(maxdiag2[name],diag[name])
    weights=combined_weight_by_J(second)
    total=sum(weights.values())
    forbidden=sum(x for J,x in ((float(k),v) for k,v in weights.items()) if J>2.0+1e-15)
    scalar_relevant=sum(x for J,x in ((float(k),v) for k,v in weights.items()) if J in (0.0,1.0))
    second_norm=matrix_norm(second)
    max_spin=max((max(key[0]) for row in second for state in row for key in state),default=0)/2

    passed=(
        max(errors,default=0.0)<1e-9
        and all(a==b for a,b in supports)
        and max(maxdiag.values(),default=0.0)<1e-10
        and refdiag['outer_wrong_charge_fraction']<1e-18
        and refdiag['HE_wrong_charge_fraction']<1e-18
        and refdiag['K_wrong_charge_fraction']<1e-18
        and second_norm>1e-10
        and forbidden/max(total,1e-30)<1e-18
        and scalar_relevant>1e-14
        and max(maxdiag2.values(),default=0.0)<1e-10
        and max_spin<=3.5+1e-12
    )
    return {
        'status':'state-to-state composition gate for matrix-covariant C_e(K)',
        'passed':bool(passed),
        'reference_edge':[source_v,target_v],
        'gauss_column_component_relative_errors':errors,
        'gauss_column_component_support_pairs':supports,
        'generalized_gauss_diagnostics':maxdiag,
        'independent_reference_diagnostics':refdiag,
        'selected_J1_basis_key':repr(J1key),
        'selected_J1_reference_amplitude':[J1amp.real,J1amp.imag],
        'second_edge':[source_v,second_target],
        'second_CK_matrix_norm':second_norm,
        'second_CK_weight_by_source_J':weights,
        'second_CK_forbidden_J_gt_2_fraction':forbidden/max(total,1e-30),
        'second_CK_scalar_relevant_J01_weight':scalar_relevant,
        'second_CK_diagnostics':maxdiag2,
        'second_CK_max_spin_reached':max_spin,
        'selection_rule':'A rank-(0+1) 2x2 covariant operator acting on J=1 may populate J=0,1,2 but no J>2; future scalar H_L keeps only exact scalar-relevant J=0,1 paths.',
        'next_use':'Compose C(V) then C(K) then C(K) only through the five preregistered scalar rank paths and take the oriented trace at Jmax=7/2.',
        'scope_note':'Composition prerequisite only; no traced H_L amplitude or HDA closure is claimed here.'
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--v',type=int,default=0)
    ap.add_argument('--w',type=int,default=1)
    ap.add_argument('--output',type=Path)
    a=ap.parse_args(); out=run(a.v,a.w); text=json.dumps(out,indent=2); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
