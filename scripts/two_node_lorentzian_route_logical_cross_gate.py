#!/usr/bin/env python3
"""Signed two-node logical Lorentzian x operator-first route cross.

This gate uses the exact 4x4 shared geometry metric from the same two-node route
sector as operator_first_two_node_route_hda_gate.py.  It intentionally does NOT
reuse the older one-node 2x2 averaged route coefficient, because

    sqrt((Q0+Q1)/2)

is nonlinear and generates two-node correlation terms.

For beta=hbar=1 the independently frozen full Lorentzian correction on one node
has logical coefficient

    G_L,node = g Y_node,   g=-4.760637696520545.

The gate angularly averages the exact positive 4x4 spectral square root and
computes

    C0=-i[G_L,0, Omega_shared],
    C1=-i[G_L,1, Omega_shared].

These are finite logical ordering regressions, not the full HDA commutator.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import operator_first_two_node_route_hda_gate as TWO
import lorentzian_route_logical_cross_gate as ONE

ROOT=Path(__file__).resolve().parents[1]
SIGN=ROOT/'verification_results/LORENTZIAN_REPO_SIGN.json'

I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],dtype=complex)
Y=np.array([[0,-1j],[1j,0]],dtype=complex)
Z=np.array([[1,0],[0,-1]],dtype=complex)
PAULI={'I':I,'X':X,'Y':Y,'Z':Z}


def sqrt_psd(A):
    H=0.5*(A+A.conj().T)
    vals,U=np.linalg.eigh(H)
    if vals.min()<-1e-10:
        raise RuntimeError(f'non-positive shared route block: {vals}')
    vals=np.maximum(vals,0.0)
    return (U*np.sqrt(vals))@U.conj().T


def decompose(M):
    out={}
    for a,A in PAULI.items():
        for b,B in PAULI.items():
            out[a+b]=np.trace(np.kron(A,B)@M)/4.0
    return out


def clean_coeff(c,tol=1e-12):
    return {k:[float(v.real),float(v.imag)] for k,v in c.items() if abs(v)>tol}


def swap_matrix():
    S=np.zeros((4,4),complex)
    for a in range(2):
        for b in range(2):
            S[2*b+a,2*a+b]=1
    return S


def angular_average_shared(n_theta):
    _,_,Q=TWO.shared_flux_gram_operator()
    O=np.zeros((4,4),complex)
    mineig=math.inf
    for n in range(n_theta):
        th=2*np.pi*n/n_theta
        p0,p1=math.cos(th),math.sin(th)
        A=p0*p0*Q[0][0]+p0*p1*(Q[0][1]+Q[1][0])+p1*p1*Q[1][1]
        vals=np.linalg.eigvalsh(0.5*(A+A.conj().T))
        mineig=min(mineig,float(vals.min()))
        O+=sqrt_psd(A)
    return O/n_theta,mineig


def coeff_norm(c,keys):
    return math.sqrt(sum(abs(c[k])**2 for k in keys))


def run(n_theta=32768):
    sign=json.loads(SIGN.read_text(encoding='utf-8'))
    if not sign.get('passed',False):
        raise RuntimeError('signed Lorentzian coefficient evidence not passed')
    g=float(sign['local_full_correction_coefficient'])
    O,mineig=angular_average_shared(n_theta)
    G0=g*np.kron(Y,I)
    G1=g*np.kron(I,Y)
    C0=-1j*(G0@O-O@G0)
    C1=-1j*(G1@O-O@G1)
    cO=decompose(O); c0=decompose(C0); c1=decompose(C1)
    S=swap_matrix()

    local0=coeff_norm(c0,('XI','ZI'))
    ent0=coeff_norm(c0,('XX','XZ','ZX','ZZ'))
    local1=coeff_norm(c1,('IX','IZ'))
    ent1=coeff_norm(c1,('XX','XZ','ZX','ZZ'))

    one=ONE.run()['signed_full_beta1_correction_cross']
    oneX=float(one['pauli']['X'][0]); oneZ=float(one['pauli']['Z'][0])
    naive0=oneX*np.kron(X,I)+oneZ*np.kron(Z,I)
    naive_rel=float(np.linalg.norm(C0-naive0)/max(np.linalg.norm(C0),1e-30))

    forbidden_O=[k for k in cO if 'Y' in k]
    forbidden_C0=[k for k in c0 if k[0] not in ('X','Z')]
    forbidden_C1=[k for k in c1 if k[1] not in ('X','Z')]

    checks={
        'signed_evidence_no_fit':sign.get('fitting_used') is False,
        'shared_symbol_positive':mineig>-1e-10,
        'Omega_hermitian':float(np.linalg.norm(O-O.conj().T))<1e-12,
        'Omega_no_Y_components':max((abs(cO[k]) for k in forbidden_O),default=0.0)<1e-11,
        'C0_hermitian':float(np.linalg.norm(C0-C0.conj().T))<1e-11,
        'C1_hermitian':float(np.linalg.norm(C1-C1.conj().T))<1e-11,
        'C0_only_XZ_on_acted_node':max((abs(c0[k]) for k in forbidden_C0),default=0.0)<1e-11,
        'C1_only_XZ_on_acted_node':max((abs(c1[k]) for k in forbidden_C1),default=0.0)<1e-11,
        'node_swap_covariance':float(np.linalg.norm(C1-S@C0@S))<1e-10,
        'cross_nonzero':float(np.linalg.norm(C0))>1e-3 and float(np.linalg.norm(C1))>1e-3,
        'entangling_cross_nonzero':ent0>1e-3 and ent1>1e-3,
        'local_entangling_norm_balance':abs(local0-ent0)<1e-9 and abs(local1-ent1)<1e-9,
        'one_node_coefficient_not_transplantable':naive_rel>0.9,
        'reference_XI':abs(c0['XI'].real+0.09539104)<5e-7,
        'reference_ZI':abs(c0['ZI'].real+0.16522213)<5e-7,
        'reference_XX':abs(c0['XX'].real+0.08261107)<5e-7,
    }

    return {
        'status':'signed two-node logical Lorentzian x operator-first shared-route cross',
        'passed':all(checks.values()),
        'beta':1.0,'hbar':1.0,'n_theta':n_theta,
        'full_Lorentzian_local_Y_coefficient':g,
        'minimum_shared_symbol_eigenvalue':mineig,
        'Omega_shared_pauli':clean_coeff(cO),
        'C0_identity':'-i[g Y0, Omega_shared]',
        'C0_pauli':clean_coeff(c0),
        'C1_identity':'-i[g Y1, Omega_shared]',
        'C1_pauli':clean_coeff(c1),
        'C0_frobenius_norm':float(np.linalg.norm(C0)),
        'C1_frobenius_norm':float(np.linalg.norm(C1)),
        'C0_local_XI_ZI_norm':local0,
        'C0_entangling_XX_XZ_ZX_ZZ_norm':ent0,
        'C1_local_IX_IZ_norm':local1,
        'C1_entangling_XX_XZ_ZX_ZZ_norm':ent1,
        'one_node_naive_embedded_cross_relative_mismatch':naive_rel,
        'one_node_regression_scope_correction':(
            'The older 2x2 coefficient is a one-node ordering diagnostic only. It must not be inserted as the two-node shared-route coefficient. '
            'The 4x4 shared square root generates additional entangling Pauli channels.'
        ),
        'checks':checks,
        'scope':'Finite angularly averaged logical regression. Off-shell spin-changing G x R_op regulator scaling remains open.',
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--n-theta',type=int,default=32768)
    p.add_argument('--output',type=Path)
    a=p.parse_args(); out=run(a.n_theta); text=json.dumps(out,indent=2,sort_keys=True); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__=='__main__': raise SystemExit(main())
