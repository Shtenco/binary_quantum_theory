#!/usr/bin/env python3
"""Exact doubled-spin parity bookkeeping for the Euclidean/Lorentzian Peter-Weyl stack.

Use the already verified grading

    Pi |{s_e}> = (-1)^(sum_e s_e)|{s_e}>,  s_e=2j_e,

for which every primitive H_E sequence flips exactly three edge parities and
therefore H_E is Pi-odd.

The remaining parity assignments follow directly from the declared operators:

    V                         even
    K=[V,H_E]                 odd
    C_e(O)=h_e[h_e^-1,O]
      = O-h_e O h_e^-1       same parity as O,

because conjugation by one fundamental h and one h^-1 contributes two parity
flips. Hence C(V) is even, C(K) is odd and

    H_L ~ Tr[C(K) C(K) C(V)]

is even. For P projecting to the even all-j=1/2 logical sector,

    P H_E P = 0,
    P(H_E H_L + H_L H_E)P = 0,

while P H_L P is not forbidden by this grading.

This is a selection-rule theorem only; a nonzero amplitude requires a separate
matrix-element calculation.
"""
from __future__ import annotations

import json


def mul(*signs):
    out = +1
    for s in signs:
        out *= s
    return out


def commutator_parity(a, b):
    return mul(a, b)


def covariant_leg_parity(operator_parity):
    direct = operator_parity
    conjugated = mul(-1, operator_parity, -1)
    if direct != conjugated:
        raise AssertionError("covariant leg terms have inconsistent parity")
    return direct


def run():
    HE = -1
    V = +1
    K = commutator_parity(V, HE)
    CV = covariant_leg_parity(V)
    CK = covariant_leg_parity(K)
    HL = mul(CK, CK, CV)
    mixed = mul(HE, HL)
    HL2 = mul(HL, HL)
    HE2 = mul(HE, HE)

    passed = (
        HE == -1
        and V == +1
        and K == -1
        and CV == +1
        and CK == -1
        and HL == +1
        and mixed == -1
        and HE2 == +1
        and HL2 == +1
    )

    return {
        "status": "Peter-Weyl Euclidean/Lorentzian doubled-spin parity gate",
        "passed": bool(passed),
        "grading": "Pi=(-1)^(sum_e 2j_e)",
        "parities": {
            "H_E": HE,
            "V": V,
            "K=[V,H_E]": K,
            "C(V)": CV,
            "C(K)": CK,
            "H_L~Tr[C(K)C(K)C(V)]": HL,
            "H_E H_L + H_L H_E": mixed,
            "H_E^2": HE2,
            "H_L^2": HL2,
        },
        "logical_even_sector_consequences": {
            "P_H_E_P": "zero by parity",
            "P_H_L_P": "allowed by parity; amplitude must be computed separately",
            "P_mixed_master_P": "P(H_E H_L+H_L H_E)P=0 by parity",
            "P_G_P": "for G=H_E+lambda H_L, PGP=lambda P H_L P",
            "P_G2_P": "P H_E^2 P + lambda^2 P H_L^2 P",
        },
        "scope": (
            "Exact Z2 operator bookkeeping within the declared Peter-Weyl gravity construction; "
            "it is a finite selection-rule certificate rather than an experimental observable."
        ),
    }


if __name__ == "__main__":
    out = run()
    print(json.dumps(out, indent=2))
    raise SystemExit(0 if out["passed"] else 1)
