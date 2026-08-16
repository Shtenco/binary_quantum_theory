#!/usr/bin/env python3
"""Exact S4 irrep spectrum of the measured BCQG q->metric calibration."""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import numpy as np
import sympy as sp

def run(evidence:Path,tol=1e-10):
    d=json.loads(evidence.read_text())
    Mnum=np.asarray(d['q_to_metric_h_map'],float)
    r12=1/sp.sqrt(12); r6=1/sp.sqrt(6)
    M=sp.Matrix([
      [r12,0,0,0,0,r12],
      [0,r12,0,0,r12,0],
      [0,0,r12,r12,0,0],
      [0,0,r6,-r6,0,0],
      [0,r6,0,0,-r6,0],
      [r6,0,0,0,0,-r6],
    ])
    O=sp.zeros(6)
    for a,b in ((0,5),(1,4),(2,3)):
        O[a,b]=O[b,a]=1
    Gram=sp.simplify(M.T*M)
    target=sp.Rational(1,4)*sp.eye(6)-sp.Rational(1,12)*O
    Pplus=(sp.eye(6)+O)/2   # A1 + E, dimensions 1+2
    Pminus=(sp.eye(6)-O)/2  # T2, dimension 3
    Mfloat=np.array(M.evalf(),float)
    checks={
      'source_passed':bool(d.get('passed')),
      'measured_map_matches_closed_form':np.linalg.norm(Mnum-Mfloat)<tol,
      'Gram_closed_form':Gram==target,
      'plus_projector_rank3':Pplus.rank()==3,
      'minus_projector_rank3':Pminus.rank()==3,
      'plus_scale_square_one_sixth':sp.simplify(Gram*Pplus-sp.Rational(1,6)*Pplus)==sp.zeros(6),
      'minus_scale_square_one_third':sp.simplify(Gram*Pminus-sp.Rational(1,3)*Pminus)==sp.zeros(6),
      'det_closed_form':sp.simplify(M.det()+sp.sqrt(2)/108)==0,
    }
    # If K_q respects S4 and is diagonal by irreps, K_h=M^-T K_q M^-1.
    # Therefore physical E=T2 isotropy requires kT2/(1/3)=kE/(1/6), i.e. kT2=2 kE.
    # DeWitt c=1/2 adds kA1/(1/6)=-1/2*kE/(1/6), hence kA1=-kE/2.
    return {
      'status':'exact S4 channel spectrum of BCQG coarse metric calibration',
      'passed':bool(all(checks.values())),'checks':{k:bool(v) for k,v in checks.items()},
      'q_to_metric_closed_form':[[str(sp.simplify(M[i,j])) for j in range(6)] for i in range(6)],
      'metric_calibration_Gram_formula':'M_hq^T M_hq = (1/4) I - (1/12) O_opposite',
      'det_M_hq':'-sqrt(2)/108',
      'S4_channel_scale_squared':{'A1':'1/6','E':'1/6','T2':'1/3'},
      'S4_channel_singular_scale':{'A1':'1/sqrt(6)','E':'1/sqrt(6)','T2':'1/sqrt(3)'},
      'condition_number':'sqrt(2)',
      'finite_metric_isotropy_raw_q_criterion':'lambda_T2_q = 2 lambda_E_q',
      'DeWitt_c_half_raw_q_blind_ratio':'lambda_A1_q : lambda_E_q : lambda_T2_q = -1/2 : 1 : 2',
      'interpretation':'The first finite coarse metric calibration is tetrahedrally equivariant but not orthonormal across irreps. Equal raw Hilbert-space E and T2 kinetic eigenvalues would create a false physical anisotropy. All universality tests must transform through the measured M_hq before comparing continuum metric eigenvalues.',
      'noncircularity_note':'The -1/2:1:2 ratio is an external blind discriminator implied by the independently measured metric calibration plus the GR/DeWitt target. It must never be inserted into the depth-two amplitude producer or used to select states/cutoffs.'
    }

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--evidence',type=Path,default=Path('verification_results/COLLECTIVE_L1_COARSE_FLUX_RESPONSE.json'))
    p.add_argument('--output',type=Path)
    a=p.parse_args();o=run(a.evidence);txt=json.dumps(o,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+'\n')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
