#!/usr/bin/env python3
"""Internal SU(2)/SO(3) isotropy self-averaging proxy.

This is deliberately NOT the Plebanski wedge simplicity calculation.  It tests
only the statistical statement that an extensive symmetric second-rank tensor
built from isotropically distributed qubit Bloch vectors self-averages toward a
multiple of the identity with N^{-1/2} fluctuations.

The actual microscopic gravity test must compute X^ij = B^i cup/wedge B^j from
the coarse 2-cochains.  This proxy exists to distinguish a plausible symmetry
mechanism from inserting an explicit simplicity penalty.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def defect(vectors: np.ndarray) -> float:
    X = vectors.T @ vectors
    tf = X - np.eye(3) * np.trace(X) / 3.0
    return float(np.linalg.norm(tf) / np.linalg.norm(X))


def sample_vectors(rng: np.random.Generator, n: int, z_scale: float) -> np.ndarray:
    v = rng.normal(size=(n, 3))
    v[:, 2] *= z_scale
    v /= np.linalg.norm(v, axis=1)[:, None]
    return v


def run(seed: int = 260809, replicates: int = 300) -> dict[str, object]:
    rng = np.random.default_rng(seed)
    sizes = np.array([16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192])

    iso_rows = []
    means = []
    for n in sizes:
        reps = replicates if n <= 1024 else max(100, replicates // 2)
        vals = [defect(sample_vectors(rng, int(n), 1.0)) for _ in range(reps)]
        mean = float(np.mean(vals))
        means.append(mean)
        iso_rows.append({
            "N": int(n),
            "replicates": reps,
            "mean_defect": mean,
            "std_defect": float(np.std(vals)),
        })

    exponent = float(np.polyfit(np.log(sizes), np.log(means), 1)[0])

    # Anisotropic negative controls: if internal isotropy is not present the
    # traceless tensor need not self-average to zero.
    aniso_rows = []
    for z_scale in (1.5, 2.0, 3.0):
        vals = []
        for n in (1024, 8192):
            local = [
                defect(sample_vectors(rng, n, z_scale))
                for _ in range(max(80, replicates // 3))
            ]
            vals.append({"N": n, "mean_defect": float(np.mean(local))})
        aniso_rows.append({"z_scale": z_scale, "rows": vals})

    passed = abs(exponent + 0.5) < 0.05 and all(
        row["rows"][-1]["mean_defect"] > 0.10 for row in aniso_rows
    )

    return {
        "status": "statistical internal-isotropy proxy, not Plebanski simplicity",
        "passed": bool(passed),
        "seed": seed,
        "isotropic": {
            "rows": iso_rows,
            "power_exponent_mean_defect_vs_N": exponent,
            "expected_independent_self_averaging_exponent": -0.5,
        },
        "anisotropic_negative_controls": aniso_rows,
        "conditional_lesson": "If the true extensive coarse wedge tensor X^ij has unbroken internal SO(3) symmetry and finite-correlation self-averaging, its traceless part can become irrelevant without an explicit simplicity penalty.",
        "warning": "The true gravity gate is Delta_simp from X^ij = B^i wedge/cup B^j. Bloch-vector covariance must never be substituted for that observable.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=260809)
    parser.add_argument("--replicates", type=int, default=300)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.replicates < 20:
        parser.error("use at least 20 replicates")
    result = run(args.seed, args.replicates)
    text = json.dumps(result, ensure_ascii=False, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
