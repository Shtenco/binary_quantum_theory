#!/usr/bin/env python3
"""Exact symbolic qubit QGT gate: Fubini-Study metric + Berry curvature."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp

def run():
    th,ph=sp.symbols('theta phi', real=True)
    psi=sp.Matrix([sp.cos(th/2),sp.exp(sp.I*ph)*sp.sin(th/2)])
    ds=[psi.diff(th),psi.diff(ph)]
    bra=lambda v: sp.conjugate(v.T)
    P=sp.eye(2)-psi*bra(psi)
    Q=sp.Matrix(2,2,lambda a,b:sp.simplify((bra(ds[a])*P*ds[b])[0]))
    g=Q.applyfunc(lambda z:sp.simplify(sp.re(z)))
    target=sp.diag(sp.Rational(1,4),sp.sin(th)**2/4)
    Ath=sp.simplify(-sp.I*(bra(psi)*ds[0])[0])
    Aph=sp.simplify(-sp.I*(bra(psi)*ds[1])[0])
    F=sp.simplify(sp.diff(Aph,th)-sp.diff(Ath,ph))
    chern=sp.simplify(sp.integrate(sp.integrate(F,(ph,0,2*sp.pi)),(th,0,sp.pi))/(2*sp.pi))
    qcurv=sp.simplify(2*sp.im(Q[0,1]))
    metric_ok=sp.simplify(g-target)==sp.zeros(2,2)
    magnitude_ok=sp.simplify(qcurv**2-sp.sin(th)**2/4)==0
    passed=bool(metric_ok and magnitude_ok and sp.simplify(F-sp.sin(th)/2)==0 and chern==1)
    return {'status':'exact q=2 quantum-geometric-tensor gate','passed':passed,'Q':[[str(Q[i,j]) for j in range(2)] for i in range(2)],'Fubini_Study_metric':[[str(g[i,j]) for j in range(2)] for i in range(2)],'Berry_connection_A_theta':str(Ath),'Berry_connection_A_phi':str(Aph),'Berry_curvature_F_theta_phi':str(F),'Chern_number':str(chern),'Q_imaginary_curvature_magnitude_relation':'|2 Im Q_theta_phi|=sin(theta)/2; sign depends on Q/A convention','scope':'projective qubit geometry only; does not identify Fubini-Study metric with spacetime metric or prove a Maxwell phase'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=Path('verification_results/Q2_QUANTUM_GEOMETRIC_TENSOR.json')); a=ap.parse_args(); out=run(); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2)); return 0 if out['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
