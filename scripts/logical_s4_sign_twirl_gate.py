#!/usr/bin/env python3
"""Exact S4 sign-character twirl on the logical four-spin singlet qubit.

The ordinary one-cell S4 twirl selects scalar operators and leaves only I.
An oriented epsilon contraction instead transforms with the sign character under
odd face permutations.  The appropriate projector on operator space is

    T_sgn(O)=(1/24) sum_g sgn(g) U_g O U_g^dagger.

For the two-dimensional [2,2] singlet representation of S4, End(V) decomposes
as A1 + A2 + E.  This gate verifies that the A2/sign sector is exactly the
one-dimensional logical Y channel:

    T_sgn(Y)=Y,
    T_sgn(I)=T_sgn(X)=T_sgn(Z)=0.

This is a representation-theory statement.  It does not prove that a given
Lorentzian amplitude is nonzero or that the final Hermitian Hamiltonian contains
a physical one-cell Y field.  It only fixes the unique possible sign-covariant
one-cell logical operator if an epsilon-oriented projection survives.
"""
from __future__ import annotations

import itertools
import json
import math
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


def vec(M): return M.reshape(-1)


def sign_superoperator(reps,perms):
    S=np.zeros((4,4),dtype=complex)
    E=[]
    for i in range(2):
        for j in range(2):
            M=np.zeros((2,2),complex); M[i,j]=1
            E.append(M)
    for c,M in enumerate(E):
        S[:,c]=vec(sign_twirl_one(M,reps,perms))
    return S


def cjson(z):
    z=complex(z); return [float(z.real),float(z.imag)]


def run():
    basis=S4.singlet_basis()
    perms=list(itertools.permutations(range(4)))
    reps=[S4.logical_representation(p,basis) for p in perms]

    tw={name:sign_twirl_one(P,reps,perms) for name,P in S4.PAULI.items()}
    y_err=float(np.linalg.norm(tw['Y']-S4.PAULI['Y']))
    forbidden=max(float(np.linalg.norm(tw[a])) for a in ('I','X','Z'))

    Sup=sign_superoperator(reps,perms)
    ev=np.linalg.eigvals(Sup)
    rank=int(np.linalg.matrix_rank(Sup,tol=1e-10))
    projector_error=float(np.linalg.norm(Sup@Sup-Sup))
    eig1=int(np.sum(np.abs(ev-1)<1e-9))

    # Covariance control: Y must transform exactly with permutation sign.
    cov_err=0.0
    for U,p in zip(reps,perms):
        cov_err=max(cov_err,float(np.linalg.norm(U@S4.PAULI['Y']@U.conj().T-perm_sign(p)*S4.PAULI['Y'])))

    # Ordinary scalar and sign projectors must be orthogonal.
    scalarY=S4.twirl_one(S4.PAULI['Y'],reps)
    scalar_sign_overlap=float(np.linalg.norm(scalarY))

    passed=(
        len(perms)==24 and y_err<1e-12 and forbidden<1e-12
        and rank==1 and eig1==1 and projector_error<1e-12
        and cov_err<1e-12 and scalar_sign_overlap<1e-12
    )
    return {
        'status':'exact logical S4 sign-character twirl gate',
        'passed':bool(passed),
        'permutation_count':len(perms),
        'sign_twirl_rank':rank,
        'sign_twirl_eigenvalue_one_multiplicity':eig1,
        'projector_idempotence_error':projector_error,
        'Y_fixed_error':y_err,
        'I_X_Z_max_residual_norm':forbidden,
        'Y_sign_covariance_max_error':cov_err,
        'ordinary_scalar_twirl_of_Y_norm':scalar_sign_overlap,
        'sign_twirl_pauli':{k:[[cjson(z) for z in row] for row in M] for k,M in tw.items()},
        'unique_sign_covariant_channel':'Y',
        'representation_decomposition':'End(E_[2,2]) = A1(I) + A2(Y) + E(X,Z)',
        'lorentzian_consequence':(
            'If the full epsilon-oriented Lorentzian one-cell operator transforms with the S4 sign character, '
            'its logical sign-covariant projection is proportional to Y and no I/X/Z sign-channel survives.'
        ),
        'mirror_note':(
            'This does not by itself break mirror/orientation covariance: an orientation pseudoscalar coefficient '
            'and logical Y both change sign under frame reversal, so their product can be scalar.'
        ),
        'scope':'Exact finite representation theory only; no nonzero P H_L P amplitude or physical mass/force is claimed.'
    }


if __name__=='__main__':
    out=run(); print(json.dumps(out,indent=2)); raise SystemExit(0 if out['passed'] else 1)
