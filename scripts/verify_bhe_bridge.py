#!/usr/bin/env python3
"""Exact finite checks for the Bell--Heisenberg--equivalence bridge."""

from __future__ import annotations

import itertools
import json
import math


TOL = 1e-12


def classical_chsh_maximum() -> int:
    values = (-1, 1)
    return max(abs(a0 * (b0 + b1) + a1 * (b0 - b1))
               for a0, a1, b0, b1 in itertools.product(values, repeat=4))


def singlet_correlation(a: float, b: float) -> float:
    return -math.cos(a - b)


def quantum_chsh() -> float:
    a0, a1 = 0.0, math.pi / 2.0
    b0, b1 = math.pi / 4.0, -math.pi / 4.0
    return abs(singlet_correlation(a0, b0) + singlet_correlation(a0, b1)
               + singlet_correlation(a1, b0) - singlet_correlation(a1, b1))


def matmul(a: tuple[tuple[complex, ...], ...],
           b: tuple[tuple[complex, ...], ...]) -> tuple[tuple[complex, ...], ...]:
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def matrix_error(a: tuple[tuple[complex, ...], ...],
                 b: tuple[tuple[complex, ...], ...]) -> float:
    return max(abs(a[i][j] - b[i][j])
               for i in range(len(a)) for j in range(len(a[0])))


def heisenberg_error() -> float:
    # With hbar = omega = 1: H=sigma_z/2 and d sigma_x/dt=-sigma_y.
    h = ((0.5 + 0j, 0j), (0j, -0.5 + 0j))
    sigma_x = ((0j, 1 + 0j), (1 + 0j, 0j))
    sigma_y = ((0j, -1j), (1j, 0j))
    hs, sh = matmul(h, sigma_x), matmul(sigma_x, h)
    derivative = tuple(tuple(1j * (hs[i][j] - sh[i][j]) for j in range(2))
                       for i in range(2))
    target = tuple(tuple(-sigma_y[i][j] for j in range(2)) for i in range(2))
    return matrix_error(derivative, target)


def local_connection_error(alpha: float = 0.37, links: int = 8) -> float:
    # g_n U g_{n+1}^-1 = 1 for U=exp(i alpha), g_n=exp(i n alpha).
    transformed = []
    for n in range(links):
        g_n = complex(math.cos(n * alpha), math.sin(n * alpha))
        u = complex(math.cos(alpha), math.sin(alpha))
        g_next_inverse = complex(math.cos(-(n + 1) * alpha),
                                 math.sin(-(n + 1) * alpha))
        transformed.append(g_n * u * g_next_inverse)
    return max(abs(value - 1.0) for value in transformed)


def main() -> int:
    classical = classical_chsh_maximum()
    quantum = quantum_chsh()
    heisenberg = heisenberg_error()
    local_frame = local_connection_error()
    checks = {
        "classical_chsh_bound": classical == 2,
        "quantum_tsirelson_value": abs(quantum - 2.0 * math.sqrt(2.0)) < TOL,
        "bell_violation": quantum > classical,
        "heisenberg_commutator": heisenberg < TOL,
        "constant_connection_locally_removable": local_frame < TOL,
    }
    result = {
        "checks": checks,
        "passed": all(checks.values()),
        "classical_chsh_maximum": classical,
        "quantum_chsh": quantum,
        "tsirelson_bound": 2.0 * math.sqrt(2.0),
        "heisenberg_matrix_error": heisenberg,
        "local_frame_error": local_frame,
        "scope": "finite identities, not an empirical Bell experiment",
    }
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
