#!/usr/bin/env python3
"""Kernel-safety certificate for singular operator-first route symbols."""
from __future__ import annotations
import argparse, json, math, sys
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_euclidean_sine_ordering_gate as SINE
import peter_weyl_operator_route_block_engine as BLK

TOL_EIG=1e-10
TOL_CHECK=1e-10
CARRIER=8


def symbol_and_derivative(Q,p,c):
    p0,p1=map(float,p)
    A=(p0*p0*Q[0][0]
       +p0*p1*(Q[0][1]+Q[1][0])
       +p1*p1*Q[1][1])
    A=0.5*(A+A.conj().T)
    dA=np.zeros_like(A)
    Qp=np.zeros_like(A)
    for b,pb in enumerate((p0,p1)):
        dA += pb*(Q[c][b]+Q[b][c])
        Qp += pb*Q[c][b]
    return A,0.5*(dA+dA.conj().T),Qp


def sylvester_solution(A,dA):
    lam,U=np.linalg.eigh(A)
    lam=np.maximum(lam,0.0)
    om=np.sqrt(lam)
    D=U.conj().T@dA@U
    X=np.zeros_like(D)
    for r in range(len(om)):
        for s in range(len(om)):
            den=om[r]+om[s]
            if den>1e-11:
                X[r,s]=D[r,s]/den
    X=U@X@U.conj().T
    Om=(U*om)@U.conj().T
    residual=np.linalg.norm(Om@X+X@Om-dA)
    return lam,U,Om,X,float(residual)


def run():
    initial=PW.basis_full_jhalf()[0]
    he=SINE.safe_H_sine({initial:1+0j},0,5)
    sectors=[];seen=set()
    for key,_amp in sorted(he.items(),key=lambda kv:abs(kv[1]),reverse=True):
        sec=BLK.sector_id(key)
        if sec not in seen:
            seen.add(sec);sectors.append(sec)

    modes=[(CARRIER+i,CARRIER-1+j) for i in range(-2,3) for j in range(-2,3)]
    min_eig=math.inf
    max_qp_kernel=0.0
    max_kernel_dA=0.0
    max_syl=0.0
    singular_cases=0
    derivative_rows=0

    for sec in sectors:
        Q=BLK.shared_Q(sec)
        for p in modes:
            # Kernel is common to A for both directional derivatives.
            A,_,_=symbol_and_derivative(Q,p,0)
            vals,U=np.linalg.eigh(A)
            min_eig=min(min_eig,float(vals.min()))
            ker=np.where(vals<TOL_EIG)[0]
            if len(ker):
                singular_cases+=1
            P0=U[:,ker] if len(ker) else np.zeros((A.shape[0],0),complex)
            for c in (0,1):
                derivative_rows+=1
                A,dA,Qp=symbol_and_derivative(Q,p,c)
                if len(ker):
                    max_qp_kernel=max(max_qp_kernel,float(np.linalg.norm(Qp@P0)))
                    max_kernel_dA=max(max_kernel_dA,float(np.linalg.norm(P0.conj().T@dA@P0)))
                _lam,_U,_Om,_X,res=sylvester_solution(A,dA)
                max_syl=max(max_syl,res)

    checks={
        'all_33_reached_sectors_checked':len(sectors)==33,
        'all_25_modes_checked':len(modes)==25,
        'singular_cases_actually_present':singular_cases>0,
        'symbols_positive_semidefinite_up_to_roundoff':min_eig>-TOL_EIG,
        'Qp_annihilates_kernel':max_qp_kernel<TOL_CHECK,
        'kernel_kernel_derivative_block_zero':max_kernel_dA<TOL_CHECK,
        'sylvester_equation_solvable':max_syl<TOL_CHECK,
    }
    checks={k:bool(v) for k,v in checks.items()}
    return {
        'status':'operator-first route singular-kernel Sylvester safety',
        'passed':all(checks.values()),
        'HE_basis_outputs':len(he),
        'reached_distinct_sectors':len(sectors),
        'momentum_modes':len(modes),
        'derivative_rows':derivative_rows,
        'singular_cases':singular_cases,
        'minimum_symbol_eigenvalue':float(min_eig),
        'max_Qp_on_kernel':float(max_qp_kernel),
        'max_kernel_dA_block':float(max_kernel_dA),
        'max_sylvester_residual':float(max_syl),
        'checks':checks,
        'theorem':'For A=sum_i B_i^dagger B_i, ker(A)=intersection ker(B_i), hence P0 (partial A) P0=0 and Omega X+X Omega=partial A is solvable even for singular Omega=sqrt(A).',
        'scope':'Kernel-safe principal anticommutator on all declared one-step H_E-reached finite blocks; not a claim of global Frechet differentiability across arbitrary rank-changing families.'
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path)
    a=p.parse_args();out=run();text=json.dumps(out,indent=2,sort_keys=True);print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
