#!/usr/bin/env python3
"""Unprojected finite-lattice Regge -> Fierz-Pauli scaling test.

This script deliberately does not TT-project the microscopic Hessian. It asks
whether the exact lattice edge Hessian, restricted only by the geometric
edge->metric map, approaches the full quadratic Fierz-Pauli tensor structure as
the lowest lattice momentum is sent to zero.

It also measures how the exact Regge vertex-displacement gauge subspace embeds
into the 10-component continuum metric subspace. Both are falsification tests:
a non-vanishing continuum residual would block the proposed gravity bridge.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regge_flat_lattice import FlatRegge4D  # noqa: E402

FP_RATIOS = np.array([1.0, -2.0, 2.0, -1.0])
ORIENTATIONS = {
    "axial": np.array([1.0, 0.0, 0.0, 0.0]),
    "diagonal2": np.array([1.0, 1.0, 0.0, 0.0]),
    "diagonal3": np.array([1.0, 1.0, 1.0, 0.0]),
}


def symmetric_basis_4d() -> np.ndarray:
    """Orthonormal Frobenius basis for real symmetric 4x4 tensors."""
    basis = []
    for i in range(4):
        B = np.zeros((4, 4)); B[i, i] = 1.0; basis.append(B)
    for i in range(4):
        for j in range(i + 1, 4):
            B = np.zeros((4, 4)); B[i, j] = B[j, i] = 1.0 / math.sqrt(2.0); basis.append(B)
    return np.asarray(basis)


def spin2_quadratic_basis(k: np.ndarray) -> list[np.ndarray]:
    """Four independent two-derivative symmetric-tensor structures."""
    basis = symmetric_basis_4d(); k = np.asarray(k, float); k2 = float(k @ k)
    tr = np.array([np.trace(B) for B in basis])
    V = np.array([k @ B for B in basis]).T
    s = np.array([k @ B @ k for B in basis])
    return [
        k2 * np.eye(10),
        V.T @ V,
        0.5 * (np.outer(s, tr) + np.outer(tr, s)),
        k2 * np.outer(tr, tr),
    ]


def metric_edge_map(model: FlatRegge4D) -> np.ndarray:
    basis = symmetric_basis_4d()
    out = np.zeros((len(model.direction_types), len(basis)))
    for a, nt in enumerate(model.direction_types):
        n = np.asarray(nt, dtype=float)
        for A, B in enumerate(basis):
            out[a, A] = n @ B @ n
    return out


def fit_fierz_pauli(H10: np.ndarray, k: np.ndarray) -> dict[str, object]:
    tensors = spin2_quadratic_basis(k)
    design = np.column_stack([T.ravel() for T in tensors])
    coeff, *_ = np.linalg.lstsq(design, H10.ravel(), rcond=None)
    fit = sum(coeff[i] * tensors[i] for i in range(4))
    residual = np.linalg.norm(H10 - fit) / max(np.linalg.norm(H10), 1e-30)
    ratios = coeff / coeff[0]
    ratio_error = np.linalg.norm(ratios - FP_RATIOS) / np.linalg.norm(FP_RATIOS)
    return {"coefficients": coeff.tolist(), "ratios": ratios.tolist(), "matrix_residual": float(residual), "ratio_error": float(ratio_error)}


def analyze_mode(L: int, orientation: np.ndarray, step: float) -> dict[str, object]:
    model = FlatRegge4D(L)
    k = (2.0 * np.pi / L) * orientation
    start = time.time(); H_regge = model.hessian(k, step=step); elapsed = time.time() - start
    H_kin = -H_regge
    A = metric_edge_map(model); zero = np.zeros_like(A); A_real = np.block([[A, zero], [zero, A]])
    Q_metric, _ = np.linalg.qr(A_real)
    G = model.gauge_basis(k)
    overlap_sv = np.linalg.svd(Q_metric.T @ G, compute_uv=False)
    leakage = np.linalg.norm((np.eye(30) - Q_metric @ Q_metric.T) @ G) / math.sqrt(G.shape[1])
    H_metric = A_real.T @ H_kin @ A_real
    H_cos = H_metric[:10, :10]; H_sin = H_metric[10:, 10:]; H10 = 0.5 * (H_cos + H_sin)
    cross_ratio = np.linalg.norm(H_metric[:10, 10:]) / max(np.linalg.norm(H10), 1e-30)
    cos_sin_difference = np.linalg.norm(H_cos - H_sin) / max(np.linalg.norm(H10), 1e-30)
    fp = fit_fierz_pauli(H10, k); eig = np.linalg.eigvalsh(H_metric)
    return {
        "L": L, "orientation": orientation.tolist(), "k": k.tolist(), "k_norm": float(np.linalg.norm(k)),
        "hessian_seconds": float(elapsed),
        "raw_regge_null_dimension_at_1e-3": int(np.sum(np.abs(np.linalg.eigvalsh(H_regge)) < 1e-3)),
        "gauge_dimension": int(G.shape[1]), "gauge_metric_leakage": float(leakage),
        "minimum_gauge_metric_principal_cosine": float(overlap_sv.min()),
        "cos_sin_cross_ratio": float(cross_ratio), "cos_sin_difference": float(cos_sin_difference),
        "smallest_metric_eigenvalues_by_abs": eig[np.argsort(np.abs(eig))[:8]].tolist(), "fierz_pauli": fp,
    }


def power_exponent(sizes: list[int], values: list[float]) -> float | None:
    if len(sizes) < 3 or any(v <= 0 for v in values): return None
    slope = np.polyfit(np.log(np.asarray(sizes, float)), np.log(np.asarray(values, float)), 1)[0]
    return float(-slope)


def continuum_ratios(sizes: list[int], ratios: list[list[float]]) -> list[float] | None:
    if len(sizes) < 3: return None
    x = 1.0 / np.asarray(sizes, float) ** 2; arr = np.asarray(ratios, float)
    return [float(np.polyfit(x, arr[:, j], 1)[1]) for j in range(4)]


def summarize(results: dict[str, list[dict[str, object]]]) -> dict[str, object]:
    summary = {}
    for name, rows in results.items():
        sizes = [int(r["L"]) for r in rows]
        leaks = [float(r["gauge_metric_leakage"]) for r in rows]
        residuals = [float(r["fierz_pauli"]["matrix_residual"]) for r in rows]
        ratio_errors = [float(r["fierz_pauli"]["ratio_error"]) for r in rows]
        ratios = [r["fierz_pauli"]["ratios"] for r in rows]
        cont = continuum_ratios(sizes, ratios)
        cont_error = None if cont is None else float(np.linalg.norm(np.asarray(cont) - FP_RATIOS) / np.linalg.norm(FP_RATIOS))
        summary[name] = {
            "sizes": sizes,
            "gauge_leakage_power_p_for_L^-p": power_exponent(sizes, leaks),
            "FP_matrix_residual_power_p_for_L^-p": power_exponent(sizes, residuals),
            "FP_ratio_error_power_p_for_L^-p": power_exponent(sizes, ratio_errors),
            "continuum_ratios_linear_in_1_over_L2": cont,
            "continuum_ratio_relative_error": cont_error,
        }
    return summary


def markdown_report(payload: dict[str, object]) -> str:
    lines = ["# Gravity bridge scaling: unprojected Regge -> Fierz-Pauli", "", "Finite-lattice evidence only; this report does **not** claim that nonlinear IR Einstein gravity is proved.", "", "| orientation | L | gauge leakage | min cosine | FP residual | FP ratio error |", "|:--|--:|--:|--:|--:|--:|"]
    for name, rows in payload["results"].items():
        for row in rows:
            fp = row["fierz_pauli"]
            lines.append(f"| {name} | {row['L']} | {row['gauge_metric_leakage']:.8g} | {row['minimum_gauge_metric_principal_cosine']:.8g} | {fp['matrix_residual']:.8g} | {fp['ratio_error']:.8g} |")
    lines += ["", "## Scaling summary", ""]
    for name, item in payload["summary"].items():
        lines += [f"### {name}", "", f"- gauge leakage exponent: `{item['gauge_leakage_power_p_for_L^-p']}`", f"- FP matrix residual exponent: `{item['FP_matrix_residual_power_p_for_L^-p']}`", f"- FP ratio-error exponent: `{item['FP_ratio_error_power_p_for_L^-p']}`", f"- continuum FP ratios: `{item['continuum_ratios_linear_in_1_over_L2']}`", f"- continuum ratio relative error: `{item['continuum_ratio_relative_error']}`", ""]
    lines += ["## Interpretation boundary", "", "A successful trend is finite-lattice evidence only; nonlinear Ward closure, Lorentzian dynamics and microscopic universality remain separate tests."]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sizes", type=int, nargs="+", default=[3, 4])
    parser.add_argument("--orientations", nargs="+", choices=sorted(ORIENTATIONS), default=["axial", "diagonal2", "diagonal3"])
    parser.add_argument("--step", type=float, default=2e-4)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    if any(L < 3 for L in args.sizes): parser.error("all lattice sizes must be >= 3")
    if not np.isfinite(args.step) or args.step <= 0: parser.error("--step must be finite and positive")
    results = {}
    for name in args.orientations:
        rows = []
        for L in args.sizes:
            print(f"[{name}] L={L}", flush=True); rows.append(analyze_mode(L, ORIENTATIONS[name], args.step))
        results[name] = rows
    payload = {"status": "finite-lattice evidence; nonlinear Einstein IR not proved", "kinetic_convention": "H_kin = -H_Regge", "target_Fierz_Pauli_ratios": FP_RATIOS.tolist(), "results": results, "summary": summarize(results)}
    text = json.dumps(payload, indent=2); print(text)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_text(text + "\n", encoding="utf-8"); args.output.with_suffix(".md").write_text(markdown_report(payload), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())