#!/usr/bin/env python3
"""Algebraic killer gate for assembling the Lorentzian covariant triple.

The trace in Tr[C_a(K) C_b(K) C_c(V)] is only over the auxiliary fundamental
2x2 index.  Its matrix entries are operators on geometry and need not commute.
Therefore ordinary scalar cyclic-trace shortcuts are unsafe.

This gate uses deterministic noncommuting geometry matrices and verifies two
identities with operator order preserved:

1. the full oriented 24-permutation epsilon sum on a four-valent node equals
   the exact K-pair commutator grouping face by face;
2. for operator-valued 2x2 matrices A=s_A I+a.sigma etc.,

   Tr_aux(ABC) = 2 [
       s_A s_B s_C
     + s_A b_i c_i
     + a_i s_B c_i
     + a_i b_i s_C
     + i eps_ijk a_i b_j c_k ],

   with every geometry product kept in the displayed order.

This is an algebra/assembler gate only.  It contains no Peter-Weyl amplitudes
and makes no H_L or HDA closure claim.
"""
from __future__ import annotations
import itertools
import json
import numpy as np

SEED=20260813
GEOM_DIM=4
I2=np.eye(2,dtype=complex)
SIGMA=[
    np.array([[0,1],[1,0]],complex),
    np.array([[0,-1j],[1j,0]],complex),
    np.array([[1,0],[0,-1]],complex),
]
EPS3=np.zeros((3,3,3),int)
for p in itertools.permutations(range(3)):
    inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
    EPS3[p]=(-1)**inv


def random_operator(rng):
    return rng.normal(size=(GEOM_DIM,GEOM_DIM))+1j*rng.normal(size=(GEOM_DIM,GEOM_DIM))


def covariant_operator(rng):
    s=random_operator(rng)
    v=[random_operator(rng) for _ in range(3)]
    full=np.kron(I2,s)
    for sig,x in zip(SIGMA,v):
        full += np.kron(sig,x)
    return full,s,v


def partial_trace_aux(M):
    g=GEOM_DIM
    return M[:g,:g]+M[g:,g:]


def parity(base,perm):
    idx=[base.index(x) for x in perm]
    inv=sum(idx[i]>idx[j] for i in range(3) for j in range(i+1,3))
    return -1 if inv%2 else 1


def pauli_formula(A,B,C):
    _,sA,a=A; _,sB,b=B; _,sC,c=C
    out=sA@sB@sC
    out += sum(sA@b[i]@c[i] for i in range(3))
    out += sum(a[i]@sB@c[i] for i in range(3))
    out += sum(a[i]@b[i]@sC for i in range(3))
    out += 1j*sum(
        EPS3[i,j,k]*(a[i]@b[j]@c[k])
        for i,j,k in itertools.product(range(3),repeat=3)
        if EPS3[i,j,k]
    )
    return 2*out


def run():
    rng=np.random.default_rng(SEED)
    K={e:covariant_operator(rng) for e in (1,2,3,4)}
    V={e:covariant_operator(rng) for e in (1,2,3,4)}
    neighbors=(1,2,3,4)

    raw=np.zeros((GEOM_DIM,GEOM_DIM),complex)
    grouped=np.zeros_like(raw)
    raw_term_count=0
    grouped_commutator_count=0
    for r,omit in enumerate(neighbors):
        base=tuple(x for x in neighbors if x!=omit)
        face=(-1)**r
        for perm in itertools.permutations(base):
            a,b,c=perm
            raw += face*parity(base,perm)*partial_trace_aux(
                K[a][0]@K[b][0]@V[c][0]
            )
            raw_term_count += 1
        x,y,z=base
        grouped += face*(
            partial_trace_aux((K[x][0]@K[y][0]-K[y][0]@K[x][0])@V[z][0])
            + partial_trace_aux((K[y][0]@K[z][0]-K[z][0]@K[y][0])@V[x][0])
            + partial_trace_aux((K[z][0]@K[x][0]-K[x][0]@K[z][0])@V[y][0])
        )
        grouped_commutator_count += 3
    eps_rel=float(np.linalg.norm(raw-grouped)/max(np.linalg.norm(raw),1e-30))

    pauli_errors=[]
    for a,b,c in itertools.permutations((1,2,3),3):
        lhs=partial_trace_aux(K[a][0]@K[b][0]@V[c][0])
        rhs=pauli_formula(K[a],K[b],V[c])
        pauli_errors.append(float(np.linalg.norm(lhs-rhs)/max(np.linalg.norm(lhs),1e-30)))
    max_pauli=max(pauli_errors,default=0.0)

    passed=(raw_term_count==24 and grouped_commutator_count==12 and eps_rel<1e-12 and max_pauli<1e-12)
    return {
        'status':'operator-valued Lorentzian triple assembler algebra gate',
        'passed':bool(passed),
        'seed':SEED,
        'geometry_operator_dimension':GEOM_DIM,
        'raw_oriented_permutation_terms':raw_term_count,
        'grouped_K_commutator_terms':grouped_commutator_count,
        'full_epsilon_vs_commutator_grouping_relative_error':eps_rel,
        'operator_valued_pauli_trace_relative_errors':pauli_errors,
        'max_operator_valued_pauli_trace_relative_error':max_pauli,
        'grouped_identity':'For each oriented face (x,y,z): Tr([K_x,K_y]V_z)+Tr([K_y,K_z]V_x)+Tr([K_z,K_x]V_y).',
        'ordering_rule':'Never use cyclicity of the auxiliary partial trace to reorder geometry operators; all products preserve the original right-to-left operator action.',
        'next_use':'Use this ordering in the real Peter-Weyl H_L column after state-to-state C(V) and C(K) composition gates pass.',
        'scope_note':'Synthetic noncommuting-operator algebra check only; no physical amplitude is used.'
    }

if __name__=='__main__':
    out=run(); print(json.dumps(out,indent=2)); raise SystemExit(0 if out['passed'] else 1)
