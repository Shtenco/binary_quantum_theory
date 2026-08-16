#!/usr/bin/env python3
"""Exact coarse-boundary rank theorem for the strict-interior L1 q=4 channel.

This is the first dynamical internal-link contraction for the canonical
24-chamber barycentric tetra block.

For each fine chamber u, select the unique q=4 Euclidean oriented spec whose
curvature plaquette AND double-hit source link lie entirely inside the same
coarse block.  Project to the exactly-four-spin-change sector.  This channel is
strictly vacuum-exterior by support: no exterior node or exterior/boundary edge
is touched, so the exterior remains exactly the homogeneous background.

Each resulting microscopic Gauss state is then coarse-grained by contracting
all 36 internal dual links, leaving the 24 boundary magnetic indices open.  We
do not materialize the 2^24 boundary tensor.  Instead its Gram kernel is
computed exactly as a double-layer tensor network; complete face recoupling is
unitary and therefore leaves this Gram invariant.

The 24 chamber-source boundary vectors are shown to have an exact six-channel
block form after the frozen permutation-parity rephasing.  Chambers are grouped
by the unordered pair formed by the first two entries of their S4 permutation,
i.e. by one of the six coarse tetrahedral edges.  The Gram is

  G = D_parity * d[(1-r) diag(J4,...,J4) + r J24] * D_parity

with six J4 blocks.  Therefore its structural rank is exactly six whenever
r != 1 and r != -1/5, independently of floating-point zero-eigenvalue noise.

This is a target-independent boundary tangent-rank theorem.  The six channels
are naturally coarse-edge-labelled, but this gate does NOT identify them with
GR metric components and does NOT measure the DeWitt coefficient.
"""
from __future__ import annotations

import argparse
import functools
import itertools
import json
import math
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import opt_einsum as oe

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_zeroaware_volume_migration_experiment as ZVM
from collective_barycentric_E_boundary_support_gate import barycentric_with_parent
from pl_dual_complex import DualComplex, seed_16cell_boundary
from pl_peter_weyl_euclidean_local import LocalPLPeterWeylEuclidean

JMAX2=3
TOL=1e-10
STRUCT_TOL=1e-10


def add(dst,src,scale,tol=TOL):
    for k,a in src.items():
        z=dst.get(k,0j)+scale*a
        if abs(z)>tol:
            dst[k]=z
        elif k in dst:
            del dst[k]


def permutation_parity(p):
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inv%2 else 1


def build_strict_columns():
    ZVM.patch_and_clear()
    fine,parent=barycentric_with_parent(seed_16cell_boundary())
    D=DualComplex(fine)
    G=LocalPLPeterWeylEuclidean(D)
    inside=set(v for v,p in enumerate(parent) if p==0)
    nodes=sorted(inside)
    internal_edges=sorted(e for e in G.EDGES if e[0] in inside and e[1] in inside)
    boundary_edges=sorted(e for e in G.EDGES if (e[0] in inside)^(e[1] in inside))
    internal_eidx={e:i for i,e in enumerate(internal_edges)}
    seed=((1,)*len(G.EDGES),(0,)*D.n_tets)

    # For this canonical barycentric block, slots 0,1,2 are internal adjacent
    # transpositions and slot 3 is the unique block-boundary leg.
    slot_checks=[]
    for u in nodes:
        flags=[D.neighbor[(u,r)] in inside for r in range(4)]
        slot_checks.append(flags==[True,True,True,False])

    cols=[]; worker_rows=[]
    for local_index,u in enumerate(nodes):
        strict=[]
        q4_total=0
        for sign,spec in G.oriented_specs(u):
            v,ra,rb,rc=spec
            path=D.plaquette_path(v,ra,rb)
            if len(path)-1!=4:
                continue
            q4_total+=1
            source_neighbor=D.neighbor[(v,rc)]
            if set(path[:-1])<=inside and source_neighbor in inside:
                strict.append((sign,spec,path))
        if len(strict)!=1:
            raise RuntimeError(('expected one strict-interior q4 spec',local_index,u,len(strict)))

        sign,spec,path=strict[0]
        raw={}
        add(raw,dict(G.T_items(seed,*spec,JMAX2,False)),-0.5j*sign)
        add(raw,dict(G.T_items(seed,*spec,JMAX2,True)),+0.5j*sign)
        p4={k:a for k,a in raw.items() if abs(a)>TOL and sum(s!=1 for s in k[0])==4}
        if not p4:
            raise RuntimeError(('empty strict q4 P4 column',local_index))

        compact=defaultdict(complex)
        exterior_clean=True
        boundary_clean=True
        for (spins,Ks),amp in p4.items():
            if any(spins[G.EIDX[e]]!=1 for e in boundary_edges):
                boundary_clean=False
            for v in range(D.n_tets):
                if v not in inside and Ks[v]!=0:
                    exterior_clean=False
            # Strict support means every changed spin must be an internal edge.
            changed_global={i for i,s in enumerate(spins) if s!=1}
            changed_internal={G.EIDX[e] for e in internal_edges if spins[G.EIDX[e]]!=1}
            if changed_global!=changed_internal:
                exterior_clean=False
            sig=(
                tuple(spins[G.EIDX[e]] for e in internal_edges),
                tuple(Ks[v] for v in nodes),
            )
            compact[sig]+=amp

        compact={k:a for k,a in compact.items() if abs(a)>TOL}
        cols.append(compact)
        worker_rows.append({
            'local_index':local_index,
            'global_node':u,
            'q4_specs_total':q4_total,
            'strict_specs':len(strict),
            'projected_microscopic_support':len(compact),
            'projected_microscopic_norm':math.sqrt(sum(abs(a)**2 for a in compact.values())),
            'boundary_spins_unchanged':boundary_clean,
            'exterior_exactly_background_by_labels':exterior_clean,
        })

        # Prevent refinement-level branch caches from accumulating obsolete
        # 768-edge input keys across the 24 independent source columns.
        G.primitive_items.cache_clear()
        G.T_items.cache_clear()
        G.oriented_intertwiner.cache_clear()

    return D,G,nodes,inside,internal_edges,internal_eidx,cols,worker_rows,slot_checks


def boundary_gram(D,G,nodes,inside,internal_edges,internal_eidx,cols):
    states=sorted(set().union(*(set(c) for c in cols)),key=repr)
    sidx={s:i for i,s in enumerate(states)}
    C=np.zeros((len(states),len(cols)),complex)
    for j,c in enumerate(cols):
        for s,a in c.items():
            C[sidx[s],j]=a

    # The barycentric ordering inside one parent block is exactly the S4
    # permutation ordering used by itertools.permutations.
    perms=tuple(itertools.permutations(range(4)))
    if len(nodes)!=len(perms):
        raise RuntimeError('canonical block is not 24 chambers')

    @functools.lru_cache(maxsize=None)
    def local_tensor(si,local_u):
        internal_spins,inside_K=states[si]
        global_u=nodes[local_u]
        ls=[]
        for r in range(3):
            w=D.neighbor[(global_u,r)]
            if w not in inside:
                raise RuntimeError(('internal slot escaped block',local_u,r))
            e=tuple(sorted((global_u,w)))
            ls.append(internal_spins[internal_eidx[e]])
        ls.append(1) # untouched strict-channel boundary edge
        K=inside_K[local_u]
        if K not in PW.allowed_k2_t(*tuple(ls)):
            raise RuntimeError(('invalid local K after restriction',local_u,tuple(ls),K))
        T=PW.intertwiner_tensor_cached(tuple(ls),K).copy()
        # Same orientation convention as the full PL engine: absorb epsilon on
        # the larger global endpoint of each internal dual edge.
        for r in range(3):
            w=D.neighbor[(global_u,r)]
            if global_u>w:
                T=PW.apply_axis_np(T,r,PW.epsilon_j(ls[r]))
        return T

    def overlap(i,j):
        args=[]
        for local_u,global_u in enumerate(nodes):
            A=local_tensor(i,local_u)
            B=local_tensor(j,local_u)
            # Sum the shared open boundary magnetic index between bra/ket,
            # then fuse the three ket/bra internal index pairs.
            X=np.tensordot(A,B.conj(),axes=([3],[3]))
            X=np.transpose(X,(0,3,1,4,2,5))
            X=X.reshape([A.shape[r]*B.shape[r] for r in range(3)])
            inds=[]
            for r in range(3):
                w=D.neighbor[(global_u,r)]
                inds.append(internal_eidx[tuple(sorted((global_u,w)))])
            args.extend([X,inds])
        args.append([])
        return oe.contract(*args,optimize='greedy')

    K=np.empty((len(states),len(states)),complex)
    for i in range(len(states)):
        for j in range(i,len(states)):
            z=overlap(i,j)
            K[i,j]=z;K[j,i]=np.conjugate(z)

    Gsrc=C.conj().T@K@C
    Gsrc=.5*(Gsrc+Gsrc.conj().T)
    return states,C,K,Gsrc,perms


def structural_rank_theorem(Gsrc,perms):
    phase=np.array([permutation_parity(p) for p in perms],float)
    H=Gsrc*phase[:,None]*phase[None,:]
    groups=[tuple(sorted(p[:2])) for p in perms]
    census=Counter(groups)
    if sorted(census.values())!=[4]*6:
        raise RuntimeError(('bad coarse-edge cosets',census))

    d=float(np.mean(np.diag(H).real))
    if d<=0:
        raise RuntimeError(('nonpositive boundary norm square',d))
    same=[];different=[]
    for i in range(24):
        for j in range(24):
            z=H[i,j]/d
            (same if groups[i]==groups[j] else different).append(z)
    r=float(np.mean([z.real for z in different]))

    predicted=np.empty_like(H)
    for i in range(24):
        for j in range(24):
            predicted[i,j]=d*(1.0 if groups[i]==groups[j] else r)

    same_def=max(abs(z-1) for z in same)
    diff_def=max(abs(z-r) for z in different)
    structure_rel=float(np.linalg.norm(H-predicted)/max(np.linalg.norm(H),1e-300))
    imag_rel=float(np.max(np.abs(H.imag))/d)

    lambda_uniform=4*d*(1+5*r)
    lambda_shape=4*d*(1-r)
    structural_rank=6 if abs(1-r)>1e-8 and abs(1+5*r)>1e-8 else None

    evals=np.linalg.eigvalsh(H)
    return {
        'parity_rephased_same_edge_normalized_max_defect':float(same_def),
        'parity_rephased_different_edge_normalized_max_defect':float(diff_def),
        'block_model_relative_defect':structure_rel,
        'imaginary_relative_defect':imag_rel,
        'd_boundary_norm_square':d,
        'r_inter_edge_overlap':r,
        'coarse_edge_groups':[list(g) for g in groups],
        'coarse_edge_group_census':{str(k):v for k,v in sorted(census.items())},
        'analytic_nonzero_eigenvalues':{
            'uniform_trace_like':lambda_uniform,
            'fivefold_shape_like':lambda_shape,
            'zero_multiplicity':18,
        },
        'numeric_eigenvalues_ascending':[float(x) for x in evals],
        'structural_boundary_rank':structural_rank,
    }


def run():
    t0=time.perf_counter()
    D,G,nodes,inside,internal_edges,internal_eidx,cols,worker_rows,slot_checks=build_strict_columns()
    states,C,K,Gsrc,perms=boundary_gram(D,G,nodes,inside,internal_edges,internal_eidx,cols)
    theorem=structural_rank_theorem(Gsrc,perms)

    Kherm=float(np.linalg.norm(K-K.conj().T)/max(np.linalg.norm(K),1e-300))
    Kevals=np.linalg.eigvalsh(.5*(K+K.conj().T))
    Gherm=float(np.linalg.norm(Gsrc-Gsrc.conj().T)/max(np.linalg.norm(Gsrc),1e-300))

    checks={
        'L1_full_closed_nodes_384':D.n_tets==384,
        'L1_full_closed_dual_links_768':len(G.EDGES)==768,
        'canonical_parent_has_24_chambers':len(nodes)==24,
        'canonical_parent_has_36_internal_links':len(internal_edges)==36,
        'canonical_slots_012_internal_3_boundary':all(slot_checks),
        'one_strict_q4_spec_per_source':all(r['strict_specs']==1 for r in worker_rows),
        'six_total_q4_specs_per_source':all(r['q4_specs_total']==6 for r in worker_rows),
        'twenty_projected_states_per_source':all(r['projected_microscopic_support']==20 for r in worker_rows),
        'strict_channel_boundary_spins_unchanged':all(r['boundary_spins_unchanged'] for r in worker_rows),
        'strict_channel_exterior_exact_background':all(r['exterior_exactly_background_by_labels'] for r in worker_rows),
        'boundary_kernel_Hermitian':Kherm<1e-12,
        'boundary_kernel_numeric_PSD':float(Kevals.min())>-1e-18,
        'source_Gram_Hermitian':Gherm<1e-12,
        'six_edge_cosets_of_four':len(set(tuple(x) for x in theorem['coarse_edge_groups']))==6,
        'exact_two_overlap_block_structure':theorem['block_model_relative_defect']<STRUCT_TOL,
        'structural_rank_is_6':theorem['structural_boundary_rank']==6,
    }

    return {
        'status':'exact strict-interior L1 q4 coarse-boundary rank theorem',
        'passed':bool(all(checks.values())),
        'science_status':'L1_STRICT_INTERIOR_BOUNDARY_RANK_PRECURSOR',
        'checks':checks,
        'microscopic_source_columns':24,
        'microscopic_states_unique_after_block_restriction':len(states),
        'microscopic_occurrences':int(np.count_nonzero(C)),
        'support_multiplicity_histogram':{str(k):v for k,v in sorted(Counter(np.count_nonzero(C,axis=1)).items())},
        'worker_rows':worker_rows,
        'boundary_kernel_min_numeric_eigenvalue':float(Kevals.min()),
        'boundary_kernel_max_numeric_eigenvalue':float(Kevals.max()),
        'boundary_kernel_Hermiticity_relative_defect':Kherm,
        'source_Gram_Hermiticity_relative_defect':Gherm,
        **theorem,
        'runtime_seconds':time.perf_counter()-t0,
        'interpretation':'Contracting the 36 internal links maps the 24 strict-interior fine-chamber Euclidean directions onto exactly six coarse-edge-labelled boundary directions. The six channels decompose into one uniform and five degenerate orthogonal shape directions in this homogeneous channel. This dimension match is a metric-tangent precursor, not yet a DeWitt/GR result.',
        'scope_note':'Strict-interior q4 / vacuum-exterior channel only. Crossing q4 sectors, full one-E support, Hermitian Lorentzian S, route, depth-two Krylov closure, metric Hessian and collective HDA remain required for the production W_block and GR-universality verdict.'
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path)
    a=p.parse_args();o=run();txt=json.dumps(o,indent=2);print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
