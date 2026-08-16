#!/usr/bin/env python3
"""Compute one exact L0 16-cell physical-sine Euclidean column E_v|Omega_0>."""
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
from pl_dual_complex import DualComplex,seed_16cell_boundary
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean

TOL=1e-10
JMAX2=5

def encode(state):
    return [
      {'spins':list(k[0]),'Ks':list(k[1]),'re':float(a.real),'im':float(a.imag)}
      for k,a in sorted(state.items(),key=lambda kv:(kv[0][0],kv[0][1]))
    ]

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--node',type=int,required=True)
    ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args()
    D=DualComplex(seed_16cell_boundary());G=PLPeterWeylEuclidean(D)
    if not (0<=a.node<D.n_tets):ap.error(f'--node must be 0..{D.n_tets-1}')
    seed=((1,)*len(G.EDGES),(0,)*D.n_tets)
    col=G.H_sine_basis(seed,a.node,JMAX2,TOL)
    out={'status':'distributed exact L0 Euclidean node column','node':a.node,
         'Jmax':JMAX2/2,'seed':{'spins':list(seed[0]),'Ks':list(seed[1])},
         'support':len(col),'norm':G.norm(col),'column':encode(col),
         'passed':bool(col and G.norm(col)>TOL)}
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='column'},indent=2))
    return 0 if out['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
