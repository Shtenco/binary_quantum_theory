#!/usr/bin/env python3
"""Exact amplitude-level depth-1 Euclidean Krylov image on the 16-cell L0 carrier.

This is the first target-independent collective effective-basis measurement built
from actual complex Peter-Weyl amplitudes rather than support reachability.
For the homogeneous all-j=1/2, K=0 seed |Omega_0>, compute all sixteen local
physical-sine columns E_v|Omega_0>, form their exact sparse Gram matrix and
publish its complete singular spectrum/rank.

No GR target, DeWitt coefficient, dimensional target, TT count or HDA residual
enters the basis construction.  This is an E-only precursor to the production
G+R depth-2 Krylov basis; it MUST NOT be supplied as a complete science row to
the collective universality killer.
"""
from __future__ import annotations
import argparse,json,math,sys
from collections import defaultdict
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
from pl_dual_complex import DualComplex,seed_16cell_boundary
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean

TOL=1e-10
SVD_REL=1e-10
JMAX2=3  # one E from j=1/2 reaches at most j=3/2 conservatively; actual seed support is smaller


def inner(a,b):
    if len(a)>len(b):a,b=b,a
    return sum(np.conjugate(x)*b.get(k,0j) for k,x in a.items())

def norm(a):return math.sqrt(max(float(inner(a,a).real),0.0))

def add(dst,src,scale=1.0):
    for k,a in src.items():
        z=dst.get(k,0j)+scale*a
        if abs(z)>TOL:dst[k]=z
        elif k in dst:del dst[k]

def q4_distance(D,a,b):
    if a==b:return 0
    seen={a};front={a};d=0
    while front:
        d+=1;nxt=set()
        for v in front:
            nxt.update(D.neighbor[(v,r)] for r in range(4))
        if b in nxt:return d
        nxt-=seen;seen|=nxt;front=nxt
    raise RuntimeError('disconnected dual graph')

def run():
    D=DualComplex(seed_16cell_boundary());G=PLPeterWeylEuclidean(D)
    seed=((1,)*len(G.EDGES),(0,)*D.n_tets)
    cols=[G.H_sine_basis(seed,v,JMAX2,TOL) for v in range(D.n_tets)]
    if any(not c for c in cols):raise RuntimeError('empty local E column')
    n=len(cols);Gram=np.empty((n,n),complex)
    for i in range(n):
        for j in range(i,n):
            z=inner(cols[i],cols[j]);Gram[i,j]=z;Gram[j,i]=np.conjugate(z)
    herm=float(np.linalg.norm(Gram-Gram.conj().T)/max(np.linalg.norm(Gram),1e-30))
    evals=np.linalg.eigvalsh((Gram+Gram.conj().T)/2)
    evals=np.maximum(evals,0.0);svals=np.sqrt(evals[::-1]);smax=max(float(svals[0]),1e-300)
    rank=int(np.sum(svals/smax>SVD_REL))
    norms=[norm(c) for c in cols]
    constant={}
    for c in cols:add(constant,c)

    # Q4 covariance diagnostic: normalized Gram must depend only on dual-graph distance.
    bydist=defaultdict(list)
    for i in range(n):
        for j in range(i,n):
            d=q4_distance(D,i,j)
            bydist[d].append(Gram[i,j]/max(norms[i]*norms[j],1e-300))
    distance_rows={}
    max_spread=0.0
    for d,vals in sorted(bydist.items()):
        arr=np.asarray(vals,complex);mu=arr.mean();spread=float(np.max(np.abs(arr-mu)))
        max_spread=max(max_spread,spread)
        distance_rows[str(d)]={'count':len(vals),'mean_re':float(mu.real),'mean_im':float(mu.imag),'max_abs_spread':spread}

    # All E columns have odd doubled-spin parity whereas the seed is even, so seed overlap is exactly absent.
    seed_parity=(-1)**sum(seed[0])
    wrong=[]
    for v,c in enumerate(cols):
        for k in c:
            if (-1)**sum(k[0])==seed_parity:wrong.append((v,k))
    checks={
      'sixteen_nonzero_columns':len(cols)==16 and all(x>TOL for x in norms),
      'gram_hermitian':herm<1e-12,
      'positive_gram':float(np.min(np.linalg.eigvalsh((Gram+Gram.conj().T)/2)))>-1e-9,
      'uniform_local_norms':max(norms)-min(norms)<1e-10,
      'q4_distance_covariance':max_spread<1e-10,
      'seed_E_parity_orthogonal':not wrong,
      'nonzero_krylov_rank':rank>0,
    }
    return {
      'status':'exact L0 amplitude-level Euclidean Krylov precursor',
      'passed':bool(all(checks.values())),'science_status':'AMPLITUDE_PRECURSOR_E_ONLY',
      'checks':checks,'nodes':n,'edges':len(G.EDGES),'Jmax':JMAX2/2,
      'seed':'all j=1/2, all K=0','svd_relative_threshold':SVD_REL,
      'local_support_sizes':[len(c) for c in cols],
      'local_norms':norms,'constant_lapse_support':len(constant),'constant_lapse_norm':norm(constant),
      'gram_hermitian_relative_defect':herm,
      'gram_eigenvalues_ascending':[float(x) for x in evals],
      'amplitude_singular_values_descending':[float(x) for x in svals],
      'amplitude_krylov_rank':rank,
      'q4_normalized_gram_by_distance':distance_rows,
      'q4_max_covariance_spread':max_spread,
      'seed_parity':seed_parity,
      'wrong_seed_parity_outputs':len(wrong),
      'interpretation':'The first effective collective carrier is now measured from actual complex PL Peter-Weyl E amplitudes. Its rank is the target-independent dimension of span{E_v|Omega_0>} before Lorentzian/route completion.',
      'scope_note':'E-only depth-1 L0 amplitude precursor. Do not populate c_DeWitt, constraint ranks, TT count or collective HDA from this file. Production W0 requires Hermitian S, operator-first R, and depth-2 histories inside the independently frozen representation wall.'
    }

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);a=ap.parse_args();o=run();txt=json.dumps(o,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
