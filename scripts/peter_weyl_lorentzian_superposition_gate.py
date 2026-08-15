#!/usr/bin/env python3
"""Exact Lorentzian ordered-triple action on an arbitrary Gauss superposition.

The production logical/full-state code historically exposed

    ordered_triple_state(initial_key,...)

which immediately wrapped one basis key as `{initial_key:1}`.  All subsequent
operations C(V), C(K_sine), C(K_sine) already act linearly on a sparse state
dictionary.  This module exposes that latent linear API directly:

    ordered_triple_state_from_gauss(gauss_state,...)

No operator algebra changes.  The exact source-J selection pruning and the same
physical-sine cached stack are reused.

This is the key runtime reduction for a second Lorentzian layer: L may be
applied term-by-term to the complete first-layer superposition rather than by
expanding into one expensive L column per intermediate Gauss basis key.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_covariant_volume_leg_gate as CV
import peter_weyl_lorentzian_logical_projection_gate as LP
import peter_weyl_lorentzian_ordered_triple_gate as RAW
import peter_weyl_lorentzian_gauss_action_gate as LGA

TOL=1e-10


def add(dst,src,scale=1.0,tol=TOL):
    for key,amp in src.items():
        z=dst.get(key,0j)+scale*amp
        if abs(z)>tol:
            dst[key]=z
        elif key in dst:
            del dst[key]


def norm2(state):
    return float(sum(abs(a)**2 for a in state.values()))


def relerr(a,b):
    keys=set(a)|set(b)
    num=math.sqrt(sum(abs(a.get(k,0j)-b.get(k,0j))**2 for k in keys))
    den=math.sqrt(norm2(b))
    return num/max(den,1e-30)


def update_diag(dst,name,value):
    dst[name]=max(dst.get(name,0.0),float(value))


def ordered_triple_covariant_from_gauss(gauss_state,source_v,a,b,c,jmax2):
    """Exact raw covariant Tr[C_a(K)C_b(K)C_c(V)] on a Gauss superposition.

    The sine stack must already be installed by LP.install_sine_cached_stack().
    """
    old=LP.JMAX2
    LP.JMAX2=int(jmax2)
    try:
        psi=CV.gauss_to_covariant(dict(gauss_state),source_v)
        total={}
        diag={
            'CV_complete_basis_leakage':0.0,
            'CK_outer_complete_basis_leakage':0.0,
            'CK_internal_volume_sector_leakage':0.0,
            'CK_complete_charge_basis_leakage':0.0,
        }
        for i,j,k in itertools.product(range(2),repeat=3):
            s1,leakV=RAW.COMP.C_volume_component(psi,source_v,c,k,i,int(jmax2))
            update_diag(diag,'CV_complete_basis_leakage',leakV)
            if not s1:
                continue
            s2,d2=RAW.KCOMP.C_K_component(s1,source_v,b,j,k,int(jmax2))
            for name,val in (
                ('CK_outer_complete_basis_leakage',d2['outer_complete_basis_leakage']),
                ('CK_internal_volume_sector_leakage',d2['internal_volume_sector_leakage']),
                ('CK_complete_charge_basis_leakage',d2['complete_charge_basis_leakage']),
            ):
                update_diag(diag,name,val)
            # Same exact scalar-channel selection rule used by production LP.
            # J labels are doubled: keep J=0,1; discard J>=2, which a final
            # rank-(0+1) C(K) cannot return to the scalar J=0 sector.
            s2={key:amp for key,amp in s2.items() if key[2] in (0,2)}
            if not s2:
                continue
            s3,d3=RAW.KCOMP.C_K_component(s2,source_v,a,i,j,int(jmax2))
            for name,val in (
                ('CK_outer_complete_basis_leakage',d3['outer_complete_basis_leakage']),
                ('CK_internal_volume_sector_leakage',d3['internal_volume_sector_leakage']),
                ('CK_complete_charge_basis_leakage',d3['complete_charge_basis_leakage']),
            ):
                update_diag(diag,name,val)
            add(total,s3,tol=TOL)
        return total,diag
    finally:
        LP.JMAX2=old


def ordered_triple_gauss_from_gauss(gauss_state,source_v,a,b,c,jmax2):
    cov,diag=ordered_triple_covariant_from_gauss(gauss_state,source_v,a,b,c,jmax2)
    gauss,accepted2,rejected2=LGA.project_scalar_gauss(cov,source_v,TOL)
    return gauss,diag,accepted2,rejected2


def epsilon_sum_gauss_from_gauss(gauss_state,source_v,jmax2):
    neighbors=PW.NEIG[source_v]
    total={}; rows=[]; diagmax={}; rejected2=0.0; accepted2=0.0
    for r,omit in enumerate(neighbors):
        base=tuple(x for x in neighbors if x!=omit)
        face=(-1)**r
        for perm in itertools.permutations(base):
            coef=face*LP.parity(base,perm)
            a,b,c=perm
            st,diag,acc,rej=ordered_triple_gauss_from_gauss(
                gauss_state,source_v,a,b,c,jmax2
            )
            add(total,st,coef,tol=TOL)
            accepted2+=acc; rejected2+=rej
            for name,val in diag.items():
                update_diag(diagmax,name,val)
            rows.append({'ordered_edges':[a,b,c],'coefficient':coef,'support':len(st),'norm':math.sqrt(norm2(st))})
    return total,rows,diagmax,accepted2,rejected2


def run_linearity_gate(jmax2=5):
    basis=PW.basis_full_jhalf()
    if len(basis)<2:
        raise RuntimeError('need at least two Gauss logical keys')
    k0,k1=basis[0],basis[1]
    alpha=0.37-0.21j
    source=0; a,b,c=2,3,4
    restore,caches=LP.install_sine_cached_stack()
    try:
        sup,diag_sup,acc_sup,rej_sup=ordered_triple_gauss_from_gauss(
            {k0:1+0j,k1:alpha},source,a,b,c,jmax2
        )
        s0,diag0,acc0,rej0=ordered_triple_gauss_from_gauss(
            {k0:1+0j},source,a,b,c,jmax2
        )
        s1,diag1,acc1,rej1=ordered_triple_gauss_from_gauss(
            {k1:1+0j},source,a,b,c,jmax2
        )
        linear={}; add(linear,s0,+1); add(linear,s1,alpha)
        err=relerr(sup,linear)
        support_equal=set(sup)==set(linear)
        max_physical=max(
            float(diag_sup.get('CV_complete_basis_leakage',0.0)),
            float(diag_sup.get('CK_outer_complete_basis_leakage',0.0)),
            float(diag_sup.get('CK_internal_volume_sector_leakage',0.0)),
        )
        cache_info={
            name:{'hits':fn.cache_info().hits,'misses':fn.cache_info().misses,'currsize':fn.cache_info().currsize}
            for name,fn in caches.items()
        }
        checks={
            'superposition_output_nonzero':len(sup)>0 and norm2(sup)>1e-20,
            'support_matches_sum_of_columns':support_equal,
            'amplitudes_linear':err<1e-9,
            'physical_basis_volume_leakage':max_physical<1e-8,
            'superposition_nonscalar_rejection':math.sqrt(max(rej_sup,0.0))<1e-8,
            'column_nonscalar_rejection':math.sqrt(max(rej0+rej1,0.0))<1e-8,
            'finite_norms':all(math.isfinite(x) for x in [math.sqrt(norm2(sup)),math.sqrt(norm2(linear))]),
        }
        return {
            'status':'exact Lorentzian ordered-triple superposition linearity gate',
            'passed':all(checks.values()),
            'source_node':source,
            'ordered_edges':[a,b,c],
            'Jmax':jmax2/2,
            'input_coefficients':{'basis0':[1.0,0.0],'basis1':[alpha.real,alpha.imag]},
            'superposition_support':len(sup),
            'column_sum_support':len(linear),
            'superposition_norm':math.sqrt(norm2(sup)),
            'column_sum_norm':math.sqrt(norm2(linear)),
            'relative_linearity_error':err,
            'max_physical_basis_volume_leakage':max_physical,
            'superposition_scalar_accepted_norm':math.sqrt(max(acc_sup,0.0)),
            'superposition_nonscalar_rejected_norm':math.sqrt(max(rej_sup,0.0)),
            'cache_info':cache_info,
            'checks':checks,
            'production_consequence':(
                'A second Lorentzian layer may apply each of the 24 ordered triples directly to the complete first-layer Gauss superposition. '
                'Sharding, if needed, is purely a linear resource partition and does not require one L column per intermediate basis key.'
            ),
            'scope':'Computational linearity/equivalence gate at a reduced safe cutoff; it is not an HDA result.',
        }
    finally:
        restore()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--jmax2',type=int,default=5)
    p.add_argument('--output',type=Path)
    a=p.parse_args(); out=run_linearity_gate(a.jmax2); text=json.dumps(out,indent=2,sort_keys=True); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
