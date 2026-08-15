#!/usr/bin/env python3
"""Gate for generic operator-first route blocks on genuine H_E^sine outputs.

Checks two things independently:

1. on the all-j=1/2 initial sector, the generic block engine exactly reproduces
   the separately implemented 4x4 two-node Q_shared construction;
2. on several largest genuine spin-changed H_E^sine output sectors, the exact
   operator-first route commutator retains O(epsilon) HDA convergence without
   taking geometry expectations before the square root.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_euclidean_sine_ordering_gate as SINE
import peter_weyl_operator_route_block_engine as BLK
import operator_first_two_node_route_hda_gate as TWO
import operator_route_sparse_fourier as SF

EPS=(0.25,0.125,0.0625,0.03125,0.015625)
CARRIER=8


def fit(vals):
    return float(np.polyfit(np.log(np.asarray(EPS)),np.log(np.asarray(vals)),1)[0])


def route_case(key,epsilon,carrier=CARRIER):
    N,M=SF.frozen_lapses(epsilon)
    psi=BLK.carrier_global_state(key,carrier)
    RR=BLK.route_commutator_global(N,M,psi,epsilon)
    D=BLK.route_target_global(N,M,psi,epsilon)
    return BLK.relative_defect(RR,D,+1),len(RR),len(D)


def matrix_error(A,B):
    return max(float(np.linalg.norm(A[a][b]-B[a][b])) for a in range(2) for b in range(2))


def run(n_sectors=5):
    initial=PW.basis_full_jhalf()[0]
    sec0=BLK.sector_id(initial)
    Qgeneric=BLK.shared_Q(sec0)
    _,_,Qind=TWO.shared_flux_gram_operator()
    initial_Q_error=matrix_error(Qgeneric,Qind)
    initial_basis=BLK.sector_basis(sec0)

    # Genuine physical-sine one-node output; P H_E P=0 guarantees nonzero
    # columns are spin/intertwiner changed rather than a trivial logical copy.
    he=SINE.safe_H_sine({initial:1+0j},0,5)
    ranked=sorted(he.items(),key=lambda kv:abs(kv[1]),reverse=True)
    selected=[]; seen=set()
    for key,amp in ranked:
        sec=BLK.sector_id(key)
        if sec in seen:
            continue
        seen.add(sec); selected.append((key,amp,sec))
        if len(selected)>=n_sectors:
            break

    sector_rows=[]
    all_endpoints=[]; all_exponents=[]; min_symbol=math.inf
    modes=[(CARRIER+i,CARRIER-1+j) for i in range(-2,3) for j in range(-2,3)]
    for key,amp,sec in selected:
        vals=[]; rr_support=[]; d_support=[]
        for e in EPS:
            d,nrr,nd=route_case(key,e)
            vals.append(d); rr_support.append(nrr); d_support.append(nd)
        p=fit(vals)
        mineig=BLK.sector_min_symbol_eigenvalue(sec,modes)
        min_symbol=min(min_symbol,mineig)
        basis=BLK.sector_basis(sec)
        row={
            'source_key':repr(key),
            'HE_source_abs_amplitude':float(abs(amp)),
            'spins2':list(key[0]),
            'source_Ks2':list(key[1]),
            'sector_dimension':len(basis),
            'allowed_sector_keys':[{'Ks2':list(k[1])} for k in basis],
            'defects':vals,
            'endpoint':vals[-1],
            'epsilon_exponent':p,
            'RR_geometry_support':rr_support,
            'D_geometry_support':d_support,
            'minimum_symbol_eigenvalue_on_checked_modes':mineig,
        }
        sector_rows.append(row); all_endpoints.append(vals[-1]); all_exponents.append(p)

    initial_vals=[route_case(initial,e)[0] for e in EPS]
    initial_p=fit(initial_vals)
    spin_changed=all(tuple(k[0])!=(1,)*len(PW.EDGES) for k,_,_ in selected)
    checks={
        'initial_generic_Q_matches_independent_4x4_Q':initial_Q_error<1e-12,
        'initial_sector_dimension_four':len(initial_basis)==4,
        'HE_output_nonzero':len(he)>0,
        'enough_distinct_spin_sectors':len(selected)==n_sectors,
        'selected_outputs_are_spin_changed':spin_changed,
        'all_checked_symbols_positive_semidefinite':min_symbol>-1e-8,
        'initial_route_exponent_near_one':0.99<initial_p<1.01,
        'higher_spin_route_exponents_near_one':min(all_exponents)>0.98 and max(all_exponents)<1.02,
        'higher_spin_endpoints_small':max(all_endpoints)<2e-5,
    }
    return {
        'status':'operator-first shared-route blocks on genuine spin-changed Peter-Weyl sectors',
        'passed':all(checks.values()),
        'route_nodes':[0,1],
        'local_route_legs':list(BLK.LOCAL_ROUTE_LEGS),
        'initial_sector_Q_error_vs_independent_4x4':initial_Q_error,
        'initial_sector_dimension':len(initial_basis),
        'initial_defects':initial_vals,
        'initial_epsilon_exponent':initial_p,
        'HE_sine_support':len(he),
        'checked_distinct_higher_spin_sectors':len(selected),
        'sector_rows':sector_rows,
        'minimum_symbol_eigenvalue':min_symbol,
        'checks':checks,
        'production_use':'This block completion is the route operator used on spin-changed G|psi> states in the full G x R_op cross commutator.',
        'scope':'Route-only HDA on selected genuine H_E-reached sectors; no Lorentzian amplitudes enter this gate.',
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--n-sectors',type=int,default=5)
    p.add_argument('--output',type=Path)
    a=p.parse_args(); out=run(a.n_sectors); text=json.dumps(out,indent=2,sort_keys=True); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
