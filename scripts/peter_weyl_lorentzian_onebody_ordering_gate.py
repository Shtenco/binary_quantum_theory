#!/usr/bin/env python3
"""Ordering audit for the exact Lorentzian one-body environment trace.

The heavy Peter-Weyl calculation is stored in
verification_results/PETER_WEYL_LORENTZIAN_ENVTRACE_ORBIT.json.  It yields the
raw structural 24-term operator L_raw before the final physical overall
prefactor / Hermitian convention is fixed.

This cheap audit tests the algebraic fact that the stored raw operator is
anti-Hermitian and almost purely i*Y.  It then displays, without selecting one
post hoc, the two standard Hermitian completions

    H_even = (L_raw + L_raw^dagger)/2
    H_odd  = (L_raw - L_raw^dagger)/(2 i).

For the frozen evidence H_even is zero to numerical precision, while H_odd is a
nonzero Hermitian Y operator.  The gate deliberately does NOT declare which
completion is the physical Lorentzian constraint.  That convention must be
fixed independently from the canonical quantization/classical-limit
prescription and only then used in HDA tests.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

DEFAULT_EVIDENCE = Path("verification_results/PETER_WEYL_LORENTZIAN_ENVTRACE_ORBIT.json")
EXPECTED_Y = 1.3389293521464034

PAULI = {
    "I": np.eye(2, dtype=complex),
    "X": np.array([[0, 1], [1, 0]], dtype=complex),
    "Y": np.array([[0, -1j], [1j, 0]], dtype=complex),
    "Z": np.array([[1, 0], [0, -1]], dtype=complex),
}


def zpair(z: complex):
    z = complex(z)
    return [float(z.real), float(z.imag)]


def matrix_from_pairs(rows):
    return np.array([[complex(*z) for z in row] for row in rows], dtype=complex)


def pauli_coefficients(M):
    return {name: zpair(np.trace(P @ M) / 2.0) for name, P in PAULI.items()}


def relative_norm(A, reference):
    return float(np.linalg.norm(A) / max(np.linalg.norm(reference), 1e-30))


def run(evidence_path: Path):
    data = json.loads(evidence_path.read_text(encoding="utf-8"))
    L = matrix_from_pairs(data["full_24term_onebody_from_orbit"])

    Ldag = L.conj().T
    H_even = (L + Ldag) / 2.0
    H_odd = (L - Ldag) / (2.0j)

    raw_norm = float(np.linalg.norm(L))
    antihermiticity_defect = relative_norm(L + Ldag, L)
    even_fraction = relative_norm(H_even, L)
    odd_hermiticity_defect = relative_norm(H_odd - H_odd.conj().T, H_odd)

    c_raw = pauli_coefficients(L)
    c_even = pauli_coefficients(H_even)
    c_odd_complex = {name: np.trace(P @ H_odd) / 2.0 for name, P in PAULI.items()}
    c_odd = {name: zpair(v) for name, v in c_odd_complex.items()}

    non_y = float(np.sqrt(sum(abs(c_odd_complex[k]) ** 2 for k in ("I", "X", "Z"))))
    y = complex(c_odd_complex["Y"])
    odd_norm = float(np.linalg.norm(H_odd))
    eigenvalues = [float(x) for x in np.linalg.eigvalsh(H_odd)]

    checks = {
        "source_heavy_gate_passed": bool(data.get("passed", False)),
        "source_decision_nonzero": data.get("decision") == "NONZERO_TRUE_ONE_BODY_RAW_Y",
        "raw_nonzero": raw_norm > 1e-10,
        "raw_antihermitian": antihermiticity_defect < 1e-12,
        "hermitian_even_projection_zero": even_fraction < 1e-12,
        "odd_completion_hermitian": odd_hermiticity_defect < 1e-12,
        "odd_completion_nonzero": odd_norm > 1e-10,
        "odd_completion_pure_Y": non_y / max(abs(y), 1e-30) < 1e-12,
        "odd_Y_real": abs(y.imag) < 1e-12,
        "odd_Y_matches_frozen_evidence": abs(y.real - EXPECTED_Y) < 1e-12,
        "opposite_eigenvalues": abs(eigenvalues[0] + eigenvalues[1]) < 1e-12,
    }

    return {
        "status": "Lorentzian one-body Hermitian-ordering fork audit",
        "passed": all(checks.values()),
        "source_evidence": str(evidence_path),
        "raw_frobenius_norm": raw_norm,
        "raw_pauli": c_raw,
        "raw_antihermiticity_relative_defect": antihermiticity_defect,
        "H_even_definition": "(L_raw + L_raw^dagger)/2",
        "H_even_relative_norm": even_fraction,
        "H_even_pauli": c_even,
        "H_odd_definition": "(L_raw - L_raw^dagger)/(2i)",
        "H_odd_hermiticity_relative_defect": odd_hermiticity_defect,
        "H_odd_frobenius_norm": odd_norm,
        "H_odd_pauli": c_odd,
        "H_odd_eigenvalues": eigenvalues,
        "checks": checks,
        "decision": "ORDERING_FORK_CONFIRMED",
        "scientific_scope": (
            "The raw finite Peter-Weyl Lorentzian one-body amplitude is nonzero "
            "and anti-Hermitian. The even Hermitian projection kills it, while "
            "the anti-Hermitian-to-Hermitian completion yields a nonzero Y term. "
            "This gate does not choose the physical completion; the choice must "
            "be fixed independently before interpreting a mirror splitting or "
            "using the completed H_L in the final HDA calculation."
        ),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    out = run(args.evidence)
    text = json.dumps(out, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
