#!/usr/bin/env python3
"""Geometric hypersurface-deformation algebra on a 4-simplex boundary.

Implements the Bonzom--Dittrich simplex deformation fields directly in vertex
coordinates.  Vertex 0 is used to define the spatial tetrahedron sigma(0)
with vertices 1..4.

H(k): move vertex k along the outward unit normal of sigma(0).
D(k,l): move vertex k tangentially to sigma(0), normal to face sigma(0,l),
        with the normalization -3 V(0) grad(lambda_l).

The finite-difference commutator is tested against
 [H(k),H(k')] = [D(k',k)-D(k,k')]/[3 V(0)]
for random nondegenerate Euclidean 4-simplices.
"""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import numpy as np


def simplex_volume(points:np.ndarray)->float:
    base=points[1:]-points[0]
    gram=base@base.T
    return math.sqrt(max(float(np.linalg.det(gram)),0.0))/math.factorial(len(points)-1)


def spatial_normal(vertices:np.ndarray)->np.ndarray:
    pts=vertices[1:]
    edges=pts[1:]-pts[0]
    _,_,vh=np.linalg.svd(edges)
    n=vh[-1];n=n/np.linalg.norm(n)
    centroid=pts.mean(axis=0)
    # outward from the full simplex, i.e. away from vertex 0
    if np.dot(n,vertices[0]-centroid)>0:n=-n
    return n


def H_field(vertices:np.ndarray,k:int)->np.ndarray:
    out=np.zeros_like(vertices);out[k]=spatial_normal(vertices);return out


def barycentric_gradient(vertices:np.ndarray,l:int)->np.ndarray:
    """Gradient of lambda_l inside the affine span of spatial tetrahedron 1..4."""
    pts=vertices[1:];edges=pts[1:]-pts[0]
    Q,_=np.linalg.qr(edges.T)  # 4x3 orthonormal tangent basis
    y=(pts-pts[0])@Q
    system=np.column_stack([y,np.ones(4)])
    target=np.zeros(4);target[l-1]=1.0
    coeff=np.linalg.solve(system,target)
    return Q@coeff[:3]


def D_field(vertices:np.ndarray,k:int,l:int)->np.ndarray:
    V0=simplex_volume(vertices[1:])
    out=np.zeros_like(vertices)
    out[k]=-3.0*V0*barycentric_gradient(vertices,l)
    return out


def HH_commutator(vertices:np.ndarray,k:int,kp:int,eps:float)->np.ndarray:
    X=H_field(vertices,k);Y=H_field(vertices,kp)
    DY=(H_field(vertices+eps*X,kp)-H_field(vertices-eps*X,kp))/(2*eps)
    DX=(H_field(vertices+eps*Y,k)-H_field(vertices-eps*Y,k))/(2*eps)
    return DY-DX


def one(vertices:np.ndarray,k:int,kp:int,eps:float)->dict:
    V0=simplex_volume(vertices[1:])
    lhs=HH_commutator(vertices,k,kp,eps)
    rhs=(D_field(vertices,kp,k)-D_field(vertices,k,kp))/(3.0*V0)
    defect=float(np.linalg.norm(lhs-rhs)/(np.linalg.norm(lhs)+np.linalg.norm(rhs)+1e-30))
    return {'k':k,'kp':kp,'spatial_tetra_volume':V0,'lhs_norm':float(np.linalg.norm(lhs)),'rhs_norm':float(np.linalg.norm(rhs)),'relative_defect':defect}


def random_simplex(seed:int)->np.ndarray:
    rng=np.random.default_rng(seed)
    for _ in range(1000):
        v=rng.normal(size=(5,4))
        if simplex_volume(v[1:])>0.03 and simplex_volume(v)>0.005:return v
    raise RuntimeError('failed to draw nondegenerate simplex')


def run(samples:int=20,eps:float=3e-6)->dict:
    rows=[]
    for s in range(samples):
        v=random_simplex(1000+s)
        for k in range(1,5):
            for kp in range(k+1,5):rows.append(one(v,k,kp,eps))
    defects=np.array([r['relative_defect'] for r in rows])
    passed=bool(defects.max()<1e-8)
    return {
      'status':'geometric 4-simplex HDA boundary regression','passed':passed,
      'samples':samples,'pairs_per_simplex':6,'finite_difference_step':eps,
      'identity':'[H(k),H(kp)]=(D(kp,k)-D(k,kp))/(3 V_tet)',
      'max_relative_defect':float(defects.max()),'median_relative_defect':float(np.median(defects)),'mean_relative_defect':float(defects.mean()),
      'rows':rows,
      'scope_note':'Classical flat-simplex deformation algebra benchmark. It does not prove the quantum-link constraint algebra or generic curved 4D diffeomorphism symmetry.'
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--samples',type=int,default=20);ap.add_argument('--eps',type=float,default=3e-6);ap.add_argument('--output',type=Path);a=ap.parse_args();o=run(a.samples,a.eps);t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
