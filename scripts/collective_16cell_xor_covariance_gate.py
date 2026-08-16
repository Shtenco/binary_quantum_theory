#!/usr/bin/env python3
"""Exact XOR-translation covariance of 16-cell PL Peter-Weyl node columns.

The boundary 16-cell tetrahedra are bit-labelled 0..15.  XOR by a mask flips a
subset of the four primal +/- coordinate choices while preserving the local
axis/slot label r.  It permutes dual nodes and dual edges and carries the
orientation character chi(mask)=(-1)^popcount(mask).

Given the already-computed sixteen E_v|Omega> JSON columns, this gate verifies
both the structural PL identities and the actual sparse amplitude equation

  E_m|Omega> = chi(m) U_m E_0|Omega>

without fitting a phase.  The same structural character is the prerequisite for
transporting later pseudoscalar Lorentzian S node columns, which still require a
held-out direct S-node validation before production use.
"""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import numpy as np
from pl_dual_complex import DualComplex,seed_16cell_boundary
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean

TOL=1e-8

def decode(d):return {(tuple(r['spins']),tuple(r['Ks'])):complex(r['re'],r['im']) for r in d['column']}
def load(root):
    out={}
    for p in Path(root).rglob('node_*.json'):
        d=json.loads(p.read_text(encoding='utf-8'))
        if d.get('passed') and 'column' in d:out[int(d['node'])]=decode(d)
    if sorted(out)!=list(range(16)):raise RuntimeError(('need exact nodes 0..15',sorted(out)))
    return out

def relerr(a,b):
    keys=set(a)|set(b);num=math.sqrt(sum(abs(a.get(k,0j)-b.get(k,0j))**2 for k in keys));den=math.sqrt(sum(abs(z)**2 for z in b.values()))
    return num/max(den,1e-30)

def run(root):
    cols=load(root);D=DualComplex(seed_16cell_boundary());G=PLPeterWeylEuclidean(D);edges=list(G.EDGES);ei={e:i for i,e in enumerate(edges)}
    structural=[];rows=[];maxerr=0.0;support_ok=True
    def map_key(key,mask):
        spins,Ks=key;ns=[0]*len(edges)
        for old,(a,b) in enumerate(edges):ns[ei[tuple(sorted((a^mask,b^mask)))]]=spins[old]
        nk=[0]*16
        for v,K in enumerate(Ks):nk[v^mask]=K
        return tuple(ns),tuple(nk)
    for mask in range(16):
        chi=-1 if mask.bit_count()%2 else 1
        neigh_ok=all(D.neighbor[(v^mask,r)]==(D.neighbor[(v,r)]^mask) for v in range(16) for r in range(4))
        sign_ok=all(D.local_sign(v^mask,r)==chi*D.local_sign(v,r) for v in range(16) for r in range(4))
        tet_ok=all(tuple(2*i+(((v>> (3-i))&1)^((mask>>(3-i))&1)) for i in range(4))==D.tets[v^mask] for v in range(16))
        structural.append({'mask':mask,'popcount':mask.bit_count(),'character':chi,'neighbor_slot_equivariance':neigh_ok,'local_orientation_character':sign_ok,'tetra_bit_action':tet_ok})
        mapped={map_key(k,mask):chi*z for k,z in cols[0].items()}
        same=set(mapped)==set(cols[mask]);support_ok&=same;err=relerr(mapped,cols[mask]);maxerr=max(maxerr,err)
        rows.append({'mask':mask,'popcount':mask.bit_count(),'expected_character':chi,'support_identical':same,'relative_amplitude_error':err})
    checks={'all_structural_XOR_identities':all(all(x[k] for k in ('neighbor_slot_equivariance','local_orientation_character','tetra_bit_action')) for x in structural),
            'all_sparse_supports_identical_under_XOR':support_ok,
            'all_E_amplitudes_follow_frozen_orientation_character':maxerr<TOL}
    return {'status':'exact 16-cell XOR translation covariance of collective E node columns','passed':bool(all(checks.values())),'science_status':'AUTOMORPHISM_PREREQUISITE',
            'group':'(Z2)^4 primal sign flips / dual-node XOR translations','character':'chi(mask)=(-1)^popcount(mask)','tolerance':TOL,
            'max_relative_amplitude_error':maxerr,'checks':checks,'structural_rows':structural,'amplitude_rows':rows,
            'interpretation':'The translation subgroup alone is node-transitive and carries the Euclidean pseudoscalar orientation character. No coordinate-permutation/S4 covariance assumption is needed to map node 0 to any of the 16 dual nodes.',
            'S_transport_preregistered_consequence':'V is orientation-even, K=[V,E] carries chi, two K factors give chi^2=1, and the PL epsilon/localSign contributes chi; therefore the raw Lorentzian and Hermitian S are predicted to carry the same chi. Production use of this S transport still requires one direct held-out nonzero-mask S column comparison.',
            'scope_note':'Exact E-amplitude and structural automorphism gate. It does not substitute the held-out direct S-node calculation.'}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();o=run(a.root);t=json.dumps(o,indent=2);print(t);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8');return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
