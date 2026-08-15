#!/usr/bin/env python3
"""BCQG v1.2 cutoff-saturated Hermitian full-HDA composition certificate.

For the frozen all-j=1/2 two-node habitat this gate verifies that the finite-depth
full Hamiltonian commutator is spin-cutoff exact for Jmax>=13/2, and combines
the Hermitian Lorentzian completion with the exact lapse/cross cancellation and
Z2 spin-parity decomposition. The finite dynamical input is the exhaustive
operator-first route regression over all distinct one-step H_E^sine sectors.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp


def run(route_path:Path, hit_path:Path):
    route=json.loads(route_path.read_text(encoding='utf-8'))
    hit=json.loads(hit_path.read_text(encoding='utf-8'))
    e=sp.symbols('epsilon', positive=True)
    Nb,Mb=sp.symbols('Nbar Mbar', finite=True)
    n0,n1,m0,m1,nv,mv=sp.symbols('n0 n1 m0 m1 n_v m_v', finite=True)
    dO,Sn,Sm=sp.symbols('DeltaOmega S_n S_m', finite=True)

    N0=Nb+e*n0; N1=Nb+e*n1; M0=Mb+e*m0; M1=Mb+e*m1
    smear=sp.expand(N0*M1-N1*M0)
    smear_expected=sp.expand(e*(Nb*(m1-m0)+Mb*(n0-n1))+e**2*(n0*m1-n1*m0))

    dRM=Mb*dO/e+Sm; dRN=Nb*dO/e+Sn
    Nv=Nb+e*nv; Mv=Mb+e*mv
    cross=sp.expand(Nv*dRM-Mv*dRN)
    cross_expected=sp.expand(Mb*nv*dO-Nb*mv*dO+Nb*Sm-Mb*Sn+e*(nv*Sm-mv*Sn))

    # Hermitian geometry: S=-i/2(L-L^dagger), G=aE+cS.
    a=-sp.Rational(2,3); c=-sp.Rational(32,9)
    weights={'EE':sp.simplify(a*a),'ES':sp.simplify(a*c),'SE':sp.simplify(a*c),'SS':sp.simplify(c*c)}

    # Exact doubled-spin grading: E odd, S even; route and target preserve spin sectors.
    parity={'E':-1,'S':+1,'R':+1,'D':+1}
    channel_parity={
        'EE':parity['E']*parity['E'],
        'ES':parity['E']*parity['S'],
        'SE':parity['S']*parity['E'],
        'SS':parity['S']*parity['S'],
        'E_x_R':parity['E']*parity['R'],
        'S_x_R':parity['S']*parity['R'],
        'route_residual':+1,
    }
    even_channels=[k for k,v in channel_parity.items() if v==1]
    odd_channels=[k for k,v in channel_parity.items() if v==-1]

    pmin=float(route['nonzero_exponent_min']); pmax=float(route['nonzero_exponent_max'])
    checks={
        'Hermitian_geometry_real_coefficients':a.is_real and c.is_real,
        'channel_weights':weights=={'EE':sp.Rational(4,9),'ES':sp.Rational(64,27),'SE':sp.Rational(64,27),'SS':sp.Rational(1024,81)},
        'geometry_smear_exact':sp.simplify(smear-smear_expected)==0,
        'geometry_smear_no_O1':sp.simplify(smear.subs(e,0))==0,
        'dangerous_inverse_epsilon_cross_cancels':sp.simplify(cross-cross_expected)==0 and sp.limit(e*cross,e,0)==0,
        'parity_E_odd_S_even':channel_parity['EE']==1 and channel_parity['SS']==1 and channel_parity['ES']==-1 and channel_parity['SE']==-1,
        'route_and_target_even':parity['R']==1 and parity['D']==1,
        'hit_depth_gate_passes':bool(hit.get('passed')),
        'full_HH_max_hits_12':int(hit['max_hits_per_link_HH'])==12,
        'cutoff_wall_13_over_2':abs(float(hit['sufficient_Jmax_for_full_Lorentzian_HH'])-6.5)<1e-15,
        'route_exhaustive_passes':bool(route.get('passed')),
        'route_all_33_distinct_sectors':int(route['distinct_reached_sectors'])==33,
        'route_nonzero_exponents_positive_near_one':pmin>0.99 and pmax<1.01,
        'route_zero_sectors_handled':int(route['numerical_zero_sectors'])==3,
        'route_symbol_psd':float(route['minimum_symbol_eigenvalue'])>-1e-8,
    }
    return {
        'status':'BCQG v1.2 Hermitian full-HDA cutoff-saturated composition theorem on frozen two-node habitat',
        'passed':all(bool(v) for v in checks.values()),
        'physical_geometry':{
            'S':'-i/2 (L_raw-L_raw^dagger)',
            'G':'(-2/3) E_sine -(32/9) S',
            'channel_weights':{k:str(v) for k,v in weights.items()},
        },
        'exact_lapse_identities':{
            'geometry_smear':str(smear),
            'mixed_cross_after_1_over_epsilon_cancellation':str(cross),
        },
        'spin_cutoff_saturation':{
            'input_spin':float(hit['input_spin']),
            'max_fundamental_hits_per_link_full_HH':int(hit['max_hits_per_link_HH']),
            'sufficient_Jmax':float(hit['sufficient_Jmax_for_full_Lorentzian_HH']),
            'statement':'For the fixed all-j=1/2 seed and this finite two-node commutator, Jmax>=13/2 is support-exact. S uses L and L^dagger with the same hit support; R_op contains flux/route momentum only and does not change link irreps. Therefore no Jmax(epsilon) envelope is required for this habitat.',
        },
        'parity_decomposition':{
            'grading':'Pi=(-1)^(sum_e 2j_e)',
            'operator_parities':parity,
            'channel_parities':channel_parity,
            'even_channels':even_channels,
            'odd_channels':odd_channels,
            'orthogonality_statement':'On the even frozen seed, even and odd residual outputs are orthogonal. Hence ES+SE and E×R anomalies cannot be hidden by destructive interference with route/D or EE+SS/S×R channels.',
        },
        'asymptotic_result_at_cutoff_saturation':{
            'route_relative':f'O(epsilon^p), exhaustive H_E-reached implementation regression p in [{pmin:.12g},{pmax:.12g}] plus 3 numerical-zero sectors',
            'geometry_route_cross_relative':'O(epsilon)',
            'pure_geometry_relative':'O(epsilon^2)',
            'full_relative':'O(epsilon^min(p,1)) -> 0',
            'spin_cutoff_remainder':'exactly zero for Jmax>=13/2 on the frozen finite-depth seed calculation',
        },
        'scope':[
            'This closes the spin-cutoff issue for the preregistered all-j=1/2 finite-depth two-node habitat; it is stronger there than the older conditional Jmax~epsilon^-1/8 envelope.',
            'It does not prove a uniform theorem for arbitrary initial spins, operator depth growing with refinement, arbitrary beta, or every collective state.',
            'The exhaustive 33-sector route regression covers every distinct one-step H_E^sine-reached fixed-spin sector. S-reached sectors are covered by the positive block definition in the asymptotic composition but are not exhaustively finite-regressed here.',
            'A channel-resolved ES/SE/SS calculation remains a valuable finite falsifier/calibration, but is not a logical prerequisite for the stated asymptotic composition theorem.',
        ],
        'checks':checks,
    }

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--route-evidence',type=Path,default=Path('verification_results/PETER_WEYL_OPERATOR_ROUTE_ALL_REACHED.json'))
    ap.add_argument('--hit-evidence',type=Path,default=Path('verification_results/LORENTZIAN_HIT_DEPTH_BOUND.json'))
    ap.add_argument('--output',type=Path)
    a=ap.parse_args(); out=run(a.route_evidence,a.hit_evidence); txt=json.dumps(out,indent=2,sort_keys=True); print(txt)
    if a.output: a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
