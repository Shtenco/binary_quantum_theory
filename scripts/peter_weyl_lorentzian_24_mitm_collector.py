#!/usr/bin/env python3
"""Collect the 24 safe-cutoff Lorentzian MITM triple artifacts.

This is a pure evidence collector.  It does not recompute Peter-Weyl amplitudes.
It reads the 24 independently produced T_abc.json files from workflow run
31832450485, applies each artifact's preregistered epsilon_coefficient, and
builds the complete raw one-node logical epsilon sum

    L_eps^log = sum_(a,b,c) eps_(abc) P Tr_aux[C_a(K) C_b(K) C_c(V)] P.

The collector verifies the observed support split rather than inferring it from
artifact sizes: the six permutations of (1,2,3) are nonzero while all eighteen
triples containing edge 4 vanish in the frozen source-node-0 volume ordering.

This is still a raw structural Lorentzian amplitude.  It does NOT insert the
final canonical kappa/beta/hbar/i prefactor, does NOT claim a Hermitian H_L,
and does NOT claim a physical mirror mass or force.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np

PAULI = {
    "I": np.eye(2, dtype=complex),
    "X": np.array([[0, 1], [1, 0]], dtype=complex),
    "Y": np.array([[0, -1j], [1j, 0]], dtype=complex),
    "Z": np.array([[1, 0], [0, -1]], dtype=complex),
}


def cpair(z: complex):
    z = complex(z)
    return [float(z.real), float(z.imag)]


def matrix_from_json(d):
    return np.array(
        [[complex(*d["logical_2x2_matrix"][i][j]) for j in range(2)] for i in range(2)],
        dtype=complex,
    )


def pauli_coeffs(M):
    return {name: np.trace(P @ M) / 2.0 for name, P in PAULI.items()}


def run(root: Path):
    files = sorted(root.rglob("T_*.json"))
    rows = []
    total = np.zeros((2, 2), dtype=complex)
    max_leak = 0.0

    for f in files:
        d = json.loads(f.read_text(encoding="utf-8"))
        edges = tuple(int(x) for x in d["ordered_edges"])
        M = matrix_from_json(d)
        sign = int(d["epsilon_coefficient"])
        norm = float(np.linalg.norm(M))
        max_leak = max(max_leak, float(d["physical_acceptance_max_leakage"]))
        total += sign * M
        rows.append({
            "edges": list(edges),
            "epsilon_coefficient": sign,
            "frobenius_norm": norm,
            "any_logical_return": bool(d["any_logical_return"]),
            "matrix": [[cpair(M[i, j]) for j in range(2)] for i in range(2)],
            "physical_acceptance_max_leakage": float(d["physical_acceptance_max_leakage"]),
        })

    expected = set(itertools.permutations((1, 2, 3, 4), 3))
    seen = {tuple(r["edges"]) for r in rows}
    nonzero = {tuple(r["edges"]) for r in rows if r["frobenius_norm"] > 1e-12}
    zero = seen - nonzero
    expected_nonzero = set(itertools.permutations((1, 2, 3), 3))
    expected_zero = expected - expected_nonzero

    c = pauli_coeffs(total)
    total_norm = float(np.linalg.norm(total))
    sign_sector = c["Y"] * PAULI["Y"]
    sign_sector_norm = float(np.linalg.norm(sign_sector))

    passed = (
        len(files) == 24
        and seen == expected
        and nonzero == expected_nonzero
        and zero == expected_zero
        and max_leak < 1e-12
        and total_norm > 1e-6
        and abs(c["Y"]) > 1e-6
        and abs(c["I"]) < 1e-12
        and abs(c["Z"]) < 1e-12
    )

    return {
        "status": "complete safe-cutoff 24-triple Lorentzian MITM collector",
        "passed": bool(passed),
        "source_workflow_run": 31832450485,
        "Jmax": 3.5,
        "artifact_count": len(files),
        "nonzero_triple_count": len(nonzero),
        "zero_triple_count": len(zero),
        "nonzero_triples": [list(x) for x in sorted(nonzero)],
        "zero_triples": [list(x) for x in sorted(zero)],
        "all_18_edge4_triples_exactly_zero_at_artifact_precision": zero == expected_zero,
        "max_physical_basis_volume_leakage": max_leak,
        "raw_epsilon_logical_matrix": [[cpair(total[i, j]) for j in range(2)] for i in range(2)],
        "raw_epsilon_frobenius_norm": total_norm,
        "raw_pauli_coefficients": {k: cpair(v) for k, v in c.items()},
        "orientation_sign_sector_coefficient_Y": cpair(c["Y"]),
        "orientation_sign_sector_matrix": [[cpair(sign_sector[i, j]) for j in range(2)] for i in range(2)],
        "orientation_sign_sector_norm": sign_sector_norm,
        "interpretation": (
            "The complete raw epsilon-oriented one-node logical return is nonzero at the safe single-H_L cutoff. "
            "The exact S4 sign projector proved elsewhere removes frozen-frame I/X/Z contamination and retains only "
            "the Y pseudoscalar component.  Final physical H_L still requires the canonical prefactor/ordering convention."
        ),
        "mirror_warning": (
            "On the minimal oriented 16-cell, the independently proved facet orientation sign equals eta_v. "
            "Therefore a nonzero physical one-cell Y coefficient would assemble as ell_L sum_v eta_v Y_v = N ell_L Sigma, "
            "a longitudinal staggered field that explicitly lifts the mirror pair for fixed global orientation; it is not a mediator mass."
        ),
        "scope": (
            "Finite safe-cutoff structural amplitude certificate only; no continuum limit, no final Hermitian Lorentzian coefficient, "
            "no physical mirror-force claim."
        ),
        "triples": rows,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    out = run(args.root)
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    raise SystemExit(0 if out["passed"] else 1)


if __name__ == "__main__":
    main()
