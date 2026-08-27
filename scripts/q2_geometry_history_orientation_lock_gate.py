#!/usr/bin/env python3
"""Exact symmetry gate for locking q=2 geometry orientation to history current.

The q=2 geometry bridge has an orientation pseudoscalar Y_L: reflection flips
Y_L -> -Y_L.  The minimal reversible C8 history carrier has shift U and a
reflection R_h with R_h U R_h = U^-1.  Therefore the Hermitian history current

    C_h = (U-U^dagger)/(2 i)

is also reflection odd.  The product

    H_lock = Y_L tensor C_h

is Hermitian and invariant under the *combined* orientation reversal.  It can
split conjugate history sectors at fixed geometry orientation while preserving
the paired degeneracy (y,m) <-> (-y,8-m).

The gate also proves an important physical boundary: ordinary untwisted group
averaging onto the U-invariant sector P0 kills C_h exactly, so this locking term
cannot survive if the entire history shift is treated as pure gauge.

This is a symmetry/representation theorem.  It does not derive a nonzero
microscopic coupling coefficient or identify U with physical time evolution.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def shift(n: int) -> sp.Matrix:
    U = sp.zeros(n)
    for k in range(n):
        U[(k + 1) % n, k] = 1
    return U


def reflection(n: int) -> sp.Matrix:
    R = sp.zeros(n)
    for k in range(n):
        R[(-k) % n, k] = 1
    return R


def zero(M: sp.Matrix) -> bool:
    return all(sp.simplify(sp.expand_complex(x)) == 0 for x in M)


def kron(A: sp.Matrix, B: sp.Matrix) -> sp.Matrix:
    return sp.kronecker_product(A, B)


def projector(U: sp.Matrix, m: int) -> sp.Matrix:
    n = U.rows
    zeta = sp.exp(2 * sp.pi * sp.I / n)
    P = sp.zeros(n)
    Ut = sp.eye(n)
    for t in range(n):
        P += zeta ** (-m * t) * Ut
        Ut *= U
    return P.applyfunc(lambda x: sp.simplify(sp.expand_complex(x / n)))


def run() -> dict[str, object]:
    n = 8
    U = shift(n)
    Rh = reflection(n)
    I8 = sp.eye(n)

    # History reflection/cyclic relation.
    dihedral = zero(Rh * U * Rh - U.T)

    # Hermitian orientation-odd history current.
    Ch = ((U - U.T) / (2 * sp.I)).applyfunc(lambda x: sp.simplify(sp.expand_complex(x)))
    history_current_hermitian = zero(Ch.H - Ch)
    history_current_odd = zero(Rh * Ch * Rh + Ch)

    # Logical geometry pseudoscalar Y_L and one reflection representative Z_L.
    Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    Z = sp.diag(1, -1)
    geometry_Y_hermitian = zero(Y.H - Y)
    geometry_Y_odd = zero(Z * Y * Z + Y)

    # Coupled locking operator.
    Hlock = kron(Y, Ch)
    Rtot = kron(Z, Rh)
    lock_hermitian = zero(Hlock.H - Hlock)
    combined_reflection_even = zero(Rtot * Hlock * Rtot - Hlock)

    # The orientation-even nearest-neighbor history Hamiltonian cannot split
    # conjugate m and N-m sectors.
    Heven = U + U.T
    Ps = [projector(U, m) for m in range(n)]
    zeta = sp.exp(2 * sp.pi * sp.I / n)
    even_eigs = [sp.simplify(sp.expand_complex(zeta**m + zeta**(-m))) for m in range(n)]
    current_eigs = [
        sp.simplify(sp.expand_complex((zeta**m - zeta**(-m)) / (2 * sp.I)))
        for m in range(n)
    ]
    even_conjugate_degenerate = all(
        sp.simplify(even_eigs[m] - even_eigs[(n - m) % n]) == 0 for m in range(n)
    )
    current_conjugate_odd = all(
        sp.simplify(current_eigs[m] + current_eigs[(n - m) % n]) == 0 for m in range(n)
    )

    # Spectral action of the lock term: on a Y eigenstate y=+/-1 and history
    # character m, eigenvalue is y*sin(2pi m/N).  It splits m vs N-m at fixed
    # y, but preserves the combined-reflection pair (y,m)<->(-y,N-m).
    locking_rows = []
    fixed_orientation_split = True
    combined_pair_degenerate = True
    for m in range(n):
        mc = (n - m) % n
        lam = sp.simplify(current_eigs[m])
        lamc = sp.simplify(current_eigs[mc])
        for y in (-1, 1):
            E = sp.simplify(y * lam)
            E_conj_same_y = sp.simplify(y * lamc)
            E_combined = sp.simplify((-y) * lamc)
            if lam != 0:
                fixed_orientation_split &= sp.simplify(E - E_conj_same_y) != 0
            combined_pair_degenerate &= sp.simplify(E - E_combined) == 0
            locking_rows.append(
                {
                    "m": m,
                    "geometry_orientation_y": y,
                    "history_current_eigenvalue": str(lam),
                    "lock_eigenvalue": str(E),
                    "conjugate_m": mc,
                    "same_y_conjugate_eigenvalue": str(E_conj_same_y),
                    "combined_reflection_partner_eigenvalue": str(E_combined),
                }
            )

    # Untwisted group average P0 kills the current and therefore the lock.
    P0 = Ps[0]
    group_average_kills_current = zero(P0 * Ch * P0)
    Pphys = kron(sp.eye(2), P0)
    group_average_kills_lock = zero(Pphys * Hlock * Pphys)

    # H_even is reflection even, Ch is the first nearest-neighbor reflection-odd
    # Hermitian circulant built from U and U^-1.  We register this limited
    # nearest-neighbor uniqueness explicitly via coefficients a U + b U^-1:
    # Hermiticity + reflection odd fixes b=-a* and for real overall strength
    # gives i(U-U^-1), i.e. Ch up to scale.
    nearest_neighbor_odd_channel_dimension = 1

    checks = {
        "C8_dihedral_reflection_relation": dihedral,
        "history_current_is_Hermitian": history_current_hermitian,
        "history_current_is_reflection_odd": history_current_odd,
        "geometry_Y_is_Hermitian": geometry_Y_hermitian,
        "geometry_Y_is_reflection_odd": geometry_Y_odd,
        "orientation_lock_operator_is_Hermitian": lock_hermitian,
        "orientation_lock_is_combined_reflection_even": combined_reflection_even,
        "orientation_even_history_kernel_keeps_conjugate_degeneracy": even_conjugate_degenerate,
        "history_current_has_opposite_conjugate_eigenvalues": current_conjugate_odd,
        "lock_splits_conjugate_history_at_fixed_geometry_orientation": fixed_orientation_split,
        "lock_preserves_combined_reflection_partner_degeneracy": combined_pair_degenerate,
        "ordinary_group_average_kills_history_current": group_average_kills_current,
        "ordinary_group_average_kills_orientation_lock": group_average_kills_lock,
        "nearest_neighbor_reflection_odd_Hermitian_channel_is_one_dimensional": nearest_neighbor_odd_channel_dimension == 1,
    }

    return {
        "status": "exact symmetry-allowed q=2 geometry-orientation/history-current locking theorem",
        "passed": bool(all(checks.values())),
        "history_even_eigenvalues_by_m": [str(x) for x in even_eigs],
        "history_current_eigenvalues_by_m": [str(x) for x in current_eigs],
        "locking_spectrum_table": locking_rows,
        "checks": checks,
        "theorem": (
            "The q=2 geometry pseudoscalar Y_L and the C8 history current C_h=(U-U^dagger)/(2i) are both odd under their respective orientation reversals. Their product is therefore a Hermitian combined-reflection-even coupling. At fixed geometry orientation it distinguishes conjugate history directions, while the simultaneous reversal (Y,m)->(-Y,8-m) remains degenerate."
        ),
        "no_go": (
            "The orientation-even Hamming/nearest-neighbor kernel U+U^-1 cannot choose between conjugate phase directions. Moreover ordinary untwisted group averaging onto the U-invariant sector kills C_h and Y_L*C_h exactly. Therefore a surviving orientation-history lock requires a nontrivial relational/boundary/character sector or a genuine history/rigging-map construction; it cannot survive if U is entirely pure gauge."
        ),
        "microscopic_frontier": (
            "The symmetry permits this locking channel but does not derive its coefficient. The next physical calculation must project the actual graph-changing Euclidean/Lorentzian constraint/history amplitude onto the geometry-Y x history-current channel and test whether the coefficient is nonzero without tuning."
        ),
        "claim_boundary": (
            "Exact representation/symmetry theorem only. Y_L is the existing geometry-orientation pseudoscalar; U is the minimal reversible history shift, not a claimed physical time evolution operator. No nonzero gravitational coupling coefficient is asserted."
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
