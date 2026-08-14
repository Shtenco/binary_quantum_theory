#!/usr/bin/env python3
"""Exact 16-cell facet-orientation sign versus mirror staggered eta.

The boundary facets of the four-dimensional cross-polytope are indexed by a
four-bit word b.  Facet b contains one vertex from each antipodal pair,
represented geometrically as

    v_a = (-1)^{b_a} e_a,  a=0,1,2,3.

With the natural ordered basis (v_0,v_1,v_2,v_3), the induced boundary
orientation sign relative to a fixed ambient R4 orientation is the sign of

    det[v_0 v_1 v_2 v_3]
      = product_a (-1)^{b_a}
      = (-1)^popcount(b).

But the microscopic mirror-order construction independently uses

    eta_b=(-1)^popcount(b)

to bipartition the Q4 dual graph.  Thus the simplicial orientation sign and the
staggered mirror eta agree exactly, up to the one global convention that flips
all facet orientations simultaneously.

Consequence: if an epsilon/sign-covariant one-cell logical term is ell*Y_v in a
locally positively oriented frame, then on the globally labelled 16-cell its
assembled pattern is ell*eta_v*Y_v, hence N*ell*Sigma.  This is a conditional
operator consequence; the gate does not assert ell is nonzero.
"""
from __future__ import annotations

import itertools
import json
import numpy as np


def eta(bits):
    return -1 if sum(bits) % 2 else +1


def facet_matrix(bits):
    M=np.zeros((4,4),dtype=int)
    for a,b in enumerate(bits):
        M[a,a]=-1 if b else +1
    return M


def run():
    rows=[]
    all_match=True
    dual_ok=True
    for bits in itertools.product((0,1),repeat=4):
        label=sum(bits[a]<<a for a in range(4))
        det=int(round(np.linalg.det(facet_matrix(bits))))
        e=eta(bits)
        all_match &= (det==e)
        # each one-bit flip is a dual Q4 neighbor and must reverse orientation
        neigh=[]
        for a in range(4):
            bb=list(bits); bb[a]^=1; bb=tuple(bb)
            d2=int(round(np.linalg.det(facet_matrix(bb))))
            dual_ok &= (d2==-det and eta(bb)==-e)
            neigh.append(sum(bb[k]<<k for k in range(4)))
        rows.append({
            'label':label,
            'bits':list(bits),
            'popcount':sum(bits),
            'eta':e,
            'facet_orientation_det_sign':det,
            'matches_eta':det==e,
            'Q4_neighbors':sorted(neigh),
        })
    rows.sort(key=lambda r:r['label'])
    eta_vec=[r['eta'] for r in rows]
    orient_vec=[r['facet_orientation_det_sign'] for r in rows]
    passed=(len(rows)==16 and all_match and dual_ok and eta_vec==orient_vec)
    return {
        'status':'exact 16-cell orientation-sign / staggered-eta gate',
        'passed':bool(passed),
        'facet_count':len(rows),
        'eta_vector':eta_vec,
        'orientation_sign_vector':orient_vec,
        'all_orientation_signs_equal_eta':bool(all_match),
        'every_Q4_edge_flips_both_signs':bool(dual_ok),
        'identity':'sgn det[v0 v1 v2 v3]=(-1)^popcount(b)=eta_b',
        'global_sign_note':'Reversing the global orientation multiplies every facet sign and every assembled epsilon coefficient by the same overall -1; the staggered pattern is unchanged up to that global convention.',
        'conditional_lorentzian_consequence':'If a nonzero local epsilon/sign-covariant logical amplitude has coefficient ell_L times Y in the positively oriented local frame, its 16-cell assembly is ell_L sum_v eta_v Y_v = 16 ell_L Sigma. It is then a longitudinal staggered field for the mirror order, not a mediator mass term.',
        'scope':'Exact finite simplicial orientation statement. It does not prove ell_L is nonzero, does not fix the physical Lorentzian prefactor, and does not establish a mirror force.',
        'facets':rows,
    }

if __name__=='__main__':
    out=run(); print(json.dumps(out,indent=2)); raise SystemExit(0 if out['passed'] else 1)
