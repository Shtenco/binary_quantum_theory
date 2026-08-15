#!/usr/bin/env python3
"""Derive the missing Lorentzian phase from the declared Thiemann bracket stack.

Repository raw operators omit the universal Poisson-to-commutator prefactors:

    K_raw = [V, H_E]
    C_raw(O) = h [h^-1, O]
    L_raw ~ Tr[C_raw(K_raw) C_raw(K_raw) C_raw(V)].

The corresponding classical Lorentzian structure contains

    {A,K} {A,K} {A,V},   with K ~ {V,H_E}.

Thus, after substituting K, there are five Poisson brackets. Under the standard
canonical correspondence

    { , } -> [ , ] / (i hbar)

the raw structural triple acquires the universal phase

    (1/i)^5 = -i

(up to real powers of hbar and real convention-dependent constants).

This gate applies only that phase to the frozen exact environment-trace matrix.
It tests that -i L_raw is Hermitian and equals the previously displayed
anti-Hermitian-to-Hermitian completion. It does not determine the remaining
real kappa/beta/hbar normalization, nor prove uniqueness against every other
factor ordering.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

DEFAULT_EVIDENCE = Path("verification_results/PETER_WEYL_LORENTZIAN_ENVTRACE_ORBIT.json")

INNER_K_BRACKETS = 2       # one {V,H_E} inside each of the two K legs
OUTER_K_BRACKETS = 2       # two {A,K} legs
VOLUME_LEG_BRACKETS = 1    # one {A,V} leg
TOTAL_BRACKETS = INNER_K_BRACKETS + OUTER_K_BRACKETS + VOLUME_LEG_BRACKETS
EXPECTED_Y = 1.3389293521464034

PAULI = {
    "I": np.eye(2, dtype=complex),
    "X": np.array([[0, 1], [1, 0]], dtype=complex),
    "Y": np.array([[0, -1j], [1j, 0]], dtype=complex),
    "Z": np.array([[1, 0], [0, -1]], dtype=complex),
}


def matrix_from_pairs(rows):
    return np.array([[complex(*z) for z in row] for row in rows], dtype=complex)


def zpair(z):
    z = complex(z)
    return [float(z.real), float(z.imag)]


def pauli(M):
    return {name: zpair(np.trace(P @ M) / 2.0) for name, P in PAULI.items()}


def relnorm(A, B):
    return float(np.linalg.norm(A) / max(np.linalg.norm(B), 1e-30))


def run(evidence_path: Path):
    data = json.loads(evidence_path.read_text(encoding="utf-8"))
    L = matrix_from_pairs(data["full_24term_onebody_from_orbit"])

    phase = (1.0 / 1j) ** TOTAL_BRACKETS
    H_phase = phase * L
    H_odd = (L - L.conj().T) / (2.0j)

    p = {name: np.trace(P @ H_phase) / 2.0 for name, P in PAULI.items()}
    y = complex(p["Y"])
    non_y = float(np.sqrt(sum(abs(p[k]) ** 2 for k in ("I", "X", "Z"))))

    checks = {
        "source_evidence_passed": bool(data.get("passed", False)),
        "nested_bracket_count_is_five": TOTAL_BRACKETS == 5,
        "phase_is_minus_i": abs(phase + 1j) < 1e-15,
        "phase_completed_operator_hermitian": relnorm(H_phase - H_phase.conj().T, H_phase) < 1e-12,
        "phase_matches_odd_completion": relnorm(H_phase - H_odd, H_odd) < 1e-12,
        "phase_completed_operator_pure_Y": non_y / max(abs(y), 1e-30) < 1e-12,
        "phase_completed_Y_is_real": abs(y.imag) < 1e-12,
        "phase_completed_Y_matches_frozen_value": abs(y.real - EXPECTED_Y) < 1e-12,
    }

    return {
        "status": "conditional canonical Lorentzian commutator-phase certificate",
        "passed": all(checks.values()),
        "raw_operator_definition": "Tr[C_raw(K_raw) C_raw(K_raw) C_raw(V)]",
        "K_raw_definition": "[V,H_E]",
        "classical_nested_structure": "{A,{V,H_E}} {A,{V,H_E}} {A,V}",
        "poisson_bracket_count": TOTAL_BRACKETS,
        "quantization_correspondence": "{,} -> [,]/(i hbar)",
        "dimensionless_phase": zpair(phase),
        "omitted_real_scale": "real powers/constants in hbar, kappa, beta and regulator normalization",
        "phase_completed_pauli": {name: zpair(value) for name, value in p.items()},
        "phase_completed_eigenvalues": [float(x) for x in np.linalg.eigvalsh(H_phase)],
        "phase_vs_odd_completion_relative_error": relnorm(H_phase - H_odd, H_odd),
        "checks": checks,
        "decision": "CANONICAL_BRACKET_PHASE_SELECTS_MINUS_I_TIMES_RAW",
        "scope": (
            "Within the declared Thiemann nested-bracket architecture and the "
            "standard Poisson-to-commutator correspondence, the missing universal "
            "complex phase is -i. This selects the nonzero Hermitian Y completion "
            "of the frozen raw one-body block. The remaining real normalization, "
            "full symmetric factor-ordering choice and complete two-node HDA are "
            "separate obligations."
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
