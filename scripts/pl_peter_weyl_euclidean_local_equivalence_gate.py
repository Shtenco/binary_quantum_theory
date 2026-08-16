#!/usr/bin/env python3
"""Prove active-cone PL Euclidean backend equals the full reference backend.

The gate compares complete sparse physical-sine columns, including support and
complex amplitudes, on two orientation-distinct nodes of the 16-cell S3.  The
local backend may be used on refinement levels only after this exact regression
passes.  Performance is reported but never used as a science acceptance test.
"""
from __future__ import annotations
import argparse,json,math,time
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import peter_weyl_zeroaware_volume_migration_experiment as ZVM
from pl_dual_complex import DualComplex,seed_16cell_boundary
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean
from pl_peter_weyl_euclidean_local import LocalPLPeterWeylEuclidean

TOL=1e-10
JMAX2=3


def norm2(s):
    return sum(abs(a)**2 for a in s.values())


def relerr(a,b):
    keys=set(a)|set(b)
    num=math.sqrt(sum(abs(a.get(k,0j)-b.get(k,0j))**2 for k in keys))
    den=math.sqrt(max(norm2(b),1e-300))
    return num/den


def run():
    ZVM.patch_and_clear()
    D=DualComplex(seed_16cell_boundary())
    full=PLPeterWeylEuclidean(D)
    local=LocalPLPeterWeylEuclidean(D)
    seed=((1,)*len(full.EDGES),(0,)*D.n_tets)
    rows=[]
    for v in (0,D.n_tets-1):
        t=time.perf_counter();a=full.H_sine_basis(seed,v,JMAX2,TOL);tf=time.perf_counter()-t
        t=time.perf_counter();b=local.H_sine_basis(seed,v,JMAX2,TOL);tl=time.perf_counter()-t
        rows.append({
            'node':v,
            'full_support':len(a),
            'local_support':len(b),
            'support_exact':set(a)==set(b),
            'relative_amplitude_error':relerr(b,a),
            'full_norm':full.norm(a),
            'local_norm':local.norm(b),
            'full_seconds':tf,
            'local_seconds':tl,
            'speedup':tf/max(tl,1e-12),
        })
    checks={
        'all_support_exact':all(r['support_exact'] for r in rows),
        'all_amplitudes_exact_1e-10':all(r['relative_amplitude_error']<1e-10 for r in rows),
        'all_nonzero':all(r['full_support']>0 and r['local_support']>0 for r in rows),
    }
    return {
        'status':'exact equivalence of full and active-cone PL Peter-Weyl Euclidean backends',
        'passed':bool(all(checks.values())),
        'Jmax':JMAX2/2,
        'nodes_tested':[r['node'] for r in rows],
        'checks':checks,
        'rows':rows,
        'science_note':'This gate validates only an exact computational factorization of untouched-node overlaps. It changes no BCQG operator or physical result.',
        'next_use':'After PASS, use LocalPLPeterWeylEuclidean for the 384-node first-refinement block amplitude producer.'
    }


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();txt=json.dumps(o,indent=2);print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
