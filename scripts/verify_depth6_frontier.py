#!/usr/bin/env python3
"""Fail-closed verifier for the current finite depth-6 BQG frontier.

This validator deliberately distinguishes:
- closed irreps,
- structural support closure,
- active master-kernel work,
- full finite depth-6 theorem,
- continuum/physical completion.

It MUST fail if documentation or automation tries to promote the current
frontier beyond the evidence recorded in depth6_frontier.json.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "depth6_frontier.json"

EXPECTED_MULT = {
    "[5]": 27227,
    "[4,1]": 104146,
    "[3,2]": 130903,
    "[3,1,1]": 153455,
    "[2,2,1]": 130503,
    "[2,1,1,1]": 103318,
    "[1^5]": 26794,
}
S5_DIMS = {
    "[5]": 1,
    "[4,1]": 4,
    "[3,2]": 5,
    "[3,1,1]": 6,
    "[2,2,1]": 5,
    "[2,1,1,1]": 4,
    "[1^5]": 1,
}

def main() -> int:
    errors: list[str] = []
    data = json.loads(LEDGER.read_text(encoding="utf-8"))

    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if data.get("status") != "ACTIVE_NOT_CLOSED":
        errors.append("current frontier must remain ACTIVE_NOT_CLOSED")

    shell = data.get("shell", {})
    if shell.get("gauss_admissible_spin_assignments") != 264962:
        errors.append("Gauss shell count mismatch")
    if shell.get("hilbert_dimension") != 3111637:
        errors.append("Hilbert dimension mismatch")
    if shell.get("s5_spin_orbits") != 2757:
        errors.append("S5 orbit count mismatch")

    mult = data.get("multiplicities", {})
    if mult != EXPECTED_MULT:
        errors.append("S5 multiplicity table mismatch")

    reconstructed = sum(EXPECTED_MULT[k] * S5_DIMS[k] for k in EXPECTED_MULT)
    if reconstructed != 3111637:
        errors.append(f"internal dimension reconstruction mismatch: {reconstructed}")

    closed = data.get("closed_irreps", {})
    required_closed = {"[1^5]", "[5]", "[4,1]"}
    if set(closed) != required_closed:
        errors.append("closed_irreps must contain exactly the three currently certified sectors")
    for key in required_closed:
        if closed.get(key, {}).get("status") != "CLOSED":
            errors.append(f"{key} is not marked CLOSED")

    s4 = data.get("s4_sign_frontier", {})
    if s4.get("total_dimension") != 130112:
        errors.append("S4-sign total dimension mismatch")
    if s4.get("h0_thresholded_maxflow") != 130096:
        errors.append("S4-sign H0 flow mismatch")
    if s4.get("exact_h0_null_directions") != 16:
        errors.append("expected exactly 16 exact H0-null directions")

    h1 = s4.get("h1_lift", {})
    if h1.get("rank") != 16 or h1.get("dimension") != 16:
        errors.append("16D H1 lift must be rank 16/16")
    if not (float(h1.get("sigma_min", 0.0)) > 1.0):
        errors.append("H1 lift sigma_min unexpectedly weak")

    giant = s4.get("giant_component", {})
    if giant.get("columns") != 130007:
        errors.append("giant column count mismatch")
    if giant.get("rank_aware_maxflow") != 130007:
        errors.append("giant rank-aware maxflow mismatch")
    if giant.get("target_flow") != 130007:
        errors.append("giant target flow mismatch")
    if giant.get("deficient_inputs_after_rank_aware_flow") != 0:
        errors.append("giant still has rank-aware flow deficit")

    plan = giant.get("square_minor_plan", {})
    if plan.get("rows") != 130007 or plan.get("columns") != 130007:
        errors.append("square-minor plan dimension mismatch")
    if plan.get("expected_nonzero_scalar_entries") != 47543521:
        errors.append("square-minor nnz estimate mismatch")
    if plan.get("zero_selected_rows") != 0:
        errors.append("square-minor plan contains zero selected rows")

    # CURRENT TRUTH: the numerical sparse rank has not yet been established.
    if plan.get("numerical_rank") is not None:
        errors.append(
            "numerical_rank must remain null until an independently preserved "
            "rank-revealing factorization certificate is committed"
        )
    if plan.get("status") != "NOT_YET_FACTORIZED":
        errors.append("square-minor status must remain NOT_YET_FACTORIZED")

    if s4.get("sector_status") != "ACTIVE_NOT_CLOSED":
        errors.append("[2,1,1,1] must remain ACTIVE_NOT_CLOSED")
    if data.get("finite_depth6_theorem_status") != "NOT_YET_PROVED":
        errors.append("full finite depth-6 theorem must remain NOT_YET_PROVED")

    remaining = data.get("remaining_irreps_after_s4_sign")
    if remaining != ["[3,2]", "[3,1,1]", "[2,2,1]"]:
        errors.append("remaining irrep frontier mismatch")

    result = {
        "valid": not errors,
        "status": data.get("status"),
        "finite_depth6_theorem_status": data.get("finite_depth6_theorem_status"),
        "closed_irreps": sorted(closed),
        "s4_sign_status": s4.get("sector_status"),
        "giant_square_minor": {
            "shape": [plan.get("rows"), plan.get("columns")],
            "expected_nonzero_scalar_entries": plan.get("expected_nonzero_scalar_entries"),
            "numerical_rank": plan.get("numerical_rank"),
            "status": plan.get("status"),
        },
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
