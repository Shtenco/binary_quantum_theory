#!/usr/bin/env python3
"""Gauge-covariant map: one qubit per oriented face -> adjoint B coefficients.

A qubit density matrix supplies three real Pauli expectation values (its Bloch
vector).  Under SU(2) conjugation this vector transforms in the SO(3) adjoint.
Combined with the oriented 2-cell carrying the qubit, this is the minimal local
algebra needed for an adjoint-valued discrete 2-form coefficient B_f^i.

The finite test verifies:
  * SU(2) conjugation -> SO(3) Bloch-vector covariance;
  * gauge-covariant parallel transport of many face qubits to a block frame;
  * independence from arbitrary local face-frame choices.

It does not define a microscopic dynamics or derive Plebanski simplicity.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


I2 = np.eye(2, dtype=complex)
PAULI = np.array([
    [[0, 1], [1, 0]],
    [[0, -1j], [1j, 0]],
    [[1, 0], [0, -1]],
], dtype=complex)


def random_su2(rng: np.random.Generator) -> np.ndarray:
    q = rng.normal(size=4)
    q /= np.linalg.norm(q)
    a, b, c, d = q
    return np.array([
        [a + 1j * d, c + 1j * b],
        [-c + 1j * b, a - 1j * d],
    ], dtype=complex)


def random_density(rng: np.random.Generator) -> np.ndarray:
    direction = rng.normal(size=3)
    direction /= np.linalg.norm(direction)
    radius = rng.uniform(0.05, 0.98)
    rho = 0.5 * I2.copy()
    for i in range(3):
        rho += 0.5 * radius * direction[i] * PAULI[i]
    return rho


def bloch(rho: np.ndarray) -> np.ndarray:
    return np.array([np.trace(rho @ PAULI[i]).real for i in range(3)])


def adjoint_so3(U: np.ndarray) -> np.ndarray:
    R = np.zeros((3, 3), dtype=float)
    for i in range(3):
        for j in range(3):
            R[i, j] = 0.5 * np.trace(
                PAULI[i] @ U @ PAULI[j] @ U.conj().T
            ).real
    return R


def transport_density(P: np.ndarray, rho: np.ndarray) -> np.ndarray:
    return P @ rho @ P.conj().T


def run(seed: int = 260809, faces: int = 17, trials: int = 32) -> dict[str, object]:
    rng = np.random.default_rng(seed)
    max_single_covariance = 0.0
    max_rotation_orthogonality = 0.0
    max_rotation_determinant = 0.0
    max_block_covariance = 0.0
    max_block_norm_invariance = 0.0

    single_rows = []
    block_rows = []

    for trial in range(trials):
        rho = random_density(rng)
        U = random_su2(rng)
        R = adjoint_so3(U)
        lhs = bloch(transport_density(U, rho))
        rhs = R @ bloch(rho)
        covariance = float(np.linalg.norm(lhs - rhs))
        orthogonality = float(np.linalg.norm(R.T @ R - np.eye(3)))
        determinant_error = abs(float(np.linalg.det(R)) - 1.0)
        max_single_covariance = max(max_single_covariance, covariance)
        max_rotation_orthogonality = max(max_rotation_orthogonality, orthogonality)
        max_rotation_determinant = max(max_rotation_determinant, determinant_error)
        single_rows.append({
            "trial": trial,
            "bloch_covariance_error": covariance,
            "SO3_orthogonality_error": orthogonality,
            "SO3_determinant_error": determinant_error,
        })

        # Each face has a local density matrix, an oriented combinatorial weight,
        # and an SU(2) transport P_f from its local frame to the block frame.
        rhos = [random_density(rng) for _ in range(faces)]
        transports = [random_su2(rng) for _ in range(faces)]
        orientation_weights = rng.choice(np.array([-1.0, 1.0]), size=faces)

        block = np.zeros(3)
        for w, P, rf in zip(orientation_weights, transports, rhos):
            block += w * bloch(transport_density(P, rf))

        # Independent arbitrary local gauge rotations g_f and one block-frame
        # rotation G.  Transport convention: P_f -> G P_f g_f^dagger.
        local_gauge = [random_su2(rng) for _ in range(faces)]
        G = random_su2(rng)
        RG = adjoint_so3(G)

        transformed_block = np.zeros(3)
        for w, P, rf, gf in zip(orientation_weights, transports, rhos, local_gauge):
            rho_g = gf @ rf @ gf.conj().T
            P_g = G @ P @ gf.conj().T
            transformed_block += w * bloch(transport_density(P_g, rho_g))

        block_covariance = float(np.linalg.norm(transformed_block - RG @ block))
        norm_invariance = abs(float(np.linalg.norm(transformed_block) - np.linalg.norm(block)))
        max_block_covariance = max(max_block_covariance, block_covariance)
        max_block_norm_invariance = max(max_block_norm_invariance, norm_invariance)
        block_rows.append({
            "trial": trial,
            "faces": faces,
            "block_covariance_error": block_covariance,
            "block_norm_invariance_error": norm_invariance,
        })

    passed = (
        max_single_covariance < 1e-12
        and max_rotation_orthogonality < 1e-12
        and max_rotation_determinant < 1e-12
        and max_block_covariance < 1e-11
        and max_block_norm_invariance < 1e-11
    )

    return {
        "status": "finite algebraic face-qubit -> adjoint B coefficient gate",
        "passed": bool(passed),
        "seed": seed,
        "trials": trials,
        "faces_per_block": faces,
        "max_errors": {
            "single_qubit_SU2_to_SO3_covariance": max_single_covariance,
            "adjoint_SO3_orthogonality": max_rotation_orthogonality,
            "adjoint_SO3_determinant": max_rotation_determinant,
            "gauge_covariant_blocking": max_block_covariance,
            "block_norm_gauge_invariance": max_block_norm_invariance,
        },
        "single_rows": single_rows,
        "block_rows": block_rows,
        "microscopic_interpretation": {
            "face_carrier": "one qubit density operator rho_f on each oriented microscopic 2-cell",
            "internal_coefficients": "b_f^i = Tr(rho_f sigma^i)",
            "edge_transport": "SU(2) parallel transport to a chosen block frame",
            "coarse_object": "adjoint-valued discrete 2-form coefficients; geometric area/metric is not inserted",
        },
        "scope_note": "This is gauge covariance of a candidate blocking variable, not a microscopic rewrite law and not evidence that simplicity or four-dimensional geometry emerges.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=260809)
    parser.add_argument("--faces", type=int, default=17)
    parser.add_argument("--trials", type=int, default=32)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.faces < 1 or args.trials < 1:
        parser.error("faces and trials must be positive")
    result = run(args.seed, args.faces, args.trials)
    text = json.dumps(result, ensure_ascii=False, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
