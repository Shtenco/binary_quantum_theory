#!/usr/bin/env python3
"""Exact one-E amplitude column for one fine node of a canonical L1 block.

Construct the full L1 barycentric subdivision of the 16-cell S3 so every dual
plaquette is complete. Select parent coarse tetrahedron 0 and one of its 24
fine tetrahedral chambers. Compute the production zero-aware physical-sine
E_u|Omega_L1> column in the global 384-node / 768-dual-link Peter-Weyl habitat.

This is the first direct refinement-level amplitude precursor. It does not yet
contract the 36 internal block links or define a coarse boundary isometry.
"""
from __future__ import annotations
import argparse,json,traceback
from collections import Counter
from pathlib import Path
import numpy as np
import peter_weyl_zeroaware_volume_migration_experiment as ZVM
from pl_dual_complex import DualComplex,seed_16cell_boundary
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean
from collective_barycentric_E_boundary_support_gate import barycentric_with_parent

JMAX2=3

def encode(key,amp):
    return {'spins':list(key[0]),'Ks':list(key[1]),'re':float(amp.real),'im':float(amp.imag)}

def run(local_index,parent_id=0):
    ZVM.patch_and_clear()
    coarse=seed_16cell_boundary()
    fine,parent=barycentric_with_parent(coarse)
    D=DualComplex(fine)
    G=PLPeterWeylEuclidean(D)
    inside=sorted(v for v,p in enumerate(parent) if p==parent_id)
    if len(inside)!=24:
        raise RuntimeError(('parent block size',len(inside)))
    if not 0<=local_index<24:
        raise ValueError(local_index)
    v=inside[local_index]
    seed=((1,)*len(G.EDGES),(0,)*D.n_tets)
    col=G.H_sine_basis(seed,v,JMAX2)
    n=G.norm(col)
    changed=Counter(sum(s!=1 for s in key[0]) for key in col)
    par=Counter(sum(key[0])%2 for key in col)

    # Identify the block boundary dual links for later projection diagnostics.
    ins=set(inside)
    boundary=[e for e in G.EDGES if (e[0] in ins)^(e[1] in ins)]
    patterns=Counter()
    for key in col:
        patterns[tuple(key[0][G.EIDX[e]] for e in boundary)]+=1

    finite=all(np.isfinite([z.real,z.imag]).all() for z in col.values())
    max_spin2=max((max(k[0]) for k in col),default=-1)
    spin3_states=sum(1 for k in col if 3 in k[0])
    checks={
        'L1_nodes_384':D.n_tets==384,
        'L1_dual_links_768':len(G.EDGES)==768,
        'parent_has_24_fine_nodes':len(inside)==24,
        'parent_boundary_has_24_dual_links':len(boundary)==24,
        'column_nonzero':len(col)>0 and n>1e-12,
        'finite_amplitudes':finite,
        # One T term can hit a microscopic source link twice. Starting from
        # doubled spin 1, representation support therefore allows spin2=3.
        # Whether physical-sine cancellations remove that sector is measured,
        # never imposed as a hard truncation.
        'within_preregistered_worker_cutoff':max_spin2<=JMAX2,
    }
    return {
        'status':'exact L1 barycentric fine-node Euclidean amplitude column',
        'passed':bool(all(checks.values())),
        'science_status':'L1_BLOCK_E_PRECURSOR',
        'parent_coarse_tetra':parent_id,
        'local_fine_index':local_index,
        'global_fine_node':v,
        'L1_nodes':D.n_tets,
        'L1_dual_links':len(G.EDGES),
        'parent_fine_nodes':inside,
        'parent_boundary_dual_links':[list(e) for e in boundary],
        'support':len(col),
        'norm':n,
        'max_reached_doubled_spin':max_spin2,
        'spin3_state_count':spin3_states,
        'spin3_cancellation_diagnostic':spin3_states==0,
        'changed_edge_count_distribution':{str(k):v for k,v in sorted(changed.items())},
        'sum_doubled_spin_parity_distribution':{str(k):v for k,v in sorted(par.items())},
        'distinct_boundary_spin_patterns':len(patterns),
        'boundary_pattern_multiplicities':sorted(patterns.values()),
        'checks':checks,
        'seed':{'spins':list(seed[0]),'Ks':list(seed[1])},
        'column':[encode(k,a) for k,a in sorted(col.items(),key=lambda kv:repr(kv[0]))],
        'interpretation':'A genuine exact E column on the first barycentric refinement level, computed on the full closed regulator rather than truncating plaquettes at the coarse-block boundary.',
        'scope_note':'Fine-Hilbert amplitude precursor only. Internal-link contraction and the coarse boundary isometry W_block are separate next steps.'
    }

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--local-index',type=int,choices=range(24),required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    try:
        o=run(a.local_index);code=0 if o['passed'] else 1
    except Exception as exc:
        o={'status':'worker exception','passed':False,'science_status':'INFRASTRUCTURE_DIAGNOSTIC','local_fine_index':a.local_index,'error_type':type(exc).__name__,'error':str(exc),'traceback':traceback.format_exc()};code=1
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in o.items() if k!='column'},indent=2))
    return code

if __name__=='__main__':
    raise SystemExit(main())
