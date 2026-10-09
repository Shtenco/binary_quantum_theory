#!/usr/bin/env python3
"""Exact microscopic bilinear refinement tensor at j=1/2 -> j=1.

The old node singlet and the four fresh ancilla spins each carry the S4 [2,2]
irrep.  Edgewise symmetric blocking defines a bilinear map from old x ancilla
singlets into the coarse j=1 singlet space.

This gate verifies that, after projection onto the coarse [2,2] sector, the
resulting tensor is an exact S4 intertwiner
    [2,2] old tensor [2,2] anc -> [2,2] coarse
and has rank two.  It also verifies that no fixed nonzero ancilla vector can
make the induced old->coarse map S4-equivariant.
"""
from __future__ import annotations
import itertools, json, sys
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
import peter_weyl_j1_s4_block_gate as J1
from bqg_ancilla_peter_weyl_refinement_gate import inclusion

PERMS=tuple(itertools.permutations(range(4)))
CHAR22={(1,1,1,1):2,(2,1,1):0,(2,2):2,(3,1):-1,(4,):0}

def block_tensor(old,anc,B):
    return np.einsum(
        "Aae,Bbf,Ccg,Ddh,abcd,efgh->ABCD",
        B,B,B,B,old,anc,optimize=True
    )

def coarse_P22():
    P=np.zeros((3,3),complex)
    for p in PERMS:
        P += CHAR22[J1.cycle_type(p)]*J1.permutation_matrix(2,p)
    P*=2/24
    return (P+P.conj().T)/2

def run():
    kf,tf=J1.local_basis(1)
    kc,tc=J1.local_basis(2)
    B=inclusion(1).conj().T.reshape(3,2,2)

    # Tfull: coarse singlet index r, old logical b, ancilla logical a
    T=np.zeros((3,2,2),complex)
    leakage=0.0
    for b,old in enumerate(tf):
        for a,anc in enumerate(tf):
            out=block_tensor(old,anc,B)
            coeff=np.array([np.vdot(c,out) for c in tc],complex)
            T[:,b,a]=coeff
            proj=sum(coeff[r]*tc[r] for r in range(3))
            leakage += float(np.vdot(out-proj,out-proj).real)

    P22=coarse_P22()
    T22=np.einsum("rs,sba->rba",P22,T)
    F=T22.reshape(3,4)

    cov_err=0.0
    for p in PERMS:
        Uc=J1.permutation_matrix(2,p)
        Uf=J1.permutation_matrix(1,p)
        Ua=Uf
        rhs=F@np.kron(Uf,Ua)
        lhs=Uc@F
        cov_err=max(cov_err,float(np.linalg.norm(lhs-rhs)))

    svals=np.linalg.svd(F,compute_uv=False)
    rank=int(np.sum(svals>1e-10))

    # No nonzero invariant ancilla vector in [2,2].
    # Solve Ua(p) v = v for all p by nullspace of stacked equations.
    A=[]
    for p in PERMS:
        A.append(J1.permutation_matrix(1,p)-np.eye(2))
    A=np.vstack(A)
    inv_s=np.linalg.svd(A,compute_uv=False)
    invariant_nullity=int(np.sum(inv_s<1e-10))

    # Character-product decomposition check: [22]x[22]=[4]+[22]+[1^4].
    chars={}
    for p in PERMS:
        ct=J1.cycle_type(p)
        chars.setdefault(ct,complex(np.trace(J1.permutation_matrix(1,p))))
    # use representative traces; known classes are constant numerically
    reps={}
    for p in PERMS:
        ct=J1.cycle_type(p)
        reps.setdefault(ct,float(np.trace(J1.permutation_matrix(1,p)).real))
    product={ct:reps[ct]**2 for ct in reps}
    # expected product chars = chi_[4] + chi_[22] + chi_[1^4]
    expected={
      (1,1,1,1):4,(2,1,1):0,(2,2):4,(3,1):1,(4,):0
    }
    char_err=max(abs(product[ct]-expected[ct]) for ct in expected)

    passed=(leakage<1e-9 and cov_err<1e-9 and rank==2 and invariant_nullity==0 and char_err<1e-9)
    out={
      "status":"exact microscopic bilinear q2 refinement tensor",
      "passed":bool(passed),
      "Gauss_projection_leakage":leakage,
      "S4_covariance_error":cov_err,
      "coarse_22_tensor_rank":rank,
      "coarse_22_singular_values":[float(x) for x in svals],
      "ancilla_invariant_vector_dimension":invariant_nullity,
      "product_character_error":float(char_err),
      "decomposition":"[2,2]_old x [2,2]_anc = [4] + [2,2] + [1^4]",
      "claim":"A fixed pure ancilla singlet cannot define an S4-equivariant old-to-coarse map; the correct microscopic refinement object is the bilinear old x ancilla -> coarse tensor."
    }
    print(json.dumps(out,indent=2))
    return 0 if passed else 2

if __name__=="__main__": raise SystemExit(run())
