#!/usr/bin/env python3
"""Hodge-weighted microscopic -> continuum mirror stiffness gate.

For a dimensionless staggered mirror order sigma on tetrahedral dual nodes, the
circumcentric DEC scalar Dirichlet energy is

    H_grad = Z_sigma/2 * sum_f (A_f/d_f) (sigma_L-sigma_R)^2.

Near a uniform staggered ordered state, a microscopic face coupling can be
written

    H_micro = 1/2 * sum_f J_f (sigma_L-sigma_R)^2 + const.

Coefficient matching therefore requires

    J_f = Z_sigma * A_f/d_f,
    Z_sigma = J_f * d_f/A_f.

This gate verifies the regular-tetrahedron closed form and a random shared-face
circumcentric geometry control. It also demonstrates that constant J_f on an
irregular mesh does not generally represent one metric-covariant continuum
Z_sigma; Hodge weighting or RG restoration is required.

Natural units hbar=c=1 are used for the final alpha formula.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def triangle_area(p0,p1,p2):
    return 0.5*np.linalg.norm(np.cross(p1-p0,p2-p0))


def circumcenter_tetra(P):
    p0=P[0]
    A=2.0*(P[1:]-p0)
    b=np.sum(P[1:]**2,axis=1)-np.sum(p0**2)
    return np.linalg.solve(A,b)


def regular_control(ell=1.0,J=1.0):
    # Equilateral shared face in z=0 and two regular tetrahedra on opposite sides.
    p0=np.array([0.0,0.0,0.0])
    p1=np.array([ell,0.0,0.0])
    p2=np.array([0.5*ell,math.sqrt(3)*ell/2,0.0])
    fc=(p0+p1+p2)/3
    h=math.sqrt(2/3)*ell
    p3=fc+np.array([0.0,0.0,h])
    p4=fc-np.array([0.0,0.0,h])
    c1=circumcenter_tetra(np.array([p0,p1,p2,p3]))
    c2=circumcenter_tetra(np.array([p0,p1,p2,p4]))
    A=triangle_area(p0,p1,p2)
    d=np.linalg.norm(c1-c2)
    Z=J*d/A
    A_exact=math.sqrt(3)*ell**2/4
    d_exact=ell/math.sqrt(6)
    Z_exact=(2*math.sqrt(2)/3)*(J/ell)
    return {
        "ell":ell,"J":J,"A_numeric":A,"A_exact":A_exact,
        "d_numeric":d,"d_exact":d_exact,
        "Z_numeric":Z,"Z_exact":Z_exact,
        "area_error":abs(A-A_exact),"dual_length_error":abs(d-d_exact),
        "Z_error":abs(Z-Z_exact),
    }


def random_pair_control(trials=256,seed=20260814,Z_target=1.7):
    rng=np.random.default_rng(seed)
    recovery=[]
    constant_J_Z=[]
    tangent=[]
    for _ in range(trials):
        # Random nondegenerate shared triangle.
        while True:
            F=rng.normal(size=(3,3))
            n=np.cross(F[1]-F[0],F[2]-F[0])
            nn=np.linalg.norm(n)
            if nn>0.25: break
        nhat=n/nn
        # Apex offsets on opposite sides plus arbitrary in-plane pieces.
        q3=F.mean(axis=0)+rng.normal(size=3)+nhat*(0.8+rng.random())
        q4=F.mean(axis=0)+rng.normal(size=3)-nhat*(0.8+rng.random())
        # Enforce opposite sides if random in-plane addition changed normal sign.
        plane0=F[0]
        if np.dot(q3-plane0,nhat)<=0: q3 += nhat*2.0
        if np.dot(q4-plane0,nhat)>=0: q4 -= nhat*2.0
        try:
            c1=circumcenter_tetra(np.vstack([F,q3]))
            c2=circumcenter_tetra(np.vstack([F,q4]))
        except np.linalg.LinAlgError:
            continue
        A=triangle_area(*F)
        dvec=c2-c1
        d=abs(np.dot(dvec,nhat))
        if d<1e-8: continue
        tang=np.linalg.norm(dvec-np.dot(dvec,nhat)*nhat)/np.linalg.norm(dvec)
        tangent.append(tang)
        Jf=Z_target*A/d
        recovery.append(Jf*d/A)
        constant_J_Z.append(d/A)  # J=1 negative control
    rec=np.asarray(recovery)
    cj=np.asarray(constant_J_Z)
    return {
        "trials_used":len(rec),
        "Z_target":Z_target,
        "max_Hodge_weighted_Z_recovery_error":float(np.max(abs(rec-Z_target))),
        "max_dual_tangent_fraction":float(np.max(tangent)),
        "constant_J_recovered_Z_mean":float(cj.mean()),
        "constant_J_recovered_Z_std":float(cj.std()),
        "constant_J_recovered_Z_CV":float(cj.std()/abs(cj.mean())),
    }


def run():
    regular=regular_control()
    random=random_pair_control()
    # Combine with alpha=beta^2/(4*pi*G*Z) in natural units.
    # For regular tetrahedra Z=(2 sqrt2/3) J/ell.
    alpha_prefactor=3.0/(8.0*math.sqrt(2)*math.pi)
    passed=(
        regular["area_error"]<1e-12
        and regular["dual_length_error"]<1e-12
        and regular["Z_error"]<1e-12
        and random["max_Hodge_weighted_Z_recovery_error"]<1e-10
        and random["max_dual_tangent_fraction"]<1e-10
        and random["constant_J_recovered_Z_CV"]>0.05
    )
    return {
        "status":"Hodge-weighted mirror stiffness matching gate",
        "passed":bool(passed),
        "DEC_energy":"H_grad=(Z_sigma/2) sum_f (A_f/d_f)(Delta sigma_f)^2",
        "microscopic_energy":"H_micro=(1/2) sum_f J_f(Delta sigma_f)^2+const",
        "matching":"J_f=Z_sigma*A_f/d_f; Z_sigma=J_f*d_f/A_f",
        "regular_tetrahedron":regular,
        "random_shared_face_control":random,
        "regular_closed_form":"Z_sigma=(2*sqrt(2)/3)*(J/ell)",
        "regular_alpha_natural_units":"alpha=(3*beta_m^2*ell)/(8*sqrt(2)*pi*G*J)",
        "alpha_dimensionless_prefactor_3_over_8sqrt2pi":alpha_prefactor,
        "interpretation":(
            "The geometry/Hodge data fix how a microscopic face coupling must scale to represent one continuum "
            "mirror stiffness. Constant J on a strongly irregular mesh gives a position-dependent effective Z; "
            "metric-covariant continuum dynamics requires Hodge-weighted J_f or an RG flow to the same form."
        ),
        "remaining_inputs":"Physical ell, J relative to Newton G, and matter source beta_m are still required for a numerical alpha."
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output",type=Path)
    a=ap.parse_args()
    out=run(); text=json.dumps(out,indent=2); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(text+"\n",encoding="utf-8")
    return 0 if out["passed"] else 1

if __name__=="__main__":
    raise SystemExit(main())
