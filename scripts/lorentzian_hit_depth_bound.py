#!/usr/bin/env python3
"""Conservative per-link Peter-Weyl cutoff bound for a Thiemann-type K5 Hamiltonian.

Only operator support/hit counts are studied here, not amplitudes.  The local
Euclidean term is represented by a triangular plaquette plus h_c[h_c^-1,V].
The Lorentzian term is represented schematically by

    C_i(K) C_j(K) C_k(V),
    C_e(X)=h_e [h_e^-1, X],
    K ~ [V,H_E].

The script enumerates all local K5 choices and asks for the largest number of
fundamental-holonomy hits that can accumulate on one physical link.  This gives
a sufficient Peter-Weyl Jmax for a cutoff-exact HH calculation.  It is not a
claim that the dynamically reached spin saturates the bound.
"""
from __future__ import annotations
import itertools,json
from collections import Counter

VERTICES=tuple(range(5))
EDGES=tuple(itertools.combinations(VERTICES,2))

def edge(a:int,b:int)->tuple[int,int]:
    return tuple(sorted((a,b)))

def add(*profiles:Counter)->Counter:
    out=Counter()
    for p in profiles: out.update(p)
    return out

def euclidean_profiles(v:int):
    neigh=[x for x in VERTICES if x!=v]
    out=[]
    for a,b,c in itertools.permutations(neigh,3):
        # alpha_ab = (v,a)(a,b)(b,v), while C_c(V) contributes
        # h_c and h_c^-1 on the radial link (v,c).
        p=Counter()
        p[edge(v,a)]+=1
        p[edge(a,b)]+=1
        p[edge(v,b)]+=1
        p[edge(v,c)]+=2
        out.append(((a,b,c),p))
    return out

def lorentzian_profiles(v:int):
    neigh=[x for x in VERTICES if x!=v]
    he=euclidean_profiles(v)
    out=[]
    # K~[V,H_E] has the same holonomy-hit support as an H_E term.
    # C_i(K)=h_i[h_i^-1,K] adds two explicit hits on radial link i.
    for i,j,k in itertools.permutations(neigh,3):
        for s1,p1 in he:
            c1=add(p1,Counter({edge(v,i):2}))
            for s2,p2 in he:
                c2=add(p2,Counter({edge(v,j):2}))
                cv=Counter({edge(v,k):2})
                out.append(((i,j,k,s1,s2),add(c1,c2,cv)))
    return out

def max_by_edge(profiles):
    return {e:max(p.get(e,0) for _,p in profiles) for e in EDGES}

def run():
    he={v:euclidean_profiles(v) for v in VERTICES}
    hl={v:lorentzian_profiles(v) for v in VERTICES}
    he_node={v:max_by_edge(he[v]) for v in VERTICES}
    hl_node={v:max_by_edge(hl[v]) for v in VERTICES}

    max_he=max(max(x.values()) for x in he_node.values())
    max_hl=max(max(x.values()) for x in hl_node.values())

    # For an HH bracket use distinct node Hamiltonians.  The two terms are
    # chosen independently, so the maximal hit number on an edge is the sum of
    # the two per-node maxima.  On their shared edge 6+6 is actually attained.
    hh_rows=[]
    max_hh=0
    witness=None
    for v,w in itertools.combinations(VERTICES,2):
        for e in EDGES:
            hits=hl_node[v][e]+hl_node[w][e]
            hh_rows.append({"nodes":[v,w],"edge":list(e),"max_hits":hits})
            if hits>max_hh:
                max_hh=hits;witness=(v,w,e)

    j_in=0.5
    safe_jmax=j_in+max_hh/2
    # dim direct_sum_{j=0,1/2,...,Jmax} (2j+1)^2
    nmax=int(round(2*safe_jmax))+1
    link_dimension=sum(n*n for n in range(1,nmax+1))

    result={
      "status":"conservative per-link Lorentzian Peter-Weyl wall",
      "max_hits_per_link_HE":max_he,
      "max_hits_per_link_HL":max_hl,
      "max_hits_per_link_HH":max_hh,
      "HH_witness":{"nodes":list(witness[:2]),"shared_edge":list(witness[2])},
      "input_spin":j_in,
      "sufficient_Jmax_for_full_Lorentzian_HH":safe_jmax,
      "single_link_dimension_at_that_cutoff":link_dimension,
      "node_Lorentzian_maxima":{str(v):{str(e):n for e,n in hl_node[v].items()} for v in VERTICES},
      "scope_note":(
        "Support-count bound for the stated nested-commutator regularization. "
        "It is sufficient, not necessarily minimal: actual amplitudes may cancel "
        "or populate a lower maximum spin. The reached-spin wall must be measured "
        "in the final Lorentzian calculation."
      )
    }
    result["passed"]=(max_he==2 and max_hl==6 and max_hh==12 and safe_jmax==6.5 and link_dimension==1015)
    return result

if __name__=='__main__':
    out=run();print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
