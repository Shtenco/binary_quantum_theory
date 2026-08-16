#!/usr/bin/env python3
"""One exact shard of the first-block strict-interior Euclidean depth-two return.

A shard applies the unique strict-internal physical-sine Euclidean term at one
of the 24 fine chambers to one canonical background-orthogonal coarse-edge
tangent.  Three input edge classes are needed by S4: same=(01),
adjacent=(02), opposite=(23), all relative to reference edge (01).

The worker does not contract different node shards and does not compare to GR.
It only emits an exact sparse reduced internal state.  The collector sums the
24 node shards linearly before boundary overlaps are evaluated.

Strict-sector exact cutoff: the first q4 carrier has max doubled spin 2.  One
strict T word can hit its source c-link twice and every plaquette link at most
once, so a second strict action cannot exceed doubled spin 4 (j=2).  JMAX2=4 is
therefore an exact wall for this strict-only E^2 precursor; it does not replace
the larger wall used by the full production E/S depth-two calculation.
"""
from __future__ import annotations
import argparse,json,math,time,traceback,sys
from collections import defaultdict
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
import collective_l1_coarse_flux_response_gate as CF

JMAX2=4
TOL=1e-10
CLASS_EDGE={'same':(0,1),'adjacent':(0,2),'opposite':(2,3)}

def add(dst,src,scale=1.0):
    for k,a in src.items():
        z=dst.get(k,0j)+scale*a
        if abs(z)>TOL:dst[k]=z
        elif k in dst:del dst[k]

def strict_spec(D,G,inside,nodes,li):
    u=nodes[li];rows=[]
    for sign,spec in G.oriented_specs(u):
        v,a,b,c=spec;path=D.plaquette_path(v,a,b)
        if len(path)-1==4 and set(path[:-1])<=inside and D.neighbor[(v,c)] in inside:
            rows.append((sign,spec))
    if len(rows)!=1:raise RuntimeError(('strict spec count',li,len(rows)))
    return rows[0]

def full_key(reduced,G,nodes,internal,IE):
    isp,Kloc=reduced;spins=[1]*len(G.EDGES)
    for e,i in IE.items():spins[G.EIDX[e]]=isp[i]
    Ks=[0]*G.dual.n_tets
    for u,k in zip(nodes,Kloc):Ks[u]=k
    return tuple(spins),tuple(Ks)

def reduce_key(key,G,nodes,internal):
    spins,Ks=key;ints=set(internal);ins=set(nodes)
    for e in G.EDGES:
        if e not in ints and spins[G.EIDX[e]]!=1:
            raise RuntimeError(('strict shard changed noninternal link',e,spins[G.EIDX[e]]))
    for v,k in enumerate(Ks):
        if v not in ins and k!=0:raise RuntimeError(('strict shard changed outside K',v,k))
    return (tuple(spins[G.EIDX[e]] for e in internal),tuple(Ks[v] for v in nodes))

def tangent(edge,norm_evidence,D,G,inside,nodes,perms,internal,IE,seed,edge_li):
    li=edge_li[edge]
    col=CF.strict_col(D,G,inside,nodes,internal,IE,seed,li)
    phase=CF.parity(perms[li])
    col={k:phase*a for k,a in col.items()}
    base=(tuple([1]*len(internal)),tuple([0]*len(nodes)))
    n0=float(norm_evidence['background_boundary_norm_square'])
    hh=norm_evidence['parity_rephased_background_overlap']
    h=complex(float(hh['real']),float(hh['imag']))
    dperp=float(norm_evidence['background_orthogonal_per_source_norm_square'])
    col[base]=col.get(base,0j)-h/n0
    col={k:a/math.sqrt(dperp) for k,a in col.items() if abs(a)>TOL}
    return col,li,phase

def apply_shard(state,node_index,D,G,inside,nodes,internal,IE):
    sign,spec=strict_spec(D,G,inside,nodes,node_index)
    out=defaultdict(complex);raw_branches=0
    for reduced,a0 in state.items():
        key=full_key(reduced,G,nodes,internal,IE)
        rr=dict(G.T_items(key,*spec,JMAX2,False))
        aa=dict(G.T_items(key,*spec,JMAX2,True))
        branch={};add(branch,rr,-.5j*sign);add(branch,aa,+.5j*sign)
        raw_branches+=len(branch)
        for k,a in branch.items():out[reduce_key(k,G,nodes,internal)]+=a0*a
    return {k:a for k,a in out.items() if abs(a)>TOL},raw_branches

def save_npz(path,state,ninternal,nnodes):
    rows=sorted(state.items(),key=lambda kv:repr(kv[0]));path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    if rows:
        isp=np.asarray([k[0] for k,_ in rows],np.int16);Ks=np.asarray([k[1] for k,_ in rows],np.int16);amp=np.asarray([a for _,a in rows],np.complex128)
    else:
        isp=np.zeros((0,ninternal),np.int16);Ks=np.zeros((0,nnodes),np.int16);amp=np.zeros((0,),np.complex128)
    np.savez_compressed(path,internal_spins=isp,Ks=Ks,amp=amp)

def run(edge_class,node_index,norm_evidence,out_dir):
    t0=time.time();norm=json.loads(Path(norm_evidence).read_text())
    if not norm.get('passed'):raise RuntimeError('tangent normalization evidence must PASS')
    D,G,inside,nodes,perms,internal,IE,seed,edge_li=CF.setup()
    edge=CLASS_EDGE[edge_class]
    state,source_li,phase=tangent(edge,norm,D,G,inside,nodes,perms,internal,IE,seed,edge_li)
    out,branches=apply_shard(state,node_index,D,G,inside,nodes,internal,IE)
    maxspin=max((max(k[0]) for k in out),default=0)
    finite=all(np.isfinite([z.real,z.imag]).all() for z in out.values())
    checks={
      'L1_closed_384':D.n_tets==384,
      'parent_block_24':len(nodes)==24,
      'input_tangent_support21':len(state)==21,
      'output_finite':finite,
      'strict_exact_spin_wall_doubled_le4':maxspin<=JMAX2,
      'node_index_valid':0<=node_index<24,
    }
    out_dir=Path(out_dir);out_dir.mkdir(parents=True,exist_ok=True)
    save_npz(out_dir/f'{edge_class}_node_{node_index}.npz',out,len(internal),len(nodes))
    meta={
      'status':'one exact strict-interior E depth2 shard','passed':bool(all(checks.values())),
      'science_status':'STRICT_E_DEPTH2_SHARD','edge_class':edge_class,'source_edge':list(edge),
      'source_representative_local_index':source_li,'source_parity_rephasing':phase,
      'second_action_local_index':node_index,'Jmax':JMAX2/2,
      'input_support':len(state),'output_support':len(out),'raw_branch_support_sum':branches,
      'max_reached_doubled_spin':maxspin,'checks':checks,'runtime_seconds':time.time()-t0,
      'scope_note':'One linear shard only. No GR target, Lorentzian S, route, boundary-shard summation or physical Feshbach denominator is used.'
    }
    (out_dir/f'{edge_class}_node_{node_index}.json').write_text(json.dumps(meta,indent=2)+'\n')
    return meta

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--edge-class',choices=tuple(CLASS_EDGE),required=True)
    p.add_argument('--node-index',type=int,choices=range(24),required=True)
    p.add_argument('--normalization',type=Path,default=Path('verification_results/COLLECTIVE_L1_TANGENT_NORMALIZATION.json'))
    p.add_argument('--out-dir',type=Path,required=True)
    a=p.parse_args()
    try:o=run(a.edge_class,a.node_index,a.normalization,a.out_dir);code=0 if o['passed'] else 1
    except Exception as exc:o={'status':'strict E depth2 worker exception','passed':False,'error_type':type(exc).__name__,'error':str(exc),'traceback':traceback.format_exc()};code=1
    print(json.dumps(o,indent=2));return code
if __name__=='__main__':raise SystemExit(main())
