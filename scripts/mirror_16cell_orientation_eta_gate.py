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

Consequently a local epsilon/sign-covariant one-cell term ell*Y_v assembles on
the globally labelled 16-cell as

    ell sum_v eta_v Y_v = 16 ell Sigma.

For the two exact classical mirror vacua Y_v=chi eta_v, chi=+/-1, the unit-ell
energies are +/-16 and the splitting is exactly 32|ell|.  On N cells the same
algebra gives 2N|ell|.  This is a conditional operator consequence; the gate
does not assert the Lorentzian coefficient ell is nonzero.
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
    eta_vec=np.array([r['eta'] for r in rows],dtype=int)
    orient_vec=np.array([r['facet_orientation_det_sign'] for r in rows],dtype=int)

    vacua={}
    for chi in (+1,-1):
        Y=chi*eta_vec
        Sigma=float(np.mean(eta_vec*Y))
        unit_ell_energy=float(np.sum(orient_vec*Y))
        vacua[str(chi)]={
            'Sigma':Sigma,
            'Y_vector':Y.tolist(),
            'unit_ell_orientation_field_energy':unit_ell_energy,
        }
    unit_split=abs(vacua['1']['unit_ell_orientation_field_energy']-vacua['-1']['unit_ell_orientation_field_energy'])

    passed=(
        len(rows)==16 and all_match and dual_ok
        and np.array_equal(eta_vec,orient_vec)
        and vacua['1']['Sigma']==1.0 and vacua['-1']['Sigma']==-1.0
        and abs(unit_split-32.0)<1e-12
    )
    return {
        'status':'exact 16-cell orientation-sign / staggered-eta gate',
        'passed':bool(passed),
        'facet_count':len(rows),
        'eta_vector':eta_vec.tolist(),
        'orientation_sign_vector':orient_vec.tolist(),
        'all_orientation_signs_equal_eta':bool(all_match),
        'every_Q4_edge_flips_both_signs':bool(dual_ok),
        'identity':'sgn det[v0 v1 v2 v3]=(-1)^popcount(b)=eta_b',
        'mirror_vacua_under_unit_orientation_field':vacua,
        'unit_ell_mirror_pair_energy_splitting':float(unit_split),
        'general_N_splitting':'Delta E = 2 N |ell| for Y_v=chi eta_v under ell sum_v eta_v Y_v',
        'global_sign_note':'Reversing the global orientation multiplies every facet sign and every assembled epsilon coefficient by the same overall -1; the staggered pattern is unchanged up to that global convention.',
        'conditional_lorentzian_consequence':'If a nonzero local epsilon/sign-covariant logical amplitude has coefficient ell_L times Y in the positively oriented local frame, its 16-cell assembly is ell_L sum_v eta_v Y_v = 16 ell_L Sigma. On a fixed global orientation it is a longitudinal staggered field and splits the two ideal mirror vacua by 32|ell_L|, rather than acting as a mediator mass term.',
        'survival_condition':'For an exact spontaneous two-vacuum mirror branch on a fixed global orientation, the renormalized one-cell coefficient must vanish in the symmetry-restored/full operator limit (or an additional mechanism must identify global orientation reversal as gauge-equivalent).',
        'scope':'Exact finite simplicial orientation and classical-vacuum response statement. It does not prove ell_L is nonzero, does not fix the physical Lorentzian prefactor, and does not establish a mirror force.',
        'facets':rows,
    }

if __name__=='__main__':
    out=run(); print(json.dumps(out,indent=2)); raise SystemExit(0 if out['passed'] else 1)
