#!/usr/bin/env python3
"""BCQG graph-independent PL dual-face regulator gate.

Checks the geometry needed to lift the production K5 Euclidean plaquette from
triangle-only paths to arbitrary tetrahedral PL-3 dual complexes.  The closed
loop for a pair of local faces is the complete dual 2-cell around their common
primal edge.
"""
from __future__ import annotations
import argparse,json,sys
from collections import Counter
from pathlib import Path

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))
from pl_dual_complex import (DualComplex,boundary_4simplex,
                             seed_16cell_boundary,barycentric_subdivision)


def audit(name,tets):
    D=DualComplex(tets)
    degree=Counter()
    for v in range(D.n_tets):
        degree[len({D.neighbor[(v,r)] for r in range(4)})]+=1
    edge_val=Counter(len(ts) for ts in D.edge_incidence.values())
    local_paths=Counter(); bad_reverse=0; bad_len=0
    for v in range(D.n_tets):
        for r in range(4):
            for s in range(r+1,4):
                p=D.plaquette_path(v,r,s)
                q=D.plaquette_path(v,s,r)
                if p!=tuple(reversed(q)):
                    bad_reverse+=1
                e=D.primal_edge_for_face_pair(v,r,s)
                if len(p)-1!=len(D.edge_incidence[e]):
                    bad_len+=1
                local_paths[len(p)-1]+=1
    return {
      'name':name,'tetrahedra':D.n_tets,'dual_edges':len(D.dual_edges()),
      'primal_edges':len(D.edge_incidence),
      'dual_vertex_degree_distribution':{str(k):v for k,v in sorted(degree.items())},
      'primal_edge_valence_dual_face_length_distribution':{str(k):v for k,v in sorted(edge_val.items())},
      'local_oriented_plaquette_length_distribution':{str(k):v for k,v in sorted(local_paths.items())},
      'reverse_path_defects':bad_reverse,'length_defects':bad_len,
      'orientation_plus':sum(s==1 for s in D.orientation),
      'orientation_minus':sum(s==-1 for s in D.orientation),
      'passed':bool(degree==Counter({4:D.n_tets}) and bad_reverse==0 and bad_len==0)
    },D


def run():
    k5=boundary_4simplex()
    c16=seed_16cell_boundary()
    b1=barycentric_subdivision(c16)
    b2=barycentric_subdivision(b1)
    rows=[]; adapters={}
    for name,tets in [('4simplex_boundary_K5',k5),('16cell_boundary',c16),
                      ('16cell_barycentric_L1',b1),('16cell_barycentric_L2',b2)]:
        row,D=audit(name,tets); rows.append(row); adapters[name]=D

    # K5 compatibility: every dual node sees all four other facets and every
    # primal-edge dual face is triangular.
    K=adapters['4simplex_boundary_K5']
    k5_complete=all({K.neighbor[(v,r)] for r in range(4)}==set(range(5))-{v}
                    for v in range(5))
    k5_tri=all(len(ts)==3 for ts in K.edge_incidence.values())

    # Independent frozen 16-cell orientation character: tet vertices
    # (2*i+bit_i) have eta=(-1)^sum bits.  The orientability solver must recover
    # it up to one global sign; sign[0]=+1 fixes that global sign here.
    C=adapters['16cell_boundary']
    eta=[]
    for t in C.tets:
        eta.append((-1)**sum(v%2 for v in t))
    orient_eta=all(a==b for a,b in zip(C.orientation,eta))

    expected={
      '4simplex_boundary_K5':{'3':10},
      '16cell_boundary':{'4':24},
      '16cell_barycentric_L1':{'4':288,'6':128,'8':48},
      '16cell_barycentric_L2':{'4':6912,'6':3072,'8':576,'12':256,'16':96},
    }
    regression=all(r['primal_edge_valence_dual_face_length_distribution']==expected[r['name']]
                   for r in rows)
    passed=all(r['passed'] for r in rows) and k5_complete and k5_tri and orient_eta and regression
    return {
      'status':'graph-independent oriented PL dual-face regulator geometry',
      'passed':bool(passed),'rows':rows,
      'K5_complete_dual_graph':bool(k5_complete),
      'K5_all_regulator_faces_triangular':bool(k5_tri),
      'orientation_solver_matches_16cell_popcount_eta':bool(orient_eta),
      'plaquette_length_regression':bool(regression),
      'key_result':'The K5 path v-a-b-v is the valence-3 special case. Refinement requires the full dual 2-cell around each primal edge; L2 already contains loop lengths 4,6,8,12,16.',
      'production_rule':'Replace the hard-coded triangular plaquette in T_sequences by DualComplex.plaquette_path(v,r,s), while keeping the local oriented epsilon sign supplied by the tetrahedral frame.',
      'scope_note':'Geometry/regulator-path theorem and regression only; Peter-Weyl matrix amplitudes on the larger dual complexes are the next gate.'
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
