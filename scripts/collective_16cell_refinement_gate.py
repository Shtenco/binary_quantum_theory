#!/usr/bin/env python3
"""BCQG collective PL-S3 refinement gate.

Build the canonical 16-cell boundary and its barycentric refinements. The gate
separates exact topological dimension from the still-missing collective metric
and dynamical measurements. Level 0 and level 1 are exhaustively checked by
vertex-link GF(2) homology; level 2 is explicitly constructed and checked on a
deterministic vertex sample. The standard PL theorem that barycentric
subdivision preserves the PL-manifold class is recorded separately and is not
misreported as a numerical metric-dimension measurement.
"""
from __future__ import annotations
import argparse, itertools, json, math, sys
from collections import defaultdict
from pathlib import Path

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))
import manifold_dimension_gate as MD


def seed_16cell_boundary():
    # vertices 2*i and 2*i+1 are antipodal +/-e_i, i=0..3.
    return sorted(tuple(2*i + bit for i,bit in enumerate(bits))
                  for bits in itertools.product((0,1), repeat=4))


def faces_by_dim(tets):
    out=defaultdict(set)
    for tet in tets:
        for size in range(1,5):
            for f in itertools.combinations(tet,size):
                out[size-1].add(tuple(sorted(f)))
    return out


def f_vector(tets):
    F=faces_by_dim(tets)
    return [len(F[d]) for d in range(4)]


def barycentric_subdivision(tets):
    F=faces_by_dim(tets)
    all_faces=sorted(set().union(*F.values()), key=lambda x:(len(x),x))
    face_id={f:i for i,f in enumerate(all_faces)}
    subtets=set()
    for tet in tets:
        for perm in itertools.permutations(tet):
            chain=[]
            cur=[]
            for v in perm:
                cur.append(v)
                chain.append(face_id[tuple(sorted(cur))])
            subtets.add(tuple(chain))
    return sorted(subtets)


def barycentric_fvector(f):
    # f'_k = sum_{j>=k} f_j (k+1)! S(j+1,k+1), through dimension 3.
    S={(1,1):1,(2,1):1,(2,2):1,(3,1):1,(3,2):3,(3,3):1,
       (4,1):1,(4,2):7,(4,3):6,(4,4):1}
    out=[]
    for k in range(4):
        out.append(sum(f[j]*math.factorial(k+1)*S[(j+1,k+1)]
                       for j in range(k,4)))
    return out


def sampled_link_check(tets, n=64):
    verts=sorted(set(itertools.chain.from_iterable(tets)))
    if len(verts)<=n:
        sample=verts
    else:
        idx=sorted(set(round(i*(len(verts)-1)/(n-1)) for i in range(n)))
        sample=[verts[i] for i in idx]
    bad=[]; rows=[]
    for v in sample:
        b=MD.betti_numbers(MD.vertex_link(tets,v))
        ok=(b==[1,0,1])
        rows.append({'vertex':int(v),'link_betti_GF2':b,'passed':bool(ok)})
        if not ok:
            bad.append(int(v))
    return {'sample_size':len(sample),'bad_vertices':bad,
            'passed':not bad,'rows':rows}


def run(max_explicit_level=2, sample_level2=64):
    levels=[]
    tets=seed_16cell_boundary()
    expected=[8,24,32,16]
    for lev in range(max_explicit_level+1):
        fv=f_vector(tets)
        if fv!=expected:
            raise RuntimeError(f'f-vector mismatch L{lev}: {fv} != {expected}')
        row={'level':lev,'vertices':fv[0],'edges':fv[1],
             'triangles':fv[2],'tetrahedra':fv[3],
             'f_vector':fv,'topological_dimension':3}
        if lev<=1:
            a=MD.analyze(tets)
            row['link_check_mode']='exhaustive'
            row['dominant_local_dimension']=a['dominant_local_dimension']
            row['link_defect_fraction']=a['manifold_link_defect_fraction']
            row['link_check_passed']=(
                a['dominant_local_dimension']==3 and
                a['manifold_link_defect_fraction']==0.0)
        else:
            a=sampled_link_check(tets,sample_level2)
            row['link_check_mode']='deterministic_sample'
            row['link_sample_size']=a['sample_size']
            row['link_bad_vertices']=a['bad_vertices']
            row['link_check_passed']=a['passed']
        levels.append(row)
        if lev<max_explicit_level:
            tets=barycentric_subdivision(tets)
            expected=barycentric_fvector(expected)

    continuation=[]
    fv=levels[-1]['f_vector']
    for lev in range(max_explicit_level+1,5):
        fv=barycentric_fvector(fv)
        continuation.append({'level':lev,'f_vector':fv,
                             'vertices':fv[0],'tetrahedra':fv[3]})

    passed=all(r['link_check_passed'] for r in levels)
    return {
      'status':'collective PL-S3 refinement finite gate',
      'passed':bool(passed),
      'seed':'boundary of the 4D cross-polytope (16-cell)',
      'levels_explicit':levels,
      'f_vector_continuation':continuation,
      'pl_statement':'Barycentric subdivision of a PL manifold preserves its PL homeomorphism class; therefore every subdivision level of the frozen seed remains a PL 3-manifold/S3.',
      'what_is_directly_measured':'local topological/manifold dimension from vertex-link homology on explicit levels',
      'what_is_not_measured':'metric/Hausdorff dimension of a collective BCQG state, DeWitt coefficient, constraint rank, or collective HDA defect',
      'metric_D_space_available':False,
      'scope_note':'Topological D=3 is necessary but is not substituted for the collective metric criterion D_space -> 3.'
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--max-explicit-level',type=int,default=2,choices=(0,1,2))
    ap.add_argument('--sample-level2',type=int,default=64)
    ap.add_argument('--output',type=Path)
    a=ap.parse_args()
    out=run(a.max_explicit_level,a.sample_level2)
    text=json.dumps(out,indent=2)
    print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
