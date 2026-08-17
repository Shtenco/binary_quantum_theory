#!/usr/bin/env python3
"""Exact S4 sign-character twirl on one and two logical singlet qubits.

For the two-dimensional [2,2] logical representation E of S4,

    End(E)=A1(I)+A2(Y)+E(X,Z).

The one-cell sign-character projector

    T_sgn(O)=(1/24) sum_g sgn(g) U_g O U_g^dagger

therefore selects exactly Y.

For two logical cells under the diagonal action U_g tensor U_g, the sign sector
of operator space has dimension three. The expected exact basis is

    I tensor Y,
    Y tensor I,
    X tensor Z - Z tensor X.

These are the only two-cell logical operators transforming with the sign
character. This is a representation-theory control for an orientation/epsilon-
covariant Lorentzian operator. No nonzero physical Lorentzian amplitude is
asserted here.
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import logical_s4_twirl_gate as S4


def perm_sign(p):
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inv%2 else +1


def sign_twirl_one(M,reps,perms):
    out=np.zeros_like(M,dtype=complex)
    for U,p in zip(reps,perms):
        out += perm_sign(p)*(U@M@U.conj().T)
    return out/len(perms)


def sign_twirl_two(M,reps,perms):
    out=np.zeros_like(M,dtype=complex)
    for U,p in zip(reps,perms):
        W=np.kron(U,U)
        out += perm_sign(p)*(W@M@W.conj().T)
    return out/len(perms)


def vec(M): return M.reshape(-1)


def superoperator(dim,twirl):
    n=dim*dim
    S=np.zeros((n,n),complex)
    col=0
    for i in range(dim):
        for j in range(dim):
            M=np.zeros((dim,dim),complex); M[i,j]=1
            S[:,col]=vec(twirl(M)); col+=1
    return S


def cjson(z):
    z=complex(z); return [float(z.real),float(z.imag)]


def run():
    basis=S4.singlet_basis()
    perms=list(itertools.permutations(range(4)))
    reps=[S4.logical_representation(p,basis) for p in perms]

    one={name:sign_twirl_one(P,reps,perms) for name,P in S4.PAULI.items()}
    y_err=float(np.linalg.norm(one['Y']-S4.PAULI['Y']))
    one_forbidden=max(float(np.linalg.norm(one[a])) for a in ('I','X','Z'))

    S1=superoperator(2,lambda M: sign_twirl_one(M,reps,perms))
    rank1=int(np.linalg.matrix_rank(S1,tol=1e-10))
    proj1=float(np.linalg.norm(S1@S1-S1))

    cov1=0.0
    for U,p in zip(reps,perms):
        cov1=max(cov1,float(np.linalg.norm(U@S4.PAULI['Y']@U.conj().T-perm_sign(p)*S4.PAULI['Y'])))

    I,X,Y,Z=[S4.PAULI[a] for a in ('I','X','Y','Z')]
    IY=np.kron(I,Y)
    YI=np.kron(Y,I)
    XZmZX=np.kron(X,Z)-np.kron(Z,X)
    expected=[IY,YI,XZmZX]
    expected_names=['IY','YI','XZ-ZX']

    two_fix_errors=[float(np.linalg.norm(sign_twirl_two(M,reps,perms)-M)) for M in expected]
    two_cov_errors=[]
    for M in expected:
        e=0.0
        for U,p in zip(reps,perms):
            W=np.kron(U,U)
            e=max(e,float(np.linalg.norm(W@M@W.conj().T-perm_sign(p)*M)))
        two_cov_errors.append(e)

    S2=superoperator(4,lambda M: sign_twirl_two(M,reps,perms))
    rank2=int(np.linalg.matrix_rank(S2,tol=1e-10))
    proj2=float(np.linalg.norm(S2@S2-S2))
    ev2=np.linalg.eigvals(S2)
    eig1_2=int(np.sum(np.abs(ev2-1)<1e-9))

    gram=np.array([[np.trace(A.conj().T@B) for B in expected] for A in expected],complex)
    basis_rank=int(np.linalg.matrix_rank(gram,tol=1e-10))
    offdiag=float(np.linalg.norm(gram-np.diag(np.diag(gram))))

    B=np.column_stack([vec(M) for M in expected])
    max_span_resid=0.0
    product_results={}
    for a,A in S4.PAULI.items():
        for b,Bp in S4.PAULI.items():
            lab=a+b
            T=sign_twirl_two(np.kron(A,Bp),reps,perms)
            coef,*_=np.linalg.lstsq(B,vec(T),rcond=None)
            resid=float(np.linalg.norm(vec(T)-B@coef))
            max_span_resid=max(max_span_resid,resid)
            if np.linalg.norm(T)>1e-12:
                product_results[lab]={
                    'norm':float(np.linalg.norm(T)),
                    'basis_coefficients':{n:cjson(c) for n,c in zip(expected_names,coef)},
                    'span_residual':resid,
                }

    scalarY=S4.twirl_one(Y,reps)
    passed=(
        len(perms)==24 and rank1==1 and y_err<1e-12 and one_forbidden<1e-12
        and proj1<1e-12 and cov1<1e-12 and np.linalg.norm(scalarY)<1e-12
        and rank2==3 and eig1_2==3 and proj2<1e-12
        and max(two_fix_errors)<1e-12 and max(two_cov_errors)<1e-12
        and basis_rank==3 and offdiag<1e-12 and max_span_resid<1e-12
    )
    return {
        'status':'exact logical S4 sign-character twirl gate',
        'passed':bool(passed),
        'one_cell':{
            'sign_sector_dimension':rank1,
            'projector_idempotence_error':proj1,
            'Y_fixed_error':y_err,
            'I_X_Z_max_residual_norm':one_forbidden,
            'Y_sign_covariance_max_error':cov1,
            'ordinary_scalar_twirl_of_Y_norm':float(np.linalg.norm(scalarY)),
            'unique_channel':'Y',
        },
        'two_cell':{
            'sign_sector_dimension':rank2,
            'eigenvalue_one_multiplicity':eig1_2,
            'projector_idempotence_error':proj2,
            'basis':expected_names,
            'basis_fixed_errors':dict(zip(expected_names,two_fix_errors)),
            'basis_sign_covariance_errors':dict(zip(expected_names,two_cov_errors)),
            'basis_gram':[[cjson(z) for z in row] for row in gram],
            'basis_rank':basis_rank,
            'basis_offdiagonal_norm':offdiag,
            'max_generic_pauli_span_residual':max_span_resid,
            'nonzero_pauli_product_sign_twirl':product_results,
        },
        'representation_decomposition':'End(E)=A1(I)+A2(Y)+E(X,Z); two-cell diagonal sign sector = span{IY,YI,XZ-ZX}.',
        'lorentzian_consequence':(
            'If an epsilon-oriented one-cell/two-cell Lorentzian logical operator transforms with the S4 sign character, '
            'the one-cell part is proportional to Y and the two-cell part lies in span{IY,YI,XZ-ZX}. '
            'Ordinary scalar S4 channels {II,XX+ZZ,YY} and sign-covariant channels must not be conflated.'
        ),
        'scope':(
            'Finite exact representation theory only. The gate classifies orientation/epsilon-covariant operator '
            'channels and does not establish a nonzero physical Lorentzian amplitude or any additional interaction.'
        )
    }


if __name__=='__main__':
    out=run(); print(json.dumps(out,indent=2)); raise SystemExit(0 if out['passed'] else 1)
