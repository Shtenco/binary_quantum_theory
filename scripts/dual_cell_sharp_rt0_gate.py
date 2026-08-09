#!/usr/bin/env python3
"""Generic tetrahedral dual-cell sharp map: dual 1-cochain -> RT0 vector field.

For a circumcentric dual in three dimensions a primal triangular face f is dual
to an orthogonal edge *f of length d_f.  The diagonal DEC Hodge map sends a
dual-edge 1-cochain omega_f to the primal face flux

    Phi_f = (A_f / d_f) omega_f.

On one tetrahedron arbitrary four face fluxes are represented exactly by the
lowest Raviart--Thomas field

    beta_T(x) = sum_i Phi_i (x-x_i) / (3 V_T),

where x_i is the vertex opposite face i.  For a constant vector beta and
omega_i=d_i n_i.beta this reconstruction is exact.

This script regression-tests those identities on random tetrahedra and checks
that circumcenters of adjacent tetrahedra differ orthogonally to their shared
face, as required by the circumcentric dual construction.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np


def tetra_geometry(X):
    A=np.column_stack([X[1]-X[0],X[2]-X[0],X[3]-X[0]])
    V=abs(float(np.linalg.det(A)))/6.0
    E=[]
    for i in range(4):
        ids=[j for j in range(4) if j!=i]
        a,b,c=X[ids]
        e=0.5*np.cross(b-a,c-a)
        if np.dot(e,X[i]-a)>0:e=-e
        E.append(e)
    E=np.asarray(E,float)
    return V,E,np.linalg.norm(E,axis=1)


def circumcenter(X):
    v0=X[0]
    M=2.0*(X[1:]-v0)
    b=np.sum(X[1:]**2,axis=1)-np.dot(v0,v0)
    return np.linalg.solve(M,b)


def run(seed=260809,samples=1000):
    rng=np.random.default_rng(seed)
    max_constant_reconstruction_error=0.0
    max_arbitrary_face_flux_error=0.0
    max_constant_flux_closure=0.0
    max_shared_face_tangent_fraction=0.0

    for _ in range(samples):
        while True:
            X=rng.normal(size=(4,3));V,E,A=tetra_geometry(X)
            if V>0.05 and np.min(A)>0.05:break
        n=E/A[:,None]

        # Constant vector field: the dual-edge integral is d_i n_i.beta.
        beta=rng.normal(size=3)
        d=np.exp(rng.normal(size=4))
        omega=d*(n@beta)
        Phi=(A/d)*omega
        x=rng.normal(size=3)
        reconstructed=sum(Phi[i]*(x-X[i]) for i in range(4))/(3.0*V)
        max_constant_reconstruction_error=max(
            max_constant_reconstruction_error,float(np.linalg.norm(reconstructed-beta)))
        max_constant_flux_closure=max(max_constant_flux_closure,float(abs(Phi.sum())))

        # Arbitrary face fluxes: RT0 reproduces each integrated normal flux.
        arbitrary=rng.normal(size=4)
        def rt0(xx):
            return sum(arbitrary[i]*(xx-X[i]) for i in range(4))/(3.0*V)
        for i in range(4):
            ids=[j for j in range(4) if j!=i]
            centroid=X[ids].mean(axis=0)
            observed=A[i]*float(n[i]@rt0(centroid))
            max_arbitrary_face_flux_error=max(
                max_arbitrary_face_flux_error,abs(observed-arbitrary[i]))

        # Independent adjacent-tetrahedron control for the circumcentric dual:
        # both circumcenters project to the circumcenter of the common face, so
        # their difference must have zero tangent component.
        while True:
            P=rng.normal(size=(3,3))
            normal=np.cross(P[1]-P[0],P[2]-P[0]);nn=np.linalg.norm(normal)
            if nn>0.1:break
        normal/=nn
        t1=rng.normal(size=3);t1-=np.dot(t1,normal)*normal
        t2=rng.normal(size=3);t2-=np.dot(t2,normal)*normal
        h1=float(np.exp(rng.normal()));h2=float(np.exp(rng.normal()))
        T1=np.vstack([P,P.mean(axis=0)+t1+h1*normal])
        T2=np.vstack([P,P.mean(axis=0)+t2-h2*normal])
        c1,c2=circumcenter(T1),circumcenter(T2);dc=c2-c1
        for tangent in (P[1]-P[0],P[2]-P[0]):
            frac=abs(float(dc@tangent))/max(np.linalg.norm(dc)*np.linalg.norm(tangent),1e-30)
            max_shared_face_tangent_fraction=max(max_shared_face_tangent_fraction,frac)

    passed=(max_constant_reconstruction_error<1e-11
            and max_arbitrary_face_flux_error<1e-11
            and max_constant_flux_closure<1e-11
            and max_shared_face_tangent_fraction<1e-11)
    return {
      'status':'generic dual-cell Hodge/RT0 sharp reconstruction','passed':bool(passed),
      'samples':samples,'seed':seed,
      'max_constant_vector_reconstruction_error':max_constant_reconstruction_error,
      'max_arbitrary_face_flux_reconstruction_error':max_arbitrary_face_flux_error,
      'max_constant_vector_face_flux_closure':max_constant_flux_closure,
      'max_adjacent_circumcenter_tangent_fraction':max_shared_face_tangent_fraction,
      'exact_map':'Phi_f=(A_f/d_f) omega_f; beta_T(x)=sum_f Phi_f (x-x_f)/(3 V_T)',
      'scope_note':'Circumcentric/diagonal-Hodge kinematic gate. Generic non-well-centered or barycentric/Galerkin dual choices require a non-diagonal Hodge operator and a separate universality test.'
    }

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--samples',type=int,default=1000);ap.add_argument('--seed',type=int,default=260809);ap.add_argument('--output',type=Path);a=ap.parse_args()
    out=run(a.seed,a.samples);txt=json.dumps(out,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
