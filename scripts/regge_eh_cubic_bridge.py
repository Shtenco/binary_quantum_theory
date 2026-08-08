#!/usr/bin/env python3
"""Compare finite Regge action with direct continuum Einstein-Hilbert action.

A deterministic generic three-wave symmetric metric field is placed on a flat
4-torus.  For each lattice size L we evaluate

  S_Regge = sum_h A_h delta_h

on the Freudenthal 4D Regge lattice and independently evaluate

  S_EH = integral sqrt(g) R d^4x

with spectral derivatives on an auxiliary continuum grid.  Polynomial fits in
the field amplitude extract quadratic and cubic coefficients.  Standard Regge
normalization predicts S_Regge / S_EH -> 1/2 in the smooth limit, so both c2
and c3 must independently approach that factor.

This is a nonlinear finite-lattice bridge test.  It is not a proof of the full
microscopic CIMFIG/BCQG RG flow, nonlinear gauge closure, Lorentzian unitarity,
or emergence of four dimensions.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from bcqg_unified_verification import FlatRegge4D  # noqa: E402


def polarizations(seed: int = 260809) -> np.ndarray:
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(3):
        M = rng.normal(size=(4, 4))
        M = 0.5 * (M + M.T)
        M -= np.trace(M) * np.eye(4) / 4.0
        M /= np.linalg.norm(M)
        out.append(M)
    return np.asarray(out)


def spectral_diff(field: np.ndarray, axis: int, domain_length: float) -> np.ndarray:
    n = field.shape[axis]
    dx = domain_length / n
    freq = 2.0 * np.pi * np.fft.fftfreq(n, d=dx)
    axes = (0, 1, 2, 3)
    F = np.fft.fftn(field, axes=axes)
    shape = [1] * field.ndim
    shape[axis] = n
    return np.fft.ifftn(F * (1j * freq.reshape(shape)), axes=axes).real


def continuum_metric(L: float, grid: int, eps: float, P: np.ndarray) -> np.ndarray:
    coord = np.arange(grid) * L / grid
    X = np.meshgrid(coord, coord, coord, coord, indexing="ij")
    phases = [
        2.0 * np.pi * X[0] / L,
        2.0 * np.pi * X[1] / L,
        2.0 * np.pi * (X[0] + X[1]) / L,
    ]
    g = np.zeros((grid, grid, grid, grid, 4, 4))
    g[...] = np.eye(4)
    for tensor, phase in zip(P, phases):
        g += eps * np.cos(phase)[..., None, None] * tensor
    return g


def eh_action(L: float, grid: int, eps: float, P: np.ndarray) -> float:
    g = continuum_metric(L, grid, eps, P)
    gi = np.linalg.inv(g)
    det = np.linalg.det(g)
    if np.any(det <= 0):
        raise ValueError("metric lost positive definiteness")
    sqrtg = np.sqrt(det)

    # dg[..., derivative_index, i, j]
    dg = np.stack([spectral_diff(g, mu, L) for mu in range(4)], axis=-3)

    # Gamma[..., rho, mu, nu]
    Gamma = np.zeros(g.shape[:-2] + (4, 4, 4))
    for rho in range(4):
        for mu in range(4):
            for nu in range(4):
                total = 0.0
                for sig in range(4):
                    total += 0.5 * gi[..., rho, sig] * (
                        dg[..., mu, nu, sig]
                        + dg[..., nu, mu, sig]
                        - dg[..., sig, mu, nu]
                    )
                Gamma[..., rho, mu, nu] = total

    # dGamma[..., derivative_index, rho, mu, nu]
    dGamma = np.stack([spectral_diff(Gamma, a, L) for a in range(4)], axis=-4)
    Ric = np.zeros(g.shape[:-2] + (4, 4))
    for mu in range(4):
        for nu in range(4):
            total = np.zeros(g.shape[:-2])
            for rho in range(4):
                total += dGamma[..., rho, rho, mu, nu] - dGamma[..., nu, rho, mu, rho]
                for sig in range(4):
                    total += (
                        Gamma[..., rho, mu, nu] * Gamma[..., sig, rho, sig]
                        - Gamma[..., sig, mu, rho] * Gamma[..., rho, nu, sig]
                    )
            Ric[..., mu, nu] = total
    R = np.einsum("...ij,...ij->...", gi, Ric)
    dV = (L / grid) ** 4
    return float(np.sum(sqrtg * R) * dV)


def regge_edge_lengths(model: FlatRegge4D, L: int, eps: float, P: np.ndarray) -> np.ndarray:
    mids = model.midpoints
    phases = [
        2.0 * np.pi * mids[:, 0] / L,
        2.0 * np.pi * mids[:, 1] / L,
        2.0 * np.pi * (mids[:, 0] + mids[:, 1]) / L,
    ]
    q = model.background_q.astype(float).copy()
    for tensor, phase in zip(P, phases):
        amp = np.einsum("ei,ij,ej->e", model.directions, tensor, model.directions)
        q += eps * amp * np.cos(phase)
    return q


def polynomial_coefficients(eps: np.ndarray, values: list[float], degree: int = 5) -> np.ndarray:
    design = np.column_stack([eps ** p for p in range(degree + 1)])
    coeff, *_ = np.linalg.lstsq(design, np.asarray(values), rcond=None)
    return coeff


def one_size(L: int, grid: int, eps_max: float, samples: int, P: np.ndarray) -> dict[str, object]:
    model = FlatRegge4D(L)
    eps = np.linspace(-eps_max, eps_max, samples)
    regge = [model.action(regge_edge_lengths(model, L, e, P)) for e in eps]
    continuum = [eh_action(float(L), grid, e, P) for e in eps]
    cr = polynomial_coefficients(eps, regge)
    cc = polynomial_coefficients(eps, continuum)

    c2_ratio = float(cr[2] / cc[2])
    c3_ratio = float(cr[3] / cc[3])
    nonlinear_ratio_regge = float(cr[3] / cr[2])
    nonlinear_ratio_eh = float(cc[3] / cc[2])
    nonlinear_relative_error = abs(nonlinear_ratio_regge - nonlinear_ratio_eh) / abs(nonlinear_ratio_eh)

    return {
        "L": L,
        "regge_coefficients_c0_to_c5": cr.tolist(),
        "EH_coefficients_c0_to_c5": cc.tolist(),
        "c2_Regge_over_EH": c2_ratio,
        "c3_Regge_over_EH": c3_ratio,
        "c3_over_c2_Regge": nonlinear_ratio_regge,
        "c3_over_c2_EH": nonlinear_ratio_eh,
        "c3_over_c2_relative_error": float(nonlinear_relative_error),
        "linear_term_abs_Regge": float(abs(cr[1])),
        "linear_term_abs_EH": float(abs(cc[1])),
    }


def power_p(sizes: np.ndarray, error: np.ndarray) -> float:
    return float(-np.polyfit(np.log(sizes), np.log(error), 1)[0])


def continuum_intercept(sizes: np.ndarray, values: np.ndarray) -> float:
    return float(np.polyfit(1.0 / sizes**2, values, 1)[1])


def report_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# Regge -> Einstein-Hilbert cubic bridge",
        "",
        "Finite-lattice nonlinear evidence only; **not** a proof of full microscopic quantum gravity.",
        "",
        "| L | c2 Regge/EH | c3 Regge/EH | (c3/c2) Regge | (c3/c2) EH | relative error |",
        "|--:|--:|--:|--:|--:|--:|",
    ]
    for r in payload["rows"]:
        lines.append(
            f"| {r['L']} | {r['c2_Regge_over_EH']:.8f} | {r['c3_Regge_over_EH']:.8f} | "
            f"{r['c3_over_c2_Regge']:.8f} | {r['c3_over_c2_EH']:.8f} | {r['c3_over_c2_relative_error']:.8f} |"
        )
    lines += ["", "## Smooth-limit diagnostics", ""]
    for k, v in payload["summary"].items():
        lines.append(f"- {k}: `{v}`")
    lines += [
        "",
        "The conventional smooth Regge normalization is `S_Regge -> 0.5 S_EH`; therefore c2 and c3 are tested independently against 0.5.  The three-wave field contains a momentum-conserving triad, so its cubic coefficient is nonzero.",
        "",
        "Still open: cubic gauge Ward closure, blocked effective action and universality, Lorentzian measure/unitarity, 4D emergence without a 4D scaffold, matter, and experiment.",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sizes", type=int, nargs="+", default=[5, 6], help="use 5 6 7 8 for the continuum scan")
    parser.add_argument("--grid", type=int, default=8, help="auxiliary spectral grid per continuum dimension")
    parser.add_argument("--eps-max", type=float, default=0.03)
    parser.add_argument("--samples", type=int, default=11)
    parser.add_argument("--seed", type=int, default=260809)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    if any(L < 3 for L in args.sizes):
        parser.error("sizes must be >= 3")
    if args.grid < 8:
        parser.error("grid must be >= 8 to avoid low-order aliasing in this test")
    if args.samples < 7 or args.samples % 2 == 0:
        parser.error("samples must be odd and >= 7")
    if args.eps_max <= 0:
        parser.error("eps-max must be positive")

    P = polarizations(args.seed)
    rows = [one_size(L, args.grid, args.eps_max, args.samples, P) for L in args.sizes]
    sizes = np.asarray(args.sizes, float)

    summary: dict[str, object] = {
        "target_Regge_over_EH": 0.5,
        "continuum_EH_c3_over_c2_mean": float(np.mean([r["c3_over_c2_EH"] for r in rows])),
    }
    if len(rows) >= 3:
        r2 = np.asarray([r["c2_Regge_over_EH"] for r in rows])
        r3 = np.asarray([r["c3_Regge_over_EH"] for r in rows])
        nr = np.asarray([r["c3_over_c2_relative_error"] for r in rows])
        summary.update({
            "c2_error_power_p_for_L^-p": power_p(sizes, np.abs(r2 - 0.5)),
            "c3_error_power_p_for_L^-p": power_p(sizes, np.abs(r3 - 0.5)),
            "nonlinear_ratio_error_power_p_for_L^-p": power_p(sizes, nr),
            "c2_Regge_over_EH_intercept_linear_1_over_L2": continuum_intercept(sizes, r2),
            "c3_Regge_over_EH_intercept_linear_1_over_L2": continuum_intercept(sizes, r3),
        })

    payload = {
        "status": "nonlinear finite-lattice bridge evidence; full Einstein IR not proved",
        "polarization_seed": args.seed,
        "continuum_grid": args.grid,
        "eps_max": args.eps_max,
        "samples": args.samples,
        "rows": rows,
        "summary": summary,
    }
    text = json.dumps(payload, indent=2)
    print(text)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
        args.output.with_suffix(".md").write_text(report_markdown(payload), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
