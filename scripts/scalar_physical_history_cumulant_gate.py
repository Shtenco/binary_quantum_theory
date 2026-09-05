#!/usr/bin/env python3
"""Physical scalar W-history -> three connected Ward cumulants.

This is the production measurement interface immediately upstream of the
already-closed scalar connected-history consumer pipeline.

Legal input is a theory-specific connected physical generating functional W
sampled with the two certified Ward-source insertions Q and zeta at geometric
boundary/history separations (tau, r).  The gate never accepts a constraint
resolvent parameter z as a replacement for physical omega.

Two source-derivative modes are supported at each separation point:

1. provided_connected_hessian:
   the history engine directly supplies d2W/dJ_a dJ_b;
2. central_difference_W:
   the gate forms centered second differences of W.  This is exact for a
   quadratic source dependence and otherwise carries the usual finite-source
   O(h^2) truncation that must be controlled by a source-step scan.

The discrete physical Fourier convention is

  G_ab(omega,k) = sum_p weight_p exp(i omega tau_p - i k.r_p) G_ab(p).

No continuum-volume normalization is silently invented; quadrature weights are
part of the input packet and therefore part of the frozen history convention.
"""
from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path
from typing import Any

REQUIRED_FLAGS=(
    'theory_specific_physical_history',
    'connected_functional_W_not_raw_Z',
    'physical_tau_certified',
    'physical_spatial_separation_certified',
    'ward_source_insertions_certified',
    'same_history_normalization_across_sources',
)
REQUIRED_PROVENANCE=(
    'physical_history_hash',
    'ward_source_hash',
    'time_space_convention_hash',
    'history_normalization_hash',
)


def _c(x: Any) -> complex:
    if isinstance(x,(int,float)):
        return complex(float(x),0.0)
    if isinstance(x,list) and len(x)==2:
        return complex(float(x[0]),float(x[1]))
    if isinstance(x,dict) and set(x)>={'re','im'}:
        return complex(float(x['re']),float(x['im']))
    if isinstance(x,str):
        return complex(x.replace('I','j').replace(' ','').replace('*j','j'))
    raise TypeError(f'unsupported complex value {x!r}')


def _json_c(z: complex, tol: float=1e-14) -> dict[str,float]:
    re=0.0 if abs(z.real)<tol else float(z.real)
    im=0.0 if abs(z.imag)<tol else float(z.imag)
    return {'re':re,'im':im}


def _sympy_c(z: complex, tol: float=1e-14) -> str:
    re=0.0 if abs(z.real)<tol else z.real
    im=0.0 if abs(z.imag)<tol else z.imag
    if im==0.0:
        return f'{re:.17g}'
    if re==0.0:
        return f'({im:.17g})*I'
    return f'({re:.17g})+({im:.17g})*I'


def _finite(v: float) -> bool:
    return math.isfinite(float(v))


def point_hessian(point: dict[str,Any], source_steps: dict[str,float]) -> tuple[complex,complex,complex,str]:
    mode=point.get('derivative_mode')
    if mode=='provided_connected_hessian':
        h=point.get('connected_hessian',{})
        return _c(h['G_QQ']),_c(h['G_Qzeta']),_c(h['G_zetazeta']),mode
    if mode!='central_difference_W':
        raise ValueError(f'unsupported derivative_mode {mode!r}')
    hQ=float(source_steps['Q']); hZ=float(source_steps['zeta'])
    if hQ<=0 or hZ<=0 or not (_finite(hQ) and _finite(hZ)):
        raise ValueError('central source steps must be finite and positive')
    W=point.get('W_samples',{})
    w0=_c(W['00'])
    gqq=(_c(W['Q+'])-2*w0+_c(W['Q-']))/(hQ*hQ)
    gzz=(_c(W['zeta+'])-2*w0+_c(W['zeta-']))/(hZ*hZ)
    gqz=(_c(W['++'])-_c(W['+-'])-_c(W['-+'])+_c(W['--']))/(4*hQ*hZ)
    return gqq,gqz,gzz,mode


def measure(packet: dict[str,Any]) -> dict[str,Any]:
    errors:list[str]=[]
    if packet.get('schema')!='BQG_PHYSICAL_SCALAR_W_HISTORY_V1':
        errors.append('schema must be BQG_PHYSICAL_SCALAR_W_HISTORY_V1')
    flags=packet.get('physical_flags',{}) if isinstance(packet.get('physical_flags',{}),dict) else {}
    provenance=packet.get('provenance',{}) if isinstance(packet.get('provenance',{}),dict) else {}
    missing_flags=[x for x in REQUIRED_FLAGS if flags.get(x) is not True]
    missing_prov=[x for x in REQUIRED_PROVENANCE if not provenance.get(x)]
    points=packet.get('points',[])
    modes=packet.get('modes',[])
    if not isinstance(points,list) or not points: errors.append('points must be a nonempty list')
    if not isinstance(modes,list) or not modes: errors.append('modes must be a nonempty list')
    source_steps=packet.get('source_steps',{}) if isinstance(packet.get('source_steps',{}),dict) else {}

    realspace=[]
    derivative_modes=set()
    if not errors:
        for i,p in enumerate(points):
            try:
                tau=float(p['tau']); r=[float(x) for x in p['r']]; weight=float(p.get('weight',1.0))
                if len(r)!=3: raise ValueError('r must have length 3')
                if not all(_finite(x) for x in [tau,*r,weight]): raise ValueError('nonfinite geometry/weight')
                gqq,gqz,gzz,dmode=point_hessian(p,source_steps)
                derivative_modes.add(dmode)
                realspace.append({'tau':tau,'r':r,'weight':weight,'G_QQ':gqq,'G_Qzeta':gqz,'G_zetazeta':gzz})
            except Exception as exc:
                errors.append(f'point[{i}]: {exc}')

    fourier=[]
    if not errors:
        for i,m in enumerate(modes):
            try:
                omega=float(m['omega']); k=[float(x) for x in m['k']]
                if len(k)!=3: raise ValueError('k must have length 3')
                if not all(_finite(x) for x in [omega,*k]): raise ValueError('nonfinite mode')
                sums={'G_QQ':0j,'G_Qzeta':0j,'G_zetazeta':0j}
                for p in realspace:
                    phase=omega*p['tau']-sum(k[a]*p['r'][a] for a in range(3))
                    e=cmath.exp(1j*phase)*p['weight']
                    for key in sums: sums[key]+=e*p[key]
                fourier.append({
                    'omega':omega,'k':k,
                    'G_QQ':_json_c(sums['G_QQ']),
                    'G_Qzeta':_json_c(sums['G_Qzeta']),
                    'G_zetazeta':_json_c(sums['G_zetazeta']),
                    'downstream_connected_history_packet':{
                        'schema':'BQG_CONNECTED_SCALAR_HISTORY_V1',
                        'G_QQ':_sympy_c(sums['G_QQ']),
                        'G_Qzeta':_sympy_c(sums['G_Qzeta']),
                        'G_zetazeta':_sympy_c(sums['G_zetazeta']),
                        'physical_flags':{
                            'theory_specific_connected_history':not missing_flags,
                            'vacuum_disconnected_pieces_removed':flags.get('connected_functional_W_not_raw_Z') is True,
                            'physical_omega_certified':flags.get('physical_tau_certified') is True,
                            'ward_source_basis_certified':flags.get('ward_source_insertions_certified') is True,
                            'legendre_hessian_convention_certified':flags.get('legendre_hessian_convention_certified') is True,
                        },
                        'provenance':{
                            'connected_history_hash':provenance.get('physical_history_hash',''),
                            'ward_basis_hash':provenance.get('ward_source_hash',''),
                            'history_convention_hash':provenance.get('history_normalization_hash',''),
                        },
                        'conserved_probe_frozen':flags.get('conserved_probe_frozen') is True,
                        'background_and_scale_convention_frozen':flags.get('background_and_scale_convention_frozen') is True,
                        'source_convention_hash':provenance.get('source_convention_hash',''),
                        'background_convention_hash':provenance.get('background_convention_hash',''),
                    }
                })
            except Exception as exc:
                errors.append(f'mode[{i}]: {exc}')

    finite_difference_used='central_difference_W' in derivative_modes
    step_scan=packet.get('source_step_scan_certified') is True
    physical_ready=(
        not errors and not missing_flags and not missing_prov
        and flags.get('legendre_hessian_convention_certified') is True
        and flags.get('conserved_probe_frozen') is True
        and flags.get('background_and_scale_convention_frozen') is True
        and bool(provenance.get('source_convention_hash'))
        and bool(provenance.get('background_convention_hash'))
        and (not finite_difference_used or step_scan)
    )
    return {
        'schema':'BQG_SCALAR_PHYSICAL_HISTORY_CUMULANTS_V1',
        'passed':not errors,
        'science_status':(
            'PHYSICAL_SCALAR_CONNECTED_CUMULANTS_MEASURED'
            if physical_ready else
            'MEASUREMENT_INTERFACE_VALID_PHYSICAL_PROVENANCE_INCOMPLETE'
        ),
        'physical_interpretation_allowed':physical_ready,
        'derivative_modes':sorted(derivative_modes),
        'finite_difference_source_step_scan_required':finite_difference_used,
        'source_step_scan_certified':step_scan,
        'missing_required_flags':missing_flags,
        'missing_required_provenance':missing_prov,
        'realspace_connected_cumulants':[
            {'tau':p['tau'],'r':p['r'],'weight':p['weight'],
             'G_QQ':_json_c(p['G_QQ']),'G_Qzeta':_json_c(p['G_Qzeta']),'G_zetazeta':_json_c(p['G_zetazeta'])}
            for p in realspace
        ],
        'fourier_modes':fourier,
        'fourier_convention':'sum_p weight_p exp(i*omega*tau_p - i*k.r_p) G_ab(p)',
        'open_input':'source-dressed theory-specific physical connected W[J_Q,J_zeta; tau,r]',
        'forbidden_substitutions':['constraint spectral z -> physical omega','raw Z second derivatives -> connected W cumulants','Feshbach resolvent -> physical history correlator'],
        'errors':errors,
    }


def _quadratic_W(q:float,z:float,gqq:float,gqz:float,gzz:float)->float:
    return 0.5*gqq*q*q+gqz*q*z+0.5*gzz*z*z


def selftest()->dict[str,Any]:
    h=0.01
    def wp(q,z): return _quadratic_W(q,z,2.0,0.5,3.0)
    p={
        'tau':0.0,'r':[0.0,0.0,0.0],'weight':1.0,
        'derivative_mode':'central_difference_W',
        'W_samples':{
            '00':wp(0,0),'Q+':wp(h,0),'Q-':wp(-h,0),
            'zeta+':wp(0,h),'zeta-':wp(0,-h),
            '++':wp(h,h),'+-':wp(h,-h),'-+':wp(-h,h),'--':wp(-h,-h),
        }
    }
    base={
        'schema':'BQG_PHYSICAL_SCALAR_W_HISTORY_V1',
        'source_steps':{'Q':h,'zeta':h},'source_step_scan_certified':True,
        'points':[p],'modes':[{'omega':0.0,'k':[0.0,0.0,0.0]}],
        'physical_flags':{
            'theory_specific_physical_history':True,
            'connected_functional_W_not_raw_Z':True,
            'physical_tau_certified':True,
            'physical_spatial_separation_certified':True,
            'ward_source_insertions_certified':True,
            'same_history_normalization_across_sources':True,
            'legendre_hessian_convention_certified':True,
            'conserved_probe_frozen':True,
            'background_and_scale_convention_frozen':True,
        },
        'provenance':{
            'physical_history_hash':'synthetic-history','ward_source_hash':'synthetic-ward',
            'time_space_convention_hash':'synthetic-time-space','history_normalization_hash':'synthetic-norm',
            'source_convention_hash':'synthetic-source','background_convention_hash':'synthetic-background',
        }
    }
    ok=measure(base); mode=ok['fourier_modes'][0]
    def close(obj,x): return abs(obj['re']-x)<1e-10 and abs(obj['im'])<1e-10
    tests={
        'quadratic_central_difference_G_QQ_exact':close(mode['G_QQ'],2.0),
        'quadratic_central_difference_G_Qzeta_exact':close(mode['G_Qzeta'],0.5),
        'quadratic_central_difference_G_zetazeta_exact':close(mode['G_zetazeta'],3.0),
        'complete_synthetic_history_is_physical_ready':ok['physical_interpretation_allowed'] is True,
    }
    bad=json.loads(json.dumps(base)); bad['physical_flags']['physical_tau_certified']=False
    badm=measure(bad)
    tests['uncertified_tau_fails_closed']=badm['physical_interpretation_allowed'] is False
    raw=json.loads(json.dumps(base)); raw['physical_flags']['connected_functional_W_not_raw_Z']=False
    rawm=measure(raw)
    tests['raw_Z_like_input_fails_closed']=rawm['physical_interpretation_allowed'] is False
    nostep=json.loads(json.dumps(base)); nostep['source_step_scan_certified']=False
    nostepm=measure(nostep)
    tests['finite_difference_without_step_scan_fails_closed']=nostepm['physical_interpretation_allowed'] is False
    return {'passed':all(tests.values()),'tests':tests,'positive_control':ok}


def main()->int:
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--packet',type=Path); ap.add_argument('--output',type=Path); a=ap.parse_args()
    out={'selftest':selftest()}
    if a.packet: out['production']=measure(json.loads(a.packet.read_text(encoding='utf-8')))
    out['passed']=bool(out['selftest']['passed'] and (not a.packet or out['production']['passed']))
    txt=json.dumps(out,indent=2); print(txt)
    if a.output: a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__=='__main__': raise SystemExit(main())
