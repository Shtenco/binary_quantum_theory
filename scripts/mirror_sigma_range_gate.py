#!/usr/bin/env python3
"""Finite mirror-mode gap/range gate on the 16-cell Q4 block.

The microscopic mirror order is a Z2 order parameter, so it has no Goldstone
mode. A long-range force therefore requires a parametrically light collective
sigma excitation (typically near a critical point), not merely the existence of
the two ordered mirror vacua.

This gate diagonalizes the lowest three levels of the same 16-qubit Q4
transverse-field Ising Hamiltonian used by mirror_order_16cell_gate.py and
records the gap outside the lowest two-state mirror sector,

    Delta_sigma^(16)(h) = E2 - E0.

At small h/J this approaches the exact classical one-defect cost 8J. The finite
Q4 cluster shows softening around its crossover but no vanishing gap. The
physical mediator range remains conditional on the continuum/refined limit and
the conversion of J to physical energy:

    lambda_sigma = hbar c_sigma / Delta_sigma.

This is a finite range falsifier, not a thermodynamic critical-exponent theorem.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh


N = 16
DIM = 1 << N
J = 1.0
EDGES = [(v, v ^ (1 << b)) for v in range(16) for b in range(4) if v < (v ^ (1 << b))]


def precompute():
    idx = np.arange(DIM, dtype=np.int64)
    flips = [idx ^ (1 << i) for i in range(N)]
    diag = np.zeros(DIM, dtype=float)
    m2 = np.zeros(DIM, dtype=float)
    for s in range(DIM):
        z = [1 - 2 * ((s >> i) & 1) for i in range(N)]
        diag[s] = -J * sum(z[a] * z[b] for a, b in EDGES)
        m = sum(z) / N
        m2[s] = m * m
    return flips, diag, m2


FLIPS, DIAG, M2 = precompute()


def lowest(h):
    def mv(vec):
        out = DIAG * vec
        for f in FLIPS:
            out += -h * vec[f]
        return out

    H = LinearOperator((DIM, DIM), matvec=mv, dtype=float)
    vals, vecs = eigsh(H, k=3, which="SA", tol=1e-10, maxiter=3000)
    order = np.argsort(vals)
    vals = vals[order]
    psi0 = vecs[:, order[0]]
    sigma2 = float(np.sum(np.abs(psi0) ** 2 * M2))
    return {
        "h_over_J": float(h / J),
        "E0_over_J": float(vals[0] / J),
        "E1_over_J": float(vals[1] / J),
        "E2_over_J": float(vals[2] / J),
        "doublet_split_over_J": float((vals[1] - vals[0]) / J),
        "gap_outside_lowest_two_over_J": float((vals[2] - vals[0]) / J),
        "Sigma_squared": sigma2,
    }


def run():
    hs = (0.2, 0.5, 1.0, 1.5, 2.0, 2.25, 2.5, 2.625, 2.75, 3.0, 3.5, 4.0)
    rows = [lowest(h) for h in hs]
    low = rows[0]
    soft = min(rows, key=lambda r: r["gap_outside_lowest_two_over_J"])
    classical_gap = 8.0
    low_gap = low["gap_outside_lowest_two_over_J"]

    passed = (
        abs(classical_gap - 8.0) < 1e-15
        and 7.5 < low_gap < 8.1
        and low["Sigma_squared"] > 0.99
        and soft["gap_outside_lowest_two_over_J"] > 0.0
        and soft["gap_outside_lowest_two_over_J"] < low_gap
    )

    return {
        "status": "finite 16-cell mirror-mode gap/range gate",
        "passed": bool(passed),
        "classical_h_zero_local_defect_gap_over_J": classical_gap,
        "scan": rows,
        "small_h_result": {
            "h_over_J": low["h_over_J"],
            "Delta16_over_J": low_gap,
            "range_formula": "lambda_sigma = hbar*c_sigma/(Delta16_over_J*J)",
            "range_over_ell_formula": "lambda_sigma/ell = 1/(Delta16_over_J*j_sigma), j_sigma=J*ell/(hbar*c_sigma)",
        },
        "finite_Q4_softest_scan_point": soft,
        "main_result": (
            "The ordered seed does not contain an automatically long-range Z2 mediator. Deep in the ordered phase "
            "the first excitation outside the mirror doublet is O(8J). The finite Q4 crossover softens this gap "
            "but does not close it. Macroscopic range requires a refined/thermodynamic near-critical sigma mode "
            "or a separately light mediator."
        ),
        "critical_requirement": (
            "For r >> ell, a mirror force needs m_sigma*r <= O(1). In a relativistic continuum identification "
            "this means Delta_sigma << hbar*c_sigma/r. The present finite seed alone does not establish that."
        ),
        "scope": (
            "E2-E0 is a finite two-level-excluded spectral gap. Calling it a physical sigma mass requires a "
            "continuum mode identification, time normalization, and refined-limit dispersion."
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
