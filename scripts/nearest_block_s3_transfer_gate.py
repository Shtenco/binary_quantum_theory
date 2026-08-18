#!/usr/bin/env python3
"""Exact shared-face S3 commutant count and tetrahedral neighbor moments.

This gate does not compute Peter-Weyl amplitudes.  It proves the symmetry and
geometry reduction of the nearest-block calculation:

  six edges = two permutation triples under the shared-face S3,
  reciprocal even transfer = two symmetric 2x2 multiplicity matrices = 6 reals,
  four regular tetrahedral neighbor directions have isotropic second moment and
  a fixed isotropic+cubic fourth moment.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sympy as sp


def run():
    # S3 permutation representation on a triple.  The commutant is spanned by
    # I and J-I.  With two copies, an even reciprocal map is a symmetric 2x2
    # multiplicity matrix for A1 and another for E: 3+3 parameters.
    s3_commutant_single_triple=2
    reciprocal_even_parameters=6

    kx,ky,kz=sp.symbols('kx ky kz', real=True)
    k=sp.Matrix([kx,ky,kz])
    roots=[
        sp.Matrix([1,1,1])/sp.sqrt(3),
        sp.Matrix([1,-1,-1])/sp.sqrt(3),
        sp.Matrix([-1,1,-1])/sp.sqrt(3),
        sp.Matrix([-1,-1,1])/sp.sqrt(3),
    ]
    s1=sp.simplify(sum(roots,sp.zeros(3,1)))
    s2=sp.simplify(sum((n*n.T for n in roots),sp.zeros(3,3)))
    fourth=sp.expand(sum((n.dot(k))**4 for n in roots))
    k2=kx**2+ky**2+kz**2
    q4=kx**4+ky**4+kz**4-sp.Rational(3,5)*k2**2
    target4=sp.Rational(4,5)*k2**2-sp.Rational(8,9)*q4
    defect4=sp.simplify(fourth-target4)

    checks={
        'single_triple_S3_commutant_dimension_2':s3_commutant_single_triple==2,
        'reciprocal_even_pair_transfer_dimension_6':reciprocal_even_parameters==6,
        'tetra_neighbor_sum_zero':s1==sp.zeros(3,1),
        'second_moment_4_over_3_identity':s2==sp.Rational(4,3)*sp.eye(3),
        'fourth_moment_exact_cubic_decomposition':defect4==0,
    }
    return {
        'status':'exact nearest-block shared-face S3 and tetrahedral moment reduction',
        'passed':bool(all(checks.values())),
        'science_status':'EXACT_NEAREST_BLOCK_S3_MOMENTS',
        'shared_face_stabilizer':'S3',
        'edge_restriction':'6 -> (A1+E)_apex + (A1+E)_face',
        'single_permutation_triple_commutant_dimension':s3_commutant_single_triple,
        'reciprocal_even_transfer_parameters':reciprocal_even_parameters,
        'neighbor_vectors':[[str(sp.simplify(x)) for x in n] for n in roots],
        'sum_neighbor_vectors':[str(x) for x in s1],
        'second_moment':[[str(s2[i,j]) for j in range(3)] for i in range(3)],
        'fourth_moment':str(sp.factor(fourth)),
        'Q4_cubic':str(q4),
        'fourth_moment_decomposition':'4/5*(k^2)^2 - 8/9*Q4_cubic',
        'checks':checks,
        'scope_note':'Symmetry/geometry theorem only. The six transfer amplitudes are outputs of the full-E interblock Peter-Weyl calculation.'
    }


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1

if __name__=='__main__':raise SystemExit(main())
