#!/usr/bin/env python3
"""Serial BQG S4-twirled local constraint-master scan across equal-spin j.

For each doubled spin s2:
  * all ten K5 links carry j=s2/2;
  * nodes 1..4 are fixed in K=0;
  * node 0 spans the full equal-spin singlet basis K2=0,2,...,2*s2;
  * C0 = H_E,0^sine is the same production Peter-Weyl Euclidean constraint;
  * M_raw = C0^dag C0 is built as the Gram matrix of one-hit images;
  * M_tw is the exact S4 twirl in the node-0 singlet representation;
  * M_tw is restricted to the full [2,2] isotypic sector.

Because M_tw is S4 invariant, the restricted spectrum must be the spectrum of
the multiplicity matrix A_j, each eigenvalue repeated exactly twice.

This gate therefore produces the first serial sequence A_j and its isolation
gaps gamma_j without fitting an embedding or changing the microscopic
constraint between scales.
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

def restrict(A,P):
    w,U=np.linalg.eigh(P); B=U[:,w>0.5]
    R=B.conj().T@A@B
    return (R+R.conj().T)/2

def pair_reduce(ev,tol_scale):
    ev=np.sort(np.asarray(ev,float))
    assert len(ev)%2==0
    vals=[]; spreads=[]
    for i in range(0,len(ev),2):
        pair=ev[i:i+2]
        vals.append(float(np.mean(pair)))
        spreads.append(float(np.ptp(pair)))
    return vals,spreads,max(spreads,default=0.0)

def one_scale(s2):
    spins=(s2,)*len(PW.EDGES)
    K2=tuple(range(0,2*s2+1,2))
    # One fundamental hit changes j by 1/2; conservative doubled-spin wall.
    jmax2=s2+3
    imgs=[]
    for K in K2:
        key=(spins,(K,0,0,0,0))
        imgs.append(SINE.safe_H_sine({key:1+0j},0,jmax2))
    M=gram(imgs)

    Msym=np.zeros_like(M)
    for p in PERMS:
        U=J1.permutation_matrix(s2,p)
        Msym += U.conj().T@M@U
    Msym/=24
    Msym=(Msym+Msym.conj().T)/2

    P=p22(s2)
    M22=restrict(Msym,P)
    ev=np.linalg.eigvalsh(M22).real
    avals,spreads,maxspread=pair_reduce(ev,max(np.max(np.abs(ev)),1.0))
    # Adjacent multiplicity gaps, plus the isolation gap of the lowest channel.
    gaps=[float(avals[i+1]-avals[i]) for i in range(len(avals)-1)]
    gamma_low=float(gaps[0]) if gaps else math.inf

    raw_s4=max(float(np.linalg.norm(M@J1.permutation_matrix(s2,p)-J1.permutation_matrix(s2,p)@M)) for p in PERMS)
    tw_s4=max(float(np.linalg.norm(Msym@J1.permutation_matrix(s2,p)-J1.permutation_matrix(s2,p)@Msym)) for p in PERMS)
    m22=math.ceil(s2/3)
    rank=int(round(np.trace(P).real))
    norm=max(float(np.linalg.norm(Msym,2)),1.0)
    passed=(rank==2*m22 and tw_s4<2e-7*norm and maxspread<2e-7*max(float(np.max(np.abs(ev))),1.0))

    return {
      "s2":s2,"j":s2/2,"passed":bool(passed),
      "singlet_dimension":s2+1,
      "m22":m22,"P22_rank":rank,
      "raw_S4_commutator_max":raw_s4,
      "twirled_S4_commutator_max":tw_s4,
      "twirl_relative_change":float(np.linalg.norm(Msym-M)/max(np.linalg.norm(M),1e-30)),
      "A_j_eigenvalues":avals,
      "A_j_adjacent_gaps":gaps,
      "gamma_low":gamma_low,
      "pair_spread_max":maxspread,
      "full_twirled_master_eigenvalues":[float(x) for x in np.linalg.eigvalsh(Msym).real],
      "column_supports":[len(x) for x in imgs],
      "max_spin_after_constraint":float(max((max(k[0])/2 for img in imgs for k in img),default=0.0)),
    }

def run(s2_values):
    ZVM.patch_and_clear()
    rows=[one_scale(s2) for s2 in s2_values]
    return {
      "status":"serial BQG local S4-twirled Euclidean constraint-master multiplicity scan",
      "passed":bool(all(r["passed"] for r in rows)),
      "operator":"M_j^tw = S4-twirl[(H_E,0^sine)^dag H_E,0^sine]",
      "rows":rows,
      "claim_boundary":"Finite local Euclidean, boundary-frame-twirled diagnostic. This yields A_j and gamma_j, not yet inter-scale iota_j, R_j, eta_j or epsilon_j, and not the full global/Lorentzian master."
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--s2",default="4,5,6,7,8")
    ap.add_argument("--output",type=Path)
    a=ap.parse_args()
    vals=[int(x) for x in a.s2.split(",") if x.strip()]
    out=run(vals); txt=json.dumps(out,indent=2); print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(txt+"\n",encoding="utf-8")
    return 0 if out["passed"] else 2
if __name__=="__main__": raise SystemExit(main())
