#!/usr/bin/env python3
"""Parameterized safe Jmax=7/2 logical matrix for one ordered Lorentzian triple.

For any distinct source-neighbor triple (a,b,c), compute

    T_abc = P Tr_aux[C_a(K) C_b(K) C_c(V)] P

on the source logical K={0,2} basis with the other K5 logical nodes frozen to
K=0.  The third C(K) is contracted meet-in-the-middle using

    C(K)_ij^dagger=-C(K)_ji

for raw K=[V,H_E^sine].  This is the same exact contraction used by the validated
single-triple MITM gate, now parameterized so the 24 epsilon-oriented terms can
be evaluated independently and assembled linearly afterwards.
"""
from __future__ import annotations
import argparse,itertools,json
from pathlib import Path
import numpy as np
import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_lorentzian_logical_projection_gate as LP

PAULI={
 'I':np.eye(2,dtype=complex),'X':np.array([[0,1],[1,0]],complex),
 'Y':np.array([[0,-1j],[1j,0]],complex),'Z':np.array([[1,0],[0,-1]],complex)
}
def inner(a,b):
    if len(a)>len(b): return np.conj(inner(b,a))
    return sum(np.conj(v)*b.get(k,0j) for k,v in a.items())
def cp(z): z=complex(z); return [float(z.real),float(z.imag)]

def run(a,b,c,source=0,jmax2=7):
    neigh=PW.NEIG[source]
    if len({a,b,c})!=3 or any(x not in neigh for x in (a,b,c)):
        raise ValueError(f'(a,b,c) must be distinct neighbors of source {source}: {neigh}')
    LP.JMAX2=jmax2
    restore,_=LP.install_sine_cached_stack()
    try:
        spins=(1,)*len(PW.EDGES); logical=[]
        for K in (0,2):
            Ks=[0]*len(PW.VERT); Ks[source]=K
            key=(spins,tuple(Ks)); logical.append(LP.CV.gauss_to_covariant({key:1+0j},source))
        back={}; max_outer=max_vol=max_charge=max_cv=0.0
        for f in range(2):
            for j,i in itertools.product(range(2),repeat=2):
                s,d=LP.RAW.KCOMP.C_K_component(logical[f],source,a,j,i,jmax2)
                back[(f,j,i)]=s
                max_outer=max(max_outer,float(d['outer_complete_basis_leakage']))
                max_vol=max(max_vol,float(d['internal_volume_sector_leakage']))
                max_charge=max(max_charge,float(d['complete_charge_basis_leakage']))
        M=np.zeros((2,2),complex)
        for q in range(2):
            for i,j,k in itertools.product(range(2),repeat=3):
                s1,lv=LP.RAW.COMP.C_volume_component(logical[q],source,c,k,i,jmax2)
                max_cv=max(max_cv,float(lv))
                if s1:
                    s2,d=LP.RAW.KCOMP.C_K_component(s1,source,b,j,k,jmax2)
                    max_outer=max(max_outer,float(d['outer_complete_basis_leakage']))
                    max_vol=max(max_vol,float(d['internal_volume_sector_leakage']))
                    max_charge=max(max_charge,float(d['complete_charge_basis_leakage']))
                    s2={key:amp for key,amp in s2.items() if key[2] in (0,2)}
                else: s2={}
                if s2:
                    for f in range(2): M[f,q] -= inner(back[(f,j,i)],s2)
        physical=max(max_cv,max_outer,max_vol)
        coeff={name:cp(np.trace(P@M)/2.0) for name,P in PAULI.items()}
        return {
          'status':'parameterized safe ordered Lorentzian MITM logical matrix','passed':bool(physical<1e-8 and np.all(np.isfinite(M))),
          'source_node':source,'ordered_edges':[a,b,c],'Jmax':jmax2/2,
          'logical_2x2_matrix':[[cp(M[r,s]) for s in range(2)] for r in range(2)],
          'frobenius_norm':float(np.linalg.norm(M)),'any_logical_return':bool(np.linalg.norm(M)>1e-10),
          'pauli_coefficients':coeff,'physical_acceptance_max_leakage':physical,
          'historical_charge_diagnostic':max_charge,'historical_charge_is_hard_acceptance':False,
          'scope':'One ordered triple at safe cutoff; no epsilon assembly, final Hermitian prefactor, mass or force claim.'
        }
    finally: restore()

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--a',type=int,required=True); p.add_argument('--b',type=int,required=True); p.add_argument('--c',type=int,required=True); p.add_argument('--coefficient',type=int,default=1); p.add_argument('--output',type=Path); x=p.parse_args()
    o=run(x.a,x.b,x.c); o['epsilon_coefficient']=x.coefficient; t=json.dumps(o,indent=2); print(t)
    if x.output: x.output.parent.mkdir(parents=True,exist_ok=True); x.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
