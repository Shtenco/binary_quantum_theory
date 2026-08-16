#!/usr/bin/env python3
"""Exact conservative one-S boundary support of the canonical barycentric block.

The production Hermitian Lorentzian block is S=-i(L-L^dagger)/2. Dagger does
not enlarge fundamental-holonomy hit support, so it is enough to enumerate the
nested raw Lorentzian support C_i(K) C_j(K) C_k(V), K~[V,E], on the full L1
barycentric 16-cell dual complex.

No amplitudes and no GR targets enter. This is a target-independent support
wall for the first dynamical collective carrier, not a claim that every
reachable representation has nonzero final amplitude.
"""
from __future__ import annotations
import argparse,itertools,json,sys
from collections import Counter,defaultdict
from functools import lru_cache
from pathlib import Path
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
from pl_dual_complex import DualComplex,seed_16cell_boundary,faces_by_dim


def barycentric_with_parent(tets):
    F=faces_by_dim(tets);allf=sorted(set().union(*F.values()),key=lambda x:(len(x),x));fid={f:i for i,f in enumerate(allf)}
    fine=[];parent=[]
    for pi,t in enumerate(tets):
        for p in itertools.permutations(t):
            cur=[];chain=[]
            for v in p:cur.append(v);chain.append(fid[tuple(sorted(cur))])
            fine.append(tuple(chain));parent.append(pi)
    return fine,parent


def e_profiles(D,v):
    out=[]
    for omitted in range(4):
        tri=tuple(r for r in range(4) if r!=omitted)
        for a,b,c in ((tri[0],tri[1],tri[2]),(tri[1],tri[2],tri[0]),(tri[2],tri[0],tri[1])):
            h=Counter();w=D.neighbor[(v,c)];h[tuple(sorted((v,w)))]+=2
            p=D.plaquette_path(v,a,b)
            for x,y in zip(p[:-1],p[1:]):h[tuple(sorted((x,y)))]+=1
            out.append(h)
    return tuple(out)


def spin_after_hits(n):
    S={1}
    for _ in range(n):S={y for x in S for y in (x-1,x+1) if y>=0}
    return S


def couple_support(spins):
    total={0}
    for s in spins:
        nxt=set()
        for a in total:nxt.update(range(abs(a-s),a+s+1,2))
        total=nxt
    return total


@lru_cache(None)
def face_support(hit_tuple):
    opts=[sorted(spin_after_hits(n)) for n in hit_tuple];out=set()
    for spins in itertools.product(*opts):out|=couple_support(spins)
    return frozenset(out)


def block_summary(D,parent,parent_id):
    inside={v for v,p in enumerate(parent) if p==parent_id}
    boundary=[e for e in D.dual_edges() if (e[0] in inside)^(e[1] in inside)]
    group=defaultdict(list);edge_group={}
    for e in boundary:
        a,b=e;outside=b if a in inside else a;g=parent[outside];group[g].append(e);edge_group[e]=g
    if sorted(len(es) for es in group.values())!=[6,6,6,6]:raise RuntimeError(('bad boundary partition',parent_id))
    for g in group:group[g]=sorted(group[g])

    union={g:set() for g in group};patterns=Counter();nprof=0;max_face=0;max_link=0
    for v in sorted(inside):
        EP=e_profiles(D,v)
        for i,j,k in itertools.permutations(range(4),3):
            outer=Counter()
            for r in (i,j,k):outer[tuple(sorted((v,D.neighbor[(v,r)])))]+=2
            for p1 in EP:
                for p2 in EP:
                    h=Counter();h.update(outer);h.update(p1);h.update(p2)
                    bh={e:n for e,n in h.items() if e in edge_group};by=Counter()
                    for e,n in bh.items():by[edge_group[e]]+=n
                    patterns[tuple(sorted(by.values()))]+=1;nprof+=1
                    if by:max_face=max(max_face,max(by.values()))
                    if bh:max_link=max(max_link,max(bh.values()))
                    for g,edges in group.items():union[g].update(face_support(tuple(bh.get(e,0) for e in edges)))
    all_support=sorted(set().union(*union.values()))
    return {'parent':parent_id,'fine_tetrahedra':len(inside),'boundary_links':len(boundary),'boundary_links_per_face':sorted(len(x) for x in group.values()),
            'lorentzian_support_profiles':nprof,'max_hits_on_one_coarse_face':max_face,'max_hits_on_one_boundary_fine_link':max_link,
            'coarse_face_total_spin2_support':all_support,'pattern_counts':{str(k):v for k,v in sorted(patterns.items())}}


def run():
    coarse=seed_16cell_boundary();fine,parent=barycentric_with_parent(coarse);D=DualComplex(fine)
    rows=[block_summary(D,parent,p) for p in range(len(coarse))];base=rows[0]
    core=lambda r:{k:v for k,v in r.items() if k!='parent'}
    identical=all(core(r)==core(base) for r in rows)
    expect_patterns={str(()):1296,str((1,1)):1728,str((1,3)):9216,str((1,5)):12096,
                     str((2,)):9936,str((2,2)):576,str((2,4)):1728,str((4,)):25200,str((6,)):21168}
    checks={'all_16_blocks_identical':identical,'profiles_per_block':base['lorentzian_support_profiles']==82944,
            'max_face_hits_is_6':base['max_hits_on_one_coarse_face']==6,'max_boundary_link_hits_is_6':base['max_hits_on_one_boundary_fine_link']==6,
            'full_spin2_support_0_to_12':base['coarse_face_total_spin2_support']==list(range(13)),
            'pattern_census':base['pattern_counts']==expect_patterns}
    return {'status':'target-independent one-S support of canonical barycentric block','passed':bool(all(checks.values())),'checks':checks,
            'fine_tetrahedra_total':len(fine),'coarse_blocks':len(coarse),'profiles_total':sum(r['lorentzian_support_profiles'] for r in rows),
            'canonical_block':base,'required_coarse_face_spins':[x/2 for x in range(13)],
            'one_step_production_face_wall':6.0,
            'interpretation':'One Hermitian Lorentzian S expands the exact conservative coarse-face support from the one-E wall j<=4 to j<=6. Since the operator-first route preserves spin labels, the one-step G+R collective carrier is finite with face support j=0,1/2,...,6 before amplitude pruning.',
            'amplitude_note':'Support reachability is conservative. Dynamical cancellations may remove sectors only after explicit amplitudes are computed; no sector may be removed beforehand to improve GR targets.',
            'scope_note':'One-S / one full production-constraint action only. Repeated collective actions require a separately frozen closure depth or leakage-controlled compression.'}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);a=ap.parse_args();o=run();txt=json.dumps(o,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
