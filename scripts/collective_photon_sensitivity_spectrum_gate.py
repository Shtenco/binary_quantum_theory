#!/usr/bin/env python3
"""Exact sensitivity spectrum of the measured five-channel BCQG photon response."""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import numpy as np
import sympy as sp

def run(evidence:Path,tol=1e-10):
    d=json.loads(evidence.read_text())
    R=np.asarray(d['balanced_photon_phase_response_per_kappa'],float)
    s3=sp.sqrt(3)
    X=sp.Matrix([
      [1/s3,0,0,0,0,-1/s3],
      [s3/4,1/(4*s3),0,0,-s3/4,-1/(4*s3)],
      [s3/4,0,1/(4*s3),-s3/4,0,-1/(4*s3)],
      [s3/4,0,-s3/4,1/(4*s3),0,-1/(4*s3)],
      [s3/4,-s3/4,0,0,1/(4*s3),-1/(4*s3)],
    ])
    Xn=np.array(X.evalf(),float)
    M=sp.simplify(X*X.T)
    ev=[sp.Rational(1,12),sp.Rational(1,3),sp.Rational(1,3),
        (sp.Integer(19)-sp.sqrt(265))/24,(sp.Integer(19)+sp.sqrt(265))/24]
    evn=np.sort(np.array([float(x.evalf()) for x in ev]))
    sv=np.sqrt(evn)[::-1]
    cond=math.sqrt(float(((sp.Integer(19)+sp.sqrt(265))/2).evalf()))
    measured=np.linalg.svd(R,compute_uv=False)
    null=np.linalg.svd(R)[2][-1];null/=np.mean(null)
    checks={
      'source_passed':bool(d.get('passed')),
      'measured_response_matches_closed_form':np.linalg.norm(R-Xn)<tol,
      'rank5':np.linalg.matrix_rank(R,tol=tol)==5,
      'uniform_null':np.linalg.norm(null-np.ones(6))<tol,
      'closed_form_singular_values_match':np.linalg.norm(measured-sv)<tol,
      'finite_tomography_condition_number':abs(np.linalg.cond(R)-cond)<tol,
    }
    return {
      'status':'exact BCQG five-channel photon sensitivity spectrum',
      'passed':bool(all(checks.values())),'checks':{k:bool(v) for k,v in checks.items()},
      'response_per_kappa_closed_form':[[str(sp.simplify(x)) for x in X.row(i)] for i in range(5)],
      'RRt_closed_form':[[str(sp.simplify(M[i,j])) for j in range(5)] for i in range(5)],
      'RRt_eigenvalues_closed_form':['1/12','1/3','1/3','(19-sqrt(265))/24','(19+sqrt(265))/24'],
      'singular_values_numeric_descending':measured.tolist(),
      'tomography_condition_number_closed_form':'sqrt((19+sqrt(265))/2)',
      'tomography_condition_number_numeric':float(np.linalg.cond(R)),
      'uniform_trace_null_vector':null.tolist(),
      'interpretation':'After the common trace mode is rejected, all five BCQG shape directions are optically observable with finite conditioning. The weakest-to-strongest phase sensitivity ratio is fixed by the closed-form condition number, independent of the unknown overall kappa.',
      'scale_note':'All singular values multiply kappa=k ell_*/2. The condition number and relative sensitivity spectrum are dimensionless and require no absolute length-scale setting.'
    }

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--evidence',type=Path,default=Path('verification_results/COLLECTIVE_L1_COARSE_FLUX_RESPONSE.json'))
    p.add_argument('--output',type=Path)
    a=p.parse_args();o=run(a.evidence);txt=json.dumps(o,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+'\n')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
