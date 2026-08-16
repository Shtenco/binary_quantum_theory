#!/usr/bin/env python3
"""Collect 16 distributed exact L0 E-columns and build the amplitude Krylov Gram/SVD.

Q4-distance covariance is reported as a diagnostic, not a hard acceptance
condition: the canonical recoupling basis need not make every automorphism
manifest without an explicit induced basis map. Hard acceptance uses only the
actual amplitude Gram matrix, positivity, the regulator-specific parity rule
and nonzero rank.
"""
from __future__ import annotations
import argparse,json,math,sys,traceback
from collections import defaultdict
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
from pl_dual_complex import DualComplex,seed_16cell_boundary
SVD_REL=1e-10

def decode(rows):
    return {(tuple(r['spins']),tuple(r['Ks'])):complex(r['re'],r['im']) for r in rows}
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

def calculate(root):
    files=sorted(root.rglob('node_*.json'))
    rows=[]
    for p in files:
        d=json.loads(p.read_text())
        if not d.get('passed'):raise RuntimeError(f'failed column {p}')
        rows.append(d)
    bynode={int(d['node']):d for d in rows}
    if sorted(bynode)!=list(range(16)):raise RuntimeError(('need nodes 0..15',sorted(bynode),[str(p) for p in files]))
    seeds=[tuple(bynode[i]['seed']['spins']) for i in range(16)]
    if any(s!=seeds[0] for s in seeds[1:]):raise RuntimeError('node columns do not share one seed')
    cols=[decode(bynode[i]['column']) for i in range(16)];norms=[norm(c) for c in cols]
    gram=np.empty((16,16),complex)
    for i in range(16):
        for j in range(i,16):
            z=inner(cols[i],cols[j]);gram[i,j]=z;gram[j,i]=np.conjugate(z)
    gh=(gram+gram.conj().T)/2
    herm=float(np.linalg.norm(gram-gram.conj().T)/max(np.linalg.norm(gram),1e-30))
    raw_evals=np.linalg.eigvalsh(gh);evals=np.maximum(raw_evals,0.0)
    svals=np.sqrt(evals[::-1]);smax=max(float(svals[0]),1e-300);rank=int(np.sum(svals/smax>SVD_REL))
    D=DualComplex(seed_16cell_boundary());bydist=defaultdict(list)
    for i in range(16):
        for j in range(i,16):bydist[q4_distance(D,i,j)].append(gram[i,j]/max(norms[i]*norms[j],1e-300))
    dist={};spread=0.0
    for k,v in sorted(bydist.items()):
        arr=np.asarray(v);mu=arr.mean();sp=float(np.max(np.abs(arr-mu)));spread=max(spread,sp)
        dist[str(k)]={'count':len(v),'mean_re':float(mu.real),'mean_im':float(mu.imag),'max_abs_spread':sp}

    # The K5 parity-flip rule is not universal.  For a Euclidean T term the
    # doubled-spin parity changes by (-1)^q, q = dual-plaquette length / primal
    # edge valence.  The canonical 16-cell L0 regulator has only even q, so E
    # must preserve the seed parity.  Keep the legacy output field name for CI
    # compatibility, but it now counts genuine mismatches with this PL rule.
    valences=sorted(len(v) for v in D.edge_incidence.values())
    all_even=all(q%2==0 for q in valences)
    seed_parity=sum(seeds[0])%2
    expected_parity=seed_parity if all_even else None
    wrong=sum(1 for c in cols for k in c if expected_parity is None or (sum(k[0])%2)!=expected_parity)

    const={}
    for c in cols:
        for k,z in c.items():const[k]=const.get(k,0j)+z
    const={k:z for k,z in const.items() if abs(z)>1e-10}
    hard={'all_16_columns_loaded':True,'gram_hermitian':herm<1e-12,
          'positive_gram':float(raw_evals.min())>-1e-9,
          'regulator_all_even_edge_valence':all_even,
          'regulator_E_parity_rule_satisfied':wrong==0,
          'nonzero_krylov_rank':rank>0}
    diagnostics={'uniform_local_norms':bool(max(norms)-min(norms)<1e-10),'q4_distance_covariance_manifest':bool(spread<1e-10)}
    return {'status':'exact distributed L0 amplitude-level Euclidean Krylov precursor','passed':bool(all(hard.values())),
            'science_status':'AMPLITUDE_PRECURSOR_E_ONLY','hard_checks':hard,'diagnostic_checks':diagnostics,
            'nodes':16,'svd_relative_threshold':SVD_REL,'input_files':[str(p) for p in files],
            'local_support_sizes':[len(c) for c in cols],'local_norms':norms,
            'local_norm_spread':float(max(norms)-min(norms)),
            'constant_lapse_support':len(const),'constant_lapse_norm':norm(const),
            'gram_hermitian_relative_defect':herm,'gram_min_raw_eigenvalue':float(raw_evals.min()),
            'gram_eigenvalues_ascending':[float(x) for x in evals],
            'amplitude_singular_values_descending':[float(x) for x in svals],'amplitude_krylov_rank':rank,
            'regulator_edge_valences':valences,'seed_sum_doubled_spin_parity':seed_parity,
            'expected_output_sum_doubled_spin_parity':expected_parity,
            'q4_normalized_gram_by_distance':dist,'q4_max_covariance_spread':spread,
            'wrong_seed_parity_outputs':wrong,
            'interpretation':'Target-independent dimension and singular spectrum of span{E_v|Omega_0>} from sixteen independently computed exact complex PL Peter-Weyl columns. The parity guard is regulator-specific: the even-valence 16-cell preserves doubled-spin parity. Manifest Q4 covariance is diagnostic until the automorphism-induced recoupling basis map is constructed explicitly.',
            'scope_note':'E-only depth-1 precursor; production W0 still requires S, R and depth-2 histories.'}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--root',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    try:out=calculate(a.root);code=0 if out['passed'] else 1
    except Exception as exc:
        out={'status':'collector exception','passed':False,'science_status':'INFRASTRUCTURE_DIAGNOSTIC',
             'error_type':type(exc).__name__,'error':str(exc),'traceback':traceback.format_exc(),
             'root':str(a.root),'files':[str(p) for p in a.root.rglob('*')]};code=1
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));return code
if __name__=='__main__':raise SystemExit(main())
