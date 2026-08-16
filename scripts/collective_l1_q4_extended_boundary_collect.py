#!/usr/bin/env python3
"""Coarse-grain the 24 exact L1 q=4 artifacts with explicit environment sectors.

Input files are the sparse outputs of ``collective_l1_block_e_q4_worker.py``.
Each row stores global spin/K changes relative to the homogeneous background.
This collector reconstructs the canonical coarse block and splits every basis
state into

  * 36 internal-link spins and 24 inside intertwiners,
  * 24 cut boundary-link spins,
  * an orthogonal exterior signature (external-only spin changes and outside K).

States with different exterior signatures or different boundary representation
patterns are never summed together.  They form orthogonal extended-Hilbert
edge-mode sectors.  Within each sector, all 36 internal links are contracted
exactly and boundary-tensor overlaps are evaluated as a double-layer network.

The collector reports both:

1. the strict vacuum-exterior / unchanged-boundary sector, whose 24 source
   vectors reduce structurally to six coarse-edge channels; and
2. the complete q=4 extended boundary map, which retains the crossing sectors
   and is tested for full source rank.

No GR target, metric dimension, DeWitt coefficient or constraint rank is used
in the decomposition.  Local-vs-crossing is defined solely by graph support.
"""
from __future__ import annotations

import argparse
import functools
import itertools
import json
import math
import sys
import traceback
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import opt_einsum as oe

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import k5_peter_weyl_safe_hda_column as PW
from collective_barycentric_E_boundary_support_gate import barycentric_with_parent
from pl_dual_complex import DualComplex, seed_16cell_boundary
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean

REL=1e-10
TOL=1e-10


def parity(p):
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inv%2 else 1


def load_rows(root):
    rows=[]
    for p in Path(root).rglob('q4_*.json'):
        d=json.loads(p.read_text())
        if not d.get('passed'):
            raise RuntimeError(('failed q4 worker',str(p)))
        if d.get('science_status')!='L1_BLOCK_E_Q4_EXACT_PROJECTION':
            continue
        rows.append((int(d['local_fine_index']),d,str(p)))
    rows=sorted(rows)
    if [i for i,_,_ in rows]!=list(range(24)):
        raise RuntimeError(('need q4 local indices 0..23',[i for i,_,_ in rows]))
    return rows


def reconstruct_groups(worker_rows):
    fine,parent=barycentric_with_parent(seed_16cell_boundary())
    D=DualComplex(fine);G=PLPeterWeylEuclidean(D)
    inside=set(v for v,p in enumerate(parent) if p==0);nodes=sorted(inside)
    internal=sorted(e for e in G.EDGES if e[0] in inside and e[1] in inside)
    boundary=sorted(e for e in G.EDGES if (e[0] in inside)^(e[1] in inside))
    external=sorted(e for e in G.EDGES if e[0] not in inside and e[1] not in inside)
    IE={e:i for i,e in enumerate(internal)};BE={e:i for i,e in enumerate(boundary)}
    external_set=set(external)

    # group -> source -> block restriction -> amplitude
    groups=defaultdict(lambda:defaultdict(lambda:defaultdict(complex)))
    occurrence_patterns=Counter()
    for local_index,d,_ in worker_rows:
        for r in d['states']:
            isp=[1]*len(internal);bsp=[1]*len(boundary);Ks=[0]*len(nodes)
            env_spin=[];env_K=[]
            for ei,s in r['spin_changes']:
                e=G.EDGES[int(ei)];s=int(s)
                if e in IE:
                    isp[IE[e]]=s
                elif e in BE:
                    bsp[BE[e]]=s
                elif e in external_set:
                    env_spin.append((e,s))
                else:
                    raise RuntimeError(('edge partition failure',e))
            for v,K in r['K_changes']:
                v=int(v);K=int(K)
                if v in inside:
                    Ks[nodes.index(v)]=K
                else:
                    env_K.append((v,K))
            env=(tuple(sorted(env_spin)),tuple(sorted(env_K)))
            bpat=tuple(bsp)
            state=(tuple(isp),tuple(Ks))
            groups[(env,bpat)][local_index][state]+=complex(r['re'],r['im'])
            occurrence_patterns[(len(env_spin),len(env_K),sum(s!=1 for s in bpat))]+=1

    # Freeze the purely combinatorial local slot structure used by the static
    # and dynamic block contractions.
    slot_ok=True
    boundary_by_node={}
    for u in nodes:
        flags=[D.neighbor[(u,r)] in inside for r in range(4)]
        slot_ok &= flags==[True,True,True,False]
        e=tuple(sorted((u,D.neighbor[(u,3)])))
        if e not in BE:
            slot_ok=False
        boundary_by_node[u]=e

    return D,G,inside,nodes,internal,boundary,IE,BE,boundary_by_node,groups,occurrence_patterns,slot_ok


def sector_source_gram(D,nodes,inside,internal,IE,BE,boundary_by_node,key,srcdict):
    env,bsp=key
    states=sorted(set().union(*(set(c) for c in srcdict.values())),key=repr)
    sidx={s:i for i,s in enumerate(states)}
    srcs=sorted(srcdict)
    C=np.zeros((len(states),len(srcs)),complex)
    for jj,src in enumerate(srcs):
        for st,a in srcdict[src].items():
            C[sidx[st],jj]=a

    @functools.lru_cache(maxsize=None)
    def local_tensor(si,local_u):
        internal_spins,inside_K=states[si]
        u=nodes[local_u]
        ls=[]
        for r in range(3):
            w=D.neighbor[(u,r)]
            e=tuple(sorted((u,w)))
            ls.append(internal_spins[IE[e]])
        ls.append(bsp[BE[boundary_by_node[u]]])
        K=inside_K[local_u]
        if K not in PW.allowed_k2_t(*tuple(ls)):
            raise RuntimeError(('invalid local block intertwiner',local_u,tuple(ls),K))
        T=PW.intertwiner_tensor_cached(tuple(ls),K).copy()
        for r in range(3):
            w=D.neighbor[(u,r)]
            if u>w:
                T=PW.apply_axis_np(T,r,PW.epsilon_j(ls[r]))
        return T

    def overlap(i,j):
        args=[]
        for local_u,u in enumerate(nodes):
            A=local_tensor(i,local_u);B=local_tensor(j,local_u)
            # Boundary representation pattern is identical inside one sector.
            X=np.tensordot(A,B.conj(),axes=([3],[3]))
            X=np.transpose(X,(0,3,1,4,2,5))
            X=X.reshape([A.shape[r]*B.shape[r] for r in range(3)])
            inds=[]
            for r in range(3):
                w=D.neighbor[(u,r)]
                inds.append(IE[tuple(sorted((u,w)))])
            args.extend([X,inds])
        args.append([])
        return oe.contract(*args,optimize='greedy')

    K=np.empty((len(states),len(states)),complex)
    for i in range(len(states)):
        for j in range(i,len(states)):
            z=overlap(i,j);K[i,j]=z;K[j,i]=np.conjugate(z)
    Gs=C.conj().T@K@C
    Gs=.5*(Gs+Gs.conj().T)
    return srcs,Gs,len(states),int(np.count_nonzero(C))


def strict_structure(G):
    perms=tuple(itertools.permutations(range(4)))
    phase=np.array([parity(p) for p in perms],float)
    H=G*phase[:,None]*phase[None,:]
    edge_group=[tuple(sorted(p[:2])) for p in perms]
    d=float(np.mean(np.diag(H).real))
    same=[];diff=[]
    for i in range(24):
        for j in range(24):
            z=H[i,j]/d
            (same if edge_group[i]==edge_group[j] else diff).append(z)
    r=float(np.mean([z.real for z in diff]))
    pred=np.array([[d*(1 if edge_group[i]==edge_group[j] else r) for j in range(24)] for i in range(24)],complex)
    rel=float(np.linalg.norm(H-pred)/max(np.linalg.norm(H),1e-300))
    structural_rank=6 if abs(1-r)>1e-8 and abs(1+5*r)>1e-8 else None
    return {
        'coarse_edge_groups':[list(x) for x in edge_group],
        'coarse_edge_group_census':{str(k):v for k,v in sorted(Counter(edge_group).items())},
        'd_boundary_norm_square':d,
        'r_inter_edge_overlap':r,
        'block_model_relative_defect':rel,
        'same_group_normalized_max_defect':float(max(abs(z-1) for z in same)),
        'different_group_normalized_max_defect':float(max(abs(z-r) for z in diff)),
        'structural_boundary_rank':structural_rank,
        'analytic_uniform_eigenvalue':4*d*(1+5*r),
        'analytic_shape_eigenvalue_fivefold':4*d*(1-r),
        'analytic_zero_multiplicity':18,
    }


def left_S4_covariance(G):
    perms=tuple(itertools.permutations(range(4)))
    phase=np.array([parity(p) for p in perms],float)
    H=G*phase[:,None]*phase[None,:]
    def inv(p):
        q=[0]*4
        for i,x in enumerate(p):q[x]=i
        return tuple(q)
    def compose(p,q):return tuple(p[q[i]] for i in range(4))
    by=defaultdict(list)
    for i,p in enumerate(perms):
        ip=inv(p)
        for j,q in enumerate(perms):
            by[compose(ip,q)].append(H[i,j])
    spread=max(max(abs(z-sum(v)/len(v)) for z in v) for v in by.values())
    scale=max(float(np.max(np.abs(H))),1e-300)
    kernel={str(k):[float((sum(v)/len(v)).real/scale),float((sum(v)/len(v)).imag/scale)] for k,v in sorted(by.items())}
    return float(spread/scale),kernel


def calculate(root):
    workers=load_rows(root)
    D,G,inside,nodes,internal,boundary,IE,BE,boundary_by_node,groups,occ_patterns,slot_ok=reconstruct_groups(workers)

    total=np.zeros((24,24),complex)
    sector_stats=Counter();vacuum_G=None
    vacuum_key=((),tuple([1]*len(boundary)))
    for key,srcdict in groups.items():
        srcs,Gs,nstates,nocc=sector_source_gram(D,nodes,inside,internal,IE,BE,boundary_by_node,key,srcdict)
        for i,si in enumerate(srcs):
            for j,sj in enumerate(srcs):
                total[si,sj]+=Gs[i,j]
        sector_stats[(len(srcs),nocc,nstates)]+=1
        if key==vacuum_key:
            if srcs!=list(range(24)):
                raise RuntimeError('vacuum sector missing source columns')
            vacuum_G=Gs
    if vacuum_G is None:
        raise RuntimeError('no strict vacuum sector')

    total=.5*(total+total.conj().T)
    evals=np.linalg.eigvalsh(total)
    svals=np.sqrt(np.maximum(evals,0))[::-1]
    smax=max(float(svals[0]),1e-300)
    rank=int(np.sum(svals/smax>REL))
    covdef,kernel=left_S4_covariance(total)
    strict=strict_structure(vacuum_G)

    checks={
        'all_24_q4_workers_loaded':len(workers)==24,
        'L1_closed_nodes_384':D.n_tets==384,
        'canonical_block_36_internal_links':len(internal)==36,
        'canonical_block_24_boundary_links':len(boundary)==24,
        'canonical_slots_012_internal_3_boundary':slot_ok,
        'environment_boundary_sector_count_193':len(groups)==193,
        'occurrence_pattern_census':occ_patterns==Counter({(0,0,0):480,(1,2,2):960}),
        'vacuum_intrinsic_rank_6':strict['structural_boundary_rank']==6,
        'vacuum_block_structure':strict['block_model_relative_defect']<1e-10,
        'extended_q4_source_rank_24':rank==24,
        'extended_q4_positive_definite':float(evals.min())>0,
        'extended_q4_left_S4_covariance':covdef<1e-10,
    }
    return {
        'status':'exact L1 q4 extended-Hilbert coarse-boundary decomposition',
        'passed':bool(all(checks.values())),
        'science_status':'L1_Q4_EXTENDED_BOUNDARY_PRECURSOR',
        'checks':checks,
        'sector_count':len(groups),
        'sector_shape_histogram':{str(k):v for k,v in sorted(sector_stats.items())},
        'occurrence_pattern_census':{str(k):v for k,v in sorted(occ_patterns.items())},
        'vacuum_sector':strict,
        'extended_source_rank':rank,
        'extended_Gram_eigenvalues_ascending':[float(x) for x in evals],
        'extended_singular_values_descending':[float(x) for x in svals],
        'extended_min_eigenvalue':float(evals.min()),
        'extended_max_eigenvalue':float(evals.max()),
        'extended_min_to_max_singular_ratio':float(svals[-1]/svals[0]),
        'left_S4_covariance_relative_defect':covdef,
        'left_S4_rephased_convolution_kernel_normalized':kernel,
        'interpretation':'The q4 Euclidean image separates target-independently into a six-dimensional strict-interior coarse-edge carrier and orthogonal crossing/environment sectors. Retaining the latter restores full rank 24, so coarse-graining does not delete the fine directions; it classifies them into intrinsic block geometry versus inter-block coupling channels.',
        'scope_note':'q4 Euclidean depth-one only. Full production W_block must add q6/q8 where dynamically relevant, Hermitian Lorentzian S, route and depth-two histories before metric Hessian, constraint-rank and collective-HDA measurements.'
    }


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    try:
        o=calculate(a.root);code=0 if o['passed'] else 1
    except Exception as exc:
        o={'status':'collector exception','passed':False,'science_status':'INFRASTRUCTURE_DIAGNOSTIC','error_type':type(exc).__name__,'error':str(exc),'traceback':traceback.format_exc()};code=1
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8');print(json.dumps(o,indent=2));return code

if __name__=='__main__':raise SystemExit(main())
