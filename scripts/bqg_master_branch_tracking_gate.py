#!/usr/bin/env python3
"""Resolve the microscopic refinement image against *all* target master channels.

This is the decisive branch-tracking diagnostic.  The previous overlap gate
compared the microscopic blocking image only to the *lowest* target master
multiplicity channel.  Here we decompose that same rank-2 generated [2,2] copy
against every isolated target master [2,2] copy.

If the microscopic image has near-unit overlap with some non-lowest channel,
then the apparent RG failure is a branch-label failure rather than an
incompatibility between binary refinement and constraint dynamics.
"""
from __future__ import annotations
import argparse, itertools, json, math, sys
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))

import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_euclidean_sine_ordering_gate as SINE
import peter_weyl_j1_s4_block_gate as J1
import peter_weyl_zeroaware_volume_migration_experiment as ZVM
from bqg_ancilla_peter_weyl_refinement_gate import inclusion

PERMS=tuple(itertools.permutations(range(4)))
CHI22={(1,1,1,1):2,(2,1,1):0,(2,2):2,(3,1):-1,(4,):0}

def inner(a,b):
    if len(a)>len(b): return np.conj(inner(b,a))
    return sum(np.conj(v)*b.get(k,0j) for k,v in a.items())

def gram(imgs):
    n=len(imgs); G=np.zeros((n,n),complex)
    for i in range(n):
        for j in range(i,n):
            z=inner(imgs[i],imgs[j]); G[i,j]=z; G[j,i]=np.conj(z)
    return (G+G.conj().T)/2

def p22(s2):
    d=s2+1; P=np.zeros((d,d),complex)
    for p in PERMS:
        P += CHI22[J1.cycle_type(p)]*J1.permutation_matrix(s2,p)
    return (P+P.conj().T)/2 * (2/24)

def master_channels(s2):
    spins=(s2,)*len(PW.EDGES)
    K2=tuple(range(0,2*s2+1,2))
    imgs=[SINE.safe_H_sine({(spins,(K,0,0,0,0)):1+0j},0,s2+3) for K in K2]
    M=gram(imgs)
    Ms=np.zeros_like(M)
    for p in PERMS:
        U=J1.permutation_matrix(s2,p)
        Ms += U.conj().T@M@U
    Ms/=24; Ms=(Ms+Ms.conj().T)/2
    P=p22(s2)
    wP,UP=np.linalg.eigh(P); B=UP[:,wP>0.5]
    M22=(B.conj().T@Ms@B); M22=(M22+M22.conj().T)/2
    w,U=np.linalg.eigh(M22); order=np.argsort(w); w=w[order]; U=U[:,order]
    chans=[]
    for q in range(0,len(w),2):
        S=B@U[:,q:q+2]
        chans.append({
            "index":q//2,
            "eigenvalue":float(np.mean(w[q:q+2])),
            "basis":S,
            "projector":S@S.conj().T,
            "pair_spread":float(np.ptp(w[q:q+2])),
        })
    return chans

def local_basis(s2):
    return J1.local_basis(s2)

def block_tensor(old,anc,Bedge):
    return np.einsum("Aae,Bbf,Ccg,Ddh,abcd,efgh->ABCD",
                     Bedge,Bedge,Bedge,Bedge,old,anc,optimize=True)

def refinement_tensor(s2):
    ks,old=local_basis(s2)
    kt,target=local_basis(s2+1)
    ka,anc=local_basis(1)
    Bedge=inclusion(s2).conj().T.reshape(s2+2,s2+1,2)
    T=np.zeros((len(target),len(old),len(anc)),complex)
    for b,ob in enumerate(old):
        for a,aa in enumerate(anc):
            out=block_tensor(ob,aa,Bedge)
            T[:,b,a]=np.array([np.vdot(t,out) for t in target],complex)
    return T

def p22_basis(s2):
    P=p22(s2); w,U=np.linalg.eigh(P); return U[:,w>0.5]

def run(s2):
    ZVM.patch_and_clear()
    src=master_channels(s2)
    dst=master_channels(s2+1)
    # source trajectory is still current lowest channel for this diagnostic
    Ss=src[0]["basis"]
    T=refinement_tensor(s2)
    Bt=p22_basis(s2+1)

    G=np.einsum("rba,bu->rua",T,Ss).reshape(T.shape[0],4)
    G22=Bt@(Bt.conj().T@G)
    U,svals,Vh=np.linalg.svd(G22,full_matrices=False)
    Q=U[:,:2]
    Pblock=Q@Q.conj().T

    overlaps=[]
    for c in dst:
        F=float(np.trace(Pblock@c["projector"]).real/2.0)
        overlaps.append({
            "channel_index":c["index"],
            "master_eigenvalue":c["eigenvalue"],
            "overlap":F,
            "chi":float(math.sqrt(max(0.0,1.0-F))),
        })
    overlaps.sort(key=lambda x:x["overlap"],reverse=True)
    best=overlaps[0]
    total=float(sum(x["overlap"] for x in overlaps))

    return {
        "status":"microscopic refinement vs all target master channels",
        "passed":bool(abs(total-1.0)<1e-8 and best["overlap"]>0.0),
        "source_j":s2/2,
        "target_j":(s2+1)/2,
        "source_channel":"lowest master channel",
        "target_channel_overlaps":overlaps,
        "best_target_channel":best,
        "sum_overlap":total,
        "generated_singular_values":[float(x) for x in svals],
        "interpretation":"If best_target_channel is not index 0 with near-unit overlap, the previous low-channel mismatch is a branch-label issue rather than microscopic/master incompatibility."
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--s2",type=int,required=True)
    ap.add_argument("--output",type=Path)
    a=ap.parse_args()
    out=run(a.s2); txt=json.dumps(out,indent=2); print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(txt+"\n",encoding="utf-8")
    return 0 if out["passed"] else 2

if __name__=="__main__":
    raise SystemExit(main())
