#!/usr/bin/env python3
"""Executable q=2 -> Pancharatnam compact U(1) structural gate.

Checks on a deterministic closed loop of qubit rays:
- normalized-overlap links transform as U_vw -> exp[-i lambda_v] U_vw exp[i lambda_w];
- closed plaquette holonomy is invariant under arbitrary local representative phases;
- plaquette phase equals the Bargmann invariant phase;
- the continuum Hopf curvature integrates to first Chern number one.

This is a kinematic/gauge-topology gate, not a photon-dynamics or alpha gate.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import numpy as np

TOL=2e-12


def spinor(theta,phi):
    return np.array([np.cos(theta/2),np.exp(1j*phi)*np.sin(theta/2)],complex)


def link(a,b):
    z=np.vdot(a,b)
    if abs(z)<1e-12: raise ValueError('orthogonal neighboring rays have undefined Pancharatnam link')
    return z/abs(z)


def holonomy(states):
    z=1+0j
    for i in range(len(states)):
        z*=link(states[i],states[(i+1)%len(states)])
    return z/abs(z)


def run():
    # Generic nonorthogonal quadrilateral on CP1.
    params=[(.61,.15),(1.04,1.17),(1.31,2.44),(.88,4.71)]
    psi=[spinor(t,p) for t,p in params]
    phases=np.array([.37,-.82,1.41,2.03])
    gauged=[np.exp(1j*x)*v for x,v in zip(phases,psi)]

    U=np.array([link(psi[i],psi[(i+1)%4]) for i in range(4)])
    Ug=np.array([link(gauged[i],gauged[(i+1)%4]) for i in range(4)])
    predicted=np.array([np.exp(-1j*phases[i])*U[i]*np.exp(1j*phases[(i+1)%4]) for i in range(4)])
    link_cov=float(np.max(np.abs(Ug-predicted)))
    W=holonomy(psi); Wg=holonomy(gauged)
    hol_inv=float(abs(W-Wg))

    # Bargmann invariant is the product of raw overlaps; normalization removes only magnitude.
    B=1+0j
    for i in range(4): B*=np.vdot(psi[i],psi[(i+1)%4])
    barg=B/abs(B)
    barg_err=float(abs(W-barg))

    # Analytic Hopf curvature F=(1/2) sin(theta) dtheta^dphi.
    # Gauss-Legendre in theta and exact 2pi phi factor gives C1=1.
    x,w=np.polynomial.legendre.leggauss(64)
    theta=(x+1)*np.pi/2
    wt=w*np.pi/2
    integral=2*np.pi*np.sum(wt*.5*np.sin(theta))
    c1=float(integral/(2*np.pi))

    checks={
        'link_gauge_covariance':link_cov<TOL,
        'closed_holonomy_gauge_invariance':hol_inv<TOL,
        'holonomy_equals_normalized_Bargmann_invariant':barg_err<TOL,
        'first_Chern_number_one':abs(c1-1)<2e-14,
    }
    return {
        'status':'exact q=2 Pancharatnam/Hopf compact U1 structural gate',
        'passed':bool(all(checks.values())),
        'science_status':'KINEMATIC_COMPACT_U1_FROM_Q2_RAYS',
        'link_covariance_max_error':link_cov,
        'holonomy_gauge_invariance_error':hol_inv,
        'Bargmann_holonomy_error':barg_err,
        'plaquette_holonomy':[float(W.real),float(W.imag)],
        'plaquette_phase_rad':float(np.angle(W)),
        'first_Chern_number_numeric':c1,
        'checks':checks,
        'interpretation':'q=2 projective rays canonically define compact U1 Pancharatnam links and quantized Hopf curvature. A propagating photon still requires a deconfined Lorentzian Maxwell fixed point and a computed phase stiffness Z_A.',
    }


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1

if __name__=='__main__':raise SystemExit(main())
