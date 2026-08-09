#!/usr/bin/env python3
"""Verify that the simplex tangential deformation vector is the face flux.

For an oriented spatial tetrahedron with barycentric coordinates lambda_l,
Bonzom--Dittrich's d=4 simplex-boundary normalization gives

    check N_l = 3 V grad(lambda_l),

whose magnitude is exactly the area of the face opposite vertex l.  Thus the
canonical face flux E_l can be identified with check N_l (up to one fixed
orientation convention), and the vertex-smooth diffeomorphism action is

    D(k,l) f = - E_l . d/dx_k f.

The script checks the exact geometric identities on random tetrahedra and
compares the differential action with centered finite differences on random
quadratic test functionals.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np


def run(seed:int=260809,samples:int=100,eps:float=1e-7):
    rng=np.random.default_rng(seed)
    max_area_rel=0.0;max_closure=0.0;max_der_rel=0.0
    for _ in range(samples):
        while True:
            A=rng.normal(size=(3,3))
            if np.linalg.det(A)<0:A[:,0]*=-1
            det=float(np.linalg.det(A))
            if det>0.25:break
        V=det/6.0
        inv=np.linalg.inv(A)
        grad_lambda=np.zeros((4,3))
        # x=A lambda, hence grad(lambda_i) is row i of A^{-1}.
        grad_lambda[1:]=inv
        grad_lambda[0]=-grad_lambda[1:].sum(axis=0)
        E=3.0*V*grad_lambda
        max_closure=max(max_closure,float(np.linalg.norm(E.sum(axis=0))))

        X=np.column_stack([np.zeros(3),A]).T
        for l in range(4):
            ids=[i for i in range(4) if i!=l]
            area=0.5*np.linalg.norm(np.cross(X[ids[1]]-X[ids[0]],
                                             X[ids[2]]-X[ids[0]]))
            max_area_rel=max(max_area_rel,float(abs(np.linalg.norm(E[l])-area)/area))

        c=rng.normal(size=(4,3))
        M=rng.normal(size=(4,3,3));M=0.5*(M+M.transpose(0,2,1))
        B=rng.normal(size=(4,4));B=0.5*(B+B.T)
        def f(xx):
            val=float(np.sum(c*xx))
            for i in range(4):val+=0.5*float(xx[i]@M[i]@xx[i])
            for i in range(4):
                for j in range(4):val+=0.25*B[i,j]*float(xx[i]@xx[j])
            return val
        grad=np.empty((4,3))
        for k in range(4):
            grad[k]=c[k]+M[k]@X[k]+0.5*sum(B[k,j]*X[j] for j in range(4))
        for k in range(4):
            for l in range(4):
                if k==l:continue
                disp=-E[l]
                analytic=float(disp@grad[k])
                xp=X.copy();xm=X.copy();xp[k]+=eps*disp;xm[k]-=eps*disp
                fd=(f(xp)-f(xm))/(2*eps)
                rel=abs(fd-analytic)/max(1.0,abs(fd),abs(analytic))
                max_der_rel=max(max_der_rel,float(rel))

    passed=max_area_rel<1e-12 and max_closure<1e-12 and max_der_rel<1e-6
    return {
      'status':'flux-to-vertex-smooth diffeomorphism bridge',
      'passed':bool(passed),'samples':samples,'seed':seed,'finite_difference_eps':eps,
      'max_relative_face_area_error':max_area_rel,
      'max_flux_closure_error':max_closure,
      'max_relative_directional_derivative_error':max_der_rel,
      'exact_identity':'E_l = 3 V grad(lambda_l); D(k,l) f = - E_l . partial_{x_k} f',
      'scope_note':'Classical relational/simplex bridge. It supplies the target D action for the quantum habitat test; it is not itself quantum HDA closure.'
    }

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--samples',type=int,default=100);ap.add_argument('--seed',type=int,default=260809);ap.add_argument('--output',type=Path);a=ap.parse_args()
    out=run(a.seed,a.samples);txt=json.dumps(out,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
