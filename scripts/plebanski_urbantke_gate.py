#!/usr/bin/env python3
"""Plebanski/Urbantke two-form -> metric reconstruction and simplicity gate.

This is a Euclidean finite-dimensional control for a future microscopic
face/diamond-qubit blocking map.  It deliberately separates two statements:

1. a non-degenerate triple of 2-forms can determine an Urbantke conformal metric;
2. the Plebanski simplicity/metricity constraint is an independent condition.

The second point is crucial: an arbitrary GL(3) change of basis of the 2-form
triple leaves the Urbantke conformal metric invariant while generally violating
simplicity.  Therefore metric reconstruction alone must never be counted as a
GR gate.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import numpy as np


def levi_civita(rank: int) -> np.ndarray:
    shape = (rank,) * rank
    eps = np.zeros(shape, dtype=float)
    for p in itertools.permutations(range(rank)):
        inversions = sum(
            p[i] > p[j]
            for i in range(rank)
            for j in range(i + 1, rank)
        )
        eps[p] = -1.0 if inversions % 2 else 1.0
    return eps


EPS3 = levi_civita(3)
EPS4 = levi_civita(4)


def wedge_one_forms(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Components of a wedge b as an antisymmetric 4x4 matrix."""
    return np.outer(a, b) - np.outer(b, a)


def euclidean_self_dual_two_forms(tetrad: np.ndarray) -> np.ndarray:
    """Sigma^i = e^0∧e^i + 1/2 eps^i_jk e^j∧e^k, i=1..3."""
    if tetrad.shape != (4, 4):
        raise ValueError("tetrad must have shape (4,4)")
    if abs(np.linalg.det(tetrad)) < 1e-10:
        raise ValueError("degenerate tetrad")

    B = np.zeros((3, 4, 4), dtype=float)
    for i in range(3):
        B[i] += wedge_one_forms(tetrad[0], tetrad[i + 1])
        for j in range(3):
            for k in range(3):
                B[i] += (
                    0.5
                    * EPS3[i, j, k]
                    * wedge_one_forms(tetrad[j + 1], tetrad[k + 1])
                )
    return B


def wedge_inner_matrix(B: np.ndarray) -> np.ndarray:
    """X^ij where B^i∧B^j = X^ij d^4x in the coordinate orientation."""
    return 0.25 * np.einsum("abcd,iab,jcd->ij", EPS4, B, B)


def simplicity_defect(B: np.ndarray) -> tuple[float, np.ndarray]:
    """Dimensionless traceless part of X^ij = B^i∧B^j."""
    X = wedge_inner_matrix(B)
    trace_part = np.eye(3) * np.trace(X) / 3.0
    defect = np.linalg.norm(X - trace_part) / max(np.linalg.norm(X), 1e-30)
    return float(defect), X


def urbantke_tensor(B: np.ndarray) -> np.ndarray:
    """Unnormalised densitised Urbantke tensor.

    U_mn = eps_ijk eps^abcd B^i_ma B^j_bc B^k_dn.

    For the self-dual convention used here and a tetrad e,
        U_mn = 12 det(e) g_mn.
    The overall sign is an orientation convention.
    """
    U = np.einsum("ijk,abcd,ima,jbc,kdn->mn", EPS3, EPS4, B, B, B)
    return 0.5 * (U + U.T)


def determinant_normalised(metric: np.ndarray) -> np.ndarray:
    det = float(np.linalg.det(metric))
    if abs(det) < 1e-30:
        raise ValueError("degenerate metric tensor")
    return metric / (abs(det) ** 0.25)


def conformal_metric_error(U: np.ndarray, target_metric: np.ndarray) -> float:
    """Compare metrics up to overall nonzero scale/sign."""
    a = determinant_normalised(U)
    b = determinant_normalised(target_metric)
    return float(min(np.linalg.norm(a - b), np.linalg.norm(a + b)) / np.linalg.norm(b))


def random_tetrad(seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    for _ in range(100):
        e = np.eye(4) + 0.25 * rng.normal(size=(4, 4))
        if abs(np.linalg.det(e)) > 0.2:
            if np.linalg.det(e) < 0:
                e[0] *= -1.0
            return e
    raise RuntimeError("failed to generate a nondegenerate tetrad")


def random_so3(rng: np.random.Generator) -> np.ndarray:
    q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    if np.linalg.det(q) < 0:
        q[:, 0] *= -1.0
    return q


def traceless_symmetric_generator(rng: np.random.Generator) -> np.ndarray:
    s = rng.normal(size=(3, 3))
    s = 0.5 * (s + s.T)
    s -= np.eye(3) * np.trace(s) / 3.0
    norm = np.linalg.norm(s)
    if norm < 1e-12:
        raise RuntimeError("degenerate random generator")
    return s / norm


def matrix_exp_symmetric(generator: np.ndarray, alpha: float) -> np.ndarray:
    vals, vecs = np.linalg.eigh(generator)
    return vecs @ np.diag(np.exp(alpha * vals)) @ vecs.T


def run(seeds: int = 8) -> dict[str, object]:
    exact_rows = []
    rotation_rows = []
    distortion_rows = []

    max_exact_metric_error = 0.0
    max_exact_simplicity = 0.0
    max_urbantke_identity_error = 0.0
    max_rotation_metric_error = 0.0
    max_rotation_simplicity = 0.0

    for seed in range(seeds):
        tetrad = random_tetrad(1000 + seed)
        det_e = float(np.linalg.det(tetrad))
        metric = tetrad.T @ tetrad
        B = euclidean_self_dual_two_forms(tetrad)
        U = urbantke_tensor(B)
        simp, X = simplicity_defect(B)
        metric_error = conformal_metric_error(U, metric)
        identity_error = float(
            np.linalg.norm(U - 12.0 * det_e * metric)
            / max(np.linalg.norm(U), 1e-30)
        )
        wedge_target = 2.0 * det_e * np.eye(3)
        wedge_error = float(
            np.linalg.norm(X - wedge_target)
            / max(np.linalg.norm(wedge_target), 1e-30)
        )
        exact_rows.append({
            "seed": seed,
            "det_tetrad": det_e,
            "simplicity_defect": simp,
            "urbantke_conformal_metric_error": metric_error,
            "urbantke_identity_error": identity_error,
            "simple_wedge_identity_error": wedge_error,
        })
        max_exact_metric_error = max(max_exact_metric_error, metric_error)
        max_exact_simplicity = max(max_exact_simplicity, simp)
        max_urbantke_identity_error = max(max_urbantke_identity_error, identity_error)

        rng = np.random.default_rng(2000 + seed)
        R = random_so3(rng)
        Brot = np.einsum("ij,jab->iab", R, B)
        rot_simp, _ = simplicity_defect(Brot)
        rot_metric_error = conformal_metric_error(urbantke_tensor(Brot), metric)
        rotation_rows.append({
            "seed": seed,
            "simplicity_defect": rot_simp,
            "urbantke_conformal_metric_error": rot_metric_error,
        })
        max_rotation_metric_error = max(max_rotation_metric_error, rot_metric_error)
        max_rotation_simplicity = max(max_rotation_simplicity, rot_simp)

        # det(M)=1 anisotropic GL(3) distortions preserve the Urbantke
        # conformal metric but violate Plebanski simplicity.  Using exp(alpha S)
        # with tr(S)=0 keeps det(M)=1 exactly up to floating error.
        S = traceless_symmetric_generator(rng)
        for alpha in (0.05, 0.10, 0.20, 0.40, 0.70):
            M = matrix_exp_symmetric(S, alpha)
            Bdist = np.einsum("ij,jab->iab", M, B)
            dist_simp, _ = simplicity_defect(Bdist)
            dist_metric_error = conformal_metric_error(urbantke_tensor(Bdist), metric)
            distortion_rows.append({
                "seed": seed,
                "alpha": alpha,
                "det_internal_map": float(np.linalg.det(M)),
                "simplicity_defect": dist_simp,
                "urbantke_conformal_metric_error": dist_metric_error,
            })

    # Aggregate the deliberately distorted controls by alpha.
    distortion_summary = []
    for alpha in (0.05, 0.10, 0.20, 0.40, 0.70):
        rows = [r for r in distortion_rows if r["alpha"] == alpha]
        distortion_summary.append({
            "alpha": alpha,
            "mean_simplicity_defect": float(np.mean([r["simplicity_defect"] for r in rows])),
            "min_simplicity_defect": float(np.min([r["simplicity_defect"] for r in rows])),
            "max_urbantke_conformal_metric_error": float(
                np.max([r["urbantke_conformal_metric_error"] for r in rows])
            ),
        })

    passed = (
        max_exact_metric_error < 1e-11
        and max_exact_simplicity < 1e-11
        and max_urbantke_identity_error < 1e-11
        and max_rotation_metric_error < 1e-11
        and max_rotation_simplicity < 1e-11
        and distortion_summary[-1]["mean_simplicity_defect"] > 0.1
        and distortion_summary[-1]["max_urbantke_conformal_metric_error"] < 1e-11
    )

    return {
        "status": "finite Euclidean Plebanski/Urbantke control",
        "seeds": seeds,
        "passed": bool(passed),
        "exact_simple_sector": {
            "max_simplicity_defect": max_exact_simplicity,
            "max_urbantke_conformal_metric_error": max_exact_metric_error,
            "max_U_minus_12deteg_error": max_urbantke_identity_error,
            "rows": exact_rows,
        },
        "internal_SO3_control": {
            "max_simplicity_defect": max_rotation_simplicity,
            "max_urbantke_conformal_metric_error": max_rotation_metric_error,
            "rows": rotation_rows,
        },
        "GL3_distortion_control": {
            "summary": distortion_summary,
            "rows": distortion_rows,
            "lesson": "Urbantke metric reconstruction alone does not imply Plebanski simplicity; the simplicity defect is an independent gravity gate",
        },
        "future_microscopic_targets": {
            "simplicity": "Delta_simp(b) -> 0 without post-hoc projection",
            "nondegeneracy": "coarse wedge matrix X^ij remains nonsingular in the scaling window",
            "metric": "Urbantke metric becomes local and regulator/blocking independent",
            "connection": "a coarse connection satisfies D_A B -> 0",
            "einstein": "the anti-self-dual curvature component and microscopic Ward/HDA defects vanish in the same scaling window",
        },
        "scope_note": "This control uses real Euclidean self-dual 2-forms. Lorentzian reality conditions and emergence from binary face/diamond variables remain open.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", type=int, default=8)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.seeds < 1:
        parser.error("seeds must be positive")
    result = run(args.seeds)
    text = json.dumps(result, ensure_ascii=False, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
