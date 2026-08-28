#!/usr/bin/env python3
"""Exact q=2 directed-history factorization of the undirected graph Laplacian.

Starting from the already-derived minimal orientation-resolved history step

    W = P_+ \otimes U + P_- \otimes U^{-1},
    P_\pm=(I\pm Y_L)/2,

this gate studies the full directed one-step difference

    Delta_W = W-I.

Because W is unitary and W+W^dagger is orientation independent,

    Delta_W^dagger Delta_W
      = 2I-W-W^dagger
      = I_geom \otimes (2I-U-U^dagger).

Thus the oriented first-order difference is an exact factor of the ordinary
undirected C8 graph Laplacian.  In a history character U|theta>=e^{i theta}|theta>,

    Delta(theta)=(cos theta-1) I - sin theta J,
    J=-iY_L, J^2=-I,

and

    Delta(theta)^dagger Delta(theta)=4 sin^2(theta/2) I.

The Hermitian odd current alone, D=(W-W^dagger)/(2i), instead has eigenvalue
sin(theta) and therefore an extra zero at theta=pi.  The even term
(cos(theta)-1)I in the complete forward difference removes that finite-lattice
doubler without being inserted as an independent coefficient.

This is an exact finite-history representation theorem.  It does not identify
the history index with physical time, derive a physical Dirac operator, or
establish a fermion sector.
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


def simplify_matrix(M: sp.Matrix) -> sp.Matrix:
    return M.applyfunc(lambda x: sp.simplify(sp.expand_complex(x)))


def zero(M: sp.Matrix) -> bool:
    return all(sp.simplify(sp.expand_complex(x)) == 0 for x in M)


def run() -> dict[str, object]:
    n = 8
    U = shift(n)
    Rh = reflection(n)
    I8 = sp.eye(n)
    I2 = sp.eye(2)

    Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    Z = sp.diag(1, -1)
    J = simplify_matrix(-sp.I * Y)
    Pp = simplify_matrix((I2 + Y) / 2)
    Pm = simplify_matrix((I2 - Y) / 2)

    W = simplify_matrix(sp.kronecker_product(Pp, U) + sp.kronecker_product(Pm, U.T))
    I16 = sp.eye(2 * n)
    Delta = simplify_matrix(W - I16)

    Lh = simplify_matrix(2 * I8 - U - U.T)
    target_L = sp.kronecker_product(I2, Lh)
    left_square = simplify_matrix(Delta.H * Delta)
    right_square = simplify_matrix(Delta * Delta.H)

    D = simplify_matrix((W - W.H) / (2 * sp.I))
    Ch = simplify_matrix((U - U.T) / (2 * sp.I))
    even = simplify_matrix((W + W.H) / 2)
    Ce = simplify_matrix((U + U.T) / 2)

    current_square_target = simplify_matrix(
        sp.kronecker_product(I2, Lh - (Lh * Lh) / 4)
    )

    Rtot = sp.kronecker_product(Z, Rh)

    checks = {
        "J_squared_is_minus_identity": zero(J * J + I2),
        "W_is_unitary": zero(W.H * W - I16) and zero(W * W.H - I16),
        "combined_orientation_history_reversal_covariance": zero(Rtot * W * Rtot - W),
        "even_part_is_orientation_unresolved": zero(even - sp.kronecker_product(I2, Ce)),
        "odd_current_is_Y_tensor_history_current": zero(D - sp.kronecker_product(Y, Ch)),
        "forward_difference_left_square_is_graph_laplacian": zero(left_square - target_L),
        "forward_difference_right_square_is_graph_laplacian": zero(right_square - target_L),
        "odd_current_square_has_exact_lattice_correction": zero(D * D - current_square_target),
    }

    theta = sp.symbols("theta", real=True)
    Delta_theta = simplify_matrix((sp.cos(theta) - 1) * I2 - sp.sin(theta) * J)
    spectral_square = simplify_matrix(Delta_theta.T * Delta_theta)
    spectral_target = simplify_matrix(4 * sp.sin(theta / 2) ** 2 * I2)
    checks["continuous_character_forward_factorization"] = zero(spectral_square - spectral_target)

    # Exact C8 character spectrum.  The full forward difference has a single
    # zero at m=0, while the odd Hermitian current has the extra m=4 zero.
    rows = []
    forward_zero_modes = []
    current_zero_modes = []
    for m in range(n):
        th = sp.Rational(m, 4) * sp.pi
        lap = sp.simplify(2 - 2 * sp.cos(th))
        current2 = sp.simplify(sp.sin(th) ** 2)
        forward2 = sp.simplify(4 * sp.sin(th / 2) ** 2)
        exact_match = sp.simplify(lap - forward2) == 0
        if sp.simplify(forward2) == 0:
            forward_zero_modes.append(m)
        if sp.simplify(current2) == 0:
            current_zero_modes.append(m)
        rows.append(
            {
                "m": m,
                "theta": str(th),
                "graph_laplacian_eigenvalue": str(lap),
                "forward_difference_norm_squared": str(forward2),
                "odd_current_squared": str(current2),
                "forward_matches_laplacian": bool(exact_match),
            }
        )

    checks["forward_difference_has_only_trivial_C8_zero"] = forward_zero_modes == [0]
    checks["odd_current_has_pi_doubler_zero"] = current_zero_modes == [0, 4]
    checks["all_C8_forward_squares_match_laplacian"] = all(r["forward_matches_laplacian"] for r in rows)

    # Small-angle hierarchy: the same exact step contains a leading directed
    # J term and the even O(theta^2) lattice correction.
    scalar_series = sp.series(sp.cos(theta) - 1, theta, 0, 6).removeO()
    orient_series = sp.series(-sp.sin(theta), theta, 0, 6).removeO()
    lap_series = sp.series(4 * sp.sin(theta / 2) ** 2, theta, 0, 8).removeO()

    passed = bool(all(checks.values()))
    return {
        "status": "exact orientation-resolved forward-difference factorization of the C8 graph Laplacian",
        "passed": passed,
        "definition": {
            "W": "P_+ tensor U8 + P_- tensor U8^-1",
            "Delta_W": "W-I",
            "history_laplacian": "L_h=2I-U8-U8^dagger",
            "J": "-i Y_L = [[0,-1],[1,0]]",
        },
        "exact_factorization": "(W-I)^dagger(W-I)=I_geom tensor L_h=(W-I)(W-I)^dagger",
        "odd_current_identity": "D=(W-W^dagger)/(2i)=Y_L tensor C_h",
        "odd_current_square_identity": "D^2=I_geom tensor (L_h-L_h^2/4)",
        "character_form": "Delta(theta)=(cos(theta)-1)I-sin(theta)J",
        "character_norm_square": "Delta(theta)^T Delta(theta)=4 sin^2(theta/2) I",
        "C8_character_rows": rows,
        "forward_difference_zero_modes_m": forward_zero_modes,
        "odd_current_zero_modes_m": current_zero_modes,
        "small_theta": {
            "even_scalar_part_cos_minus_1": str(scalar_series),
            "directed_J_coefficient_minus_sin": str(orient_series),
            "laplacian_eigenvalue": str(lap_series),
        },
        "checks": checks,
        "doubler_correction": (
            "The symmetric Hermitian current sin(theta) has an additional finite-lattice zero at theta=pi. "
            "The complete directed difference W-I contains the even (cos(theta)-1)I term automatically, and its norm square has only the trivial C8 zero. This is Wilson-like algebraically but is not a claim of a derived Wilson-fermion action."
        ),
        "interpretation": (
            "Within the already-derived minimal reversible history carrier, resolving geometry orientation provides an exact first-order directed difference whose positive square is the ordinary orientation-unresolved graph Laplacian. In the small-angle sector the leading term is proportional to the real complex structure J, while the scalar correction starts at second order."
        ),
        "claim_boundary": (
            "Exact finite-dimensional kinematics/representation theory only. The history index is not identified with physical time; Delta_W is not claimed to be the physical Dirac operator; no fermion, spin-statistics theorem, mass term, Standard-Model matter sector, or physical dispersion relation is derived here."
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
