#!/usr/bin/env python3
"""Canonical runner for the L1 q4 extended-Hilbert boundary decomposition.

This thin runner reuses all low-level reconstruction/contraction helpers from
``collective_l1_q4_extended_boundary_collect.py`` but fixes the vacuum-sector
key to the actual environment tuple ``((),())``.  The older module remains a
library; this file is the executable science gate.
"""
from __future__ import annotations
import argparse,json,traceback
from collections import Counter
from pathlib import Path
import numpy as np
import collective_l1_q4_extended_boundary_collect as B


def calculate(root):
    workers=B.load_rows(root)
    D,G,inside,nodes,internal,boundary,IE,BE,boundary_by_node,groups,occ_patterns,slot_ok=B.reconstruct_groups(workers)
    total=np.zeros((24,24),complex);sector_stats=Counter();vacuum_G=None
    vacuum_key=(((),()),tuple([1]*len(boundary)))
    for key,srcdict in groups.items():
        srcs,Gs,nstates,nocc=B.sector_source_gram(D,nodes,inside,internal,IE,BE,boundary_by_node,key,srcdict)
        for i,si in enumerate(srcs):
            for j,sj in enumerate(srcs):total[si,sj]+=Gs[i,j]
        sector_stats[(len(srcs),nocc,nstates)]+=1
        if key==vacuum_key:
            if srcs!=list(range(24)):raise RuntimeError('vacuum sector missing source columns')
            vacuum_G=Gs
    if vacuum_G is None:raise RuntimeError(('no strict vacuum sector',len(groups)))
    total=.5*(total+total.conj().T);evals=np.linalg.eigvalsh(total);svals=np.sqrt(np.maximum(evals,0))[::-1];smax=max(float(svals[0]),1e-300);rank=int(np.sum(svals/smax>B.REL));covdef,kernel=B.left_S4_covariance(total);strict=B.strict_structure(vacuum_G)
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
        'status':'exact L1 q4 extended-Hilbert coarse-boundary decomposition','passed':bool(all(checks.values())),'science_status':'L1_Q4_EXTENDED_BOUNDARY_PRECURSOR','checks':checks,
        'sector_count':len(groups),'sector_shape_histogram':{str(k):v for k,v in sorted(sector_stats.items())},'occurrence_pattern_census':{str(k):v for k,v in sorted(occ_patterns.items())},'vacuum_sector':strict,
        'extended_source_rank':rank,'extended_Gram_eigenvalues_ascending':[float(x) for x in evals],'extended_singular_values_descending':[float(x) for x in svals],'extended_min_eigenvalue':float(evals.min()),'extended_max_eigenvalue':float(evals.max()),'extended_min_to_max_singular_ratio':float(svals[-1]/svals[0]),
        'left_S4_covariance_relative_defect':covdef,'left_S4_rephased_convolution_kernel_normalized':kernel,
        'interpretation':'The q4 Euclidean image separates target-independently into a six-dimensional strict-interior coarse-edge carrier and orthogonal crossing/environment sectors. Retaining the latter restores full rank 24, so coarse-graining classifies rather than deletes the fine directions.',
        'scope_note':'q4 Euclidean depth-one only; S, route and depth-two histories are still required before the production GR-universality measurement.'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    try:o=calculate(a.root);code=0 if o['passed'] else 1
    except Exception as exc:o={'status':'collector exception','passed':False,'science_status':'INFRASTRUCTURE_DIAGNOSTIC','error_type':type(exc).__name__,'error':str(exc),'traceback':traceback.format_exc()};code=1
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8');print(json.dumps(o,indent=2));return code

if __name__=='__main__':raise SystemExit(main())
