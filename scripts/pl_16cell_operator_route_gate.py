#!/usr/bin/env python3
"""Operator-first route HDA on the independent 16-cell PL-S3 habitat.

Build the exact local flux-Gram operators from the PL-oriented four-valent
Peter-Weyl intertwiner bases at adjacent 16-cell dual nodes 0 and 1.  Quantize
the shared metric before the square root and run the exact sparse-Fourier route
commutator/half-density target regression.

This is deliberately independent of the historical K5-oriented-intertwiner
wrapper.  It tests whether the positive route sector survives the first
non-K5 PL habitat.
"""
from __future__ import annotations
import argparse,json,math,sys
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
import k5_peter_weyl_safe_hda_column as PW
import operator_route_sparse_fourier as SF
from pl_dual_complex import DualComplex,seed_16cell_boundary
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean

EPS=(0.25,0.125,0.0625,0.03125,0.015625)
LOCAL_SLOTS=(1,2)


def normalize(v):
    n=math.sqrt(float(np.vdot(v,v).real))
    if n<1e-15: raise RuntimeError('zero intertwiner')
    return v/n


def apply_dot(T,a,b,ls):
    out=np.zeros_like(T,dtype=complex)
    ma=PW.spin_mats_cached(ls[a]);mb=PW.spin_mats_cached(ls[b])
    for c in range(3):
        x=PW.apply_axis_np(T,b,mb[c]);x=PW.apply_axis_np(x,a,ma[c]);out+=x
    return out


def local_Q(G,spins,v):
    ls=G.local_spins(spins,v)
    allowed=tuple(PW.allowed_k2_t(*ls))
    basis=tuple(normalize(G.oriented_intertwiner(v,ls,K)) for K in allowed)
    Q=[[np.zeros((len(allowed),len(allowed)),complex) for _ in range(2)] for _ in range(2)]
    for a,la in enumerate(LOCAL_SLOTS):
        for b,lb in enumerate(LOCAL_SLOTS):
            for j,ket in enumerate(basis):
                x=apply_dot(ket,la,lb,ls)
                for i,bra in enumerate(basis): Q[a][b][i,j]=np.vdot(bra,x)
            Q[a][b]=.5*(Q[a][b]+Q[a][b].conj().T)
    return allowed,Q


def shared_Q(G,spins):
    a0,q0=local_Q(G,spins,0);a1,q1=local_Q(G,spins,1)
    I0=np.eye(len(a0));I1=np.eye(len(a1));Q=[[None,None],[None,None]]
    for a in range(2):
        for b in range(2):
            A=.5*(np.kron(q0[a][b],I1)+np.kron(I0,q1[a][b]))
            Q[a][b]=.5*(A+A.conj().T)
    return a0,a1,q0,q1,Q


def fit(vals):
    e=[];v=[]
    for x,y in zip(EPS,vals):
        if y>1e-14: e.append(x);v.append(y)
    if len(v)<3:return None
    return float(np.polyfit(np.log(e),np.log(v),1)[0])


def min_symbol(Q,modes):
    m=math.inf
    for k in modes:
        A=(k[0]*k[0]*Q[0][0]+k[0]*k[1]*(Q[0][1]+Q[1][0])+k[1]*k[1]*Q[1][1])
        m=min(m,float(np.linalg.eigvalsh(.5*(A+A.conj().T)).min()))
    return m


def one(Q,eps,carrier,index):
    N,M=SF.frozen_lapses(eps)
    d=Q[0][0].shape[0]
    psi=SF.carrier_state(d,carrier,index)
    RR=SF.route_commutator(Q,N,M,psi,eps)
    D=SF.route_target(Q,N,M,psi,eps)
    # historical sign convention is RR + D -> 0
    return SF.relative_defect(RR,D,+1),set(RR)|set(D)|set(psi)


def run():
    D=DualComplex(seed_16cell_boundary());G=PLPeterWeylEuclidean(D)
    spins=(1,)*len(G.EDGES)
    a0,a1,q0,q1,Q=shared_Q(G,spins)
    rows={};all_modes=set();mineig=math.inf
    labels=[]
    for i,K0 in enumerate(a0):
        for j,K1 in enumerate(a1): labels.append((i*len(a1)+j,K0,K1))
    for idx,K0,K1 in labels:
        vals=[]
        for e in EPS:
            x,modes=one(Q,e,8,idx);vals.append(x);all_modes|=modes
        p=fit(vals)
        rows[f'K0={K0},K1={K1}']={'defects':vals,'endpoint':vals[-1],'epsilon_exponent':p}
    carrier={}
    for k in (2,4,8,16):
        vals=[]
        for e in EPS:
            x,modes=one(Q,e,k,0);vals.append(x);all_modes|=modes
        carrier[str(k)]={'defects':vals,'endpoint':vals[-1],'epsilon_exponent':fit(vals)}
    mineig=min_symbol(Q,all_modes)
    exps=[r['epsilon_exponent'] for r in rows.values() if r['epsilon_exponent'] is not None]
    ends=[r['endpoint'] for r in rows.values()]
    off=math.sqrt(sum(np.linalg.norm(A-np.diag(np.diag(A)))**2 for row in Q for A in row))
    checks={
      'adjacent_nodes':1 in {D.neighbor[(0,r)] for r in range(4)},
      'two_by_two_local_K_spaces':len(a0)==2 and len(a1)==2,
      'shared_Q_operator_valued':off>1e-4,
      'symbol_PSD_roundoff':mineig>-1e-10,
      'all_endpoints_below_2e-5':max(ends)<2e-5,
      'all_nonzero_exponents_near_one':bool(exps) and min(exps)>.99 and max(exps)<1.01,
      'carrier16_better_than_carrier2':carrier['16']['endpoint']<carrier['2']['endpoint']
    }
    return {
      'status':'operator-first route HDA on independent 16-cell PL-S3 habitat',
      'passed':all(checks.values()),'nodes':[0,1],'local_slots':list(LOCAL_SLOTS),
      'allowed_K2_node0':list(a0),'allowed_K2_node1':list(a1),
      'epsilon':list(EPS),'basis_rows':rows,'carrier_rows':carrier,
      'minimum_symbol_eigenvalue':mineig,'shared_Q_offdiagonal_norm':off,
      'checks':checks,
      'interpretation':'The positive matrix-valued route normal retains its ~linear HDA residual on the first independent non-K5 PL-S3 habitat using PL-oriented intertwiner bases.',
      'scope_note':'Fixed all-j=1/2 4x4 route block at adjacent 16-cell nodes. Spin-changing 16-cell route blocks and full geometry+route commutator remain next.'
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path)
    a=ap.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
