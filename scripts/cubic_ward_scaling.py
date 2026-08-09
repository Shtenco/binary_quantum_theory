#!/usr/bin/env python3
"""Direct cubic diffeomorphism Ward-scaling test for the Regge lattice.

For g = eta + lambda h and an infinitesimal periodic vector field xi, split

    delta g = delta_0 g + lambda delta_1 g

with delta_0 g = d_mu xi_nu + d_nu xi_mu and delta_1 g = L_xi h.
The coefficient of lambda^2 in the directional variation of the action gives
separately delta_0 S_3 and delta_1 S_2.  The nonlinear Ward defect is

    W3 = |delta_0 S_3 + delta_1 S_2| /
         (|delta_0 S_3| + |delta_1 S_2|).

The continuum Einstein-Hilbert calculation is evaluated independently as a
numerical control and should give W3 ~ numerical zero.  The finite Regge W3 is
then scanned versus L.  No TT projection is used.

This tests restoration of continuum diffeomorphism symmetry on a fixed 4D
Regge scaffold.  It does not prove the microscopic binary RG flow, four-
dimensional emergence, Lorentzian unitarity, matter coupling, or experiment.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = Path(__file__).resolve().parent
for p in (ROOT, SCRIPTS):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from bcqg_unified_verification import FlatRegge4D  # noqa: E402
from regge_eh_cubic_bridge import polarizations, spectral_diff  # noqa: E402

XI_VECTOR = np.array([0.7, -0.2, 0.4, 0.1], dtype=float)
XI_VECTOR /= np.linalg.norm(XI_VECTOR)


def h_and_gauge(coords: np.ndarray, L: float, P: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return h, delta0 g and delta1 g = L_xi h on arbitrary coordinates."""
    x1 = coords[..., 0]
    x2 = coords[..., 1]
    k = 2.0 * np.pi / L
    ph1 = k * x1
    ph2 = k * x2
    ph3 = k * (x1 + x2)

    h = np.zeros(coords.shape[:-1] + (4, 4))
    dh = np.zeros(coords.shape[:-1] + (4, 4, 4))  # derivative rho, mu, nu
    for tensor, phase, derivative_mask in zip(P, [ph1, ph2, ph3], [(1, 0), (0, 1), (1, 1)]):
        h += np.cos(phase)[..., None, None] * tensor
        if derivative_mask[0]:
            dh[..., 0, :, :] += (-k * np.sin(phase))[..., None, None] * tensor
        if derivative_mask[1]:
            dh[..., 1, :, :] += (-k * np.sin(phase))[..., None, None] * tensor

    # xi^rho = v^rho sin(k x1)
    xi = np.sin(ph1)[..., None] * XI_VECTOR
    dxi = np.zeros(coords.shape[:-1] + (4, 4))  # derivative mu, vector rho
    dxi[..., 0, :] = (k * np.cos(ph1))[..., None] * XI_VECTOR

    delta0 = np.zeros_like(h)
    delta1 = np.zeros_like(h)
    for mu in range(4):
        for nu in range(4):
            delta0[..., mu, nu] = dxi[..., mu, nu] + dxi[..., nu, mu]
            total = np.zeros(coords.shape[:-1])
            for rho in range(4):
                total += xi[..., rho] * dh[..., rho, mu, nu]
                total += h[..., rho, nu] * dxi[..., mu, rho]
                total += h[..., mu, rho] * dxi[..., nu, rho]
            delta1[..., mu, nu] = total
    return h, delta0, delta1


def eh_action_from_metric(g: np.ndarray, L: float) -> float:
    gi = np.linalg.inv(g)
    det = np.linalg.det(g)
    if np.any(det <= 0):
        raise ValueError("metric lost positive definiteness")
    sqrtg = np.sqrt(det)

    dg = np.stack([spectral_diff(g, mu, L) for mu in range(4)], axis=-3)
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
    dV = (L / g.shape[0]) ** 4
    return float(np.sum(sqrtg * R) * dV)


def fit_lambda2(lam: np.ndarray, values: list[float], degree: int = 4) -> tuple[float, np.ndarray]:
    design = np.column_stack([lam ** p for p in range(degree + 1)])
    coeff, *_ = np.linalg.lstsq(design, np.asarray(values), rcond=None)
    return float(coeff[2]), coeff


def continuum_ward(L: int, P: np.ndarray, grid: int, lam_max: float, nlam: int, alpha: float) -> dict[str, object]:
    coord = np.arange(grid) * L / grid
    X = np.meshgrid(coord, coord, coord, coord, indexing="ij")
    coords = np.stack(X, axis=-1)
    h, delta0, delta1 = h_and_gauge(coords, float(L), P)
    lam = np.linspace(-lam_max, lam_max, nlam)
    D0: list[float] = []
    D1: list[float] = []
    eye = np.eye(4)
    for x in lam:
        g = eye + x * h
        D0.append((eh_action_from_metric(g + alpha * delta0, L) - eh_action_from_metric(g - alpha * delta0, L)) / (2.0 * alpha))
        D1.append((eh_action_from_metric(g + alpha * x * delta1, L) - eh_action_from_metric(g - alpha * x * delta1, L)) / (2.0 * alpha))
    A, c0 = fit_lambda2(lam, D0)
    B, c1 = fit_lambda2(lam, D1)
    W = abs(A + B) / (abs(A) + abs(B) + 1e-30)
    return {
        "delta0_S3": A,
        "delta1_S2": B,
        "W3": float(W),
        "D0_polynomial": c0.tolist(),
        "D1_polynomial": c1.tolist(),
    }


def regge_ward(L: int, P: np.ndarray, lam_max: float, nlam: int, alpha: float) -> dict[str, object]:
    model = FlatRegge4D(L)
    h, delta0, delta1 = h_and_gauge(model.midpoints, float(L), P)
    n = model.directions
    edge_h = np.einsum("ei,eij,ej->e", n, h, n)
    edge_d0 = np.einsum("ei,eij,ej->e", n, delta0, n)
    edge_d1 = np.einsum("ei,eij,ej->e", n, delta1, n)

    lam = np.linspace(-lam_max, lam_max, nlam)
    D0: list[float] = []
    D1: list[float] = []
    for x in lam:
        q = model.background_q + x * edge_h
        D0.append((model.action(q + alpha * edge_d0) - model.action(q - alpha * edge_d0)) / (2.0 * alpha))
        D1.append((model.action(q + alpha * x * edge_d1) - model.action(q - alpha * x * edge_d1)) / (2.0 * alpha))
    A, c0 = fit_lambda2(lam, D0)
    B, c1 = fit_lambda2(lam, D1)
    W = abs(A + B) / (abs(A) + abs(B) + 1e-30)
    return {
        "L": L,
        "delta0_S3": A,
        "delta1_S2": B,
        "W3": float(W),
        "D0_polynomial": c0.tolist(),
        "D1_polynomial": c1.tolist(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sizes", type=int, nargs="+", default=[3, 4, 5])
    parser.add_argument("--grid", type=int, default=8, help="continuum control grid")
    parser.add_argument("--lam-max", type=float, default=0.03)
    parser.add_argument("--nlam", type=int, default=9)
    parser.add_argument("--alpha", type=float, default=3e-5)
    parser.add_argument("--seed", type=int, default=260809)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    if any(L < 3 for L in args.sizes):
        parser.error("sizes must be >= 3")
    if args.grid < 8:
        parser.error("grid must be >= 8")
    if args.nlam < 7 or args.nlam % 2 == 0:
        parser.error("nlam must be odd and >= 7")
    if args.lam_max <= 0 or args.alpha <= 0:
        parser.error("lam-max and alpha must be positive")

    P = polarizations(args.seed)
    control_L = max(5, min(args.sizes))
    continuum = continuum_ward(control_L, P, args.grid, args.lam_max, args.nlam, args.alpha)
    rows = [regge_ward(L, P, args.lam_max, args.nlam, args.alpha) for L in args.sizes]

    summary: dict[str, object] = {
        "continuum_control_L": control_L,
        "continuum_W3": continuum["W3"],
    }
    if len(rows) >= 3:
        sizes = np.asarray(args.sizes, float)
        W = np.asarray([r["W3"] for r in rows])
        summary["all_sizes_W3_power_p_for_L^-p"] = float(-np.polyfit(np.log(sizes), np.log(W), 1)[0])
        mask = sizes >= 5
        if np.sum(mask) >= 3:
            summary["L_ge_5_W3_power_p_for_L^-p"] = float(-np.polyfit(np.log(sizes[mask]), np.log(W[mask]), 1)[0])

    payload = {
        "status": "direct nonlinear Ward-restoration evidence on fixed 4D Regge scaffold",
        "definition": "W3 = |delta0 S3 + delta1 S2|/(|delta0 S3|+|delta1 S2|)",
        "parameters": {
            "sizes": args.sizes,
            "grid": args.grid,
            "lam_max": args.lam_max,
            "nlam": args.nlam,
            "alpha": args.alpha,
            "seed": args.seed,
        },
        "continuum_control": continuum,
        "rows": rows,
        "summary": summary,
    }
    text = json.dumps(payload, indent=2)
    print(text)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
