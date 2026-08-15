#!/usr/bin/env python3
"""Exact 4x4 two-node operator-first route-normal HDA gate.

The physical sine two-node HDA gate uses the shared metric of nodes 0 and 1.
This gate quantizes that same shared metric before taking the square root.
On the all-j=1/2 sector with K2=K3=K4=0, the geometry block is

    (K0,K1) in {(0,0),(0,2),(2,0),(2,2)}.

For local route legs (1,2), construct exact Peter-Weyl flux matrices Q_v^{ab}
and then

    Q_shared^{ab}=1/2(Q_0^{ab} tensor I + I tensor Q_1^{ab}).

The route operator is

    Omega(p)=sqrt_operator(Q_shared^{ab} p_a p_b),
    R[N]=1/2{N,Omega}.

No geometry expectation value is taken before the spectral square root.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import k5_peter_weyl_safe_hda_column as PW

EPS=(0.25,0.125,0.0625,0.03125,0.015625)
LOCAL_LEGS=(1,2)


def normalize(v):
    n=math.sqrt(float(np.vdot(v,v).real))
    if n<1e-15:
        raise RuntimeError('zero-norm intertwiner')
    return v/n


def local_basis(v):
    ls=(1,1,1,1)
    return [normalize(PW.oriented_intertwiner(v,ls,K)) for K in (0,2)]


def apply_dot(T,leg_a,leg_b,ls=(1,1,1,1)):
    out=np.zeros_like(T,dtype=complex)
    ma=PW.spin_mats_cached(ls[leg_a]); mb=PW.spin_mats_cached(ls[leg_b])
    for c in range(3):
        tmp=PW.apply_axis_np(T,leg_b,mb[c])
        tmp=PW.apply_axis_np(tmp,leg_a,ma[c])
        out+=tmp
    return out


def local_flux_gram_operator(v):
    basis=local_basis(v)
    Q=[[np.zeros((2,2),complex) for _ in range(2)] for _ in range(2)]
    legs=LOCAL_LEGS
    for a,la in enumerate(legs):
        for b,lb in enumerate(legs):
            for j,ket in enumerate(basis):
                acted=apply_dot(ket,la,lb)
                for i,bra in enumerate(basis):
                    Q[a][b][i,j]=np.vdot(bra,acted)
            Q[a][b]=0.5*(Q[a][b]+Q[a][b].conj().T)
    return Q


def shared_flux_gram_operator():
    q0=local_flux_gram_operator(0)
    q1=local_flux_gram_operator(1)
    I2=np.eye(2,dtype=complex)
    Q=[[None,None],[None,None]]
    for a in range(2):
        for b in range(2):
            Q[a][b]=0.5*(np.kron(q0[a][b],I2)+np.kron(I2,q1[a][b]))
            Q[a][b]=0.5*(Q[a][b]+Q[a][b].conj().T)
    return q0,q1,Q


def sqrt_psd(A):
    A=0.5*(A+A.conj().T)
    vals,U=np.linalg.eigh(A)
    if vals.min() < -1e-9:
        raise RuntimeError(f'Q(p) not PSD: {vals}')
    vals=np.maximum(vals,0.0)
    return (U*np.sqrt(vals))@U.conj().T


def setup(L,epsilon):
    y=2*np.pi*np.arange(L)/L
    Y,Z=np.meshgrid(y,y,indexing='ij')
    k=np.fft.fftfreq(L,d=1.0/L)
    KY,KZ=np.meshgrid(k,k,indexing='ij')
    def dvec(f,axis):
        K=KY if axis==0 else KZ
        return np.fft.ifft2((1j*K/epsilon)[None,:,:]*np.fft.fft2(f,axes=(-2,-1)),axes=(-2,-1))
    def dscalar(f,axis):
        K=KY if axis==0 else KZ
        return np.fft.ifft2((1j*K/epsilon)*np.fft.fft2(f))
    return Y,Z,KY,KZ,dvec,dscalar


def omega_symbols(Q,KY,KZ,epsilon):
    L=KY.shape[0]
    out=np.zeros((L,L,4,4),complex)
    mineig=math.inf
    for x in range(L):
        for y in range(L):
            p=(KY[x,y],KZ[x,y])
            A=(p[0]*p[0]*Q[0][0]
               +p[0]*p[1]*(Q[0][1]+Q[1][0])
               +p[1]*p[1]*Q[1][1])
            vals=np.linalg.eigvalsh(0.5*(A+A.conj().T))
            mineig=min(mineig,float(vals.min()))
            out[x,y]=sqrt_psd(A)/epsilon
    return out,mineig


def omega_apply(f,Oms):
    F=np.fft.fft2(f,axes=(-2,-1))
    return np.fft.ifft2(np.einsum('xyij,jxy->ixy',Oms,F),axes=(-2,-1))


def route_apply(A,f,Oms):
    return 0.5*(A[None,:,:]*omega_apply(f,Oms)+omega_apply(A[None,:,:]*f,Oms))


def route_target(Q,N,M,f,dvec,dscalar):
    dN=[dscalar(N,a) for a in range(2)]
    dM=[dscalar(M,a) for a in range(2)]
    one=[N*dM[a]-M*dN[a] for a in range(2)]
    L=N.shape[0]
    beta=np.zeros((2,4,4,L,L),complex)
    for a in range(2):
        for b in range(2):
            beta[a]+=Q[a][b][:,:,None,None]*one[b][None,None,:,:]
    df=[dvec(f,a) for a in range(2)]
    out=np.zeros_like(f)
    for a in range(2):
        out+=np.einsum('ijxy,jxy->ixy',beta[a],df[a])
    div=np.zeros((4,4,L,L),complex)
    for a in range(2):
        for i in range(4):
            for j in range(4):
                div[i,j]+=dscalar(beta[a,i,j],a)
    out+=0.5*np.einsum('ijxy,jxy->ixy',div,f)
    return out


def normalized(v):
    x=np.asarray(v,dtype=complex)
    return x/np.linalg.norm(x)


def one_case(Q,L,epsilon,carrier,spinor):
    Y,Z,KY,KZ,dvec,dscalar=setup(L,epsilon)
    Oms,mineig=omega_symbols(Q,KY,KZ,epsilon)
    N=0.9+epsilon*(0.13*np.sin(Y)+0.07*np.cos(Z))
    M=1.1+epsilon*(0.11*np.cos(Y)+0.09*np.sin(Z))
    scalar=np.exp(1j*(carrier*Y+(carrier-1)*Z))
    f=spinor[:,None,None]*scalar[None,:,:]
    RR=route_apply(N,route_apply(M,f,Oms),Oms)-route_apply(M,route_apply(N,f,Oms),Oms)
    D=route_target(Q,N,M,f,dvec,dscalar)
    defect=float(np.linalg.norm(RR+D)/max(np.linalg.norm(D),1e-30))
    return defect,mineig


def fit_power(vals):
    return float(np.polyfit(np.log(np.asarray(EPS)),np.log(np.asarray(vals)),1)[0])


def diagonal_expectation(Q,idx):
    return np.array([[float(Q[a][b][idx,idx].real) for b in range(2)] for a in range(2)])


def run(L=48):
    q0,q1,Q=shared_flux_gram_operator()
    spinors={
        'K0K0':normalized([1,0,0,0]),
        'K0K2':normalized([0,1,0,0]),
        'K2K0':normalized([0,0,1,0]),
        'K2K2':normalized([0,0,0,1]),
        'equal':normalized([1,1,1,1]),
        'phase':normalized([1,1j,-1,0.5j]),
        'random':normalized([0.5+0.1j,-0.2+0.6j,0.7-0.3j,-0.4+0.2j]),
    }
    state_rows={}; min_q=math.inf
    for name,s in spinors.items():
        vals=[]
        for e in EPS:
            d,m=one_case(Q,L,e,8,s); vals.append(d); min_q=min(min_q,m)
        state_rows[name]={'defects':vals,'endpoint':vals[-1],'epsilon_exponent':fit_power(vals)}

    carrier_rows={}
    for k in (2,4,8,16):
        vals=[]
        for e in EPS:
            d,m=one_case(Q,L,e,k,spinors['K0K0']); vals.append(d); min_q=min(min_q,m)
        carrier_rows[str(k)]={'defects':vals,'endpoint':vals[-1],'epsilon_exponent':fit_power(vals)}

    # On the initial K0K0 basis vector, the diagonal shared metric must agree
    # exactly with the expectation-metric construction used by the historical
    # sine two-node gate.
    expected_initial=0.75*np.eye(2)
    initial_diag=diagonal_expectation(Q,0)
    diag_error=float(np.linalg.norm(initial_diag-expected_initial))

    # Nontriviality: operator-first shared Q must have off-diagonal geometry
    # matrix elements, otherwise this would collapse back to expectation-first.
    offdiag_norm=math.sqrt(sum(
        np.linalg.norm(A-np.diag(np.diag(A)))**2
        for row in Q for A in row
    ))

    exps=[r['epsilon_exponent'] for r in state_rows.values()]
    endpoints=[r['endpoint'] for r in state_rows.values()]
    cexps=[r['epsilon_exponent'] for r in carrier_rows.values()]
    checks={
        'initial_diagonal_metric_matches_historical_shared_Q':diag_error<1e-12,
        'shared_Q_is_genuinely_operator_valued':offdiag_norm>1e-4,
        'spectral_Qp_positive':min_q>-1e-8,
        'all_state_endpoints_below_2e-6':max(endpoints)<2e-6,
        'all_state_exponents_near_one':min(exps)>0.99 and max(exps)<1.01,
        'all_carrier_exponents_near_one':min(cexps)>0.99 and max(cexps)<1.01,
        'primary_endpoint_below_1e-6':state_rows['K0K0']['endpoint']<1e-6,
        'carrier16_better_than_carrier2':carrier_rows['16']['endpoint']<carrier_rows['2']['endpoint'],
    }
    return {
        'status':'exact two-node 4x4 operator-first shared-route HDA gate',
        'passed':all(checks.values()),
        'nodes':[0,1],
        'local_route_legs':list(LOCAL_LEGS),
        'geometry_basis':['K0=0,K1=0','K0=0,K1=2','K0=2,K1=0','K0=2,K1=2'],
        'L':L,'epsilon':list(EPS),
        'local_Q0':[[q0[a][b].real.tolist() for b in range(2)] for a in range(2)],
        'local_Q1':[[q1[a][b].real.tolist() for b in range(2)] for a in range(2)],
        'shared_Q':[[Q[a][b].real.tolist() for b in range(2)] for a in range(2)],
        'initial_diagonal_shared_metric':initial_diag.tolist(),
        'initial_metric_error_from_0p75I':diag_error,
        'shared_Q_offdiagonal_geometry_norm':offdiag_norm,
        'minimum_Qp_eigenvalue':min_q,
        'state_robustness_carrier8':state_rows,
        'carrier_robustness_K0K0':carrier_rows,
        'checks':checks,
        'interpretation':(
            'The operator-first route normal remains HDA-consistent on the exact two-node logical geometry block used by the next full GxR construction. '
            'It is genuinely matrix-valued in K0,K1 and therefore is not the historical expectation-first surrogate.'
        ),
        'scope':'Fixed all-j=1/2 two-node geometry block. Spin-changing block completion is the next step for the full H_E+H_L+R commutator.',
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--L',type=int,default=48)
    ap.add_argument('--output',type=Path)
    a=ap.parse_args(); out=run(a.L); text=json.dumps(out,indent=2,sort_keys=True); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
