#!/usr/bin/env python3
from __future__ import annotations
import argparse,itertools,json,sys
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_euclidean_sine_ordering_gate as SINE
import peter_weyl_j1_s4_block_gate as J1
import peter_weyl_zeroaware_volume_migration_experiment as ZVM

S2=4; JMAX2=7
K2=(0,2,4,6,8)
PERMS=tuple(itertools.permutations(range(4)))
CHI={(1,1,1,1):2,(2,1,1):0,(2,2):2,(3,1):-1,(4,):0}

def inner(a,b):
    if len(a)>len(b): return np.conj(inner(b,a))
    return sum(np.conj(v)*b.get(k,0j) for k,v in a.items())

def key(K):
    return (S2,)*len(PW.EDGES),(K,0,0,0,0)

def image(K):
    return SINE.safe_H_sine({key(K):1+0j},0,JMAX2)

def gram(imgs):
    n=len(imgs); G=np.zeros((n,n),complex)
    for i in range(n):
        for j in range(i,n):
            z=inner(imgs[i],imgs[j]); G[i,j]=z; G[j,i]=np.conj(z)
    return (G+G.conj().T)/2

def p22():
    P=np.zeros((5,5),complex)
    for p in PERMS: P += CHI[J1.cycle_type(p)]*J1.permutation_matrix(S2,p)
    P*=2/24
    return (P+P.conj().T)/2

def volume():
    ks,ts=J1.local_basis(S2); V=np.zeros((5,5),complex)
    for j,T in enumerate(ts):
        VT=PW.apply_volume_tensor(T,(S2,S2,S2,S2))
        for i,S in enumerate(ts): V[i,j]=np.vdot(S,VT)
    return (V+V.conj().T)/2

def restrict(A,P):
    w,U=np.linalg.eigh(P); B=U[:,w>0.5]
    R=B.conj().T@A@B
    return (R+R.conj().T)/2

def run():
    ZVM.patch_and_clear()
    imgs=[image(K) for K in K2]
    M=gram(imgs); P=p22()
    # Raw boundary-conditioned local master is not expected to be a scalar
    # under a permutation acting only on node-0 when the environment is frozen.
    # Build the exact S4 twirl of this actual master to remove that boundary-frame
    # choice without fitting any coefficient.
    Msym=np.zeros_like(M)
    for p in PERMS:
        U=J1.permutation_matrix(S2,p)
        Msym += U.conj().T@M@U
    Msym /= len(PERMS)
    Msym=(Msym+Msym.conj().T)/2

    M22=restrict(Msym,P); V22=restrict(volume(),P)
    em=np.sort(np.linalg.eigvalsh(M22).real)
    ev=np.sort(np.linalg.eigvalsh(V22).real)
    mspread=max(np.ptp(em[:2]),np.ptp(em[2:]))
    vspread=max(np.ptp(ev[:2]),np.ptp(ev[2:]))
    comm=np.linalg.norm(M22@V22-V22@M22)
    scale=max(np.linalg.norm(M22)*np.linalg.norm(V22),1e-30)
    wm,Um=np.linalg.eigh(M22); wv,Uv=np.linalg.eigh(V22)
    Um=Um[:,np.argsort(wm)]; Uv=Uv[:,np.argsort(wv)]
    Pm=Um[:,:2]@Um[:,:2].conj().T; Pv=Uv[:,:2]@Uv[:,:2].conj().T
    overlap=float(np.trace(Pm@Pv).real/2)
    s4_raw=max(np.linalg.norm(M@J1.permutation_matrix(S2,p)-J1.permutation_matrix(S2,p)@M) for p in PERMS)
    s4=max(np.linalg.norm(Msym@J1.permutation_matrix(S2,p)-J1.permutation_matrix(S2,p)@Msym) for p in PERMS)
    nM=max(np.linalg.norm(Msym,2),1.0)
    passed=(np.min(np.linalg.eigvalsh(Msym).real)>-1e-8*nM and s4<2e-7*nM and
            mspread<2e-7*max(np.max(np.abs(em)),1.0) and
            vspread<2e-7*max(np.max(np.abs(ev)),1.0))
    return {
      "status":"actual local Peter-Weyl Euclidean constraint master + exact S4-twirled multiplicity diagnostic at j=2",
      "passed":bool(passed),
      "P22_rank":int(round(np.trace(P).real)),
      "raw_boundary_conditioned_master_eigenvalues":[float(x) for x in np.linalg.eigvalsh(M).real],
      "raw_S4_commutator_max":float(s4_raw),
      "twirled_master_eigenvalues":[float(x) for x in np.linalg.eigvalsh(Msym).real],
      "twirled_S4_commutator_max":float(s4),
      "twirl_relative_change":float(np.linalg.norm(Msym-M)/max(np.linalg.norm(M),1e-30)),
      "master_restricted_eigenvalues":[float(x) for x in em],
      "master_multiplicity_eigenvalues":[float(np.mean(em[:2])),float(np.mean(em[2:]))],
      "master_multiplicity_gap":float(abs(np.mean(em[2:])-np.mean(em[:2]))),
      "master_pair_spread_max":float(mspread),
      "volume_restricted_eigenvalues":[float(x) for x in ev],
      "master_volume_commutator_norm":float(comm),
      "master_volume_commutator_relative":float(comm/scale),
      "low_channel_subspace_overlap":overlap,
      "column_supports":[len(x) for x in imgs],
      "max_spin_after_constraint":float(max((max(k[0])/2 for img in imgs for k in img),default=0)),
      "scope":"raw local Euclidean C0^dag C0 plus exact S4 twirl of its boundary-conditioned node-0 block; twirl is a symmetry-restored finite diagnostic, not the full global/Lorentzian master"
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",type=Path); a=ap.parse_args()
    out=run(); txt=json.dumps(out,indent=2); print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(txt+"\n",encoding="utf-8")
    return 0 if out["passed"] else 2
if __name__=="__main__": raise SystemExit(main())
