#!/usr/bin/env python3
"""Finite-dimensional control for the collective HDA structure-function reduction bound."""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np

def opnorm(A):return float(np.linalg.norm(A,2))
def run(seed=314159):
    rng=np.random.default_rng(seed)
    # Coarse shift space R^3 -> Hermitian operator space on a 4D retained block.
    Dc=[]
    for _ in range(3):
        X=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4));Dc.append((X+X.conj().T)/2)
    # L_D exact for Euclidean shift norm is the largest singular value of the
    # linear map gamma -> vec(sum gamma_i D_i).
    K=np.stack([x.reshape(-1) for x in Dc],axis=1)
    LD=float(np.linalg.svd(K,compute_uv=False)[0])
    omega=rng.normal(size=3);Qf=rng.normal(size=(3,3));Qf=(Qf+Qf.T)/2+3*np.eye(3)
    dQ=rng.normal(size=(3,3))*0.03;Qc=Qf-dQ
    beta_f=Qf@omega;beta_c=Qc@omega
    def D(beta):return sum(float(beta[i])*Dc[i] for i in range(3))
    # Add a small independent generator-intertwining defect E_D.
    X=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4));ED=(X+X.conj().T)/2*0.01
    Dproj=D(beta_f)+ED
    delta_str=opnorm(Dproj-D(beta_c));delta_D=opnorm(ED);delta_Q=opnorm(dQ);om=float(np.linalg.norm(omega))
    bound=delta_D+LD*delta_Q*om
    # Full HDA bound bookkeeping control.
    delta_micro=0.017;etaN=0.041;etaM=0.037;hbar=0.8
    direct_upper=delta_micro+2*etaN*etaM+hbar*delta_str
    reduced_upper=delta_micro+2*etaN*etaM+hbar*bound
    # Rank-three shift theorem on nondegenerate Qc.
    shift_rank=int(np.linalg.matrix_rank(Qc,tol=1e-12))
    checks={
      'coarse_metric_nondegenerate':shift_rank==3,
      'three_structure_shifts_independent':shift_rank==3,
      'direct_structure_defect_below_reduced_bound':delta_str<=bound*(1+1e-12)+1e-12,
      'full_direct_bound_below_reduced_bound':direct_upper<=reduced_upper*(1+1e-12)+1e-12,
      'finite_shift_operator_norm':np.isfinite(LD) and LD>0,
    }
    return {'status':'collective HDA structure-function reduction theorem control','passed':bool(all(checks.values())),
      'science_status':'CONDITIONAL_C3_REDUCTION_THEOREM','checks':checks,'seed':seed,
      'delta_str_direct':delta_str,'delta_D':delta_D,'L_D':LD,'delta_Q':delta_Q,'omega_norm':om,
      'delta_str_reduced_bound':bound,'delta_micro':delta_micro,'eta_N':etaN,'eta_M':etaM,'hbar':hbar,
      'HDA_direct_upper_control':direct_upper,'HDA_reduced_upper_control':reduced_upper,'structure_shift_rank':shift_rank,
      'formula':'Delta_HH <= delta_micro + 2 eta_N eta_M + hbar*(delta_D + L_D delta_Q ||omega||)',
      'science_guard':'PASS certifies the norm implication only. Production C3 must measure every defect from corrected BCQG operators and retain the direct collective bracket as a held-out check.'}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
