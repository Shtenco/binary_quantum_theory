#!/usr/bin/env python3
"""Test the existing all-j=1/2 K5 spin-network tensor as a global binary ancilla line."""
from __future__ import annotations
import itertools,json,sys
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))

import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_j1_s4_block_gate as J1

S5=tuple(itertools.permutations(range(5)))
BASIS=tuple(itertools.product((0,1),repeat=5))
INDEX={b:i for i,b in enumerate(BASIS)}

def parity(g):
    inv=sum(g[i]>g[j] for i in range(5) for j in range(i+1,5))
    return -1 if inv%2 else 1

def local_axis_perm(g,v):
    gv=g[v]
    inv=[0]*5
    for a,b in enumerate(g): inv[b]=a
    old=list(PW.NEIG[v])
    target=list(PW.NEIG[gv])
    perm=[]
    for u in target:
        w=inv[u]
        perm.append(old.index(w))
    return tuple(perm)

def global_rep(g,orientation_sign=False):
    R=np.zeros((32,32),complex)
    Ulocal=[J1.permutation_matrix(1,local_axis_perm(g,v)) for v in range(5)]
    sign=parity(g) if orientation_sign else 1
    for col,b in enumerate(BASIS):
        for c in BASIS:
            amp=1+0j
            out=[0]*5
            for v in range(5):
                amp*=Ulocal[v][c[v],b[v]]
                if abs(amp)<1e-15: break
                out[g[v]]=c[v]
            if abs(amp)>1e-15:
                R[INDEX[tuple(out)],col]+=sign*amp
    return R

def projector(reps,character):
    P=np.zeros((32,32),complex)
    for g,R in zip(S5,reps):
        P += character(g)*R
    P/=120
    return (P+P.conj().T)/2

def rank_projector(P):
    w=np.linalg.eigvalsh(P).real
    return int(np.sum(w>0.5)),float(np.linalg.norm(P@P-P)),w

def line_error(reps,v,character):
    v=v/np.linalg.norm(v)
    return max(float(np.linalg.norm(R@v-character(g)*v)) for g,R in zip(S5,reps))

def analyze(orientation_sign):
    reps=[global_rep(g,orientation_sign) for g in S5]
    unit=max(float(np.linalg.norm(R.conj().T@R-np.eye(32))) for R in reps)
    Ptriv=projector(reps,lambda g:1)
    Psign=projector(reps,parity)
    rt,et,_=rank_projector(Ptriv)
    rs,es,_=rank_projector(Psign)
    v=PW.v5_tensor()
    vn=v/np.linalg.norm(v)
    return {
      "orientation_sign_included":orientation_sign,
      "representation_unitarity_error":unit,
      "trivial_projector_rank":rt,
      "trivial_projector_error":et,
      "sign_projector_rank":rs,
      "sign_projector_error":es,
      "V5_trivial_line_error":line_error(reps,vn,lambda g:1),
      "V5_sign_line_error":line_error(reps,vn,parity),
      "V5_trivial_projector_weight":float(np.vdot(vn,Ptriv@vn).real),
      "V5_sign_projector_weight":float(np.vdot(vn,Psign@vn).real),
    }

def run():
    a=analyze(False)
    b=analyze(True)
    candidates=[]
    for x in (a,b):
        if x["representation_unitarity_error"]<1e-9:
            if x["trivial_projector_rank"]==1 and x["V5_trivial_line_error"]<1e-9:
                candidates.append(("trivial",x["orientation_sign_included"]))
            if x["sign_projector_rank"]==1 and x["V5_sign_line_error"]<1e-9:
                candidates.append(("sign",x["orientation_sign_included"]))
    out={
      "status":"global K5 binary-ancilla S5 symmetry test",
      "passed":bool(candidates),
      "V5_norm":float(np.linalg.norm(PW.v5_tensor())),
      "V5_nonzero_components":int(np.sum(np.abs(PW.v5_tensor())>1e-12)),
      "bare_action":a,
      "orientation_corrected_action":b,
      "accepted_symmetry_lines":[{"irrep":x[0],"orientation_sign_included":x[1]} for x in candidates],
      "claim_boundary":"A one-dimensional S5 symmetry line gives a canonical correlated K5 ancilla tensor for refinement. This is a kinematical symmetry selection only; it does not yet prove that physical master/history dynamics prepares this ancilla layer."
    }
    print(json.dumps(out,indent=2))
    return 0 if out["passed"] else 2

if __name__=="__main__":
    raise SystemExit(run())
