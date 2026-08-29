#!/usr/bin/env python3
"""Independent Bell/CHSH kinematics regression for the q=2 carrier.

This gate checks only standard two-qubit quantum kinematics: Pauli observables,
the singlet correlator E(a,b)=-a.b, CHSH violation, and the Tsirelson bound.
It is deliberately independent of BCQG geometry/gravity dynamics and therefore
must not be interpreted as deriving nonlocality from the microscopic model.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

TOL = 2e-12
SQRT2 = float(np.sqrt(2.0))

SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def observable(direction: np.ndarray) -> np.ndarray:
    n = np.asarray(direction, dtype=float)
    norm = float(np.linalg.norm(n))
    if norm <= 0.0:
        raise ValueError("measurement direction must be nonzero")
    n = n / norm
    return n[0] * SX + n[1] * SY + n[2] * SZ


def expectation(state: np.ndarray, operator: np.ndarray) -> complex:
    return np.vdot(state, operator @ state)


def correlator(state: np.ndarray, a: np.ndarray, b: np.ndarray) -> float:
    value = expectation(state, np.kron(observable(a), observable(b)))
    if abs(float(value.imag)) > TOL:
        raise ValueError("correlator acquired an unphysical imaginary component")
    return float(value.real)


def run(seed: int = 260830, random_trials: int = 128) -> dict:
    zero = np.array([1.0, 0.0], dtype=complex)
    one = np.array([0.0, 1.0], dtype=complex)
    singlet = (np.kron(zero, one) - np.kron(one, zero)) / SQRT2

    state_norm_error = abs(float(np.vdot(singlet, singlet).real) - 1.0)

    canonical_axes = [
        np.array([1.0, 0.0, 0.0]),
        np.array([0.0, 1.0, 0.0]),
        np.array([0.0, 0.0, 1.0]),
    ]

    hermiticity_error = 0.0
    involution_error = 0.0
    local_mean_error = 0.0
    correlator_error = 0.0

    for n in canonical_axes:
        A = observable(n)
        hermiticity_error = max(hermiticity_error, float(np.linalg.norm(A - A.conj().T)))
        involution_error = max(involution_error, float(np.linalg.norm(A @ A - I2)))
        local_mean_error = max(
            local_mean_error,
            abs(float(expectation(singlet, np.kron(A, I2)).real)),
            abs(float(expectation(singlet, np.kron(I2, A)).real)),
        )

    rng = np.random.default_rng(seed)
    for _ in range(random_trials):
        a = rng.normal(size=3)
        b = rng.normal(size=3)
        a = a / np.linalg.norm(a)
        b = b / np.linalg.norm(b)
        A = observable(a)
        B = observable(b)
        hermiticity_error = max(
            hermiticity_error,
            float(np.linalg.norm(A - A.conj().T)),
            float(np.linalg.norm(B - B.conj().T)),
        )
        involution_error = max(
            involution_error,
            float(np.linalg.norm(A @ A - I2)),
            float(np.linalg.norm(B @ B - I2)),
        )
        correlator_error = max(
            correlator_error,
            abs(correlator(singlet, a, b) + float(np.dot(a, b))),
        )

    # Standard optimal CHSH directions. With our sign convention the singlet
    # yields -2*sqrt(2), so the physically relevant quantity is |S|.
    a = np.array([1.0, 0.0, 0.0])
    a_prime = np.array([0.0, 0.0, 1.0])
    b = (a + a_prime) / SQRT2
    b_prime = (a - a_prime) / SQRT2

    A = observable(a)
    Ap = observable(a_prime)
    B = observable(b)
    Bp = observable(b_prime)
    chsh_operator = (
        np.kron(A, B)
        + np.kron(A, Bp)
        + np.kron(Ap, B)
        - np.kron(Ap, Bp)
    )
    chsh_value = float(expectation(singlet, chsh_operator).real)
    chsh_abs = abs(chsh_value)
    tsirelson = 2.0 * SQRT2
    chsh_operator_norm = float(np.linalg.norm(chsh_operator, 2))
    chsh_hermiticity_error = float(np.linalg.norm(chsh_operator - chsh_operator.conj().T))
    chsh_spectrum = [float(x) for x in np.linalg.eigvalsh(chsh_operator)]

    checks = {
        "singlet_normalized": bool(state_norm_error < TOL),
        "spin_observables_Hermitian": bool(hermiticity_error < TOL),
        "spin_observables_square_to_identity": bool(involution_error < TOL),
        "singlet_local_means_zero": bool(local_mean_error < TOL),
        "singlet_correlator_equals_minus_a_dot_b": bool(correlator_error < TOL),
        "CHSH_classical_bound_is_violated": bool(chsh_abs > 2.0 + 1e-12),
        "optimal_CHSH_reaches_Tsirelson": bool(abs(chsh_abs - tsirelson) < TOL),
        "CHSH_operator_obeys_Tsirelson_bound": bool(chsh_operator_norm <= tsirelson + TOL),
        "CHSH_operator_Hermitian": bool(chsh_hermiticity_error < TOL),
    }

    return {
        "status": "independent Bell/CHSH two-qubit kinematics regression",
        "passed": bool(all(checks.values())),
        "science_status": "STANDARD_QM_KINEMATICS_REGRESSION",
        "random_trials": int(random_trials),
        "seed": int(seed),
        "tolerance": TOL,
        "state_norm_error": float(state_norm_error),
        "observable_Hermiticity_error": float(hermiticity_error),
        "observable_involution_error": float(involution_error),
        "singlet_local_mean_error": float(local_mean_error),
        "singlet_correlator_max_error": float(correlator_error),
        "CHSH_value": float(chsh_value),
        "CHSH_absolute_value": float(chsh_abs),
        "classical_CHSH_bound": 2.0,
        "Tsirelson_bound": float(tsirelson),
        "CHSH_operator_norm": float(chsh_operator_norm),
        "CHSH_operator_Hermiticity_error": float(chsh_hermiticity_error),
        "CHSH_operator_spectrum": chsh_spectrum,
        "checks": checks,
        "scope_note": (
            "This gate validates standard two-qubit quantum kinematics on the q=2 carrier. "
            "It does not derive the singlet, Bell nonlocality, geometry, gravity, or BCQG "
            "dynamics from microscopic coefficients."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--seed", type=int, default=260830)
    parser.add_argument("--random-trials", type=int, default=128)
    args = parser.parse_args()

    result = run(seed=args.seed, random_trials=args.random_trials)
    text = json.dumps(result, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
