#!/usr/bin/env python3
"""Equivalence gate: sparse-Fourier operator-first route engine vs 48x48 FFT.

The sparse engine is intended only as an exact runtime reduction for the frozen
trigonometric lapse / plane-wave HDA probes.  This gate compares it against the
independently implemented exact two-node 4x4 FFT route gate before the sparse
engine is allowed into the full spin-changing G x R calculation.
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

import operator_first_two_node_route_hda_gate as GRID
import operator_route_sparse_fourier as SF

EPS=(0.25,0.125,0.0625,0.03125,0.015625)


def fit(vals):
    return float(np.polyfit(np.log(np.asarray(EPS)),np.log(np.asarray(vals)),1)[0])


def sparse_case(Q,epsilon,carrier=8):
    N,M=SF.frozen_lapses(epsilon)
    psi=SF.carrier_state(4,carrier,0)
    RR=SF.route_commutator(Q,N,M,psi,epsilon)
    D=SF.route_target(Q,N,M,psi,epsilon)
    defect=SF.relative_defect(RR,D,+1)
    residual=dict(RR); SF.add_mode_dict(residual,D,+1)
    return {
        'defect':defect,
        'psi_modes':len(psi),
        'RR_modes':len(RR),
        'D_modes':len(D),
        'residual_modes':len(residual),
    }


def run(L=48,carrier=8):
    _,_,Q=GRID.shared_flux_gram_operator()
    spinor=np.array([1,0,0,0],complex)
    rows=[]; sparse_vals=[]; grid_vals=[]
    for e in EPS:
        s=sparse_case(Q,e,carrier)
        g,mineig=GRID.one_case(Q,L,e,carrier,spinor)
        sparse_vals.append(s['defect']); grid_vals.append(g)
        rel=abs(s['defect']-g)/max(abs(g),1e-30)
        rows.append({
            'epsilon':e,
            'sparse_defect':s['defect'],
            'fft_defect':g,
            'relative_difference':rel,
            'sparse_RR_modes':s['RR_modes'],
            'sparse_D_modes':s['D_modes'],
            'sparse_residual_modes':s['residual_modes'],
            'fft_minimum_Qp_eigenvalue':mineig,
        })
    ps=fit(sparse_vals); pg=fit(grid_vals)
    max_rel=max(r['relative_difference'] for r in rows)
    checks={
        'all_defects_finite':all(math.isfinite(x) for x in sparse_vals+grid_vals),
        'sparse_fft_max_relative_difference':max_rel<1e-7,
        'sparse_exponent_near_one':0.99<ps<1.01,
        'fft_exponent_near_one':0.99<pg<1.01,
        'exponents_agree':abs(ps-pg)<1e-6,
        'sparse_support_is_small':max(r['sparse_residual_modes'] for r in rows)<100,
    }
    return {
        'status':'exact sparse-Fourier versus FFT operator-first two-node route equivalence',
        'passed':all(checks.values()),
        'L_fft':L,'carrier':carrier,'epsilon':list(EPS),
        'rows':rows,
        'sparse_epsilon_exponent':ps,
        'fft_epsilon_exponent':pg,
        'max_relative_defect_difference':max_rel,
        'checks':checks,
        'production_decision':'Sparse Fourier may replace the FFT grid only for the frozen finite-harmonic lapse / plane-wave probe family if this gate passes.',
        'scope':'Runtime equivalence, not new HDA evidence; physical HDA evidence remains the independent operator-first route gates.',
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--L',type=int,default=48)
    p.add_argument('--carrier',type=int,default=8)
    p.add_argument('--output',type=Path)
    a=p.parse_args(); out=run(a.L,a.carrier); text=json.dumps(out,indent=2,sort_keys=True); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
