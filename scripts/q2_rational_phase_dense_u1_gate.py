#!/usr/bin/env python3
"""Exact rational-phase bridge from q=2 C4/J to dense U(1).

The q=2 C4 carrier already provides the real complex structure

    J = [[0,-1],[1,0]],  J^2=-I.

Once ordinary rational coefficients are available, every rational point on the
unit circle gives a phase matrix a I + b J.  The Pythagorean parameterization

    a=(q^2-p^2)/(p^2+q^2),
    b=2pq/(p^2+q^2)

is exact and rational.  Because Q is dense in R and stereographic projection is
continuous away from one point (which is itself rational), these rational unit
phases are dense in U(1).  Archimedean completion closes the dense subgroup to
all of SO(2) ~= U(1).

This route does not require exact finite-level mu_8, mu_16, ... as primitive
phase alphabets.  The dyadic history-root tower remains a sufficient separate
mechanism, not a necessary one.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path


def pythagorean_phase(p: int, q: int) -> tuple[Fraction, Fraction]:
    if p == 0 and q == 0:
        raise ValueError("p=q=0 is undefined")
    d = p * p + q * q
    return Fraction(q * q - p * p, d), Fraction(2 * p * q, d)


def phase_mul(z: tuple[Fraction, Fraction], w: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    a, b = z
    c, d = w
    return a * c - b * d, a * d + b * c


def phase_matrix(z: tuple[Fraction, Fraction]):
    a, b = z
    return ((a, -b), (b, a))


def matmul2(A, B):
    return tuple(
        tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def transpose2(A):
    return ((A[0][0], A[1][0]), (A[0][1], A[1][1]))


def det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def rational_phase_set(B: int) -> list[float]:
    angles = set()
    for p in range(-B, B + 1):
        for q in range(-B, B + 1):
            if p == 0 and q == 0:
                continue
            a, b = pythagorean_phase(p, q)
            angles.add(round(math.atan2(float(b), float(a)) % (2 * math.pi), 15))
    return sorted(angles)


def max_circular_gap(angles: list[float]) -> float:
    if not angles:
        return 2 * math.pi
    gaps = []
    for i, a in enumerate(angles):
        b = angles[(i + 1) % len(angles)]
        if i == len(angles) - 1:
            b += 2 * math.pi
        gaps.append(b - a)
    return max(gaps)


def run() -> dict[str, object]:
    I = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
    J = ((Fraction(0), Fraction(-1)), (Fraction(1), Fraction(0)))
    minus_I = ((Fraction(-1), Fraction(0)), (Fraction(0), Fraction(-1)))

    # Exact Pythagorean identities on a broad integer sample.
    norm_exact = True
    orthogonal_exact = True
    det_exact = True
    samples = []
    for p in range(-12, 13):
        for q in range(-12, 13):
            if p == 0 and q == 0:
                continue
            z = pythagorean_phase(p, q)
            a, b = z
            norm_exact &= a * a + b * b == 1
            M = phase_matrix(z)
            orthogonal_exact &= matmul2(transpose2(M), M) == I
            det_exact &= det2(M) == 1
            if len(samples) < 12:
                samples.append({"p": p, "q": q, "a": str(a), "b": str(b)})

    # Exact multiplicative closure of rational unit phases.
    closure_exact = True
    seed = [pythagorean_phase(0, 1), pythagorean_phase(1, 1), pythagorean_phase(1, 2), pythagorean_phase(2, 3)]
    products = []
    for z in seed:
        for w in seed:
            u = phase_mul(z, w)
            closure_exact &= u[0] * u[0] + u[1] * u[1] == 1
            products.append((str(u[0]), str(u[1])))

    # Matrix multiplication agrees exactly with complex phase multiplication.
    matrix_hom_exact = all(
        phase_matrix(phase_mul(z, w)) == matmul2(phase_matrix(z), phase_matrix(w))
        for z in seed for w in seed
    )

    # C4 phases are present exactly.
    c4 = {
        "1": (Fraction(1), Fraction(0)),
        "i": (Fraction(0), Fraction(1)),
        "-1": (Fraction(-1), Fraction(0)),
        "-i": (Fraction(0), Fraction(-1)),
    }
    c4_present = all(a * a + b * b == 1 for a, b in c4.values())

    # Finite density diagnostic; the theorem itself is the rational
    # stereographic/Pythagorean parameterization plus density of Q in R.
    bounds = [2, 4, 8, 16, 32]
    density_rows = []
    for B in bounds:
        ang = rational_phase_set(B)
        density_rows.append(
            {
                "B": B,
                "distinct_rational_unit_phases": len(ang),
                "max_circular_gap_radians": max_circular_gap(ang),
            }
        )
    gap_monotone = all(
        density_rows[i + 1]["max_circular_gap_radians"]
        < density_rows[i]["max_circular_gap_radians"]
        for i in range(len(density_rows) - 1)
    )

    checks = {
        "J_squared_is_minus_I": matmul2(J, J) == minus_I,
        "pythagorean_parameterization_has_exact_unit_norm": norm_exact,
        "rational_phase_matrices_are_exact_SO2": orthogonal_exact and det_exact,
        "rational_unit_phases_closed_under_multiplication": closure_exact,
        "phase_matrix_is_exact_multiplicative_homomorphism": matrix_hom_exact,
        "coarse_mu4_is_exact_subset": c4_present,
        "finite_density_control_gap_decreases": gap_monotone,
        "B32_max_gap_below_0p07_rad": density_rows[-1]["max_circular_gap_radians"] < 0.07,
    }

    return {
        "status": "exact arithmetic/representation bridge: rational unit phases are a dense subgroup whose Archimedean completion is SO(2) ~= U(1)",
        "passed": bool(all(checks.values())),
        "J": [[str(x) for x in row] for row in J],
        "pythagorean_formula": "a=(q^2-p^2)/(p^2+q^2), b=2pq/(p^2+q^2)",
        "exact_sample_points": samples,
        "sample_products": products[:12],
        "density_control": density_rows,
        "checks": checks,
        "theorem": (
            "The rational points on S^1 are parameterized by rational stereographic slope t=p/q via ((1-t^2)/(1+t^2), 2t/(1+t^2)); Q is dense in R, so these points are dense in S^1. Under a+bi <-> aI+bJ they form a dense subgroup of SO(2). Completing Q in the Archimedean norm gives R, and the unit elements of R[J] are exactly SO(2) ~= U(1)."
        ),
        "senior_correction": (
            "An infinite exact root-of-unity tower is sufficient but not necessary for continuous phase emergence. Once the q=2 C4 supplies J and history/arithmetic supplies Q followed by Archimedean completion to R, continuous U(1) follows directly from the unit circle in R[J]."
        ),
        "claim_boundary": (
            "This is an exact arithmetic/topological representation result. It does not derive the physical history measure, the dynamical real coefficients of amplitudes, or the physical selection of the Archimedean completion."
        ),
    }


def main() -> int:
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
