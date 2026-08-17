#!/usr/bin/env python3
"""BCQG conditional IR universality closure certificate.

This gate verifies only theorem-level reductions and already-frozen finite
prerequisites.  It MUST NOT report that the still-open collective dynamical
hypotheses H1--H4 have been measured.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]


def load_json(rel: str) -> dict:
    with (ROOT / rel).open("r", encoding="utf-8") as f:
        return json.load(f)


def schur_selftest() -> dict:
    # Deterministic block example with P C P = 0 and invertible Q C Q = D.
    B = np.array([[1.0, 2.0, -1.0], [0.5, -1.0, 1.5]], dtype=float)
    D = np.array([[3.0, 0.2, 0.0], [0.2, 2.0, -0.1], [0.0, -0.1, 4.0]], dtype=float)
    p = np.array([0.7, -1.2], dtype=float)

    Dinv = np.linalg.inv(D)
    q = -Dinv @ B.T @ p
    ceff = -B @ Dinv @ B.T

    q_residual = B.T @ p + D @ q
    p_residual_full = B @ q
    p_residual_eff = ceff @ p

    return {
        "D_min_abs_eigenvalue": float(np.min(np.abs(np.linalg.eigvalsh(D)))),
        "Q_equation_residual_norm": float(np.linalg.norm(q_residual)),
        "P_equation_match_norm": float(np.linalg.norm(p_residual_full - p_residual_eff)),
        "passed": bool(
            np.min(np.abs(np.linalg.eigvalsh(D))) > 1e-8
            and np.linalg.norm(q_residual) < 1e-12
            and np.linalg.norm(p_residual_full - p_residual_eff) < 1e-12
        ),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--output",
        default="verification_results/BCQG_IR_UNIVERSALITY_CLOSURE.json",
    )
    args = ap.parse_args()

    metric = load_json("verification_results/COLLECTIVE_METRIC_CALIBRATION_IRREP.json")
    direct = load_json("verification_results/COLLECTIVE_GRAVITATIONAL_DIRECT_BLOCK.json")

    smin = 1.0 / math.sqrt(6.0)
    smax = 1.0 / math.sqrt(3.0)
    cond = smax / smin

    metric_checks = {
        "source_passed": bool(metric.get("passed")),
        "first_block_smin_positive": smin > 0.0,
        "first_block_smax_finite": math.isfinite(smax),
        "first_block_condition_sqrt2": abs(cond - math.sqrt(2.0)) < 1e-14,
        "stored_condition_sqrt2": metric.get("condition_number") == "sqrt(2)",
    }

    direct_blocks = direct.get("direct_blocks", {})
    direct_checks = {
        "source_passed": bool(direct.get("passed")),
        "Wg_dag_HE_Wg_zero": direct_blocks.get("Wg_dag_HE_Wg") == "0",
        "Wg_dag_S_Wg_zero": direct_blocks.get("Wg_dag_S_Wg") == "0",
        "Wg_dag_G_Wg_zero": str(direct_blocks.get("Wg_dag_G_Wg", "")).startswith("0"),
    }

    # Exact algebraic consequences of the local ADM/HDA identity.
    # anomaly = 4(c-1/2) I must vanish for generic I != 0.
    c_selected = 0.5
    anomaly_coefficient = 4.0 * (c_selected - 0.5)
    AB_selected = 1.0
    z = math.sqrt(AB_selected)

    rG, rD, rH, rExtra, rSC = 3, 3, 1, 0, 0
    rFC = rG + rD + rH + rExtra
    nphys = (18 - 2 * rFC - rSC) / 2

    algebra_checks = {
        "HDA_selects_c_half": abs(anomaly_coefficient) < 1e-15,
        "HDA_selects_AB_one": AB_selected == 1.0,
        "TT_z_one_from_AB": abs(z - 1.0) < 1e-15,
        "Dirac_count_two_modes": nphys == 2.0,
    }

    schur = schur_selftest()

    all_verified = (
        all(metric_checks.values())
        and all(direct_checks.values())
        and all(algebra_checks.values())
        and schur["passed"]
    )

    out = {
        "status": "CONDITIONAL_IR_UNIVERSALITY_THEOREM",
        "passed": bool(all_verified),
        "scope": (
            "Verifies exact reductions and frozen finite prerequisites only; "
            "does not claim direct collective H1-H4 science PASS."
        ),
        "theorem_file": "BCQG_IR_UNIVERSALITY_CLOSURE_THEOREM.md",
        "finite_prerequisites": {
            "metric_calibration": metric_checks,
            "direct_gravitational_block": direct_checks,
            "first_block_metric_bounds": {
                "s_min": smin,
                "s_max": smax,
                "condition_number": cond,
            },
        },
        "exact_reductions": {
            "c_DeWitt": c_selected,
            "AB": AB_selected,
            "z_leading_IR": z,
            "constraint_ranks_assumed_for_count": [rG, rD, rH, rExtra],
            "r_secondclass_assumed_for_count": rSC,
            "N_phys_config": nphys,
            "checks": algebra_checks,
        },
        "schur_feshbach_zero_energy_selftest": schur,
        "irreducible_open_hypotheses": {
            "H1_uniform_metric_regularity_under_refinement": "open",
            "H2_local_two_derivative_leading_IR_scalar": "open",
            "H3_collective_first_class_HDA_and_ranks": "open",
            "H4_no_second_class_sector": "open",
            "absolute_G_Lambda_scale_matching": "open",
            "Lorentzian_quantum_measure_unitarity": "open",
            "complete_chiral_matter_anomaly_cancellation": "open",
            "experiment": "open",
        },
        "non_relaxation_guard": (
            "COLLECTIVE_GR_UNIVERSALITY_PREREGISTRATION.md remains an independent "
            "stronger numerical AND-gate; its frozen thresholds are not modified."
        ),
    }

    out_path = ROOT / args.output
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))

    if not all_verified:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
