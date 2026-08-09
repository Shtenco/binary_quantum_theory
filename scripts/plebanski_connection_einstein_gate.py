#!/usr/bin/env python3
"""Connection-first Plebański control: B -> A_B -> F(A_B) -> Einstein gate.

The positive control is the unit Euclidean 4-sphere in stereographic
coordinates, written only through its self-dual 2-forms B^i.  The compatible
SO(3) connection is solved from D_A B = 0 without supplying a Levi-Civita
connection.  Its curvature is then decomposed into the B/self-dual and
anti-self-dual sectors.

The negative control is a non-Einstein conformally-flat metric.  It has a
perfectly valid simple B^i triple and Urbantke metric, but its compatible
connection has a large anti-self-dual curvature component.  This demonstrates
that metric reconstruction is not equivalent to the Einstein equations.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import numpy as np


def levi_civita(rank: int) -> np.ndarray:
    eps = np.zeros((rank,) * rank, dtype=float)
    for p in itertools.permutations(range(rank)):
        inv = sum(p[i] > p[j] for i in range(rank) for j in range(i + 1, rank))
        eps[p] = -1.0 if inv % 2 else 1.0
    return eps


EPS3 = levi_civita(3)


def wedge_one_forms(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.outer(a, b) - np.outer(b, a)


def flat_dual_bases() -> tuple[np.ndarray, np.ndarray]:
    tetrad = np.eye(4)
    plus = np.zeros((3, 4, 4), dtype=float)
    minus = np.zeros_like(plus)
    for i in range(3):
        plus[i] += wedge_one_forms(tetrad[0], tetrad[i + 1])
        minus[i] += wedge_one_forms(tetrad[0], tetrad[i + 1])
        for j in range(3):
            for k in range(3):
                spatial = 0.5 * EPS3[i, j, k] * wedge_one_forms(
                    tetrad[j + 1], tetrad[k + 1]
                )
                plus[i] += spatial
                minus[i] -= spatial
    return plus, minus


SIGMA_PLUS, SIGMA_MINUS = flat_dual_bases()
TRIPLES = list(itertools.combinations(range(4), 3))
PAIRS = list(itertools.combinations(range(4), 2))


def omega_s4(x: np.ndarray) -> float:
    """Unit S^4 stereographic conformal factor: g = Omega^2 delta."""
    return float(2.0 / (1.0 + np.dot(x, x)))


def omega_non_einstein(x: np.ndarray) -> float:
    """Smooth positive conformal factor chosen to have tracefree Ricci != 0."""
    exponent = 0.15 * (x[0] * x[1] + 0.30 * x[2] ** 2 - 0.20 * x[3])
    return float(np.exp(exponent))


def B_from_omega(x: np.ndarray, omega_fn) -> np.ndarray:
    omega = omega_fn(np.asarray(x, dtype=float))
    return (omega ** 2) * SIGMA_PLUS


def exterior_derivative_B(x: np.ndarray, omega_fn, step: float) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    derivative = np.zeros((4, 3, 4, 4), dtype=float)
    for mu in range(4):
        xp = x.copy(); xm = x.copy()
        xp[mu] += step; xm[mu] -= step
        derivative[mu] = (
            B_from_omega(xp, omega_fn) - B_from_omega(xm, omega_fn)
        ) / (2.0 * step)

    dB = np.zeros((3, len(TRIPLES)), dtype=float)
    for i in range(3):
        for t, (mu, nu, rho) in enumerate(TRIPLES):
            dB[i, t] = (
                derivative[mu, i, nu, rho]
                + derivative[nu, i, rho, mu]
                + derivative[rho, i, mu, nu]
            )
    return dB


def compatible_connection(x: np.ndarray, omega_fn, step: float) -> tuple[np.ndarray, float, float]:
    """Solve dB^i + eps^ijk A^j wedge B^k = 0 for 12 A-components."""
    B = B_from_omega(x, omega_fn)
    dB = exterior_derivative_B(x, omega_fn, step)
    matrix = np.zeros((12, 12), dtype=float)
    rhs = np.zeros(12, dtype=float)

    row = 0
    for i in range(3):
        for t, (mu, nu, rho) in enumerate(TRIPLES):
            rhs[row] = -dB[i, t]
            for j in range(3):
                for a in range(4):
                    value = 0.0
                    for k in range(3):
                        value += EPS3[i, j, k] * (
                            (1.0 if a == mu else 0.0) * B[k, nu, rho]
                            + (1.0 if a == nu else 0.0) * B[k, rho, mu]
                            + (1.0 if a == rho else 0.0) * B[k, mu, nu]
                        )
                    matrix[row, 4 * j + a] = value
            row += 1

    solution = np.linalg.solve(matrix, rhs)
    residual = float(
        np.linalg.norm(matrix @ solution - rhs) / max(np.linalg.norm(rhs), 1e-30)
    )
    return solution.reshape(3, 4), residual, float(np.linalg.cond(matrix))


def curvature_from_B(
    x: np.ndarray,
    omega_fn,
    connection_step: float,
    derivative_step: float,
) -> tuple[np.ndarray, float, float]:
    """Compute F(A_B), deriving A_B locally from B at every sample point."""
    x = np.asarray(x, dtype=float)
    A, compatibility_residual, cond = compatible_connection(x, omega_fn, connection_step)

    dA = np.zeros((4, 3, 4), dtype=float)
    for mu in range(4):
        xp = x.copy(); xm = x.copy()
        xp[mu] += derivative_step; xm[mu] -= derivative_step
        Ap = compatible_connection(xp, omega_fn, connection_step)[0]
        Am = compatible_connection(xm, omega_fn, connection_step)[0]
        dA[mu] = (Ap - Am) / (2.0 * derivative_step)

    F = np.zeros((3, 4, 4), dtype=float)
    for i in range(3):
        for mu in range(4):
            for nu in range(4):
                value = dA[mu, i, nu] - dA[nu, i, mu]
                for j in range(3):
                    for k in range(3):
                        value += EPS3[i, j, k] * A[j, mu] * A[k, nu]
                F[i, mu, nu] = value
    return F, compatibility_residual, cond


def decompose_curvature(F: np.ndarray, x: np.ndarray, omega_fn) -> tuple[np.ndarray, np.ndarray]:
    """F^i = self_coeff[i,j] B^j + anti_coeff[i,j] Bbar^j."""
    omega2 = omega_fn(np.asarray(x, dtype=float)) ** 2
    Bplus = omega2 * SIGMA_PLUS
    Bminus = omega2 * SIGMA_MINUS

    columns = []
    for basis in (Bplus, Bminus):
        for j in range(3):
            columns.append(np.array([basis[j, a, b] for a, b in PAIRS]))
    matrix = np.column_stack(columns)

    coeff = np.zeros((3, 6), dtype=float)
    for i in range(3):
        vector = np.array([F[i, a, b] for a, b in PAIRS])
        coeff[i] = np.linalg.solve(matrix, vector)
    return coeff[:, :3], coeff[:, 3:]


def point_diagnostics(x: np.ndarray, omega_fn, hB: float, hA: float) -> dict[str, object]:
    F, compatibility, cond = curvature_from_B(x, omega_fn, hB, hA)
    self_coeff, anti_coeff = decompose_curvature(F, x, omega_fn)
    self_scalar = np.eye(3) * np.trace(self_coeff) / 3.0
    self_tf = float(np.linalg.norm(self_coeff - self_scalar))
    anti_norm = float(np.linalg.norm(anti_coeff))
    self_norm = float(np.linalg.norm(self_coeff))
    einstein_anti_defect = anti_norm / max(self_norm + anti_norm, 1e-30)
    einstein_self_tf_defect = self_tf / max(self_norm, 1e-30)
    return {
        "x": [float(v) for v in x],
        "compatibility_residual": compatibility,
        "compatibility_condition_number": cond,
        "self_coefficients": self_coeff.tolist(),
        "anti_self_coefficients": anti_coeff.tolist(),
        "anti_self_norm": anti_norm,
        "self_tracefree_norm": self_tf,
        "einstein_anti_defect": float(einstein_anti_defect),
        "einstein_self_tracefree_defect": float(einstein_self_tf_defect),
    }


def run(hB: float = 2e-5, hA: float = 2e-4) -> dict[str, object]:
    points = [
        np.array([0.0, 0.0, 0.0, 0.0]),
        np.array([0.10, 0.20, -0.15, 0.05]),
        np.array([0.30, -0.20, 0.10, 0.25]),
        np.array([-0.25, 0.15, 0.20, -0.10]),
        np.array([0.18, -0.27, -0.12, 0.22]),
    ]

    positive = [point_diagnostics(x, omega_s4, hB, hA) for x in points]
    negative = [point_diagnostics(x, omega_non_einstein, hB, hA) for x in points]

    pos_max_anti = max(row["einstein_anti_defect"] for row in positive)
    pos_max_tf = max(row["einstein_self_tracefree_defect"] for row in positive)
    pos_max_compat = max(row["compatibility_residual"] for row in positive)
    neg_min_anti = min(row["einstein_anti_defect"] for row in negative)

    passed = (
        pos_max_anti < 1e-6
        and pos_max_tf < 1e-6
        and pos_max_compat < 1e-10
        and neg_min_anti > 0.10
    )

    return {
        "status": "finite Euclidean connection-first Einstein control",
        "passed": bool(passed),
        "finite_difference_steps": {"B_derivative": hB, "A_derivative": hA},
        "positive_control_S4": {
            "description": "unit Euclidean 4-sphere in stereographic coordinates; Einstein and conformally flat",
            "max_anti_self_defect": float(pos_max_anti),
            "max_self_tracefree_defect": float(pos_max_tf),
            "max_compatibility_residual": float(pos_max_compat),
            "rows": positive,
        },
        "negative_control_non_Einstein": {
            "description": "simple nondegenerate conformally-flat B field with a non-Einstein conformal factor",
            "min_anti_self_defect": float(neg_min_anti),
            "rows": negative,
        },
        "lesson": "simple B fields and an Urbantke metric are not enough; the compatible-connection curvature must also enter the Einstein self-dual sector",
        "scope_note": "Euclidean finite-difference control. Lorentzian reality conditions, quantum dynamics and emergence from frozen binary variables remain open.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--B-step", type=float, default=2e-5)
    parser.add_argument("--A-step", type=float, default=2e-4)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.B_step <= 0 or args.A_step <= 0:
        parser.error("finite-difference steps must be positive")
    result = run(args.B_step, args.A_step)
    text = json.dumps(result, ensure_ascii=False, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
