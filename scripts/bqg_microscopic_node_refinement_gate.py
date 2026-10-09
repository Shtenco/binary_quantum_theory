#!/usr/bin/env python3
"""Microscopic node-refinement bridge: q=2 ancillas -> canonical j=1/2 -> j=1 W.

At each of the four incident edges:
  old V_{1/2} + fresh ancilla V_{1/2} -> symmetric V_1.

The four fresh ancillas are placed in a Gauss-singlet state chi living in the
same two-dimensional Inv[(1/2)^⊗4] space.

For each ancilla singlet basis vector chi_a and each old singlet basis vector,
we block edgewise and project the resulting tensor onto the j=1 singlet basis.
This yields two 3x2 maps T_a.  We test whether the already registered canonical
S4-[2,2] intertwiner W lies in span{T_0,T_1}; if yes, we recover the required
ancilla singlet coefficients directly from the binary microscopic construction.
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import peter_weyl_j1_s4_block_gate as J1
from bqg_ancilla_peter_weyl_refinement_gate import inclusion

TOL=1e-11

def blocking_coisometry():
    # n=1: J: V_1 -> V_1/2 \otimes V_1/2 ; B=J^dagger.
    J=inclusion(1)
    return J.conj().T.reshape(3,2,2)

def blocked_tensor(old,anc,B):
    # old[a,b,c,d], anc[e,f,g,h], B[A,a,e] ... -> coarse[A,B,C,D]
    return np.einsum(
        "Aae,Bbf,Ccg,Ddh,abcd,efgh->ABCD",
        B,B,B,B,old,anc,
        optimize=True,
    )

def run():
    kf,tf=J1.local_basis(1)  # K2=(0,2)
    kc,tc=J1.local_basis(2)  # K2=(0,2,4)
    assert tuple(kf)==(0,2)
    assert tuple(kc)==(0,2,4)

    B=blocking_coisometry()

    maps=[]
    leakage=[]
    for anc in tf:
        T=np.zeros((3,2),complex)
        leak=0.0
        for j,old in enumerate(tf):
            out=blocked_tensor(old,anc,B)
            coeff=np.array([np.vdot(c,out) for c in tc],complex)
            T[:,j]=coeff
            proj=sum(coeff[i]*tc[i] for i in range(3))
            leak += float(np.vdot(out-proj,out-proj).real)
        maps.append(T)
        leakage.append(leak)

    W=np.column_stack([
        np.array([0.0,1.0,0.0],complex),
        np.array([2/3,0.0,-np.sqrt(5)/3],complex),
    ])

    A=np.column_stack([maps[0].reshape(-1),maps[1].reshape(-1)])
    wvec=W.reshape(-1)
    coeff,resid,rank,svals=np.linalg.lstsq(A,wvec,rcond=None)
    rec=coeff[0]*maps[0]+coeff[1]*maps[1]
    abs_err=float(np.linalg.norm(rec-W))
    rel_err=abs_err/float(np.linalg.norm(W))

    # Normalize ancilla state coefficients and separate overall map amplitude.
    cnorm=float(np.linalg.norm(coeff))
    anc_coeff=(coeff/cnorm) if cnorm>0 else coeff
    Tnorm=anc_coeff[0]*maps[0]+anc_coeff[1]*maps[1]
    # best scalar alpha with alpha*Tnorm ~ W
    alpha=np.vdot(Tnorm,W)/np.vdot(Tnorm,Tnorm)
    phase_fixed=alpha*Tnorm
    final_err=float(np.linalg.norm(phase_fixed-W))

    # Check that each microscopic map lands in the j=1 Gauss singlet sector.
    total_leak=float(sum(leakage))

    return {
      "status":"microscopic q2-ancilla four-valent node refinement test",
      "passed":bool(rel_err<1e-9 and final_err<1e-9 and total_leak<1e-9),
      "fine_K2_basis":list(kf),
      "coarse_K2_basis":list(kc),
      "ancilla_K2_basis":list(kf),
      "T_ancilla_basis":[
        [[float(z.real),float(z.imag)] for z in T.reshape(-1)]
        for T in maps
      ],
      "least_squares_rank":int(rank),
      "singular_values":[float(x) for x in svals],
      "raw_coefficients":[[float(z.real),float(z.imag)] for z in coeff],
      "normalized_ancilla_coefficients":[[float(z.real),float(z.imag)] for z in anc_coeff],
      "overall_map_amplitude":[float(alpha.real),float(alpha.imag)],
      "relative_reconstruction_error":rel_err,
      "phase_fixed_error":final_err,
      "Gauss_projection_leakage_sum":total_leak,
      "canonical_W":[[float(z.real),float(z.imag)] for z in W.reshape(-1)],
      "claim_boundary":"Tests whether the known canonical local S4 [2,2] refinement map is induced by adding a four-qubit Gauss-singlet ancilla and edgewise symmetric q=2 blocking. It does not yet prove that the microscopic Hamiltonian dynamically prepares the required ancilla singlet."
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path)
    a=ap.parse_args()
    out=run(); txt=json.dumps(out,indent=2); print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(txt+"\n",encoding="utf-8")
    return 0 if out["passed"] else 2

if __name__=="__main__":
    raise SystemExit(main())
