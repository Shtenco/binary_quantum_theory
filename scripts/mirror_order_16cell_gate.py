#!/usr/bin/env python3
"""Microscopic 16-cell -> staggered mirror order gate.

The 16 tetrahedra of the 16-cell boundary are naturally labelled by four-bit
strings: choose one vertex from each of four antipodal pairs. Two tetrahedra
share a triangular face iff their labels differ in one bit, so the dual graph
is the 4D hypercube Q4.

The geometric Bell/gluing rule reverses oriented Y across a shared face.
Because Q4 is bipartite, define eta_v=(-1)^popcount(v) and the staggered
orientation variable sigma_v=eta_v Y_v. Then the required Y_v Y_w=-1 becomes
sigma_v sigma_w=+1 on every dual edge.

This gate verifies:
- Q4 dual combinatorics;
- two exact classical mirror vacua Sigma=+/-1;
- exact local-defect and domain-wall costs;
- a sparse 16-qubit transverse-field Ising control showing an ordered low-energy
  mirror doublet for small transverse field.

It is a finite microscopic order-parameter bridge, not a derivation of the
physical force coupling alpha.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh


N = 16
DIM = 1 << N


def dual_edges():
    return [(v, v ^ (1 << b)) for v in range(16) for b in range(4) if v < (v ^ (1 << b))]


EDGES = dual_edges()
ETA = np.array([1 if (v.bit_count() % 2 == 0) else -1 for v in range(16)], dtype=int)


def classical_gate(J=1.0):
    degrees = [0] * 16
    for a, b in EDGES:
        degrees[a] += 1
        degrees[b] += 1

    vacua = {}
    for chi in (+1, -1):
        Y = chi * ETA
        sigma = ETA * Y
        edge_products = [int(Y[a] * Y[b]) for a, b in EDGES]
        energy = J * sum(edge_products)
        vacua[str(chi)] = {
            "Sigma": float(np.mean(sigma)),
            "all_Y_edge_products_minus_one": all(x == -1 for x in edge_products),
            "gluing_Y_energy": float(energy),
        }

    Y0 = ETA.copy()
    E0 = J * sum(Y0[a] * Y0[b] for a, b in EDGES)
    Y1 = Y0.copy()
    Y1[0] *= -1
    E1 = J * sum(Y1[a] * Y1[b] for a, b in EDGES)

    Ydw = Y0.copy()
    for v in range(16):
        if v & 1:
            Ydw[v] *= -1
    Edw = J * sum(Ydw[a] * Ydw[b] for a, b in EDGES)
    frustrated = sum(Ydw[a] * Ydw[b] == +1 for a, b in EDGES)

    return {
        "dual_vertices": 16,
        "dual_edges": len(EDGES),
        "degrees": degrees,
        "all_degree_four": all(d == 4 for d in degrees),
        "bipartite_eta": ETA.tolist(),
        "edge_eta_products_all_minus_one": all(ETA[a] * ETA[b] == -1 for a, b in EDGES),
        "vacua": vacua,
        "single_orientation_flip_cost_over_J": float((E1 - E0) / J),
        "half_hypercube_domain_wall_frustrated_edges": int(frustrated),
        "half_hypercube_domain_wall_cost_over_J": float((Edw - E0) / J),
    }


def quantum_scan(h_values=(0.2, 0.5, 1.0, 2.0, 3.0, 4.0), J=1.0):
    idx = np.arange(DIM, dtype=np.int64)
    flips = [idx ^ (1 << i) for i in range(N)]

    diag = np.zeros(DIM, dtype=float)
    mvals = np.empty(DIM, dtype=float)
    for s in range(DIM):
        z = [1 - 2 * ((s >> i) & 1) for i in range(N)]
        diag[s] = -J * sum(z[i] * z[j] for i, j in EDGES)
        mvals[s] = sum(z) / N

    rows = []
    for h in h_values:
        def mv(vec):
            out = diag * vec
            for f in flips:
                out += -h * vec[f]
            return out

        H = LinearOperator((DIM, DIM), matvec=mv, dtype=float)
        vals, vecs = eigsh(H, k=3, which="SA", tol=1e-9, maxiter=2000)
        order = np.argsort(vals)
        vals = vals[order]
        vecs = vecs[:, order]
        psi0 = vecs[:, 0]
        sigma2 = float(np.sum(np.abs(psi0) ** 2 * mvals**2))
        abs_sigma = float(np.sum(np.abs(psi0) ** 2 * np.abs(mvals)))
        rows.append({
            "h_over_J": float(h / J),
            "E0_over_J": float(vals[0] / J),
            "E1_over_J": float(vals[1] / J),
            "E2_over_J": float(vals[2] / J),
            "mirror_doublet_splitting_over_J": float((vals[1] - vals[0]) / J),
            "gap_E2_minus_E1_over_J": float((vals[2] - vals[1]) / J),
            "Sigma_squared": sigma2,
            "mean_abs_Sigma": abs_sigma,
        })
    return rows


def run():
    classical = classical_gate()
    rows = quantum_scan()
    low = rows[0]
    high = rows[-1]
    passed = (
        classical["dual_edges"] == 32
        and classical["all_degree_four"]
        and classical["edge_eta_products_all_minus_one"]
        and classical["vacua"]["1"]["Sigma"] == 1.0
        and classical["vacua"]["-1"]["Sigma"] == -1.0
        and abs(classical["single_orientation_flip_cost_over_J"] - 8.0) < 1e-12
        and classical["half_hypercube_domain_wall_frustrated_edges"] == 8
        and abs(classical["half_hypercube_domain_wall_cost_over_J"] - 16.0) < 1e-12
        and low["Sigma_squared"] > 0.99
        and low["mirror_doublet_splitting_over_J"] < 1e-8
        and low["gap_E2_minus_E1_over_J"] > 7.5
        and high["Sigma_squared"] < 0.2
    )
    return {
        "status": "microscopic 16-cell staggered mirror-order gate",
        "passed": bool(passed),
        "classical": classical,
        "quantum_scan": rows,
        "derived_order_parameter": "Sigma=(1/16) sum_v eta_v Y_v, eta_v=(-1)^popcount(v)",
        "microscopic_interpretation": (
            "The required alternating oriented-volume sign across tetrahedral faces becomes a uniform "
            "Z2 mirror order in the staggered variable. The two classical sectors Sigma=+/-1 are exact "
            "mirror partners; finite transverse dynamics produces an ordered low-energy doublet."
        ),
        "continuum_bridge": (
            "A coarse pseudoscalar sigma(x) can be identified with block averages of the staggered "
            "orientation operator. Its soft fluctuations are a candidate mediator/order-parameter mode."
        ),
        "remaining_parameter": (
            "The force strength alpha is not fixed by this gate. It requires the normalization and coupling "
            "of the coarse sigma mode to physical matter/energy and the enlarged quantum HDA."
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
