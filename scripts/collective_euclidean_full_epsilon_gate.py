#!/usr/bin/env python3
"""Target-independent audit of cyclic vs fully antisymmetrized tetrahedral Euclidean epsilon ordering.

On the canonical 16-cell PL-S3 seed compare the production cyclic-frame
construction

    E_cyclic = sum_omit eta_omit sum_{3 cyclic} e_{abc}

with the explicitly antisymmetrized form

    E_full = 1/2 sum_omit eta_omit sum_{pi in S3} sgn(pi) e_{pi(a,b,c)}.

The factor 1/2 makes the two definitions identical if the elementary sine term
is exactly antisymmetric under swapping its first two local slots.  No GR,
Lorentzian, HDA or continuum target enters this test.  The preregistered
v1.3 tetrahedral charged-volume backend is used throughout.
"""
from __future__ import annotations
import argparse,itertools,json,math,sys,traceback
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
from pl_dual_complex import DualComplex,seed_16cell_boundary
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean
from tetrahedral_volume_backend import install_tetrahedral_volume_backend

TOL=1e-9
JMAX2=5

def perm_sign(base,perm):
    idx=[base.index(x) for x in perm]
    inv=sum(idx[i]>idx[j] for i in range(3) for j in range(i+1,3))
    return -1 if inv%2 else 1

def norm(s):return math.sqrt(sum(abs(a)**2 for a in s.values()))
def relerr(a,b):
    keys=set(a)|set(b);num=math.sqrt(sum(abs(a.get(k,0j)-b.get(k,0j))**2 for k in keys));den=norm(b)
    return num/max(den,1e-300)
def add(dst,src,scale=1.0,tol=1e-12):
    for k,a in src.items():
        z=dst.get(k,0j)+scale*a
        if abs(z)>tol:dst[k]=z
        elif k in dst:del dst[k]

def sine_term(G,key,v,a,b,c):
    out={}
    add(out,dict(G.T_items(key,v,a,b,c,JMAX2,False)),-0.5j)
    add(out,dict(G.T_items(key,v,a,b,c,JMAX2,True)),+0.5j)
    return {k:z for k,z in out.items() if abs(z)>1e-10}

def run():
    D=DualComplex(seed_16cell_boundary());G=PLPeterWeylEuclidean(D)
    seed=((1,)*len(G.EDGES),(0,)*D.n_tets);v=0
    with install_tetrahedral_volume_backend():
        current=G.H_sine_basis(seed,v,JMAX2,TOL)
        full={};pair_rows=[];max_pair=0.0
        for omitted in range(4):
            base=tuple(r for r in range(4) if r!=omitted);eta=D.local_sign(v,omitted)
            # Three cyclic representatives and their first-two swaps.
            a,b,c=base
            cyc=((a,b,c),(b,c,a),(c,a,b))
            for p in cyc:
                q=(p[1],p[0],p[2]);A=sine_term(G,seed,v,*p);B=sine_term(G,seed,v,*q)
                tmp={};add(tmp,A,+1);add(tmp,B,+1)
                defect=norm(tmp)/max(norm(A),norm(B),1e-300);max_pair=max(max_pair,defect)
                pair_rows.append({'omitted':omitted,'ordered':list(p),'swapped_first_two':list(q),
                                  'support_A':len(A),'support_B':len(B),'norm_A':norm(A),'norm_B':norm(B),
                                  'antisymmetry_relative_defect':defect})
            for p in itertools.permutations(base):
                add(full,sine_term(G,seed,v,*p),0.5*eta*perm_sign(base,p))
        full={k:z for k,z in full.items() if abs(z)>TOL}
    err=relerr(full,current);support=set(full)==set(current)
    checks={
      'finite_current':all(np.isfinite([z.real,z.imag]).all() for z in current.values()),
      'finite_full':all(np.isfinite([z.real,z.imag]).all() for z in full.values()),
      'elementary_first_two_antisymmetry':bool(max_pair<TOL),
      'cyclic_equals_full_antisymmetrized':bool(err<TOL),
      'sparse_support_identical':bool(support),
    }
    return {'status':'16-cell tetrahedral Euclidean cyclic/full-epsilon audit','passed':bool(all(checks.values())),
      'science_status':'FINITE_OPERATOR_ORDERING_FALSIFIER','source_node':0,'Jmax':JMAX2/2,
      'checks':checks,'current_support':len(current),'full_support':len(full),'current_norm':norm(current),'full_norm':norm(full),
      'cyclic_vs_full_relative_error':err,'max_elementary_antisymmetry_defect':max_pair,'pair_rows':pair_rows,
      'definition':'E_full=(1/2) sum_omit eta_omit sum_{pi in S3} sgn(pi) e_pi using the same tetrahedral charged-volume backend as v1.3',
      'interpretation_if_pass':'The frozen 12-spec cyclic implementation is exactly equivalent to the complete tetrahedral epsilon contraction on this seed; the pairing-stabilizer E-character issue must then come from representation/frame structure rather than missing anti-cyclic terms.',
      'interpretation_if_fail':'The frozen cyclic Euclidean ordering is not the complete antisymmetrized tetrahedral epsilon operator at finite regulator and must be audited before using full tetrahedral covariance claims.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args()
    try:o=run();code=0 if o['passed'] else 1
    except Exception as exc:o={'status':'Euclidean full-epsilon audit exception','passed':False,'science_status':'INFRASTRUCTURE_DIAGNOSTIC','error_type':type(exc).__name__,'error':str(exc),'traceback':traceback.format_exc()};code=1
    t=json.dumps(o,indent=2,sort_keys=True);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return code
if __name__=='__main__':raise SystemExit(main())
