#!/usr/bin/env python3
"""Exact algebra gate for TT_POLE_UNIVERSALITY_NO_GO.md.

Checks:
1) a real symmetric 2x2 TT kernel commuting with the continuous polarization
   rotation generator is scalar;
2) a local Lorentz-invariant four-derivative TT kernel K=Z*s+a2*alpha*s^2
   leaves the perturbative massless branch s=0 unshifted at O(a2*k^4);
3) a preferred-foliation spatial term eta*a2*k^4 does produce such a shift,
   making the symmetry distinction explicit.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp

def run():
    a,b,d=sp.symbols('a b d', real=True)
    M=sp.Matrix([[a,b],[b,d]])
    J=sp.Matrix([[0,-1],[1,0]])
    comm=sp.expand(M*J-J*M)
    sol=sp.solve(list(comm),[b,d],dict=True)
    scalar_commutant=(sol==[{b:0,d:a}])

    Z,alpha,eta,A,k,delta=sp.symbols('Z alpha eta A k delta', nonzero=True)
    # Ansatz omega^2=k^2+delta*A*k^4, hence s=-delta*A*k^4.
    s=-delta*A*k**4
    K_lor=sp.expand(Z*s+alpha*A*s**2)
    coeff_lor=sp.expand(K_lor).coeff(A,1).coeff(k,4)
    delta_lor=sp.solve(sp.Eq(coeff_lor,0),delta)

    K_pref=sp.expand(Z*s+eta*A*k**4)
    coeff_pref=sp.expand(K_pref).coeff(A,1).coeff(k,4)
    delta_pref=sp.solve(sp.Eq(coeff_pref,0),delta)

    passed=bool(scalar_commutant and delta_lor==[0] and delta_pref==[eta/Z])
    return {
      'status':'exact algebra gate for TT pole universality hierarchy',
      'passed':passed,
      'little_group':{
        'symmetric_matrix':'[[a,b],[b,d]]',
        'rotation_generator':'[[0,-1],[1,0]]',
        'commutator':[[str(x) for x in row] for row in comm.tolist()],
        'solution':{'b':'0','d':'a'},
        'dimension_after_SO3':1
      },
      'lorentz_invariant':{
        's':'-omega^2+k^2',
        'kernel':'Z*s + alpha*A*s^2',
        'massless_shift_ansatz':'omega^2=k^2+delta*A*k^4',
        'O(A*k^4)_coefficient':str(coeff_lor),
        'solution_delta':0,
        'physical_k4_massless_pole_shift_dimension':0
      },
      'preferred_foliation_control':{
        'kernel':'Z*s + eta*A*k^4',
        'O(A*k^4)_coefficient':str(coeff_pref),
        'solution_delta':'eta/Z'
      },
      'hierarchy':'S4 quartic TT = 6 -> SO3 spatial = 1 -> local Lorentz metric-only massless k4 pole shift = 0',
      'scope':'local analytic parity-even quadratic TT sector around isotropic flat vacuum; extra fields/order parameters/nonlocality can evade the final zero-dimensional result'
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=Path('verification_results/TT_POLE_UNIVERSALITY_NO_GO.json')); a=ap.parse_args()
    out=run(); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps(out,indent=2)); return 0 if out['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
