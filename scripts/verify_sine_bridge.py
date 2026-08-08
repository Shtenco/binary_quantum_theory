#!/usr/bin/env python3
"""Dependency-free checks for the exact sine spectral bridge.

This verifies identities of the finite periodic lattice model. It does not
claim empirical validation of CIMFIG or of quantum gravity.
"""

from __future__ import annotations

import argparse
import itertools
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


def torus_spectrum(size: int, dimension: int) -> list[float]:
    """Return the exact Fourier spectrum of the periodic cubic graph."""
    momenta = (2.0 * math.pi * n / size for n in range(size))
    axis = tuple(momenta)
    return sorted(laplacian_symbol(k) for k in itertools.product(axis, repeat=dimension))


def run_checks(size: int = 7, dimension: int = 3) -> dict[str, object]:
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

    fourth_order_limit = sum(x ** 4 for x in direction) / (12.0 * norm2)
    fourth_order_sequence = [
        (1.0 - row["lambda_over_k2"]) / row["scale"] ** 2
        for row in continuum
    ]

    spectrum = torus_spectrum(size, dimension)
    vertex_count = size ** dimension
    expected_gap = 4.0 * math.sin(math.pi / size) ** 2
    nonzero = [value for value in spectrum if value > TOL]
    gap_multiplicity = sum(abs(value - expected_gap) < TOL for value in spectrum)
    heat_times = (0.1, 0.3, 1.0, 3.0)
    heat_trace = [sum(math.exp(-time * value) for value in spectrum)
                  for time in heat_times]
    axis_spectrum = torus_spectrum(size, 1)
    factorized_heat_trace = [
        sum(math.exp(-time * value) for value in axis_spectrum) ** dimension
        for time in heat_times
    ]
    heat_factorization_error = max(
        abs(direct - factorized)
        for direct, factorized in zip(heat_trace, factorized_heat_trace)
    )
    expected_trace = 2.0 * dimension * vertex_count
    # Kirchhoff's matrix-tree theorem in log form avoids overflow.
    log_spanning_trees = sum(math.log(value) for value in nonzero) - math.log(vertex_count)

    checks = {
        "incidence_laplacian_identity": max(identity_errors) < TOL,
        "exact_sine_dispersion": max(dispersion_errors) < TOL,
        "symplectic_determinant": max(determinant_errors) < TOL,
        "continuum_error_decreases": all(
            abs(1.0 - continuum[i + 1]["lambda_over_k2"])
            < abs(1.0 - continuum[i]["lambda_over_k2"])
            for i in range(len(continuum) - 1)
        ),
        "fourth_order_coefficient": abs(fourth_order_sequence[-1] - fourth_order_limit) < 2e-5,
        "torus_mode_count": len(spectrum) == size ** dimension,
        "unique_zero_mode": sum(value < TOL for value in spectrum) == 1,
        "torus_spectral_gap": abs(nonzero[0] - expected_gap) < TOL,
        "gap_multiplicity": gap_multiplicity == 2 * dimension,
        "laplacian_trace_sum_rule": abs(sum(spectrum) - expected_trace) < TOL * vertex_count,
        "spectral_upper_bound": spectrum[-1] <= 4.0 * dimension + TOL,
        "heat_trace_monotone": all(heat_trace[i + 1] < heat_trace[i]
                                   for i in range(len(heat_trace) - 1)),
        "heat_trace_factorization": heat_factorization_error < TOL * vertex_count,
        "positive_spanning_tree_count": log_spanning_trees > 0.0,
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
        "fourth_order_target": fourth_order_limit,
        "fourth_order_sequence": fourth_order_sequence,
        "torus": {
            "size": size,
            "dimension": dimension,
            "mode_count": len(spectrum),
            "zero_mode_multiplicity": sum(value < TOL for value in spectrum),
            "spectral_gap": nonzero[0],
            "expected_gap": expected_gap,
            "gap_multiplicity": gap_multiplicity,
            "expected_gap_multiplicity": 2 * dimension,
            "laplacian_trace": sum(spectrum),
            "expected_laplacian_trace": expected_trace,
            "spectral_maximum": spectrum[-1],
            "heat_times": heat_times,
            "heat_trace": heat_trace,
            "factorized_heat_trace": factorized_heat_trace,
            "max_heat_factorization_error": heat_factorization_error,
            "log_spanning_tree_count": log_spanning_trees,
        },
        "physical_validation": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, help="Optional JSON output path")
    parser.add_argument("--size", type=int, default=7, help="Periodic side length")
    parser.add_argument("--dimension", type=int, default=3, help="Torus dimension")
    args = parser.parse_args()
    if args.size < 3 or args.dimension < 1:
        parser.error("--size must be >= 3 and --dimension must be >= 1")
    result = run_checks(args.size, args.dimension)
    payload = json.dumps(result, ensure_ascii=False, indent=2)
    print(payload)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + "\n", encoding="utf-8")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
