#!/usr/bin/env python3
"""Freeze and verify the same intrinsic S3 l=1 lapse family through L3.

This is a protocol gate, not a GR/HDA science result.  Lapses are ambient radial
coordinate harmonics evaluated on dual-cell centroids of the canonical embedded
16-cell barycentric refinement.  No target-dependent fit or per-level lapse
renormalization is performed.
"""
from __future__ import annotations
import argparse,itertools,json,math,sys
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
from collective_regular_background_metric_dimension_gate import seed,subdivide

PAIRS=tuple(itertools.combinations(range(4),2));PRIMARY=(0,1)

def level(coords,tets,l):
    # Dual nodes are tetrahedral chamber centroids.  Radial projection supplies
    # one fixed unit-S3 coordinate chart family across all subdivision levels.
    P=np.asarray([coords[list(t)].mean(axis=0) for t in tets],float)
    nr=np.linalg.norm(P,axis=1)
    if float(nr.min())<1e-14:raise RuntimeError(('zero radial centroid',l,float(nr.min())))
    X=P/nr[:,None]
    mean=X.mean(axis=0);cov=(X.T@X)/len(X);rms=np.sqrt(np.diag(cov))
    tangent={};max_tan=0.0
    for mu,nu in PAIRS:
        B=np.zeros_like(X);B[:,nu]=X[:,mu];B[:,mu]=-X[:,nu]
        defect=np.abs(np.einsum('ij,ij->i',X,B));mx=float(defect.max());max_tan=max(max_tan,mx)
        tangent[f'{mu},{nu}']={'max_radial_dot':mx,'rms_shift_norm':float(np.sqrt(np.mean(np.sum(B*B,axis=1))))}
    iso=np.eye(4)*float(np.trace(cov))/4
    return {'level':l,'vertices':len(coords),'tetrahedra':len(tets),'dual_nodes':len(tets),
            'minimum_centroid_radius':float(nr.min()),'maximum_centroid_radius':float(nr.max()),
            'lapse_means':mean.tolist(),'lapse_rms':rms.tolist(),'lapse_covariance':cov.tolist(),
            'covariance_isotropy_defect':float(np.linalg.norm(cov-iso)/max(np.linalg.norm(iso),1e-30)),
            'max_abs_lapse_mean':float(np.max(np.abs(mean))),'pair_rotation_fields':tangent,
            'max_tangency_defect':max_tan}

def run(max_level=3):
    c,t=seed();rows=[]
    for l in range(max_level+1):
        rows.append(level(c,t,l))
        if l<max_level:c,t=subdivide(c,t)
    rms=np.asarray([r['lapse_rms'] for r in rows]);reference=rms[0]
    max_rms_drift=float(np.max(np.abs(rms-reference)))
    checks={'four_levels_L0_to_L3':len(rows)==4,
            'all_centroids_nonzero':all(r['minimum_centroid_radius']>1e-14 for r in rows),
            'zero_lapse_means':max(r['max_abs_lapse_mean'] for r in rows)<1e-12,
            'coordinate_covariance_isotropic':max(r['covariance_isotropy_defect'] for r in rows)<1e-12,
            'no_level_dependent_lapse_RMS_drift':max_rms_drift<1e-12,
            'all_six_rotation_fields_tangent':max(r['max_tangency_defect'] for r in rows)<1e-12,
            'primary_pair_frozen':PRIMARY==(0,1),
            'five_heldout_pairs':len(PAIRS)-1==5}
    return {'status':'frozen intrinsic S3 l=1 collective lapse family','passed':bool(all(checks.values())),
            'science_status':'PROTOCOL_ONLY','primary_pair':list(PRIMARY),
            'heldout_pairs':[list(x) for x in PAIRS if x!=PRIMARY],
            'definition':'N_mu(x)=x_mu at radially normalized dual-cell centroid; no per-level amplitude fit',
            'max_lapse_RMS_drift':max_rms_drift,'checks':checks,'levels':rows,
            'interpretation':'The same four lowest nonconstant S3 scalar harmonics and all six SO(4) rotation pairs are transported through the canonical barycentric refinement before any collective HDA result is inspected.',
            'scope_note':'Lapse/shift protocol only. The measured collective metric still determines sharp_Q and the diffeomorphism target.'}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--max-level',type=int,default=3);p.add_argument('--output',type=Path);a=p.parse_args();o=run(a.max_level);txt=json.dumps(o,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+'\n')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
