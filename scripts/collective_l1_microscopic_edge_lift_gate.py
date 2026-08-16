#!/usr/bin/env python3
"""Construct the canonical six-column microscopic lift of the L1 edge carrier.

The strict-interior q=4 source columns c_p are labelled by the 24 barycentric
chambers p in S4.  The coarse-boundary theorem groups four parity-related
chambers by the unordered pair e={p0,p1}, one of the six coarse tetrahedral
edges.

Define the target-independent microscopic edge lift

    chi_e = 1/2 sum_{p: {p0,p1}=e} sgn(p) c_p.

The factor 1/2 makes the six coset coefficient columns Euclidean-normalized in
chamber space.  This gate evaluates their actual Peter-Weyl Hilbert Gram before
any internal-link contraction.  A common norm times I6 gives a canonical
microscopic isometry W_g after one overall normalization.

No coarse-boundary inner product is substituted for the microscopic Hilbert
inner product.  This is the six-column W used by later operator compression.
"""
from __future__ import annotations
import argparse,itertools,json,math,sys
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
import collective_l1_strict_interior_boundary_rank_gate as BG


def parity(p):
    inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
    return -1 if inv%2 else 1


def run():
    D,G,nodes,inside,internal_edges,internal_eidx,cols,worker_rows,slot_checks=BG.build_strict_columns()
    states=sorted(set().union(*(set(c) for c in cols)),key=repr);si={s:i for i,s in enumerate(states)}
    C=np.zeros((len(states),24),complex)
    for j,c in enumerate(cols):
        for st,a in c.items():C[si[st],j]=a

    perms=tuple(itertools.permutations(range(4)))
    edge_groups=[tuple(sorted(p[:2])) for p in perms];edges=sorted(set(edge_groups))
    Q=np.zeros((24,6),float)
    for i,(p,e) in enumerate(zip(perms,edge_groups)):
        Q[i,edges.index(e)]=parity(p)/2.0
    lifts=C@Q
    Gram=lifts.conj().T@lifts
    Gram=.5*(Gram+Gram.conj().T)
    nu=float(np.mean(np.diag(Gram).real))
    defect=float(np.linalg.norm(Gram-nu*np.eye(6))/max(np.linalg.norm(Gram),1e-300))
    W=lifts/math.sqrt(nu)
    iso=float(np.linalg.norm(W.conj().T@W-np.eye(6)))
    support=[int(np.sum(np.abs(W[:,i])>1e-12)) for i in range(6)]

    # Every microscopic basis state in the strict P4 columns differs from the
    # all-j=1/2 seed on exactly four internal edges, hence background overlap is
    # exactly zero in the orthonormal Gauss basis.
    background_orthogonal=all(any(s!=1 for s in st[0]) for st in states if any(abs(C[si[st],:])>1e-12))
    checks={
        'six_edge_cosets':len(edges)==6 and all(edge_groups.count(e)==4 for e in edges),
        'coset_coefficient_isometry':float(np.linalg.norm(Q.T@Q-np.eye(6)))<1e-14,
        'microscopic_edge_Gram_common_norm_I6':defect<1e-12,
        'common_norm_positive':nu>0,
        'normalized_W_isometry':iso<1e-12,
        'every_edge_lift_nonzero':all(x>0 for x in support),
        'microscopic_background_exactly_orthogonal':background_orthogonal,
    }
    return {
        'status':'canonical microscopic six-edge L1 metric-carrier isometry',
        'passed':bool(all(checks.values())),'checks':checks,
        'edge_order':[list(e) for e in edges],
        'chamber_coset_coefficient_rule':'Q[p,e]=sgn(p)/2 when sorted(p[:2])=e, else 0',
        'microscopic_unique_basis_states':len(states),
        'microscopic_edge_lift_common_norm_square':nu,
        'microscopic_edge_Gram_relative_I6_defect':defect,
        'normalized_isometry_defect':iso,
        'normalized_edge_lift_support_sizes':support,
        'W_definition':'W_g[:,e] = chi_e / sqrt(nu), chi_e = (1/2) sum_{p in edge coset e} sgn(p) c_p',
        'interpretation':'The six coarse-edge directions are represented by six mutually orthogonal equal-norm vectors already in the microscopic Peter-Weyl Hilbert space. Therefore later W_g^dagger C W_g compression can use the true microscopic inner product while the boundary contraction supplies the geometric identification of the same six channels.',
        'scope_note':'Strict-interior q4 metric carrier only. This W_g must be enlarged or leakage-tested against S, route and depth-two production actions before it can be called the complete collective effective space.'
    }


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();txt=json.dumps(o,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1

if __name__=='__main__':raise SystemExit(main())
