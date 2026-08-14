#!/usr/bin/env python3
"""Symmetry-resolved mirror sigma gap/range gate on the 16-cell Q4 block.

The microscopic mirror order is Z2. The finite ordered block therefore has a
nearly degenerate even/odd pair whose tiny splitting is global tunnelling, not
a propagating sigma mass.

Moreover, simply using E2-E0 can select a mirror-even state that does not couple
to the mirror-odd order operator Sigma. The physically relevant finite spectral
diagnostic is therefore the first *additional odd-parity state* with nonzero
Sigma spectral weight after excluding the tunnelling partner:

    Delta_sigma,odd = min(E_n-E_0)
      for n outside the mirror doublet and |<0|Sigma|n>|^2 > 0.

This gate block-diagonalizes the 16-qubit Q4 transverse-field Ising Hamiltonian
into exact global-Z2 parity sectors of dimension 32768, computes the sigma
spectral weights, and records a low-frequency Lehmann susceptibility after
excluding the tunnelling state.

The result is a finite microscopic time/range diagnostic, not yet the physical
continuum sigma mass. Continuum identification still requires block/volume
normalization, refined dispersion and physical scale setting.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh


N = 16
FULL_DIM = 1 << N
MASK = FULL_DIM - 1
J = 1.0
EDGES = [(v, v ^ (1 << b)) for v in range(16) for b in range(4) if v < (v ^ (1 << b))]


def build_parity_basis_data():
    reps = np.asarray([s for s in range(FULL_DIM) if s < (s ^ MASK)], dtype=np.int64)
    position = {int(s): i for i, s in enumerate(reps)}
    dim = len(reps)
    diag = np.zeros(dim, dtype=float)
    sigma = np.zeros(dim, dtype=float)
    neighbor = np.zeros((N, dim), dtype=np.int32)
    reversed_rep = np.zeros((N, dim), dtype=bool)

    for j, s0 in enumerate(reps):
        s = int(s0)
        z = [1 - 2 * ((s >> i) & 1) for i in range(N)]
        diag[j] = -J * sum(z[a] * z[b] for a, b in EDGES)
        sigma[j] = sum(z) / N
        for i in range(N):
            t = s ^ (1 << i)
            tc = t ^ MASK
            rep = min(t, tc)
            neighbor[i, j] = position[rep]
            reversed_rep[i, j] = (t != rep)

    return reps, diag, sigma, neighbor, reversed_rep


REPS, DIAG, SIGMA_DIAG, NEIGHBOR, REVERSED_REP = build_parity_basis_data()
PARITY_DIM = len(REPS)


def parity_operator(h, parity):
    signs = np.where(REVERSED_REP, float(parity), 1.0)

    def mv(vec):
        out = DIAG * vec
        for i in range(N):
            out[NEIGHBOR[i]] += -h * signs[i] * vec
        return out

    return LinearOperator((PARITY_DIM, PARITY_DIM), matvec=mv, dtype=float)


def spectral_row(h, odd_levels=16, weight_tol=1e-10):
    # The ground state is even for h>0. The lowest odd state is the finite-size
    # tunnelling partner. Additional odd states are the sector seen by Sigma.
    # k=16 is deliberately used: at the deep ordered control it captures
    # >99.9998% of the non-tunnelling Sigma spectral weight, while k=8 captures
    # only about 99.782% and is insufficient for the preregistered >99.9% gate.
    even_vals, even_vecs = eigsh(
        parity_operator(h, +1), k=1, which="SA", tol=1e-10, maxiter=3500
    )
    odd_vals, odd_vecs = eigsh(
        parity_operator(h, -1), k=odd_levels, which="SA", tol=1e-10, maxiter=3500
    )
    order = np.argsort(odd_vals)
    odd_vals = odd_vals[order]
    odd_vecs = odd_vecs[:, order]

    E0 = float(even_vals[0])
    psi0 = even_vecs[:, 0]
    sigma_psi = SIGMA_DIAG * psi0
    sigma2 = float(np.vdot(sigma_psi, sigma_psi).real)
    weights = np.abs(odd_vecs.T.conj() @ sigma_psi) ** 2

    tunnelling_gap = float(odd_vals[0] - E0)
    tunnelling_weight = float(weights[0])
    candidates = []
    for n in range(1, len(odd_vals)):
        gap = float(odd_vals[n] - E0)
        weight = float(weights[n])
        if weight > weight_tol:
            candidates.append((n, gap, weight))
    if not candidates:
        raise RuntimeError("no non-tunnelling Sigma-coupled odd state found in requested spectrum")

    first = min(candidates, key=lambda x: x[1])

    # Low-frequency odd-sector susceptibility after removing the global
    # tunnelling partner. With chi_*(iw)=A-B w^2+..., inverse susceptibility is
    # chi_*^-1 ~= A^-1 + (B/A^2) w^2. This is a finite-block temporal response,
    # not yet a continuum kinetic coefficient.
    A = 0.0
    B = 0.0
    low_weight = 0.0
    for _, gap, weight in candidates:
        A += 2.0 * weight / gap
        B += 2.0 * weight / (gap**3)
        low_weight += weight
    remaining_weight = max(sigma2 - tunnelling_weight, 0.0)
    captured_fraction = low_weight / remaining_weight if remaining_weight > 0 else 1.0
    Zt = B / (A * A) if A > 0 else float("inf")
    omega_eff = float(np.sqrt(A / B)) if B > 0 else float("inf")

    return {
        "h_over_J": float(h / J),
        "odd_levels_computed": int(odd_levels),
        "E0_even_over_J": E0 / J,
        "tunnelling_gap_over_J": tunnelling_gap / J,
        "tunnelling_Sigma_weight": tunnelling_weight,
        "Sigma_squared": sigma2,
        "first_non_tunnelling_odd_index": int(first[0]),
        "Delta_sigma_odd_over_J": first[1] / J,
        "first_non_tunnelling_Sigma_weight": first[2],
        "low_spectrum_remaining_weight_fraction": float(captured_fraction),
        "susceptibility_A_times_J": float(A * J),
        "susceptibility_B_times_J3": float(B * J**3),
        "finite_block_J_times_Zt": float(J * Zt),
        "finite_block_omega_eff_over_J": float(omega_eff / J),
    }


def run():
    hs = (0.2, 0.5, 1.0, 1.5, 2.0, 2.1, 2.2, 2.25, 2.4, 2.625, 2.75)
    rows = [spectral_row(h) for h in hs]
    low = rows[0]
    soft = min(rows, key=lambda r: r["Delta_sigma_odd_over_J"])

    passed = (
        PARITY_DIM == 32768
        and low["Sigma_squared"] > 0.99
        and abs(low["Delta_sigma_odd_over_J"] - 7.9700878769645) < 2e-7
        and low["low_spectrum_remaining_weight_fraction"] > 0.999
        and 5.0 < soft["Delta_sigma_odd_over_J"] < 6.0
        and abs(soft["h_over_J"] - 2.2) < 1e-12
        and soft["tunnelling_gap_over_J"] < soft["Delta_sigma_odd_over_J"]
    )

    return {
        "status": "symmetry-resolved finite 16-cell mirror sigma range gate",
        "passed": bool(passed),
        "parity_sector_dimension": PARITY_DIM,
        "definition": (
            "Delta_sigma_odd is the first odd-parity excitation with nonzero Sigma spectral weight after "
            "excluding the lowest odd global-tunnelling partner."
        ),
        "scan": rows,
        "deep_order_result": low,
        "softest_checked_sigma_odd_point": soft,
        "range_formula": "lambda_sigma = hbar*c_sigma/Delta_sigma after a continuum mode identification",
        "range_over_ell_formula": (
            "lambda_sigma/ell = 1/(delta_sigma*j_sigma), delta_sigma=Delta_sigma/J, "
            "j_sigma=J*ell/(hbar*c_sigma)"
        ),
        "main_result": (
            "The tiny mirror-doublet splitting is tunnelling, and raw E2-E0 can belong to the wrong Z2 parity. "
            "The Sigma spectral function instead remains gapped at O(J): about 7.97009 J at h/J=0.2 and "
            "no lower than about 5.58411 J in the checked finite-Q4 crossover scan. The seed therefore does "
            "not contain an automatically long-range mirror mediator."
        ),
        "temporal_result": (
            "The low-frequency Lehmann expansion after removing the tunnelling state supplies a finite-block "
            "inverse-susceptibility omega^2 coefficient J*Zt. Converting it to a continuum time-kinetic "
            "normalization still requires block-volume/field normalization and refined dispersion."
        ),
        "critical_requirement": (
            "A macroscopic force still requires m_sigma*r <= O(1). A refined/thermodynamic mode must become "
            "parametrically lighter than the O(J) seed excitation, or a separate light mediator is needed."
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
