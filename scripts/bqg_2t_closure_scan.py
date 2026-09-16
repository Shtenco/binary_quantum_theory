#!/usr/bin/env python3
"""Falsification-first BQG -> Sp(2,R) closure scanner.

The script intentionally does not construct Bars constraints for the user.
It accepts an independently defined finite operator basis and asks whether a
three-dimensional subspace closes as sl(2,R) ~= sp(2,R).

Input JSON format:
{
  "operators": {"name": [[...], ...], ...},
  "hbar": 1.0,
  "tolerance": 1e-10,
  "commutator_convention": "quantum_i"
}

`quantum_i` means [A,B]/(i*hbar)=f*C.
`lie` means [A,B]/hbar=f*C and is useful for non-Hermitian matrix
representations of the abstract Lie algebra. The convention is never inferred.

The scan is deliberately conservative: candidates are linear combinations
only of the supplied operators. No optimization over arbitrary nonlinear
operators is performed.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import numpy as np


def comm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def frob(a: np.ndarray) -> float:
    return float(np.linalg.norm(a, ord="fro"))


def orthonormal_basis(vectors: list[np.ndarray], tol: float) -> list[np.ndarray]:
    out: list[np.ndarray] = []
    for v in vectors:
        w = v.astype(complex, copy=True)
        for q in out:
            w -= np.vdot(q, w) * q
        n = np.linalg.norm(w)
        if n > tol:
            out.append(w / n)
    return out


def project_coefficients(x: np.ndarray, basis: list[np.ndarray]) -> tuple[np.ndarray, float]:
    coeff = np.array([np.vdot(b, x) for b in basis], dtype=complex)
    residual = x - sum(c * b for c, b in zip(coeff, basis))
    return coeff, frob(residual)


def analyze_triplet(
    triplet: list[np.ndarray],
    names: list[str],
    tol: float,
    hbar: float,
    convention: str,
) -> dict:
    q = orthonormal_basis(triplet, tol)
    if len(q) != 3:
        return {"rank": len(q), "accepted_as_sp2": False, "reason": "triplet is linearly dependent"}

    divisor = 1j * hbar if convention == "quantum_i" else hbar
    f = np.zeros((3, 3, 3), dtype=float)
    max_res = 0.0
    max_imag_coeff = 0.0

    for i, j in itertools.product(range(3), repeat=2):
        c = comm(q[i], q[j]) / divisor
        coeff, res = project_coefficients(c, q)
        max_res = max(max_res, res)
        max_imag_coeff = max(max_imag_coeff, float(np.max(np.abs(np.imag(coeff)))))
        f[i, j, :] = np.real(coeff)

    # Jacobi residual on the actual matrices. This is a representation check,
    # independent of whether the chosen structure constants are subsequently
    # recognized as sl(2,R).
    jacobi_max = 0.0
    for i, j, k in itertools.product(range(3), repeat=3):
        jac = (
            comm(q[i], comm(q[j], q[k]))
            + comm(q[j], comm(q[k], q[i]))
            + comm(q[k], comm(q[i], q[j]))
        )
        jacobi_max = max(jacobi_max, frob(jac))

    # Adjoint matrices: (ad_i)_j^k = f_{ij}^k.
    ad = [f[i] for i in range(3)]
    K = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            K[i, j] = np.trace(ad[i] @ ad[j])
    evals = np.linalg.eigvalsh((K + K.T) / 2)
    npos = int(np.sum(evals > tol))
    nneg = int(np.sum(evals < -tol))
    nzero = 3 - npos - nneg

    accepted = (
        max_res <= tol
        and jacobi_max <= tol
        and max_imag_coeff <= tol
        and npos == 2
        and nneg == 1
    )
    return {
        "names": names,
        "rank": 3,
        "max_closure_residual": max_res,
        "max_jacobi_residual": jacobi_max,
        "max_imaginary_structure_component": max_imag_coeff,
        "structure_constants": f.tolist(),
        "killing_eigenvalues": evals.tolist(),
        "killing_signature": [npos, nneg, nzero],
        "accepted_as_sp2": accepted,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("--tolerance", type=float, default=None)
    ap.add_argument("--hbar", type=float, default=None)
    ap.add_argument("--convention", choices=["quantum_i", "lie"], default=None)
    args = ap.parse_args()

    data = json.loads(args.input.read_text(encoding="utf-8"))
    tol = float(args.tolerance if args.tolerance is not None else data.get("tolerance", 1e-10))
    hbar = float(args.hbar if args.hbar is not None else data.get("hbar", 1.0))
    convention = args.convention or data.get("commutator_convention", "quantum_i")
    if convention not in {"quantum_i", "lie"}:
        raise SystemExit("commutator_convention must be 'quantum_i' or 'lie'")

    names = list(data["operators"])
    ops = [np.asarray(data["operators"][n], dtype=complex) for n in names]
    if not ops:
        raise SystemExit("No operators supplied")
    shape = ops[0].shape
    if len(shape) != 2 or shape[0] != shape[1]:
        raise SystemExit("Operators must be square matrices")
    if any(o.shape != shape for o in ops):
        raise SystemExit("All operators must have the same shape")

    results = []
    if len(ops) >= 3:
        for idx in itertools.combinations(range(len(ops)), 3):
            results.append(
                analyze_triplet(
                    [ops[i] for i in idx],
                    [names[i] for i in idx],
                    tol,
                    hbar,
                    convention,
                )
            )

    accepted = [r for r in results if r.get("accepted_as_sp2")]
    out = {
        "operator_names": names,
        "matrix_dimension": shape[0],
        "tolerance": tol,
        "hbar": hbar,
        "commutator_convention": convention,
        "triplets_tested": len(results),
        "sp2_triplets": accepted,
        "best_residual": min((r.get("max_closure_residual", float("inf")) for r in results), default=None),
        "verdict": "POSITIVE_CANDIDATE" if accepted else "NO_SP2_TRIPLET_IDENTIFIED",
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
