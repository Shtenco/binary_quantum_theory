#!/usr/bin/env python3
"""Audit the combinatorial normalization of H_sine against the canonical tetrahedral formula.

The reference epsilon^{ijk} sum has six permutations. Pairing each permutation
with i<->j gives three cyclic forward-minus-reverse loop contributions. The
repository's oriented_specs emits three cyclic specs per omitted face and its
T_sequences already contains pf-pr.

For the reference coefficient -2/(3 i hbar), symmetric completion of O gives

  Herm[c_E O] = c_E (O-O^dagger)/2

while the repository defines

  H_sine_raw=(O-O^dagger)/(2i).

Therefore n_E = c_E*i = -2/(3 hbar). Combined with the nested K-K-V
normalization, |g_R|=8 n_E^2/hbar^5=32/(9 hbar^7).
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

C_L=1.3389293521464034
GLOBAL_RAW_SPLIT=42.84573926868491


def parity(p):
    inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
    return -1 if inv%2 else 1


def run(hbar=1.0):
    perms=list(itertools.permutations((0,1,2)))
    pos=[p for p in perms if parity(p)==1]
    neg=[p for p in perms if parity(p)==-1]
    cyclic=[(0,1,2),(1,2,0),(2,0,1)]
    reverse=[(1,0,2),(2,1,0),(0,2,1)]

    pairs=[]
    for f,r in zip(cyclic,reverse):
        pairs.append({"forward":list(f),"reverse":list(r),"forward_sign":parity(f),"reverse_sign":parity(r)})

    cE=-2.0/(3.0j*hbar)
    nE=cE*1j
    gR_abs=8.0*(abs(nE)**2)/(hbar**5)
    local= gR_abs*C_L
    global_split=gR_abs*GLOBAL_RAW_SPLIT

    checks={
        "six_epsilon_permutations":len(perms)==6,
        "three_positive":len(pos)==3,
        "three_negative":len(neg)==3,
        "positive_are_cyclic":set(pos)==set(cyclic),
        "negative_are_reverse":set(neg)==set(reverse),
        "each_pair_has_opposite_sign":all(x["forward_sign"]==1 and x["reverse_sign"]==-1 for x in pairs),
        "nE_is_real":abs(nE.imag)<1e-15,
        "nE_matches_minus_2_over_3hbar":abs(nE.real+2.0/(3.0*hbar))<1e-15,
        "gR_matches_32_over_9_hbar7":abs(gR_abs-32.0/(9.0*hbar**7))<1e-14,
        "local_normalized_value":abs(local-(32.0/9.0)*C_L/(hbar**7))<1e-12,
        "global_normalized_value":abs(global_split-(32.0/9.0)*GLOBAL_RAW_SPLIT/(hbar**7))<1e-11,
    }
    return {
        "status":"conditional Euclidean sine normalization match",
        "passed":all(checks.values()),
        "hbar":hbar,
        "epsilon_permutations":{"positive":[list(x) for x in pos],"negative":[list(x) for x in neg],"paired":pairs},
        "repository_combinatorics_assumption":"oriented_specs gives the three cyclic specs and T_sequences contains forward-minus-reverse pf-pr",
        "canonical_unsym_euclidean_coefficient":"-2/(3 i hbar)",
        "repo_sine_definition":"(O-O^dagger)/(2i)",
        "n_E":nE.real,
        "n_E_identity":"-2/(3 hbar)",
        "abs_g_R":gR_abs,
        "abs_g_R_identity":"32/(9 hbar^7)",
        "frozen_local_phase_completed_raw_cL":C_L,
        "normalized_local_onebody_magnitude":local,
        "frozen_global_raw_pair_split":GLOBAL_RAW_SPLIT,
        "normalized_global_pair_split_magnitude":global_split,
        "checks":checks,
        "scope":(
            "Combinatorial/coefficient match in the original tetrahedral fundamental-trace convention. "
            "The result is a dimensionless canonical normalization relation, not an absolute energy scale. "
            "If auxiliary trace or path normalization conventions change, rerun this gate."
        ),
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--hbar',type=float,default=1.0)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args(); out=run(args.hbar); text=json.dumps(out,indent=2,sort_keys=True); print(text)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
