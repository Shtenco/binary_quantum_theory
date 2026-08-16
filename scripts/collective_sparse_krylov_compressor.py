#!/usr/bin/env python3
"""Target-independent sparse Gram/whitening compressor for collective columns.

Input is a directory tree of JSON column files with a common microscopic seed
and rows ``spins,Ks,re,im``.  The compressor never constructs the full Hilbert
space.  It forms only the union of actually reached Peter-Weyl keys, the small
raw-column Gram matrix, and a canonical spectral whitening map.

The first production use is the 16 exact E_v|Omega_0> columns on the 16-cell.
The same algorithm is intended for the later E+S+R+depth2 column set.
"""
from __future__ import annotations
import argparse,json,math
from collections import Counter
from pathlib import Path
import numpy as np
REL=1e-10

def decode(d):
    return {(tuple(r['spins']),tuple(r['Ks'])):complex(r['re'],r['im']) for r in d['column']}

def load(root,pattern='node_*.json'):
    rows=[]
    for p in sorted(Path(root).rglob(pattern)):
        d=json.loads(p.read_text(encoding='utf-8'))
        if not d.get('passed'):raise RuntimeError(f'failed input column {p}')
        if 'column' not in d:continue
        rows.append((p,d,decode(d)))
    if not rows:raise RuntimeError(f'no column JSON matching {pattern} below {root}')
    seeds={(tuple(d['seed']['spins']),tuple(d['seed']['Ks'])) for _,d,_ in rows}
    if len(seeds)!=1:raise RuntimeError(f'columns do not share one seed: {len(seeds)} seeds')
    return rows,next(iter(seeds))

def analyze(root,pattern='node_*.json'):
    rows,seed=load(root,pattern);cols=[c for _,_,c in rows]
    keys=sorted(set().union(*(c.keys() for c in cols)),key=repr);ki={k:i for i,k in enumerate(keys)}
    A=np.zeros((len(keys),len(cols)),complex)
    for j,c in enumerate(cols):
        for k,z in c.items():A[ki[k],j]=z
    gram=A.conj().T@A;gh=.5*(gram+gram.conj().T)
    evals,U=np.linalg.eigh(gh);svals=np.sqrt(np.maximum(evals,0))[::-1]
    top=max(float(svals[0]),1e-300);rank=int(np.sum(svals/top>REL))
    keep=evals>max(float(evals.max()),1e-300)*REL**2
    Ukeep=U[:,keep];lam=evals[keep]
    whiten=Ukeep@np.diag(1/np.sqrt(lam))
    W=A@whiten
    orth=float(np.linalg.norm(W.conj().T@W-np.eye(W.shape[1])))
    recon=W@(W.conj().T@A)
    rerr=float(np.linalg.norm(recon-A)/max(np.linalg.norm(A),1e-300))
    seed_overlap=np.asarray([c.get(seed,0j) for c in cols])
    seed_overlap_norm=float(np.linalg.norm(seed_overlap))
    seed_in_union=seed in ki
    if seed_in_union:
        sv=np.zeros(len(keys),complex);sv[ki[seed]]=1
        seed_projection=float(np.linalg.norm(W.conj().T@sv))
        seed_residual=math.sqrt(max(0.0,1-seed_projection**2))
    else:
        seed_projection=0.0;seed_residual=1.0
    changed=Counter();mxspin=Counter();changedK=Counter()
    for spins,Ks in keys:
        changed[sum(s!=1 for s in spins)]+=1
        mxspin[max(spins) if spins else 0]+=1
        changedK[sum(x!=0 for x in Ks)]+=1
    positive=evals[evals>0]
    cond=float(positive.max()/positive.min()) if len(positive) else math.inf
    checks={
      'all_columns_independent_at_frozen_relative_threshold':rank==len(cols),
      'positive_definite_raw_gram':float(evals.min())>1e-12,
      'whitened_basis_orthonormal':orth<1e-12,
      'raw_columns_reconstructed':rerr<1e-12,
      'seed_exactly_outside_E_union':not seed_in_union and seed_overlap_norm<1e-14,
    }
    return {
      'status':'target-independent sparse collective Krylov compressor',
      'passed':bool(all(checks.values())),'science_status':'E_ONLY_PRECURSOR',
      'svd_relative_threshold':REL,'input_columns':len(cols),'input_files':[str(p) for p,_,_ in rows],
      'union_support':len(keys),'raw_column_rank':rank,
      'gram_eigenvalues_ascending':[float(x) for x in evals],
      'gram_condition_number':cond,'raw_singular_values_descending':[float(x) for x in svals],
      'whitened_basis_dimension':int(W.shape[1]),'whitened_orthonormality_defect_fro':orth,
      'raw_column_reconstruction_relative_error':rerr,
      'seed_in_union_support':seed_in_union,'seed_overlap_norm':seed_overlap_norm,
      'seed_projection_norm_into_whitened_span':seed_projection,'seed_residual_norm':seed_residual,
      'seed_plus_column_span_dimension':int(W.shape[1]+(1 if seed_residual>1e-12 else 0)),
      'changed_edge_count_distribution':{str(k):int(v) for k,v in sorted(changed.items())},
      'max_doubled_spin_distribution':{str(k):int(v) for k,v in sorted(mxspin.items())},
      'changed_K_node_count_distribution':{str(k):int(v) for k,v in sorted(changedK.items())},
      'checks':checks,
      'interpretation':'The exact reached-state union is Gram-whitened without embedding it into an exponentially large dense Hilbert space. The whitening coefficients are sufficient to reconstruct an orthonormal effective embedding from the raw sparse columns.',
      'scope_note':'E-only first use. Do not promote this 17-dimensional seed+E space to production W0 until Hermitian S, route and target-independent depth-2 images/leakage are added.'
    },gram,evals,U,whiten

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,required=True);p.add_argument('--pattern',default='node_*.json');p.add_argument('--json-output',type=Path,required=True);p.add_argument('--npz-output',type=Path,required=True);a=p.parse_args()
    out,G,e,U,W=analyze(a.root,a.pattern);txt=json.dumps(out,indent=2);print(txt)
    a.json_output.parent.mkdir(parents=True,exist_ok=True);a.json_output.write_text(txt+'\n',encoding='utf-8')
    a.npz_output.parent.mkdir(parents=True,exist_ok=True);np.savez_compressed(a.npz_output,gram=G,eigenvalues=e,eigenvectors=U,whitener=W)
    return 0 if out['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
