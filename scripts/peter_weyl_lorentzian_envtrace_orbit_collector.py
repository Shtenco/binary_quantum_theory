#!/usr/bin/env python3
"""Fast exact S4-orbit collector for the unbiased Lorentzian one-body term.

After tracing the four neighboring logical qubits with I_env/16, local face
permutations are restored.  The 24 ordered triples form one S4 orbit of T_123.
With the preregistered convention epsilon(123)=-1,

  L_eps,1body = - sum_{p in S4} sgn(p) U_p Tbar_123 U_p^dagger
               = -24 T_sgn(Tbar_123).

The exact logical S4 representation is the same one used by the proved sign-
twirl gate.  Tbar_132 is also computed from independent Peter-Weyl environment
blocks and compared with U_(23) Tbar_123 U_(23)^dagger as a nontrivial covariance
check.

Raw structural amplitudes only; no final kappa/beta/hbar/i prefactor.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import numpy as np

import logical_s4_twirl_gate as S4

PAULI=S4.PAULI


def cp(z):
    z=complex(z); return [float(z.real),float(z.imag)]


def mfrom(d):
    return np.array([[complex(*d['environment_sum_matrix'][i][j]) for j in range(2)] for i in range(2)],complex)


def parity(p):
    inv=sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j])
    return -1 if inv%2 else 1


def coeffs(M):
    return {k:np.trace(P@M)/2 for k,P in PAULI.items()}


def load_avg(root,triple):
    rows=[]; M=np.zeros((2,2),complex); env=set(); maxleak=0.0
    for f in root.rglob('block_*.json'):
        d=json.loads(f.read_text(encoding='utf-8'))
        if tuple(d['ordered_edges'])!=tuple(triple): continue
        if not d.get('passed',False): raise RuntimeError(f'failed block {f}')
        e=set(d['environment_indices'])
        if env & e: raise RuntimeError(f'duplicate env for {triple}: {env&e}')
        env |= e; M += mfrom(d); rows.append(str(f))
        maxleak=max(maxleak,float(d['max_physical_basis_volume_leakage']))
    if env!=set(range(16)) or len(rows)!=4:
        raise RuntimeError(f'incomplete {triple}: env={sorted(env)}, files={len(rows)}')
    return M/16.0,maxleak


def run(root):
    T123,l1=load_avg(root,(1,2,3))
    T132,l2=load_avg(root,(1,3,2))
    basis=S4.singlet_basis()
    perms=list(itertools.permutations(range(4)))
    reps={p:S4.logical_representation(p,basis) for p in perms}

    swap=(0,2,1,3)
    pred132=reps[swap]@T123@reps[swap].conj().T
    cov_err=float(np.linalg.norm(T132-pred132)/max(np.linalg.norm(T132),np.linalg.norm(pred132),1e-30))

    sign_twirl=np.zeros((2,2),complex)
    for p in perms:
        U=reps[p]
        sign_twirl += parity(p)*(U@T123@U.conj().T)
    sign_twirl/=24.0
    full=-24.0*sign_twirl

    c123=coeffs(T123); csign=coeffs(sign_twirl); cfull=coeffs(full)
    nonY_sign=np.sqrt(sum(abs(csign[k])**2 for k in ('I','X','Z')))
    passed=bool(
        max(l1,l2)<1e-8 and cov_err<1e-8 and
        abs(csign['Y'])>1e-10 and nonY_sign<1e-10 and np.all(np.isfinite(full))
    )
    return {
        'status':'S4-orbit environment-unbiased Lorentzian one-body collector',
        'passed':passed,
        'Jmax':3.5,
        'environment_states':16,
        'T123_environment_average':[[cp(T123[i,j]) for j in range(2)] for i in range(2)],
        'T123_pauli':{k:cp(v) for k,v in c123.items()},
        'T132_environment_average':[[cp(T132[i,j]) for j in range(2)] for i in range(2)],
        'T132_from_S4_covariance':[[cp(pred132[i,j]) for j in range(2)] for i in range(2)],
        'T132_covariance_relative_error':cov_err,
        'sign_twirl_T123':[[cp(sign_twirl[i,j]) for j in range(2)] for i in range(2)],
        'sign_twirl_pauli':{k:cp(v) for k,v in csign.items()},
        'full_24term_onebody_from_orbit':[[cp(full[i,j]) for j in range(2)] for i in range(2)],
        'full_24term_onebody_frobenius_norm':float(np.linalg.norm(full)),
        'full_24term_onebody_pauli':{k:cp(v) for k,v in cfull.items()},
        'onebody_Y_coefficient_raw':cp(cfull['Y']),
        'onebody_Y_abs_raw':float(abs(cfull['Y'])),
        'max_physical_basis_volume_leakage':max(l1,l2),
        'identity':'L_eps,1body=-24*T_sgn(Tbar_123), epsilon(123)=-1',
        'decision':'NONZERO_TRUE_ONE_BODY_RAW_Y' if abs(cfull['Y'])>1e-10 else 'ZERO_TRUE_ONE_BODY_RAW_Y',
        'scope':'Exact finite logical environment trace plus S4 orbit reduction at Jmax=7/2; structural raw coefficient only, not final physical H_L normalization.',
    }


def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--root',type=Path,required=True); p.add_argument('--output',type=Path); a=p.parse_args()
    out=run(a.root); txt=json.dumps(out,indent=2); print(txt)
    if a.output: a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
