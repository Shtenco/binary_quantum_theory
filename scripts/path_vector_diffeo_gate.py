#!/usr/bin/env python3
"""Two-dimensional transverse path register -> vector-field diffeomorphism algebra.

A coarse embedded edge in a 3D slice has two local transverse rerouting
directions.  On an LxL periodic route-position register use centered derivatives
and define

    D_beta f = beta^x d_x f + beta^y d_y f.

The continuum target is the Lie bracket of vector fields,

    [D_beta,D_gamma] = D_[beta,gamma].

This is a stronger version of the one-dimensional path-diffeomorphism gate.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np


def defect(L:int)->float:
    x=2*np.pi*np.arange(L)/L
    X,Y=np.meshgrid(x,x,indexing='ij')
    a=2*np.pi/L
    def dx(f):return (np.roll(f,-1,axis=0)-np.roll(f,1,axis=0))/(2*a)
    def dy(f):return (np.roll(f,-1,axis=1)-np.roll(f,1,axis=1))/(2*a)

    bx=np.sin(X)+0.2*np.cos(Y)
    by=0.3*np.cos(X)+0.25*np.sin(Y)
    gx=0.4*np.cos(X)+0.15*np.sin(Y)
    gy=np.sin(Y)+0.2*np.cos(X)

    dbx_dx=np.cos(X);dbx_dy=-0.2*np.sin(Y)
    dby_dx=-0.3*np.sin(X);dby_dy=0.25*np.cos(Y)
    dgx_dx=-0.4*np.sin(X);dgx_dy=0.15*np.cos(Y)
    dgy_dx=-0.2*np.sin(X);dgy_dy=np.cos(Y)

    bracket_x=bx*dgx_dx+by*dgx_dy-gx*dbx_dx-gy*dbx_dy
    bracket_y=bx*dgy_dx+by*dgy_dy-gx*dby_dx-gy*dby_dy

    def Db(f):return bx*dx(f)+by*dy(f)
    def Dg(f):return gx*dx(f)+gy*dy(f)

    tests=(
        np.exp(1j*(X+Y)),
        np.exp(1j*(2*X-Y))+0.2*np.exp(1j*Y),
        np.cos(X+2*Y)+0.3j*np.sin(2*X+Y),
    )
    errs=[]
    for f in tests:
        lhs=Db(Dg(f))-Dg(Db(f))
        rhs=bracket_x*dx(f)+bracket_y*dy(f)
        errs.append(float(np.linalg.norm(lhs-rhs)/np.linalg.norm(rhs)))
    return max(errs)


def run():
    sizes=np.array([24,32,48,64,96,128],float)
    errors=np.array([defect(int(L)) for L in sizes])
    p=-float(np.polyfit(np.log(sizes),np.log(errors),1)[0])
    passed=1.85<p<2.1 and errors[-1]<0.01
    return {
      'status':'2D transverse path-vector diffeomorphism Lie gate',
      'passed':bool(passed),
      'sizes':sizes.astype(int).tolist(),
      'relative_defects':errors.tolist(),
      'fitted_decay_exponent':p,
      'continuum_target':'[D_beta,D_gamma] -> D_{beta.grad gamma - gamma.grad beta}',
      'interpretation':'A refined two-direction route register supports the local non-Abelian vector-field algebra with approximately O(a^2) defect. This is diffeomorphism kinematics, not the Hamiltonian-constraint HDA by itself.'
    }

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);a=ap.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
