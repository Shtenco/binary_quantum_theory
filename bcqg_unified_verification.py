#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BCQG UNIFIED VERIFICATION SUITE
===============================

A single reproducible Python program that re-runs the decisive numerical and
algebraic checks developed for Binary Causal Quantum Gravity (BCQG).

The suite deliberately separates:
  * DERIVED/EXACT finite-model statements;
  * CONSTRUCTIVE consistency demonstrations;
  * STOCHASTIC finite-size evidence;
  * claims that remain unproved for the full microscopic edge-bit partition sum.

Default profile: full.
Outputs:
  BCQG_UNIFIED_RESULTS.json
  BCQG_UNIFIED_REPORT.md

Dependencies: numpy, scipy, pandas. Optional heavy checks use torch and numba.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import time
import traceback
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Callable

import numpy as np
import pandas as pd
from scipy.linalg import expm, logm
from scipy.special import logsumexp


# -----------------------------------------------------------------------------
# Verification infrastructure
# -----------------------------------------------------------------------------

@dataclass
class Check:
    section: str
    name: str
    value: Any
    expected: Any
    tolerance: Any
    passed: bool
    note: str = ""


CHECKS: list[Check] = []
RESULTS: dict[str, Any] = {}


def scalarize(x: Any) -> Any:
    if isinstance(x, (np.floating, np.integer, np.bool_)):
        return x.item()
    if isinstance(x, np.ndarray):
        return [scalarize(v) for v in x.tolist()]
    if isinstance(x, dict):
        return {str(k): scalarize(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [scalarize(v) for v in x]
    if isinstance(x, complex):
        return {"real": float(x.real), "imag": float(x.imag)}
    return x


def add_check(section: str, name: str, value: Any, expected: Any,
              tolerance: Any, passed: bool, note: str = "") -> None:
    CHECKS.append(Check(section, name, scalarize(value), scalarize(expected),
                        scalarize(tolerance), bool(passed), note))


def close(value: float, expected: float, atol: float = 1e-10,
          rtol: float = 1e-8) -> bool:
    return bool(np.isclose(value, expected, atol=atol, rtol=rtol))


def relative_error(a: np.ndarray | float, b: np.ndarray | float) -> float:
    aa = np.asarray(a)
    bb = np.asarray(b)
    return float(np.linalg.norm(aa - bb) / max(np.linalg.norm(bb), 1e-30))


def timed(section: str, fn: Callable[[], dict[str, Any]]) -> None:
    start = time.time()
    print(f"\n=== {section} ===", flush=True)
    try:
        out = fn()
        out["elapsed_seconds"] = time.time() - start
        RESULTS[section] = out
        print(f"completed in {out['elapsed_seconds']:.3f} s", flush=True)
    except Exception as exc:
        RESULTS[section] = {
            "error": repr(exc),
            "traceback": traceback.format_exc(),
            "elapsed_seconds": time.time() - start,
        }
        add_check(section, "section execution", repr(exc), "no exception", None,
                  False, "The section failed to execute.")
        print(traceback.format_exc(), flush=True)


# -----------------------------------------------------------------------------
# 1. Exact boundary-of-5-simplex binary geometry and perfect action
# -----------------------------------------------------------------------------

EPS = 0.08
Q0 = 1.0
KAPPA_R = 0.8
LAMBDA_V = 0.12


def build_local_4simplex_lookup(eps: float = EPS, q0: float = Q0):
    local_edges = list(itertools.combinations(range(5), 2))
    local_triangles = list(itertools.combinations(range(5), 3))

    def coordinates(qmat: np.ndarray) -> np.ndarray | None:
        gram = np.empty((4, 4), dtype=float)
        for i in range(1, 5):
            for j in range(1, 5):
                gram[i - 1, j - 1] = (qmat[0, i] + qmat[0, j] - qmat[i, j]) / 2
        vals, vecs = np.linalg.eigh(gram)
        if vals.min() <= 1e-12:
            return None
        x = vecs @ np.diag(np.sqrt(vals))
        return np.vstack([np.zeros(4), x])

    def outward_normal(coords_: np.ndarray, omitted: int) -> np.ndarray:
        facet = [i for i in range(5) if i != omitted]
        ref = coords_[facet[0]]
        matrix = np.stack([coords_[v] - ref for v in facet[1:]], axis=0)
        _, _, vh = np.linalg.svd(matrix)
        n = vh[-1] / np.linalg.norm(vh[-1])
        if np.dot(n, coords_[omitted] - ref) > 0:
            n = -n
        return n

    lookup = []
    for pattern in range(1 << 10):
        bits = np.array([(pattern >> i) & 1 for i in range(10)], dtype=np.int8)
        sigma = 2 * bits - 1
        qvals = q0 * (1 + eps * sigma)
        qmat = np.zeros((5, 5))
        for a, (i, j) in enumerate(local_edges):
            qmat[i, j] = qmat[j, i] = qvals[a]
        c = coordinates(qmat)
        if c is None:
            lookup.append(None)
            continue
        emat = np.stack([c[i] - c[0] for i in range(1, 5)], axis=0)
        volume = abs(np.linalg.det(emat)) / math.factorial(4)
        normals = {i: outward_normal(c, i) for i in range(5)}
        angles = {}
        for tri in local_triangles:
            opposite = [i for i in range(5) if i not in tri]
            u, v = opposite
            cosine = np.clip(-np.dot(normals[u], normals[v]), -1.0, 1.0)
            angles[tri] = float(np.arccos(cosine))
        lookup.append((float(volume), angles))
    return lookup, local_edges


def enumerate_boundary_5simplex():
    vertices = range(6)
    edges = list(itertools.combinations(vertices, 2))
    edge_index = {e: i for i, e in enumerate(edges)}
    triangles = list(itertools.combinations(vertices, 3))
    simplices = list(itertools.combinations(vertices, 5))
    lookup, local_edges = build_local_4simplex_lookup()

    simplex_maps = []
    for simplex in simplices:
        gv = list(simplex)
        local_of = {g: i for i, g in enumerate(gv)}
        emap = []
        for le in local_edges:
            ge = tuple(sorted((gv[le[0]], gv[le[1]])))
            emap.append(edge_index[ge])
        tmap = {}
        for gt in itertools.combinations(gv, 3):
            lt = tuple(sorted(local_of[g] for g in gt))
            tmap[tuple(gt)] = lt
        simplex_maps.append((emap, tmap))

    incident = [[edge_index[tuple(sorted((v, u)))] for u in vertices if u != v]
                for v in vertices]
    nstates = 1 << 15
    curvature = np.empty(nstates)
    volume = np.empty(nstates)
    coarse = np.empty(nstates, dtype=np.int16)

    for mask in range(nstates):
        bits = np.array([(mask >> i) & 1 for i in range(15)], dtype=np.int8)
        sigma = 2 * bits - 1
        areas = {}
        for a, b, c in triangles:
            qab = Q0 * (1 + EPS * sigma[edge_index[(a, b)]])
            qac = Q0 * (1 + EPS * sigma[edge_index[(a, c)]])
            qbc = Q0 * (1 + EPS * sigma[edge_index[(b, c)]])
            dot = (qab + qac - qbc) / 2
            areas[(a, b, c)] = 0.5 * math.sqrt(max(qab * qac - dot * dot, 0.0))
        total_volume = 0.0
        angle_sum = {t: 0.0 for t in triangles}
        for emap, tmap in simplex_maps:
            lp = 0
            for li, gi in enumerate(emap):
                lp |= int(bits[gi]) << li
            item = lookup[lp]
            if item is None:
                raise RuntimeError("Degenerate simplex")
            sv, sa = item
            total_volume += sv
            for gt, lt in tmap.items():
                angle_sum[gt] += sa[lt]
        R = sum(areas[t] * (2 * math.pi - angle_sum[t]) for t in triangles)
        cmask = 0
        for v in vertices:
            if sigma[incident[v]].sum() > 0:
                cmask |= 1 << v
        curvature[mask] = R
        volume[mask] = total_volume
        coarse[mask] = cmask
    return curvature, volume, coarse


def walsh_coefficients(eff: np.ndarray) -> dict[int, float]:
    coeff = {}
    for subset in range(64):
        total = 0.0
        for state in range(64):
            prod = 1.0
            for v in range(6):
                if (subset >> v) & 1:
                    prod *= 1.0 if (state >> v) & 1 else -1.0
            total += eff[state] * prod
        coeff[subset] = total / 64.0
    return coeff


def reconstruct_walsh(coeff: dict[int, float], order: int) -> np.ndarray:
    out = np.zeros(64)
    for state in range(64):
        val = 0.0
        for subset, c in coeff.items():
            if subset.bit_count() > order:
                continue
            prod = 1.0
            for v in range(6):
                if (subset >> v) & 1:
                    prod *= 1.0 if (state >> v) & 1 else -1.0
            val += c * prod
        out[state] = val
    return out


def section_exact_finite_rg() -> dict[str, Any]:
    R, V, coarse = enumerate_boundary_5simplex()
    S = -KAPPA_R * R + LAMBDA_V * V
    logw = -S - logsumexp(-S)
    w = np.exp(logw)
    ER = float(np.dot(w, R))
    EV = float(np.dot(w, V))
    counts = np.bincount(coarse, minlength=64)
    Seff = np.empty(64)
    for c in range(64):
        idx = np.flatnonzero(coarse == c)
        Seff[c] = -logsumexp(-S[idx])
    coeff = walsh_coefficients(Seff)
    Kn = {n: float(np.mean([v for m, v in coeff.items() if m.bit_count() == n]))
          for n in range(7)}
    approx2 = reconstruct_walsh(coeff, 2)
    aligned2 = approx2 + np.mean(Seff - approx2)
    rmse2 = float(np.sqrt(np.mean((aligned2 - Seff) ** 2)))
    maxerr2 = float(np.max(np.abs(aligned2 - Seff)))
    logp = -Seff - logsumexp(-Seff)
    logq = -approx2 - logsumexp(-approx2)
    p, q = np.exp(logp), np.exp(logq)
    kl2 = float(np.sum(p * (logp - logq)))
    tv2 = float(0.5 * np.sum(np.abs(p - q)))
    full_reconstruction = reconstruct_walsh(coeff, 6)
    full_error = float(np.max(np.abs(full_reconstruction - Seff)))

    expected_K = {
        0: -22.1958378678422,
        1: -0.09239099201843348,
        2: -0.09859657616304501,
        3: -0.0027511105832090264,
        4: 0.006926785787356778,
        5: 0.0010713230903191633,
        6: -0.016881021565499477,
    }
    add_check("finite_rg", "number of microgeometries", len(R), 32768, 0, len(R) == 32768)
    add_check("finite_rg", "curvature expectation", ER, 20.212063520058123, 2e-10,
              close(ER, 20.212063520058123, 2e-10, 0))
    add_check("finite_rg", "volume expectation", EV, 0.13883624356487617, 2e-12,
              close(EV, 0.13883624356487617, 2e-12, 0))
    add_check("finite_rg", "effective action minimum", Seff.min(), -24.190705970275907, 2e-10,
              close(float(Seff.min()), -24.190705970275907, 2e-10, 0))
    add_check("finite_rg", "effective action maximum", Seff.max(), -21.86238676042551, 2e-10,
              close(float(Seff.max()), -21.86238676042551, 2e-10, 0))
    for n, expv in expected_K.items():
        add_check("finite_rg", f"symmetric Walsh K{n}", Kn[n], expv, 5e-10,
                  close(Kn[n], expv, 5e-10, 0))
    add_check("finite_rg", "order-2 RMSE", rmse2, 0.03410180196203392, 5e-10,
              close(rmse2, 0.03410180196203392, 5e-10, 0))
    add_check("finite_rg", "order-2 KL", kl2, 0.0006770913213629531, 5e-10,
              close(kl2, 0.0006770913213629531, 5e-10, 0))
    add_check("finite_rg", "full Walsh reconstruction", full_error, 0.0, 1e-12,
              full_error < 1e-12)
    return {
        "curvature_range": [float(R.min()), float(R.max())],
        "volume_range": [float(V.min()), float(V.max())],
        "expectation_R": ER,
        "expectation_V": EV,
        "effective_action_range": [float(Seff.min()), float(Seff.max())],
        "microstates_per_coarse_state_range": [int(counts.min()), int(counts.max())],
        "symmetric_Walsh_coefficients": Kn,
        "order2": {"rmse": rmse2, "max_error": maxerr2, "KL": kl2, "TV": tv2},
        "full_reconstruction_max_error": full_error,
    }


# -----------------------------------------------------------------------------
# 2. Analytic causal/orientation and massless-pole checks
# -----------------------------------------------------------------------------

def section_orientation_and_pole() -> dict[str, Any]:
    # Exact soft selector ratios.
    Qvals = np.array([q for q in range(-6, 7, 2)])
    gammas = [0, 0.25, 0.5, 1, 2, 4]
    ratios = {}
    for gamma in gammas:
        # aggregate wrong/correct for the stated sector counts, excluding Q=0
        # Degeneracies for six signs: C(6,(Q+6)/2).
        wrong = 0.0
        correct = 0.0
        for Q in Qvals:
            deg = math.comb(6, (Q + 6) // 2)
            if Q == 0:
                continue
            pc = 1.0 / (1.0 + math.exp(-2 * gamma * abs(Q)))
            correct += deg * pc
            wrong += deg * (1 - pc)
        ratios[gamma] = wrong / correct

    # Symmetric i epsilon no-go on arbitrary real actions.
    rng = np.random.default_rng(1234)
    S = rng.normal(size=100)
    T = np.abs(rng.normal(size=100))
    eps = 0.03
    Zp = np.sum(np.exp(1j * S - eps * T))
    Zm = np.sum(np.exp(-1j * S - eps * T))
    mod_ratio = abs(Zm / Zp)

    # Lattice massless pole.
    Ls_fit = np.arange(12, 129, dtype=float)
    lam_fit = 4 * np.sin(np.pi / Ls_fit) ** 2
    exponent = np.polyfit(np.log(Ls_fit), np.log(lam_fit), 1)[0]
    L_limit = 256.0
    limit = float(L_limit ** 2 * 4 * np.sin(np.pi / L_limit) ** 2)
    add_check("orientation_pole", "symmetric i-epsilon modulus ratio", mod_ratio, 1.0, 1e-12,
              abs(mod_ratio - 1) < 1e-12)
    add_check("orientation_pole", "massless gap exponent", exponent, -1.994687633, 5e-5,
              abs(exponent - (-1.994687633)) < 5e-5)
    add_check("orientation_pole", "L^2 gap approaches 4pi^2", limit, 4 * math.pi ** 2, 0.01,
              abs(limit - 4 * math.pi ** 2) < 0.01)
    return {
        "soft_selector_wrong_to_correct": {str(k): v for k, v in ratios.items()},
        "symmetric_iepsilon_modulus_ratio": mod_ratio,
        "massless_gap_fit_exponent": exponent,
        "L2_gap_at_L256": limit,
        "target_4pi2": 4 * math.pi ** 2,
    }


# -----------------------------------------------------------------------------
# 3. TT projector, six-scalar no-go, edge-to-tensor and transfer dynamics
# -----------------------------------------------------------------------------

def symmetric_basis_3d() -> np.ndarray:
    basis = []
    for i in range(3):
        B = np.zeros((3, 3)); B[i, i] = 1; basis.append(B)
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        B = np.zeros((3, 3)); B[i, j] = B[j, i] = 1 / math.sqrt(2); basis.append(B)
    return np.asarray(basis)


def tt_projector_3d(k: np.ndarray):
    basis = symmetric_basis_3d()
    kh = 2 * np.sin(np.asarray(k) / 2)
    C = np.zeros((4, 6))
    for i in range(3):
        for A, B in enumerate(basis):
            C[i, A] = (B @ kh)[i]
    for A, B in enumerate(basis):
        C[3, A] = np.trace(B)
    _, s, vh = np.linalg.svd(C)
    null = vh.T[:, np.sum(s > 1e-12):]
    P = null @ null.T
    return C, P, null


def section_tt_transfer() -> dict[str, Any]:
    k = np.array([0.31, -0.22, 0.17])
    C, P, U = tt_projector_3d(k)
    peig = np.linalg.eigvalsh(P)
    rank = np.linalg.matrix_rank(P, tol=1e-12)

    # 6-scalar symmetric Hessian no-go: off-diagonal c, diagonal zero.
    t = 0.161154
    c = -0.09928408
    H6 = c * (np.ones((6, 6)) - np.eye(6))
    eig6 = np.linalg.eigvalsh(H6)

    # Six directed spatial lengths -> tensor h_ij.
    dirs = np.array([[1,0,0],[0,1,0],[0,0,1],[1,1,0],[1,0,1],[0,1,1]], float)
    dirs = dirs / np.linalg.norm(dirs, axis=1)[:, None]
    basis = symmetric_basis_3d()
    M = np.array([[n @ B @ n for B in basis] for n in dirs])
    detM = float(np.linalg.det(M))
    condM = float(np.linalg.cond(M))

    # Symplectic causal transfer.
    r = 1 / math.sqrt(3)
    kh2 = float(np.sum((2 * np.sin(k / 2)) ** 2))
    lam = r * r * kh2
    T = np.array([[1 - lam / 2, 1], [-lam * (1 - lam / 4), 1 - lam / 2]])
    J = np.array([[0, 1], [-1, 0]], float)
    sympl = np.linalg.norm(T.T @ J @ T - J)
    determinant = float(np.linalg.det(T))
    vals = np.linalg.eigvals(T)

    add_check("tt_transfer", "TT projector rank", rank, 2, 0, rank == 2)
    add_check("tt_transfer", "TT projector trace", np.trace(P), 2.0, 1e-12,
              abs(np.trace(P) - 2) < 1e-12)
    add_check("tt_transfer", "TT constraint residual", np.linalg.norm(C @ U), 0.0, 1e-12,
              np.linalg.norm(C @ U) < 1e-12)
    add_check("tt_transfer", "six-scalar Hessian degeneracy", eig6[1:].std(), 0.0, 1e-12,
              eig6[1:].std() < 1e-12,
              "Spectrum has one 5c mode and five -c modes, never 4 zero + 2 physical.")
    add_check("tt_transfer", "edge-to-tensor map determinant", detM, 1 / math.sqrt(8), 1e-12,
              abs(detM - 1 / math.sqrt(8)) < 1e-12)
    add_check("tt_transfer", "symplectic transfer determinant", determinant, 1.0, 1e-12,
              abs(determinant - 1) < 1e-12)
    add_check("tt_transfer", "symplectic residual", sympl, 0.0, 1e-12, sympl < 1e-12)
    return {
        "TT_projector_eigenvalues": peig.tolist(),
        "TT_rank": rank,
        "six_scalar_spectrum": eig6.tolist(),
        "edge_tensor_map_det": detM,
        "edge_tensor_map_condition": condM,
        "transfer_lambda": lam,
        "transfer_eigenvalues": [[float(z.real), float(z.imag)] for z in vals],
        "symplectic_residual": sympl,
    }


# -----------------------------------------------------------------------------
# 4. Flat 4D Regge lattice: Bianchi nulls and curvature-squared lifting
# -----------------------------------------------------------------------------

class FlatRegge4D:
    def __init__(self, L: int = 3):
        self.L = L
        self.d = 4
        self.pairs = list(itertools.combinations(range(5), 2))
        self.local_triangles = list(itertools.combinations(range(5), 3))
        self.opposite_pairs = [tuple(i for i in range(5) if i not in tri)
                               for tri in self.local_triangles]
        self._build()

    def vertex_id(self, coord):
        coord = np.asarray(coord, dtype=int) % self.L
        value = 0; factor = 1
        for x in coord:
            value += int(x) * factor; factor *= self.L
        return value

    def _build(self):
        edge_map = {}; edge_dirs = []; edge_mid = []; sedges = []; stris = []
        triangle_map = {}; triangle_edges = []
        pairpos = {p: i for i, p in enumerate(self.pairs)}

        def canonical(a, b):
            a = np.asarray(a, int); b = np.asarray(b, int); delta = b - a
            if np.all(delta >= 0): start, direction = a, delta
            elif np.all(delta <= 0): start, direction = b, -delta
            else: raise RuntimeError("Invalid edge")
            mask = sum((1 << i) for i in range(4) if direction[i])
            return (tuple((start % self.L).tolist()), mask), start, direction

        for bt in itertools.product(range(self.L), repeat=4):
            base = np.array(bt, int)
            for perm in itertools.permutations(range(4)):
                lifted = [base.copy()]; cur = base.copy()
                for axis in perm:
                    cur = cur.copy(); cur[axis] += 1; lifted.append(cur)
                vids = [self.vertex_id(v) for v in lifted]
                local_e = np.empty(10, int)
                for pos, (i, j) in enumerate(self.pairs):
                    key, start, direction = canonical(lifted[i], lifted[j])
                    if key not in edge_map:
                        edge_map[key] = len(edge_dirs)
                        edge_dirs.append(direction.astype(float))
                        edge_mid.append(start.astype(float) + 0.5 * direction)
                    local_e[pos] = edge_map[key]
                tri_ids = []
                for tri in self.local_triangles:
                    key = tuple(sorted(vids[i] for i in tri))
                    eids = tuple(sorted(local_e[pairpos[tuple(sorted(p))]]
                                        for p in itertools.combinations(tri, 2)))
                    if key not in triangle_map:
                        triangle_map[key] = len(triangle_edges)
                        triangle_edges.append(eids)
                    tri_ids.append(triangle_map[key])
                sedges.append(local_e); stris.append(tri_ids)
        self.directions = np.asarray(edge_dirs)
        self.midpoints = np.asarray(edge_mid)
        self.simplex_edges = np.asarray(sedges)
        self.simplex_triangles = np.asarray(stris)
        self.triangle_edges = np.asarray(triangle_edges)
        self.background_q = np.sum(self.directions ** 2, axis=1)
        self.direction_types = sorted({tuple(x.astype(int)) for x in self.directions})
        self.type_index = {x: i for i, x in enumerate(self.direction_types)}
        self.edge_type = np.array([self.type_index[tuple(x.astype(int))]
                                   for x in self.directions])

    def deficits(self, q):
        q = np.asarray(q, float)
        lq = q[self.simplex_edges]; ns = len(lq)
        qmat = np.zeros((ns, 5, 5))
        for pos, (i, j) in enumerate(self.pairs):
            qmat[:, i, j] = qmat[:, j, i] = lq[:, pos]
        gram = np.empty((ns, 4, 4))
        for i in range(1, 5):
            for j in range(1, 5):
                gram[:, i - 1, j - 1] = (qmat[:, 0, i] + qmat[:, 0, j] - qmat[:, i, j]) / 2
        inv = np.linalg.inv(gram)
        bary = np.zeros((ns, 5, 5)); bary[:, 1:, 1:] = inv
        sums = inv.sum(axis=2)
        bary[:, 0, 1:] = -sums; bary[:, 1:, 0] = -sums; bary[:, 0, 0] = inv.sum(axis=(1, 2))
        angles = np.empty((ns, 10))
        for idx, (a, b) in enumerate(self.opposite_pairs):
            cos = -bary[:, a, b] / np.sqrt(bary[:, a, a] * bary[:, b, b])
            angles[:, idx] = np.arccos(np.clip(cos, -1, 1))
        asum = np.zeros(len(self.triangle_edges))
        np.add.at(asum, self.simplex_triangles.ravel(), angles.ravel())
        return 2 * np.pi - asum

    def areas(self, q):
        qe = q[self.triangle_edges]
        qa, qb, qc = qe[:, 0], qe[:, 1], qe[:, 2]
        scalar = 0.5 * (qa + qb - qc)
        return 0.5 * np.sqrt(qa * qb - scalar ** 2)

    def action(self, q):
        return float(np.sum(self.areas(q) * self.deficits(q)))

    def q_from_mode(self, coeff, k):
        coeff = np.asarray(coeff)
        phase = self.midpoints @ k
        return self.background_q + coeff[:15][self.edge_type] * np.cos(phase) \
            + coeff[15:][self.edge_type] * np.sin(phase)

    def hessian(self, k, step=2e-4):
        n = 30; z = np.zeros(n); f0 = self.action(self.q_from_mode(z, k))
        H = np.zeros((n, n))
        cache = {}
        def f(x):
            key = tuple(np.round(x, 12))
            if key not in cache: cache[key] = self.action(self.q_from_mode(x, k))
            return cache[key]
        for i in range(n):
            ei = np.zeros(n); ei[i] = step
            H[i, i] = (f(ei) - 2 * f0 + f(-ei)) / step ** 2
        for i in range(n):
            ei = np.zeros(n); ei[i] = step
            for j in range(i + 1, n):
                ej = np.zeros(n); ej[j] = step
                H[i, j] = H[j, i] = (f(ei + ej) - f(ei - ej) - f(-ei + ej) + f(-ei - ej)) / (4 * step ** 2)
        return 0.5 * (H + H.T)

    def deficit_jacobian(self, k, step=2e-5):
        J = np.empty((len(self.triangle_edges), 30))
        for i in range(30):
            e = np.zeros(30); e[i] = step
            J[:, i] = (self.deficits(self.q_from_mode(e, k)) - self.deficits(self.q_from_mode(-e, k))) / (2 * step)
        return J

    def gauge_basis(self, k):
        vecs = []
        for mu in range(4):
            vc = np.zeros(30); vs = np.zeros(30)
            for a, nt in enumerate(self.direction_types):
                n = np.asarray(nt, float)
                factor = 4 * n[mu] * np.sin(0.5 * k @ n)
                vc[15 + a] = -factor; vs[a] = factor
            vecs.extend([vc, vs])
        G = np.column_stack(vecs)
        U, s, _ = np.linalg.svd(G, full_matrices=False)
        return U[:, s > 1e-12]


def section_flat_regge() -> dict[str, Any]:
    model = FlatRegge4D(3)
    k = (2 * np.pi / 3) * np.array([1.0, 1.0, 0.0, 0.0])
    flat_action = model.action(model.background_q)
    H = model.hessian(k)
    eig, vec = np.linalg.eigh(H)
    null = vec[:, np.abs(eig) < 1e-3]
    G = model.gauge_basis(k)
    bianchi = np.linalg.norm(H @ G) / (np.linalg.norm(H) * np.sqrt(G.shape[1]))
    # Gauge overlap with numerical null space.
    overlap_sv = np.linalg.svd(null.T @ G, compute_uv=False)

    # Identify non-gauge action-null directions.
    nong = (np.eye(30) - G @ G.T) @ null
    Us, ss, _ = np.linalg.svd(nong, full_matrices=False)
    Vspur = Us[:, ss > 1e-3]

    Jd = model.deficit_jacobian(k)
    Kcurv = Jd.T @ Jd
    spur_curv = np.linalg.eigvalsh(Vspur.T @ Kcurv @ Vspur)
    alpha = 1e-4
    Hrg = 0.5 * (H + alpha * Kcurv + (H + alpha * Kcurv).T)
    erg = np.linalg.eigvalsh(Hrg)
    null_after = int(np.sum(np.abs(erg) < 1e-3))
    bianchi_after = np.linalg.norm(Hrg @ G) / (np.linalg.norm(Hrg) * np.sqrt(G.shape[1]))

    add_check("flat_regge", "background flat action", flat_action, 0.0, 1e-10,
              abs(flat_action) < 1e-10)
    add_check("flat_regge", "raw real null dimension", null.shape[1], 10, 0,
              null.shape[1] == 10)
    add_check("flat_regge", "exact gauge real dimension", G.shape[1], 8, 0, G.shape[1] == 8)
    add_check("flat_regge", "spurious real dimension", Vspur.shape[1], 2, 0,
              Vspur.shape[1] == 2)
    add_check("flat_regge", "Bianchi residual", bianchi, 0.0, 2e-6, bianchi < 2e-6)
    add_check("flat_regge", "minimum gauge/null principal cosine", overlap_sv.min(), 1.0, 1e-5,
              overlap_sv.min() > 0.99999)
    add_check("flat_regge", "curvature term positive on spurious sector", spur_curv.min(), ">0", 0,
              spur_curv.min() > 100)
    add_check("flat_regge", "null dimension after R2 correction", null_after, 8, 0,
              null_after == 8)
    add_check("flat_regge", "Bianchi preserved after R2", bianchi_after, 0.0, 2e-6,
              bianchi_after < 2e-6)
    return {
        "lattice": {"vertices": 81, "edges": len(model.directions),
                    "triangles": len(model.triangle_edges),
                    "four_simplices": len(model.simplex_edges)},
        "background_action": flat_action,
        "small_eigenvalues": eig[np.abs(eig) < 1e-3].tolist(),
        "raw_null_dimension": int(null.shape[1]),
        "gauge_dimension": int(G.shape[1]),
        "spurious_dimension": int(Vspur.shape[1]),
        "Bianchi_residual": bianchi,
        "minimum_gauge_null_overlap": float(overlap_sv.min()),
        "spurious_curvature_eigenvalues": spur_curv.tolist(),
        "alpha_R2": alpha,
        "corrected_null_dimension": null_after,
        "corrected_Bianchi_residual": bianchi_after,
    }


# -----------------------------------------------------------------------------
# 5. Spin-2 bootstrap and universal soft coupling
# -----------------------------------------------------------------------------

def symmetric_basis_4d():
    basis = []
    for i in range(4):
        B = np.zeros((4, 4)); B[i, i] = 1; basis.append(B)
    for i in range(4):
        for j in range(i + 1, 4):
            B = np.zeros((4, 4)); B[i, j] = B[j, i] = 1 / math.sqrt(2); basis.append(B)
    return np.asarray(basis)


def spin2_quadratic_basis(k):
    basis = symmetric_basis_4d(); k = np.asarray(k, float); k2 = k @ k
    tr = np.array([np.trace(B) for B in basis])
    V = np.array([k @ B for B in basis]).T
    s = np.array([k @ B @ k for B in basis])
    return [k2 * np.eye(10), V.T @ V,
            0.5 * (np.outer(s, tr) + np.outer(tr, s)),
            k2 * np.outer(tr, tr)]


def spin2_gauge_map(k):
    basis = symmetric_basis_4d(); k = np.asarray(k, float)
    G = np.zeros((10, 4))
    for mu in range(4):
        T = np.zeros((4, 4)); T[:, mu] += k; T[mu, :] += k
        for A, B in enumerate(basis): G[A, mu] = np.sum(B * T)
    return G


def section_spin2_bootstrap() -> dict[str, Any]:
    momenta = [np.array([1,0,0,0.]), np.array([1,1,0,0.]),
               np.array([1,2,1,0.]), np.array([2,-1,1,3.])]
    cols = []
    for op in range(4):
        blocks = []
        for k in momenta:
            blocks.append((spin2_quadratic_basis(k)[op] @ spin2_gauge_map(k)).ravel())
        cols.append(np.concatenate(blocks))
    C = np.column_stack(cols)
    _, s, vh = np.linalg.svd(C, full_matrices=False)
    coeff = vh[-1] / vh[-1, 0]
    residual = np.linalg.norm(C @ coeff) / np.linalg.norm(C)
    rank = np.linalg.matrix_rank(C, tol=1e-11)

    ktest = np.array([0.31, -0.22, 0.17, 0.29])
    H = sum(coeff[i] * spin2_quadratic_basis(ktest)[i] for i in range(4))
    G = spin2_gauge_map(ktest)
    eig = np.linalg.eigvalsh(H)

    # Soft universality generic 2->2 kinematics.
    theta = 0.73; E = 1.0
    p1 = np.array([ E, 0, 0, E]); p2 = np.array([ E, 0, 0,-E])
    p3 = np.array([-E,-E*np.sin(theta),0,-E*np.cos(theta)])
    p4 = np.array([-E, E*np.sin(theta),0, E*np.cos(theta)])
    Pmom = np.column_stack([p1,p2,p3,p4])
    _, sm, vhm = np.linalg.svd(Pmom)
    r = np.linalg.matrix_rank(Pmom, tol=1e-12)
    g = vhm[r:].T[:, 0]; g /= np.mean(g)

    add_check("spin2_bootstrap", "quadratic constraint null dimension", 4-rank, 1, 0, 4-rank == 1)
    add_check("spin2_bootstrap", "derived coefficients", coeff, [1,-2,2,-1], 1e-12,
              np.max(np.abs(coeff - np.array([1,-2,2,-1]))) < 1e-12)
    add_check("spin2_bootstrap", "quadratic Ward residual", residual, 0.0, 1e-12, residual < 1e-12)
    add_check("spin2_bootstrap", "four gauge null modes", int(np.sum(np.abs(eig)<1e-10)), 4, 0,
              int(np.sum(np.abs(eig)<1e-10)) == 4)
    add_check("spin2_bootstrap", "soft coupling universality", g, np.ones(4), 1e-12,
              np.max(np.abs(g-1)) < 1e-12)
    return {
        "singular_values": s.tolist(),
        "derived_Fierz_Pauli_coefficients": coeff.tolist(),
        "Ward_residual": residual,
        "test_spectrum": eig.tolist(),
        "soft_momentum_singular_values": sm.tolist(),
        "relative_gravitational_couplings": g.tolist(),
    }


# -----------------------------------------------------------------------------
# 6. Linear ADM constraints and two physical modes
# -----------------------------------------------------------------------------

def section_linear_adm() -> dict[str, Any]:
    basis = symmetric_basis_3d()
    k = np.array([0.31, -0.22, 0.17])
    kh = 2 * np.sin(k / 2); k2 = float(kh @ kh)
    cH = np.array([kh @ B @ kh - k2*np.trace(B) for B in basis])
    cM = np.zeros((3,6))
    for i in range(3):
        for A,B in enumerate(basis): cM[i,A]=(B@kh)[i]
    F = np.zeros((4,12)); F[0,:6]=cH; F[1:,6:]=cM
    J = np.block([[np.zeros((6,6)),np.eye(6)],[-np.eye(6),np.zeros((6,6))]])
    PB = F@J@F.T
    Ctt = np.zeros((4,6))
    for i in range(3):
        for A,B in enumerate(basis): Ctt[i,A]=(B@kh)[i]
    for A,B in enumerate(basis): Ctt[3,A]=np.trace(B)
    _,_,vh=np.linalg.svd(Ctt); Utt=vh.T[:,4:]
    Z=np.block([[Utt,np.zeros((6,2))],[np.zeros((6,2)),Utt]])
    Jred=Z.T@J@Z
    Hred=np.block([[k2*np.eye(2),np.zeros((2,2))],[np.zeros((2,2)),np.eye(2)]])
    flow=np.linalg.eigvals(Jred@Hred)
    add_check("linear_adm", "constraint rank", np.linalg.matrix_rank(F), 4, 0,
              np.linalg.matrix_rank(F)==4)
    add_check("linear_adm", "linear constraint brackets", np.linalg.norm(PB), 0.0, 1e-12,
              np.linalg.norm(PB)<1e-12)
    add_check("linear_adm", "TT dimension", Utt.shape[1], 2, 0, Utt.shape[1]==2)
    add_check("linear_adm", "canonical reduced symplectic form", np.linalg.norm(Jred-np.array([[0,0,1,0],[0,0,0,1],[-1,0,0,0],[0,-1,0,0]])), 0.0, 1e-12,
              np.linalg.norm(Jred-np.array([[0,0,1,0],[0,0,0,1],[-1,0,0,0],[0,-1,0,0]]))<1e-12)
    return {"khat2":k2,"constraint_rank":int(np.linalg.matrix_rank(F)),
            "constraint_bracket_norm":float(np.linalg.norm(PB)),
            "TT_dimension":int(Utt.shape[1]),
            "reduced_H_spectrum":np.linalg.eigvalsh(Hred).tolist(),
            "flow_eigenvalues":[[float(z.real),float(z.imag)] for z in flow]}


# -----------------------------------------------------------------------------
# 7. Binary ADM Legendre transform and causal TT transfer
# -----------------------------------------------------------------------------

def sym6(vals):
    xx,yy,zz,xy,xz,yz=vals
    return np.array([[xx,xy,xz],[xy,yy,yz],[xz,yz,zz]],float)


def adm_data(q,qdot,B,N,R):
    qi=np.linalg.inv(q); sq=np.sqrt(np.linalg.det(q)); K=(qdot-B)/(2*N)
    Kup=qi@K@qi; trK=np.einsum('ij,ij->',qi,K); K2=np.einsum('ij,ij->',K,Kup)
    L=N*sq*(K2-trK**2+R); pi=sq*(Kup-qi*trK)
    pil=q@pi@q; pic=np.einsum('ij,ij->',pil,pi); pit=np.einsum('ij,ij->',q,pi)
    H=(pic-.5*pit**2)/sq-sq*R
    return L,pi,H


def section_binary_legendre_transfer() -> dict[str, Any]:
    q=sym6([1.08,.94,1.03,.055,-.038,.044]); qd=sym6([.072,-.051,.039,.028,-.019,.023])
    B=sym6([.017,-.012,.009,-.006,.004,.007]); N=1.07; R=.083
    L,pi,H=adm_data(q,qd,B,N,R)
    pqd=np.einsum('ij,ij->',pi,qd); pB=np.einsum('ij,ij->',pi,B)
    leg=pqd-N*H-pB-L

    # Binary TT coordinate register.
    nq=6; M=2**nq; Xmax=8.; dx=2*Xmax/M
    x=-Xmax+dx*np.arange(M); p=2*np.pi*np.fft.fftfreq(M,d=dx)
    F=np.fft.fft(np.eye(M),axis=0)/np.sqrt(M)
    P2=F.conj().T@np.diag(p**2)@F; P2=0.5*(P2+P2.conj().T)
    omega=.415172768553; Xop=np.diag(x)
    Htt=0.5*P2+0.5*omega**2*(Xop@Xop); Htt=0.5*(Htt+Htt.conj().T)
    dt=.02; U=expm(-1j*dt*Htt); unitarity=np.linalg.norm(U.conj().T@U-np.eye(M))
    E,V=np.linalg.eigh(Htt); UH=V.conj().T@U@V; Erec=-np.angle(np.diag(UH))/dt
    low_err=float(np.max(np.abs(Erec[:10]-E[:10])))
    ground_rel=abs(E[0]-.5*omega)/(.5*omega)
    add_check("binary_legendre", "ADM Legendre identity", abs(leg), 0.0, 1e-14, abs(leg)<1e-14)
    add_check("binary_legendre", "TT transfer unitarity", unitarity, 0.0, 1e-12, unitarity<1e-12)
    add_check("binary_legendre", "Hamiltonian recovered from transfer phases", low_err, 0.0, 1e-11, low_err<1e-11)
    add_check("binary_legendre", "binary ground energy vs continuum", ground_rel, 0.0, 1e-8, ground_rel<1e-8)
    return {"Legendre_residual":float(abs(leg)),"TT_unitarity_residual":float(unitarity),
            "max_low_energy_transfer_log_error":low_err,"ground_relative_error":float(ground_rel),
            "first_10_binary_energies":E[:10].tolist()}


# -----------------------------------------------------------------------------
# 8. Primitive growth phase uniqueness and DAG covariance
# -----------------------------------------------------------------------------

def section_growth_axioms() -> dict[str, Any]:
    M=8; values=[n for n in range(-M,M+1) if n!=0]; vi={n:i for i,n in enumerate(values)}
    rows=[]
    for n in range(-M,M+1):
        for m in range(-M,M+1):
            r=n+m
            if r < -M or r > M: continue
            row=np.zeros(len(values))
            if r!=0: row[vi[r]]+=1
            if n!=0: row[vi[n]]-=1
            if m!=0: row[vi[m]]-=1
            if np.linalg.norm(row)>0: rows.append(row)
    A=np.vstack(rows); _,s,vh=np.linalg.svd(A); rank=np.sum(s>1e-11); nv=vh[-1]
    linear=np.array(values,float); linear/=np.linalg.norm(linear); alignment=abs(nv@linear)

    # DAG covariance.
    I=np.eye(2,dtype=complex); X=np.array([[0,1],[1,0]],complex); Y=np.array([[0,-1j],[1j,0]],complex); Z=np.array([[1,0],[0,-1]],complex)
    def kron_all(ops):
        o=ops[0]
        for x in ops[1:]: o=np.kron(o,x)
        return o
    def emb(nq,mapping): return kron_all([mapping.get(i,I) for i in range(nq)])
    nq=6; dt=.18
    hA=.37*emb(nq,{0:X})+.22*emb(nq,{1:X})+.31*emb(nq,{0:Z,1:Z})
    hC=.28*emb(nq,{1:Y,2:Y})+.19*emb(nq,{2:X})+.24*emb(nq,{1:Z,2:Z})
    hB=.33*emb(nq,{4:X})+.26*emb(nq,{5:Y})+.29*emb(nq,{4:Z,5:Z})
    UA,UB,UC=[expm(-1j*dt*h) for h in [hA,hB,hC]]
    UABC=UC@UB@UA; UBAC=UC@UA@UB; UACB=UB@UC@UA
    valid=max(np.linalg.norm(UABC-UBAC),np.linalg.norm(UABC-UACB),np.linalg.norm(UBAC-UACB))
    invalid=np.linalg.norm(UABC-UB@UA@UC)
    add_check("growth_axioms", "composition equation null dimension", len(values)-rank, 1, 0,
              len(values)-rank==1)
    add_check("growth_axioms", "unique phase linearity", alignment, 1.0, 1e-12, alignment>1-1e-12)
    add_check("growth_axioms", "valid DAG linear extensions", valid, 0.0, 1e-12, valid<1e-12)
    add_check("growth_axioms", "causal order sensitivity", invalid, ">0", 0, invalid>1e-3)
    return {"composition_matrix_rank":int(rank),"null_dimension":int(len(values)-rank),
            "phase_linearity_alignment":float(alignment),"valid_extension_max_error":float(valid),
            "invalid_order_difference":float(invalid)}


# -----------------------------------------------------------------------------
# 9. Nonlinear 3+1 ADM spectral HDA (optional heavy, torch)
# -----------------------------------------------------------------------------

def nonlinear_hda_test_K2(seed=20260726):
    import torch
    torch.set_default_dtype(torch.float64)
    K=2; NG=10; physical_K=1; P=NG**3
    x=2*np.pi*np.arange(NG)/NG
    phi1=[np.ones(NG)]; dphi1=[np.zeros(NG)]; modeid=[0]
    for m in range(1,K+1):
        phi1 += [np.sqrt(2)*np.cos(m*x),np.sqrt(2)*np.sin(m*x)]
        dphi1 += [-np.sqrt(2)*m*np.sin(m*x),np.sqrt(2)*m*np.cos(m*x)]
        modeid += [m,m]
    phi1=np.asarray(phi1); dphi1=np.asarray(dphi1)
    basis=[]; db=[[],[],[]]; maxmode=[]
    for a,b,c in itertools.product(range(len(phi1)),repeat=3):
        basis.append(phi1[a][:,None,None]*phi1[b][None,:,None]*phi1[c][None,None,:])
        db[0].append(dphi1[a][:,None,None]*phi1[b][None,:,None]*phi1[c][None,None,:])
        db[1].append(phi1[a][:,None,None]*dphi1[b][None,:,None]*phi1[c][None,None,:])
        db[2].append(phi1[a][:,None,None]*phi1[b][None,:,None]*dphi1[c][None,None,:])
        maxmode.append(max(modeid[a],modeid[b],modeid[c]))
    Phi=torch.tensor(np.asarray(basis).reshape(-1,P)); DPhi=torch.tensor(np.asarray(db).reshape(3,-1,P)); NB=Phi.shape[0]
    pmask=torch.tensor(np.asarray(maxmode)<=physical_K)
    Blist=[]
    for i in range(3):
        B=np.zeros((3,3));B[i,i]=1;Blist.append(B)
    for i,j in [(0,1),(0,2),(1,2)]:
        B=np.zeros((3,3));B[i,j]=B[j,i]=1/np.sqrt(2);Blist.append(B)
    Bsym=torch.tensor(np.asarray(Blist)); freq=torch.fft.fftfreq(NG,d=1.0/NG); ik=1j*freq
    def sd(field,axis):
        FF=torch.fft.fftn(field,dim=(0,1,2)); shape=[1]*field.ndim; shape[axis]=NG
        return torch.fft.ifftn(FF*ik.reshape(shape),dim=(0,1,2)).real
    def comp(c):return torch.einsum('ab,bp->pa',c,Phi)
    def dcomp(c):return torch.einsum('ab,ibp->ipa',c,DPhi)
    def mat(c):return torch.einsum('pa,aij->pij',c,Bsym)
    def geom(qc):
        q=mat(comp(qc)); dc=dcomp(qc); dq=torch.stack([mat(dc[a]) for a in range(3)])
        qi=torch.linalg.inv(q); sq=torch.sqrt(torch.linalg.det(q)); Gamma=torch.zeros((P,3,3,3))
        for kk in range(3):
            for i in range(3):
                for j in range(3):
                    tot=torch.zeros(P)
                    for l in range(3):tot+=.5*qi[:,kk,l]*(dq[i,:,j,l]+dq[j,:,i,l]-dq[l,:,i,j])
                    Gamma[:,kk,i,j]=tot
        Gf=Gamma.reshape(NG,NG,NG,3,3,3); dG=torch.stack([sd(Gf,a).reshape(P,3,3,3) for a in range(3)])
        Ric=torch.zeros((P,3,3))
        for i in range(3):
            for j in range(3):
                tot=torch.zeros(P)
                for kk in range(3):
                    tot+=dG[kk,:,kk,i,j]-dG[j,:,kk,i,kk]
                    for l in range(3):tot+=Gamma[:,kk,i,j]*Gamma[:,l,kk,l]-Gamma[:,l,i,kk]*Gamma[:,kk,j,l]
                Ric[:,i,j]=tot
        R=torch.einsum('pij,pij->p',qi,Ric);return q,qi,sq,Gamma,R
    def HH(qc,pc,Nc):
        q,qi,sq,Gamma,R=geom(qc);pi=mat(comp(pc));pil=q@pi@q
        kin=torch.einsum('pij,pij->p',pil,pi)-.5*torch.einsum('pij,pij->p',q,pi)**2
        dens=kin/sq-sq*R;Nf=torch.einsum('b,bp->p',Nc,Phi);return torch.mean(Nf*dens)
    def DD(qc,pc,Vc):
        q,qi,sq,Gamma,R=geom(qc);pi=mat(comp(pc));pif=pi.reshape(NG,NG,NG,3,3)
        dpi=torch.stack([sd(pif,a).reshape(P,3,3) for a in range(3)]);div=torch.zeros((P,3))
        for kk in range(3):
            tot=torch.zeros(P)
            for j in range(3):
                tot+=dpi[j,:,j,kk]
                for l in range(3):tot+=Gamma[:,kk,j,l]*pi[:,j,l]
            div[:,kk]=tot
        Hi=-2*torch.einsum('pik,pk->pi',q,div);Vf=torch.einsum('ib,bp->pi',Vc,Phi);return torch.mean(torch.einsum('pi,pi->p',Vf,Hi))
    def PB(F,G,q,p):
        Fq,Fp=torch.autograd.grad(F,(q,p),create_graph=True,retain_graph=True);Gq,Gp=torch.autograd.grad(G,(q,p),create_graph=True,retain_graph=True)
        return torch.sum(Fq*Gp-Fp*Gq)
    rng=np.random.default_rng(seed);qc=torch.zeros((6,NB),requires_grad=True);pc=torch.zeros((6,NB),requires_grad=True)
    with torch.no_grad():
        qc[0,0]=qc[1,0]=qc[2,0]=1; pert=torch.tensor(rng.normal(size=(6,NB)));mom=torch.tensor(rng.normal(size=(6,NB)))
        pert[:,~pmask]=0;mom[:,~pmask]=0;pert[:,0]=0;qc+=.003*pert;pc+=.002*mom
    def rs(scale):
        a=torch.zeros(NB);v=torch.tensor(scale*rng.normal(size=NB));a[pmask]=v[pmask];return a
    def rv(scale):
        a=torch.zeros((3,NB));v=torch.tensor(scale*rng.normal(size=(3,NB)));a[:,pmask]=v[:,pmask];return a
    N=rs(.08);M=rs(.08);V=rv(.05);W=rv(.05);HN=HH(qc,pc,N);HM=HH(qc,pc,M);DV=DD(qc,pc,V);DW=DD(qc,pc,W)
    lhs=[PB(DV,DW,qc,pc),PB(DV,HN,qc,pc),PB(HN,HM,qc,pc)]
    def sf(c):return torch.einsum('b,bp->p',c,Phi).reshape(NG,NG,NG)
    def vf(c):return torch.einsum('ib,bp->pi',c,Phi).reshape(NG,NG,NG,3)
    def ps(f):return torch.einsum('bp,p->b',Phi,f.reshape(P))/P
    def pv(f):return torch.einsum('bp,pi->ib',Phi,f.reshape(P,3))/P
    Nf=sf(N);Mf=sf(M);Vf=vf(V);Wf=vf(W);dN=torch.stack([sd(Nf,a) for a in range(3)],dim=-1);dM=torch.stack([sd(Mf,a) for a in range(3)],dim=-1)
    dV=torch.zeros((NG,NG,NG,3,3));dW=torch.zeros_like(dV)
    for j in range(3):
        for i in range(3):dV[...,j,i]=sd(Vf[...,i],j);dW[...,j,i]=sd(Wf[...,i],j)
    VW=torch.einsum('...j,...ji->...i',Vf,dW)-torch.einsum('...j,...ji->...i',Wf,dV);VdN=torch.einsum('...i,...i->...',Vf,dN)
    qnow,qinow,_,_,_=geom(qc);beta=torch.einsum('...ij,...j->...i',qinow.reshape(NG,NG,NG,3,3),Nf[...,None]*dM-Mf[...,None]*dN)
    rhs=[DD(qc,pc,pv(VW)),HH(qc,pc,ps(VdN)),DD(qc,pc,pv(beta))]
    rel=lambda a,b:float((torch.abs(a-b)/(torch.abs(a)+torch.abs(b)+1e-30)).detach())
    return [rel(lhs[i],rhs[i]) for i in range(3)], NB


def section_nonlinear_hda() -> dict[str, Any]:
    try:
        errs, NB = nonlinear_hda_test_K2()
    except ImportError as exc:
        add_check("nonlinear_hda", "torch available", repr(exc), "installed", None, False)
        return {"skipped": True, "reason": repr(exc)}
    labels=["DD","DH","HH"]
    tolerances=[1e-10,1e-8,2e-5]
    for lab,e,tol in zip(labels,errs,tolerances):
        add_check("nonlinear_hda",f"3+1 nonlinear {lab} residual",e,0.0,tol,e<tol)
    return {"retained_K":2,"physical_K":1,"basis_modes_per_field":int(NB),
            "canonical_variables":int(12*NB),"residuals":dict(zip(labels,errs))}


# -----------------------------------------------------------------------------
# 10. Binary two-polarization critical phase (optional stochastic)
# -----------------------------------------------------------------------------

def section_critical_phase(profile: str) -> dict[str, Any]:
    try:
        from numba import njit
    except ImportError as exc:
        add_check("critical_phase", "numba available", repr(exc), "installed", None, False)
        return {"skipped":True,"reason":repr(exc)}

    @njit
    def neighbors(L):
        N=L**4; neigh=np.empty((N,8),np.int64); coords=np.empty((N,4),np.int64)
        strides=np.array([1,L,L*L,L*L*L],np.int64)
        for idx in range(N):
            for mu in range(4):
                st=strides[mu];c=(idx//st)%L;coords[idx,mu]=c
                neigh[idx,2*mu]=idx+st if c<L-1 else idx-(L-1)*st
                neigh[idx,2*mu+1]=idx-st if c>0 else idx+(L-1)*st
        return neigh,coords
    @njit
    def wolff(s,neigh,beta,stack,cluster,marks,mid):
        N=s.size;padd=1-math.exp(-2*beta);seed=np.random.randint(N);target=s[seed]
        stack[0]=seed;top=1;marks[seed]=mid;csize=0
        while top:
            top-=1;site=stack[top];cluster[csize]=site;csize+=1
            for a in range(8):
                nb=neigh[site,a]
                if marks[nb]!=mid and s[nb]==target and np.random.random()<padd:
                    marks[nb]=mid;stack[top]=nb;top+=1
        for i in range(csize):s[cluster[i]]=-s[cluster[i]]
    @njit
    def measure(s,coords,L,ct,st):
        N=s.size;M=0.
        for i in range(N):M+=s[i]
        Sk=0.
        for mu in range(4):
            re=0.;im=0.
            for i in range(N):
                c=coords[i,mu];re+=s[i]*ct[c];im+=s[i]*st[c]
            Sk+=(re*re+im*im)/N
        return M/N,M*M/N,Sk/4
    @njit
    def sim(L,beta,ntherm,nmeas,seed):
        np.random.seed(seed);neigh,coords=neighbors(L);N=L**4
        s1=np.where(np.random.random(N)<.5,-1,1).astype(np.int8);s2=np.where(np.random.random(N)<.5,-1,1).astype(np.int8)
        stack=np.empty(N,np.int64);cluster=np.empty(N,np.int64);m1=np.zeros(N,np.int64);m2=np.zeros(N,np.int64);id1=1;id2=1
        ct=np.empty(L);st=np.empty(L)
        for c in range(L):
            ang=2*math.pi*c/L;ct[c]=math.cos(ang);st[c]=math.sin(ang)
        for _ in range(ntherm):wolff(s1,neigh,beta,stack,cluster,m1,id1);id1+=1;wolff(s2,neigh,beta,stack,cluster,m2,id2);id2+=1
        sm2=0.;sm4=0.;sa=0.;S0=0.;Sk=0.
        for _ in range(nmeas):
            for z in range(2):wolff(s1,neigh,beta,stack,cluster,m1,id1);id1+=1;wolff(s2,neigh,beta,stack,cluster,m2,id2);id2+=1
            a,A0,Ak=measure(s1,coords,L,ct,st);b,B0,Bk=measure(s2,coords,L,ct,st)
            sm2+=.5*(a*a+b*b);sm4+=.5*(a**4+b**4);sa+=.5*(abs(a)+abs(b));S0+=.5*(A0+B0);Sk+=.5*(Ak+Bk)
        inv=1/nmeas;mm2=sm2*inv;mm4=sm4*inv;ma=sa*inv;S0*=inv;Sk*=inv
        U=1-mm4/(3*mm2*mm2);chi=N*(mm2-ma*ma);xi=.5/math.sin(math.pi/L)*math.sqrt(max(S0/Sk-1,0))
        return U,chi,xi/L,mm2
    _=sim(4,.14955,10,10,1)
    Ls=[6,8,10,12]; beta=.14955
    nmeas=1800 if profile=="quick" else 3200
    rows=[]
    for L in Ls:
        vals=[]
        reps=2 if profile=="quick" else 3
        for r in range(reps): vals.append(sim(L,beta,900 if profile=="quick" else 1300,nmeas,50000+100*L+r))
        arr=np.asarray(vals);rows.append({"L":L,"Binder":float(arr[:,0].mean()),"chi":float(arr[:,1].mean()),"xi_over_L":float(arr[:,2].mean()),"m2":float(arr[:,3].mean())})
    df=pd.DataFrame(rows);Larr=df.L.to_numpy(float)
    pchi=float(np.polyfit(np.log(Larr),np.log(df.chi),1)[0]);pm2=float(-np.polyfit(np.log(Larr),np.log(df.m2),1)[0]);zgap=float(-np.polyfit(np.log(Larr),np.log(1/(df.xi_over_L*Larr)),1)[0])
    spread=float(df.xi_over_L.max()-df.xi_over_L.min())
    add_check("critical_phase","xi/L approximately size independent",spread,0.0,0.12,spread<0.12,
              "Stochastic finite-size evidence in the reduced two-TT-bit model.")
    add_check("critical_phase","mass gap exponent",zgap,1.0,0.30,abs(zgap-1)<0.30)
    add_check("critical_phase","susceptibility grows sub-volume",pchi,"0<p<4",0,0<pchi<4)
    add_check("critical_phase","order parameter critical exponent",pm2,2.0,0.5,abs(pm2-2)<0.5)
    return {"beta":beta,"replicates":reps,"measurements_per_replica":nmeas,"rows":rows,
            "xi_over_L_spread":spread,"susceptibility_exponent":pchi,"m2_exponent":pm2,"gap_exponent":zgap,
            "scope_note":"Demonstrates a critical phase in the reduced two-polarization binary model, not yet the full edge-Regge partition sum."}


# -----------------------------------------------------------------------------
# Report generation
# -----------------------------------------------------------------------------

def write_outputs(outdir: Path, profile: str):
    outdir.mkdir(parents=True, exist_ok=True)
    summary = {
        "profile": profile,
        "generated_utc": pd.Timestamp.utcnow().isoformat(),
        "checks_total": len(CHECKS),
        "checks_passed": sum(c.passed for c in CHECKS),
        "checks_failed": sum(not c.passed for c in CHECKS),
        "all_passed": all(c.passed for c in CHECKS),
        "checks": [asdict(c) for c in CHECKS],
        "sections": scalarize(RESULTS),
        "scientific_scope": {
            "verified": "Decisive finite-model, bootstrap, causal-transfer, ADM and reduced critical-phase calculations.",
            "not_proved": "That the full microscopic edge-bit causal Regge partition sum nonperturbatively flows to the demonstrated TT critical fixed point."
        }
    }
    (outdir / "BCQG_UNIFIED_RESULTS.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False),encoding="utf-8")
    lines=["# BCQG Unified Verification Report","",f"Profile: **{profile}**","",
           f"Checks passed: **{summary['checks_passed']}/{summary['checks_total']}**","",
           "## Check table","","| Section | Check | Status | Value | Expected | Tolerance |","|---|---|---:|---:|---:|---:|"]
    for c in CHECKS:
        status="PASS" if c.passed else "FAIL"
        lines.append(f"| {c.section} | {c.name} | {status} | `{c.value}` | `{c.expected}` | `{c.tolerance}` |")
    lines += ["","## Scientific conclusion","",
              "The suite verifies internal consistency of the constructed BCQG chain across exact finite RG, flat-Regge Bianchi modes, spurious-mode lifting, spin-2 bootstrap, canonical constraints, causal transfer and the reduced binary TT critical phase.","",
              "It does **not** prove that the full microscopic edge-bit causal Regge sum flows nonperturbatively to that critical fixed point. That remains the single principal open calculation.",""]
    for name,data in RESULTS.items():
        lines += [f"## {name}","","```json",json.dumps(scalarize(data),indent=2,ensure_ascii=False),"```",""]
    (outdir / "BCQG_UNIFIED_REPORT.md").write_text("\n".join(lines),encoding="utf-8")
    return summary


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--profile",choices=["quick","full"],default="full")
    parser.add_argument(
        "--output",
        default="verification_results",
        help="Output directory (default: ./verification_results)",
    )
    parser.add_argument("--skip-flat-regge",action="store_true")
    parser.add_argument("--skip-hda",action="store_true")
    parser.add_argument("--skip-critical",action="store_true")
    args=parser.parse_args()
    timed("finite_rg",section_exact_finite_rg)
    timed("orientation_pole",section_orientation_and_pole)
    timed("tt_transfer",section_tt_transfer)
    if not args.skip_flat_regge: timed("flat_regge",section_flat_regge)
    timed("spin2_bootstrap",section_spin2_bootstrap)
    timed("linear_adm",section_linear_adm)
    timed("binary_legendre",section_binary_legendre_transfer)
    timed("growth_axioms",section_growth_axioms)
    if not args.skip_hda: timed("nonlinear_hda",section_nonlinear_hda)
    if not args.skip_critical: timed("critical_phase",lambda:section_critical_phase(args.profile))
    summary=write_outputs(Path(args.output),args.profile)
    print("\n=== FINAL SUMMARY ===")
    print(json.dumps({k:summary[k] for k in ["checks_total","checks_passed","checks_failed","all_passed"]},indent=2))
    if not summary["all_passed"]:
        raise SystemExit(2)

if __name__=="__main__":main()
