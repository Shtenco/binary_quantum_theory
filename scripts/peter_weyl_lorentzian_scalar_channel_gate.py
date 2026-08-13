#!/usr/bin/env python3
"""Exact SU(2) scalar-channel gate for the Lorentzian two-K one-V triple.

Every fundamental 2x2 covariant leg transforms as 1/2 x 1/2* = 0 + 1.
Starting from a Gauss scalar and requiring the traced triple to end in J=0,
this script enumerates every allowed rank/intermediate-J path in

    (0 + 1) tensor (0 + 1) tensor (0 + 1).

The result is exact representation theory, not a numerical truncation.  Only
five scalar paths exist:

    000, 011, 101, 110, 111.

In particular no scalar-relevant intermediate state after the second leg has
J=2.  A future H_L implementation may therefore discard J=2 at that stage by
an exact selection rule, while still keeping the full link-spin cutoff required
by holonomy support.
"""
from __future__ import annotations
import json


def coupled(J, k):
    return tuple(range(abs(J-k), J+k+1))


def enumerate_scalar_paths():
    rows=[]
    for k1 in (0,1):
        for J1 in coupled(0,k1):
            for k2 in (0,1):
                for J2 in coupled(J1,k2):
                    for k3 in (0,1):
                        if 0 in coupled(J2,k3):
                            rows.append({
                                'ranks':[k1,k2,k3],
                                'intermediate_J':[J1,J2],
                                'final_J':0,
                            })
    return rows


def multiplicities_after_three_legs():
    dist={0:1}
    for _ in range(3):
        nxt={}
        for J,mult in dist.items():
            for k in (0,1):
                for Jo in coupled(J,k):
                    nxt[Jo]=nxt.get(Jo,0)+mult
        dist=nxt
    return dist


def link_dimension(Jmax):
    nmax=int(round(2*Jmax))+1
    return sum(n*n for n in range(1,nmax+1))


def run():
    rows=enumerate_scalar_paths()
    rank_words=[''.join(str(x) for x in r['ranks']) for r in rows]
    mult=multiplicities_after_three_legs()
    scalar_intermediate_J=sorted({J for r in rows for J in r['intermediate_J']})
    second_leg_J=sorted({r['intermediate_J'][1] for r in rows})

    # From the separately preregistered hit-depth calculation:
    # HE=2, HL=6 hits/link.  These are support consequences only.
    HE_hits=2; HL_hits=6; input_j=0.5
    walls={
        'single_HL': input_j + HL_hits/2,
        'mixed_HE_HL_commutator': input_j + (HE_hits+HL_hits)/2,
        'HL_HL_commutator': input_j + (2*HL_hits)/2,
    }
    dims={name:link_dimension(J) for name,J in walls.items()}

    passed=(
        rank_words == ['000','011','101','110','111']
        and mult.get(0)==5
        and second_leg_J == [0,1]
        and 2 not in second_leg_J
        and walls == {
            'single_HL':3.5,
            'mixed_HE_HL_commutator':4.5,
            'HL_HL_commutator':6.5,
        }
        and dims == {
            'single_HL':204,
            'mixed_HE_HL_commutator':385,
            'HL_HL_commutator':1015,
        }
    )
    return {
        'status':'exact scalar-channel preregistration for traced Lorentzian triple',
        'passed':bool(passed),
        'scalar_paths':rows,
        'rank_words':rank_words,
        'three_leg_total_J_multiplicities':{str(k):v for k,v in sorted(mult.items())},
        'scalar_multiplicity':mult.get(0,0),
        'all_scalar_relevant_intermediate_J':scalar_intermediate_J,
        'scalar_relevant_J_after_second_leg':second_leg_J,
        'exact_pruning_rule':'For a final J=0 triple, discard second-leg J=2 exactly; ranks 0 or 1 in the last leg cannot couple J=2 to J=0.',
        'support_hit_counts':{'HE':HE_hits,'HL':HL_hits},
        'cutoff_walls_Jmax':walls,
        'single_link_dimensions':dims,
        'next_use':'Implement H_L in irreducible rank channels 000,011,101,110,111; validate single H_L at Jmax=7/2 before mixed and HL-HL brackets.',
        'scope_note':'Pure SU(2) selection-rule and support-cost gate; no H_L amplitudes are claimed here.'
    }

if __name__=='__main__':
    out=run(); print(json.dumps(out,indent=2)); raise SystemExit(0 if out['passed'] else 1)
