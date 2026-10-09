#!/usr/bin/env python3
"""Cross-scale microscopic/master channel overlap for BQG refinement.

For a source spin j and target j+1/2:
1. compute the S4-twirled local Euclidean constraint master at both scales;
2. select the isolated lowest [2,2] master channel (rank two);
3. build the exact microscopic q2 bilinear refinement tensor by adding a fresh
   four-spin-1/2 Gauss-singlet ancilla and symmetric edge blocking;
4. feed source selected channel x ancilla [2,2] through the blocking tensor;
5. extract the resulting target [2,2] copy;
6. compare its projector with the target master-selected [2,2] copy.

The overlap is a genuine cross-scale datum and does not require comparing
arbitrary basis vectors between multiplicity spaces.
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
    P*=2/24
    return (P+P.conj().T)/2

def master_data(s2):
    spins=(s2,)*len(PW.EDGES)
    K2=tuple(range(0,2*s2+1,2))
    imgs=[]
    for K in K2:
        imgs.append(SINE.safe_H_sine({(spins,(K,0,0,0,0)):1+0j},0,s2+3))
    M=gram(imgs)
    Ms=np.zeros_like(M)
    for p in PERMS:
        U=J1.permutation_matrix(s2,p)
        Ms += U.conj().T@M@U
    Ms/=24; Ms=(Ms+Ms.conj().T)/2
    P=p22(s2)
    wP,UP=np.linalg.eigh(P); B=UP[:,wP>0.5]
    M22=(B.conj().T@Ms@B); M22=(M22+M22.conj().T)/2
    w,U=np.linalg.eigh(M22)
    order=np.argsort(w); w=w[order]; U=U[:,order]
    # lowest master channel = first exact pair
    S=B@U[:,:2]
    # gap to next pair, if it exists
    if len(w)>2:
        gamma=float(np.mean(w[2:4])-np.mean(w[:2]))
    else:
        gamma=math.inf
    return {
      "selected_basis":S,
      "P22_basis":B,
      "selected_projector":S@S.conj().T,
      "gamma":gamma,
      "restricted_eigenvalues":[float(x) for x in w],
    }

def block_tensor(old,anc,Bedge):
    return np.einsum(
      "Aae,Bbf,Ccg,Ddh,abcd,efgh->ABCD",
      Bedge,Bedge,Bedge,Bedge,old,anc,optimize=True
    )

def refinement_tensor(s2):
    ks,old=J1.local_basis(s2)
    kt,target=J1.local_basis(s2+1)
    ka,anc=J1.local_basis(1)
    Bedge=inclusion(s2).conj().T.reshape(s2+2,s2+1,2)
    T=np.zeros((len(target),len(old),len(anc)),complex)
    leak=0.0
    for b,ob in enumerate(old):
        for a,aa in enumerate(anc):
            out=block_tensor(ob,aa,Bedge)
            coeff=np.array([np.vdot(t,out) for t in target],complex)
            T[:,b,a]=coeff
            proj=sum(coeff[r]*target[r] for r in range(len(target)))
            leak += float(np.vdot(out-proj,out-proj).real)
    return T,leak

def run(s2):
    ZVM.patch_and_clear()
    src=master_data(s2); dst=master_data(s2+1)
    T,leak=refinement_tensor(s2)

    Ss=src["selected_basis"]     # ds x 2
    St=dst["selected_basis"]     # dt x 2
    Bt=dst["P22_basis"]          # dt x (2m)

    # Source selected logical x ancilla logical -> target ambient singlet.
    G=np.einsum("rba,bu->rua",T,Ss).reshape(T.shape[0],4)

    # Full generated target [2,2] component.
    G22=Bt@ (Bt.conj().T@G)
    U,svals,Vh=np.linalg.svd(G22,full_matrices=False)
    rank=int(np.sum(svals>1e-10))
    Q=U[:,:rank]
    Pblock=Q@Q.conj().T

    Pmaster=dst["selected_projector"]
    overlap=float(np.trace(Pblock@Pmaster).real/2.0)
    angle=float(np.linalg.norm(Pblock-Pmaster,2))

    # Direct selected-target map and relative microscopic weight.
    Gsel=St.conj().T@G
    sel_weight=float(np.linalg.norm(Gsel)**2)
    total_weight=float(np.linalg.norm(G22)**2)
    frac=sel_weight/total_weight if total_weight>0 else 0.0

    # Equal singular values are the Schur diagnostic for the generated copy.
    nonzero=svals[:2]
    pair_spread=float(abs(nonzero[0]-nonzero[1])) if len(nonzero)>=2 else math.inf

    passed=(leak<1e-8 and rank==2 and pair_spread<1e-8 and -1e-10<=overlap<=1+1e-10 and abs(frac-overlap)<1e-8)

    return {
      "status":"microscopic/master cross-scale channel overlap",
      "passed":bool(passed),
      "source_s2":s2,"source_j":s2/2,
      "target_s2":s2+1,"target_j":(s2+1)/2,
      "source_gamma":src["gamma"],
      "target_gamma":dst["gamma"],
      "source_master_restricted_eigenvalues":src["restricted_eigenvalues"],
      "target_master_restricted_eigenvalues":dst["restricted_eigenvalues"],
      "microscopic_generated_rank":rank,
      "microscopic_generated_singular_values":[float(x) for x in svals],
      "microscopic_pair_spread":pair_spread,
      "Gauss_projection_leakage":leak,
      "channel_projector_overlap":overlap,
      "channel_principal_angle_sine":angle,
      "selected_weight_fraction":frac,
      "claim_boundary":"Measures whether the binary-ancilla blocking image of the source master-selected [2,2] channel aligns with the next-scale local master-selected [2,2] channel. This is a local Euclidean RG channel datum, not yet the full graph-changing physical-projector epsilon."
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
