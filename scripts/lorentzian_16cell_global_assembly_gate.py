#!/usr/bin/env python3
"""Assemble the phase-completed local Lorentzian Y block on the oriented 16-cell.

This gate composes three already independent results:

1. the exact finite Peter-Weyl environment trace gives
       L_raw = i c_L Y,  c_L=1.3389293521464034;
2. the five-bracket canonical phase gives -i L_raw = c_L Y up to a real
   overall normalization/sign;
3. the exact 16-cell orientation gate gives local facet sign
       eta_v=(-1)^popcount(v),
   and the Lorentzian epsilon assembler transforms in the S4 sign character.

Therefore the globally oriented one-body structural operator is

    H_L,1body = g_R c_L sum_v eta_v Y_v
              = 16 g_R c_L Sigma,

where g_R is the still-open real normalization/sign and
Sigma=(1/16)sum eta_v Y_v.

On ideal mirror-order vacua Y_v=chi eta_v, chi=+/-1, the structural energy
splitting is

    |Delta E| = 32 c_L |g_R|.

This is a longitudinal staggered field, not a mediator mass. At fixed global
orientation it explicitly lifts the internal Y->-Y degeneracy unless its
renormalized coefficient vanishes. Under simultaneous global-orientation and
Y reversal, eta_v Y_v is invariant.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

DEFAULT_EVIDENCE = Path("verification_results/PETER_WEYL_LORENTZIAN_ENVTRACE_ORBIT.json")
C_FROZEN = 1.3389293521464034
N = 16


def eta(label: int) -> int:
    return -1 if label.bit_count() % 2 else +1


def run(evidence_path: Path):
    data = json.loads(evidence_path.read_text(encoding="utf-8"))
    ypair = data["onebody_Y_coefficient_raw"]
    c = float(abs(complex(*ypair)))

    eta_vec = np.array([eta(v) for v in range(N)], dtype=int)
    sum_eta = int(np.sum(eta_vec))

    rows = {}
    for chi in (+1, -1):
        Y = chi * eta_vec
        sigma = float(np.mean(eta_vec * Y))
        signed_sum = float(np.sum(eta_vec * Y))
        unsigned_sum = float(np.sum(Y))
        rows[str(chi)] = {
            "Sigma": sigma,
            "sum_eta_Y": signed_sum,
            "sum_Y_negative_control": unsigned_sum,
            "structural_energy_coefficient_per_gR": c * signed_sum,
        }

    split = abs(
        rows["1"]["structural_energy_coefficient_per_gR"]
        - rows["-1"]["structural_energy_coefficient_per_gR"]
    )
    per_cell_split = split / N

    # Fixed-orientation internal mirror: Y -> -Y, eta fixed.
    # Combined orientation+mirror: eta -> -eta and Y -> -Y.
    rng = np.random.default_rng(20260815)
    Ytest = rng.normal(size=N)
    fixed_before = float(np.dot(eta_vec, Ytest))
    fixed_after = float(np.dot(eta_vec, -Ytest))
    combined_after = float(np.dot(-eta_vec, -Ytest))

    checks = {
        "source_raw_gate_passed": bool(data.get("passed", False)),
        "source_nonzero_raw_Y": data.get("decision") == "NONZERO_TRUE_ONE_BODY_RAW_Y",
        "frozen_coefficient_match": abs(c - C_FROZEN) < 1e-12,
        "sixteen_facets": len(eta_vec) == 16,
        "balanced_eta": sum_eta == 0,
        "plus_vacuum_sigma": rows["1"]["Sigma"] == 1.0,
        "minus_vacuum_sigma": rows["-1"]["Sigma"] == -1.0,
        "orientation_signed_sum_plus": rows["1"]["sum_eta_Y"] == 16.0,
        "orientation_signed_sum_minus": rows["-1"]["sum_eta_Y"] == -16.0,
        "unsigned_staggered_sum_cancels_plus": rows["1"]["sum_Y_negative_control"] == 0.0,
        "unsigned_staggered_sum_cancels_minus": rows["-1"]["sum_Y_negative_control"] == 0.0,
        "splitting_matches_32c": abs(split - 32.0 * c) < 1e-12,
        "fixed_orientation_mirror_flips_term": abs(fixed_after + fixed_before) < 1e-12,
        "combined_orientation_mirror_preserves_term": abs(combined_after - fixed_before) < 1e-12,
    }

    return {
        "status": "conditional global 16-cell Lorentzian orientation-field assembly",
        "passed": all(checks.values()),
        "local_phase_completed_Y_coefficient_per_real_normalization": c,
        "eta_vector": eta_vec.tolist(),
        "facet_count": N,
        "global_operator_identity": "H_L,1body = g_R c_L sum_v eta_v Y_v = 16 g_R c_L Sigma",
        "ideal_vacua": rows,
        "mirror_pair_splitting_coefficient_per_abs_gR": split,
        "mirror_pair_splitting_per_cell_per_abs_gR": per_cell_split,
        "fixed_orientation_internal_mirror": "eta fixed, Y->-Y: one-body term changes sign",
        "combined_global_orientation_and_mirror": "eta->-eta, Y->-Y: eta*Y is invariant",
        "negative_control": "If the required orientation eta factor is omitted, sum_v Y_v vanishes on both ideal staggered vacua.",
        "renormalization_condition": (
            "A degenerate spontaneous internal mirror pair at fixed global orientation "
            "requires the renormalized one-body coefficient g_R c_L to vanish in the "
            "full/refined operator limit, or else a physical symmetry must identify "
            "the simultaneous global-orientation reversal sector."
        ),
        "interpretation": (
            "The nonzero Lorentzian logical one-body term is a longitudinal field "
            "conjugate to the staggered orientation order Sigma, not a mediator mass "
            "and not by itself a force between separated bodies."
        ),
        "checks": checks,
        "scope": (
            "Exact finite algebra once the frozen local coefficient and orientation-sign "
            "covariance are accepted. The unknown real normalization/sign g_R remains; "
            "no physical energy scale or mirror force is claimed."
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
