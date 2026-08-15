#!/usr/bin/env python3
"""Reconstruct conditional Lorentzian multi-node Walsh coefficients.

Input mode
----------
Point --input-dir at 24 JSON block files from one envtrace batch. Each file
must represent one unique ordered triple, carry the frozen epsilon coefficient,
and contain the same environment indices. For the canonical node-0 batch-0
artifacts those indices are 0,1,2,3, corresponding to the complete K1/K2
binary cube with K3=K4=0.

Frozen-evidence mode
--------------------
Without --input-dir, validate the committed machine evidence against the
canonical numerical anchors. This makes the recovered result part of ordinary
repository regression even though the historical Actions artifacts themselves
are not committed.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],dtype=complex)
Y=np.array([[0,-1j],[1j,0]],dtype=complex)
Z=np.diag([1,-1]).astype(complex)
PAULI={'I':I,'X':X,'Y':Y,'Z':Z}

ANCHORS={
    'onebody_local':0.33709171624286727,
    'source_x_node1':0.03631787483605024,
    'source_x_node2':0.006983526478664483,
    'source_x_node1node2':0.01396705295732858,
}
Y_ANCHORS={
    'YI1I2':0.3359014033398999j,
    'YZ1I2':-0.00702861722247964j,
    'YI1Z2':0.002338130606598994j,
    'YZ1Z2':0.004676261213197787j,
}


def cpair(x):
    return complex(float(x[0]),float(x[1]))


def matrix(rows):
    return np.asarray([[cpair(rows[r][c]) for c in range(2)] for r in range(2)],dtype=complex)


def norm_coeff(d,keys):
    return math.sqrt(sum(abs(d.get(k,0j))**2 for k in keys))


def reconstruct(input_dir:Path):
    files=sorted(input_dir.rglob('*.json'))
    blocks=[]
    for p in files:
        d=json.loads(p.read_text(encoding='utf-8'))
        if 'ordered_edges' in d and 'environments' in d:
            blocks.append((p,d))
    triples=[tuple(d['ordered_edges']) for _,d in blocks]
    if len(blocks)!=24 or len(set(triples))!=24:
        raise RuntimeError(f'require 24 unique triple blocks, got {len(blocks)} files / {len(set(triples))} triples')
    if not all(bool(d.get('passed',False)) for _,d in blocks):
        raise RuntimeError('one or more source blocks did not pass their original gate')
    envsets={tuple(d['environment_indices']) for _,d in blocks}
    if len(envsets)!=1:
        raise RuntimeError(f'inconsistent environment sets: {envsets}')
    envs=next(iter(envsets))
    if tuple(envs)!=(0,1,2,3):
        raise RuntimeError(f'canonical Walsh gate requires environments 0,1,2,3; got {envs}')

    M={e:np.zeros((2,2),dtype=complex) for e in envs}
    max_leak=0.0
    for _,d in blocks:
        coef=int(d['epsilon_coefficient'])
        max_leak=max(max_leak,float(d['max_physical_basis_volume_leakage']))
        for row in d['environments']:
            M[int(row['environment_index'])]+=coef*matrix(row['logical_2x2_matrix'])

    A={
        'I1I2':(M[0]+M[1]+M[2]+M[3])/4,
        'Z1I2':(M[0]-M[1]+M[2]-M[3])/4,
        'I1Z2':(M[0]+M[1]-M[2]-M[3])/4,
        'Z1Z2':(M[0]-M[1]-M[2]+M[3])/4,
    }
    coeff={}
    for suffix,B in A.items():
        for a,P in PAULI.items():
            z=np.trace(P@B)/2
            if abs(z)>1e-12:
                coeff[a+suffix]=complex(z)

    groups={
        'onebody_local':norm_coeff(coeff,('II1I2','XI1I2','YI1I2','ZI1I2')),
        'source_x_node1':norm_coeff(coeff,('IZ1I2','XZ1I2','YZ1I2','ZZ1I2')),
        'source_x_node2':norm_coeff(coeff,('II1Z2','XI1Z2','YI1Z2','ZI1Z2')),
        'source_x_node1node2':norm_coeff(coeff,('IZ1Z2','XZ1Z2','YZ1Z2','ZZ1Z2')),
    }
    reconstruction=[]
    for e in range(4):
        z1=1 if not (e&1) else -1
        z2=1 if not ((e>>1)&1) else -1
        R=A['I1I2']+z1*A['Z1I2']+z2*A['I1Z2']+z1*z2*A['Z1Z2']
        reconstruction.append(float(np.linalg.norm(R-M[e])))

    checks={
        '24_unique_triples':len(blocks)==24 and len(set(triples))==24,
        'worker_leakage':max_leak<1e-12,
        'reconstruction':max(reconstruction)<2e-16,
        'group_anchors':all(abs(groups[k]-v)<1e-13 for k,v in ANCHORS.items()),
        'Y_anchors':all(abs(coeff.get(k,0j)-v)<1e-13 for k,v in Y_ANCHORS.items()),
    }
    return {
        'status':'reconstructed exact conditional Lorentzian environment Walsh gate',
        'passed':all(checks.values()),
        'triple_count':len(blocks),
        'group_norms':groups,
        'raw_pauli':{k:[float(v.real),float(v.imag)] for k,v in coeff.items()},
        'reconstruction_errors':reconstruction,
        'max_leakage':max_leak,
        'checks':checks,
        'scope':'Diagonal logical environments 0..3 only; off-diagonal environment transitions are not reconstructed.'
    }


def frozen_check(path:Path):
    d=json.loads(path.read_text(encoding='utf-8'))
    coeff={k:cpair(v) for k,v in d['raw_pauli'].items()}
    groups={k:float(v) for k,v in d['group_norms'].items()}
    checks={
        'evidence_passed':bool(d.get('passed',False)),
        '24_unique_triples_recorded':int(d.get('triple_count',0))==24,
        'worker_leakage':float(d['max_leakage'])<1e-12,
        'reconstruction':max(map(float,d['reconstruction_errors']))<2e-16,
        'group_anchors':all(abs(groups[k]-v)<1e-13 for k,v in ANCHORS.items()),
        'Y_anchors':all(abs(coeff.get(k,0j)-v)<1e-13 for k,v in Y_ANCHORS.items()),
        'scope_is_diagonal': 'off-diagonal' in d.get('scope','').lower(),
    }
    return {
        'status':'frozen conditional Lorentzian environment Walsh regression',
        'passed':all(checks.values()),
        'group_norms':groups,
        'Y_coefficients':{k:[float(coeff[k].real),float(coeff[k].imag)] for k in Y_ANCHORS},
        'checks':checks,
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input-dir',type=Path)
    p.add_argument('--evidence',type=Path,default=Path('verification_results/PETER_WEYL_LORENTZIAN_ENVTRACE_WALSH_NODE012.json'))
    p.add_argument('--output',type=Path)
    a=p.parse_args()
    out=reconstruct(a.input_dir) if a.input_dir else frozen_check(a.evidence)
    text=json.dumps(out,indent=2,sort_keys=True)
    print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
