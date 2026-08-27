#!/usr/bin/env python3
"""Exact winding-composition -> phase-character theorem for q=2 histories.

Once a complete oriented cycle history supplies integer winding w in Z, any
unit-norm scalar/history weight Omega that

  Omega(0)=1,
  Omega(w1+w2)=Omega(w1) Omega(w2)

is a group character of Z and is uniquely fixed by u=Omega(1):

  Omega(w)=u^w.

Using the q=2 real complex structure J, unit rational choices u=aI+bJ provide
exact rational SO(2) characters; Archimedean completion supplies all SO(2)
characters. Orientation reversal w->-w sends the character to inverse/transpose,
which is complex conjugation in spectral notation.

The script also verifies the exact finite C4 character table and the special
Gaussian-rational torsion fact: the rational/gaussian phase field has primitive
finite torsion mu4; higher exact roots require a larger coefficient field (or a
larger history spectrum such as the separate C8 dilation).
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def mm(A, B):
    return tuple(
        tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def mt(A):
    return ((A[0][0], A[1][0]), (A[0][1], A[1][1]))


def eye():
    return ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))


def phase_matrix(a: Fraction, b: Fraction):
    return ((a, -b), (b, a))


def mpow(A, n: int):
    if n == 0:
        return eye()
    if n < 0:
        # Unit SO(2) matrices have inverse transpose.
        return mpow(mt(A), -n)
    out = eye()
    base = A
    k = n
    while k:
        if k & 1:
            out = mm(out, base)
        base = mm(base, base)
        k >>= 1
    return out


def pythagorean_phase(p: int, q: int):
    d = p * p + q * q
    if d == 0:
        raise ValueError
    return Fraction(q * q - p * p, d), Fraction(2 * p * q, d)


def gaussian_mul(z, w):
    a, b = z
    c, d = w
    return a * c - b * d, a * d + b * c


def gaussian_conj(z):
    return z[0], -z[1]


def gaussian_pow(z, n: int):
    if n == 0:
        return (1, 0)
    if n < 0:
        # only used for unit Gaussian roots below
        return gaussian_pow(gaussian_conj(z), -n)
    out = (1, 0)
    base = z
    k = n
    while k:
        if k & 1:
            out = gaussian_mul(out, base)
        base = gaussian_mul(base, base)
        k >>= 1
    return out


def read_history(path: Path | None):
    if path is None:
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def run(history_json: dict | None = None) -> dict[str, object]:
    # Exact rational SO(2) characters of Z.
    rational_generators = [
        pythagorean_phase(0, 1),  # 1
        pythagorean_phase(1, 1),  # i
        pythagorean_phase(1, 2),  # 3/5 + 4/5 i
        pythagorean_phase(2, 3),  # 5/13 + 12/13 i
        pythagorean_phase(3, 5),  # 8/17 + 15/17 i
    ]
    character_law = True
    orientation_conjugation = True
    unit_norm = True
    character_examples = []
    for a, b in rational_generators:
        U = phase_matrix(a, b)
        unit_norm &= mm(mt(U), U) == eye()
        for m in range(-6, 7):
            orientation_conjugation &= mpow(U, -m) == mt(mpow(U, m))
            for n in range(-6, 7):
                character_law &= mpow(U, m + n) == mm(mpow(U, m), mpow(U, n))
        character_examples.append(
            {
                "generator": [str(a), str(b)],
                "Omega_3": [[str(x) for x in row] for row in mpow(U, 3)],
                "Omega_minus3": [[str(x) for x in row] for row in mpow(U, -3)],
            }
        )

    # Finite C4 character table in exact Gaussian integer arithmetic.
    iunit = (0, 1)
    chars = []
    finite_character_law = True
    orthogonality = True
    for m in range(4):
        row = [gaussian_pow(iunit, m * k) for k in range(4)]
        chars.append(row)
        for a in range(4):
            for b in range(4):
                finite_character_law &= gaussian_pow(iunit, m * ((a + b) % 4)) == gaussian_mul(
                    gaussian_pow(iunit, m * a), gaussian_pow(iunit, m * b)
                )
    for m in range(4):
        for n in range(4):
            s = (0, 0)
            for k in range(4):
                term = gaussian_mul(chars[m][k], gaussian_conj(chars[n][k]))
                s = (s[0] + term[0], s[1] + term[1])
            target = (4, 0) if m == n else (0, 0)
            orthogonality &= s == target

    # Exact torsion of Gaussian integers at norm one is visibly mu4:
    # a,b integers and a^2+b^2=1 has exactly four solutions.
    gaussian_integer_unit_circle = sorted(
        (a, b)
        for a in range(-2, 3)
        for b in range(-2, 3)
        if a * a + b * b == 1
    )
    expected_mu4 = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    mu4_exact = gaussian_integer_unit_circle == expected_mu4

    history_input_ok = True
    history_evidence = None
    if history_json is not None:
        pf = history_json.get("physical_frontier", {})
        history_input_ok = bool(history_json.get("passed")) and str(
            pf.get("history_to_winding", "")
        ).startswith("EXACT")
        history_evidence = {
            "passed": history_json.get("passed"),
            "history_to_winding": pf.get("history_to_winding"),
            "winding_values_seen": history_json.get("winding_universal_cover", {}).get(
                "winding_values_seen"
            ),
        }

    checks = {
        "history_input_certifies_integer_winding": history_input_ok,
        "rational_generators_are_exact_unit_rotations": unit_norm,
        "Z_character_composition_law": character_law,
        "orientation_reversal_is_inverse_transpose_conjugation": orientation_conjugation,
        "finite_C4_character_law": finite_character_law,
        "finite_C4_character_orthogonality": orthogonality,
        "Gaussian_integer_norm1_torsion_seed_is_mu4": mu4_exact,
    }

    return {
        "status": "exact history-composition character theorem: integer winding dual phase weights are SO(2)/U(1) characters",
        "passed": bool(all(checks.values())),
        "history_evidence": history_evidence,
        "rational_character_examples": character_examples,
        "finite_C4_character_table_gaussian_pairs": [
            [[a, b] for a, b in row] for row in chars
        ],
        "gaussian_integer_unit_circle": [list(x) for x in gaussian_integer_unit_circle],
        "checks": checks,
        "theorem": (
            "For the additive winding group Z, any normalized multiplicative unit-phase weight Omega is a group character and is uniquely determined by u=Omega(1): Omega(w)=u^w. In the real q=2 phase representation u is an SO(2) matrix aI+bJ. Rational unit choices give a dense character subgroup after the rational-phase theorem; Archimedean completion gives all SO(2) ~= U(1) characters."
        ),
        "orientation_rule": "w -> -w sends Omega(w) -> Omega(w)^(-1) = Omega(w)^T, i.e. complex conjugation in spectral notation",
        "gaussian_torsion_note": (
            "The algebraic integers of Q(i) are Z[i]. A root of unity in Q(i) is an algebraic-integer unit, so its norm-one coordinates are integer solutions of a^2+b^2=1: exactly +/-1,+/-i. Thus mu4 is the complete finite torsion seed inside the Gaussian rational phase field; exact mu8 requires adjoining sqrt(2) or using the separate 8D history spectrum."
        ),
        "claim_boundary": (
            "The character form follows from winding additivity, sequential composition and unit norm. The theorem does not determine the physical character generator u (the analogue of a theta/action parameter), nor prove that the gravitational physical-projector assigns weights depending only on winding."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--history-json", type=Path)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    out = run(read_history(args.history_json))
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
