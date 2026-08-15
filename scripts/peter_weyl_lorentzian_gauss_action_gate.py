#!/usr/bin/env python3
"""General Gauss-basis action of the full epsilon-oriented sine Lorentzian node.

This module is the bridge from the already validated covariant K-K-V engine to
a reusable state-to-state operator on the ordinary Gauss spin-network basis.
It does not reimplement Lorentzian physics.  It reuses exactly

    peter_weyl_lorentzian_logical_projection_gate.epsilon_sum_state

which is the 24-term oriented sum built from

    Tr_aux[C_a(K_sine) C_b(K_sine) C_c(V)],
    K_sine=[V,H_E^sine].

The new ingredient is only the exact scalar closure

    (spins,K_other,J=0,M=0,K12=K34)
       -> (spins,K_all)

without imposing all-j=1/2 or K in {0,2}.  This makes the same raw Lorentzian
operator available on spin-changed states produced by H_E and, at a larger
cutoff, by H_L itself.

The gate checks:
1. exact agreement with the older logical projection on their common domain;
2. scalar closure and production-basis validity;
3. round-trip closure on a genuine H_E^sine-reached higher-spin Gauss key;
4. finite physical leakage of the reused 24-term Lorentzian stack.

No beta, kappa, hbar, final real sign, or HDA fit is introduced here.
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
import peter_weyl_euclidean_sine_ordering_gate as SINE
import peter_weyl_lorentzian_logical_projection_gate as LP
import peter_weyl_covariant_volume_leg_gate as CV

TOL=1e-11
JMAX2_SINGLE=7


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


def covariant_scalar_to_gauss_key(key,source_v):
    """Return the ordinary Gauss key for a scalar covariant key, else None."""
    spins,Kother,J2,M2,K12,K34=key
    if J2!=0 or M2!=0 or K12!=K34:
        return None
    Ks=list(Kother)
    if len(Ks)!=len(PW.VERT):
        return None
    Ks[source_v]=K12
    Ks=tuple(Ks)

    # Validate every local intertwiner against the actual spin configuration.
    for v in PW.VERT:
        allowed=PW.allowed_k2_t(*PW.local_spins(spins,v))
        if Ks[v] not in allowed:
            return None
    return (tuple(spins),Ks)


def project_scalar_gauss(state,source_v,tol=TOL):
    out={}
    rejected2=0.0
    accepted2=0.0
    for key,amp in state.items():
        g=covariant_scalar_to_gauss_key(key,source_v)
        if g is None:
            rejected2+=abs(amp)**2
            continue
        accepted2+=abs(amp)**2
        z=out.get(g,0j)+amp
        if abs(z)>tol:
            out[g]=z
        elif g in out:
            del out[g]
    return out,float(accepted2),float(rejected2)


def logical_subset(state):
    """Subset matching the historical all-j=1/2 logical projection domain."""
    out={}
    for key,amp in state.items():
        spins,Ks=key
        if tuple(spins)==(1,)*len(PW.EDGES) and all(k in (0,2) for k in Ks):
            out[key]=amp
    return out


def epsilon_raw_basis_installed(initial,source_v,jmax2=JMAX2_SINGLE):
    """Full raw 24-term node action; sine stack must already be installed."""
    old=LP.JMAX2
    LP.JMAX2=int(jmax2)
    try:
        covariant,rows,diag=LP.epsilon_sum_state(initial,source_v)
    finally:
        LP.JMAX2=old
    gauss,accepted2,rejected2=project_scalar_gauss(covariant,source_v)
    return gauss,covariant,rows,diag,accepted2,rejected2


def apply_L_raw_state_installed(state,source_v,jmax2=JMAX2_SINGLE,prune=TOL):
    """Linear raw L action while one shared sine Lorentzian cache is installed."""
    out={}
    max_diag={}
    rejected2=0.0
    input_rows=[]
    for key,amp0 in state.items():
        gauss,cov,rows,diag,accepted,rej=epsilon_raw_basis_installed(key,source_v,jmax2)
        add(out,gauss,amp0,tol=prune)
        rejected2+=abs(amp0)**2*rej
        for name,val in diag.items():
            if isinstance(val,(int,float)):
                max_diag[name]=max(max_diag.get(name,0.0),float(val))
        input_rows.append({
            'input_key':repr(key),
            'input_abs_amp':float(abs(amp0)),
            'covariant_support':len(cov),
            'gauss_support':len(gauss),
            'scalar_accepted_norm':math.sqrt(max(accepted,0.0)),
            'nonscalar_rejected_norm':math.sqrt(max(rej,0.0)),
            'oriented_terms':len(rows),
        })
    return {k:a for k,a in out.items() if abs(a)>prune},max_diag,rejected2,input_rows


def apply_L_raw_state(state,source_v,jmax2=JMAX2_SINGLE,prune=TOL):
    restore,caches=LP.install_sine_cached_stack()
    try:
        out,diag,rej,rows=apply_L_raw_state_installed(state,source_v,jmax2,prune)
        cache_info={
            name:{'hits':fn.cache_info().hits,'misses':fn.cache_info().misses,'currsize':fn.cache_info().currsize}
            for name,fn in caches.items()
        }
        return out,diag,rej,rows,cache_info
    finally:
        restore()


def run(source_v=0):
    initial=PW.basis_full_jhalf()[0]
    restore,caches=LP.install_sine_cached_stack()
    try:
        general,cov,rows,diag,accepted2,rejected2=epsilon_raw_basis_installed(
            initial,source_v,JMAX2_SINGLE
        )
        old_logical=LP.project_all_logical(cov,source_v)
        new_logical=logical_subset(general)
        logical_error=relerr(new_logical,old_logical)
        logical_support_equal=set(new_logical)==set(old_logical)

        # Cheap genuinely spin-changed round trip: take the largest physical
        # H_E^sine output key, embed it into the covariant scalar basis, and
        # verify the general closure maps every scalar component back to the
        # same Gauss key.  This tests the new nonlogical projection without
        # running another expensive H_L column.
        he=SINE.safe_H_sine({initial:1+0j},source_v,5)
        if not he:
            raise RuntimeError('H_E^sine unexpectedly empty')
        higher=max(he.items(),key=lambda kv:abs(kv[1]))[0]
        higher_is_spin_changed=tuple(higher[0])!=(1,)*len(PW.EDGES)
        cov_high=CV.gauss_to_covariant({higher:1+0j},source_v)
        high_back,high_acc,high_rej=project_scalar_gauss(cov_high,source_v)
        high_roundtrip_error=relerr(high_back,{higher:1+0j})

        scalar_fraction=accepted2/max(accepted2+rejected2,1e-30)
        max_physical=max(
            float(diag.get('CV_complete_basis_leakage',0.0)),
            float(diag.get('CK_outer_complete_basis_leakage',0.0)),
            float(diag.get('CK_internal_volume_sector_leakage',0.0)),
        )
        cache_info={
            name:{'hits':fn.cache_info().hits,'misses':fn.cache_info().misses,'currsize':fn.cache_info().currsize}
            for name,fn in caches.items()
        }

        checks={
            'raw_L_nonzero':len(general)>0 and norm2(general)>1e-20,
            'orientation_term_count_24':len(rows)==24,
            'logical_projection_support_exact':logical_support_equal,
            'logical_projection_amplitudes_exact':logical_error<1e-10,
            'scalar_closure_fraction':scalar_fraction>1-1e-10,
            'physical_stack_leakage':max_physical<1e-8,
            'HE_reached_key_spin_changed':higher_is_spin_changed,
            'higher_spin_covariant_roundtrip_support':set(high_back)=={higher},
            'higher_spin_covariant_roundtrip_amplitude':high_roundtrip_error<1e-10,
            'higher_spin_covariant_nonscalar_rejection':high_rej<1e-20,
        }
        return {
            'status':'general Gauss-basis action adapter for the full epsilon-oriented sine Lorentzian node',
            'passed':all(checks.values()),
            'source_node':source_v,
            'single_HL_Jmax':JMAX2_SINGLE/2,
            'input_key':repr(initial),
            'raw_gauss_support':len(general),
            'raw_gauss_norm':math.sqrt(norm2(general)),
            'covariant_support':len(cov),
            'scalar_closure_fraction':scalar_fraction,
            'nonscalar_rejected_norm':math.sqrt(max(rejected2,0.0)),
            'max_physical_basis_volume_leakage':max_physical,
            'historical_logical_support':len(old_logical),
            'general_logical_subset_support':len(new_logical),
            'logical_projection_relative_error':logical_error,
            'HE_sine_reached_higher_spin_key':repr(higher),
            'higher_spin_roundtrip_relative_error':high_roundtrip_error,
            'higher_spin_roundtrip_scalar_accepted_norm':math.sqrt(max(high_acc,0.0)),
            'higher_spin_roundtrip_nonscalar_rejected_norm':math.sqrt(max(high_rej,0.0)),
            'cache_info':cache_info,
            'checks':checks,
            'phase_note':'This returns L_raw. The canonical complex phase -i and the real Lorentzian coefficient are applied by a separate upstream normalization layer.',
            'next_use':'Use apply_L_raw_state_installed inside one shared-cache two-node H_E/H_L commutator, with the pair cutoff set by the independent hit-depth bound.',
            'scope':'State-to-state operator adapter only; not yet a two-node Lorentzian HDA closure result.',
        }
    finally:
        restore()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--node',type=int,default=0)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args(); out=run(args.node); text=json.dumps(out,indent=2,sort_keys=True); print(text)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
