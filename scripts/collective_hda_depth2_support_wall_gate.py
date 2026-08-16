#!/usr/bin/env python3
"""Exact conservative depth-2 coarse-face support wall for collective HDA.

The one-S barycentric gate proves that one production Lorentzian action has 121
unique hit-tuples on a fixed coarse face.  A Hamiltonian-Hamiltonian commutator
requires two constraint actions.  Before amplitudes are inspected, form every
pair-sum of the one-S hit tuples and compute exact SU(2) reachability.

Route is spin-preserving and E has smaller support than S, so SxS is a
conservative wall for every depth-2 term in [H,H].
"""
from __future__ import annotations
import argparse,itertools,json,sys
from collections import Counter,defaultdict
from pathlib import Path
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
from pl_dual_complex import DualComplex,seed_16cell_boundary
import collective_barycentric_S_boundary_support_gate as SG


def one_S_hit_tuples():
    coarse=seed_16cell_boundary();fine,parent=SG.barycentric_with_parent(coarse);D=DualComplex(fine)
    inside={v for v,p in enumerate(parent) if p==0}
    boundary=[e for e in D.dual_edges() if (e[0] in inside)^(e[1] in inside)]
    group=defaultdict(list);edge_group={}
    for e in boundary:
        a,b=e;outside=b if a in inside else a;g=parent[outside];group[g].append(e);edge_group[e]=g
    for g in group:group[g]=sorted(group[g])
    face=sorted(group)[0];edges=group[face];out=set()
    for v in sorted(inside):
        EP=SG.e_profiles(D,v)
        for i,j,k in itertools.permutations(range(4),3):
            outer=Counter()
            for r in (i,j,k):outer[tuple(sorted((v,D.neighbor[(v,r)])))]+=2
            for p1 in EP:
                for p2 in EP:
                    h=Counter();h.update(outer);h.update(p1);h.update(p2)
                    out.add(tuple(h.get(e,0) for e in edges))
    return sorted(out)


def run():
    one=one_S_hit_tuples()
    two={tuple(a[i]+b[i] for i in range(6)) for a in one for b in one}
    support=set()
    for h in two:support.update(SG.face_support(h))
    support=sorted(support)
    checks={'one_S_unique_hit_tuples':len(one)==121,
            'depth2_unique_pair_sum_tuples':len(two)==4447,
            'max_total_face_hits_12':max(sum(x) for x in two)==12,
            'max_single_boundary_link_hits_12':max(max(x) for x in two)==12,
            'depth2_spin2_support_0_to_18':support==list(range(19))}
    return {'status':'exact conservative depth-2 collective HDA coarse-face support wall',
            'passed':bool(all(checks.values())),'checks':checks,
            'one_S_unique_hit_tuples':len(one),'depth2_unique_hit_tuples':len(two),
            'max_total_hits_on_face':max(sum(x) for x in two),
            'max_hits_on_one_boundary_link':max(max(x) for x in two),
            'coarse_face_total_spin2_support':support,
            'required_depth2_coarse_face_spins':[x/2 for x in support],
            'sufficient_depth2_face_Jmax':9.0,
            'interpretation':'Every two-action E/S/R term needed by the first collective [H,H] experiment fits inside the target-independent coarse-face representation wall j=0,1/2,...,9. SxS is conservative because one S has the largest spin-changing support and the operator-first route preserves spins.',
            'scope_note':'Representation support only. The production effective basis is the amplitude-level operator-image/Krylov span inside this wall, with leakage reported; the full direct sum of all support multiplicities is neither required nor computationally sensible.'}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);a=ap.parse_args();o=run();txt=json.dumps(o,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
