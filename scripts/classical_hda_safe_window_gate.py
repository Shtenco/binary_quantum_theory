#!/usr/bin/env python3
"""Classical ADM hypersurface-deformation algebra benchmark on a periodic 3D grid.

This is a regulator/control test for the future microscopic quantum-link HDA.
It evaluates H[N] and H[M] independently, obtains functional derivatives with
torch autograd, forms their canonical Poisson bracket, and compares it with the
diffeomorphism generator D[beta],

    beta^a = q^{ab}(N d_b M - M d_b N).

The fields and lapses are deliberately low-momentum.  Increasing the spectral
grid therefore tests the spatial momentum-wall/aliasing error rather than a
putative quantum anomaly.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np
import torch

torch.set_default_dtype(torch.float64)


def sym_basis3():
    B=[]
    for i in range(3):
        M=torch.zeros((3,3)); M[i,i]=1.; B.append(M)
    for i,j in ((0,1),(0,2),(1,2)):
        M=torch.zeros((3,3)); M[i,j]=M[j,i]=1/math.sqrt(2); B.append(M)
    return torch.stack(B)
BASIS=sym_basis3()


def coeff_to_mat(c):
    return torch.einsum('...A,Aij->...ij',c,BASIS)


def dspec(field,axis,box=2*math.pi):
    n=field.shape[axis]; dx=box/n
    k=2*math.pi*torch.fft.fftfreq(n,d=dx,device=field.device,dtype=field.dtype)
    F=torch.fft.fftn(field,dim=(0,1,2)); shape=[1]*field.ndim; shape[axis]=n
    return torch.fft.ifftn(F*(1j*k.reshape(shape)),dim=(0,1,2)).real


def ricci_scalar(q,box=2*math.pi):
    qi=torch.linalg.inv(q)
    dq=torch.stack([dspec(q,a,box) for a in range(3)],dim=-3)
    shp=q.shape[:-2]
    G=torch.zeros(shp+(3,3,3),dtype=q.dtype)
    for r in range(3):
        for m in range(3):
            for n in range(3):
                s=0.
                for a in range(3):
                    s=s+0.5*qi[...,r,a]*(dq[...,m,n,a]+dq[...,n,m,a]-dq[...,a,m,n])
                G[...,r,m,n]=s
    dG=torch.stack([dspec(G,a,box) for a in range(3)],dim=-4)
    Ric=torch.zeros(shp+(3,3),dtype=q.dtype)
    for m in range(3):
        for n in range(3):
            s=torch.zeros(shp,dtype=q.dtype)
            for r in range(3):
                s=s+dG[...,r,r,m,n]-dG[...,n,r,m,r]
                for a in range(3):
                    s=s+G[...,r,m,n]*G[...,a,r,a]-G[...,a,m,r]*G[...,r,n,a]
            Ric[...,m,n]=s
    return torch.einsum('...ij,...ij->...',qi,Ric)


def H_smear(qc,pc,lapse,box=2*math.pi):
    q=coeff_to_mat(qc); p=coeff_to_mat(pc); qi=torch.linalg.inv(q)
    sqrtq=torch.sqrt(torch.linalg.det(q))
    pcov=torch.einsum('...ai,...ij,...bj->...ab',q,p,q)
    pipi=torch.einsum('...ij,...ij->...',p,pcov)
    trp=torch.einsum('...ij,...ij->...',q,p)
    R=ricci_scalar(q,box)
    dens=(pipi-0.5*trp**2)/sqrtq-sqrtq*R
    dx=box/q.shape[0]
    return torch.sum(lapse*dens)*dx**3


def D_smear(qc,pc,shift,box=2*math.pi):
    q=coeff_to_mat(qc); p=coeff_to_mat(pc)
    db=torch.stack([dspec(shift,a,box) for a in range(3)],dim=-2)
    dq=torch.stack([dspec(q,a,box) for a in range(3)],dim=-3)
    Lq=torch.zeros_like(q)
    for a in range(3):
        for b in range(3):
            s=0.
            for c in range(3):
                s=s+shift[...,c]*dq[...,c,a,b]+q[...,c,b]*db[...,a,c]+q[...,a,c]*db[...,b,c]
            Lq[...,a,b]=s
    dx=box/q.shape[0]
    return torch.sum(torch.einsum('...ab,...ab->...',p,Lq))*dx**3


def poisson(F,G,qc,pc,box=2*math.pi):
    Fq,Fp=torch.autograd.grad(F,(qc,pc),create_graph=True,retain_graph=True)
    Gq,Gp=torch.autograd.grad(G,(qc,pc),create_graph=True,retain_graph=True)
    dV=(box/qc.shape[0])**3
    return torch.sum(Fq*Gp-Fp*Gq)/dV


def smooth_state(n,amp=0.01,seed=1):
    rng=np.random.default_rng(seed)
    x=torch.arange(n)*2*math.pi/n; X=torch.meshgrid(x,x,x,indexing='ij')
    qc=torch.zeros((n,n,n,6)); pc=torch.zeros_like(qc)
    qc[...,0]=qc[...,1]=qc[...,2]=1.
    modes=((1,0,0),(0,1,0))
    for A in range(6):
        for m in modes:
            ph=m[0]*X[0]+m[1]*X[1]+m[2]*X[2]
            qc[...,A]+=amp*rng.normal()*torch.cos(ph)+amp*rng.normal()*torch.sin(ph)
            pc[...,A]+=amp*rng.normal()*torch.cos(ph)+amp*rng.normal()*torch.sin(ph)
    return qc,pc,X


def one_size(n,amp=0.01,seed=1):
    qc0,pc0,X=smooth_state(n,amp,seed)
    qc=qc0.clone().requires_grad_(); pc=pc0.clone().requires_grad_()
    N=torch.sin(X[0]); M=torch.sin(X[1])
    HN=H_smear(qc,pc,N); HM=H_smear(qc,pc,M); bracket=poisson(HN,HM,qc,pc)
    q=coeff_to_mat(qc); qi=torch.linalg.inv(q)
    dN=torch.stack([dspec(N,a) for a in range(3)],dim=-1)
    dM=torch.stack([dspec(M,a) for a in range(3)],dim=-1)
    beta=torch.einsum('...ab,...b->...a',qi,N[...,None]*dM-M[...,None]*dN)
    rhs=D_smear(qc,pc,beta)
    defect=float(abs((bracket-rhs).item())/(abs(bracket.item())+abs(rhs.item())+1e-30))
    return {'L':n,'HH_bracket':float(bracket.item()),'D_beta':float(rhs.item()),'relative_HDA_defect':defect}


def run(sizes=(4,5,6,7,8),amp=0.01,seed=1):
    rows=[one_size(n,amp,seed) for n in sizes]
    defects=[r['relative_HDA_defect'] for r in rows]
    passed=all(defects[i+1]<defects[i] for i in range(len(defects)-1)) and defects[-1]<1e-8
    return {
        'status':'classical ADM HDA spectral safe-window benchmark',
        'passed':bool(passed),'amplitude':amp,'seed':seed,'sizes':list(sizes),'rows':rows,
        'definition':'Delta_HH=|{H[N],H[M]}-D[beta]|/(|{H[N],H[M]}|+|D[beta]|), beta^a=q^{ab}(N d_b M-M d_b N)',
        'safe_window_note':'Low Fourier lapses and low-mode fields are used. The rapidly falling defect is a regulator/aliasing control, not evidence for the microscopic quantum HDA.',
        'quantum_target':'Future Peter-Weyl tests must satisfy both spin-wall safety j_phys+r/2<Jmax and momentum-wall safety |k|,|p|,|k+p| well below Nyquist before an HH residual is interpreted as a quantum anomaly.'
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--sizes',type=int,nargs='+',default=[4,5,6,7,8]); ap.add_argument('--amp',type=float,default=0.01); ap.add_argument('--seed',type=int,default=1); ap.add_argument('--output',type=Path); a=ap.parse_args()
    out=run(tuple(a.sizes),a.amp,a.seed); text=json.dumps(out,indent=2); print(text)
    if a.output: a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
