#!/usr/bin/env python3
"""Finite exact/numerical regression for the coarse Feshbach and K/A/B identities.

This gate is deliberately model-independent. It verifies on deterministic
Hermitian matrices and non-orthonormal coarse carriers that

  Gc(z) = Q0^dag (z-H)^-1 Q0

is the inverse of the Feshbach Schur complement, and that the first block-
Lanczos residual obtained from K/A/B is

  B1^dag B1 = K^-1/2 [B - A^dag K^-1 A] K^-1/2.

It certifies the algebra used to interpret the production Peter-Weyl moments;
it does not supply BCQG microscopic coefficients.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

TOL = 2e-11


def invsqrt(M: np.ndarray) -> np.ndarray:
    """Hermitian positive-definite inverse square root."""
    w, U = np.linalg.eigh((M + M.conj().T) / 2)
    if float(np.min(w)) <= 0.0:
        raise ValueError("Gram not positive")
    return (U * (1.0 / np.sqrt(w))) @ U.conj().T


def run(seed: int = 260817) -> dict:
    rng = np.random.default_rng(seed)
    n = 13
    m = 4

    X = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    H = (X + X.conj().T) / 2
    V = rng.normal(size=(n, m)) + 1j * rng.normal(size=(n, m))

    K = V.conj().T @ V
    Ki2 = invsqrt(K)
    Q0 = V @ Ki2
    orth = np.linalg.norm(Q0.conj().T @ Q0 - np.eye(m))
    Pc = Q0 @ Q0.conj().T

    # Null space of Q0^dag gives an orthonormal complement without relying on
    # how complete QR chooses/rotates the first block.
    _, _, vh = np.linalg.svd(Q0.conj().T, full_matrices=True)
    W = vh.conj().T[:, m:]
    comp_orth = max(
        np.linalg.norm(W.conj().T @ W - np.eye(n - m)),
        np.linalg.norm(Q0.conj().T @ W),
    )

    z = 2.3 + 0.7j

    # Use linear solves rather than explicit matrix inverses. This is the same
    # algebraic identity, but it is substantially more stable across LAPACK /
    # NumPy builds and makes the regression about the identity rather than
    # inversion roundoff.
    zI_minus_H = z * np.eye(n) - H
    G = Q0.conj().T @ np.linalg.solve(zI_minus_H, Q0)

    Hpp = Q0.conj().T @ H @ Q0
    Hpq = Q0.conj().T @ H @ W
    Hqq = W.conj().T @ H @ W
    zI_minus_Hqq = z * np.eye(n - m) - Hqq
    C = (
        z * np.eye(m)
        - Hpp
        - Hpq @ np.linalg.solve(zI_minus_Hqq, Hpq.conj().T)
    )
    Ginv = np.linalg.solve(G, np.eye(m))
    fesh = np.linalg.norm(Ginv - C) / np.linalg.norm(C)

    A = V.conj().T @ H @ V
    B = (H @ V).conj().T @ (H @ V)
    kab = Ki2 @ (B - A.conj().T @ np.linalg.solve(K, A)) @ Ki2
    R = (np.eye(n) - Pc) @ H @ Q0
    direct = R.conj().T @ R
    kry = np.linalg.norm(kab - direct) / max(np.linalg.norm(direct), 1e-30)
    herm = max(
        np.linalg.norm(A - A.conj().T),
        np.linalg.norm(kab - kab.conj().T),
    )
    mineig = float(np.min(np.linalg.eigvalsh((kab + kab.conj().T) / 2)))

    # json.dumps does not serialize numpy.bool_. Cast every gate result to a
    # native Python bool so a passing scientific calculation cannot fail while
    # writing CI evidence.
    checks = {
        "coarse_orthonormalization": bool(orth < TOL),
        "complement_orthonormalization": bool(comp_orth < TOL),
        "Feshbach_equals_inverse_projected_resolvent": bool(fesh < TOL),
        "KAB_equals_first_block_Lanczos_residual": bool(kry < TOL),
        "Hermitian_moments": bool(herm < TOL),
        "residual_Gram_positive_semidefinite": bool(mineig > -TOL),
    }

    return {
        "status": "finite regression of exact Feshbach and block-Krylov identities",
        "passed": bool(all(checks.values())),
        "science_status": "ALGEBRAIC_IDENTITY_REGRESSION",
        "dimension": n,
        "coarse_dimension": m,
        "z": [float(z.real), float(z.imag)],
        "coarse_orthonormality_error": float(orth),
        "complement_error": float(comp_orth),
        "Feshbach_relative_error": float(fesh),
        "KAB_block_Lanczos_relative_error": float(kry),
        "Hermiticity_error": float(herm),
        "B1dagB1_min_eigenvalue": mineig,
        "condition_numbers": {
            "zI_minus_H": float(np.linalg.cond(zI_minus_H)),
            "zI_minus_Hqq": float(np.linalg.cond(zI_minus_Hqq)),
            "projected_resolvent_G": float(np.linalg.cond(G)),
            "Gram_K": float(np.linalg.cond(K)),
        },
        "checks": checks,
        "scope_note": (
            "Checks the operator algebra only. BCQG K/A/B and interblock "
            "amplitudes remain microscopic outputs."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = run()
    text = json.dumps(result, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
