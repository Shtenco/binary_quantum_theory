#!/usr/bin/env python3
"""Collect all safe-cutoff Lorentzian environment blocks into the one-body trace.

For every ordered triple and every one of the 16 diagonal logical environment
states, the input blocks contain the source 2x2 logical matrix.  This collector
forms

  Lbar_0 = (1/16) sum_env sum_abc eps_abc M_abc(env)

which is exactly the source-node one-body coefficient obtained by partial trace
over the other four logical K5 qubits, restricted to the all-j=1/2 logical
sector.  Its Pauli-Y coefficient is the decisive environment-unbiased test of a
true one-cell orientation/pseudoscalar term.

Raw structural amplitude only: no final kappa/beta/hbar/i prefactor.
"""
from __future__ import annotations

import argparse
import itertools
import json
from collections import defaultdict
from pathlib import Path

import numpy as np

PAULI={
    'I':np.eye(2,dtype=complex),
    'X':np.array([[0,1],[1,0]],complex),
    'Y':np.array([[0,-1j],[1j,0]],complex),
    'Z':np.array([[1,0],[0,-1]],complex),
}


def cp(z):
    z=complex(z)
    return [float(z.real),float(z.imag)]


def mat(d,key='environment_sum_matrix'):
    return np.array([[complex(*d[key][i][j]) for j in range(2)] for i in range(2)],dtype=complex)


def coeffs(M):
    return {name:np.trace(P@M)/2.0 for name,P in PAULI.items()}


def run(root:Path):
    files=sorted(root.rglob('block_*.json'))
    per_triple=defaultdict(lambda:{'M':np.zeros((2,2),complex),'env':set(),'sign':None,'max_leak':0.0,'blocks':0})
    max_leak=0.0
    for f in files:
        d=json.loads(f.read_text(encoding='utf-8'))
        if not d.get('passed',False):
            raise RuntimeError(f'input block did not pass: {f}')
        t=tuple(int(x) for x in d['ordered_edges'])
        r=per_triple[t]
        sign=int(d['epsilon_coefficient'])
        if r['sign'] is None: r['sign']=sign
        if r['sign']!=sign: raise RuntimeError(f'inconsistent epsilon sign for {t}')
        envs=set(int(x) for x in d['environment_indices'])
        if r['env'] & envs: raise RuntimeError(f'duplicate environment for {t}: {r["env"] & envs}')
        r['env'] |= envs
        r['M'] += mat(d)
        r['blocks'] += 1
        leak=float(d['max_physical_basis_volume_leakage'])
        r['max_leak']=max(r['max_leak'],leak)
        max_leak=max(max_leak,leak)

    expected=set(itertools.permutations((1,2,3,4),3))
    complete=(set(per_triple)==expected and all(r['env']==set(range(16)) and r['blocks']==4 for r in per_triple.values()))
    if not complete:
        missing=sorted(expected-set(per_triple))
        bad={str(k):sorted(set(range(16))-v['env']) for k,v in per_triple.items() if v['env']!=set(range(16))}
        raise RuntimeError(f'incomplete evidence: missing_triples={missing}, missing_env={bad}')

    raw_sum=np.zeros((2,2),complex)
    triples=[]
    for t in sorted(expected):
        r=per_triple[t]
        avg=r['M']/16.0
        raw_sum += r['sign']*avg
        c=coeffs(avg)
        triples.append({
            'ordered_edges':list(t),
            'epsilon_coefficient':r['sign'],
            'environment_averaged_matrix':[[cp(avg[i,j]) for j in range(2)] for i in range(2)],
            'environment_averaged_frobenius_norm':float(np.linalg.norm(avg)),
            'environment_averaged_pauli':{k:cp(v) for k,v in c.items()},
            'max_leakage':r['max_leak'],
        })

    c=coeffs(raw_sum)
    Ysector=c['Y']*PAULI['Y']
    onebody_norm=float(np.linalg.norm(raw_sum))
    y_abs=float(abs(c['Y']))
    nonY=complex(c['I']),complex(c['X']),complex(c['Z'])
    nonY_norm=float(np.sqrt(sum(abs(z)**2 for z in nonY)))

    passed=bool(
        len(files)==96 and complete and max_leak<1e-8 and
        np.all(np.isfinite(raw_sum))
    )
    return {
        'status':'environment-unbiased safe-cutoff Lorentzian one-body logical trace',
        'passed':passed,
        'Jmax':3.5,
        'input_block_files':len(files),
        'ordered_triples':24,
        'environment_states_per_triple':16,
        'max_physical_basis_volume_leakage':max_leak,
        'definition':'Lbar_0=(1/16) sum_env sum_abc epsilon_abc <env|T_abc|env>',
        'onebody_raw_epsilon_matrix':[[cp(raw_sum[i,j]) for j in range(2)] for i in range(2)],
        'onebody_raw_epsilon_frobenius_norm':onebody_norm,
        'onebody_raw_pauli':{k:cp(v) for k,v in c.items()},
        'onebody_Y_coefficient':cp(c['Y']),
        'onebody_Y_abs':y_abs,
        'onebody_nonY_pauli_norm':nonY_norm,
        'onebody_sign_sector_matrix':[[cp(Ysector[i,j]) for j in range(2)] for i in range(2)],
        'onebody_sign_sector_norm':float(np.linalg.norm(Ysector)),
        'decision':(
            'NONZERO_TRUE_ONE_BODY_RAW_Y' if y_abs>1e-10 else 'ZERO_TRUE_ONE_BODY_RAW_Y_AT_TESTED_CUTOFF'
        ),
        'interpretation':(
            'This removes the frozen K=0 logical-environment bias. A nonzero Y coefficient is a genuine one-body '
            'raw structural pseudoscalar on the tested logical sector. A zero result means the frozen-boundary Y '
            'came entirely from environment-dependent multi-cell structure. In either case, the final physical H_L '
            'still requires the canonical prefactor/ordering and continuum/refinement checks.'
        ),
        'scope':'Finite all-j=1/2 logical partial trace at safe single-H_L cutoff Jmax=7/2; no physical mass/force claim.',
        'triples':triples,
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root',type=Path,required=True)
    p.add_argument('--output',type=Path)
    a=p.parse_args()
    out=run(a.root)
    txt=json.dumps(out,indent=2)
    print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
