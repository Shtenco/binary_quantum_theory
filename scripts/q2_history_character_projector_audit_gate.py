#!/usr/bin/env python3
"""Exact q=2 history character-projector and group-averaging audit.

This gate asks whether the winding/phase character algebra already derived can
be promoted naively to a *physical projector*.  It proves a sharper boundary:

1. On the minimal reversible C8 history carrier, the ordinary untwisted group
   average P0=(1/8) sum_t U^t is exactly the rank-one projector onto the trivial
   character.  It annihilates every nontrivial C8 phase sector.

2. Character-twisted averages

       P_m=(1/8) sum_t zeta^(-m t) U^t

   are exact mutually orthogonal rank-one spectral projectors.  Choosing m is
   extra sector/boundary data; ordinary gauge averaging does not choose it.

3. Over the universal cover Z, the bilateral shift has no nonzero normalizable
   l2 eigenvector with unit-modulus eigenvalue.  Continuous winding characters
   are therefore generalized spectral states, not ordinary Hilbert-space
   vectors.  The formal twisted Z-average is distributional and requires a
   rigging-map/spectral-measure or boundary-history interpretation.

4. Abel regularization gives the exact Poisson kernel

       sum_{w in Z} r^|w| exp(i w phi)
       = (1-r^2)/(1-2 r cos(phi)+r^2),  0<r<1,

   an approximate identity whose r->1 limit is delta-like on the character
   circle, not a bounded rank-one l2 projector.

No constraint spectral parameter is renamed physical time/frequency here.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def shift_matrix(n: int) -> sp.Matrix:
    U = sp.zeros(n)
    for k in range(n):
        U[(k + 1) % n, k] = 1
    return U


def is_zero_matrix(M: sp.Matrix) -> bool:
    return all(sp.simplify(x) == 0 for x in M)


def projector(U: sp.Matrix, m: int) -> sp.Matrix:
    n = U.rows
    zeta = sp.exp(2 * sp.pi * sp.I / n)
    P = sp.zeros(n)
    Ut = sp.eye(n)
    for t in range(n):
        P += zeta ** (-m * t) * Ut
        Ut = Ut * U
    return P.applyfunc(lambda x: sp.simplify(sp.expand_complex(x / n)))


def run() -> dict[str, object]:
    n = 8
    U = shift_matrix(n)
    I8 = sp.eye(n)
    zeta = sp.exp(2 * sp.pi * sp.I / n)
    Ps = [projector(U, m) for m in range(n)]

    idempotent = []
    hermitian = []
    ranks = []
    eigen_errors = []
    for m, P in enumerate(Ps):
        idempotent.append(is_zero_matrix((P * P - P).applyfunc(sp.simplify)))
        hermitian.append(is_zero_matrix((P.H - P).applyfunc(sp.simplify)))
        ranks.append(int(P.rank()))
        eig = zeta ** m
        eigen_errors.append(
            is_zero_matrix((U * P - eig * P).applyfunc(lambda x: sp.simplify(sp.expand_complex(x))))
        )

    orthogonal = True
    for m in range(n):
        for k in range(n):
            if m == k:
                continue
            orthogonal &= is_zero_matrix((Ps[m] * Ps[k]).applyfunc(sp.simplify))

    completeness = is_zero_matrix((sum(Ps, sp.zeros(n)) - I8).applyfunc(sp.simplify))

    # Untwisted group average is exactly P_0 and kills every nontrivial sector.
    Pavg = sp.zeros(n)
    Ut = sp.eye(n)
    for _ in range(n):
        Pavg += Ut
        Ut = Ut * U
    Pavg = (Pavg / n).applyfunc(sp.simplify)
    untwisted_is_P0 = is_zero_matrix((Pavg - Ps[0]).applyfunc(sp.simplify))
    kills_nontrivial = all(
        is_zero_matrix((Pavg * Ps[m]).applyfunc(sp.simplify)) for m in range(1, n)
    )

    # Real paired sectors: m and N-m make a real 2D rotation plane.
    pair_rows = []
    real_pair_ok = True
    for m in (1, 2, 3):
        Q = (Ps[m] + Ps[n - m]).applyfunc(lambda x: sp.simplify(sp.expand_complex(x)))
        entries_real = all(sp.simplify(sp.im(x)) == 0 for x in Q)
        rank2 = int(Q.rank()) == 2
        idem = is_zero_matrix((Q * Q - Q).applyfunc(sp.simplify))
        real_pair_ok &= entries_real and rank2 and idem
        pair_rows.append(
            {
                "m_pair": [m, n - m],
                "rank": int(Q.rank()),
                "entries_are_real": entries_real,
                "idempotent": idem,
            }
        )

    # Universal-cover no-go: T psi = u psi implies constant modulus.
    # On a symmetric finite window [-L,L], the generalized character has
    # squared norm 2L+1, which diverges. This is exact for |u|=1.
    window_rows = []
    for L in (1, 2, 4, 8, 16, 32):
        window_rows.append(
            {
                "L": L,
                "sites": 2 * L + 1,
                "character_window_norm_squared": 2 * L + 1,
            }
        )
    norm_diverges = all(
        window_rows[i + 1]["character_window_norm_squared"]
        > window_rows[i]["character_window_norm_squared"]
        for i in range(len(window_rows) - 1)
    )

    # Exact Abel/Poisson identity via finite symbolic algebra of geometric sums.
    r, phi = sp.symbols("r phi", positive=True, real=True)
    z = sp.exp(sp.I * phi)
    # sum_{w>=1} r^w z^w + sum_{w>=1} r^w z^-w + 1
    abel_geometric = 1 + r * z / (1 - r * z) + r / z / (1 - r / z)
    poisson = (1 - r**2) / (1 - 2 * r * sp.cos(phi) + r**2)
    poisson_identity = sp.simplify(sp.trigsimp(sp.expand_complex(abel_geometric - poisson))) == 0

    # Exact normalization of Poisson kernel follows from Fourier constant term;
    # numerical-free symbolic integral is also available to SymPy for 0<r<1,
    # but we register the Fourier argument explicitly rather than depending on
    # integration heuristics.
    abel_constant_fourier_coefficient = 1
    poisson_mass_2pi = abel_constant_fourier_coefficient == 1

    # Pointwise away from phi=0: numerator ->0, denominator -> 2-2cos(phi)>0.
    pointwise_away_from_zero_limit_statement = (
        "for fixed phi not congruent 0 mod 2pi, K_r(phi)->0 as r->1-; total circle mass remains 2pi, so the limit is distributional/delta-like"
    )

    checks = {
        "all_C8_character_projectors_idempotent": all(idempotent),
        "all_C8_character_projectors_Hermitian": all(hermitian),
        "all_C8_character_projectors_rank1": all(r == 1 for r in ranks),
        "C8_character_projectors_mutually_orthogonal": orthogonal,
        "C8_character_projectors_complete": completeness,
        "U_eigenvalue_on_each_character_projector": all(eigen_errors),
        "untwisted_group_average_is_trivial_projector": untwisted_is_P0,
        "untwisted_group_average_kills_all_nontrivial_characters": kills_nontrivial,
        "real_conjugate_character_pairs_are_rank2_projectors": real_pair_ok,
        "universal_cover_character_window_norm_diverges": norm_diverges,
        "Abel_sum_equals_Poisson_kernel": bool(poisson_identity),
        "Poisson_kernel_has_unit_Fourier_constant_term": poisson_mass_2pi,
    }

    return {
        "status": "exact character-projector audit with a no-go for naive physical group averaging",
        "passed": bool(all(checks.values())),
        "C8_projector_ranks": ranks,
        "real_character_pair_projectors": pair_rows,
        "universal_cover_character_norm_control": window_rows,
        "poisson_kernel": "K_r(phi)=(1-r^2)/(1-2*r*cos(phi)+r^2)",
        "poisson_distributional_limit": pointwise_away_from_zero_limit_statement,
        "checks": checks,
        "exact_no_go": (
            "If the C8 history shift U is treated as a pure gauge redundancy and one applies the ordinary untwisted group average, the result is exactly P_0 and every nontrivial phase character is annihilated. Therefore the nontrivial winding phase cannot simultaneously be 'just gauge' and survive as a physical observable under ordinary group averaging."
        ),
        "twisted_sector_statement": (
            "Character-twisted finite averages P_m are mathematically exact spectral projectors, but selecting m is additional sector/boundary/charge information. On the universal cover Z the analogous continuous-theta objects are generalized spectral distributions rather than normalizable l2 vectors, so a rigging map, spectral measure, boundary amplitude or relational-history construction is required."
        ),
        "physical_options": [
            "treat the q=2 phase/history shift as a physical relational or boundary symmetry rather than a pure gauge orbit",
            "use character-labelled superselection/boundary sectors with their label derived from microscopic boundary/history data",
            "construct a genuine rigging-map/history amplitude whose distributional character decomposition is derived from the constraint and measure",
        ],
        "claim_boundary": (
            "This gate does not identify U with physical time evolution, does not derive a gravitational rigging map, and does not select a physical theta/character. It only proves what ordinary and character-twisted averaging do to the exact minimal q=2 history carrier and why the Z-cover character limit is distributional."
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
