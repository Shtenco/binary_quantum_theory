#!/usr/bin/env python3
"""Fail-closed verifier for the corrected finite depth-6 BQG frontier.

This validator deliberately distinguishes:
- finite numerical master closure,
- structural branch-sum closure,
- pending independent numerical witnesses,
- the full finite depth-6 theorem,
- continuum/physical completion.

It MUST fail if the canonical ledger reopens already closed structural work,
reverts [2,1,1,1] to ACTIVE, or promotes the full theorem beyond preserved
evidence.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "depth6_frontier.json"
CERT_2111 = ROOT / "BQG_DEPTH6_2111_MASTER_CLOSED_2026-10-01.json"

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
EXPECTED_STRUCTURAL = {
    "[3,2]": ("2755/2755", "130903/130903", 0),
    "[3,1,1]": ("2719/2719", "153455/153455", 0),
    "[2,2,1]": ("2749/2749", "130503/130503", 0),
    "[2,1,1,1]": ("2712/2712", "103318/103318", 0),
}


def require(errors: list[str], condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    errors: list[str] = []
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    cert = json.loads(CERT_2111.read_text(encoding="utf-8"))

    require(errors, data.get("schema_version") == 1, "ledger schema_version must be 1")
    require(errors, cert.get("schema_version") == 1, "2111 certificate schema_version must be 1")
    require(errors, data.get("status") == "NUMERICAL_WITNESSES_PENDING", "frontier status mismatch")

    shell = data.get("shell", {})
    require(errors, shell.get("gauss_admissible_spin_assignments") == 264962, "Gauss shell count mismatch")
    require(errors, shell.get("hilbert_dimension") == 3111637, "Hilbert dimension mismatch")
    require(errors, shell.get("s5_spin_orbits") == 2757, "S5 orbit count mismatch")

    mult = data.get("multiplicities", {})
    require(errors, mult == EXPECTED_MULT, "S5 multiplicity table mismatch")
    reconstructed = sum(EXPECTED_MULT[k] * S5_DIMS[k] for k in EXPECTED_MULT)
    require(errors, reconstructed == 3111637, f"internal dimension reconstruction mismatch: {reconstructed}")

    # Structural support/capacity is already closed for all seven S5 irreps.
    require(
        errors,
        data.get("structural_depth6_status") == "CLOSED_FOR_ALL_7_S5_IRREPS",
        "all-seven-irrep structural closure must remain frozen",
    )
    support = data.get("structural_support", {})
    for key, (blocks, columns, remainder) in EXPECTED_STRUCTURAL.items():
        s = support.get(key, {})
        require(errors, s.get("status") == "CLOSED", f"{key} structural status must remain CLOSED")
        require(errors, s.get("blocks") == blocks, f"{key} structural block ledger mismatch")
        require(errors, s.get("columns") == columns, f"{key} structural column ledger mismatch")
        require(errors, s.get("remainder") == remainder, f"{key} structural remainder must remain zero")

    closed = data.get("closed_irreps", {})
    required_closed = {"[1^5]", "[5]", "[4,1]", "[2,1,1,1]"}
    require(errors, set(closed) == required_closed, "closed_irreps must contain the four certified sectors")
    for key in ("[1^5]", "[5]", "[4,1]"):
        require(errors, closed.get(key, {}).get("status") == "CLOSED", f"{key} is not marked CLOSED")
    c2111 = closed.get("[2,1,1,1]", {})
    require(errors, c2111.get("status") == "CLOSED_FINITE_NUMERICAL", "[2,1,1,1] must be CLOSED_FINITE_NUMERICAL")
    require(errors, c2111.get("rank") == 103318, "[2,1,1,1] rank mismatch")
    require(errors, c2111.get("dimension") == 103318, "[2,1,1,1] dimension mismatch")
    require(errors, c2111.get("kernel") == "empty", "[2,1,1,1] kernel must be empty")
    require(errors, c2111.get("certificate") == CERT_2111.name, "[2,1,1,1] certificate pointer mismatch")

    # Verify the preserved [2,1,1,1] master certificate rather than trusting only the ledger.
    require(errors, cert.get("status") == "PASS", "2111 master certificate must be PASS")
    require(errors, cert.get("input_dimension") == 130112, "2111 S4-sign input dimension mismatch")
    h0 = cert.get("h0", {})
    zero = h0.get("exact_zero_subspace", {})
    require(errors, zero.get("dimension") == 16, "2111 exact H0 kernel dimension mismatch")
    require(errors, h0.get("complement_dimension") == 130096, "2111 H0 complement dimension mismatch")
    main_q = h0.get("main_unique_q_certificate", {})
    residual = h0.get("residual_sparse_certificate", {})
    require(errors, main_q.get("columns") == 123744, "2111 main H0 column count mismatch")
    require(errors, residual.get("columns") == 6352, "2111 residual H0 column count mismatch")
    require(errors, main_q.get("columns", 0) + residual.get("columns", 0) == 130096, "2111 H0 complement partition mismatch")
    require(errors, float(main_q.get("selected_sigma_min", 0.0)) > 1e-2, "2111 main H0 sigma_min below certified threshold")
    require(errors, float(residual.get("sigma_min", 0.0)) > 0.3, "2111 residual H0 sigma_min unexpectedly weak")
    require(errors, bool(h0.get("decomposition_row_disjoint")), "2111 H0 decomposition must remain row-disjoint")

    h1 = cert.get("h1_on_exact_h0_kernel", {})
    require(errors, h1.get("dimension") == 16 and h1.get("rank") == 16, "2111 H1 lift must remain rank 16/16")
    require(errors, float(h1.get("sigma_min", 0.0)) > 1.0, "2111 H1 sigma_min unexpectedly weak")
    require(errors, bool(h1.get("fresh_recompute")), "2111 H1 lift must come from fresh recompute")

    master = cert.get("master", {})
    require(errors, master.get("s4_sign_kernel_dimension") == 0, "2111 S4-sign master kernel must be empty")
    require(errors, master.get("s4_sign_status") == "CLOSED", "2111 S4-sign certificate not CLOSED")
    consequence = cert.get("irrep_consequence", {}).get("[2,1,1,1]", {})
    require(errors, consequence.get("dimension") == 103318, "2111 irrep consequence dimension mismatch")
    require(errors, consequence.get("rank") == 103318, "2111 irrep consequence rank mismatch")
    require(errors, consequence.get("kernel") == "empty", "2111 irrep consequence kernel mismatch")
    require(errors, consequence.get("status") == "CLOSED", "2111 irrep consequence status mismatch")

    s4 = data.get("s4_sign_frontier", {})
    require(errors, s4.get("total_dimension") == 130112, "S4-sign total dimension mismatch")
    require(errors, s4.get("exact_h0_null_directions") == 16, "S4-sign exact H0-null dimension mismatch")
    require(errors, s4.get("h0_complement_dimension") == 130096, "S4-sign H0 complement dimension mismatch")
    require(errors, s4.get("h0_complement_rank") == 130096, "S4-sign H0 complement rank mismatch")
    require(errors, s4.get("master_kernel_dimension") == 0, "S4-sign master kernel dimension mismatch")
    require(errors, s4.get("sector_status") == "CLOSED_FINITE_NUMERICAL", "[2,1,1,1] frontier must not regress to ACTIVE")
    require(errors, s4.get("obsolete_gate", {}).get("status") == "SUPERSEDED_DO_NOT_USE_AS_BLOCKER", "obsolete 130007 minor must not remain a blocking gate")

    # [3,2] is structurally closed; only its independent numerical witness remains.
    witnesses = data.get("numerical_master_witnesses", {})
    w32 = witnesses.get("[3,2]", {})
    require(errors, w32.get("structural_status") == "CLOSED", "[3,2] structural proof was incorrectly reopened")
    require(errors, w32.get("dimension") == 130903, "[3,2] numerical witness dimension mismatch")
    require(errors, w32.get("blocks") == 2755, "[3,2] numerical witness block count mismatch")
    require(errors, w32.get("status") == "RECOVER_OR_FINISH", "[3,2] must be recovery-first, not structural NEXT")
    require(errors, data.get("current_numerical_witness") == "[3,2]", "current numerical witness target mismatch")
    require(
        errors,
        data.get("remaining_numerical_irreps") == ["[3,2]", "[3,1,1]", "[2,2,1]"],
        "remaining numerical irrep frontier mismatch",
    )

    do_not = data.get("do_not_recompute_for_32", [])
    require(errors, any("130903/130903" in x for x in do_not), "[3,2] structural 130903/130903 must be frozen as do-not-recompute")
    require(errors, any("Jucys" in x for x in do_not), "[3,2] Jucys selector work must be frozen as do-not-recompute")

    require(errors, data.get("finite_depth6_theorem_status") == "NOT_YET_PROVED", "full finite depth-6 theorem must remain NOT_YET_PROVED")
    require(errors, cert.get("finite_depth6_full_theorem_status") == "NOT_YET_PROVED", "2111 certificate must not promote full depth-6 theorem")

    result = {
        "valid": not errors,
        "status": data.get("status"),
        "structural_depth6_status": data.get("structural_depth6_status"),
        "finite_depth6_theorem_status": data.get("finite_depth6_theorem_status"),
        "closed_irreps": sorted(closed),
        "s4_sign_status": s4.get("sector_status"),
        "s4_sign_master_kernel_dimension": s4.get("master_kernel_dimension"),
        "current_numerical_witness": data.get("current_numerical_witness"),
        "32_structural_status": w32.get("structural_status"),
        "32_numerical_status": w32.get("status"),
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
