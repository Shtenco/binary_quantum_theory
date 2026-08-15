#!/usr/bin/env python3
"""Operator-first logical route-normal HDA gate.

This gate tests the linear quantum candidate

    Omega = sqrt(Q^{ab} P_a P_b),
    R[N]  = 1/2 {N,Omega}

with the exact 2x2 logical flux matrices. It also includes a simple witness that
expectation-first square-root maps are nonlinear on superpositions.

The finite route calculation is exploratory (the values were inspected before
this file was frozen); it is a reproducible operator-selection/robustness gate,
not a preregistered held-out result.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],dtype=complex)
Z=np.array([[1,0],[0,-1]],dtype=complex)
Q00=0.75*I
Q11=0.75*I
Q01=-0.25*I-(math.sqrt(3)/4)*X+0.25*Z
Q=((Q00,Q01),(Q01,Q11))
EPS=(0.25,0.125,0.0625,0.03125,0.015625)


def sqrt_psd(A):
    vals,U=np.linalg.eigh((A+A.conj().T)/2)
    if vals.min() < -1e-10:
        raise RuntimeError(f'non-positive route block: {vals}')
    vals=np.maximum(vals,0.0)
    return (U*np.sqrt(vals))@U.conj().T


def setup(L,epsilon):
    y=2*np.pi*np.arange(L)/L
    Y,Zg=np.meshgrid(y,y,indexing='ij')
    k=np.fft.fftfreq(L,d=1.0/L)
    KY,KZ=np.meshgrid(k,k,indexing='ij')
    def dvec(f,axis):
        K=KY if axis==0 else KZ
        return np.fft.ifft2((1j*K/epsilon)[None,:,:]*np.fft.fft2(f,axes=(-2,-1)),axes=(-2,-1))
    def dscalar(f,axis):
        K=KY if axis==0 else KZ
        return np.fft.ifft2((1j*K/epsilon)*np.fft.fft2(f))
    return Y,Zg,KY,KZ,dvec,dscalar


def omega_symbols(KY,KZ,epsilon):
    L=KY.shape[0]
    out=np.zeros((L,L,2,2),dtype=complex)
    mineig=math.inf
    for i in range(L):
        for j in range(L):
            ky,kz=KY[i,j],KZ[i,j]
            A=ky*ky*Q00+2*ky*kz*Q01+kz*kz*Q11
            vals=np.linalg.eigvalsh((A+A.conj().T)/2)
            mineig=min(mineig,float(vals.min()))
            out[i,j]=sqrt_psd(A)/epsilon
    return out,mineig


def omega_apply(f,Oms):
    F=np.fft.fft2(f,axes=(-2,-1))
    return np.fft.ifft2(np.einsum('xyij,jxy->ixy',Oms,F),axes=(-2,-1))


def route_apply(A,f,Oms):
    return 0.5*(A[None,:,:]*omega_apply(f,Oms)+omega_apply(A[None,:,:]*f,Oms))


def target(N,M,f,dvec,dscalar):
    dN=[dscalar(N,a) for a in range(2)]
    dM=[dscalar(M,a) for a in range(2)]
    one=[N*dM[a]-M*dN[a] for a in range(2)]
    L=N.shape[0]
    beta=np.zeros((2,2,2,L,L),dtype=complex) # direction, geom row,col,x,y
    for a in range(2):
        for b in range(2):
            beta[a]+=Q[a][b][:,:,None,None]*one[b][None,None,:,:]
    df=[dvec(f,a) for a in range(2)]
    out=np.zeros_like(f)
    for a in range(2):
        out+=np.einsum('ijxy,jxy->ixy',beta[a],df[a])
    div=np.zeros((2,2,L,L),dtype=complex)
    for a in range(2):
        for i in range(2):
            for j in range(2):
                div[i,j]+=dscalar(beta[a,i,j],a)
    out+=0.5*np.einsum('ijxy,jxy->ixy',div,f)
    return out


def one_case(L,epsilon,carrier,spinor):
    Y,Zg,KY,KZ,dvec,dscalar=setup(L,epsilon)
    Oms,mineig=omega_symbols(KY,KZ,epsilon)
    N=0.9+epsilon*(0.13*np.sin(Y)+0.07*np.cos(Zg))
    M=1.1+epsilon*(0.11*np.cos(Y)+0.09*np.sin(Zg))
    scalar=np.exp(1j*(carrier*Y+(carrier-1)*Zg))
    f=spinor[:,None,None]*scalar[None,:,:]
    RR=(route_apply(N,route_apply(M,f,Oms),Oms)
        -route_apply(M,route_apply(N,f,Oms),Oms))
    D=target(N,M,f,dvec,dscalar)
    defect=float(np.linalg.norm(RR+D)/max(np.linalg.norm(D),1e-30))
    return defect,mineig


def fit_power(vals):
    return float(np.polyfit(np.log(np.asarray(EPS)),np.log(np.asarray(vals)),1)[0])


def normalized(v):
    v=np.asarray(v,dtype=complex)
    return v/np.linalg.norm(v)


def expectation_first_linearity_witness():
    Qw=np.diag([1.0,4.0]).astype(complex)
    e0=np.array([1.0,0.0],complex); e1=np.array([0.0,1.0],complex)
    plus=(e0+e1)/math.sqrt(2)
    def F(v):
        return math.sqrt(float(np.vdot(v,Qw@v).real))*v
    linear=(F(e0)+F(e1))/math.sqrt(2)
    direct=F(plus)
    return float(np.linalg.norm(direct-linear))


def sylvester_identity_check():
    tests=((1.0,0.3),(0.7,-0.2),(1.0,0.8))
    worst=0.0
    h=1e-6
    for p in tests:
        p=np.asarray(p,float)
        A=p[0]**2*Q00+2*p[0]*p[1]*Q01+p[1]**2*Q11
        Om=sqrt_psd(A)
        for c in (0,1):
            pp=p.copy(); pm=p.copy(); pp[c]+=h; pm[c]-=h
            Op=sqrt_psd(pp[0]**2*Q00+2*pp[0]*pp[1]*Q01+pp[1]**2*Q11)
            Omn=sqrt_psd(pm[0]**2*Q00+2*pm[0]*pm[1]*Q01+pm[1]**2*Q11)
            dO=(Op-Omn)/(2*h)
            lhs=Om@dO+dO@Om
            rhs=2*((Q00*p[0]+Q01*p[1]) if c==0 else (Q01*p[0]+Q11*p[1]))
            worst=max(worst,float(np.linalg.norm(lhs-rhs)))
    return worst


def run(L=48):
    spinors={
        'K0':normalized([1,0]),
        'K2':normalized([0,1]),
        'plus':normalized([1,1]),
        'plus_i':normalized([1,1j]),
        'random':normalized([0.6+0.2j,-0.3+0.7j]),
    }
    state_rows={}
    min_Q=math.inf
    for name,s in spinors.items():
        vals=[]
        for e in EPS:
            d,m=one_case(L,e,8,s); vals.append(d); min_Q=min(min_Q,m)
        state_rows[name]={'defects':vals,'endpoint':vals[-1],'epsilon_exponent':fit_power(vals)}

    carrier_rows={}
    for k in (2,4,8,16):
        vals=[]
        for e in EPS:
            d,m=one_case(L,e,k,spinors['K0']); vals.append(d); min_Q=min(min_Q,m)
        carrier_rows[str(k)]={'defects':vals,'endpoint':vals[-1],'epsilon_exponent':fit_power(vals)}

    linearity=expectation_first_linearity_witness()
    sylvester=sylvester_identity_check()
    primary=state_rows['K0']
    endpoints=[x['endpoint'] for x in state_rows.values()]
    exponents=[x['epsilon_exponent'] for x in state_rows.values()]
    cexponents=[x['epsilon_exponent'] for x in carrier_rows.values()]

    checks={
        'expectation_first_is_demonstrably_nonlinear':linearity>0.5,
        'Qp_positive_semidefinite_on_spectral_grid':min_Q>-1e-9,
        'matrix_sylvester_identity':sylvester<2e-8,
        'primary_endpoint_below_1e-6':primary['endpoint']<1e-6,
        'primary_epsilon_exponent_near_one':0.99<primary['epsilon_exponent']<1.01,
        'all_spinor_endpoints_below_1e-6':max(endpoints)<1e-6,
        'all_spinor_exponents_near_one':min(exponents)>0.99 and max(exponents)<1.01,
        'all_carrier_exponents_near_one':min(cexponents)>0.99 and max(cexponents)<1.01,
        'higher_carrier_endpoint_improves':carrier_rows['16']['endpoint']<carrier_rows['2']['endpoint'],
    }
    return {
        'status':'operator-first logical matrix route-normal HDA exploratory gate',
        'passed':all(checks.values()),
        'L':L,'epsilon':list(EPS),
        'flux_matrices':{
            'Q00':Q00.real.tolist(),'Q11':Q11.real.tolist(),'Q01':Q01.real.tolist(),
        },
        'expectation_first_linearity_witness_defect':linearity,
        'sylvester_finite_difference_worst_error':sylvester,
        'minimum_Qp_eigenvalue_on_checked_spectral_grids':min_Q,
        'state_robustness_carrier8':state_rows,
        'carrier_robustness_K0':carrier_rows,
        'historical_expectation_metric_endpoint_carrier8':8.264687442454126e-7,
        'operator_first_primary_endpoint_ratio_to_historical':primary['endpoint']/8.264687442454126e-7,
        'checks':checks,
        'interpretation':(
            'Operator-first spectral square root is linear/positive and preserves the matrix-valued HDA principal structure. '
            'The expectation-first construction is retained only as a semiclassical surrogate. '
            'This is not yet the geometry-changing two-node H_E+H_L+R operator-first HDA.'
        ),
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--L',type=int,default=48)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args(); out=run(args.L); text=json.dumps(out,indent=2,sort_keys=True); print(text)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
