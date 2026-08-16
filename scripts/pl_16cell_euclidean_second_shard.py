#!/usr/bin/env python3
"""One deterministic shard of H1(H0|seed>) or H0(H1|seed>) on the 16-cell."""
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
from pl_dual_complex import DualComplex,seed_16cell_boundary
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean

TOL=1e-10

def decode(rows):
    return {(tuple(r['spins']),tuple(r['Ks'])):complex(r['re'],r['im']) for r in rows}

def encode(state):
    return [
      {'spins':list(k[0]),'Ks':list(k[1]),'re':float(a.real),'im':float(a.imag)}
      for k,a in sorted(state.items(),key=lambda kv:(kv[0][0],kv[0][1])) if abs(a)>TOL
    ]

def add(dst,src,scale):
    for k,a in src.items():
        z=dst.get(k,0j)+scale*a
        if abs(z)>TOL: dst[k]=z
        elif k in dst: del dst[k]

def run(inp,direction,shard,nshards):
    payload=json.loads(inp.read_text(encoding='utf-8'))
    if direction=='h1h0':
        first=decode(payload['H0']); target=1
    elif direction=='h0h1':
        first=decode(payload['H1']); target=0
    else: raise ValueError(direction)
    items=sorted(first.items(),key=lambda kv:(kv[0][0],kv[0][1]))
    selected=[x for i,x in enumerate(items) if i % nshards == shard]
    D=DualComplex(seed_16cell_boundary()); G=PLPeterWeylEuclidean(D)
    out={}
    for key,a0 in selected:
        add(out,G.H_sine_basis(key,target,5,TOL),a0)
    return {
      'status':'16-cell Euclidean second-action shard','direction':direction,
      'shard':shard,'nshards':nshards,'processed_columns':len(selected),
      'input_support':len(items),'partial_support':len(out),'partial_norm':G.norm(out),
      'state':encode(out),'passed':len(selected)>0
    }

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input',type=Path,required=True);ap.add_argument('--direction',choices=('h1h0','h0h1'),required=True)
    ap.add_argument('--shard',type=int,required=True);ap.add_argument('--nshards',type=int,default=8);ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();o=run(a.input,a.direction,a.shard,a.nshards);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in o.items() if k!='state'},indent=2));return 0 if o['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
