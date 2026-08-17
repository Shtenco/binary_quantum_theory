#!/usr/bin/env python3
"""Symbolic positive control for soft-graviton universal coupling.

For elastic a+b->a+b scattering, momentum conservation reduces the soft
spin-2 gauge condition to (kappa_b-kappa_a)(p1-p3)=0.  Generic non-forward
scattering therefore enforces kappa_a=kappa_b.  The analogous soft-U1
condition is charge conservation and does not require equal species charges.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp

def run():
    ka,kb=sp.symbols('kappa_a kappa_b')
    # Use four independent symbolic components; p4 is eliminated by momentum conservation.
    p1=sp.Matrix(sp.symbols('p10:4')); p2=sp.Matrix(sp.symbols('p20:4')); p3=sp.Matrix(sp.symbols('p30:4')); p4=p1+p2-p3
    grav=sp.simplify(-ka*p1-kb*p2+ka*p3+kb*p4)
    target=sp.simplify((kb-ka)*(p1-p3))
    identity=(grav-target)==sp.zeros(4,1)
    # Generic component difference x != 0 gives ka=kb.
    x=sp.symbols('x', nonzero=True)
    sol=sp.solve(sp.Eq((kb-ka)*x,0),ka)
    qa,qb=sp.symbols('q_a q_b')
    photon=sp.simplify(-qa-qb+qa+qb)
    passed=bool(identity and sol==[kb] and photon==0)
    return {
      'status':'exact soft-graviton universal-coupling algebra control','passed':passed,
      'spin2_gauge_residual_after_momentum_conservation':[str(v) for v in grav],
      'factorized_target':[str(v) for v in target],
      'generic_nonforward_solution_for_kappa_a':str(sol[0]),
      'soft_U1_elastic_charge_residual':str(photon),
      'interpretation':'massless spin-2 soft gauge consistency enforces universal kappa, while spin-1 gauge consistency enforces charge conservation rather than equal charges',
      'scope':'two-species algebra illustration of the general Weinberg soft theorem; the candidate theory still has to realize the IR S-matrix assumptions'
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=Path('verification_results/SOFT_GRAVITON_UNIVERSAL_COUPLING.json')); a=ap.parse_args(); out=run(); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2)); return 0 if out['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
