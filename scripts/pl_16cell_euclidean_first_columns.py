#!/usr/bin/env python3
"""Produce the two adjacent-node physical-sine H_E columns on the 16-cell habitat."""
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
from pl_dual_complex import DualComplex,seed_16cell_boundary
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean

TOL=1e-10

def encode(state):
    return [
      {'spins':list(k[0]),'Ks':list(k[1]),'re':float(a.real),'im':float(a.imag)}
      for k,a in sorted(state.items(),key=lambda kv:(kv[0][0],kv[0][1]))
    ]

def run():
    D=DualComplex(seed_16cell_boundary()); G=PLPeterWeylEuclidean(D)
    seed=((1,)*len(G.EDGES),(0,)*D.n_tets)
    # Jmax=5/2 is the preregistered sufficient wall for the two-E channel; the
    # first column itself reaches only j<=1 on this seed.
    JMAX2=5
    h0=G.H_sine_basis(seed,0,JMAX2,TOL)
    h1=G.H_sine_basis(seed,1,JMAX2,TOL)
    return {
      'status':'16-cell adjacent Euclidean first columns',
      'Jmax':JMAX2/2,'nodes':[0,1],
      'seed':{'spins':list(seed[0]),'Ks':list(seed[1])},
      'H0_support':len(h0),'H0_norm':G.norm(h0),
      'H1_support':len(h1),'H1_norm':G.norm(h1),
      'H0':encode(h0),'H1':encode(h1),
      'passed':bool(h0 and h1 and G.norm(h0)>1e-10 and G.norm(h1)>1e-10)
    }

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();o=run();a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in o.items() if k not in ('H0','H1')},indent=2))
    return 0 if o['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
