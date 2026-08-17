#!/usr/bin/env python3
"""Exact matrix gate for BLIND_6_TO_1_TO_0_OBSERVABLE_TEST.md."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp

def run():
    R=sp.Rational
    A=sp.Matrix([
      [R(1,6),0,0,0,0,0],
      [0,0,R(1,6),0,0,0],
      [R(5,96),R(1,48),0,R(1,96),R(1,24),R(1,96)],
      [0,0,R(1,24),R(1,48),0,0],
      [R(1,81),R(1,81),R(1,81),R(1,81),R(1,81),R(1,81)],
      [R(341,3750),R(16,1875),0,R(17,1875),R(2,75),R(17,1875)]
    ])
    viso=sp.Matrix([6,24,6,36,-9,18]); one=sp.ones(6,1); y=A*viso
    contrasts=sp.zeros(5,6)
    for i in range(5): contrasts[i,0]=-1; contrasts[i,i+1]=1
    rank=contrasts.rank(); null=contrasts.nullspace()
    passed=(y==one and rank==5 and len(null)==1 and null[0].cross(one) if False else True)
    # Directly verify the one-dimensional nullspace is span(1).
    null_is_one=(len(null)==1 and null[0][0]!=0 and sp.simplify(null[0]/null[0][0]-one)==sp.zeros(6,1))
    passed=bool(y==one and rank==5 and null_is_one)
    return {
      'status':'exact blind 6-to-1-to-0 observable hierarchy gate','passed':passed,
      'det_A':str(sp.factor(A.det())),
      'isotropic_wilson_vector':[str(x) for x in viso],
      'A_times_isotropic_vector':[str(x) for x in y],
      'contrast_rank':rank,
      'contrast_nullspace_dimension':len(null),
      'contrast_nullspace_generator':[str(x) for x in null[0]],
      'stage_6_to_1':'SO3 iff five preregistered observable contrasts vanish',
      'stage_1_to_0':'under local analytic Lorentz-invariant metric-only assumptions, the remaining common k4 massless-pole shift vanishes',
      'scope':'the second stage is conditional on the assumptions proved separately in TT_POLE_UNIVERSALITY_NO_GO.md'
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=Path('verification_results/BLIND_6_TO_1_TO_0.json')); a=ap.parse_args()
    out=run(); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2)); return 0 if out['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
