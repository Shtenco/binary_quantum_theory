#!/usr/bin/env python3
"""Exact 2x2 connected-history -> scalar Ward-kernel extractor.

After the flat/local Ward quotient the physical scalar source space is
(Q,zeta).  If the theory-specific connected history supplies the properly
normalized connected Hessian

    G = W^(2) = [[G_QQ, G_Qz], [G_Qz, G_zz]],

on a nonsingular physical source quotient and in a convention for which the
Legendre Hessian identity is Gamma^(2)=G^{-1}, then

    A = G_zz / det G,
    B = -G_Qz / det G,
    C = G_QQ / det G.

Thus the microscopic history target is exactly three connected functions, not
an arbitrary ADM matrix.  Singular G is fail-closed and requires a further
constraint/gauge/source quotient; it is never pseudoinverted and interpreted
as a physical pole by this gate.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any
import sympy as sp

W2,K2=sp.symbols('w2 k2', real=True)

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


def e(x:Any)->sp.Expr:
    if isinstance(x,bool): return sp.Integer(int(x))
    if isinstance(x,int): return sp.Integer(x)
    if isinstance(x,float): return sp.Rational(str(x))
    if isinstance(x,str): return sp.sympify(x,locals={'w2':W2,'k2':K2})
    raise TypeError(x)


def ss(x:sp.Expr)->str:
    return str(sp.factor(sp.simplify(x)))


def extract(packet:dict[str,Any])->dict[str,Any]:
    if packet.get('schema')!='BQG_CONNECTED_SCALAR_HISTORY_V1':
        raise ValueError('schema must be BQG_CONNECTED_SCALAR_HISTORY_V1')
    gqq,gqz,gzz=(e(packet[k]) for k in ('G_QQ','G_Qzeta','G_zetazeta'))
    G=sp.Matrix([[gqq,gqz],[gqz,gzz]])
    det=sp.factor(sp.simplify(G.det()))
    singular=sp.simplify(det)==0
    flags=dict(packet.get('physical_flags',{}));prov=dict(packet.get('provenance',{}))
    ready=all(flags.get(x) is True for x in REQ_FLAGS) and all(bool(prov.get(x)) for x in REQ_HASHES)

    if singular:
        return {
            'schema':'BQG_CONNECTED_SCALAR_HISTORY_EXTRACTION_V1',
            'science_status':'SINGULAR_CONNECTED_SOURCE_HESSIAN_REDUCE_FURTHER',
            'connected_matrix':[[ss(G[i,j]) for j in range(2)] for i in range(2)],
            'determinant':'0',
            'nonsingular_source_quotient':False,
            'ward_kernel_emitted':False,
            'physical_interpretation_allowed':False,
            'instruction':'Identify and remove the remaining exact constraint/gauge/null source direction before Legendre inversion. Do not use a Moore-Penrose inverse as a physical pole generator.',
            'claim_boundary':'Singular source Hessian is a reduction signal, not evidence for dark matter or a propagating scalar.'
        }

    H=sp.simplify(G.inv())
    ident=sp.simplify(G*H-sp.eye(2))
    inversion_exact=all(sp.simplify(x)==0 for x in ident)
    A,B,C=sp.simplify(H[0,0]),sp.simplify(H[0,1]),sp.simplify(H[1,1])
    physical=bool(ready and inversion_exact)
    return {
        'schema':'BQG_CONNECTED_SCALAR_HISTORY_EXTRACTION_V1',
        'science_status':'PHYSICAL_WARD_KERNEL_EXTRACTED' if physical else 'ALGEBRAIC_WARD_KERNEL_EXTRACTED_PHYSICAL_PROVENANCE_INCOMPLETE',
        'connected_matrix':[[ss(G[i,j]) for j in range(2)] for i in range(2)],
        'determinant':ss(det),
        'nonsingular_source_quotient':True,
        'exact_inverse_identity':bool(inversion_exact),
        'A':ss(A),'B':ss(B),'C':ss(C),
        'formulae':{
            'A':'G_zetazeta / (G_QQ*G_zetazeta-G_Qzeta^2)',
            'B':'-G_Qzeta / (G_QQ*G_zetazeta-G_Qzeta^2)',
            'C':'G_QQ / (G_QQ*G_zetazeta-G_Qzeta^2)',
        },
        'ward_kernel_emitted':True,
        'physical_interpretation_allowed':physical,
        'physical_flags':flags,
        'provenance_complete':all(bool(prov.get(x)) for x in REQ_HASHES),
        'ward_kernel_packet':{
            'schema':'BQG_SCALAR_WARD_KERNEL_V1',
            'A':ss(A),'B':ss(B),'C':ss(C),
            'j_Q':str(packet.get('j_Q',0)),
            'j_zeta':str(packet.get('j_zeta',0)),
            'physical_flags':{
                'theory_specific_connected_history':bool(flags.get('theory_specific_connected_history')),
                'physical_omega_certified':bool(flags.get('physical_omega_certified')),
                'ward_reduction_certified':bool(flags.get('ward_source_basis_certified')),
                'conserved_probe_frozen':bool(packet.get('conserved_probe_frozen',False)),
                'background_and_scale_convention_frozen':bool(packet.get('background_and_scale_convention_frozen',False)),
            },
            'provenance':{
                'connected_history_hash':prov.get('connected_history_hash'),
                'ward_certificate_hash':prov.get('ward_basis_hash'),
                'source_convention_hash':packet.get('source_convention_hash'),
                'background_convention_hash':packet.get('background_convention_hash'),
            }
        },
        'microscopic_target':'Compute exactly three connected physical functions G_QQ, G_Qzeta, G_zetazeta in physical (omega,k) variables.',
        'claim_boundary':'This gate performs only the exact Legendre-Hessian inversion on an already physical connected source quotient. Constraint resolvents, normalized local traces, or z-spectral kernels cannot be substituted for these three functions.'
    }


def selftest()->dict[str,Any]:
    tests={}
    empty={x:False for x in REQ_FLAGS}
    ident=extract({'schema':'BQG_CONNECTED_SCALAR_HISTORY_V1','G_QQ':1,'G_Qzeta':0,'G_zetazeta':1,'physical_flags':empty,'provenance':{}})
    tests['identity_connected_control_gives_identity_1PI']=ident['A']=='1' and ident['B']=='0' and ident['C']=='1'
    tests['identity_control_fail_closed_without_provenance']=ident['physical_interpretation_allowed'] is False

    corr=extract({'schema':'BQG_CONNECTED_SCALAR_HISTORY_V1','G_QQ':2,'G_Qzeta':'1/2','G_zetazeta':3,'physical_flags':empty,'provenance':{}})
    # det = 23/4 -> inverse [[12/23,-2/23],[-2/23,8/23]]
    tests['correlated_exact_inverse_A']=corr['A']=='12/23'
    tests['correlated_exact_inverse_B']=corr['B']=='-2/23'
    tests['correlated_exact_inverse_C']=corr['C']=='8/23'

    sing=extract({'schema':'BQG_CONNECTED_SCALAR_HISTORY_V1','G_QQ':1,'G_Qzeta':1,'G_zetazeta':1,'physical_flags':empty,'provenance':{}})
    tests['singular_control_requires_further_reduction']=sing['science_status']=='SINGULAR_CONNECTED_SOURCE_HESSIAN_REDUCE_FURTHER' and sing['ward_kernel_emitted'] is False

    fullflags={x:True for x in REQ_FLAGS};fullprov={x:'synthetic' for x in REQ_HASHES}
    ready=extract({'schema':'BQG_CONNECTED_SCALAR_HISTORY_V1','G_QQ':2,'G_Qzeta':'1/2','G_zetazeta':3,'j_Q':1,'j_zeta':1,'conserved_probe_frozen':True,'background_and_scale_convention_frozen':True,'source_convention_hash':'synthetic-source','background_convention_hash':'synthetic-bg','physical_flags':fullflags,'provenance':fullprov})
    tests['complete_synthetic_history_allows_physical_extraction']=ready['physical_interpretation_allowed'] is True
    tests['complete_synthetic_emits_response_ready_packet']=all(ready['ward_kernel_packet']['physical_flags'].values()) and all(ready['ward_kernel_packet']['provenance'].values())

    return {'schema':'BQG_CONNECTED_SCALAR_HISTORY_EXTRACTOR_SELFTEST_V1','passed':bool(all(tests.values())),'tests':tests,'controls':{'identity':ident,'correlated':corr,'singular':sing,'complete_synthetic':ready},'claim_boundary':'Synthetic controls certify inversion and fail-closed logic only.'}


def main()->int:
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--packet',type=Path);ap.add_argument('--output',type=Path);a=ap.parse_args()
    out={'selftest':selftest()}
    if a.packet: out['production']=extract(json.loads(a.packet.read_text(encoding='utf-8')))
    out['passed']=bool(out['selftest']['passed'])
    txt=json.dumps(out,indent=2);print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
