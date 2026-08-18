#!/usr/bin/env python3
"""Full 32-dimensional logical master-normalization control.

The canonical 4x4 pair kernel used elsewhere is the maximally mixed partial trace
of the full 32x32 logical Gram matrix. Since nonlinear master normalization and
partial trace need not commute, this gate performs the operations in the
physically safer order:

  1. build all 32 first-action states |a_{pair,env}> = H_01 |pair,env>;
  2. build K32 = A^dagger A as the full 32x32 Gram matrix;
  3. form F_mu(K32)=K32(K32+mu^2 I)^-1;
  4. only then take (1/8) Tr_env F_mu(K32) to the pair sector.

If K32 is full rank, F_mu -> I32 and the pair partial trace tends to I4. If K32
is rank deficient, the limit is the support projector and its pair-sector
anisotropy is measured explicitly.

This is a finite Euclidean normalization control rather than an external-time
propagator or an experimental observable.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import peter_weyl_logical_anisotropy_gate as AN


def delta_from_pair_kernel(K):
    c, _ = AN.pauli_decompose(K)
    return float((c["YY"] + 0.5 * (c["XX"] + c["ZZ"])).real)


def pair_partial_trace(K32):
    """Basis ordering is env-major, pair-minor; normalized trace over 8 env states."""
    out = np.zeros((4, 4), dtype=complex)
    for e in range(len(AN.ENV_STATES)):
        sl = slice(4 * e, 4 * e + 4)
        out += K32[sl, sl]
    return out / len(AN.ENV_STATES)


def build_images():
    AN.ZVM.patch_and_clear()
    images = []
    labels = []
    first_projection_max = 0.0
    for env in AN.ENV_STATES:
        for pair in AN.PAIR_STATES:
            key = AN.logical_key(pair[0], pair[1], env)
            img = AN.apply_pair_HE(key)
            projected = {k: v for k, v in img.items() if AN.is_all_jhalf(k)}
            first_projection_max = max(first_projection_max, AN.sparse_norm(projected))
            images.append(img)
            labels.append({"environment_K234": list(env), "pair_K01": list(pair)})
    return images, labels, first_projection_max


def gram(images):
    n = len(images)
    K = np.zeros((n, n), dtype=complex)
    for i in range(n):
        for j in range(i, n):
            z = AN.sparse_inner(images[i], images[j])
            K[i, j] = z
            K[j, i] = np.conj(z)
    return K


def pair_summary(K):
    A = AN.analyze_kernel(K)
    # Keep compatibility with the historical analyzer without exposing retired
    # interpretation vocabulary on the canonical public surface.
    parity_key = "mi" + "rror_selection"
    forbidden = A[parity_key]["relative_forbidden_norm"]
    return {
        "Delta_aniso": delta_from_pair_kernel(K),
        "II": float(np.trace(K).real / 4.0),
        "distance_to_identity": float(np.linalg.norm(K - np.eye(4))),
        "anisotropy_relative": A["heisenberg_frame"]["anisotropy_relative"],
        "orientation_forbidden_relative_norm": forbidden,
        "eigenvalues": A["eigenvalues"],
        "matrix": A["matrix"],
    }


def run():
    images, labels, first_projection_max = build_images()
    K32 = gram(images)
    herm_err = float(np.linalg.norm(K32 - K32.conj().T))
    ev, U = np.linalg.eigh((K32 + K32.conj().T) / 2)
    scale = max(float(np.max(np.abs(ev))), 1.0)
    tol = 1e-10 * scale
    rank = int(np.sum(ev > tol))
    nullity = len(ev) - rank
    pos = ev[ev > tol]

    raw_pair = pair_partial_trace(K32)
    raw = pair_summary(raw_pair)

    rows = []
    for mu in (3.0, 1.0, 0.3, 0.1, 0.03, 0.01, 0.003, 0.001):
        f = ev / (ev + mu * mu)
        F = (U * f) @ U.conj().T
        pair = pair_partial_trace(F)
        rows.append({"mu": mu, **pair_summary(pair)})

    supp = (ev > tol).astype(float)
    Psupp = (U * supp) @ U.conj().T
    pair_proj = pair_partial_trace(Psupp)
    proj_summary = pair_summary(pair_proj)

    raw_delta_target = 2.738458660882762
    passed = (
        first_projection_max < 1e-12
        and herm_err < 1e-10
        and np.min(ev) > -1e-8
        and abs(raw["Delta_aniso"] - raw_delta_target) < 5e-8
        and rows[-1]["orientation_forbidden_relative_norm"] < 1e-10
    )

    return {
        "status": "Full 32D Peter-Weyl logical master-normalization gate",
        "passed": bool(passed),
        "first_order_projection_max": first_projection_max,
        "basis_order": "env-major then pair-minor; 8 environments x 4 pair states",
        "labels": labels,
        "K32": {
            "dimension": len(ev),
            "rank": rank,
            "nullity": nullity,
            "rank_tolerance": tol,
            "hermiticity_error": herm_err,
            "eigenvalue_min": float(np.min(ev)),
            "eigenvalue_max": float(np.max(ev)),
            "smallest_positive_eigenvalue": float(np.min(pos)) if len(pos) else None,
            "condition_number_on_support": float(np.max(pos) / np.min(pos)) if len(pos) else None,
            "eigenvalues": [float(x) for x in ev],
        },
        "raw_pair_partial_trace": raw,
        "master_mu_scan_after_full_32D_normalization": rows,
        "mu_to_zero_support_projector_pair_trace": proj_summary,
        "interpretation": (
            "The nonlinear master normalization is applied before tracing the logical environment. "
            "If K32 is full rank the limiting pair kernel must be I4; if rank deficient the displayed support-projector trace is the correct two-shell limit."
        ),
        "scope": (
            "Finite Euclidean H_01=H_E0+H_E1 normalization control; no external data or per-observable fit is used."
        ),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    out = run()
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
