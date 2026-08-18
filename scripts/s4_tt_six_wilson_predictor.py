#!/usr/bin/env python3
"""Evaluate the complete six-Wilson tetrahedral TT quartic prediction.

Input:
  c1...c6  coefficients of the canonical W1...W6 basis,
  n         propagation direction.

Output:
  the real 2x2 TT quartic matrix in a deterministic plus/cross frame,
  its basis-independent eigenvalues e4_1,e4_2,
  polarization mean/splitting,
  and optional real-physics factors after one common scale is supplied.

The executable also contains exact/numerical self-tests for the three nested
reference directions: rotational scalar, scalar cubic Q4, and the single Qtet
splitter.  No experimental data are used.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import numpy as np

ISO = np.asarray([6,24,6,36,-9,18], float)
Q4V = np.asarray([12/5,-57/5,12/5,-48/5,27/5,-54/5], float)
QTET = np.asarray([18/5,-33/5,-12/5,-72/5,48/5,24/5], float)
TOL = 3e-12


def normalize(v):
    v=np.asarray(v,float)
    q=float(np.linalg.norm(v))
    if q<=0: raise ValueError('zero direction')
    return v/q


def tt_basis(n):
    """Deterministic orthonormal Frobenius TT plus/cross basis."""
    n=normalize(n)
    axes=np.eye(3)
    seed=min(axes,key=lambda a:abs(float(a@n)))
    p=seed-n*float(seed@n);p=normalize(p)
    q=normalize(np.cross(n,p))
    hp=(np.outer(p,p)-np.outer(q,q))/math.sqrt(2.0)
    hx=(np.outer(p,q)+np.outer(q,p))/math.sqrt(2.0)
    return hp,hx


def W_values(h,k):
    """Canonical W1...W6 quadratic forms for real symmetric h and k."""
    k=np.asarray(k,float)
    d=np.diag(h)
    hxy,hxz,hyz=float(h[0,1]),float(h[0,2]),float(h[1,2])
    k2=k*k;k4=k2*k2
    w1=sum(d[i]**2*k4[j] for i in range(3) for j in range(3) if i!=j)/6.0
    w2=sum(d[i]**2*k4[i] for i in range(3))/3.0
    w3=(hxy*hxy*k4[2]+hxz*hxz*k4[1]+hyz*hyz*k4[0])/3.0
    w4=(hxy*hxy*(k4[0]+k4[1])+hxz*hxz*(k4[0]+k4[2])+hyz*hyz*(k4[1]+k4[2]))/6.0
    w5=(d[0]**2*k2[1]*k2[2]+d[1]**2*k2[0]*k2[2]+d[2]**2*k2[0]*k2[1])/3.0
    w6=sum(d[i]**2*k2[i]*k2[j] for i in range(3) for j in range(3) if i!=j)/6.0
    return np.asarray([w1,w2,w3,w4,w5,w6],float)


def basis_matrices(n):
    """Return six 2x2 symmetric matrices whose quadratic forms are W_r."""
    hp,hx=tt_basis(n);k=normalize(n)
    vp=W_values(hp,k);vx=W_values(hx,k);vsum=W_values(hp+hx,k)
    cross=(vsum-vp-vx)/2.0
    mats=[]
    for r in range(6):
        mats.append(np.asarray([[vp[r],cross[r]],[cross[r],vx[r]]],float))
    return np.asarray(mats),hp,hx


def evaluate(c,n):
    c=np.asarray(c,float)
    if c.shape!=(6,):raise ValueError('need six Wilson coefficients')
    nn=normalize(n)
    mats,hp,hx=basis_matrices(nn)
    M=np.tensordot(c,mats,axes=(0,0))
    M=(M+M.T)/2.0
    ev=np.linalg.eigvalsh(M)[::-1]
    q4=float(np.sum(nn**4)-3/5)
    return {
        'direction_unit':nn.tolist(),
        'TT_plus_tensor':hp.tolist(),
        'TT_cross_tensor':hx.tolist(),
        'quartic_TT_matrix':M.tolist(),
        'e4_eigenvalues_desc':ev.tolist(),
        'e4_mean':float(np.mean(ev)),
        'e4_split':float(ev[0]-ev[1]),
        'Q4_cubic':q4,
    }


def physicalize(result,lambda_R_eff=None,E_over_EP=None,L_over_lP=None):
    if lambda_R_eff is None:
        return None
    lam=float(lambda_R_eff)
    e=np.asarray(result['e4_eigenvalues_desc'],float)
    out={
      'lambda_R_eff':lam,
      'A4_times_EP2':(8*math.pi*lam*e).tolist(),
      'definition_A4':'A4_sigma = (A4_times_EP2)_sigma / E_P^2',
    }
    if E_over_EP is not None:
        x=float(E_over_EP)
        out['E_over_EP']=x
        out['delta_v_over_c']=(12*math.pi*lam*e*x*x).tolist()
        out['polarization_delta_v_over_c']=float(12*math.pi*lam*(e[0]-e[1])*x*x)
        if L_over_lP is not None:
            L=float(L_over_lP)
            out['L_over_lP']=L
            out['delta_phase']=(-4*math.pi*lam*e*L*x**3).tolist()
            out['polarization_delta_phase']=float(-4*math.pi*lam*(e[0]-e[1])*L*x**3)
    return out


def selftest():
    dirs={'100':(1,0,0),'110':(1,1,0),'111':(1,1,1),'120':(1,2,0),'generic':(2,3,5)}
    rows={};max_iso=0.0;max_q4=0.0
    for name,n in dirs.items():
        ri=evaluate(ISO,n);rq=evaluate(Q4V,n)
        max_iso=max(max_iso,max(abs(x-1.0) for x in ri['e4_eigenvalues_desc']))
        max_q4=max(max_q4,max(abs(x-rq['Q4_cubic']) for x in rq['e4_eigenvalues_desc']))
        rows[name]={'iso':ri,'scalar_Q4':rq}
    qt={name:evaluate(QTET,n) for name,n in {'100':(1,0,0),'110':(1,1,0),'111':(1,1,1)}.items()}
    targets={'100':np.asarray([3/5,-2/5]),'110':np.asarray([7/20,-2/5]),'111':np.asarray([-1/15,-1/15])}
    max_qtet=max(float(np.max(np.abs(np.asarray(qt[k]['e4_eigenvalues_desc'])-np.sort(v)[::-1]))) for k,v in targets.items())
    split=np.asarray([qt['100']['e4_split'],qt['110']['e4_split'],qt['111']['e4_split']])
    checks={
      'isotropic_vector_gives_identity_on_TT':max_iso<TOL,
      'scalar_Q4_vector_gives_Q4_times_identity':max_q4<TOL,
      'Qtet_high_symmetry_spectra':max_qtet<TOL,
      'Qtet_split_ratio_1_3over4_0':float(np.max(np.abs(split-np.asarray([1,.75,0]))))<TOL,
    }
    return {'passed':bool(all(checks.values())),'checks':checks,'max_iso_error':max_iso,'max_Q4_error':max_q4,'max_Qtet_error':max_qtet,'Qtet':qt}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--coefficients',nargs=6,type=float,metavar=('C1','C2','C3','C4','C5','C6'))
    p.add_argument('--direction',nargs=3,type=float,metavar=('NX','NY','NZ'))
    p.add_argument('--lambda-r-eff',type=float)
    p.add_argument('--energy-over-EP',type=float)
    p.add_argument('--L-over-lP',type=float)
    p.add_argument('--selftest',action='store_true')
    p.add_argument('--output',type=Path)
    a=p.parse_args()

    out={'status':'complete six-Wilson TT sky/polarization predictor','science_status':'OBSERVABLE_DICTIONARY'}
    if a.selftest or a.coefficients is None:
        out['selftest']=selftest()
    if a.coefficients is not None:
        if a.direction is None:p.error('--direction is required with --coefficients')
        r=evaluate(a.coefficients,a.direction)
        out['coefficients']=a.coefficients
        out['prediction']=r
        ph=physicalize(r,a.lambda_r_eff,a.energy_over_EP,a.L_over_lP)
        if ph is not None:out['physicalization']=ph
    out['passed']=bool(out.get('selftest',{'passed':True})['passed'])
    text=json.dumps(out,indent=2);print(text)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__=='__main__':raise SystemExit(main())
