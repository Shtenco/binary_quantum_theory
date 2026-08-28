#!/usr/bin/env python3
"""Exact S4 sign-orbit reduction of the four-face Lorentzian epsilon assembler.

For a fixed ordered four-neighbor frame (0,1,2,3), the raw Lorentzian epsilon
assembler contains all 24 ordered triples obtained by omitting one neighbor and
permuting the remaining three.  This gate proves combinatorially that its
coefficient for the triple encoded by p=(a,b,c,d) is one global sign times the
S4 sign character:

    epsilon_coeff(p) = -sgn(p)

for the repository's current face-sign convention (-1)^r.

Therefore, if the genuine microscopic ordered triple is S4-covariant on the
logical [2,2] carrier,

    T_{p(a)p(b)p(c)} = U_p O U_p^dagger,

then the full 24-term logical epsilon sum is just -24 times the S4 sign twirl of
one canonical logical operator O.  Since End(E)=A1(I)+A2(Y)+E(X,Z), the result
is exactly proportional to Y:

    L_epsilon^logical = -12 Tr(Y O) Y

with the overall minus sign fixed only by the declared frame/face convention.

This is an exact reduction theorem.  It does not by itself prove genuine
Peter-Weyl S4 covariance of the sine-ordered triple; that remains a separate
amplitude gate.
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import logical_s4_twirl_gate as S4
import logical_s4_sign_twirl_gate as SGN


def perm_sign(p):
    inv = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inv % 2 else +1


def parity(base, perm):
    idx = [base.index(x) for x in perm]
    inv = sum(idx[i] > idx[j] for i in range(len(idx)) for j in range(i + 1, len(idx)))
    return -1 if inv % 2 else +1


def epsilon_coeff(frame, triple):
    omitted = next(x for x in frame if x not in triple)
    r = frame.index(omitted)
    base = tuple(x for x in frame if x != omitted)
    return ((-1) ** r) * parity(base, triple)


def run():
    frame = (0, 1, 2, 3)
    perms = list(itertools.permutations(frame))

    rows = []
    coeff_relation = True
    seen = set()
    for p in perms:
        tri = tuple(p[:3])
        coeff = epsilon_coeff(frame, tri)
        s = perm_sign(p)
        coeff_relation &= coeff == -s
        seen.add(tri)
        rows.append({
            "permutation": list(p),
            "ordered_triple": list(tri),
            "omitted": p[3],
            "epsilon_coefficient": coeff,
            "permutation_sign": s,
            "coefficient_equals_minus_sign": coeff == -s,
        })

    # There are exactly 4 choices of omitted neighbor times 3! orderings.
    complete_24_orbit = len(perms) == 24 and len(seen) == 24

    basis = S4.singlet_basis()
    reps = [S4.logical_representation(p, basis) for p in perms]
    Y = S4.PAULI["Y"]

    # Generic deterministic logical operator.  No special symmetry is built in.
    O = np.array(
        [[1.25 + 0.5j, -0.75 + 1.125j],
         [0.375 - 0.625j, -2.0 + 0.25j]],
        dtype=complex,
    )

    sign_twirl = SGN.sign_twirl_one(O, reps, perms)
    hs_coeff = np.trace(Y.conj().T @ O) / np.trace(Y.conj().T @ Y)
    expected_twirl = hs_coeff * Y
    sign_twirl_error = float(np.linalg.norm(sign_twirl - expected_twirl))

    # Direct 24-term epsilon orbit using the proven coefficient map.
    full = np.zeros((2, 2), complex)
    for U, p in zip(reps, perms):
        coeff = -perm_sign(p)
        full += coeff * (U @ O @ U.conj().T)

    expected_full = -24.0 * expected_twirl
    full_error = float(np.linalg.norm(full - expected_full))

    # Equivalent compact coefficient formula, because Tr(Y^dag Y)=2.
    compact = -12.0 * np.trace(Y @ O) * Y
    compact_error = float(np.linalg.norm(full - compact))

    # Basis-level selection: I,X,Z vanish, Y survives.
    basis_results = {}
    basis_ok = True
    for name, P in S4.PAULI.items():
        T = SGN.sign_twirl_one(P, reps, perms)
        target = Y if name == "Y" else np.zeros_like(Y)
        err = float(np.linalg.norm(T - target))
        basis_results[name] = err
        basis_ok &= err < 1e-12

    passed = bool(
        complete_24_orbit
        and coeff_relation
        and sign_twirl_error < 1e-12
        and full_error < 1e-11
        and compact_error < 1e-11
        and basis_ok
    )

    return {
        "status": "exact S4 sign-orbit reduction of the 24-term Lorentzian epsilon assembler",
        "passed": passed,
        "frame": list(frame),
        "ordered_term_count": len(rows),
        "unique_ordered_triple_count": len(seen),
        "epsilon_coefficient_identity": "epsilon_coeff(p) = -sgn(p) for the current (-1)^r face convention",
        "coefficient_identity_passed": bool(coeff_relation),
        "rows": rows,
        "logical_sign_twirl_error": sign_twirl_error,
        "full_24_orbit_reduction_error": full_error,
        "compact_Y_formula_error": compact_error,
        "logical_basis_sign_twirl_errors": basis_results,
        "logical_formula": "L_epsilon = -24*T_sgn(O) = -12*Tr(Y O)*Y",
        "global_sign_note": (
            "The displayed overall minus sign belongs to the repository's chosen ordered frame and face sign (-1)^r. Reversing the global frame orientation flips this overall convention but not the one-dimensional Y-channel statement."
        ),
        "computational_consequence": (
            "Once genuine Peter-Weyl covariance of the ordered triple under neighbor S4 is validated on generators, the full logical epsilon node does not require 24 independent heavy amplitudes. One canonical 2x2 logical ordered-triple matrix O suffices; the 24-term sum is reconstructed exactly by the sign twirl."
        ),
        "claim_boundary": (
            "Exact combinatorics plus finite logical representation theory. This gate does not prove that the genuine sine-ordered Peter-Weyl triple obeys the required S4 covariance, does not compute O, and does not compute g_YC^gravity."
        ),
    }


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    out = run()
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
