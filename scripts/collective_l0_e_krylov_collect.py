#!/usr/bin/env python3
"""Collect 16 distributed exact L0 E-columns and build the amplitude Krylov Gram/SVD."""
from __future__ import annotations
import argparse,json,math,sys
from collections import defaultdict
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
from pl_dual_complex import DualComplex,seed_16cell_boundary

SVD_REL=1e-10

def decode(rows):
    out={}
    for r in rows:
        out[(tuple(r['spins']),tuple(r['Ks']))]=complex(r['re'],r['im'])
    return out

def inner(a,b):
    if len(a)>len(b):a,b=b,a
    return sum(np.conjugate(x)*b.get(k,0j) for k,x in a.items())

def norm(a):return math.sqrt(max(float(inner(a,a).real),0.0))

def q4_distance(D,a,b):
    if a==b:return 0
    seen={a};front={a};d=0
    while front:
        d+=1;nxt=set()
        for v in front:nxt.update(D.neighbor[(v,r)] for r in range(4))
        if b in nxt:return d
        nxt-=seen;seen|=nxt;front=nxt
    raise RuntimeError('disconnected')

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args()
    files=sorted(a.root.rglob('node_*.json'))
    rows=[]
    for p in files:
        d=json.loads(p.read_text());
        if not d.get('passed'):raise RuntimeError(f'failed column {p}')
        rows.append(d)
    bynode={int(d['node']):d for d in rows}
    if sorted(bynode)!=list(range(16)):raise RuntimeError(('need nodes 0..15',sorted(bynode)))
    cols=[decode(bynode[i]['column']) for i in range(16)]
    norms=[norm(c) for c in cols]
    G=np.empty((16,16),complex)
    for i in range(16):
        for j in range(i,16):
            z=inner(cols[i],cols[j]);G[i,j]=z;G[j,i]=np.conjugate(z)
    Gh=(G+G.conj().T)/2
    herm=float(np.linalg.norm(G-G.conj().T)/max(np.linalg.norm(G),1e-30))
    raw_evals=np.linalg.eigvalsh(Gh);evals=np.maximum(raw_evals,0.0)
    svals=np.sqrt(evals[::-1]);smax=max(float(svals[0]),1e-300)
    rank=int(np.sum(svals/smax>SVD_REL))
    D=DualComplex(seed_16cell_boundary())
    bydist=defaultdict(list)
    for i in range(16):
        for j in range(i,16):
            bydist[q4_distance(D,i,j)].append(G[i,j]/max(norms[i]*norms[j],1e-300))
    dist={};spread=0.0
    for k,v in sorted(bydist.items()):
        arr=np.asarray(v);mu=arr.mean();sp=float(np.max(np.abs(arr-mu)));spread=max(spread,sp)
        dist[str(k)]={'count':len(v),'mean_re':float(mu.real),'mean_im':float(mu.imag),'max_abs_spread':sp}
    seed_parity=(-1)**32
    wrong=0
    for c in cols:
        wrong+=sum(((-1)**sum(k[0]))==seed_parity for k in c)
    const={}
    for c in cols:
        for k,z in c.items():const[k]=const.get(k,0j)+z
    const={k:z for k,z in const.items() if abs(z)>1e-10}
    checks={'all_16_columns_loaded':len(cols)==16,'gram_hermitian':herm<1e-12,
            'positive_gram':float(raw_evals.min())>-1e-9,
            'uniform_local_norms':max(norms)-min(norms)<1e-10,
            'q4_distance_covariance':spread<1e-10,'seed_E_parity_orthogonal':wrong==0,'nonzero_krylov_rank':rank>0}
    out={'status':'exact distributed L0 amplitude-level Euclidean Krylov precursor',
         'passed':bool(all(checks.values())),'science_status':'AMPLITUDE_PRECURSOR_E_ONLY','checks':checks,
         'nodes':16,'svd_relative_threshold':SVD_REL,'local_support_sizes':[len(c) for c in cols],
         'local_norms':norms,'constant_lapse_support':len(const),'constant_lapse_norm':norm(const),
         'gram_hermitian_relative_defect':herm,'gram_eigenvalues_ascending':[float(x) for x in evals],
         'amplitude_singular_values_descending':[float(x) for x in svals],
         'amplitude_krylov_rank':rank,'q4_normalized_gram_by_distance':dist,
         'q4_max_covariance_spread':spread,'wrong_seed_parity_outputs':wrong,
         'interpretation':'This is the target-independent dimension and singular spectrum of span{E_v|Omega_0>} from sixteen independently computed exact complex PL Peter-Weyl columns.',
         'scope_note':'E-only depth-1 precursor; production W0 still requires S, R and depth-2 histories.'}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2));return 0 if out['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
