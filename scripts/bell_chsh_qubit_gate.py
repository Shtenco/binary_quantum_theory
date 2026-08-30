#!/usr/bin/env python3
"""Independent Bell/CHSH reference control for the q=2 two-qubit Hilbert carrier.

This gate reuses the exact Pauli convention already present in
``su2_quantum_link_two_qubit_gate.py`` and checks standard two-qubit quantum
kinematics: Pauli algebra, singlet SU(2) invariance, the correlation tensor,
CHSH violation, the Horodecki optimum and the Tsirelson operator bound.

It is deliberately NOT a derivation of Bell nonlocality from BCQG dynamics.
In particular, it does not identify the two tensor factors with separated
physical BCQG subsystems and does not derive singlet preparation, measurement
locality or Born probabilities from the microscopic model.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

import su2_quantum_link_two_qubit_gate as SPINOR

TOL = 2e-12
SQRT2 = float(np.sqrt(2.0))
I2 = np.asarray(SPINOR.I, dtype=complex)
SIG = tuple(np.asarray(s, dtype=complex) for s in SPINOR.SIG)
EPS = np.asarray(SPINOR.EPS, dtype=int)
ZERO2 = np.zeros((2, 2), dtype=complex)


def observable(direction: np.ndarray) -> np.ndarray:
    """Unit-vector Pauli observable n.sigma using the repository convention."""
    n = np.asarray(direction, dtype=float)
    norm = float(np.linalg.norm(n))
    if norm <= 0.0:
        raise ValueError("measurement direction must be nonzero")
    n = n / norm
    return sum((n[k] * SIG[k] for k in range(3)), start=ZERO2.copy())


def expectation(state: np.ndarray, operator: np.ndarray) -> complex:
    return np.vdot(state, operator @ state)


def correlator(state: np.ndarray, a: np.ndarray, b: np.ndarray) -> float:
    value = expectation(state, np.kron(observable(a), observable(b)))
    if abs(float(value.imag)) > TOL:
        raise ValueError("correlator acquired an unphysical imaginary component")
    return float(value.real)


def chsh_operator(a: np.ndarray, ap: np.ndarray, b: np.ndarray, bp: np.ndarray) -> np.ndarray:
    A = observable(a)
    Ap = observable(ap)
    B = observable(b)
    Bp = observable(bp)
    return np.kron(A, B) + np.kron(A, Bp) + np.kron(Ap, B) - np.kron(Ap, Bp)


def su2_rotation(axis: np.ndarray, angle: float) -> np.ndarray:
    """Spin-1/2 SU(2) rotation exp[-i angle (n.sigma)/2]."""
    n_sigma = observable(axis)
    return np.cos(angle / 2.0) * I2 - 1j * np.sin(angle / 2.0) * n_sigma


def run(seed: int = 260830, random_trials: int = 128, rotation_trials: int = 64) -> dict:
    zero = np.array([1.0, 0.0], dtype=complex)
    one = np.array([0.0, 1.0], dtype=complex)
    singlet = (np.kron(zero, one) - np.kron(one, zero)) / SQRT2

    state_norm_error = abs(float(np.vdot(singlet, singlet).real) - 1.0)

    # Exact Pauli algebra inherited from the SU(2) quantum-link convention.
    pauli_commutator_error = 0.0
    pauli_anticommutator_error = 0.0
    hermiticity_error = 0.0
    involution_error = 0.0
    for i in range(3):
        hermiticity_error = max(
            hermiticity_error,
            float(np.linalg.norm(SIG[i] - SIG[i].conj().T)),
        )
        involution_error = max(
            involution_error,
            float(np.linalg.norm(SIG[i] @ SIG[i] - I2)),
        )
        for j in range(3):
            comm = SIG[i] @ SIG[j] - SIG[j] @ SIG[i]
            comm_target = 2j * sum(
                (EPS[i, j, k] * SIG[k] for k in range(3)),
                start=ZERO2.copy(),
            )
            pauli_commutator_error = max(
                pauli_commutator_error,
                float(np.linalg.norm(comm - comm_target)),
            )
            anti = SIG[i] @ SIG[j] + SIG[j] @ SIG[i]
            anti_target = 2.0 * (1.0 if i == j else 0.0) * I2
            pauli_anticommutator_error = max(
                pauli_anticommutator_error,
                float(np.linalg.norm(anti - anti_target)),
            )

    # Singlet is annihilated by the diagonal total-spin generators and has
    # correlation tensor T_ij = -delta_ij.
    local_mean_error = 0.0
    total_spin_annihilation_error = 0.0
    correlation_tensor = np.zeros((3, 3), dtype=float)
    for i in range(3):
        local_mean_error = max(
            local_mean_error,
            float(abs(expectation(singlet, np.kron(SIG[i], I2)))),
            float(abs(expectation(singlet, np.kron(I2, SIG[i])))),
        )
        total_generator = np.kron(SIG[i], I2) + np.kron(I2, SIG[i])
        total_spin_annihilation_error = max(
            total_spin_annihilation_error,
            float(np.linalg.norm(total_generator @ singlet)),
        )
        for j in range(3):
            value = expectation(singlet, np.kron(SIG[i], SIG[j]))
            if abs(float(value.imag)) > TOL:
                raise ValueError("singlet correlation tensor acquired an imaginary component")
            correlation_tensor[i, j] = float(value.real)
    correlation_tensor_error = float(np.linalg.norm(correlation_tensor + np.eye(3)))

    rng = np.random.default_rng(seed)
    random_correlator_error = 0.0
    random_rotation_error = 0.0
    random_chsh_operator_norm_max = 0.0
    random_tsirelson_excess = 0.0

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
        random_correlator_error = max(
            random_correlator_error,
            abs(correlator(singlet, a, b) + float(np.dot(a, b))),
        )

        ap = rng.normal(size=3)
        bp = rng.normal(size=3)
        op = chsh_operator(a, ap, b, bp)
        op_norm = float(np.linalg.norm(op, 2))
        random_chsh_operator_norm_max = max(random_chsh_operator_norm_max, op_norm)
        random_tsirelson_excess = max(random_tsirelson_excess, op_norm - 2.0 * SQRT2)

    for _ in range(rotation_trials):
        axis = rng.normal(size=3)
        angle = float(rng.uniform(-4.0 * np.pi, 4.0 * np.pi))
        U = su2_rotation(axis, angle)
        random_rotation_error = max(
            random_rotation_error,
            float(np.linalg.norm(np.kron(U, U) @ singlet - singlet)),
            float(np.linalg.norm(U.conj().T @ U - I2)),
            abs(float(np.linalg.det(U).real) - 1.0),
            abs(float(np.linalg.det(U).imag)),
        )

    # Standard optimal CHSH directions for the singlet.
    a = np.array([1.0, 0.0, 0.0])
    ap = np.array([0.0, 0.0, 1.0])
    b = (a + ap) / SQRT2
    bp = (a - ap) / SQRT2
    A = observable(a)
    Ap = observable(ap)
    B = observable(b)
    Bp = observable(bp)
    bell = chsh_operator(a, ap, b, bp)

    chsh_value_complex = expectation(singlet, bell)
    chsh_imaginary_error = abs(float(chsh_value_complex.imag))
    chsh_value = float(chsh_value_complex.real)
    chsh_abs = abs(chsh_value)
    tsirelson = 2.0 * SQRT2
    chsh_operator_norm = float(np.linalg.norm(bell, 2))
    chsh_hermiticity_error = float(np.linalg.norm(bell - bell.conj().T))
    chsh_spectrum = np.linalg.eigvalsh(bell)
    expected_spectrum = np.array([-tsirelson, 0.0, 0.0, tsirelson])
    chsh_spectrum_error = float(np.linalg.norm(chsh_spectrum - expected_spectrum))

    # For dichotomic observables B_CHSH^2 = 4I - [A,A'] tensor [B,B'].
    comm_A = A @ Ap - Ap @ A
    comm_B = B @ Bp - Bp @ B
    tsirelson_identity_error = float(
        np.linalg.norm(bell @ bell - (4.0 * np.eye(4) - np.kron(comm_A, comm_B)))
    )

    # Horodecki two-qubit criterion: S_max = 2 sqrt(m1 + m2), where m1,m2
    # are the two largest eigenvalues of T^T T.
    horodecki_eigenvalues = np.linalg.eigvalsh(correlation_tensor.T @ correlation_tensor)
    horodecki_max_chsh = float(
        2.0 * np.sqrt(horodecki_eigenvalues[-1] + horodecki_eigenvalues[-2])
    )

    checks = {
        "singlet_normalized": bool(state_norm_error < TOL),
        "repository_Pauli_commutators_exact": bool(pauli_commutator_error < TOL),
        "repository_Pauli_anticommutators_exact": bool(pauli_anticommutator_error < TOL),
        "spin_observables_Hermitian": bool(hermiticity_error < TOL),
        "spin_observables_square_to_identity": bool(involution_error < TOL),
        "singlet_local_means_zero": bool(local_mean_error < TOL),
        "singlet_total_spin_zero": bool(total_spin_annihilation_error < TOL),
        "singlet_correlation_tensor_is_minus_identity": bool(correlation_tensor_error < TOL),
        "singlet_random_correlator_equals_minus_a_dot_b": bool(random_correlator_error < TOL),
        "singlet_invariant_under_common_SU2_rotations": bool(random_rotation_error < TOL),
        "CHSH_expectation_real": bool(chsh_imaginary_error < TOL),
        "CHSH_classical_bound_is_violated": bool(chsh_abs > 2.0 + 1e-12),
        "optimal_CHSH_reaches_Tsirelson": bool(abs(chsh_abs - tsirelson) < TOL),
        "CHSH_operator_obeys_Tsirelson_bound": bool(chsh_operator_norm <= tsirelson + TOL),
        "random_CHSH_operators_obey_Tsirelson_bound": bool(random_tsirelson_excess <= TOL),
        "CHSH_operator_Hermitian": bool(chsh_hermiticity_error < TOL),
        "CHSH_optimal_spectrum_matches": bool(chsh_spectrum_error < TOL),
        "Tsirelson_square_identity_holds": bool(tsirelson_identity_error < TOL),
        "Horodecki_optimum_matches_Tsirelson": bool(abs(horodecki_max_chsh - tsirelson) < TOL),
        "optimal_measurement_reaches_Horodecki_bound": bool(abs(chsh_abs - horodecki_max_chsh) < TOL),
    }

    return {
        "status": "standard Bell/CHSH reference control sharing the repository q=2 Pauli convention",
        "passed": bool(all(checks.values())),
        "science_status": "STANDARD_QM_REFERENCE_CONTROL",
        "random_trials": int(random_trials),
        "rotation_trials": int(rotation_trials),
        "seed": int(seed),
        "tolerance": float(TOL),
        "state_norm_error": float(state_norm_error),
        "Pauli_commutator_error": float(pauli_commutator_error),
        "Pauli_anticommutator_error": float(pauli_anticommutator_error),
        "observable_Hermiticity_error": float(hermiticity_error),
        "observable_involution_error": float(involution_error),
        "singlet_local_mean_error": float(local_mean_error),
        "singlet_total_spin_annihilation_error": float(total_spin_annihilation_error),
        "singlet_correlation_tensor": correlation_tensor.tolist(),
        "singlet_correlation_tensor_error": float(correlation_tensor_error),
        "singlet_random_correlator_max_error": float(random_correlator_error),
        "common_SU2_rotation_max_error": float(random_rotation_error),
        "CHSH_value": float(chsh_value),
        "CHSH_absolute_value": float(chsh_abs),
        "classical_CHSH_bound": 2.0,
        "Tsirelson_bound": float(tsirelson),
        "CHSH_operator_norm": float(chsh_operator_norm),
        "random_CHSH_operator_norm_max": float(random_chsh_operator_norm_max),
        "random_Tsirelson_excess_max": float(max(0.0, random_tsirelson_excess)),
        "CHSH_operator_Hermiticity_error": float(chsh_hermiticity_error),
        "CHSH_operator_spectrum": [float(x) for x in chsh_spectrum],
        "CHSH_optimal_spectrum_error": float(chsh_spectrum_error),
        "Tsirelson_square_identity_error": float(tsirelson_identity_error),
        "Horodecki_TtT_eigenvalues": [float(x) for x in horodecki_eigenvalues],
        "Horodecki_max_CHSH": float(horodecki_max_chsh),
        "checks": checks,
        "carrier_relation": (
            "The Pauli matrices are imported from su2_quantum_link_two_qubit_gate.py, "
            "so basis/sign conventions are shared with the repository SU(2) link algebra."
        ),
        "claim_boundary": (
            "This is a standard two-qubit Hilbert/Pauli reference control. It does not "
            "identify Bell parties with physical separated BCQG endpoints; derive the "
            "singlet, Born rule, measurement locality or entanglement from the microscopic "
            "BCQG dynamics; or constitute an experimental Bell test."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--seed", type=int, default=260830)
    parser.add_argument("--random-trials", type=int, default=128)
    parser.add_argument("--rotation-trials", type=int, default=64)
    args = parser.parse_args()

    result = run(
        seed=args.seed,
        random_trials=args.random_trials,
        rotation_trials=args.rotation_trials,
    )
    text = json.dumps(result, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
