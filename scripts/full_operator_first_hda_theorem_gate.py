#!/usr/bin/env python3
"""Symbolic/numeric certificate for the signed operator-first full-HDA asymptotic composition.

This gate does not replace the channel-resolved finite falsifier. It verifies
that, once the already tested operator-first route residual converges and the
local signed geometry operator is bounded at a regulator-safe cutoff, the
mixed and pure-geometry contaminants vanish with the frozen lapse/WKB scaling.

For beta=hbar=1 the upstream-fixed raw-code geometry operator is

    G_v = (-2/3) E_sine,v + (32 i/9) L_raw,v.

No coefficient is fitted here.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def run(route_evidence: Path | None = None):
    e=sp.symbols('epsilon', positive=True)
    Nb,Mb=sp.symbols('Nbar Mbar', finite=True)
    n0,n1,m0,m1,nv,mv=sp.symbols('n0 n1 m0 m1 n_v m_v', finite=True)
    dO,Sn,Sm=sp.symbols('DeltaOmega S_n S_m', finite=True)

    N0=Nb+e*n0; N1=Nb+e*n1
    M0=Mb+e*m0; M1=Mb+e*m1
    smear=sp.expand(N0*M1-N1*M0)
    smear_expected=sp.expand(
        e*(Nb*(m1-m0)+Mb*(n0-n1))
        +e**2*(n0*m1-n1*m0)
    )

    # On the frozen WKB family Omega_Q=e^-1 Otilde_Q. For a geometry change,
    # Delta R_M = Mbar/e DeltaO + S_m and likewise for N. The dangerous e^-1
    # term must cancel algebraically before any matrix element is evaluated.
    dRM=Mb*dO/e+Sm
    dRN=Nb*dO/e+Sn
    Nv=Nb+e*nv; Mv=Mb+e*mv
    cross=sp.expand(Nv*dRM-Mv*dRN)
    cross_expected=sp.expand(
        Mb*nv*dO-Nb*mv*dO+Nb*Sm-Mb*Sn
        +e*(nv*Sm-mv*Sn)
    )

    alpha=sp.Rational(1,8)
    p_cross_joint=sp.simplify(1-sp.Rational(13,2)*alpha)
    p_gg_joint=sp.simplify(2-13*alpha)

    aE=-sp.Rational(2,3)
    bL=sp.I*sp.Rational(32,9)
    weights={
        'EE':sp.simplify(aE*aE),
        'EL':sp.simplify(aE*bL),
        'LE':sp.simplify(aE*bL),
        'LL':sp.simplify(bL*bL),
    }

    route=None
    if route_evidence is not None and route_evidence.exists():
        route=json.loads(route_evidence.read_text(encoding='utf-8'))
    route_pass=bool(route and route.get('passed',False))
    route_exponents=[] if not route else [
        float(x['epsilon_exponent']) for x in route.get('sector_summary',[])
    ]
    route_endpoints=[] if not route else [
        float(x['endpoint']) for x in route.get('sector_summary',[])
    ]

    checks={
        'signed_E_coefficient':aE==-sp.Rational(2,3),
        'signed_Lraw_coefficient':bL==sp.I*sp.Rational(32,9),
        'signed_EE_weight':weights['EE']==sp.Rational(4,9),
        'signed_mixed_weight':weights['EL']==-sp.I*sp.Rational(64,27) and weights['LE']==-sp.I*sp.Rational(64,27),
        'signed_LL_weight':weights['LL']==-sp.Rational(1024,81),
        'geometry_smear_identity':sp.simplify(smear-smear_expected)==0,
        'geometry_smear_has_no_O1':sp.simplify(smear.subs(e,0))==0,
        'dangerous_cross_inverse_epsilon_cancels':sp.simplify(cross-cross_expected)==0 and sp.limit(e*cross,e,0)==0,
        'canonical_alpha_inside_window':0<float(alpha)<2/13,
        'canonical_alpha_cross_power':p_cross_joint==sp.Rational(3,16),
        'canonical_alpha_GG_power':p_gg_joint==sp.Rational(3,8),
        'spinchanged_operator_first_route_evidence_passes':route_pass,
        'spinchanged_route_exponents_near_one':bool(route_exponents) and min(route_exponents)>0.99 and max(route_exponents)<1.01,
        'spinchanged_route_endpoints_small':bool(route_endpoints) and max(route_endpoints)<5e-6,
    }

    out={
        'status':'signed operator-first full-HDA asymptotic composition certificate',
        'passed':all(checks.values()),
        'signed_geometry_operator':'G_v=(-2/3)E_sine,v+(32 i/9)L_raw,v at beta=hbar=1',
        'signed_channel_weights':{k:str(v) for k,v in weights.items()},
        'geometry_smear_identity':str(smear),
        'mixed_cross_after_exact_inverse_epsilon_cancellation':str(cross),
        'fixed_cutoff_result':{
            'route_only_relative':'Delta_route -> 0 (tested operator-first habitat)',
            'C_cross_over_D':'O(epsilon)',
            'C_GG_over_D':'O(epsilon^2)',
            'full_relative_residual':'Delta_route + O(epsilon) + O(epsilon^2) -> 0',
        },
        'joint_cutoff_path':{
            'Jmax':'epsilon^(-1/8)',
            'C_cross_over_D':'O(epsilon^(3/16))',
            'C_GG_over_D':'O(epsilon^(3/8))',
            'scope':'conditional on the frozen polynomial norm envelope; not a uniform arbitrary-path theorem',
        },
        'spinchanged_route_evidence':{
            'checked_sectors':0 if route is None else route.get('checked_distinct_higher_spin_sectors',0),
            'epsilon_exponents':route_exponents,
            'endpoints':route_endpoints,
            'minimum_symbol_eigenvalue':None if route is None else route.get('minimum_symbol_eigenvalue'),
            'provenance':None if route is None else route.get('provenance'),
        },
        'assumptions':[
            'fixed regulator-safe finite Peter-Weyl cutoff, hence each local signed G_v is bounded',
            'operator-first Omega_Q=sqrt(Qhat^{ab}P_aP_b)=epsilon^-1 Otilde_Q on the frozen WKB family',
            'N=Nbar+epsilon*n and M=Mbar+epsilon*m with frozen smooth n,m',
            'D target norm is O(epsilon^-1) on the nonzero WKB carrier',
            'route-only operator-first HDA residual converges on the declared sectors',
            'joint-cutoff statement additionally assumes the frozen polynomial norm envelope',
        ],
        'checks':checks,
        'finite_falsifier_status':'still required as an independent channel-resolved calibration; a timeout is not a physics FAIL',
    }
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--route-evidence',type=Path,default=Path('verification_results/PETER_WEYL_OPERATOR_ROUTE_SPINCHANGED_BLOCKS.json'))
    p.add_argument('--output',type=Path)
    a=p.parse_args(); out=run(a.route_evidence)
    text=json.dumps(out,indent=2,sort_keys=True); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
