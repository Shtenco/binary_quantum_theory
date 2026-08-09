#!/usr/bin/env python3
"""Combinatorial size of the regulator-safe K5 HH reachable spin-network basis.

Start from the fully-active K5 boundary with spin j=1/2 on every link.  A
fundamental Peter-Weyl holonomy changes twice-spin s=2j by +/-1.  The local
Hamiltonian word used in k5_thiemann_constraint_gate.py touches three triangle
links once and the radial link twice.  This script enumerates all final spin
labels after one H and after either ordering of a pair H_v H_w, filters them by
four-valent SU(2) Gauss admissibility at every node, and sums the exact local
intertwiner multiplicities.

It is an upper bound on the actually nonzero matrix support because amplitude
cancellations are ignored, but it is exact at the representation-selection
level and determines the minimum Peter-Weyl wall needed by HH histories.
"""
from __future__ import annotations
import argparse,itertools,json
from pathlib import Path

V=range(5);EDGES=list(itertools.combinations(V,2));EI={e:i for i,e in enumerate(EDGES)}

def specs(v):
    neigh=sorted(w for w in V if w!=v);out=[]
    for tri in itertools.combinations(neigh,3):
        a,b,c=tri;out.extend([(v,a,b,c),(v,b,c,a),(v,c,a,b)])
    return out

def mult4(ss):
    s1,s2,s3,s4=ss
    return len(set(range(abs(s1-s2),s1+s2+1,2)) & set(range(abs(s3-s4),s3+s4+1,2)))

def gauss_mult(spins):
    m=1
    for v in V:
        ss=[spins[EI[tuple(sorted((v,w)))]] for w in V if w!=v]
        m*=mult4(ss)
    return m

def hit_states(spins,spec):
    v,a,b,c=spec
    tri=[EI[tuple(sorted((v,a)))],EI[tuple(sorted((a,b)))],EI[tuple(sorted((b,v)))]]
    radial=EI[tuple(sorted((v,c)))]
    states={tuple(spins)}
    for e in [radial,radial]+tri:
        nxt=set()
        for st in states:
            vals=[]
            if st[e]>0:vals.append(st[e]-1)
            vals.append(st[e]+1)
            for x in vals:
                q=list(st);q[e]=x;nxt.add(tuple(q))
        states=nxt
    return states

def apply_H(spinset,v):
    out=set()
    for s in spinset:
        for sp in specs(v):out |= hit_states(s,sp)
    return out

def summarize(sset):
    valid=[s for s in sset if gauss_mult(s)>0]
    return {'raw_spin_assignments':len(sset),'Gauss_admissible_spin_assignments':len(valid),'spin_network_basis_dimension_upper_bound':sum(gauss_mult(s) for s in valid),'max_spin_reached':max(max(s) for s in valid)/2 if valid else 0.0},set(valid)

def run():
    start={(1,)*10};one={};valid1={}
    for v in V:
        summary,vs=summarize(apply_H(start,v));one[str(v)]=summary;valid1[v]=vs
    pairs={}
    for v,w in itertools.combinations(V,2):
        both=apply_H(valid1[v],w)|apply_H(valid1[w],v)
        summary,_=summarize(both);pairs[f'{v}-{w}']=summary
    ref1=next(iter(one.values()));ref2=next(iter(pairs.values()))
    symmetric=all(x==ref1 for x in one.values()) and all(x==ref2 for x in pairs.values())
    passed=(symmetric and ref1['Gauss_admissible_spin_assignments']==120 and ref1['spin_network_basis_dimension_upper_bound']==816 and ref2['Gauss_admissible_spin_assignments']==4193 and ref2['spin_network_basis_dimension_upper_bound']==24364 and abs(ref2['max_spin_reached']-2.5)<1e-12)
    return {'status':'K5 Peter-Weyl HH reachable-basis combinatorics','passed':bool(passed),'initial_spin':'j=1/2 on all ten K5 links','one_H':one,'two_H_pair_union':pairs,'universal_one_H_summary':ref1,'universal_HH_summary':ref2,'cutoff_statement':'The HH reachable set actually reaches j=5/2, so Jmax=5/2 is both sufficient by the per-link four-hit wall and saturated by allowed histories.','scope_note':'Representation-selection and Gauss multiplicity count only; actual Hamiltonian amplitudes may cancel and reduce the support further.'}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);a=ap.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
