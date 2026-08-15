#!/usr/bin/env python3
"""Exhaustive operator-first route HDA gate on every distinct H_E^sine-reached sector.

Unlike the historical top-N regression, this gate deduplicates the complete one-step
H_E^sine support by fixed-spin route sector and checks every sector. Numerical
zero-residual sectors are treated as exact/roundoff PASS instead of fitting log(0).
"""
from __future__ import annotations
import argparse, json, math, sys
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_euclidean_sine_ordering_gate as SINE
import peter_weyl_operator_route_block_engine as BLK
import operator_first_two_node_route_hda_gate as TWO
import operator_route_sparse_fourier as SF

EPS=(0.25,0.125,0.0625,0.03125,0.015625)
CARRIER=8
ZERO_TOL=5e-13

def route_case(key,epsilon,carrier=CARRIER):
    N,M=SF.frozen_lapses(epsilon)
    psi=BLK.carrier_global_state(key,carrier)
    RR=BLK.route_commutator_global(N,M,psi,epsilon)
    D=BLK.route_target_global(N,M,psi,epsilon)
    return BLK.relative_defect(RR,D,+1),len(RR),len(D)

def fit_or_zero(vals):
    arr=np.asarray(vals,float)
    if float(np.max(np.abs(arr))) <= ZERO_TOL:
        return None,'numerical_zero'
    if np.any(arr<=0):
        return None,'nonpositive_nonzero_defect'
    p=float(np.polyfit(np.log(np.asarray(EPS)),np.log(arr),1)[0])
    return p,'power_law'

def matrix_error(A,B):
    return max(float(np.linalg.norm(A[a][b]-B[a][b])) for a in range(2) for b in range(2))

def run():
    initial=PW.basis_full_jhalf()[0]
    sec0=BLK.sector_id(initial)
    Qgeneric=BLK.shared_Q(sec0)
    _,_,Qind=TWO.shared_flux_gram_operator()
    initial_Q_error=matrix_error(Qgeneric,Qind)

    he=SINE.safe_H_sine({initial:1+0j},0,5)
    ranked=sorted(he.items(),key=lambda kv:abs(kv[1]),reverse=True)
    selected=[]; seen=set()
    for key,amp in ranked:
        sec=BLK.sector_id(key)
        if sec in seen: continue
        seen.add(sec); selected.append((key,amp,sec))

    modes=[(CARRIER+i,CARRIER-1+j) for i in range(-2,3) for j in range(-2,3)]
    rows=[]; min_symbol=math.inf; nonzero_ps=[]; endpoints=[]; zero_count=0
    for key,amp,sec in selected:
        vals=[]; rr=[]; dd=[]
        for e in EPS:
            d,nr,nd=route_case(key,e)
            vals.append(float(d)); rr.append(nr); dd.append(nd)
        p,kind=fit_or_zero(vals)
        if kind=='numerical_zero': zero_count+=1
        elif p is not None: nonzero_ps.append(p)
        mineig=float(BLK.sector_min_symbol_eigenvalue(sec,modes)); min_symbol=min(min_symbol,mineig)
        endpoints.append(vals[-1])
        rows.append({
            'source_key':repr(key),'HE_source_abs_amplitude':float(abs(amp)),
            'spins2':list(key[0]),'source_Ks2':list(key[1]),
            'sector_dimension':len(BLK.sector_basis(sec)),
            'defects':vals,'endpoint':vals[-1],'fit_kind':kind,
            'epsilon_exponent':p,'RR_geometry_support':rr,'D_geometry_support':dd,
            'minimum_symbol_eigenvalue_on_checked_modes':mineig,
        })

    initial_vals=[float(route_case(initial,e)[0]) for e in EPS]
    initial_p=float(np.polyfit(np.log(np.asarray(EPS)),np.log(np.asarray(initial_vals)),1)[0])
    checks={
        'initial_generic_Q_matches_independent_4x4_Q':initial_Q_error<1e-12,
        'HE_output_nonzero':len(he)>0,
        'all_distinct_HE_sectors_checked':len(rows)==len(seen) and len(rows)>0,
        'all_outputs_spin_changed':all(tuple(k[0])!=(1,)*len(PW.EDGES) for k,_,_ in selected),
        'all_symbols_positive_semidefinite':min_symbol>-1e-8,
        'initial_route_exponent_near_one':0.99<initial_p<1.01,
        'all_nonzero_route_exponents_near_one':bool(nonzero_ps) and min(nonzero_ps)>0.98 and max(nonzero_ps)<1.02,
        'all_endpoints_small':max(endpoints)<2e-5,
        'zero_sectors_are_roundoff_small':all(max(r['defects'])<=ZERO_TOL for r in rows if r['fit_kind']=='numerical_zero'),
    }
    return {
        'status':'exhaustive operator-first route HDA on all distinct one-step H_E^sine-reached sectors',
        'passed':all(checks.values()),'HE_sine_support':len(he),
        'distinct_reached_sectors':len(rows),'numerical_zero_sectors':zero_count,
        'nonzero_powerlaw_sectors':len(nonzero_ps),'initial_Q_error':initial_Q_error,
        'initial_defects':initial_vals,'initial_epsilon_exponent':initial_p,
        'minimum_symbol_eigenvalue':min_symbol,
        'nonzero_exponent_min':min(nonzero_ps),'nonzero_exponent_max':max(nonzero_ps),
        'endpoint_max':max(endpoints),'endpoint_min':min(endpoints),
        'checks':checks,'sector_rows':rows,
        'scope':'Exhaustive over all distinct fixed-spin sectors in the one-step H_E^sine support of the frozen all-j=1/2 seed. It is not an exhaustive enumeration of all sectors reachable by the Lorentzian S operator.'
    }

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--output',type=Path)
    a=ap.parse_args(); out=run(); txt=json.dumps(out,indent=2,sort_keys=True); print(txt)
    if a.output: a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
