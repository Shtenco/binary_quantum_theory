#!/usr/bin/env python3
"""Exact GF(2) homology certificate for the 16-cell S3 spin-structure prerequisite."""
from __future__ import annotations
import argparse, itertools, json
from pathlib import Path
import numpy as np

def seed_16cell_boundary():
    return sorted(tuple(2*i+b for i,b in enumerate(bits)) for bits in itertools.product((0,1),repeat=4))

def rank_gf2(A):
    A=(A.copy()%2).astype(np.uint8); m,n=A.shape; r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i,c]),None)
        if piv is None: continue
        A[[r,piv]]=A[[piv,r]]
        for i in range(m):
            if i!=r and A[i,c]: A[i]^=A[r]
        r+=1
        if r==m: break
    return r

def run():
    tets=seed_16cell_boundary(); verts=sorted(set(v for t in tets for v in t)); edges=sorted(set(e for t in tets for e in itertools.combinations(t,2))); faces=sorted(set(f for t in tets for f in itertools.combinations(t,3)))
    vi={v:i for i,v in enumerate(verts)}; ei={e:i for i,e in enumerate(edges)}; fi={f:i for i,f in enumerate(faces)}
    B1=np.zeros((len(verts),len(edges)),dtype=np.uint8); B2=np.zeros((len(edges),len(faces)),dtype=np.uint8); B3=np.zeros((len(faces),len(tets)),dtype=np.uint8)
    for j,(a,b) in enumerate(edges): B1[vi[a],j]=1; B1[vi[b],j]=1
    for j,f in enumerate(faces):
        for e in itertools.combinations(f,2): B2[ei[tuple(sorted(e))],j]=1
    for j,t in enumerate(tets):
        for f in itertools.combinations(t,3): B3[fi[tuple(sorted(f))],j]=1
    r1,r2,r3=rank_gf2(B1),rank_gf2(B2),rank_gf2(B3)
    b0=len(verts)-r1; b1=len(edges)-r1-r2; b2=len(faces)-r2-r3; b3=len(tets)-r3
    c12=bool(np.all((B1@B2)%2==0)); c23=bool(np.all((B2@B3)%2==0))
    passed=bool((len(verts),len(edges),len(faces),len(tets))==(8,24,32,16) and (r1,r2,r3)==(7,17,15) and (b0,b1,b2,b3)==(1,0,0,1) and c12 and c23)
    return {'status':'exact GF(2) homology gate for the 16-cell S3 spin-structure prerequisite','passed':passed,'simplex_counts':{'V':len(verts),'E':len(edges),'F':len(faces),'T':len(tets)},'boundary_ranks_GF2':{'d1':r1,'d2':r2,'d3':r3},'betti_GF2':[b0,b1,b2,b3],'boundary_squared_zero':{'d1_d2':c12,'d2_d3':c23},'H1_Z2_dimension':b1,'spin_structure_count_for_S3':1,'scope':'H1(Z2)=0 supplies uniqueness once spin existence is known; spin existence follows independently from S3=SU2 being parallelizable'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=Path('verification_results/S3_MOD2_SPIN_STRUCTURE.json')); a=ap.parse_args(); out=run(); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2)); return 0 if out['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
