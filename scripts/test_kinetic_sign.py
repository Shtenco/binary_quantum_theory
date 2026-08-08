#!/usr/bin/env python3
"""TT / trace Rayleigh signs for H_kin = -H_Regge on FlatRegge4D."""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from bcqg_unified_verification import FlatRegge4D

SYM = [(i, j) for i in range(4) for j in range(i, 4)]


def h_from_v(v):
    H = np.zeros((4, 4))
    for a, (i, j) in enumerate(SYM):
        H[i, j] = H[j, i] = v[a]
    return H


def project_TT(h, k):
    k = np.asarray(k, float)
    k2 = float(np.dot(k, k))
    R = k @ h
    A = k2 * np.eye(4) + np.outer(k, k)
    xi = np.linalg.solve(A, R)
    ht = h - (np.outer(k, xi) + np.outer(xi, k))
    return ht - (np.trace(ht) / 4.0) * np.eye(4)


def main():
    m = FlatRegge4D(3)
    M = np.zeros((15, 10))
    for a, n in enumerate(m.direction_types):
        n = np.asarray(n, float)
        for b, (mu, nu) in enumerate(SYM):
            M[a, b] = n[mu] ** 2 if mu == nu else 2.0 * n[mu] * n[nu]

    k = (2 * np.pi / 3) * np.array([1.0, 0.0, 0.0, 0.0])
    H = 0.5 * (m.hessian(k) + m.hessian(k).T)
    Hkin = -H
    G = m.gauge_basis(k)
    bianchi = np.linalg.norm(Hkin @ G) / (
        np.linalg.norm(Hkin) * np.sqrt(G.shape[1]) + 1e-30
    )

    rng = np.random.default_rng(0)
    tt_vals = []
    for _ in range(40):
        h = h_from_v(rng.normal(size=10))
        htt = project_TT(h, k)
        nrm = np.sqrt(np.sum(htt * htt)) + 1e-30
        htt /= nrm
        e15 = M @ np.array([htt[i, j] for i, j in SYM])
        v = np.zeros(30)
        v[:15] = e15
        tt_vals.append(float(v @ Hkin @ v) / (float(np.dot(v, v)) + 1e-30))

    htr = np.eye(4) / 2.0
    e15 = M @ np.array([htr[i, j] for i, j in SYM])
    v = np.zeros(30)
    v[:15] = e15
    tr_val = float(v @ Hkin @ v) / (float(np.dot(v, v)) + 1e-30)

    tt_vals = np.array(tt_vals)
    print("H_kin = -H_Regge")
    print(f"  TT mean={tt_vals.mean():.4f}  min={tt_vals.min():.4f}  all>0={np.all(tt_vals > 0)}")
    print(f"  pure-trace Rayleigh={tr_val:.4f}  (<0 expected Euclidean)")
    print(f"  Bianchi residual={bianchi:.2e}  gauge_dim={G.shape[1]}")
    ok = bool(np.all(tt_vals > 0) and tr_val < 0 and bianchi < 1e-5)
    print(f"PASS={ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
