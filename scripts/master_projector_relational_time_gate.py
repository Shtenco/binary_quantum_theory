#!/usr/bin/env python3
"""Exact symbolic/numeric control: master projector + clock conditioning = unitary evolution."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp

def run():
    T1,T2,T3=sp.symbols('T1 T2 T3', real=True)
    I2=sp.eye(2); H=sp.diag(0,1); P=sp.diag(0,-1)
    C=sp.kronecker_product(P,I2)+sp.kronecker_product(I2,H)
    M=C*C
    Pphys=sp.diag(1,0,0,1)
    # clock |T>=(|0>+exp(iT)|-1>)/sqrt2, because exp(-ipT) with p=-1.
    def clock(T): return sp.Matrix([1,sp.exp(sp.I*T)])/sp.sqrt(2)
    def cond(Tout,Tin):
        co=clock(Tout); ci=clock(Tin)
        # Partial clock matrix element, returning 2x2 system operator.
        K=sp.zeros(2,2)
        for po in range(2):
          for pi in range(2):
            coeff=sp.conjugate(co[po])*ci[pi]
            # block [po,pi] in clock-major ordering
            for a in range(2):
              for b in range(2): K[a,b]+=2*coeff*Pphys[2*po+a,2*pi+b]
        return sp.simplify(K)
    K21=cond(T2,T1); K32=cond(T3,T2); K31=cond(T3,T1)
    target=sp.diag(1,sp.exp(-sp.I*(T2-T1)))
    exact_kernel=sp.simplify(K21-target)==sp.zeros(2,2)
    comp=sp.simplify(K32*K21-K31)==sp.zeros(2,2)
    unit=sp.simplify(sp.conjugate(K21.T)*K21-sp.eye(2))==sp.zeros(2,2)
    kernel_ok=(C*Pphys)==sp.zeros(4,4)
    projector_ok=(Pphys*Pphys==Pphys and Pphys.T==Pphys)
    passed=bool(exact_kernel and comp and unit and kernel_ok and projector_ok)
    return {
      'status':'exact master-projector relational-time positive control','passed':passed,
      'constraint_matrix':[[str(x) for x in row] for row in C.tolist()],
      'master_matrix':[[str(x) for x in row] for row in M.tolist()],
      'physical_projector':[[str(x) for x in row] for row in Pphys.tolist()],
      'conditioned_kernel_T2_T1':[[str(x) for x in row] for row in K21.tolist()],
      'target_exp_minus_i_H_deltaT':[[str(x) for x in row] for row in target.tolist()],
      'C_Pphys_zero':bool(kernel_ok),'Pphys_idempotent_hermitian':bool(projector_ok),
      'conditioned_kernel_exact':bool(exact_kernel),'composition_exact':bool(comp),'unitarity_exact':bool(unit),
      'interpretation':'constraint spectral data become ordinary physical evolution only after conditioning the physical projector on relational clock boundary states',
      'scope':'solvable control model, not a derived gravity clock'
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=Path('verification_results/MASTER_PROJECTOR_RELATIONAL_TIME.json')); a=ap.parse_args()
    out=run(); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2)); return 0 if out['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
