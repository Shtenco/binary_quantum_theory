#!/usr/bin/env python3
"""Noncommutative index audit for the v1.2 Lorentzian adjoint ordering.

Treat C_a(K), C_b(K), C_c(V) as 2x2 auxiliary matrices whose entries are
noncommuting operators on a finite Hilbert space.  Construct K blocks globally
anti-Hermitian and V globally Hermitian, then verify

 [sum_ijk Ka_ij Kb_jk V_ki]^dag
   = sum_ijk V_ik Kb_kj Ka_ji

with no residual minus sign.  This is the exact index identity used by the PL
48-way worker; it does not test a GR target or a Lorentzian amplitude value.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np

def blocks(M,n):return [[M[i*n:(i+1)*n,j*n:(j+1)*n] for j in range(2)] for i in range(2)]
def run(seed=1729,n=5):
    rg=np.random.default_rng(seed)
    def rand():return rg.normal(size=(2*n,2*n))+1j*rg.normal(size=(2*n,2*n))
    Xa,Xb,Xv=rand(),rand(),rand()
    Ka=Xa-Xa.conj().T;Kb=Xb-Xb.conj().T;V=Xv+Xv.conj().T
    A,B,C=blocks(Ka,n),blocks(Kb,n),blocks(V,n)
    raw=np.zeros((n,n),complex);formula=np.zeros_like(raw);wrong=np.zeros_like(raw)
    for i in range(2):
      for j in range(2):
        for k in range(2):
          raw+=A[i][j]@B[j][k]@C[k][i]
          formula+=C[i][k]@B[k][j]@A[j][i]
          wrong+=A[j][i]@B[k][j]@C[i][k]
    target=raw.conj().T
    scale=max(float(np.linalg.norm(target)),1e-30)
    defect=float(np.linalg.norm(formula-target)/scale)
    wrong_defect=float(np.linalg.norm(wrong-target)/scale)
    compK=max(float(np.linalg.norm(A[i][j].conj().T+A[j][i])) for i in range(2) for j in range(2))
    compB=max(float(np.linalg.norm(B[i][j].conj().T+B[j][i])) for i in range(2) for j in range(2))
    compV=max(float(np.linalg.norm(C[i][j].conj().T-C[j][i])) for i in range(2) for j in range(2))
    checks={'Ka_component_antihermiticity':compK<1e-13,'Kb_component_antihermiticity':compB<1e-13,
            'V_component_hermiticity':compV<1e-13,'adjoint_ordering_identity':defect<1e-13,
            'wrong_order_negative_control_rejected':wrong_defect>1e-3}
    return {'status':'noncommutative Lorentzian auxiliary-index adjoint identity','passed':bool(all(checks.values())),
            'seed':seed,'physical_operator_dimension':n,'checks':checks,'relative_identity_defect':defect,
            'wrong_order_relative_defect':wrong_defect,'max_Ka_component_defect':compK,
            'max_Kb_component_defect':compB,'max_V_component_defect':compV,
            'identity':'(sum_ijk Ka_ij Kb_jk V_ki)^dag = sum_ijk V_ik Kb_kj Ka_ji',
            'scope_note':'Algebra/index-order theorem regression. Peter-Weyl component adjointness and PL amplitudes are tested by their separate operator gates.'}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
