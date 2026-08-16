#!/usr/bin/env python3
"""Collect 24 exact L1 fine-node E columns in one canonical coarse block.

Compute the exact sparse Gram/rank in the full fine Peter-Weyl Hilbert space and
report how much of the reached support changes block-boundary representations.
No internal contraction or coarse target basis is assumed.
"""
from __future__ import annotations
import argparse,json,math,traceback
from collections import Counter
from pathlib import Path
import numpy as np
REL=1e-10

def dec(d):return {(tuple(r['spins']),tuple(r['Ks'])):complex(r['re'],r['im']) for r in d['column']}
def inner(a,b):
    if len(a)>len(b):a,b=b,a
    return sum(np.conjugate(z)*b.get(k,0j) for k,z in a.items())
def run(root):
    rows=[]
    for p in Path(root).rglob('node_*.json'):
        d=json.loads(p.read_text());
        if d.get('passed') and 'column' in d:rows.append((int(d['local_fine_index']),d,dec(d)))
    rows=sorted(rows)
    if [i for i,_,_ in rows]!=list(range(24)):raise RuntimeError(('need local indices 0..23',[i for i,_,_ in rows]))
    cols=[c for _,_,c in rows];G=np.empty((24,24),complex)
    for i in range(24):
      for j in range(i,24):
        z=inner(cols[i],cols[j]);G[i,j]=z;G[j,i]=np.conjugate(z)
    H=.5*(G+G.conj().T);evals=np.linalg.eigvalsh(H);s=np.sqrt(np.maximum(evals,0))[::-1];rank=int(np.sum(s/max(float(s[0]),1e-300)>REL));union=set().union(*(c.keys() for c in cols))
    boundary_edges=[tuple(e) for e in rows[0][1]['parent_boundary_dual_links']]
    # Edge ordering is common because every worker uses the same deterministic G.EDGES.
    # Recover indices from any state length using the global edge pairs encoded only in metadata is not possible here;
    # boundary-pattern counts were therefore already computed per worker and are aggregated as direct diagnostics.
    norms=[r[1]['norm'] for r in rows];patterns=[r[1]['distinct_boundary_spin_patterns'] for r in rows]
    herm=float(np.linalg.norm(G-G.conj().T));mine=float(evals.min());cond=float(evals.max()/max(mine,1e-300)) if mine>0 else math.inf
    checks={'all_24_fine_nodes':len(rows)==24,'Gram_Hermitian':herm<1e-12,'Gram_numeric_PSD':mine>-1e-9,'amplitude_rank_nonzero':rank>0,
            'every_column_nonzero':all(n>1e-12 for n in norms),'every_worker_used_24_boundary_links':all(len(r[1]['parent_boundary_dual_links'])==24 for r in rows)}
    return {'status':'exact L1 canonical-block Euclidean fine-Hilbert Krylov Gram','passed':bool(all(checks.values())),'science_status':'L1_BLOCK_E_PRECURSOR',
            'parent_coarse_tetra':0,'fine_nodes':24,'global_L1_nodes':rows[0][1]['L1_nodes'],'global_L1_dual_links':rows[0][1]['L1_dual_links'],
            'union_support':len(union),'amplitude_rank':rank,'Gram_Hermiticity_defect':herm,'Gram_min_eigenvalue':mine,'Gram_condition_number':cond,
            'Gram_eigenvalues_ascending':[float(x) for x in evals],'singular_values_descending':[float(x) for x in s],
            'column_norm_min':min(norms),'column_norm_max':max(norms),'distinct_boundary_spin_patterns_per_node':patterns,
            'checks':checks,
            'interpretation':'This is the first exact dynamical tangent span on an actual barycentric refinement level inside one 24-chamber coarse block. It lives in the full fine Hilbert space and therefore cannot yet be identified with the coarse boundary/metric tangent rank.',
            'scope_note':'The next required map is explicit internal-link contraction / boundary isometry. Do not feed this fine-Hilbert rank directly into the GR constraint-rank killer.'}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    try:o=run(a.root);code=0 if o['passed'] else 1
    except Exception as exc:o={'status':'collector exception','passed':False,'error_type':type(exc).__name__,'error':str(exc),'traceback':traceback.format_exc()};code=1
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(o,indent=2)+'\n');print(json.dumps(o,indent=2));return code
if __name__=='__main__':raise SystemExit(main())
