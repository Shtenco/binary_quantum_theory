#!/usr/bin/env python3
"""Regress the graph-independent Peter-Weyl Euclidean engine and open the 16-cell habitat.

1. On the boundary of a 4-simplex, the new dual-complex engine must reproduce
   the frozen K5 physical-sine H_E exactly up to the independently fixed
   tetrahedron orientation sign.
2. Without changing SU(2)/CG/volume algebra, apply the same H_E to the canonical
   16-cell PL-S3 dual graph, where every regulator face is a square rather than
   a triangle.
"""
from __future__ import annotations
import argparse,json,math,sys
from collections import Counter
from pathlib import Path

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))
import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_euclidean_sine_ordering_gate as ES
from pl_dual_complex import DualComplex,boundary_4simplex,seed_16cell_boundary
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean


def relerr(a,b,scale=1.0):
    keys=set(a)|set(b)
    num=math.sqrt(sum(abs(a.get(k,0j)-scale*b.get(k,0j))**2 for k in keys))
    den=math.sqrt(sum(abs(x)**2 for x in b.values()))
    return num/max(den,1e-30)


def run():
    JMAX2=3
    K=DualComplex(boundary_4simplex())
    G=PLPeterWeylEuclidean(K)
    initial=PW.basis_full_jhalf()[0]
    k5_rows=[]
    for v in (0,1):
        old=ES.safe_H_sine({initial:1+0j},v,JMAX2)
        new=G.H_sine_basis(initial,v,JMAX2)
        e=relerr(new,old,K.orientation[v])
        k5_rows.append({
          'node':v,'orientation_sign':K.orientation[v],
          'old_support':len(old),'new_support':len(new),
          'old_norm':G.norm(old),'new_norm':G.norm(new),
          'relative_error_after_orientation_sign':e
        })

    C=DualComplex(seed_16cell_boundary())
    P=PLPeterWeylEuclidean(C)
    seed=((1,)*len(P.EDGES),(0,)*C.n_tets)
    h=P.H_sine_basis(seed,0,JMAX2)
    changed=Counter(sum(s!=1 for s in key[0]) for key in h)
    max_spin=max((max(key[0]) for key in h),default=0)/2
    hnorm=P.norm(h)
    reference={
      'support':84,
      'norm':2.1442780351315593,
      'max_spin':1.0,
      'changed_edge_count_distribution':{'4':84}
    }
    sixteen={
      'nodes':C.n_tets,'dual_edges':len(P.EDGES),
      'node':0,'node_orientation_sign':C.orientation[0],
      'Jmax':JMAX2/2,'seed':'all dual links j=1/2; all node K=0',
      'H_sine_support':len(h),'H_sine_norm':hnorm,
      'max_spin_reached':max_spin,
      'changed_edge_count_distribution':{str(k):v for k,v in sorted(changed.items())},
      'reference':reference
    }
    sixteen['reference_errors']={
      'support':abs(len(h)-reference['support']),
      'norm':abs(hnorm-reference['norm']),
      'max_spin':abs(max_spin-reference['max_spin']),
      'changed_distribution_match':sixteen['changed_edge_count_distribution']==reference['changed_edge_count_distribution']
    }
    k5_ok=max(r['relative_error_after_orientation_sign'] for r in k5_rows)<1e-11
    ref_ok=(sixteen['reference_errors']['support']==0 and
            sixteen['reference_errors']['norm']<1e-10 and
            sixteen['reference_errors']['max_spin']<1e-12 and
            sixteen['reference_errors']['changed_distribution_match'])
    return {
      'status':'graph-independent Peter-Weyl physical-sine Euclidean operator',
      'passed':bool(k5_ok and ref_ok),
      'K5_regression':k5_rows,
      'sixteen_cell_first_column':sixteen,
      'key_result':'The frozen K5 operator is exactly the triangular-dual-face special case, and the same Peter-Weyl algebra gives a nonzero finite H_E^sine column on the independent 16-cell PL-S3 habitat.',
      'next_gate':'Compute neighboring-node H_E commutator on the 16-cell habitat, then add the Hermitian Lorentzian and operator-first route sectors using the same dual-complex regulator.',
      'scope_note':'One 16-cell Euclidean column only; not yet a 16-cell full HDA PASS.'
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path)
    a=ap.parse_args(); o=run(); t=json.dumps(o,indent=2); print(t)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
