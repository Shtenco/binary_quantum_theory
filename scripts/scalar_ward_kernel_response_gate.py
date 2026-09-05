#!/usr/bin/env python3
"""Analyze a two-function-basis scalar Ward kernel without phenomenological fits.

Input kernel is the exact flat/local Ward quotient basis (Q,zeta):

    H = [[A(w2,k2), B(w2,k2)],
         [B(w2,k2), C(w2,k2)]]

with Newtonian-gauge flat reference Q=Psi, zeta=-Phi.  Given one source vector
(j_Q,j_zeta), this gate solves H y = -j, computes the determinant, simple
omega^2 pole candidates and inverse-kernel residue matrices.

Physical interpretation is fail-closed.  Pole/response formulas are always
algebraically available, but `physical_interpretation_allowed` is true only
when the packet explicitly certifies a theory-specific connected history,
physical omega, Ward reduction and the frozen conserved source convention.
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
    'physical_omega_certified',
    'ward_reduction_certified',
    'conserved_probe_frozen',
    'background_and_scale_convention_frozen',
)
REQ_HASHES=(
    'connected_history_hash',
    'ward_certificate_hash',
    'source_convention_hash',
    'background_convention_hash',
)


def expr(x:Any)->sp.Expr:
    if isinstance(x,bool): return sp.Integer(int(x))
    if isinstance(x,int): return sp.Integer(x)
    if isinstance(x,float): return sp.Rational(str(x))
    if isinstance(x,str): return sp.sympify(x,locals={'w2':W2,'k2':K2})
    raise TypeError(x)


def s(x:sp.Expr)->str:
    return str(sp.factor(sp.simplify(x)))


def residue_matrix(H:sp.Matrix,det:sp.Expr,root:sp.Expr)->sp.Matrix|None:
    d=sp.simplify(sp.diff(det,W2).subs(W2,root))
    if d==0:
        return None
    adj=H.adjugate().applyfunc(lambda x:sp.simplify(x.subs(W2,root)))
    return sp.simplify(adj/d)


def classify_root(root:sp.Expr,R:sp.Matrix|None)->dict[str,Any]:
    out={'w2_root':s(root),'simple':R is not None}
    if R is None:
        out.update({'residue_matrix':None,'residue_eigenvalues':None,'ghost_test':'INDETERMINATE_MULTIPLE_POLE','tachyon_test':'INDETERMINATE','cs2':'INDETERMINATE'})
        return out
    eig=[]
    for ev,mult in R.eigenvals().items():
        eig.extend([sp.simplify(ev)]*int(mult))
    out['residue_matrix']=[[s(R[i,j]) for j in range(R.cols)] for i in range(R.rows)]
    out['residue_eigenvalues']=[s(x) for x in eig]
    nonzero=[x for x in eig if sp.simplify(x)!=0]
    if nonzero and all(x.is_positive is True for x in nonzero):
        out['ghost_test']='POSITIVE_NONZERO_RESIDUES'
    elif any(x.is_negative is True for x in nonzero):
        out['ghost_test']='NEGATIVE_RESIDUE_PRESENT'
    else:
        out['ghost_test']='SYMBOLIC_INDETERMINATE'

    r0=sp.simplify(root.subs(K2,0))
    if r0.is_nonnegative is True:
        out['tachyon_test']='NO_NEGATIVE_MASS2_AT_K0'
    elif r0.is_negative is True:
        out['tachyon_test']='NEGATIVE_W2_AT_K0_TACHYON'
    else:
        out['tachyon_test']='SYMBOLIC_INDETERMINATE'
    cs=sp.simplify(sp.diff(root,K2))
    out['cs2']=s(cs)
    out['mass2']=s(r0)
    return out


def analyze(packet:dict[str,Any])->dict[str,Any]:
    if packet.get('schema')!='BQG_SCALAR_WARD_KERNEL_V1':
        raise ValueError('schema must be BQG_SCALAR_WARD_KERNEL_V1')
    A,B,C=(expr(packet[k]) for k in ('A','B','C'))
    jQ,jZ=(expr(packet.get(k,0)) for k in ('j_Q','j_zeta'))
    H=sp.Matrix([[A,B],[B,C]])
    det=sp.factor(sp.simplify(H.det()))
    adj=H.adjugate()
    # H y=-j; use adj/det to avoid assuming invertibility at poles.
    numerator=sp.simplify(-adj*sp.Matrix([jQ,jZ]))
    Q_num,Z_num=numerator
    # Q=Psi and zeta=-Phi in the frozen flat reference.
    psi_num=sp.simplify(Q_num)
    phi_num=sp.simplify(-Z_num)
    weyl_num=sp.simplify(phi_num+psi_num)

    roots=[]
    try:
        raw=sp.solve(sp.Eq(det,0),W2)
    except Exception:
        raw=[]
    for root in raw:
        R=residue_matrix(H,det,root)
        roots.append(classify_root(sp.simplify(root),R))

    flags=dict(packet.get('physical_flags',{}));prov=dict(packet.get('provenance',{}))
    ready=all(flags.get(x) is True for x in REQ_FLAGS) and all(bool(prov.get(x)) for x in REQ_HASHES)
    return {
        'schema':'BQG_SCALAR_WARD_RESPONSE_RESULT_V1',
        'kernel':{'A':s(A),'B':s(B),'C':s(C),'determinant':s(det)},
        'source':{'j_Q':s(jQ),'j_zeta':s(jZ),'single_frozen_source_required':True},
        'response_common_denominator':s(det),
        'response_numerators':{
            'Psi':s(psi_num),
            'Phi':s(phi_num),
            'Phi_plus_Psi':s(weyl_num),
        },
        'omega2_poles':roots,
        'omega2_pole_count':len(roots),
        'physical_flags':flags,
        'provenance_complete':all(bool(prov.get(x)) for x in REQ_HASHES),
        'physical_interpretation_allowed':bool(ready),
        'science_status':'PHYSICAL_SCALAR_RESPONSE_ANALYZED' if ready else 'ALGEBRAIC_RESPONSE_ONLY_PHYSICAL_HISTORY_INCOMPLETE',
        'decision_rule':{
            'no_omega2_pole':'constraint/static modified-gravity response candidate; compare derived Psi and Weyl response from the same source',
            'simple_extra_pole':'candidate extra scalar only after positive residue, non-tachyonic mass, stable cs2 and source overlap checks',
            'negative_residue':'ghost candidate / physical rejection',
            'negative_w2_at_k0':'tachyon candidate / physical rejection',
        },
        'claim_boundary':'Flat/local Ward-kernel analyzer. A pole is not called dark matter unless the packet is theory-specific physical history data and all stability/clustering/lensing requirements are separately satisfied.'
    }


def selftest()->dict[str,Any]:
    tests={}
    baseflags={x:False for x in REQ_FLAGS}
    # GR-like static scalar constraint response: no w2 pole.
    gr=analyze({'schema':'BQG_SCALAR_WARD_KERNEL_V1','A':'k2','B':0,'C':'2*k2','j_Q':1,'j_zeta':1,'physical_flags':baseflags,'provenance':{}})
    tests['gr_like_static_has_no_omega2_pole']=gr['omega2_pole_count']==0
    tests['gr_like_is_fail_closed_without_history']=gr['physical_interpretation_allowed'] is False

    # Modified static response, still no new propagating scalar pole.
    mg=analyze({'schema':'BQG_SCALAR_WARD_KERNEL_V1','A':'3*k2/2','B':'k2/5','C':'7*k2/4','j_Q':1,'j_zeta':1,'physical_flags':baseflags,'provenance':{}})
    tests['modified_static_has_no_omega2_pole']=mg['omega2_pole_count']==0

    # Healthy extra scalar in zeta channel.
    healthy=analyze({'schema':'BQG_SCALAR_WARD_KERNEL_V1','A':'k2','B':0,'C':'w2-k2/4-2','j_Q':1,'j_zeta':1,'physical_flags':baseflags,'provenance':{}})
    tests['healthy_has_one_pole']=healthy['omega2_pole_count']==1
    hp=healthy['omega2_poles'][0]
    tests['healthy_positive_residue']=hp['ghost_test']=='POSITIVE_NONZERO_RESIDUES'
    tests['healthy_no_tachyon']=hp['tachyon_test']=='NO_NEGATIVE_MASS2_AT_K0'
    tests['healthy_cs2_one_quarter']=hp['cs2']=='1/4'
    tests['healthy_mass2_two']=hp['mass2']=='2'

    # Ghost control: sign flip of kinetic term.
    ghost=analyze({'schema':'BQG_SCALAR_WARD_KERNEL_V1','A':'k2','B':0,'C':'-w2+k2/4+2','j_Q':1,'j_zeta':1,'physical_flags':baseflags,'provenance':{}})
    tests['ghost_negative_residue_detected']=ghost['omega2_poles'][0]['ghost_test']=='NEGATIVE_RESIDUE_PRESENT'

    # Tachyon control with positive kinetic residue but negative mass^2.
    tach=analyze({'schema':'BQG_SCALAR_WARD_KERNEL_V1','A':'k2','B':0,'C':'w2-k2/4+2','j_Q':1,'j_zeta':1,'physical_flags':baseflags,'provenance':{}})
    tests['tachyon_detected']=tach['omega2_poles'][0]['tachyon_test']=='NEGATIVE_W2_AT_K0_TACHYON'

    # Complete synthetic provenance demonstrates only the fail-open mechanism.
    f={x:True for x in REQ_FLAGS};p={x:'synthetic' for x in REQ_HASHES}
    ready=analyze({'schema':'BQG_SCALAR_WARD_KERNEL_V1','A':'k2','B':0,'C':'w2-k2/4-2','j_Q':1,'j_zeta':1,'physical_flags':f,'provenance':p})
    tests['complete_synthetic_packet_allows_interpretation']=ready['physical_interpretation_allowed'] is True

    return {'schema':'BQG_SCALAR_WARD_RESPONSE_SELFTEST_V1','passed':bool(all(tests.values())),'tests':tests,'controls':{'gr_like':gr,'modified_static':mg,'healthy_extra_scalar':healthy,'ghost':ghost,'tachyon':tach},'claim_boundary':'Synthetic controls test classification logic only; they are not BQG predictions.'}


def main()->int:
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--packet',type=Path);ap.add_argument('--output',type=Path);a=ap.parse_args()
    out={'selftest':selftest()}
    if a.packet: out['production']=analyze(json.loads(a.packet.read_text(encoding='utf-8')))
    out['passed']=bool(out['selftest']['passed'])
    txt=json.dumps(out,indent=2);print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
