#!/usr/bin/env python3
"""Audit H_sine normalization against canonical tetrahedral combinatorics.

The reference epsilon^{ijk} sum has six permutations. Pairing i<->j produces
three cyclic forward-minus-reverse loop contributions. This gate verifies both
that algebra and the current production code:

- oriented_specs(v) contains four omitted-face blocks x three cyclic specs;
- T_sequences(v,a,b,c) contains the forward/reverse loop paths pf/pr with the
  required paired coefficients.

Then the canonical coefficient -2/(3 i hbar) and the repository definition
H_sine_raw=(O-O^dagger)/(2i) imply n_E=-2/(3 hbar). The nested K-K-V relation
gives |g_R|=32/(9 hbar^7).
"""
from __future__ import annotations

import argparse
import itertools
import json
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import k5_peter_weyl_safe_hda_column as PW

C_L=1.3389293521464034
GLOBAL_RAW_SPLIT=42.84573926868491


def parity(p):
    inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
    return -1 if inv%2 else 1


def inspect_production(v=0):
    neigh=PW.NEIG[v]
    specs=list(PW.oriented_specs(v))
    expected=[]
    blocks=[]
    for r in range(4):
        tri=tuple(neigh[i] for i in range(4) if i!=r)
        s=(-1)**r
        a,b,c=tri
        cyc=((v,a,b,c),(v,b,c,a),(v,c,a,b))
        blocks.append({"omitted_index":r,"sign":s,"cyclic_specs":[list(x) for x in cyc]})
        expected.extend((s,x) for x in cyc)

    seq_checks=[]
    for sign,spec in expected:
        vv,a,b,c=spec
        seqs=PW.T_sequences(vv,a,b,c)
        pf=(vv,a,b,vv)
        pr=(vv,b,a,vv)
        rows=[]
        for coef,seq in seqs:
            last=seq[-1]
            rows.append({"coef":coef,"last_path":list(last[1]) if last[0]=='P' else None})
        n_pf=sum(1 for coef,seq in seqs if seq[-1][0]=='P' and seq[-1][1]==pf)
        n_pr=sum(1 for coef,seq in seqs if seq[-1][0]=='P' and seq[-1][1]==pr)
        sum_pf=sum(coef for coef,seq in seqs if seq[-1][0]=='P' and seq[-1][1]==pf)
        sum_pr=sum(coef for coef,seq in seqs if seq[-1][0]=='P' and seq[-1][1]==pr)
        # There are 2^3 auxiliary-index choices, each contributing four algebraic
        # sequences. For every fixed auxiliary choice, pf/pr enter with opposite
        # signs in the same volume-commutator block. Globally their raw coefficient
        # sums vanish separately because the second block carries the opposite sign;
        # the structural test therefore checks multiplicities and pairwise sign pattern.
        pattern_ok=True
        for q in range(0,len(seqs),4):
            four=seqs[q:q+4]
            if len(four)!=4:
                pattern_ok=False; break
            coefs=[x[0] for x in four]
            paths=[x[1][-1][1] for x in four]
            if coefs != [1,-1,-1,1] or paths != [pf,pr,pf,pr]:
                pattern_ok=False; break
        seq_checks.append({
            "spec":list(spec),"orientation_sign":sign,"sequence_count":len(seqs),
            "pf_count":n_pf,"pr_count":n_pr,"pf_total_coef":sum_pf,"pr_total_coef":sum_pr,
            "four_term_forward_reverse_pattern":pattern_ok,"sample":rows[:4],
        })

    return {
        "node":v,
        "neighbor_order":list(neigh),
        "production_spec_count":len(specs),
        "expected_spec_count":len(expected),
        "specs_exactly_match":specs==expected,
        "blocks":blocks,
        "sequence_checks":seq_checks,
        "all_sequence_patterns_ok":all(x["four_term_forward_reverse_pattern"] for x in seq_checks),
        "all_sequence_counts_32":all(x["sequence_count"]==32 for x in seq_checks),
        "all_pf_pr_counts_equal":all(x["pf_count"]==x["pr_count"]==16 for x in seq_checks),
    }


def run(hbar=1.0):
    if hbar<=0:
        raise ValueError('hbar must be positive')
    perms=list(itertools.permutations((0,1,2)))
    pos=[p for p in perms if parity(p)==1]
    neg=[p for p in perms if parity(p)==-1]
    cyclic=[(0,1,2),(1,2,0),(2,0,1)]
    reverse=[(1,0,2),(2,1,0),(0,2,1)]
    pairs=[{"forward":list(f),"reverse":list(r),"forward_sign":parity(f),"reverse_sign":parity(r)}
           for f,r in zip(cyclic,reverse)]

    prod=inspect_production(0)

    cE=-2.0/(3.0j*hbar)
    nE=cE*1j
    gR_abs=8.0*(abs(nE)**2)/(hbar**5)
    local=gR_abs*C_L
    global_split=gR_abs*GLOBAL_RAW_SPLIT

    checks={
        "six_epsilon_permutations":len(perms)==6,
        "three_positive":len(pos)==3,
        "three_negative":len(neg)==3,
        "positive_are_cyclic":set(pos)==set(cyclic),
        "negative_are_reverse":set(neg)==set(reverse),
        "each_pair_has_opposite_sign":all(x["forward_sign"]==1 and x["reverse_sign"]==-1 for x in pairs),
        "production_has_4x3_specs":prod["production_spec_count"]==12,
        "production_specs_exactly_match_declared_cycles":prod["specs_exactly_match"],
        "production_T_sequences_are_32_terms":prod["all_sequence_counts_32"],
        "production_T_sequences_have_equal_pf_pr_multiplicity":prod["all_pf_pr_counts_equal"],
        "production_T_sequences_pair_forward_reverse_signs":prod["all_sequence_patterns_ok"],
        "nE_is_real":abs(nE.imag)<1e-15,
        "nE_matches_minus_2_over_3hbar":abs(nE.real+2.0/(3.0*hbar))<1e-15,
        "gR_matches_32_over_9_hbar7":abs(gR_abs-32.0/(9.0*hbar**7))<1e-14,
        "local_normalized_value":abs(local-(32.0/9.0)*C_L/(hbar**7))<1e-12,
        "global_normalized_value":abs(global_split-(32.0/9.0)*GLOBAL_RAW_SPLIT/(hbar**7))<1e-11,
    }
    return {
        "status":"conditional Euclidean sine normalization match bound to production combinatorics",
        "passed":all(checks.values()),
        "hbar":hbar,
        "epsilon_permutations":{"positive":[list(x) for x in pos],"negative":[list(x) for x in neg],"paired":pairs},
        "production_combinatorics":prod,
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
            "Code-bound combinatorial/coefficient match in the original tetrahedral fundamental-trace convention. "
            "This fixes relative dimensionless normalization, not an absolute physical energy scale. "
            "Changes to auxiliary trace, path normalization, volume normalization or oriented-spec semantics require rerunning the gate."
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
