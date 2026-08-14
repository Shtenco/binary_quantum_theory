#!/usr/bin/env python3
"""Safe Jmax=7/2 logical 2x2 matrix of ONE real Lorentzian ordered triple via meet-in-the-middle.

For T_abc=Tr_aux[C_a(K)C_b(K)C_c(V)] and raw K=[V,H_E^sine],
C(K) is anti-Hermitian as an operator-valued auxiliary matrix:

    C(K)_ij^dagger=-C(K)_ji.

Hence

    <f|T_abc|q>
      =-sum_ijk < C_a(K)_ji f |
                    C_b(K)_jk C_c(V)_ki q >.

This avoids the expensive third forward C(K) expansion and computes the exact
logical matrix element at the same preregistered Jmax=7/2 cutoff.  It tests one
ordered triple only, not the 24-term epsilon-oriented Lorentzian node sum.
"""
from __future__ import annotations

import argparse,itertools,json
from pathlib import Path
import numpy as np

import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_lorentzian_logical_projection_gate as LP

PAULI={
 'I':np.eye(2,dtype=complex),
 'X':np.array([[0,1],[1,0]],complex),
 'Y':np.array([[0,-1j],[1j,0]],complex),
 'Z':np.array([[1,0],[0,-1]],complex),
}

def inner(a,b):
    return sum(np.conj(x)*b.get(k,0j) for k,x in a.items())

def cp(z): z=complex(z); return [float(z.real),float(z.imag)]

def run(source_v=0,Jmax2=7):
    LP.JMAX2=Jmax2
    restore,caches=LP.install_sine_cached_stack()
    try:
        neigh=PW.NEIG[source_v]; a,b,c=neigh[:3]
        spins=(1,)*len(PW.EDGES)
        logical=[]
        for K in (0,2):
            Ks=[0]*len(PW.VERT); Ks[source_v]=K
            key=(spins,tuple(Ks))
            logical.append(LP.CV.gauss_to_covariant({key:1+0j},source_v))

        # Backward target states C_a(K)_ji |f>.
        back={}; max_outer=max_vol=max_charge=0.0
        for f in range(2):
            for j,i in itertools.product(range(2),repeat=2):
                s,d=LP.RAW.KCOMP.C_K_component(logical[f],source_v,a,j,i,Jmax2)
                back[(f,j,i)]=s
                max_outer=max(max_outer,float(d['outer_complete_basis_leakage']))
                max_vol=max(max_vol,float(d['internal_volume_sector_leakage']))
                max_charge=max(max_charge,float(d['complete_charge_basis_leakage']))

        M=np.zeros((2,2),complex); max_cv=0.0
        path_rows=[]
        for q in range(2):
            for i,j,k in itertools.product(range(2),repeat=3):
                s1,lv=LP.RAW.COMP.C_volume_component(logical[q],source_v,c,k,i,Jmax2)
                max_cv=max(max_cv,float(lv))
                if s1:
                    s2,d=LP.RAW.KCOMP.C_K_component(s1,source_v,b,j,k,Jmax2)
                    max_outer=max(max_outer,float(d['outer_complete_basis_leakage']))
                    max_vol=max(max_vol,float(d['internal_volume_sector_leakage']))
                    max_charge=max(max_charge,float(d['complete_charge_basis_leakage']))
                    s2={key:amp for key,amp in s2.items() if key[2] in (0,2)}
                else:
                    s2={}
                vals=[]
                for f in range(2):
                    z=-inner(back[(f,j,i)],s2) if s2 else 0j
                    M[f,q]+=z; vals.append(cp(z))
                path_rows.append({
                    'input_K2':[0,2][q], 'indices':[i,j,k],
                    'after_CV_support':len(s1), 'after_middle_CK_scalar_support':len(s2),
                    'target_contributions':vals,
                })

        coeff={name:cp(np.trace(P@M)/2.0) for name,P in PAULI.items()}
        physical_leak=max(max_cv,max_outer,max_vol)
        out={
            'status':'safe Jmax=7/2 one-triple Lorentzian logical MITM gate',
            'passed':bool(physical_leak<1e-8 and np.all(np.isfinite(M))),
            'source_node':source_v,'ordered_edges':[a,b,c],'Jmax':Jmax2/2,
            'identity':'<f|C_a(K)_ij C_b(K)_jk C_c(V)_ki|q>=-<C_a(K)_ji f|C_b(K)_jk C_c(V)_ki q>',
            'logical_2x2_matrix':[[cp(M[r,s]) for s in range(2)] for r in range(2)],
            'frobenius_norm':float(np.linalg.norm(M)),
            'any_logical_return':bool(np.linalg.norm(M)>1e-10),
            'pauli_coefficients':coeff,
            'physical_acceptance_max_leakage':physical_leak,
            'historical_charge_diagnostic':max_charge,
            'historical_charge_is_hard_acceptance':False,
            'path_rows':path_rows,
            'scope':'One ordered triple, safe cutoff. No 24-term epsilon sum, no final Hermitian H_L prefactor and no physical mass/force claim.'
        }
        return out
    finally:
        restore()

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--output',type=Path); args=ap.parse_args()
    o=run(); txt=json.dumps(o,indent=2); print(txt)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
