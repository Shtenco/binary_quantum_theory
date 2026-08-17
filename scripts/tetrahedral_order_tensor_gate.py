#!/usr/bin/env python3
"""Exact symbolic gate for the regular-tetrahedron l=4 order tensor."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp

def run():
    r=sp.sqrt(3)
    ns=[sp.Matrix(v)/r for v in ((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))]
    delta=lambda i,j: sp.Integer(1) if i==j else sp.Integer(0)
    second=sp.MutableDenseNDimArray.zeros(3,3)
    S=sp.MutableDenseNDimArray.zeros(3,3,3,3)
    U=sp.MutableDenseNDimArray.zeros(3,3,3,3)
    T=sp.MutableDenseNDimArray.zeros(3,3,3,3)
    for i in range(3):
      for j in range(3):
        second[i,j]=sp.simplify(sum(n[i]*n[j] for n in ns))
        for k in range(3):
          for l in range(3):
            S[i,j,k,l]=sp.simplify(sum(n[i]*n[j]*n[k]*n[l] for n in ns))
            U[i,j,k,l]=sp.Rational(1,3)*(delta(i,j)*delta(k,l)+delta(i,k)*delta(j,l)+delta(i,l)*delta(j,k))
            T[i,j,k,l]=sp.simplify(S[i,j,k,l]-sp.Rational(4,5)*U[i,j,k,l])
    second_err=max(abs(sp.simplify(second[i,j]-sp.Rational(4,3)*delta(i,j))) for i in range(3) for j in range(3))
    traces=[[sp.simplify(sum(T[i,i,k,l] for i in range(3))) for l in range(3)] for k in range(3)]
    x,y,z=sp.symbols('x y z', real=True); kv=(x,y,z)
    contract=sp.expand(sum(T[i,j,k,l]*kv[i]*kv[j]*kv[k]*kv[l] for i in range(3) for j in range(3) for k in range(3) for l in range(3)))
    k2=x*x+y*y+z*z
    q4=x**4+y**4+z**4-sp.Rational(3,5)*k2**2
    target=sp.expand(-sp.Rational(8,9)*q4)
    contraction_error=sp.simplify(contract-target)
    norm2=sp.simplify(sum(T[i,j,k,l]**2 for i in range(3) for j in range(3) for k in range(3) for l in range(3)))
    passed=(second_err==0 and all(v==0 for row in traces for v in row) and contraction_error==0)
    return {
      'status':'exact tetrahedral l=4 order-tensor gate','passed':bool(passed),
      'second_moment':[[str(second[i,j]) for j in range(3)] for i in range(3)],
      'trace_T_iikl':[[str(v) for v in row] for row in traces],
      'quartic_contraction':str(contract),
      'target_minus_8_over_9_Q4':str(target),
      'contraction_difference':str(contraction_error),
      'tensor_norm_squared':str(norm2),
      'interpretation':'T4 is the fully trace-free rank-four regular-tetrahedron order tensor; a physical nonzero expectation value can carry surviving tetrahedral orientation, while a regulator orientation alone cannot.'
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=Path('verification_results/TETRAHEDRAL_ORDER_TENSOR.json')); a=ap.parse_args()
    out=run(); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2)); return 0 if out['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
