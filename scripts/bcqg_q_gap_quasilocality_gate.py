#!/usr/bin/env python3
"""Executable certificate for the BCQG Q-gap -> quasi-local inverse theorem.

The gate checks the exact scalar identities in the proof and an independent
finite-range Hermitian matrix control.  It certifies the implication only; it
does not manufacture or assume a BCQG collective Q-gap.
"""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import numpy as np

def run():
    # Deterministic positive gapped nearest-neighbor control; the theorem itself
    # also covers indefinite self-adjoint A by applying the expansion to A^2.
    n=48
    A=np.diag(np.full(n,3.0))+np.diag(np.full(n-1,-0.45),1)+np.diag(np.full(n-1,-0.45),-1)
    ev=np.linalg.eigvalsh(A);delta=float(np.min(np.abs(ev)));M=float(np.max(np.abs(ev)))
    c=(M*M+delta*delta)/2.0;q=(M*M-delta*delta)/(M*M+delta*delta)
    D=np.eye(n)-(A@A)/c
    exact=np.linalg.inv(A)
    rows=[];prev=None;monotone=True;range_ok=True;bound_ok=True
    for N in (0,1,2,3,4,6,8,12):
        S=np.eye(n);term=np.eye(n)
        for _ in range(N):term=term@D;S+=term
        approx=(A@S)/c
        err=float(np.linalg.norm(exact-approx,2));bound=(M/(delta*delta))*(q**(N+1))
        if prev is not None:monotone &= err<=prev+1e-13
        prev=err;bound_ok &= err<=bound*(1+1e-10)+1e-13
        # A is range 1, so A D^N is exactly banded by 2N+1 up to roundoff.
        P=A@np.linalg.matrix_power(D,N)
        for i in range(n):
            for j in range(n):
                if abs(i-j)>2*N+1:range_ok &= abs(P[i,j])<1e-11
        rows.append({'N':N,'error_norm':err,'theorem_bound':bound,'range':2*N+1})
    # Off-diagonal inverse element must obey the tail bound with the largest N
    # whose polynomial range does not reach the chosen separation.
    spatial=[];spatial_ok=True
    for dist in (4,8,12,18,24,30):
        N=max(-1,(dist-2)//2)
        if N<0:continue
        bd=(M/(delta*delta))*(q**(N+1));amp=abs(exact[0,dist]);spatial_ok &= amp<=bd*(1+1e-10)+1e-13
        spatial.append({'distance':dist,'N':N,'inverse_element_abs':float(amp),'bound':float(bd)})
    checks={
      'positive_measured_gap_control':delta>0,
      'q_strictly_below_one':0<=q<1,
      'c_times_one_minus_q_equals_delta_squared':abs(c*(1-q)-delta*delta)<1e-12,
      'neumann_convergence_monotone':bool(monotone),
      'operator_error_below_exact_bound':bool(bound_ok),
      'finite_range_growth_exact':bool(range_ok),
      'spatial_inverse_elements_below_tail_bound':bool(spatial_ok),
    }
    return {'status':'Q-gap quasi-local Schur inverse theorem certificate','passed':bool(all(checks.values())),
      'science_status':'CONDITIONAL_Q_GAP_LOCALITY_THEOREM','checks':checks,
      'control':{'matrix_size':n,'interaction_range':1,'delta':delta,'M':M,'c':c,'q':q},
      'convergence_rows':rows,'spatial_rows':spatial,
      'bound':'||A^-1-A_N^-1|| <= (M/delta^2) q^(N+1), q=(M^2-delta^2)/(M^2+delta^2)',
      'science_guard':'PASS certifies the mathematical implication only. A direct BCQG collective producer must still measure inf_l delta_l>0 on every eliminated coupled Q-sector and promote any gapless coupled irrep into P.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
