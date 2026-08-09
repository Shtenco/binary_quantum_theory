#!/usr/bin/env python3
"""Refined path-position register -> continuum diffeomorphism Lie algebra.

A local path-rerouting qubit is the elementary carrier.  A refined coarse edge
has many neighboring microscopic route realizations |m>.  The unitary shift
S|m>=|m+1> gives the centered path derivative

    nabla = (S-S^dag)/(2a)

with symbol i sin(ka)/a.  For variable shift functions N,M define the scalar
Lie-derivative approximants D_N f=N nabla f.  The continuum target is

    [D_N,D_M] f = D_{N M' - M N'} f.

The script tests low Fourier modes on a periodic route-position register and
fits the finite-size defect exponent.
"""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import numpy as np


def defect(L:int)->float:
    x=2*np.pi*np.arange(L)/L
    a=2*np.pi/L
    def der(f):return (np.roll(f,-1)-np.roll(f,1))/(2*a)
    N=np.sin(x)+0.2*np.cos(2*x)
    M=np.cos(x)+0.15*np.sin(2*x)
    Np=np.cos(x)-0.4*np.sin(2*x)
    Mp=-np.sin(x)+0.3*np.cos(2*x)
    bracket=N*Mp-M*Np
    errs=[]
    for n in (1,2,3):
        f=np.exp(1j*n*x)+0.3*np.exp(-1j*(n+1)*x)
        lhs=N*der(M*der(f))-M*der(N*der(f))
        rhs=bracket*der(f)
        errs.append(float(np.linalg.norm(lhs-rhs)/np.linalg.norm(rhs)))
    return max(errs)

def run():
    sizes=np.array([24,32,48,64,96,128],float)
    errors=np.array([defect(int(L)) for L in sizes])
    p=-float(np.polyfit(np.log(sizes),np.log(errors),1)[0])

    # Separate exact shift unitarity / sine-symbol regression.
    max_unitarity=0.0;max_symbol=0.0
    for L in (16,31,64):
        S=np.zeros((L,L),complex)
        for m in range(L):S[(m+1)%L,m]=1
        max_unitarity=max(max_unitarity,float(np.linalg.norm(S.conj().T@S-np.eye(L))))
        a=2*np.pi/L
        D=(S-S.conj().T)/(2*a)
        for n in range(1,min(4,L//2)):
            f=np.exp(1j*n*2*np.pi*np.arange(L)/L)
            lam=np.vdot(f,D@f)/np.vdot(f,f)
            target=1j*math.sin(n*a)/a
            max_symbol=max(max_symbol,float(abs(lam-target)))

    passed=(max_unitarity<1e-12 and max_symbol<1e-12 and 1.8<p<2.1 and errors[-1]<0.02)
    return {
      'status':'refined path-register diffeomorphism Lie gate','passed':bool(passed),
      'sizes':sizes.astype(int).tolist(),'relative_defects':errors.tolist(),
      'fitted_decay_exponent':p,
      'max_shift_unitarity_error':max_unitarity,
      'max_sine_symbol_error':max_symbol,
      'exact_derivative_symbol':'i sin(k a)/a',
      'continuum_target':'[D_N,D_M] -> D_{N M_prime - M N_prime}',
      'scope_note':'One route coordinate / scalar test. A full 3D embedded-LQG construction needs the transverse path groupoid and coupling of its shift direction to the flux-derived beta field.'
    }

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);a=ap.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
