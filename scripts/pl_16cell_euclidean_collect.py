#!/usr/bin/env python3
"""Exact reducer for distributed 16-cell [H0^sine,H1^sine] shards."""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
TOL=1e-10

def decode(rows):
    return {(tuple(r['spins']),tuple(r['Ks'])):complex(r['re'],r['im']) for r in rows}

def add(dst,src,scale=1.0):
    for k,a in src.items():
        z=dst.get(k,0j)+scale*a
        if abs(z)>TOL: dst[k]=z
        elif k in dst: del dst[k]

def norm(st): return math.sqrt(sum(abs(a)**2 for a in st.values()))
def parity(key): return (-1)**sum(key[0])

def run(root,nshards):
    files=sorted(root.rglob('partial_*.json'))
    groups={'h1h0':{},'h0h1':{}}
    meta=[]
    for f in files:
        p=json.loads(f.read_text(encoding='utf-8'));d=p['direction'];s=int(p['shard'])
        if s in groups[d]: raise RuntimeError(f'duplicate {d} shard {s}')
        groups[d][s]=decode(p['state']);meta.append({k:v for k,v in p.items() if k!='state'})
    expected=set(range(nshards))
    if set(groups['h1h0'])!=expected or set(groups['h0h1'])!=expected:
        raise RuntimeError({'h1h0':sorted(groups['h1h0']),'h0h1':sorted(groups['h0h1'])})
    h1h0={};h0h1={}
    for s in range(nshards): add(h1h0,groups['h1h0'][s]);add(h0h1,groups['h0h1'][s])
    comm={};add(comm,h0h1,+1);add(comm,h1h0,-1)
    seed_parity=(-1)**32
    wrong=[k for k in comm if parity(k)!=seed_parity]
    fixed=[a for k,a in comm.items() if all(s==1 for s in k[0])]
    max_spin=max((max(k[0]) for k in comm),default=0)/2
    out={
      'status':'distributed exact 16-cell Euclidean commutator',
      'passed':bool(comm and not wrong),
      'nodes':[0,1],'Jmax':2.5,'nshards_per_direction':nshards,
      'H1H0_support':len(h1h0),'H1H0_norm':norm(h1h0),
      'H0H1_support':len(h0h1),'H0H1_norm':norm(h0h1),
      'commutator_support':len(comm),'commutator_norm':norm(comm),
      'max_spin_reached':max_spin,
      'fixed_all_jhalf_support':len(fixed),
      'fixed_all_jhalf_norm':math.sqrt(sum(abs(a)**2 for a in fixed)),
      'doubled_spin_parity_wrong_support':len(wrong),
      'shards':meta,
      'scope_note':'Independent 16-cell Euclidean geometry commutator. Route/Lorentzian/diffeomorphism comparison is a separate next-stage gate.'
    }
    return out

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--root',type=Path,required=True);ap.add_argument('--nshards',type=int,default=8);ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();o=run(a.root,a.nshards);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8');print(json.dumps(o,indent=2));return 0 if o['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
