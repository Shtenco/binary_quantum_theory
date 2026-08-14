#!/usr/bin/env python3
"""Recursive PL mirror-order persistence gate.

The seed 16-cell has a bipartite Q4 dual tetrahedron graph. This gate asks
whether the staggered orientation order survives the actual recursive PL branch
used by the canonical manifold gate.

For generations g=0..2 it builds the same global barycentric subdivisions,
constructs the tetrahedron dual graph (one node per tetrahedron, one edge per
shared triangular face), and checks:
- every tetrahedron has four dual neighbours;
- the dual graph is connected and bipartite;
- a two-colour eta_v exists with eta_v eta_w=-1 on every dual edge;
- the staggered variable sigma_v=eta_v Y_v converts the geometric preference
  Y_v Y_w=-1 into uniform sigma_v sigma_w=+1;
- the two global Sigma=+/-1 mirror vacua are exact on every checked generation.

It also records low combinatorial Laplacian eigenvalues as a diagnostic for the
future continuum-normalization calculation. Those eigenvalues are NOT turned
into a physical Z_sigma because no physical dual-edge length is assigned here.
"""
from __future__ import annotations

import argparse
import itertools
import json
from collections import defaultdict, deque
from pathlib import Path

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh

import sys
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from bcqg_global_manifold_gate import cross_polytope_boundary_4, barycentric_subdivision


def dual_edges(tets):
    faces = defaultdict(list)
    for ti, tet in enumerate(tets):
        for f in itertools.combinations(tet, 3):
            faces[tuple(sorted(f))].append(ti)
    if any(len(v) != 2 for v in faces.values()):
        raise RuntimeError("non-closed triangular face incidence")
    return sorted(tuple(v) for v in faces.values())


def bipartite_coloring(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b); adj[b].append(a)
    eta = [0] * n
    components = 0
    for root in range(n):
        if eta[root]:
            continue
        components += 1
        eta[root] = 1
        q = deque([root])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not eta[v]:
                    eta[v] = -eta[u]; q.append(v)
                elif eta[v] == eta[u]:
                    return False, eta, adj, components
    return True, eta, adj, components


def low_laplacian(n, edges, k=6):
    deg = np.zeros(n, dtype=float)
    row=[]; col=[]; data=[]
    for a,b in edges:
        deg[a]+=1; deg[b]+=1
        row.extend((a,b)); col.extend((b,a)); data.extend((-1.0,-1.0))
    row.extend(range(n)); col.extend(range(n)); data.extend(deg.tolist())
    L=coo_matrix((data,(row,col)),shape=(n,n)).tocsr()
    vals=eigsh(L,k=min(k,n-1),which="SM",return_eigenvectors=False,tol=1e-9,maxiter=5000)
    vals=np.sort(vals)
    vals[np.abs(vals)<1e-12]=0.0
    return [float(x) for x in vals]


def generation_row(tets, g):
    edges=dual_edges(tets)
    ok, eta, adj, comps=bipartite_coloring(len(tets), edges)
    degrees=[len(x) for x in adj]
    edge_products=[eta[a]*eta[b] for a,b in edges]
    vacua=[]
    if ok:
        for chi in (+1,-1):
            Y=[chi*x for x in eta]
            Sigma=sum(eta[i]*Y[i] for i in range(len(Y)))/len(Y)
            bad=sum(Y[a]*Y[b] != -1 for a,b in edges)
            vacua.append({"chi":chi,"Sigma":float(Sigma),"bad_gluing_edges":int(bad)})
    vals=low_laplacian(len(tets),edges)
    return {
        "generation":g,
        "tetrahedra":len(tets),
        "dual_edges":len(edges),
        "connected_components":comps,
        "degree_min":min(degrees),
        "degree_max":max(degrees),
        "all_degree_four":all(d==4 for d in degrees),
        "bipartite":bool(ok),
        "all_eta_edge_products_minus_one":bool(ok and all(x==-1 for x in edge_products)),
        "mirror_vacua":vacua,
        "laplacian_low_eigenvalues":vals,
        "lambda2_combinatorial":vals[1],
    }


def run(refinements=2):
    tets=cross_polytope_boundary_4()
    rows=[]
    for g in range(refinements+1):
        rows.append(generation_row(tets,g))
        if g<refinements:
            tets=barycentric_subdivision(tets)
    passed=all(
        r["connected_components"]==1
        and r["all_degree_four"]
        and r["bipartite"]
        and r["all_eta_edge_products_minus_one"]
        and len(r["mirror_vacua"])==2
        and abs(r["mirror_vacua"][0]["Sigma"]-1.0)<1e-15
        and abs(r["mirror_vacua"][1]["Sigma"]+1.0)<1e-15
        and r["mirror_vacua"][0]["bad_gluing_edges"]==0
        and r["mirror_vacua"][1]["bad_gluing_edges"]==0
        for r in rows
    )
    return {
        "status":"recursive PL staggered mirror-order persistence gate",
        "passed":bool(passed),
        "recursive_operation":"same global barycentric subdivision as bcqg_global_manifold_gate.py",
        "generations":rows,
        "order_parameter":"Sigma_g=(1/T_g) sum_t eta_t Y_t",
        "result":"The staggered Z2 mirror-order label survives the checked recursive PL S3 generations.",
        "normalization_note":(
            "The recorded combinatorial Laplacian spectrum constrains dimensionless long-wave stiffness, "
            "but a physical Z_sigma still requires a physical edge/volume scale and the kinetic/time normalization."
        )
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--refinements",type=int,default=2)
    ap.add_argument("--output",type=Path)
    a=ap.parse_args()
    out=run(a.refinements)
    text=json.dumps(out,indent=2)
    print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(text+"\n",encoding="utf-8")
    return 0 if out["passed"] else 1

if __name__=="__main__":
    raise SystemExit(main())
