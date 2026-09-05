#!/usr/bin/env python3
"""Conditioned numerical Legendre inversion for sampled scalar history modes.

This gate is the numerical counterpart of the exact symbolic
scalar_connected_history_extractor_gate.py.  It is intended for actual sampled
physical-history data, where G_QQ, G_Qzeta and G_zetazeta are floating/complex
numbers with an explicit error model.

It performs ONLY an ordinary 2x2 inverse when the connected Hessian is safely
nonsingular.  It never uses a pseudoinverse.  A near-singular or ill-conditioned
mode is fail-closed and marked for further reduction / controlled limiting
analysis.

A numerical inverse at isolated (omega,k) samples is not by itself a pole
classifier.  Physical poles require the already-frozen functional/kernel
analysis or a separately preregistered reconstruction from a sufficiently rich
mode grid.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any
import numpy as np

REQ_FLAGS=(
    'theory_specific_connected_history',
    'vacuum_disconnected_pieces_removed',
    'physical_omega_certified',
    'ward_source_basis_certified',
    'legendre_hessian_convention_certified',
)
REQ_HASHES=(
    'connected_history_hash',
    'ward_basis_hash',
    'history_convention_hash',
)


def cval(x:Any)->complex:
    if isinstance(x,bool): return complex(int(x),0)
    if isinstance(x,(int,float)): return complex(float(x),0)
    if isinstance(x,list) and len(x)==2: return complex(float(x[0]),float(x[1]))
    if isinstance(x,dict) and 're' in x and 'im' in x: return complex(float(x['re']),float(x['im']))
    if isinstance(x,str):
        s=x.replace('I','j').replace(' ','').replace('*j','j')
        try: return complex(s)
        except ValueError:
            # Pure decimal/rational strings are common in exact-compatible packets.
            if '/' in s and 'j' not in s:
                a,b=s.split('/',1); return complex(float(a)/float(b),0)
            raise
    raise TypeError(f'unsupported scalar {x!r}')


def jc(z:complex,tol:float=1e-14)->dict[str,float]:
    return {'re':0.0 if abs(z.real)<tol else float(z.real),'im':0.0 if abs(z.imag)<tol else float(z.imag)}


def analyze(packet:dict[str,Any],rcond_min:float=1e-12,residual_max:float=1e-10)->dict[str,Any]:
    errors=[]
    if packet.get('schema')!='BQG_CONNECTED_SCALAR_HISTORY_V1':
        errors.append('schema must be BQG_CONNECTED_SCALAR_HISTORY_V1')
    try:
        gqq=cval(packet['G_QQ']); gqz=cval(packet['G_Qzeta']); gzz=cval(packet['G_zetazeta'])
        G=np.array([[gqq,gqz],[gqz,gzz]],dtype=np.complex128)
    except Exception as exc:
        errors.append(f'invalid connected Hessian: {exc}')
        G=np.zeros((2,2),dtype=np.complex128)

    finite=bool(np.all(np.isfinite(G.real)) and np.all(np.isfinite(G.imag)))
    if not finite: errors.append('connected Hessian contains nonfinite values')

    det=np.linalg.det(G) if not errors else 0j
    svals=np.linalg.svd(G,compute_uv=False) if not errors else np.array([0.0,0.0])
    smax=float(np.max(svals)) if svals.size else 0.0
    smin=float(np.min(svals)) if svals.size else 0.0
    rcond=(smin/smax) if smax>0 else 0.0
    cond=(smax/smin) if smin>0 else math.inf
    safe=bool(not errors and rcond>=rcond_min and smin>0)

    flags=packet.get('physical_flags',{}) if isinstance(packet.get('physical_flags',{}),dict) else {}
    prov=packet.get('provenance',{}) if isinstance(packet.get('provenance',{}),dict) else {}
    provenance_ready=all(flags.get(x) is True for x in REQ_FLAGS) and all(bool(prov.get(x)) for x in REQ_HASHES)

    out={
        'schema':'BQG_NUMERIC_CONNECTED_SCALAR_HISTORY_INVERSION_V1',
        'passed':not errors,
        'science_status':'NUMERIC_CONNECTED_HESSIAN_NEAR_SINGULAR_REDUCE_OR_LIMIT' if not safe else 'NUMERIC_WARD_KERNEL_INVERTED',
        'ordinary_inverse_emitted':False,
        'pseudoinverse_used':False,
        'physical_interpretation_allowed':False,
        'G':[[jc(G[i,j]) for j in range(2)] for i in range(2)],
        'determinant':jc(det),
        'singular_values':[float(x) for x in svals],
        'condition_number':cond,
        'reciprocal_condition':rcond,
        'rcond_min':rcond_min,
        'inverse_residual_max':residual_max,
        'provenance_ready':bool(provenance_ready),
        'errors':errors,
        'claim_boundary':'Ordinary numerical inverse only. A sampled mode is not a dispersion/pole prediction; no pseudoinverse is used.'
    }
    if not safe:
        out['instruction']='Do not invert. Refine/remove a remaining source-null direction or study the controlled limiting behavior with uncertainties.'
        return out

    H=np.linalg.inv(G)
    resid=float(np.linalg.norm(G@H-np.eye(2),ord=2)/max(1.0,np.linalg.norm(G,ord=2)*np.linalg.norm(H,ord=2)))
    residual_ok=bool(np.isfinite(resid) and resid<=residual_max)
    physical=bool(provenance_ready and residual_ok)
    out.update({
        'science_status':'PHYSICAL_NUMERIC_WARD_KERNEL_SAMPLED' if physical else 'NUMERIC_WARD_KERNEL_INVERTED_PROVENANCE_OR_RESIDUAL_INCOMPLETE',
        'ordinary_inverse_emitted':True,
        'inverse_residual':resid,
        'inverse_residual_ok':residual_ok,
        'H':[[jc(H[i,j]) for j in range(2)] for i in range(2)],
        'A':jc(H[0,0]),'B':jc(H[0,1]),'C':jc(H[1,1]),
        'physical_interpretation_allowed':physical,
        'next_step':'Use a certified functional kernel or preregistered multi-mode reconstruction before pole/residue classification.'
    })
    return out


def selftest()->dict[str,Any]:
    flags={x:True for x in REQ_FLAGS}; prov={x:'synthetic' for x in REQ_HASHES}
    good={'schema':'BQG_CONNECTED_SCALAR_HISTORY_V1','G_QQ':2.0,'G_Qzeta':0.5000000000000002,'G_zetazeta':2.9999999999999996,'physical_flags':flags,'provenance':prov}
    g=analyze(good)
    target=np.array([[12/23,-2/23],[-2/23,8/23]],dtype=float)
    H=np.array([[g['H'][i][j]['re'] for j in range(2)] for i in range(2)])
    near={'schema':'BQG_CONNECTED_SCALAR_HISTORY_V1','G_QQ':1.0,'G_Qzeta':1.0-1e-15,'G_zetazeta':1.0,'physical_flags':flags,'provenance':prov}
    n=analyze(near,rcond_min=1e-12)
    incomplete=dict(good); incomplete['provenance']={}
    inc=analyze(incomplete)
    tests={
        'floating_connected_hessian_inverts':g['ordinary_inverse_emitted'] is True,
        'floating_inverse_matches_exact_control':bool(np.max(np.abs(H-target))<1e-12),
        'floating_inverse_residual_small':g.get('inverse_residual',1)>1e-16 and g.get('inverse_residual',1)<1e-10,
        'complete_numeric_sample_allows_physical_kernel_sample':g['physical_interpretation_allowed'] is True,
        'near_singular_fails_closed':n['ordinary_inverse_emitted'] is False and n['pseudoinverse_used'] is False,
        'missing_provenance_blocks_physical_promotion':inc['ordinary_inverse_emitted'] is True and inc['physical_interpretation_allowed'] is False,
    }
    return {'passed':all(tests.values()),'tests':tests,'controls':{'good':g,'near_singular':n,'incomplete':inc}}


def main()->int:
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--packet',type=Path); ap.add_argument('--output',type=Path); ap.add_argument('--rcond-min',type=float,default=1e-12); ap.add_argument('--residual-max',type=float,default=1e-10); args=ap.parse_args()
    out={'selftest':selftest()}
    if args.packet: out['production']=analyze(json.loads(args.packet.read_text(encoding='utf-8')),args.rcond_min,args.residual_max)
    out['passed']=bool(out['selftest']['passed'] and (not args.packet or out['production']['passed']))
    txt=json.dumps(out,indent=2); print(txt)
    if args.output: args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__=='__main__': raise SystemExit(main())
