#!/usr/bin/env python3
"""Exact Bell-gluing -> bipartite Heisenberg parent gate.

The already frozen two-cell gluing Hamiltonian is

  H_glue = -J sum_<vw> (X_v X_w - Y_v Y_w + Z_v Z_w).

On a bipartite dual graph, rotate every B-sublattice logical qubit by pi around
Y. Then X_B->-X_B, Y_B->Y_B, Z_B->-Z_B and exactly

  U H_glue U^dagger = J sum_<vw> (X_v X_w + Y_v Y_w + Z_v Z_w),

an antiferromagnetic Heisenberg Hamiltonian in Pauli normalization.

The staggered mirror order Sigma_Y=(1/N)sum eta_v Y_v is the Y component of
the Heisenberg Neel vector. This supplies a continuous-symmetry parent for the
mirror order, distinct from the conservative Ising truncation.

The gate verifies the exact two-qubit unitary identity, diagonalizes the full
16-qubit Q4 parent, and records a graph linear-spin-wave diagnostic on the same
recursive PL dual graphs. The finite and spin-wave results do NOT by themselves
prove spontaneous symmetry breaking or a physical massless sigma mode in the
full gravity theory; additional geometry dynamics can generate anisotropy.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh

import sys
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from bcqg_global_manifold_gate import cross_polytope_boundary_4, barycentric_subdivision
from scripts.mirror_order_recursive_pl_gate import dual_edges, bipartite_coloring, low_laplacian


X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)

N = 16
DIM = 1 << N
J = 1.0
Q4_EDGES = [(v, v ^ (1 << b)) for v in range(16) for b in range(4) if v < (v ^ (1 << b))]
ETA_Q4 = np.array([1 if int(v).bit_count() % 2 == 0 else -1 for v in range(N)], dtype=float)


def two_qubit_unitary_identity():
    # A pi rotation around Y is U_B=-iY up to a physically irrelevant global phase.
    UB = -1j * Y
    U = np.kron(I2, UB)
    Hglue = -(np.kron(X, X) - np.kron(Y, Y) + np.kron(Z, Z))
    Haf = np.kron(X, X) + np.kron(Y, Y) + np.kron(Z, Z)
    transformed = U @ Hglue @ U.conj().T
    return {
        "frobenius_error": float(np.linalg.norm(transformed - Haf)),
        "H_glue_eigenvalues": np.linalg.eigvalsh(Hglue).real.tolist(),
        "H_AF_eigenvalues": np.linalg.eigvalsh(Haf).real.tolist(),
    }


def q4_heisenberg_low_spectrum():
    idx = np.arange(DIM, dtype=np.int64)
    diag = np.zeros(DIM, dtype=float)
    exchange = []

    # H=J sum sigma_i.sigma_j. ZZ is diagonal. XX+YY flips an opposite-spin
    # pair with amplitude 2 and annihilates a same-spin pair.
    for s in range(DIM):
        z = [1 - 2 * ((s >> i) & 1) for i in range(N)]
        diag[s] = J * sum(z[a] * z[b] for a, b in Q4_EDGES)
    for a, b in Q4_EDGES:
        opposite = (((idx >> a) & 1) != ((idx >> b) & 1))
        exchange.append(((1 << a) | (1 << b), opposite))

    def mv(vec):
        out = diag * vec
        for mask, opposite in exchange:
            out[opposite] += 2.0 * J * vec[(idx ^ mask)[opposite]]
        return out

    H = LinearOperator((DIM, DIM), matvec=mv, dtype=float)
    vals, vecs = eigsh(H, k=4, which="SA", tol=1e-11, maxiter=4000)
    order = np.argsort(vals)
    vals = vals[order]
    psi0 = vecs[:, order[0]]

    # By exact SU(2) symmetry of the Heisenberg parent, <N_x^2>=<N_y^2>=<N_z^2>
    # in the nondegenerate singlet ground state. N_z is diagonal in this basis.
    nz = np.zeros(DIM, dtype=float)
    mtot = np.zeros(DIM, dtype=float)
    for s in range(DIM):
        z = np.array([1 - 2 * ((s >> i) & 1) for i in range(N)], dtype=float)
        nz[s] = float(np.dot(ETA_Q4, z) / N)
        mtot[s] = float(np.sum(z))

    nz2 = float(np.sum(np.abs(psi0) ** 2 * nz**2))
    mtot2 = float(np.sum(np.abs(psi0) ** 2 * mtot**2))
    gaps = vals - vals[0]

    return {
        "hilbert_dimension": DIM,
        "lowest_energies_over_J": [float(x / J) for x in vals],
        "lowest_gaps_over_J": [float(x / J) for x in gaps],
        "first_triplet_gap_over_J": float(gaps[1] / J),
        "triplet_internal_spread_over_J": float((max(vals[1:4]) - min(vals[1:4])) / J),
        "Neel_y_squared_by_SU2": nz2,
        "Neel_vector_squared_by_SU2": 3.0 * nz2,
        "total_sigma_z_squared": mtot2,
    }


def spinwave_from_laplacian(mu, degree=4):
    # Standard linear spin-wave dispersion for H_Pauli=J sum sigma.sigma
    # = 4J sum S.S, S=1/2:
    # omega/J = 2*z*sqrt(1-(lambda_adj/z)^2), lambda_adj=z-mu.
    z = float(degree)
    lam = z - float(mu)
    inside = max(0.0, 1.0 - (lam / z) ** 2)
    return 2.0 * z * math.sqrt(inside)


def recursive_spinwave(refinements=2):
    tets = cross_polytope_boundary_4()
    rows = []
    for g in range(refinements + 1):
        edges = dual_edges(tets)
        ok, eta, adj, comps = bipartite_coloring(len(tets), edges)
        vals = low_laplacian(len(tets), edges, k=6)
        mu2 = vals[1]
        rows.append({
            "generation": g,
            "tetrahedra": len(tets),
            "dual_edges": len(edges),
            "degree": min(len(x) for x in adj),
            "bipartite": bool(ok),
            "lambda2_combinatorial": float(mu2),
            "linear_spinwave_omega2_over_J": float(spinwave_from_laplacian(mu2, 4)),
        })
        if g < refinements:
            tets = barycentric_subdivision(tets)
    return rows


def run():
    unitary = two_qubit_unitary_identity()
    exact = q4_heisenberg_low_spectrum()
    recursive = recursive_spinwave(2)

    passed = (
        unitary["frobenius_error"] < 1e-12
        and exact["hilbert_dimension"] == 65536
        and abs(exact["first_triplet_gap_over_J"] - 2.31439334306155) < 5e-8
        and exact["triplet_internal_spread_over_J"] < 1e-9
        and exact["Neel_y_squared_by_SU2"] > 0.3
        and exact["total_sigma_z_squared"] < 1e-18
        and all(r["bipartite"] and r["degree"] == 4 for r in recursive)
        and all(
            recursive[i + 1]["lambda2_combinatorial"] < recursive[i]["lambda2_combinatorial"]
            for i in range(len(recursive) - 1)
        )
        and all(
            recursive[i + 1]["linear_spinwave_omega2_over_J"] < recursive[i]["linear_spinwave_omega2_over_J"]
            for i in range(len(recursive) - 1)
        )
    )

    return {
        "status": "Bell-gluing Heisenberg parent gate",
        "passed": bool(passed),
        "exact_bipartite_identity": (
            "pi rotation about logical Y on one sublattice maps -J(XX-YY+ZZ) to +J(XX+YY+ZZ) edge by edge"
        ),
        "unitary_two_qubit_control": unitary,
        "exact_Q4_parent": exact,
        "recursive_graph_spinwave_diagnostic": recursive,
        "mirror_order_embedding": (
            "Sigma_Y=(1/N)sum eta_v Y_v is the Y component of the Neel vector of the transformed AF Heisenberg parent"
        ),
        "continuum_implication": (
            "If the full low-energy projected gluing dynamics retains this continuous pseudospin symmetry and the "
            "refined/infinite-volume phase develops Neel order, mirror-orientation fluctuations belong to a "
            "Goldstone/spin-wave sector rather than the massive Z2 Ising sector. This implication is conditional."
        ),
        "anisotropy_falsifier": (
            "Any surviving X/Y/Z anisotropy induced by the full Peter-Weyl geometry Hamiltonian can gap or mix the "
            "mirror component. The next decisive gate is therefore the projected anisotropy of the actual geometry dynamics."
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
