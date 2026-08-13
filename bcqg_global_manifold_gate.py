#!/usr/bin/env python3
"""Global PL-manifold completion gate for the frozen q=2 binary-route shell.

The frozen local q=2 rule has four route states Q_2=C_4 and two causal
endpoints, hence the local shell is the suspension Sigma C_4: the octahedral
2-sphere. This verifier constructs the minimal closed simplicial 3-manifold
whose vertex links are exactly that octahedral shell: the boundary of the
4D cross-polytope (16-cell). It then applies two global barycentric refinements
and checks every simplex link.

This closes a precise canonical PL-completion gate. It does not prove that the
bare causal edge-rewrite graph uniquely selects this global face pairing.
"""
from __future__ import annotations

import argparse
import itertools
import json
from collections import defaultdict, deque
from pathlib import Path


def faces_of_tets(tets, dim):
    out=set()
    for tet in tets:
        out.update(tuple(sorted(f)) for f in itertools.combinations(tet, dim+1))
    return out


def q2_shell():
    u,v=0,1; r=(2,3,4,5); tris=set()
    for i in range(4):
        a,b=r[i],r[(i+1)%4]
        tris.add(tuple(sorted((u,a,b))))
        tris.add(tuple(sorted((v,a,b))))
    return tris


def cross_polytope_boundary_4():
    return sorted({tuple(sorted(2*a+s[a] for a in range(4)))
                   for s in itertools.product((0,1),repeat=4)})


def barycentric_subdivision(tets):
    faces=set()
    for tet in tets:
        for size in range(1,5):
            faces.update(tuple(sorted(f)) for f in itertools.combinations(tet,size))
    fid={f:i for i,f in enumerate(sorted(faces,key=lambda x:(len(x),x)))}
    out=set()
    for tet in tets:
        for perm in itertools.permutations(tet):
            prefix=[]; chain=[]
            for vertex in perm:
                prefix.append(vertex); chain.append(fid[tuple(sorted(prefix))])
            out.add(tuple(sorted(chain)))
    return sorted(out)


def connected_graph(vertices,edges):
    vertices=set(vertices)
    if not vertices:return False
    adj={v:set() for v in vertices}
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    root=next(iter(vertices));seen={root};q=deque([root])
    while q:
        u=q.popleft()
        for w in adj[u]:
            if w not in seen:seen.add(w);q.append(w)
    return len(seen)==len(vertices)


def incidence_maps(tets):
    vs=defaultdict(list);es=defaultdict(list);fs=defaultdict(list)
    for tet in tets:
        for v in tet:vs[v].append(tet)
        for e in itertools.combinations(tet,2):es[tuple(sorted(e))].append(tet)
        for f in itertools.combinations(tet,3):fs[tuple(sorted(f))].append(tet)
    return vs,es,fs


def s2_test(tris):
    verts={x for tri in tris for x in tri};cnt=defaultdict(int)
    for tri in tris:
        for e in itertools.combinations(tri,2):cnt[tuple(sorted(e))]+=1
    edges=set(cnt);closed=bool(edges) and all(n==2 for n in cnt.values())
    chi=len(verts)-len(edges)+len(tris)
    return connected_graph(verts,edges) and closed and chi==2,(len(verts),len(edges),len(tris),chi)


def s1_test(edges):
    verts={x for e in edges for x in e};deg=defaultdict(int)
    for a,b in edges:deg[a]+=1;deg[b]+=1
    return connected_graph(verts,edges) and bool(verts) and all(deg[v]==2 for v in verts)


def orientable(tets):
    occ=defaultdict(list)
    for ti,tet in enumerate(tets):
        tet=tuple(sorted(tet))
        for i in range(4):occ[tet[:i]+tet[i+1:]].append((ti,i))
    if any(len(x)!=2 for x in occ.values()):return False
    adj=defaultdict(list)
    for x in occ.values():
        (a,ia),(b,ib)=x;ratio=-((-1)**ia)*((-1)**ib)
        adj[a].append((b,ratio));adj[b].append((a,ratio))
    sign={}
    for root in range(len(tets)):
        if root in sign:continue
        sign[root]=1;q=deque([root])
        while q:
            u=q.popleft()
            for v,r in adj[u]:
                want=r*sign[u]
                if v in sign and sign[v]!=want:return False
                if v not in sign:sign[v]=want;q.append(v)
    return True


def chain_squared_zero(tets):
    simplices={2:faces_of_tets(tets,2),3:set(tuple(sorted(t)) for t in tets)}
    for dim in (2,3):
        for simplex in simplices[dim]:
            acc=defaultdict(int)
            for i in range(dim+1):
                face=simplex[:i]+simplex[i+1:];c1=(-1)**i
                for j in range(dim):
                    sub=face[:j]+face[j+1:];acc[sub]+=c1*((-1)**j)
            if any(v!=0 for v in acc.values()):return False
    return True


def gf2_rank(columns):
    piv={};rank=0
    for col in columns:
        x=col
        while x:
            p=x.bit_length()-1
            if p in piv:x^=piv[p]
            else:piv[p]=x;rank+=1;break
    return rank


def betti_f2(tets):
    S={0:sorted(faces_of_tets(tets,0)),1:sorted(faces_of_tets(tets,1)),
       2:sorted(faces_of_tets(tets,2)),3:sorted(set(tuple(sorted(t)) for t in tets))}
    idx={d:{s:i for i,s in enumerate(S[d])} for d in S};r={}
    for d in (1,2,3):
        cols=[]
        for simplex in S[d]:
            bits=0
            for face in itertools.combinations(simplex,d):bits^=1<<idx[d-1][tuple(sorted(face))]
            cols.append(bits)
        r[d]=gf2_rank(cols)
    return [len(S[d])-r.get(d,0)-r.get(d+1,0) for d in range(4)]


def shell_stats():
    tris=q2_shell();ok,st=s2_test(tris);eq={(2,3),(3,4),(4,5),(2,5)}
    return {"q":2,"route_states":4,"shell_f_vector":list(st[:3]),"shell_chi":st[3],
            "shell_is_S2":ok,"equator_is_C4_S1":s1_test(eq)}


def complex_stats(tets,g):
    vs,es,fs=incidence_maps(tets);badv=bade=badf=0
    for v,star in vs.items():
        tris={tuple(sorted(x for x in t if x!=v)) for t in star};badv+=0 if s2_test(tris)[0] else 1
    for e,star in es.items():
        se=set(e);le={tuple(sorted(x for x in t if x not in se)) for t in star};bade+=0 if s1_test(le) else 1
    for f,star in fs.items():badf+=0 if len(star)==2 else 1
    return {"generation":g,"V":len(vs),"E":len(es),"F":len(fs),"T":len(tets),
            "euler_characteristic":len(vs)-len(es)+len(fs)-len(tets),
            "all_triangles_two_sided":all(len(x)==2 for x in fs.values()),
            "bad_vertex_links":badv,"bad_edge_links":bade,"bad_face_links":badf,
            "orientable":orientable(tets),"boundary_squared_zero":chain_squared_zero(tets)}


def run(refinements=2):
    shell=shell_stats();tets=cross_polytope_boundary_4();seed_betti=betti_f2(tets);rows=[]
    for g in range(refinements+1):
        rows.append(complex_stats(tets,g))
        if g<refinements:tets=barycentric_subdivision(tets)
    passed=(shell["shell_is_S2"] and shell["equator_is_C4_S1"] and seed_betti==[1,0,0,1]
            and all(r["all_triangles_two_sided"] and r["bad_vertex_links"]==0
                    and r["bad_edge_links"]==0 and r["bad_face_links"]==0
                    and r["orientable"] and r["boundary_squared_zero"]
                    and r["euler_characteristic"]==0 for r in rows))
    return {"status":"canonical q=2 PL-globalization gate","passed":bool(passed),
            "frozen_rule":"q=2 binary routes; Q2=C4; local shell Sigma(C4)",
            "local_shell":shell,"global_completion":"boundary of the 4D cross-polytope (16-cell)",
            "seed_betti_F2":seed_betti,"recursive_operation":"global barycentric subdivision",
            "generations":rows,
            "theorem_level":"The chosen q=2 cross-polytope completion is S3 and barycentric refinement preserves its PL 3-manifold class.",
            "scope_note":"Existence and recursive stability of a natural q=2 global PL completion are closed. Uniqueness/dynamical selection of this gluing from the bare causal rewrite is not proved."}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--refinements",type=int,default=2);ap.add_argument("--output",type=Path);a=ap.parse_args()
    out=run(a.refinements);txt=json.dumps(out,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+"\n",encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__=="__main__":raise SystemExit(main())
