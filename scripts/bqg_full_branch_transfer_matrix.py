#!/usr/bin/env python3
"""Full BQG master-branch transfer matrix for one RG step.

For every source master-selected [2,2] multiplicity channel at spin j:
  1. apply the exact microscopic binary-ancilla bilinear refinement;
  2. extract the generated target [2,2] copy;
  3. resolve it against every target master [2,2] channel.

The resulting matrix
    F_rs = 1/2 Tr(P_block(source r) P_master(target s))
is row-stochastic up to numerical precision.  It is the correct finite
branch-transition object; choosing the lowest target channel a priori is only
one special trajectory.
"""
from __future__ import annotations
import argparse,itertools,json,math,sys
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
    return (P+P.conj().T)/2*(2/24)

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
    wp,B0=np.linalg.eigh(P); B=B0[:,wp>0.5]
    R=B.conj().T@Ms@B; R=(R+R.conj().T)/2
    w,U=np.linalg.eigh(R); o=np.argsort(w); w=w[o]; U=U[:,o]
    chans=[]
    for q in range(0,len(w),2):
        S=B@U[:,q:q+2]
        chans.append({
            "index":q//2,
            "eigenvalue":float(np.mean(w[q:q+2])),
            "basis":S,
            "projector":S@S.conj().T,
        })
    return chans,B

def block_tensor(old,anc,Bedge):
    return np.einsum("Aae,Bbf,Ccg,Ddh,abcd,efgh->ABCD",
                     Bedge,Bedge,Bedge,Bedge,old,anc,optimize=True)

def refinement_tensor(s2):
    _,old=J1.local_basis(s2)
    _,target=J1.local_basis(s2+1)
    _,anc=J1.local_basis(1)
    Bedge=inclusion(s2).conj().T.reshape(s2+2,s2+1,2)
    T=np.zeros((len(target),len(old),len(anc)),complex)
    leak=0.0
    for b,ob in enumerate(old):
        for a,aa in enumerate(anc):
            out=block_tensor(ob,aa,Bedge)
            c=np.array([np.vdot(t,out) for t in target],complex)
            T[:,b,a]=c
            proj=sum(c[r]*target[r] for r in range(len(target)))
            leak += float(np.vdot(out-proj,out-proj).real)
    return T,leak

def generated_projector(T,Ssrc,Btarget):
    G=np.einsum("rba,bu->rua",T,Ssrc).reshape(T.shape[0],4)
    G22=Btarget@(Btarget.conj().T@G)
    U,s,Vh=np.linalg.svd(G22,full_matrices=False)
    rank=int(np.sum(s>1e-10))
    Q=U[:,:2]
    return Q@Q.conj().T,rank,[float(x) for x in s]

def run(s2):
    ZVM.patch_and_clear()
    src,_=master_channels(s2)
    dst,Bt=master_channels(s2+1)
    T,leak=refinement_tensor(s2)
    F=np.zeros((len(src),len(dst)),float)
    ranks=[]; singular=[]
    for r,csrc in enumerate(src):
        Pblock,rank,svals=generated_projector(T,csrc["basis"],Bt)
        ranks.append(rank); singular.append(svals)
        for s,cdst in enumerate(dst):
            F[r,s]=float(np.trace(Pblock@cdst["projector"]).real/2.0)
    rowsum=F.sum(axis=1)
    best=[{
        "source_channel":r,
        "target_channel":int(np.argmax(F[r])),
        "overlap":float(np.max(F[r])),
        "chi":float(math.sqrt(max(0.0,1.0-np.max(F[r]))))
    } for r in range(len(src))]
    return {
        "status":"full microscopic/master branch-transfer matrix",
        "passed":bool(np.max(abs(rowsum-1.0))<1e-8 and all(x==2 for x in ranks) and leak<1e-8),
        "source_j":s2/2,
        "target_j":(s2+1)/2,
        "source_master_eigenvalues":[c["eigenvalue"] for c in src],
        "target_master_eigenvalues":[c["eigenvalue"] for c in dst],
        "F_matrix":F.tolist(),
        "row_sums":rowsum.tolist(),
        "best_target_per_source":best,
        "generated_ranks":ranks,
        "generated_singular_values":singular,
        "Gauss_projection_leakage":leak,
        "interpretation":"F is the finite branch-transfer matrix. A smooth RG trajectory should be tracked through the target branch maximizing physically justified continuity, not assumed to be the lowest eigenvalue at every scale."
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--s2",type=int,required=True)
    ap.add_argument("--output",type=Path)
    a=ap.parse_args()
    out=run(a.s2); txt=json.dumps(out,indent=2); print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(txt+"\n",encoding="utf-8")
    return 0 if out["passed"] else 2

if __name__=="__main__": raise SystemExit(main())
