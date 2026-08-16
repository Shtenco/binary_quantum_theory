#!/usr/bin/env python3
"""Collect the 16 exact relative E-depth2 pairs and analyze sparse Krylov growth.

The collector keeps A_r=E_r E_0, B_r=E_0 E_r and C_r=[E_0,E_r]
separate.  It forms union supports and exact small Gram spectra for each family.
No diffeomorphism target is supplied and no GR comparison is made.
"""
from __future__ import annotations
import argparse,json,math,traceback
from pathlib import Path
import numpy as np
REL=1e-10

def load_npz(p):
    d=np.load(p)
    return {(tuple(map(int,s)),tuple(map(int,k))):complex(a) for s,k,a in zip(d['spins'],d['Ks'],d['amp'])}
def inner(a,b):
    if len(a)>len(b):a,b=b,a
    return sum(np.conjugate(z)*b.get(k,0j) for k,z in a.items())
def gram_summary(states):
    G=np.empty((len(states),len(states)),complex)
    for i in range(len(states)):
      for j in range(i,len(states)):
        z=inner(states[i],states[j]);G[i,j]=z;G[j,i]=np.conjugate(z)
    H=.5*(G+G.conj().T);evals=np.linalg.eigvalsh(H);svals=np.sqrt(np.maximum(evals,0))[::-1];top=max(float(svals[0]),1e-300);rank=int(np.sum(svals/top>REL));union=set().union(*(s.keys() for s in states))
    return {'count':len(states),'union_support':len(union),'rank':rank,'gram_min_raw_eigenvalue':float(evals.min()),'gram_max_raw_eigenvalue':float(evals.max()),'singular_values_descending':[float(x) for x in svals]}
def run(root):
    root=Path(root);meta=[];A=[];B=[];C=[]
    for r in range(16):
        p=list(root.rglob(f'mask_{r}.json'))
        if len(p)!=1:raise RuntimeError((r,'metadata',p))
        d=json.loads(p[0].read_text());
        if not d.get('passed'):raise RuntimeError((r,'failed',d.get('error')))
        meta.append(d)
        def one(prefix):
            q=list(root.rglob(f'{prefix}_{r}.npz'))
            if len(q)!=1:raise RuntimeError((r,prefix,q))
            return load_npz(q[0])
        A.append(one('A'));B.append(one('B'));C.append(one('C'))
    sa=gram_summary(A);sb=gram_summary(B);sc=gram_summary(C)
    allstates=A+B;sd=gram_summary(allstates)
    comm_nonzero=sum(1 for x in C if inner(x,x).real>1e-20)
    selfzero=math.sqrt(max(float(inner(C[0],C[0]).real),0.0))
    checks={'all_16_masks_loaded':len(meta)==16,'A_and_B_rank_nonzero':sa['rank']>0 and sb['rank']>0,
            'self_commutator_zero':selfzero<1e-10,'commutators_nontrivial_away_from_self':comm_nonzero>1,
            'gram_numeric_PSD':min(sa['gram_min_raw_eigenvalue'],sb['gram_min_raw_eigenvalue'],sc['gram_min_raw_eigenvalue'],sd['gram_min_raw_eigenvalue'])>-1e-8}
    return {'status':'exact relative 16-cell Euclidean depth-2 sparse collector','passed':bool(all(checks.values())),'science_status':'E_DEPTH2_PRECURSOR',
            'checks':checks,'A_family_Er_E0':sa,'B_family_E0_Er':sb,'commutator_family':sc,'combined_ordered_depth2_family':sd,
            'nonzero_relative_commutators':comm_nonzero,'self_commutator_norm':selfzero,
            'per_mask':[{'mask':r,'A_support':meta[r]['A_Er_E0']['support'],'B_support':meta[r]['B_E0_Er']['support'],'C_support':meta[r]['commutator_B_minus_A']['support'],'C_norm':meta[r]['commutator_B_minus_A']['norm']} for r in range(16)],
            'interpretation':'This is the exact Euclidean depth-2 amplitude growth for the 16 relative node separations. It supplies the E-only second Krylov layer without using Lorentzian or GR target data.',
            'scope_note':'No XOR inference of missing operator orders; all A_r and B_r are direct. Translating relative pairs to all 256 ordered node pairs is a separate automorphism step.'}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    try:o=run(a.root);code=0 if o['passed'] else 1
    except Exception as exc:o={'status':'collector exception','passed':False,'error_type':type(exc).__name__,'error':str(exc),'traceback':traceback.format_exc()};code=1
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n');print(json.dumps(o,indent=2,sort_keys=True));return code
if __name__=='__main__':raise SystemExit(main())
