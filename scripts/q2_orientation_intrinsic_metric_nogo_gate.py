#!/usr/bin/env python3
"""Exact q=2 no-go: geometry orientation Y is invisible to linear intrinsic metric sources.

The frozen q=2 tetrahedral metric reconstruction depends on the logical shape
coordinates X,Z but not on the orientation pseudoscalar Y.  The two regular
branches (X,Z,Y)=(0,0,+/-1) therefore have identical intrinsic metric and
identical metric Jacobian.

This gate combines that exact geometry fact with the relational Pauli source
algebra.  Even if X,Y,Z all exist as gauge-invariant relational observables,
the linear map from logical sources to intrinsic metric components has a zero Y
column.  Consequently the intrinsic metric connected response has rank two and
annihilates the orientation source exactly.

Therefore a physical Y_L x history-current coupling cannot be extracted as a
linear intrinsic-metric source coefficient.  It must, if physical, enter an
orientation-sensitive variable (triad/frame orientation, connection/extrinsic
curvature, parity-odd history structure) or nonlinear response.

This is a local intrinsic-metric no-go, not a statement that all physical
orientation observables vanish.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def zero(M: sp.Matrix) -> bool:
    return all(sp.simplify(sp.expand_complex(x)) == 0 for x in M)


def vec9(M: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([M[i,j] for i in range(3) for j in range(3)])


def run() -> dict[str, object]:
    x,z,y=sp.symbols('x z y', real=True)
    r2=sp.Rational(3,4)
    a=-sp.Rational(1,4)-z/2
    b=-sp.Rational(1,4)+z/4-sp.sqrt(3)*x/4
    c=-sp.Rational(1,4)+z/4+sp.sqrt(3)*x/4
    G=sp.Matrix([[r2,a,b],[a,r2,c],[b,c,r2]])

    # Exact reconstructed intrinsic edge metric. It is symbolically independent
    # of y before any expansion.
    detG=sp.factor(G.det())
    g=sp.simplify(2*sp.sqrt(detG)*G.inv())
    dgdy=sp.simplify(g.diff(y))

    g0=sp.simplify(g.subs({x:0,z:0}))
    MX=sp.simplify(g.diff(x).subs({x:0,z:0}))
    MZ=sp.simplify(g.diff(z).subs({x:0,z:0}))
    MY=sp.zeros(3)

    B3=vec9(MX).row_join(vec9(MY)).row_join(vec9(MZ)) # X,Y,Z logical sources
    gram=sp.simplify(B3.T*B3)

    # The relational maximally mixed Pauli positive control has unit covariance
    # in all three Pauli directions. Pushing it to intrinsic metric space still
    # removes Y because the geometry Jacobian has a null orientation column.
    Sigma_xyz=sp.eye(3)
    Cmetric=sp.simplify(B3*Sigma_xyz*B3.T)
    ey=sp.Matrix([0,1,0])

    # Reflection flips Y but leaves intrinsic metric unchanged.
    branch_plus=sp.simplify(g.subs({x:0,z:0,y:1}))
    branch_minus=sp.simplify(g.subs({x:0,z:0,y:-1}))

    # Intrinsic metric response to a pure Y logical perturbation vanishes.
    pure_y_metric=sp.simplify(B3*ey)
    logical_pullback=sp.simplify(B3.T*B3)

    checks={
        'intrinsic_metric_is_symbolically_independent_of_Y': zero(dgdy),
        'regular_Y_plus_minus_branches_have_identical_metric': zero(branch_plus-branch_minus),
        'orientation_metric_jacobian_column_is_zero': zero(MY),
        'full_XYZ_metric_jacobian_rank_is_2': int(B3.rank())==2,
        'pure_Y_source_maps_to_zero_intrinsic_metric': zero(pure_y_metric),
        'logical_metric_pullback_annihilates_Y': zero(logical_pullback*ey),
        'metric_connected_response_rank_remains_2_with_unit_XYZ_source_covariance': int(Cmetric.rank())==2,
    }

    expected_gram=sp.diag(sp.Rational(9,2),0,sp.Rational(9,2))
    checks['full_Frobenius_logical_metric_gram_is_diag_9over2_0_9over2']=zero(gram-expected_gram)

    gi=g0.inv()
    dewitt=sp.Matrix([
        [sp.trace(gi*MX*gi*MX),sp.trace(gi*MX*gi*MY),sp.trace(gi*MX*gi*MZ)],
        [sp.trace(gi*MY*gi*MX),sp.trace(gi*MY*gi*MY),sp.trace(gi*MY*gi*MZ)],
        [sp.trace(gi*MZ*gi*MX),sp.trace(gi*MZ*gi*MY),sp.trace(gi*MZ*gi*MZ)],
    ])
    expected_dewitt=sp.diag(sp.Rational(3,2),0,sp.Rational(3,2))
    checks['DeWitt_logical_metric_gram_is_diag_3over2_0_3over2']=zero(dewitt-expected_dewitt)

    passed=bool(all(checks.values()))
    return {
        'status':'exact q=2 orientation-to-intrinsic-metric linear-source no-go',
        'passed':passed,
        'checks':checks,
        'background_metric':[[str(v) for v in row] for row in g0.tolist()],
        'logical_metric_jacobian':{
            'M_X':[[str(v) for v in row] for row in MX.tolist()],
            'M_Y':[[str(v) for v in row] for row in MY.tolist()],
            'M_Z':[[str(v) for v in row] for row in MZ.tolist()],
            'rank_XYZ':int(B3.rank()),
            'Frobenius_gram_XYZ':[[str(v) for v in row] for row in gram.tolist()],
            'DeWitt_gram_XYZ':[[str(v) for v in row] for row in dewitt.tolist()],
        },
        'exact_nogo':(
            'The q=2 orientation pseudoscalar Y_L is absent from the intrinsic tetrahedral metric map at fixed face-spin norm. Hence any linear intrinsic-metric source construction, including the projected relational metric Hessian, has an exact Y null direction.'
        ),
        'consequence_for_g_YC':(
            'A nonzero physical coupling involving Y_L and a history current cannot be identified with a linear intrinsic-metric Gamma^(2) coefficient. A legitimate search must use orientation-sensitive frame/triad, connection or extrinsic-curvature data, parity-odd history observables, or nonlinear metric response.'
        ),
        'claim_boundary':(
            'Local intrinsic-metric linear-response theorem only. It does not prove that physical orientation dynamics is absent, does not kill connection/extrinsic-curvature or parity-odd observables, and does not determine g_YC^gravity.'
        ),
    }


def main()->int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path)
    a=ap.parse_args(); out=run(); text=json.dumps(out,indent=2); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
