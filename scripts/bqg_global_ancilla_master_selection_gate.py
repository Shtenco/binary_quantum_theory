#!/usr/bin/env python3
"""Select the global correlated q=2 K5 ancilla by actual symmetric constraint dynamics.

Build the full 32D all-j=1/2 logical basis on K5.  For each vertex v use the
production sine-Hermitian Euclidean constraint C_v=H_E,v^sine and assemble the
positive symmetric return/master control

    M_anc = sum_v C_v^dag C_v

as a sum of Gram matrices of one-hit images.

Construct the orientation-corrected S5 action from the global ancilla symmetry
gate, restrict M_anc to the exact two-dimensional trivial invariant sector, and
test whether:
  * the restriction is nondegenerate;
  * the existing v5_tensor line is an eigenline;
  * if not, what its overlap is with the dynamically selected low/high lines.

This is finite Euclidean K5 constraint dynamics, not the full Lorentzian
physical master/history.
"""
from __future__ import annotations
import itertools,json,sys
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))

import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_euclidean_sine_ordering_gate as SINE
import peter_weyl_zeroaware_volume_migration_experiment as ZVM
import bqg_global_k5_ancilla_symmetry_gate as GSYM

BASIS=GSYM.BASIS
JMAX2=3

def inner(a,b):
    if len(a)>len(b): return np.conj(inner(b,a))
    return sum(np.conj(v)*b.get(k,0j) for k,v in a.items())

def gram(imgs):
    n=len(imgs); G=np.zeros((n,n),complex)
    for i in range(n):
        for j in range(i,n):
            z=inner(imgs[i],imgs[j]); G[i,j]=z; G[j,i]=np.conj(z)
    return (G+G.conj().T)/2

def logical_key(bits):
    return (1,)*len(PW.EDGES), tuple(0 if b==0 else 2 for b in bits)

def run():
    ZVM.patch_and_clear()
    M=np.zeros((32,32),complex)
    supports={}
    for v in range(5):
        imgs=[]
        for bits in BASIS:
            imgs.append(SINE.safe_H_sine({logical_key(bits):1+0j},v,JMAX2))
        supports[str(v)]=[len(x) for x in imgs]
        M += gram(imgs)
    M=(M+M.conj().T)/2

    reps=[GSYM.global_rep(g,orientation_sign=True) for g in GSYM.S5]
    P=sum(reps)/len(reps)
    P=(P+P.conj().T)/2
    wp,Up=np.linalg.eigh(P)
    B=Up[:,wp>0.5]
    assert B.shape==(32,2)

    comm=max(float(np.linalg.norm(M@R-R@M)) for R in reps)
    nM=max(float(np.linalg.norm(M,2)),1.0)

    Minv=B.conj().T@M@B
    Minv=(Minv+Minv.conj().T)/2
    w,U=np.linalg.eigh(Minv)
    order=np.argsort(w); w=w[order]; U=U[:,order]
    gap=float(w[1]-w[0])

    # Existing V5 line expressed in the invariant basis.
    v5=PW.v5_tensor().astype(complex)
    v5/=np.linalg.norm(v5)
    inv_weight=float(np.vdot(v5,P@v5).real)
    c=B.conj().T@v5
    c/=np.linalg.norm(c)
    overlaps=[float(abs(np.vdot(U[:,i],c))**2) for i in range(2)]
    eig_res=float(np.linalg.norm(Minv@c-(np.vdot(c,Minv@c))*c))
    expval=float(np.vdot(c,Minv@c).real)

    passed=(
        comm<1e-7*nM
        and inv_weight>1-1e-10
        and gap>1e-10
        and abs(sum(overlaps)-1)<1e-10
    )
    out={
      "status":"global K5 correlated-ancilla constraint-master selection",
      "passed":bool(passed),
      "logical_dimension":32,
      "invariant_sector_dimension":2,
      "global_master_eigenvalue_min":float(np.min(np.linalg.eigvalsh(M).real)),
      "global_master_eigenvalue_max":float(np.max(np.linalg.eigvalsh(M).real)),
      "S5_commutator_max":comm,
      "invariant_master_eigenvalues":[float(x) for x in w],
      "invariant_master_gap":gap,
      "V5_invariant_weight":inv_weight,
      "V5_master_channel_overlaps":overlaps,
      "V5_master_expectation":expval,
      "V5_eigenline_residual":eig_res,
      "vertex_column_supports":supports,
      "claim_boundary":"This is a finite symmetric Euclidean K5 constraint-return/master control on the all-j=1/2 logical ancilla sector. A nondegenerate invariant eigenline gives a dynamical ancilla selector, but is not yet the full Lorentzian physical-history ancilla prescription."
    }
    print(json.dumps(out,indent=2))
    return 0 if passed else 2

if __name__=="__main__":
    raise SystemExit(run())
