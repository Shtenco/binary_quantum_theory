#!/usr/bin/env python3
"""Finite regression of the local ADM family selected by HDA closure.

For
 H[A,B,c,Lambda]=int N[A(pi_ab pi^ab-c pi^2)/sqrt(q)-B sqrt(q)(R-2 Lambda)]
this script verifies, in the spectral safe window,
 {H[N],H[M]} = A B [ D[beta] + 4(c-1/2) I[N,M] ],
while Lambda drops out.  Hence standard HDA selects c=1/2 and AB=1;
A/B (Newton normalization) and Lambda remain free in this ansatz.
"""
from __future__ import annotations
import argparse,json,math,sys
from pathlib import Path
import torch
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
import classical_hda_safe_window_gate as HDA
from dewitt_hda_uniqueness_gate import cov_laplacian

torch.set_default_dtype(torch.float64)

def Hgen(qc,pc,lapse,A,B,c,Lambda,box=2*math.pi):
    q=HDA.coeff_to_mat(qc);p=HDA.coeff_to_mat(pc);sq=torch.sqrt(torch.linalg.det(q))
    pcov=torch.einsum('...ai,...ij,...bj->...ab',q,p,q)
    pipi=torch.einsum('...ij,...ij->...',p,pcov);trp=torch.einsum('...ij,...ij->...',q,p)
    R=HDA.ricci_scalar(q,box);dx=box/q.shape[0]
    dens=A*(pipi-c*trp**2)/sq-B*sq*(R-2*Lambda)
    return torch.sum(lapse*dens)*dx**3

def one(A,B,c,Lambda,L=7,amp=.01,seed=1):
    qc0,pc0,X=HDA.smooth_state(L,amp,seed);qc=qc0.clone().requires_grad_();pc=pc0.clone().requires_grad_()
    N=torch.sin(X[0]);M=torch.sin(X[1])
    br=HDA.poisson(Hgen(qc,pc,N,A,B,c,Lambda),Hgen(qc,pc,M,A,B,c,Lambda),qc,pc)
    q=HDA.coeff_to_mat(qc);qi=torch.linalg.inv(q)
    dN=torch.stack([HDA.dspec(N,a) for a in range(3)],dim=-1);dM=torch.stack([HDA.dspec(M,a) for a in range(3)],dim=-1)
    beta=torch.einsum('...ab,...b->...a',qi,N[...,None]*dM-M[...,None]*dN)
    D=HDA.D_smear(qc,pc,beta)
    pi=torch.einsum('...ij,...ij->...',q,HDA.coeff_to_mat(pc));lapN=cov_laplacian(N,q);lapM=cov_laplacian(M,q);dx=2*math.pi/L
    I=torch.sum(pi*(N*lapM-M*lapN))*dx**3
    pred=A*B*(D+4*(c-.5)*I)
    err=float(abs((br-pred).item())/(abs(br.item())+abs(pred.item())+1e-30))
    standard=float(abs((br-D).item())/(abs(br.item())+abs(D.item())+1e-30))
    return {'A':A,'B':B,'AB':A*B,'c':c,'Lambda':Lambda,'bracket':float(br.item()),'D_beta':float(D.item()),'predicted':float(pred.item()),'identity_error':err,'standard_HDA_defect':standard}

def run(L=7,amp=.01,seed=1):
    cases=[
      (1,1,.5,0),(2,.5,.5,0),(4,.25,.5,0),(.5,2,.5,0),(3,1/3,.5,0),
      (2,1,.5,0),(1,2,.5,0),(1,1,.4,0),(1,1,.6,0),
      (1,1,.5,-10),(1,1,.5,10)
    ]
    rows=[one(*x,L=L,amp=amp,seed=seed) for x in cases]
    identity=max(r['identity_error'] for r in rows)
    good=[r for r in rows if abs(r['AB']-1)<1e-12 and abs(r['c']-.5)<1e-12]
    bad=[r for r in rows if abs(r['AB']-1)>1e-12 or abs(r['c']-.5)>1e-12]
    passed=identity<2e-6 and max(r['standard_HDA_defect'] for r in good)<1e-7 and min(r['standard_HDA_defect'] for r in bad)>1e-3
    return {'status':'ADM/HDA local parameter-selection regression','passed':bool(passed),'L':L,'amplitude':amp,'seed':seed,'identity':'{H_ABc[N],H_ABc[M]}=AB[D[beta]+4(c-1/2)I]','selected_by_standard_HDA':{'c':0.5,'AB':1.0},'not_selected_by_HDA_in_this_ansatz':['A/B (Newton/canonical normalization)','Lambda'],'rows':rows,'scope_note':'This is a classical local ADM ansatz test, not a proof of the microscopic quantum theory. The broader HKT uniqueness theorem requires its own assumptions about locality, canonical variables and representation of hypersurface deformations.'}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--L',type=int,default=7);ap.add_argument('--amp',type=float,default=.01);ap.add_argument('--seed',type=int,default=1);ap.add_argument('--output',type=Path);a=ap.parse_args();o=run(a.L,a.amp,a.seed);t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
