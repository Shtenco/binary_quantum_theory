#!/usr/bin/env python3
"""One-data-path control: face qubits -> B -> simplicity -> Urbantke -> A -> F -> Einstein.

This is deliberately an oracle-encoded positive/negative control, NOT a microscopic
geometrogenesis result.  At each sample point the only objects passed into the
reconstruction chain are six qubit density matrices, one for each independent
oriented coordinate 2-face.  The target B field is encoded into their Bloch
vectors and then forgotten.  Downstream code reconstructs B from Pauli
expectation values, checks simplicity, reconstructs the Urbantke conformal
metric, solves D_A B = 0 for the compatible SO(3) connection, computes its
curvature, and tests the Einstein self-duality condition.

Positive control: unit Euclidean S^4 in stereographic coordinates.
Negative control: smooth conformally-flat but non-Einstein metric.

Important: tracefree self-dual F^{ij} is Weyl curvature and is NOT an Einstein
failure.  The generic vacuum Einstein gate is anti-self-dual curvature -> 0,
plus the appropriate trace/cosmological-constant condition.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import numpy as np


def levi(rank: int) -> np.ndarray:
    e = np.zeros((rank,) * rank)
    for p in itertools.permutations(range(rank)):
        inv = sum(p[i] > p[j] for i in range(rank) for j in range(i + 1, rank))
        e[p] = -1.0 if inv % 2 else 1.0
    return e


E3 = levi(3)
E4 = levi(4)
I2 = np.eye(2, dtype=complex)
PAULI = np.array([
    [[0, 1], [1, 0]],
    [[0, -1j], [1j, 0]],
    [[1, 0], [0, -1]],
], dtype=complex)
PAIRS = list(itertools.combinations(range(4), 2))
TRIPLES = list(itertools.combinations(range(4), 3))
ENCODING_SCALE = 4.0


def wedge1(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.outer(a, b) - np.outer(b, a)


def flat_dual_bases() -> tuple[np.ndarray, np.ndarray]:
    e = np.eye(4)
    plus = np.zeros((3, 4, 4)); minus = np.zeros_like(plus)
    for i in range(3):
        plus[i] += wedge1(e[0], e[i + 1])
        minus[i] += wedge1(e[0], e[i + 1])
        for j in range(3):
            for k in range(3):
                s = 0.5 * E3[i, j, k] * wedge1(e[j + 1], e[k + 1])
                plus[i] += s; minus[i] -= s
    return plus, minus


SIGMA_PLUS, SIGMA_MINUS = flat_dual_bases()


def omega_s4(x: np.ndarray) -> float:
    return float(2.0 / (1.0 + np.dot(x, x)))


def omega_non_einstein(x: np.ndarray) -> float:
    return float(np.exp(0.15 * (x[0] * x[1] + 0.30 * x[2] ** 2 - 0.20 * x[3])))


def target_B(x: np.ndarray, omega_fn) -> np.ndarray:
    return omega_fn(np.asarray(x, float)) ** 2 * SIGMA_PLUS


def encode_face_qubits(B: np.ndarray) -> dict[tuple[int, int], np.ndarray]:
    out = {}
    for mu, nu in PAIRS:
        b = B[:, mu, nu] / ENCODING_SCALE
        if np.linalg.norm(b) > 1.0 + 1e-12:
            raise ValueError("Bloch vector exceeds unit ball")
        rho = 0.5 * I2.copy()
        for i in range(3):
            rho += 0.5 * b[i] * PAULI[i]
        if np.linalg.eigvalsh(rho).min() < -1e-12:
            raise ValueError("encoded density matrix is not positive")
        out[(mu, nu)] = rho
    return out


def decode_face_qubits(rhos: dict[tuple[int, int], np.ndarray]) -> np.ndarray:
    B = np.zeros((3, 4, 4))
    for mu, nu in PAIRS:
        b = np.array([np.trace(rhos[(mu, nu)] @ PAULI[i]).real for i in range(3)])
        B[:, mu, nu] = ENCODING_SCALE * b
        B[:, nu, mu] = -B[:, mu, nu]
    return B


def B_from_qubits(x: np.ndarray, omega_fn) -> tuple[np.ndarray, float]:
    exact = target_B(x, omega_fn)
    decoded = decode_face_qubits(encode_face_qubits(exact))
    err = float(np.linalg.norm(decoded - exact) / max(np.linalg.norm(exact), 1e-30))
    return decoded, err


def simplicity(B: np.ndarray) -> tuple[float, np.ndarray]:
    X = 0.25 * np.einsum("abcd,iab,jcd->ij", E4, B, B)
    iso = np.eye(3) * np.trace(X) / 3.0
    return float(np.linalg.norm(X - iso) / max(np.linalg.norm(X), 1e-30)), X


def urbantke(B: np.ndarray) -> np.ndarray:
    U = np.einsum("ijk,abcd,ima,jbc,kdn->mn", E3, E4, B, B, B)
    return 0.5 * (U + U.T)


def detnorm(M: np.ndarray) -> np.ndarray:
    return M / abs(np.linalg.det(M)) ** 0.25


def conformal_error(U: np.ndarray, g: np.ndarray) -> float:
    a, b = detnorm(U), detnorm(g)
    return float(min(np.linalg.norm(a - b), np.linalg.norm(a + b)) / np.linalg.norm(b))


def exterior_dB(x: np.ndarray, omega_fn, h: float) -> np.ndarray:
    derivative = np.zeros((4, 3, 4, 4))
    for mu in range(4):
        xp = x.copy(); xm = x.copy(); xp[mu] += h; xm[mu] -= h
        derivative[mu] = (B_from_qubits(xp, omega_fn)[0] - B_from_qubits(xm, omega_fn)[0]) / (2 * h)
    dB = np.zeros((3, 4))
    for i in range(3):
        for t, (mu, nu, rho) in enumerate(TRIPLES):
            dB[i, t] = derivative[mu, i, nu, rho] + derivative[nu, i, rho, mu] + derivative[rho, i, mu, nu]
    return dB


def compatible_A(x: np.ndarray, omega_fn, h: float) -> tuple[np.ndarray, float, float]:
    B = B_from_qubits(x, omega_fn)[0]
    dB = exterior_dB(x, omega_fn, h)
    M = np.zeros((12, 12)); rhs = np.zeros(12)
    row = 0
    for i in range(3):
        for t, (mu, nu, rho) in enumerate(TRIPLES):
            rhs[row] = -dB[i, t]
            for j in range(3):
                for a in range(4):
                    value = 0.0
                    for k in range(3):
                        value += E3[i, j, k] * (
                            (1.0 if a == mu else 0.0) * B[k, nu, rho]
                            + (1.0 if a == nu else 0.0) * B[k, rho, mu]
                            + (1.0 if a == rho else 0.0) * B[k, mu, nu]
                        )
                    M[row, 4 * j + a] = value
            row += 1
    sol = np.linalg.solve(M, rhs)
    residual = float(np.linalg.norm(M @ sol - rhs) / max(np.linalg.norm(rhs), 1e-30))
    return sol.reshape(3, 4), residual, float(np.linalg.cond(M))


def curvature(x: np.ndarray, omega_fn, hB: float, hA: float) -> tuple[np.ndarray, float, float]:
    A, residual, cond = compatible_A(x, omega_fn, hB)
    dA = np.zeros((4, 3, 4))
    for mu in range(4):
        xp = x.copy(); xm = x.copy(); xp[mu] += hA; xm[mu] -= hA
        dA[mu] = (compatible_A(xp, omega_fn, hB)[0] - compatible_A(xm, omega_fn, hB)[0]) / (2 * hA)
    F = np.zeros((3, 4, 4))
    for i in range(3):
        for mu in range(4):
            for nu in range(4):
                F[i, mu, nu] = dA[mu, i, nu] - dA[nu, i, mu]
                for j in range(3):
                    for k in range(3):
                        F[i, mu, nu] += E3[i, j, k] * A[j, mu] * A[k, nu]
    return F, residual, cond


def decompose(F: np.ndarray, x: np.ndarray, omega_fn) -> tuple[np.ndarray, np.ndarray]:
    scale = omega_fn(x) ** 2
    columns = []
    for basis in (scale * SIGMA_PLUS, scale * SIGMA_MINUS):
        for j in range(3):
            columns.append(np.array([basis[j, a, b] for a, b in PAIRS]))
    M = np.column_stack(columns)
    coeff = np.zeros((3, 6))
    for i in range(3):
        coeff[i] = np.linalg.solve(M, np.array([F[i, a, b] for a, b in PAIRS]))
    return coeff[:, :3], coeff[:, 3:]


def diagnose(x: np.ndarray, omega_fn, hB: float, hA: float) -> dict[str, float | list]:
    B, decode_error = B_from_qubits(x, omega_fn)
    simp, _ = simplicity(B)
    g = omega_fn(x) ** 2 * np.eye(4)  # used ONLY as an external validation target
    metric_error = conformal_error(urbantke(B), g)
    F, compat, cond = curvature(x, omega_fn, hB, hA)
    selfc, antic = decompose(F, x, omega_fn)
    sn, an = np.linalg.norm(selfc), np.linalg.norm(antic)
    return {
        "x": x.tolist(),
        "qubit_decode_error": decode_error,
        "simplicity_defect": simp,
        "urbantke_conformal_metric_error": metric_error,
        "DAB_residual": compat,
        "DAB_condition_number": cond,
        "ASD_defect": float(an / max(sn + an, 1e-30)),
        "trace_F": float(np.trace(selfc)),
        "self_dual_tracefree_norm": float(np.linalg.norm(selfc - np.eye(3) * np.trace(selfc) / 3.0)),
    }


def run(hB: float = 2e-5, hA: float = 2e-4) -> dict[str, object]:
    points = [
        np.array([0.0, 0.0, 0.0, 0.0]),
        np.array([0.10, 0.20, -0.15, 0.05]),
        np.array([0.30, -0.20, 0.10, 0.25]),
        np.array([-0.25, 0.15, 0.20, -0.10]),
        np.array([0.18, -0.27, -0.12, 0.22]),
    ]
    pos = [diagnose(x, omega_s4, hB, hA) for x in points]
    neg = [diagnose(x, omega_non_einstein, hB, hA) for x in points]
    traces = np.array([r["trace_F"] for r in pos], float)
    lambda_rec = float(-np.mean(traces))
    lambda_relative_error = abs(lambda_rec - 3.0) / 3.0
    trace_constancy = float(np.std(traces) / max(abs(np.mean(traces)), 1e-30))

    summary = {
        "max_qubit_decode_error": max(r["qubit_decode_error"] for r in pos),
        "max_simplicity_defect": max(r["simplicity_defect"] for r in pos),
        "max_urbantke_metric_error": max(r["urbantke_conformal_metric_error"] for r in pos),
        "max_DAB_residual": max(r["DAB_residual"] for r in pos),
        "max_ASD_defect": max(r["ASD_defect"] for r in pos),
        "reconstructed_Lambda": lambda_rec,
        "Lambda_relative_error_vs_unit_S4": float(lambda_relative_error),
        "trace_F_constancy_defect": trace_constancy,
        "negative_control_min_ASD_defect": min(r["ASD_defect"] for r in neg),
    }
    passed = (
        summary["max_qubit_decode_error"] < 1e-12
        and summary["max_simplicity_defect"] < 1e-12
        and summary["max_urbantke_metric_error"] < 1e-12
        and summary["max_DAB_residual"] < 1e-10
        and summary["max_ASD_defect"] < 1e-6
        and summary["Lambda_relative_error_vs_unit_S4"] < 1e-6
        and summary["negative_control_min_ASD_defect"] > 0.1
    )
    return {
        "status": "single-data-path oracle control: face qubits -> Einstein",
        "passed": bool(passed),
        "microscopic_rule_derived": False,
        "oracle_encoded_geometry": True,
        "positive_control": {"geometry": "unit Euclidean S4", "rows": pos},
        "negative_control": {"geometry": "simple conformally-flat non-Einstein metric", "rows": neg},
        "summary": summary,
        "interpretation": "All reconstruction arrows after the face-qubit carrier compose correctly on one dataset. This does not show that a frozen rewrite dynamics generates those qubit states or a 4D phase.",
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--B-step", type=float, default=2e-5)
    p.add_argument("--A-step", type=float, default=2e-4)
    p.add_argument("--output", type=Path)
    a = p.parse_args()
    result = run(a.B_step, a.A_step)
    text = json.dumps(result, indent=2, ensure_ascii=False)
    print(text)
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(text + "\n", encoding="utf-8")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
