#!/usr/bin/env python3
"""Exact graph-cochain part of the dual-K5 HDA structure function.

For node lapses N,M on K5 define on every oriented edge (v,w)

    omega = N_bar dM - M_bar dN

with midpoint averages.  Algebraically this must reduce to

    omega_vw = N_v M_w - N_w M_v.

For basis lapses delta_i,delta_j the support is exactly the one shared dual edge
(i,j).  The metric/flux sharp map is deliberately not inserted here.
"""
from __future__ import annotations
import argparse,itertools,json
from pathlib import Path
import numpy as np

VERT=tuple(range(5));EDGES=tuple(itertools.combinations(VERT,2))

def omega(N,M):
    out=[]
    for v,w in EDGES:
        Nav=0.5*(N[v]+N[w]);Mav=0.5*(M[v]+M[w])
        dN=N[w]-N[v];dM=M[w]-M[v]
        out.append(Nav*dM-Mav*dN)
    return np.asarray(out,float)

def direct(N,M):
    return np.asarray([N[v]*M[w]-N[w]*M[v] for v,w in EDGES],float)

def run(seed=260809,samples=100):
    rng=np.random.default_rng(seed);max_identity=0.0;max_antisym=0.0
    for _ in range(samples):
        N=rng.normal(size=5);M=rng.normal(size=5)
        max_identity=max(max_identity,float(np.max(np.abs(omega(N,M)-direct(N,M)))))
        max_antisym=max(max_antisym,float(np.max(np.abs(omega(N,M)+omega(M,N)))))
    basis=[];single_support=True
    for i,j in EDGES:
        N=np.zeros(5);M=np.zeros(5);N[i]=1;M[j]=1
        o=omega(N,M);nz=np.flatnonzero(np.abs(o)>1e-14)
        expected=EDGES.index((i,j))
        ok=(len(nz)==1 and int(nz[0])==expected and abs(o[expected]-1)<1e-14)
        single_support &= ok
        basis.append({'pair':[i,j],'nonzero_edges':[list(EDGES[k]) for k in nz],'coefficient':float(o[expected])})
    passed=max_identity<1e-12 and max_antisym<1e-12 and single_support
    return {
      'status':'exact dual-K5 lapse cochain gate','passed':bool(passed),'samples':samples,'seed':seed,
      'max_midpoint_vs_direct_identity_error':max_identity,
      'max_antisymmetry_error':max_antisym,
      'basis_lapse_pairs':basis,
      'exact_formula':'omega_vw = N_v M_w - N_w M_v',
      'interpretation':'This fixes the graph/cochain support of the dual-node HDA shift before the geometry-dependent sharp map. For N=delta_i,M=delta_j only dual edge (i,j) is supported.'
    }

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);a=ap.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
