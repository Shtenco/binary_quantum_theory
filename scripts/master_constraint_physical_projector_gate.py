#!/usr/bin/env python3
"""Finite master-constraint physical-projector theorem selftest.

Pure operator-algebra gate. It verifies the finite statements used by
MASTER_CONSTRAINT_PHYSICAL_PROJECTOR.md; it is not the full gravity projector.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np
TOL=2e-10

def proj(Q): return Q@Q.conj().T

def build(seed=1729,n=8,kdim=2,m=4):
    rng=np.random.default_rng(seed)
    X=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
    Q,_=np.linalg.qr(X); K=Q[:,:kdim]; R=Q[:,kdim:]; P=proj(K)
    C=[]
    for a in range(m):
        Y=rng.normal(size=(n-kdim,n-kdim))+1j*rng.normal(size=(n-kdim,n-kdim))
        H=.5*(Y+Y.conj().T)+(2.5+.4*a)*np.eye(n-kdim)
        C.append(R@H@R.conj().T)
    return C,P,rng

def pos_metric(rng,m,i):
    X=rng.normal(size=(m,m))+1j*rng.normal(size=(m,m))
    G=X.conj().T@X+(.35+.1*i)*np.eye(m)
    return .5*(G+G.conj().T)

def master(C,G):
    M=np.zeros_like(C[0],dtype=complex)
    for a,Ca in enumerate(C):
        for b,Cb in enumerate(C): M+=Ca.conj().T@(G[a,b]*Cb)
    return .5*(M+M.conj().T)

def heat(M,T):
    e,U=np.linalg.eigh(M); return (U*np.exp(-T*e))@U.conj().T

def run(seed=1729):
    C,Pexp,rng=build(seed); ps=[]; rows=[]; heats=[]; ok=True
    cres=max(float(np.linalg.norm(c@Pexp)) for c in C)
    for gi in range(4):
        G=pos_metric(rng,len(C),gi); M=master(C,G); e,U=np.linalg.eigh(M)
        sc=max(float(np.max(np.abs(e))),1.); z=e<1e-10*sc
        P0=proj(U[:,z]); gap=float(np.min(e[~z])); perr=float(np.linalg.norm(P0-Pexp))
        cut=.5*gap; Pw=proj(U[:,e<cut]); werr=float(np.linalg.norm(Pw-P0))
        good=float(np.min(e))>-TOL*sc and int(z.sum())==2 and perr<2e-9 and werr<2e-10
        ok &= good; ps.append(P0)
        rows.append({"metric_index":gi,"G_eigenvalue_min":float(np.min(np.linalg.eigvalsh(G))),"master_eigenvalue_min":float(np.min(e)),"master_gap":gap,"zero_rank":int(z.sum()),"projector_error_to_common_kernel":perr,"spectral_window_cutoff":cut,"spectral_window_projector_error":werr,"passed":bool(good)})
        for T in (.002,.005,.01):
            obs=float(np.linalg.norm(heat(M,T)-P0,2)); pred=float(np.exp(-T*gap)); err=abs(obs-pred); hp=err<3e-10*max(1.,pred)
            ok &= hp; heats.append({"metric_index":gi,"T":T,"observed_operator_norm_error":obs,"predicted_exp_minus_T_gap":pred,"absolute_error":err,"passed":bool(hp)})
    pair=max(float(np.linalg.norm(ps[i]-ps[j])) for i in range(4) for j in range(i+1,4))
    ok &= pair<2e-9 and cres<2e-10
    return {"status":"exact finite master-constraint physical-projector selftest","passed":bool(ok),"seed":seed,"hilbert_dimension":8,"constraint_count":4,"prescribed_common_kernel_dimension":2,"common_kernel_constraint_residual":cres,"max_pairwise_zero_projector_difference_across_positive_G":pair,"positive_metric_tests":rows,"heat_kernel_tests":heats,"theorem":"for positive definite G, <psi|M_G|psi>=||G^(1/2) C psi||^2, hence ker(M_G)=intersection ker(C_A)","scope":"operator-algebra gate only; the gravity application still needs the full regulated constraint family and a controlled refinement/rigging limit"}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--seed',type=int,default=1729); ap.add_argument('--output',type=Path,default=Path('verification_results/MASTER_CONSTRAINT_PHYSICAL_PROJECTOR.json')); a=ap.parse_args()
    out=run(a.seed); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2)); return 0 if out['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
