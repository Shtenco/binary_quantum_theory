#!/usr/bin/env python3
"""Certificate for the unique minimal Hermitian projection used by BCQG v1.2."""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np

def herm(A): return (A+A.conj().T)/2
def anti(A): return (A-A.conj().T)/2

def run(seed=20260815,n=6):
    rng=np.random.default_rng(seed)
    A=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
    H=herm(A); K=anti(A)
    Z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); Q,R=np.linalg.qr(Z); ph=np.diag(R); ph=np.where(np.abs(ph)>0,ph/np.abs(ph),1); U=Q@np.diag(np.conj(ph))
    cov=np.linalg.norm(herm(U@A@U.conj().T)-U@H@U.conj().T)
    hs_cross=abs(np.vdot(H,K).real)
    X=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); X=herm(X)
    lhs=np.linalg.norm(A-(H+X))**2; rhs=np.linalg.norm(K)**2+np.linalg.norm(X)**2
    checks={
      'H_is_Hermitian':np.linalg.norm(H-H.conj().T)<1e-12,
      'K_is_antiHermitian':np.linalg.norm(K+K.conj().T)<1e-12,
      'unique_direct_sum_reconstruction':np.linalg.norm(A-H-K)<1e-12,
      'projection_idempotent':np.linalg.norm(herm(H)-H)<1e-12,
      'fixes_Hermitian_inputs':np.linalg.norm(herm(H)-H)<1e-12,
      'kills_antiHermitian_inputs':np.linalg.norm(herm(K))<1e-12,
      'unitary_covariance':cov<1e-12,
      'HS_real_orthogonality':hs_cross<1e-12,
      'closest_point_pythagoras':abs(lhs-rhs)<1e-10,
    }
    checks={k:bool(v) for k,v in checks.items()}
    return {
      'status':'unique linear Hermitian projection certificate','passed':all(checks.values()),
      'operator_identity':'Herm(A)=(A+A^dagger)/2; for A=-i L_raw this is S=-i/2(L_raw-L_raw^dagger)',
      'uniqueness_statement':'On a finite cutoff block, End(H)=Herm(H) direct_sum AntiHerm(H) as real Hilbert spaces. The projection with range Herm(H) and kernel AntiHerm(H) is unique; it is also the unique Hilbert-Schmidt closest Hermitian operator.',
      'unitary_covariance_defect':float(cov),'closest_point_identity_defect':float(abs(lhs-rhs)),
      'checks':checks,
      'scope':'This proves uniqueness of the minimal linear Hermitian projection of the already-defined raw operator. It does not prove uniqueness among all possible microscopic factor orderings used to define L_raw before projection.'
    }

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);a=p.parse_args();o=run();t=json.dumps(o,indent=2,sort_keys=True);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
