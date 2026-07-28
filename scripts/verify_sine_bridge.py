#!/usr/bin/env python3
"""Dependency-free checks for the exact sine spectral bridge.

This verifies identities of the finite periodic lattice model. It does not
claim empirical validation of CIMFIG or of quantum gravity.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

TOL = 2e-14


def laplacian_symbol(momentum: tuple[float, ...]) -> float:
    return 4.0 * sum(math.sin(k / 2.0) ** 2 for k in momentum)


def incidence_norm(momentum: tuple[float, ...]) -> float:
    return sum(abs(complex(math.cos(k), math.sin(k)) - 1.0) ** 2 for k in momentum)


def transfer_matrix(lam: float) -> tuple[tuple[float, float], tuple[float, float]]:
    return ((1.0 - lam / 2.0, 1.0),
            (-lam * (1.0 - lam / 4.0), 1.0 - lam / 2.0))


def determinant(matrix: tuple[tuple[float, float], tuple[float, float]]) -> float:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def run_checks() -> dict[str, object]:
    samples = ((0.13,), (0.31, -0.22, 0.17),
               (math.pi / 7.0, math.pi / 9.0, -math.pi / 11.0))
    identity_errors = [abs(incidence_norm(k) - laplacian_symbol(k)) for k in samples]
    dispersion_errors: list[float] = []
    determinant_errors: list[float] = []
    phases: list[float] = []
    for momentum in samples:
        lam = laplacian_symbol(momentum)
        if lam > 4.0:
            continue
        omega = 2.0 * math.asin(math.sqrt(lam) / 2.0)
        phases.append(omega)
        dispersion_errors.append(abs(math.sin(omega / 2.0) ** 2 - lam / 4.0))
        determinant_errors.append(abs(determinant(transfer_matrix(lam)) - 1.0))

    direction = (0.7, -0.4, 0.2)
    norm2 = sum(x * x for x in direction)
    continuum = []
    for scale in (0.5, 0.25, 0.125, 0.0625):
        momentum = tuple(scale * x for x in direction)
        continuum.append({
            "scale": scale,
            "lambda_over_k2": laplacian_symbol(momentum) / (scale * scale * norm2),
        })

    checks = {
        "incidence_laplacian_identity": max(identity_errors) < TOL,
        "exact_sine_dispersion": max(dispersion_errors) < TOL,
        "symplectic_determinant": max(determinant_errors) < TOL,
        "continuum_error_decreases": all(
            abs(1.0 - continuum[i + 1]["lambda_over_k2"])
            < abs(1.0 - continuum[i]["lambda_over_k2"])
            for i in range(len(continuum) - 1)
        ),
    }
    return {
        "scope": "exact finite periodic-lattice identities",
        "checks": checks,
        "passed": all(checks.values()),
        "max_incidence_identity_error": max(identity_errors),
        "max_dispersion_error": max(dispersion_errors),
        "max_transfer_determinant_error": max(determinant_errors),
        "stable_phases": phases,
        "continuum_sequence": continuum,
        "physical_validation": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, help="Optional JSON output path")
    args = parser.parse_args()
    result = run_checks()
    payload = json.dumps(result, ensure_ascii=False, indent=2)
    print(payload)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + "\n", encoding="utf-8")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
