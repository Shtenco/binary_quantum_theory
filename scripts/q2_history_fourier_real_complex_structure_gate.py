#!/usr/bin/env python3
"""Exact q=2 history-Fourier / real complex-structure bridge.

For the minimal orientation-resolved history lift

    W = P_+ tensor U + P_- tensor U^-1,

restrict to a history Fourier character with U eigenvalue exp(i theta).  The
logical geometry block is

    W(theta)=P_+ exp(i theta)+P_- exp(-i theta)
            = cos(theta) I + i sin(theta) Y_L.

Because J=-i Y_L is real and J^2=-I,

    W(theta)=exp(-theta J)

is an ordinary real SO(2) rotation.  This gate checks the identity exactly on
all C8 characters and verifies the group law and orientation-unresolved cosine
projection.  It is a representation theorem, not an identification of the
history coordinate with physical time.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def zero(M: sp.Matrix) -> bool:
    return all(sp.simplify(sp.expand_complex(x)) == 0 for x in M)


def run() -> dict[str, object]:
    I = sp.eye(2)
    Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    J = -sp.I * Y
    Pp = (I + Y) / 2
    Pm = (I - Y) / 2

    J_real = all(sp.im(x) == 0 for x in J)
    J_square = zero(J * J + I)

    rows = []
    all_blocks = True
    all_real = True
    unresolved_cosine = True
    reversal_pair = True
    for m in range(8):
        theta = sp.pi * sp.Rational(m, 4)
        z = sp.exp(sp.I * theta)
        Wm = (Pp * z + Pm / z).applyfunc(lambda x: sp.simplify(sp.expand_complex(x)))
        trig = (sp.cos(theta) * I + sp.I * sp.sin(theta) * Y).applyfunc(
            lambda x: sp.simplify(sp.expand_complex(x))
        )
        realrot = (sp.cos(theta) * I - sp.sin(theta) * J).applyfunc(
            lambda x: sp.simplify(sp.expand_complex(x))
        )
        ok = zero(Wm - trig) and zero(Wm - realrot)
        real_ok = all(sp.simplify(sp.im(x)) == 0 for x in Wm)
        tr_ok = sp.simplify(sp.trace(Wm) - 2 * sp.cos(theta)) == 0

        theta_r = -theta
        zr = sp.exp(sp.I * theta_r)
        Wrev = (Pm * zr + Pp / zr).applyfunc(lambda x: sp.simplify(sp.expand_complex(x)))
        rev_ok = zero(Wm - Wrev)

        all_blocks &= ok
        all_real &= real_ok
        unresolved_cosine &= tr_ok
        reversal_pair &= rev_ok
        rows.append({
            "m": m,
            "theta_over_pi": str(sp.Rational(m, 4)),
            "identity_passed": bool(ok),
            "matrix_is_real": bool(real_ok),
            "orientation_trace_is_2cos": bool(tr_ok),
            "simultaneous_orientation_history_reversal_invariant": bool(rev_ok),
        })

    # Exact symbolic group law in real-rotation form.
    a, b = sp.symbols("a b", real=True)
    Ra = sp.cos(a) * I - sp.sin(a) * J
    Rb = sp.cos(b) * I - sp.sin(b) * J
    Rab = sp.cos(a + b) * I - sp.sin(a + b) * J
    group_law = zero((Ra * Rb - Rab).applyfunc(sp.trigsimp))

    # Generator and orientation-unresolved small-angle structure.
    t = sp.symbols("t", real=True)
    Rt = sp.cos(t) * I - sp.sin(t) * J
    generator = Rt.diff(t).subs(t, 0)
    generator_exact = zero(generator + J)
    trace_series = sp.series(sp.trace(Rt) / 2, t, 0, 5).removeO()
    cosine_series_ok = sp.simplify(trace_series - (1 - t**2 / 2 + t**4 / 24)) == 0

    passed = bool(
        J_real
        and J_square
        and all_blocks
        and all_real
        and unresolved_cosine
        and reversal_pair
        and group_law
        and generator_exact
        and cosine_series_ok
    )

    return {
        "status": "exact q=2 history Fourier phase equals real SO(2) complex-structure rotation",
        "passed": passed,
        "J": [[str(x) for x in row] for row in J.tolist()],
        "checks": {
            "J_is_real": bool(J_real),
            "J_squared_is_minus_I": bool(J_square),
            "all_C8_character_blocks_match_cos_plus_iYsin": bool(all_blocks),
            "all_C8_character_blocks_are_real_rotations": bool(all_real),
            "orientation_unresolved_trace_is_cosine": bool(unresolved_cosine),
            "simultaneous_orientation_history_reversal_is_invariant": bool(reversal_pair),
            "continuous_rotation_group_law": bool(group_law),
            "infinitesimal_generator_is_minus_J": bool(generator_exact),
            "orientation_unresolved_small_angle_starts_quadratic": bool(cosine_series_ok),
        },
        "C8_rows": rows,
        "exact_identity": "W(theta)=P+ e^{i theta}+P- e^{-i theta}=cos(theta) I+i sin(theta)Y_L=exp(-theta J), J=-iY_L",
        "coarse_orientation_unresolved": "Tr_geometry W(theta)/2 = cos(theta); the orientation-odd sin(theta) term cancels when the two directions are unresolved.",
        "continuum_interpretation": "When the allowed character angles become dense and are Archimedean-completed, the same real J represents the full U(1) rotation group without requiring primitive complex-number arithmetic.",
        "claim_boundary": "Exact representation theorem only. The history Fourier character is not asserted to be physical frequency, the C8 index is not asserted to be physical time, and no matter Dirac equation is derived.",
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path)
    x = ap.parse_args()
    out = run()
    text = json.dumps(out, indent=2)
    print(text)
    if x.output:
        x.output.parent.mkdir(parents=True, exist_ok=True)
        x.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
