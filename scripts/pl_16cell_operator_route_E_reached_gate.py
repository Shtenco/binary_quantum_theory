#!/usr/bin/env python3
"""Exhaustive operator-first route HDA on all node0 E-reached 16-cell sectors.

Generate the genuine production-zeroaware E_0^sine|Omega> column on the
independent 16-cell PL-S3 habitat.  For one adjacent pair (0,neighbor slot0),
deduplicate every local fixed-spin sector actually present with nonzero
amplitude, build its exact shared flux-Gram operator, and run the same
sparse-Fourier route commutator on every intertwiner-basis carrier.

Acceptance deliberately reuses the frozen independent-PL route thresholds:
endpoint <2e-5, nonzero epsilon exponent in (0.99,1.01), PSD modulo 1e-10.
"""
from __future__ import annotations
import argparse,json,math,sys
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_zeroaware_volume_migration_experiment as ZVM
import operator_route_sparse_fourier as SF
from pl_dual_complex import DualComplex,seed_16cell_boundary
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean

EPS=(.25,.125,.0625,.03125,.015625);LOCAL_SLOTS=(1,2)

def normalize(v):
    n=math.sqrt(float(np.vdot(v,v).real))
    if n<1e-15:raise RuntimeError('zero intertwiner')
    return v/n

def apply_dot(T,a,b,ls):
    out=np.zeros_like(T,dtype=complex);ma=PW.spin_mats_cached(ls[a]);mb=PW.spin_mats_cached(ls[b])
    for c in range(3):
        x=PW.apply_axis_np(T,b,mb[c]);x=PW.apply_axis_np(x,a,ma[c]);out+=x
    return out

def local_Q_ls(G,v,ls):
    allowed=tuple(PW.allowed_k2_t(*ls));basis=tuple(normalize(G.oriented_intertwiner(v,ls,K)) for K in allowed)
    Q=[[np.zeros((len(allowed),len(allowed)),complex) for _ in range(2)] for _ in range(2)]
    for a,la in enumerate(LOCAL_SLOTS):
      for b,lb in enumerate(LOCAL_SLOTS):
        for j,ket in enumerate(basis):
          x=apply_dot(ket,la,lb,ls)
          for i,bra in enumerate(basis):Q[a][b][i,j]=np.vdot(bra,x)
        Q[a][b]=.5*(Q[a][b]+Q[a][b].conj().T)
    return allowed,Q

def shared(G,v,w,ls0,ls1):
    a0,q0=local_Q_ls(G,v,ls0);a1,q1=local_Q_ls(G,w,ls1);I0=np.eye(len(a0));I1=np.eye(len(a1));Q=[[None,None],[None,None]]
    for a in range(2):
      for b in range(2):
        A=.5*(np.kron(q0[a][b],I1)+np.kron(I0,q1[a][b]));Q[a][b]=.5*(A+A.conj().T)
    return a0,a1,Q

def one(Q,eps,index):
    N,M=SF.frozen_lapses(eps);d=Q[0][0].shape[0];psi=SF.carrier_state(d,8,index);RR=SF.route_commutator(Q,N,M,psi,eps);D=SF.route_target(Q,N,M,psi,eps)
    return SF.relative_defect(RR,D,+1),set(RR)|set(D)|set(psi)
def fit(vals):
    x=[];y=[]
    for e,v in zip(EPS,vals):
        if v>1e-14:x.append(e);y.append(v)
    if len(y)<3:return None
    return float(np.polyfit(np.log(x),np.log(y),1)[0])
def min_symbol(Q,modes):
    m=math.inf
    for k in modes:
      A=k[0]*k[0]*Q[0][0]+k[0]*k[1]*(Q[0][1]+Q[1][0])+k[1]*k[1]*Q[1][1]
      m=min(m,float(np.linalg.eigvalsh(.5*(A+A.conj().T)).min()))
    return m

def run():
    ZVM.patch_and_clear();D=DualComplex(seed_16cell_boundary());G=PLPeterWeylEuclidean(D);seed=((1,)*len(G.EDGES),(0,)*D.n_tets)
    H=G.H_sine_basis(seed,0,3);w=D.neighbor[(0,0)]
    weights={}
    for key,amp in H.items():
        sec=(G.local_spins(key[0],0),G.local_spins(key[0],w));weights[sec]=weights.get(sec,0.0)+abs(amp)**2
    sectors=sorted(weights)
    rows=[];maxend=0.0;exps=[];mineig=math.inf;zeros=0;allm=set();total_carriers=0
    for ls0,ls1 in sectors:
        a0,a1,Q=shared(G,0,w,ls0,ls1);d=len(a0)*len(a1);sr=[];smodes=set()
        for idx in range(d):
            vals=[]
            for e in EPS:
                x,m=one(Q,e,idx);vals.append(x);smodes|=m;allm|=m
            p=fit(vals);end=vals[-1];maxend=max(maxend,end);total_carriers+=1
            if p is None:
                zeros+=1
                if max(vals)>1e-11:raise RuntimeError(('insufficient exponent points but not numerical zero',ls0,ls1,vals))
            else:exps.append(p)
            sr.append({'basis_index':idx,'defects':vals,'endpoint':end,'epsilon_exponent':p})
        ms=min_symbol(Q,smodes);mineig=min(mineig,ms)
        rows.append({'local_spins_node0':list(ls0),'local_spins_neighbor':list(ls1),'amplitude_weight':weights[(ls0,ls1)],
                     'allowed_K2_node0':list(a0),'allowed_K2_neighbor':list(a1),'block_dimension':d,'minimum_symbol_eigenvalue':ms,'carriers':sr})
    checks={'production_zeroaware_E_nonzero':len(H)>0,
            'all_26_reached_sectors_present':len(sectors)==26,
            'symbol_PSD_roundoff':mineig>-1e-10,
            'all_endpoints_below_2e-5':maxend<2e-5,
            'all_nonzero_exponents_near_one':bool(exps) and min(exps)>.99 and max(exps)<1.01}
    return {'status':'exhaustive operator-first route HDA on production E-reached 16-cell PL sectors','passed':bool(all(checks.values())),
            'source_node':0,'neighbor_node':w,'epsilon':list(EPS),'E_support':len(H),'E_norm':G.norm(H),
            'distinct_fixed_spin_sectors':len(sectors),'total_intertwiner_carriers':total_carriers,'numerical_zero_carriers':zeros,
            'minimum_symbol_eigenvalue':mineig,'max_endpoint_defect':maxend,
            'nonzero_exponent_min':min(exps) if exps else None,'nonzero_exponent_max':max(exps) if exps else None,
            'checks':checks,'sectors':rows,
            'interpretation':'The operator-first route normal is tested on every fixed-spin local sector that actually appears with nonzero production E amplitude on the first independent PL-S3 collective habitat.',
            'scope_note':'Node0 plus one adjacent pair after one E action. Full collective W0 still requires Hermitian S-reached sectors and the compressed multi-block route action.'}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
