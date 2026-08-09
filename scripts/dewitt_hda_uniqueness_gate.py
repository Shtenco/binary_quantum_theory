#!/usr/bin/env python3
"""HDA selects the GR DeWitt trace coefficient c=1/2.

For
  H_c[N] = int N[(pi_ab pi^ab-c pi^2)/sqrt(q)-sqrt(q) R],
the benchmark verifies numerically
  {H_c[N],H_c[M]} = D[beta]
    +4(c-1/2) int pi (N nabla^2 M-M nabla^2 N)
with the conventions of classical_hda_safe_window_gate.py.
"""
from __future__ import annotations
import argparse,json,math,sys
from pathlib import Path
import numpy as np
import torch

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
import classical_hda_safe_window_gate as HDA

torch.set_default_dtype(torch.float64)


def Hc(qc,pc,lapse,c,box=2*math.pi):
    q=HDA.coeff_to_mat(qc); p=HDA.coeff_to_mat(pc)
    sqrtq=torch.sqrt(torch.linalg.det(q))
    pcov=torch.einsum('...ai,...ij,...bj->...ab',q,p,q)
    pipi=torch.einsum('...ij,...ij->...',p,pcov)
    trp=torch.einsum('...ij,...ij->...',q,p)
    R=HDA.ricci_scalar(q,box)
    dx=box/q.shape[0]
    return torch.sum(lapse*((pipi-c*trp**2)/sqrtq-sqrtq*R))*dx**3


def cov_laplacian(f,q,box=2*math.pi):
    qi=torch.linalg.inv(q); sqrtq=torch.sqrt(torch.linalg.det(q))
    df=torch.stack([HDA.dspec(f,a,box) for a in range(3)],dim=-1)
    v=torch.einsum('...ij,...j->...i',qi,df)*sqrtq[...,None]
    return sum(HDA.dspec(v[...,i],i,box) for i in range(3))/sqrtq


def one(c,n=7,amp=0.01,seed=1):
    qc0,pc0,X=HDA.smooth_state(n,amp,seed)
    qc=qc0.clone().requires_grad_(); pc=pc0.clone().requires_grad_()
    N=torch.sin(X[0]); M=torch.sin(X[1])
    A=Hc(qc,pc,N,c); B=Hc(qc,pc,M,c)
    bracket=HDA.poisson(A,B,qc,pc)
    q=HDA.coeff_to_mat(qc); qi=torch.linalg.inv(q)
    dN=torch.stack([HDA.dspec(N,a) for a in range(3)],dim=-1)
    dM=torch.stack([HDA.dspec(M,a) for a in range(3)],dim=-1)
    beta=torch.einsum('...ab,...b->...a',qi,N[...,None]*dM-M[...,None]*dN)
    D=HDA.D_smear(qc,pc,beta)
    pi=torch.einsum('...ij,...ij->...',q,HDA.coeff_to_mat(pc))
    lapN=cov_laplacian(N,q); lapM=cov_laplacian(M,q)
    dx=2*math.pi/n
    I=torch.sum(pi*(N*lapM-M*lapN))*dx**3
    predicted=D+4*(c-0.5)*I
    algebra_error=float(abs((bracket-predicted).item())/(abs(bracket.item())+abs(predicted.item())+1e-30))
    hda_defect=float(abs((bracket-D).item())/(abs(bracket.item())+abs(D.item())+1e-30))
    return {'c':float(c),'bracket':float(bracket.item()),'D_beta':float(D.item()),'extra_integral_I':float(I.item()),'predicted_bracket':float(predicted.item()),'analytic_formula_relative_error':algebra_error,'HDA_defect_against_GR_rhs':hda_defect}


def run(n=7,amp=0.01,seed=1):
    cs=[0.2,0.3,0.4,0.45,0.5,0.55,0.6,0.7,0.8]
    rows=[one(c,n,amp,seed) for c in cs]
    gr=next(r for r in rows if r['c']==0.5)
    passed=max(r['analytic_formula_relative_error'] for r in rows)<2e-6 and gr['HDA_defect_against_GR_rhs']<1e-7 and all((r['c']==0.5 or r['HDA_defect_against_GR_rhs']>1e-3) for r in rows)
    return {'status':'DeWitt/HDA uniqueness finite regression','passed':bool(passed),'L':n,'amplitude':amp,'seed':seed,'identity':'{H_c[N],H_c[M]}=D[beta]+4(c-1/2) int pi(N nabla^2 M-M nabla^2 N)','GR_value':'c=1/2','rows':rows,'interpretation':'For generic data the additional scalar term vanishes identically for all lapses only at c=1/2. This is a classical uniqueness/constraint-closure target for the microscopic Lorentzian model.'}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--L',type=int,default=7);ap.add_argument('--amp',type=float,default=0.01);ap.add_argument('--seed',type=int,default=1);ap.add_argument('--output',type=Path);a=ap.parse_args()
    out=run(a.L,a.amp,a.seed);text=json.dumps(out,indent=2);print(text)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
