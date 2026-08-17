#!/usr/bin/env python3
"""Exact representation-growth bridge from q=2 graph links to Peter-Weyl j.

Assume a coarse link contains n indistinguishable active q=2 graph-link strands.
Each active strand carries the exact endpoint representation (1/2,1/2) from
q2_graphlink_peter_weyl_gate.py.  On each endpoint, the fully symmetric n-fold
spin-1/2 subspace is Sym^n(C^2), the unique spin j=n/2 irrep of dimension n+1.
Hence a symmetrically blocked coarse link carries

    (j_L,j_R) = (n/2,n/2),   dim=(n+1)^2.

Allowing graph occupancy n=0..N therefore gives exactly one diagonal
Peter-Weyl sector for every j=0,1/2,...,N/2, with total dimension

    sum_{n=0}^N (n+1)^2 = sum_{j<=N/2} (2j+1)^2.

This gate explicitly constructs the symmetric SU(2) matrices and verifies the
algebra/Casimir/counting identities.  The representation theorem is exact; the
physical assumption that coarse graining dynamically selects the symmetric
strand sector remains a separate open problem.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def spin_matrices_from_symmetric_n(n: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Spin j=n/2 on occupation basis k=0..n, where m=k-n/2."""
    d = n + 1
    j = n / 2.0
    Jz = np.diag([k - j for k in range(d)]).astype(complex)
    Jp = np.zeros((d, d), complex)
    for k in range(d - 1):
        m = k - j
        Jp[k + 1, k] = math.sqrt((j - m) * (j + m + 1.0))
    Jm = Jp.conj().T
    Jx = 0.5 * (Jp + Jm)
    Jy = (Jp - Jm) / (2.0j)
    return Jx, Jy, Jz


def one_n(n: int) -> dict[str, object]:
    J = spin_matrices_from_symmetric_n(n)
    d = n + 1
    j = n / 2.0
    eps = np.zeros((3, 3, 3), int)
    eps[0, 1, 2] = eps[1, 2, 0] = eps[2, 0, 1] = 1
    eps[1, 0, 2] = eps[2, 1, 0] = eps[0, 2, 1] = -1
    su2_error = 0.0
    for a in range(3):
        for b in range(3):
            comm = J[a] @ J[b] - J[b] @ J[a]
            target = 1j * sum(eps[a, b, c] * J[c] for c in range(3))
            su2_error = max(su2_error, float(np.linalg.norm(comm - target)))
    C = sum(x @ x for x in J)
    casimir_error = float(np.linalg.norm(C - j * (j + 1.0) * np.eye(d)))

    # Left/right endpoint spaces are independent copies of the same symmetric irrep.
    sector_dimension = d * d
    return {
        "n_active_strands": n,
        "j": j,
        "endpoint_dimension": d,
        "coarse_link_sector_dimension": sector_dimension,
        "su2_error": su2_error,
        "casimir_error": casimir_error,
        "expected_casimir": j * (j + 1.0),
    }


def sum_squares(N: int) -> int:
    return (N + 1) * (N + 2) * (2 * N + 3) // 6


def run(N: int = 8) -> dict[str, object]:
    if N < 1:
        raise ValueError("N must be >= 1")
    rows = [one_n(n) for n in range(N + 1)]
    blocked_dimension = sum(r["coarse_link_sector_dimension"] for r in rows)
    peter_weyl_dimension = sum((n + 1) ** 2 for n in range(N + 1))
    closed_form_dimension = sum_squares(N)
    represented_j = [r["j"] for r in rows]
    target_j = [n / 2.0 for n in range(N + 1)]

    checks = {
        "all_symmetric_endpoint_irreps_are_exact_su2": max(r["su2_error"] for r in rows) < 1e-12,
        "all_casimirs_are_j_jplus1": max(r["casimir_error"] for r in rows) < 1e-12,
        "one_sector_for_every_half_integer_j_to_Jmax": represented_j == target_j,
        "sector_dimension_is_2jplus1_squared": all(r["coarse_link_sector_dimension"] == int((2 * r["j"] + 1) ** 2) for r in rows),
        "blocked_occupancy_dimension_equals_Peter_Weyl_truncation": blocked_dimension == peter_weyl_dimension,
        "dimension_matches_sum_of_squares_closed_form": blocked_dimension == closed_form_dimension,
    }

    return {
        "status": "exact conditional representation-growth bridge under symmetric active-strand blocking",
        "passed": bool(all(checks.values())),
        "maximum_active_strands": N,
        "Jmax": N / 2.0,
        "rows": rows,
        "blocked_total_dimension": blocked_dimension,
        "Peter_Weyl_truncated_dimension": peter_weyl_dimension,
        "closed_form_dimension": closed_form_dimension,
        "checks": checks,
        "theorem": (
            "If n indistinguishable active q=2 graph-link strands are symmetrically blocked at both endpoints, the coarse link is the unique (j,j)=(n/2,n/2) sector of dimension (n+1)^2. "
            "The occupancy union n=0..N is dimension-identical to the Peter-Weyl tower j=0,1/2,...,N/2."
        ),
        "claim_boundary": (
            "Exact representation/counting theorem conditional on symmetric endpoint blocking. "
            "The microscopic graph-changing Hamiltonian has not yet been proved to select this symmetric block or the physical weights of different occupancies n."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--N", type=int, default=8)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    out = run(args.N)
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
