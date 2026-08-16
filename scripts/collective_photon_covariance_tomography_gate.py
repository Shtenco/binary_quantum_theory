#!/usr/bin/env python3
"""Exact five-channel photon covariance tomography theorem for the BCQG traceless metric carrier."""
from __future__ import annotations
import argparse,json
from pathlib import Path
import sympy as sp

def run():
    s2=sp.sqrt(2);J=sp.Matrix([[0,sp.Rational(1,2),sp.Rational(1,2),0,0,s2/2],[sp.Rational(1,2),0,sp.Rational(1,2),0,s2/2,0],[sp.Rational(1,2),sp.Rational(1,2),0,s2/2,0,0],[sp.Rational(1,2),sp.Rational(1,2),0,-s2/2,0,0],[sp.Rational(1,2),0,sp.Rational(1,2),0,-s2/2,0],[0,sp.Rational(1,2),sp.Rational(1,2),0,0,-s2/2]])
    D=sp.zeros(5,6)
    for i in range(5):D[i,i]=1;D[i,5]=-1
    T=sp.Matrix.hstack(sp.Matrix([1,-1,0,0,0,0])/sp.sqrt(2),sp.Matrix([1,1,-2,0,0,0])/sp.sqrt(6),sp.Matrix([0,0,0,1,0,0]),sp.Matrix([0,0,0,0,1,0]),sp.Matrix([0,0,0,0,0,1]))
    R=sp.simplify(D*J*T);G=sp.simplify(R.T*R);k=sp.symbols('kappa',nonzero=True,real=True)
    checks={'rank_5':R.rank()==5,'det_exact':sp.simplify(R.det()-sp.sqrt(6)/2)==0,'inverse_exact':sp.simplify(R.inv()*R)==sp.eye(5),'covariance_determinant_factor':sp.simplify(k**10*R.det()**2-sp.Rational(3,2)*k**10)==0}
    return {'status':'exact photon covariance tomography of BCQG traceless metric carrier','passed':all(checks.values()),'science_status':'STRUCTURAL_QUANTUM_OPTICAL_BRIDGE','det_R':str(sp.factor(R.det())),'rank_R':R.rank(),'R_Gram_eigenvalues':{str(sp.simplify(x)):int(v) for x,v in G.eigenvals().items()},'condition_number_squared_exact':'(11+sqrt(73))/2','covariance_map':'Sigma_phi=kappa^2 R Sigma_g R^T','inverse_map':'Sigma_g=kappa^-2 R^-1 Sigma_phi R^-T','det_covariance_map':'det(Sigma_phi)=(3/2) kappa^10 det(Sigma_g)','gaussian_visibility':'V=exp[-Var(Delta_phi)/2] for a zero-mean Gaussian commuting/semiclassical phase fluctuation','checks':checks,'scope_note':'Tomographic linear algebra only. Requires physical kappa=k ell_star/2, a derived BCQG metric correlator, and the eikonal/commuting Gaussian regime.'}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())