#!/usr/bin/env python3
"""Meet-in-the-middle direct logical projection of the full epsilon Lorentzian raw sum.

The brute-force state-to-state gate applies

    C_a(K) C_b(K) C_c(V)

fully forward before projecting onto a logical target.  At Jmax=7/2 the third
C(K) expansion is the dominant cost.  For the raw operator used in the existing
Peter-Weyl stack,

    K_raw=[V,H_E^sine],          K_raw^dagger=-K_raw,
    C_e(K)=K-h_e K h_e^-1,

and unitary fundamental holonomy gives the operator-valued auxiliary-index
adjoint rule

    C_e(K)_{ij}^dagger = - C_e(K)_{ji}.

Therefore every matrix element can be contracted exactly as

 <f| C_a(K)_{ij} C_b(K)_{jk} C_c(V)_{ki} |i>
   = - < C_a(K)_{ji} f | C_b(K)_{jk} C_c(V)_{ki} i >.

This gate uses that identity to evaluate the complete 24-term epsilon-oriented
raw Lorentzian local logical 2x2 matrix without constructing the third-leg
forward sparse state.  It uses the same sine-ordered C(K), zero-aware volume,
Jmax=7/2 wall and leakage diagnostics as the brute-force research gate.

Important: this computes L_raw,epsilon, not the final physical Hermitian H_L
normalization.  Overall quantum prefactors are intentionally absent in the
underlying repository K/C(K) gates.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np

import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_lorentzian_logical_projection_gate as LP

JMAX2=7
TOL=1e-11

PAULI={
    'I':np.eye(2,dtype=complex),
    'X':np.array([[0,1],[1,0]],complex),
    'Y':np.array([[0,-1j],[1j,0]],complex),
    'Z':np.array([[1,0],[0,-1]],complex),
}


def sparse_inner(a,b):
    # <a|b> in the normalized covariant basis.
    if len(a)>len(b):
        return np.conj(sparse_inner(b,a))
    return sum(np.conj(x)*b.get(k,0j) for k,x in a.items())


def parity(base,perm):
    idx=[base.index(x) for x in perm]
    inv=sum(idx[i]>idx[j] for i in range(3) for j in range(i+1,3))
    return -1 if inv%2 else +1


def oriented_triples(source_v):
    neigh=PW.NEIG[source_v]
    rows=[]
    for r,omit in enumerate(neigh):
        base=tuple(x for x in neigh if x!=omit)
        face=(-1)**r
        for perm in itertools.permutations(base):
            rows.append((perm,face*parity(base,perm),omit))
    assert len(rows)==24 and len({p for p,_,_ in rows})==24
    return rows


def cpair(z): return [float(complex(z).real),float(complex(z).imag)]


def pauli_decompose(M):
    return {a:cpair(np.trace(A@M)/2.0) for a,A in PAULI.items()}


def sign_projection_coefficient_y(M):
    # In the logical basis the one-cell S4 sign sector is exactly span{Y}.
    return complex(np.trace(PAULI['Y']@M)/2.0)


def run(source_v=0,Jmax2=JMAX2):
    LP.JMAX2=Jmax2
    restore,caches=LP.install_sine_cached_stack()
    try:
        spins=(1,)*len(PW.EDGES)
        env=[0]*len(PW.VERT)
        logicalK=(0,2)

        gauss=[]; cov=[]
        for K in logicalK:
            Ks=list(env); Ks[source_v]=K
            key=(spins,tuple(Ks))
            gauss.append(key)
            cov.append(LP.CV.gauss_to_covariant({key:1+0j},source_v))

        neighbors=PW.NEIG[source_v]
        triples=oriented_triples(source_v)

        # Backward one-C(K) states: B[f,a,j,i]=C_a(K)_{ji}|f>.
        backward={}
        max_outer=max_v=max_charge=0.0
        for f in range(2):
            for a in neighbors:
                for j,i in itertools.product(range(2),repeat=2):
                    st,d=LP.RAW.KCOMP.C_K_component(cov[f],source_v,a,j,i,Jmax2)
                    backward[(f,a,j,i)]=st
                    max_outer=max(max_outer,float(d['outer_complete_basis_leakage']))
                    max_v=max(max_v,float(d['internal_volume_sector_leakage']))
                    max_charge=max(max_charge,float(d['complete_charge_basis_leakage']))

        # C(V) states, reused by all triples containing the same c.
        cv={}
        max_cv=0.0
        for q in range(2):
            for c in neighbors:
                for k,i in itertools.product(range(2),repeat=2):
                    st,leak=LP.RAW.COMP.C_volume_component(cov[q],source_v,c,k,i,Jmax2)
                    cv[(q,c,k,i)]=st
                    max_cv=max(max_cv,float(leak))

        # Forward two-leg states F[q,b,c,i,j,k]=C_b(K)_{jk} C_c(V)_{ki}|q>.
        # Only b!=c can occur in the epsilon assembler.
        forward={}
        for q in range(2):
            for b in neighbors:
                for c in neighbors:
                    if b==c: continue
                    for i,j,k in itertools.product(range(2),repeat=3):
                        s1=cv[(q,c,k,i)]
                        if not s1:
                            forward[(q,b,c,i,j,k)]={}
                            continue
                        s2,d=LP.RAW.KCOMP.C_K_component(s1,source_v,b,j,k,Jmax2)
                        # Match the existing sine-ordered triple scalar-path control.
                        s2={key:amp for key,amp in s2.items() if key[2] in (0,2)}
                        forward[(q,b,c,i,j,k)]=s2
                        max_outer=max(max_outer,float(d['outer_complete_basis_leakage']))
                        max_v=max(max_v,float(d['internal_volume_sector_leakage']))
                        max_charge=max(max_charge,float(d['complete_charge_basis_leakage']))

        M=np.zeros((2,2),complex)
        triple_contrib=[]
        for (a,b,c),coef,omit in triples:
            T=np.zeros((2,2),complex)
            for f,q in itertools.product(range(2),repeat=2):
                z=0j
                for i,j,k in itertools.product(range(2),repeat=3):
                    B=backward[(f,a,j,i)]
                    F=forward[(q,b,c,i,j,k)]
                    if B and F:
                        z -= sparse_inner(B,F)
                T[f,q]=z
            M += coef*T
            triple_contrib.append({
                'ordered_edges':[a,b,c],
                'omitted_neighbor':omit,
                'epsilon_coefficient':coef,
                'matrix':[[cpair(T[r,s]) for s in range(2)] for r in range(2)],
                'frobenius_norm':float(np.linalg.norm(T)),
            })

        coeff=pauli_decompose(M)
        ycoef=sign_projection_coefficient_y(M)
        herm=float(np.linalg.norm(M-M.conj().T))
        anti=float(np.linalg.norm(M+M.conj().T))
        physical_leak=max(max_cv,max_outer,max_v)

        cache_info={}
        for name,fn in caches.items():
            ci=fn.cache_info()
            cache_info[name]={'hits':ci.hits,'misses':ci.misses,'currsize':ci.currsize}

        # The historical primitive charge-basis diagnostic is deliberately not
        # a hard criterion, matching the validated sine-ordered triple gate.
        passed=(
            len(triples)==24
            and physical_leak<1e-8
            and np.all(np.isfinite(M))
        )

        return {
            'status':'meet-in-the-middle direct logical projection of full epsilon-oriented raw Lorentzian K-K-V sum',
            'passed':bool(passed),
            'source_node':source_v,
            'Jmax':Jmax2/2,
            'input_environment':'all other logical K=0; source K in {0,2}',
            'method_identity':'<f|C_a(K)_ij C_b(K)_jk C_c(V)_ki|q> = -<C_a(K)_ji f|C_b(K)_jk C_c(V)_ki q>',
            'oriented_triple_count':len(triples),
            'local_2x2_raw_matrix':[[cpair(M[r,s]) for s in range(2)] for r in range(2)],
            'local_2x2_frobenius_norm':float(np.linalg.norm(M)),
            'raw_projection_nonzero':bool(np.linalg.norm(M)>1e-10),
            'raw_pauli_coefficients':coeff,
            'S4_sign_channel_Y_coefficient':cpair(ycoef),
            'S4_sign_channel_Y_abs':float(abs(ycoef)),
            'hermiticity_defect_norm':herm,
            'antihermiticity_defect_norm':anti,
            'physical_acceptance_max_leakage':physical_leak,
            'diagnostics':{
                'CV_complete_basis_leakage':max_cv,
                'CK_outer_complete_basis_leakage':max_outer,
                'CK_internal_volume_sector_leakage':max_v,
                'CK_historical_complete_charge_basis_diagnostic':max_charge,
                'historical_charge_diagnostic_is_hard_acceptance':False,
            },
            'precomputed_state_counts':{
                'backward_CK':len(backward),
                'CV':len(cv),
                'forward_CK_after_CV':len(forward),
            },
            'cache_info':cache_info,
            'triple_contributions':triple_contrib,
            'interpretation':(
                'Nonzero establishes a genuine safe-cutoff raw Lorentzian logical return in the frozen environment. '
                'The displayed Y coefficient is the projection onto the unique one-cell S4 sign-character channel. '
                'Neither number is yet a physical H_L mass because the repository raw K/C(K) gates omit overall quantum prefactors and the final Hermitian Lorentzian completion is not fixed here.'
            ),
            'scope':(
                'Finite candidate-model amplitude calculation. No final Hermitian H_L normalization, no unbiased environment trace, no route/matter sector and no physical mirror-force claim.'
            ),
        }
    finally:
        restore()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--node',type=int,default=0)
    ap.add_argument('--jmax2',type=int,default=7)
    ap.add_argument('--output',type=Path)
    a=ap.parse_args(); out=run(a.node,a.jmax2); txt=json.dumps(out,indent=2); print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__=='__main__': raise SystemExit(main())
