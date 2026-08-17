#!/usr/bin/env python3
"""Executable controls for BCQG metric-regularity and gap-locality theorem.

This is theorem infrastructure, not production refinement data.
"""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]


def metric_control():
    src=json.loads((ROOT/'verification_results/COLLECTIVE_METRIC_CALIBRATION_IRREP.json').read_text(encoding='utf-8'))
    smin=1/math.sqrt(6);smax=1/math.sqrt(3)
    # deterministic perturbation with norm exactly smin/4
    rng=np.random.default_rng(271828)
    X=rng.normal(size=(6,6));u,s,v=np.linalg.svd(X,full_matrices=False)
    Delta=(smin/4)*(u@v)
    # Construct one reference map with the exact singular spectrum
    # [1/sqrt6]*3 + [1/sqrt3]*3. The theorem is basis-independent.
    Mref=np.diag([smin]*3+[smax]*3)
    M=Mref+Delta
    d=float(np.linalg.norm(Delta,2))
    sv=np.linalg.svd(M,compute_uv=False)
    lower=smin-d;upper=smax+d
    return {
      'source_passed':bool(src.get('passed')),
      'smin_ref':smin,'smax_ref':smax,'delta_norm':d,
      'theorem_lower_bound':lower,'actual_smin':float(sv.min()),
      'theorem_upper_bound':upper,'actual_smax':float(sv.max()),
      'condition_upper_bound':upper/lower,'actual_condition':float(sv.max()/sv.min()),
      'checks':{
        'delta_below_smin':bool(d<smin),
        'actual_smin_above_theorem_lower_bound':bool(float(sv.min())>=lower-1e-12),
        'actual_smax_below_theorem_upper_bound':bool(float(sv.max())<=upper+1e-12),
        'rank_six_preserved':bool(np.linalg.matrix_rank(M)==6),
      }
    }


def locality_control():
    # 1D block chain. D0=m I and nearest-neighbor T with ||D0^-1 T||<1.
    n=18;m=4.0;t=.45
    D0=m*np.eye(n)
    T=np.zeros((n,n))
    for i in range(n-1):T[i,i+1]=T[i+1,i]=t
    D=D0+T
    R=np.linalg.inv(D)
    A=np.linalg.solve(D0,T)
    r=float(np.linalg.norm(A,2));d0inv=float(np.linalg.norm(np.linalg.inv(D0),2))
    pref=d0inv/(1-r)
    worst_ratio=0.0;viol=0
    rows=[]
    for i in range(n):
      for j in range(n):
        dist=abs(i-j)
        bound=pref*(r**dist)
        val=abs(R[i,j])
        ratio=val/max(bound,1e-300)
        worst_ratio=max(worst_ratio,ratio)
        if val>bound+1e-12:viol+=1
        if i==0:rows.append({'distance':dist,'abs_resolvent':float(val),'bound':float(bound)})
    # Neumann partial sums converge to exact inverse.
    S=np.zeros_like(D);term=np.eye(n)
    D0inv=np.linalg.inv(D0)
    for k in range(120):
      if k==0:term=np.eye(n)
      elif k>0:term=term@(-A)
      S+=term@D0inv
    recon=float(np.linalg.norm(S-R,2)/np.linalg.norm(R,2))
    return {
      'dimension':n,'D0_mass':m,'nearest_neighbor_hopping':t,
      'r_norm_D0inv_T':r,'D0inv_norm':d0inv,
      'prefactor_bound':pref,'worst_actual_over_bound':worst_ratio,
      'bound_violations':viol,'neumann_inverse_relative_error_120_terms':recon,
      'rows_from_block0':rows,
      'checks':{
        'r_below_one':bool(r<1),
        'all_resolvent_elements_below_distance_bound':bool(viol==0),
        'neumann_series_reconstructs_inverse':bool(recon<1e-12),
      }
    }


def run():
    m=metric_control();l=locality_control()
    checks={
      'frozen_first_metric_calibration_passed':bool(m['source_passed']),
      'metric_perturbation_theorem_control':bool(all(m['checks'].values())),
      'finite_range_neumann_locality_control':bool(all(l['checks'].values())),
    }
    return {
      'status':'BCQG collective metric regularity and gap-locality theorem controls',
      'passed':bool(all(checks.values())),
      'science_status':'CONDITIONAL_METRIC_REGULARITY_LOCALITY_THEOREM',
      'checks':checks,'metric_control':m,'locality_control':l,
      'production_requirements':[
        'per-level dynamic metric defect ||M_dynamic-M_ref||_2 and reference singular bounds',
        'uniform positive lower metric singular bound',
        'classified/promoted low QCQ modes',
        'residual QCQ gap',
        'target-independent finite-range split D=D0+T with ||D0^-1 T||<1 when available'
      ],
      'theorem_file':'COLLECTIVE_METRIC_REGULARITY_LOCALITY_THEOREM.md'
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);a=ap.parse_args();o=run();t=json.dumps(o,indent=2,sort_keys=True);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
