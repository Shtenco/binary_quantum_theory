#!/usr/bin/env python3
"""Exact q=2 oriented-flux/history observable bridge.

On four spin-1/2 faces define the gauge-scalar oriented triple product

    Q_or = epsilon_abc J1^a J2^b J3^c.

Projected to the two-dimensional four-valent singlet carrier (K=0,2),

    Q_or = (sqrt(3)/4) Y_L.

Thus the abstract logical orientation Pauli is a genuine microscopic flux
pseudoscalar,

    Y_L = (4/sqrt(3)) Q_or.

Combining with the already-derived history current C_h and minimal orientation
step gives

    (W-W^dagger)/(2i) = Y_L tensor C_h
                       = (4/sqrt(3)) Q_or tensor C_h.

The gate also verifies that Q_or commutes with total SU(2) generators and flips
sign under an odd permutation of the first two faces.  Finally it rewrites the
exact S4 Lorentzian sign-twirl extractor in Q_or language:

    L_epsilon^logical = -12 Tr(Y O) Y
                      = -64 Tr(Q_or O) Q_or.

This supplies a microscopic gauge-scalar orientation witness for future genuine
Peter-Weyl amplitudes.  It does not determine the physical coupling coefficient.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def kron4(a,b,c,d):
    return sp.kronecker_product(a,b,c,d)


def zero(M: sp.Matrix) -> bool:
    return all(sp.simplify(sp.expand_complex(x)) == 0 for x in M)


def permute_12_operator(dim=2):
    # Swap first two tensor factors in (C^2)^4.
    P=sp.zeros(dim**4)
    for a in range(dim):
        for b in range(dim):
            for c in range(dim):
                for d in range(dim):
                    old=((a*dim+b)*dim+c)*dim+d
                    new=((b*dim+a)*dim+c)*dim+d
                    P[new,old]=1
    return P


def run() -> dict[str,object]:
    I=sp.eye(2)
    X=sp.Matrix([[0,1],[1,0]])
    Y=sp.Matrix([[0,-sp.I],[sp.I,0]])
    Z=sp.Matrix([[1,0],[0,-1]])
    js=[X/2,Y/2,Z/2]

    # epsilon tensor.
    eps={
        (0,1,2):1,(1,2,0):1,(2,0,1):1,
        (1,0,2):-1,(2,1,0):-1,(0,2,1):-1,
    }
    Q=sp.zeros(16)
    for (a,b,c),sgn in eps.items():
        Q += sgn*kron4(js[a],js[b],js[c],I)
    Q=Q.applyfunc(sp.simplify)

    # Standard K=0 and K=2 (j12=0,1) four-spin singlets.
    up=sp.Matrix([1,0]); dn=sp.Matrix([0,1])
    sing=(sp.kronecker_product(up,dn)-sp.kronecker_product(dn,up))/sp.sqrt(2)
    i0=sp.kronecker_product(sing,sing)
    tp=sp.kronecker_product(up,up)
    t0=(sp.kronecker_product(up,dn)+sp.kronecker_product(dn,up))/sp.sqrt(2)
    tm=sp.kronecker_product(dn,dn)
    i1=(sp.kronecker_product(tp,tm)-sp.kronecker_product(t0,t0)+sp.kronecker_product(tm,tp))/sp.sqrt(3)
    B=i0.row_join(i1)
    checks={
        'singlet_basis_orthonormal': zero(B.H*B-sp.eye(2)),
    }
    Qlog=(B.H*Q*B).applyfunc(sp.simplify)
    target=sp.sqrt(3)/4*Y
    checks['logical_oriented_flux_equals_sqrt3_over4_Y']=zero(Qlog-target)

    # Gauge scalar: commute with total angular momentum.
    total=[]
    for a in range(3):
        Ja=(
            kron4(js[a],I,I,I)+kron4(I,js[a],I,I)
            +kron4(I,I,js[a],I)+kron4(I,I,I,js[a])
        )
        total.append(Ja)
    comm=[(Q*Ja-Ja*Q).applyfunc(sp.simplify) for Ja in total]
    checks['Q_or_commutes_with_total_SU2']=all(zero(C) for C in comm)

    # Odd face swap reverses the pseudoscalar.
    P12=permute_12_operator()
    checks['odd_face_swap_flips_Q_or']=zero(P12*Q*P12.T+Q)

    # Q logical norm and exact inverse relation.
    checks['Q_logical_squared_is_3_over_16_I']=zero(Qlog*Qlog-sp.Rational(3,16)*sp.eye(2))
    checks['Y_equals_4_over_sqrt3_Q_logical']=zero(Y-4/sp.sqrt(3)*Qlog)
    hs_Q=sp.simplify(sp.trace(Qlog.H*Qlog))
    checks['Q_logical_HS_norm_squared_is_3_over_8']=sp.simplify(hs_Q-sp.Rational(3,8))==0

    # Symbolic extractor equivalence for a generic logical 2x2 operator.
    o00,o01,o10,o11=sp.symbols('o00 o01 o10 o11')
    O=sp.Matrix([[o00,o01],[o10,o11]])
    Ly=(-12*sp.trace(Y*O)*Y).applyfunc(sp.simplify)
    Lq=(-64*sp.trace(Qlog*O)*Qlog).applyfunc(sp.simplify)
    checks['Y_and_Q_Lorentzian_sign_twirl_extractors_are_identical']=zero(Ly-Lq)

    # If O=b_Q Q + orthogonal pieces, full epsilon sign twirl multiplies the
    # Q coefficient by -24, consistent with -64 Tr(QO) Q and Tr(Q^2)=3/8.
    bq=sp.symbols('bq')
    Oq=bq*Qlog
    Lq_pure=(-64*sp.trace(Qlog*Oq)*Qlog).applyfunc(sp.simplify)
    checks['pure_Q_coefficient_maps_to_minus24_bQ_Q']=zero(Lq_pure+24*bq*Qlog)

    # History-current identity in Q language.
    n=8
    U=sp.zeros(n)
    for k in range(n): U[(k+1)%n,k]=1
    Ch=((U-U.T)/(2*sp.I)).applyfunc(lambda x:sp.simplify(sp.expand_complex(x)))
    Pp=(sp.eye(2)+Y)/2; Pm=(sp.eye(2)-Y)/2
    W=sp.kronecker_product(Pp,U)+sp.kronecker_product(Pm,U.T)
    odd=((W-W.H)/(2*sp.I)).applyfunc(lambda x:sp.simplify(sp.expand_complex(x)))
    qhistory=(4/sp.sqrt(3)*sp.kronecker_product(Qlog,Ch)).applyfunc(lambda x:sp.simplify(sp.expand_complex(x)))
    checks['minimal_history_odd_part_equals_4_over_sqrt3_Q_tensor_Ch']=zero(odd-qhistory)

    passed=bool(all(checks.values()))
    return {
        'status':'exact microscopic oriented-flux realization of logical q=2 orientation/history channel',
        'passed':passed,
        'Q_or_logical':[[str(x) for x in row] for row in Qlog.tolist()],
        'identity':'Q_or=(sqrt(3)/4)Y_L; Y_L=(4/sqrt(3))Q_or',
        'history_identity':'(W-W^dagger)/(2i)=(4/sqrt(3)) Q_or tensor C_h',
        'Lorentzian_extractor':'L_epsilon^logical=-64 Tr(Q_or O) Q_or = -12 Tr(Y_L O) Y_L',
        'Q_Hilbert_Schmidt_norm_squared':str(hs_Q),
        'checks':checks,
        'physical_use':(
            'For a future genuine Peter-Weyl logical ordered-triple matrix O, the orientation-odd Lorentzian channel may be extracted using the gauge-scalar microscopic flux pseudoscalar Q_or rather than treating Pauli Y as a merely abstract logical label.'
        ),
        'claim_boundary':(
            'Exact local representation/operator theorem only. It does not show that the full genuine Lorentzian amplitude has a nonzero Q_or component, does not construct the physical history measure, and does not determine g_YC^gravity.'
        ),
    }


def main()->int:
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--output',type=Path); a=ap.parse_args()
    out=run(); text=json.dumps(out,indent=2); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
