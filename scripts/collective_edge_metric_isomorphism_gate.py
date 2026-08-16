#!/usr/bin/env python3
"""Exact geometric isomorphism from six tetrahedral edge channels to Sym^2(R^3).

The strict-interior L1 boundary theorem produces six target-independent coarse
channels labelled by the six edges of a regular coarse tetrahedron.  This gate
asks a purely geometric question: do infinitesimal squared-edge-length changes
provide complete coordinates on a symmetric 3x3 metric perturbation?

For a regular side-one tetrahedron with edge vectors d_e,

    delta l_e^2 = d_e^T (delta g) d_e.

Use the orthonormal symmetric-tensor coordinate basis

    xx, yy, zz, sqrt(2)xy, sqrt(2)xz, sqrt(2)yz.

The resulting 6x6 Jacobian is evaluated symbolically.  No Hamiltonian, HDA,
DeWitt coefficient, GR mode count or fitted target enters this map.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import sympy as sp


def run():
    q=sp.Rational
    s=sp.sqrt
    vertices=(
        sp.Matrix([0,0,0]),
        sp.Matrix([1,0,0]),
        sp.Matrix([q(1,2),s(3)/2,0]),
        sp.Matrix([q(1,2),1/(2*s(3)),s(q(2,3))]),
    )
    edges=[];rows=[]
    for i in range(4):
        for j in range(i+1,4):
            d=sp.simplify(vertices[j]-vertices[i]);x,y,z=d
            edges.append((i,j,d))
            rows.append([x*x,y*y,z*z,s(2)*x*y,s(2)*x*z,s(2)*y*z])
    J=sp.Matrix(rows)
    det=sp.simplify(J.det())
    rank=J.rank()
    dyad=sum((d*d.T for _,_,d in edges),sp.zeros(3))
    uniform=sp.simplify(J.inv()*sp.ones(6,1))
    edge_sum_metric=sp.simplify(sp.ones(1,6)*J)
    JTJ=sp.simplify(J.T*J)
    eig={str(sp.simplify(k)):int(v) for k,v in JTJ.eigenvals().items()}
    checks={
        'six_edges':len(edges)==6,
        'all_side_lengths_one':all(sp.simplify((d.T*d)[0]-1)==0 for _,_,d in edges),
        'Jacobian_rank_6':rank==6,
        'Jacobian_det_minus_sqrt2_over2':sp.simplify(det+s(2)/2)==0,
        'edge_dyad_tight_frame_2I':sp.simplify(dyad-2*sp.eye(3))==sp.zeros(3),
        'uniform_edge_mode_maps_to_identity_metric':uniform==sp.Matrix([1,1,1,0,0,0]),
        'edge_sum_is_twice_metric_trace':edge_sum_metric==sp.Matrix([[2,2,2,0,0,0]]),
        'JTJ_spectrum':eig=={'2':1,'1':3,'1/2':2},
    }
    return {
        'status':'exact six-edge / symmetric-metric tangent isomorphism on the regular tetrahedron',
        'passed':bool(all(checks.values())),
        'checks':checks,
        'edge_order':[[i,j] for i,j,_ in edges],
        'metric_coordinate_basis':['xx','yy','zz','sqrt(2)xy','sqrt(2)xz','sqrt(2)yz'],
        'Jacobian_exact':[[str(sp.simplify(x)) for x in J.row(i)] for i in range(6)],
        'Jacobian_determinant_exact':str(det),
        'Jacobian_rank':rank,
        'JTJ_eigenvalues':eig,
        'sum_edge_dyads_exact':[[str(x) for x in dyad.row(i)] for i in range(3)],
        'uniform_edge_mode_metric_coordinates':[str(x) for x in uniform],
        'edge_sum_metric_functional':[str(x) for x in edge_sum_metric],
        'trace_shape_identity':'sum_e delta(l_e^2) = 2 tr(delta g); therefore the five-dimensional zero-sum edge subspace maps exactly to traceless Sym^2(R^3)',
        'interpretation':'The six coarse-edge channels obtained dynamically at L1 are geometrically complete coordinates on the local symmetric metric tangent. Their 1+5 uniform/shape split is exactly the trace/traceless split for a regular tetrahedral background.',
        'scope_note':'Pure kinematic geometry only. This does not determine the kinetic supermetric, DeWitt coefficient, Hamiltonian normalization, physical mode count or HDA closure.'
    }


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();txt=json.dumps(o,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1

if __name__=='__main__':raise SystemExit(main())
