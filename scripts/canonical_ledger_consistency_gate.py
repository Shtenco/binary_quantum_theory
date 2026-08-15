#!/usr/bin/env python3
"""Cross-check canonical human/machine ledgers against frozen evidence.

The repository previously suffered status drift between old and newly audited
Peter-Weyl numbers. This gate checks the high-value canonical anchors that now
define BCQG Core Candidate v1:

- corrected Euclidean return anisotropy;
- exact nonzero Lorentzian raw Y amplitude;
- five-bracket phase;
- preregistered physical H_E^sine two-node HDA PASS;
- operator-first quantum route selection;
- conditional code-bound Euclidean/Lorentzian relative normalization;
- explicit alpha=1/8 joint-cutoff path.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "THEORY_STATUS.md"
CANDIDATE = ROOT / "BCQG_CORE_CANDIDATE_V1.md"
START = ROOT / "START_HERE.md"
LEDGER = ROOT / "theory_gates.json"
LOR_EVIDENCE = ROOT / "verification_results/PETER_WEYL_LORENTZIAN_ENVTRACE_ORBIT.json"
SINE_EVIDENCE = ROOT / "verification_results/PETER_WEYL_TWO_NODE_SINE_HDA.json"

DELTA_ANISO = 2.738458660882762
RETIRED_DELTA = 3.6832250321658044
RAW_Y = 1.3389293521464034
JMAX = 3.5
ENV_STATES = 16
SINE_ENDPOINT = 0.020030338775070305
SINE_PCROSS = 1.0056948923496356
SINE_PGG = 2.007490390559045
SINE_PJOINT = 1.0076444430189475
SINE_RUN = 31855735615
SINE_DIGEST = "sha256:21e2da508fd583d9007a5bd400d074e8cee39990656e6c75e5968d2601323526"
ROUTE_OP_ENDPOINT_TEXT = "3.837772425e-7"
ROUTE_OP_EXP_TEXT = "0.999960897"
EUNORM_TEXT = "-2/(3 hbar)"
FULL_BETA1_TEXT = "32/9"
BARE_BETA1_TEXT = "16/9"
COV_MAX = 1e-12
LEAK_MAX = 1e-12


def find_gate(gates, gate_id):
    rows = [g for g in gates if g.get("id") == gate_id]
    if len(rows) != 1:
        raise RuntimeError(f"expected exactly one {gate_id} gate, found {len(rows)}")
    return rows[0]


def contains_number(text: str, value: float) -> bool:
    return f"{value}" in text


def main() -> int:
    status = STATUS.read_text(encoding="utf-8")
    candidate = CANDIDATE.read_text(encoding="utf-8")
    start = START.read_text(encoding="utf-8")
    ledger_text = LEDGER.read_text(encoding="utf-8")
    ledger = json.loads(ledger_text)
    lor_ev = json.loads(LOR_EVIDENCE.read_text(encoding="utf-8"))
    sine_ev = json.loads(SINE_EVIDENCE.read_text(encoding="utf-8"))
    gates = ledger["gates"]

    pw = find_gate(gates, "PWLOGANISO")
    lor = find_gate(gates, "LORAMPRAW")
    phase = find_gate(gates, "LORPHASE")
    norm = find_gate(gates, "LORNORM")
    route_op = find_gate(gates, "ROUTE_OP")
    sine = find_gate(gates, "E2NODE_SINE")
    order = find_gate(gates, "LORORDER")
    joint = find_gate(gates, "JOINTDIAG")
    core = find_gate(gates, "CORECERT")

    y_pair = lor_ev["onebody_Y_coefficient_raw"]
    y_abs = math.hypot(float(y_pair[0]), float(y_pair[1]))

    checks = {
        # Machine-ledger statuses.
        "pw_gate_status": pw["status"] == "tested_finite",
        "lor_raw_gate_status": lor["status"] == "tested_finite",
        "lor_phase_gate_conditional": phase["status"] == "conditional",
        "lor_norm_gate_conditional": norm["status"] == "conditional",
        "route_op_gate_tested": route_op["status"] == "tested_finite",
        "sine_gate_tested": sine["status"] == "tested_finite",
        "lor_order_gate_open": order["status"] == "open",
        "joint_gate_conditional": joint["status"] == "conditional",
        "core_gate_conditional": core["status"] == "conditional",

        # Corrected anisotropy and retirement hygiene.
        "pw_gate_canonical_delta": contains_number(pw["claim"], DELTA_ANISO),
        "retired_delta_absent_from_machine_ledger": str(RETIRED_DELTA) not in ledger_text,
        "status_has_delta": contains_number(status, DELTA_ANISO),
        "candidate_has_delta": contains_number(candidate, DELTA_ANISO),
        "start_has_delta": contains_number(start, DELTA_ANISO),
        "status_marks_old_delta_retired": str(RETIRED_DELTA) in status and "retired" in status.lower(),
        "candidate_marks_old_delta_retired": str(RETIRED_DELTA) in candidate and "retired" in candidate.lower(),
        "start_marks_old_delta_retired": str(RETIRED_DELTA) in start and "retired" in start.lower(),

        # Raw Lorentzian evidence.
        "lor_evidence_passed": bool(lor_ev.get("passed", False)),
        "lor_evidence_decision": lor_ev.get("decision") == "NONZERO_TRUE_ONE_BODY_RAW_Y",
        "lor_evidence_jmax": abs(float(lor_ev["Jmax"]) - JMAX) < 1e-15,
        "lor_evidence_environment_count": int(lor_ev["environment_states"]) == ENV_STATES,
        "lor_evidence_raw_y": abs(y_abs - RAW_Y) < 1e-12,
        "lor_evidence_covariance": float(lor_ev["T132_covariance_relative_error"]) < COV_MAX,
        "lor_evidence_leakage": float(lor_ev["max_physical_basis_volume_leakage"]) < LEAK_MAX,
        "status_has_raw_y": contains_number(status, RAW_Y),
        "candidate_has_raw_y": contains_number(candidate, RAW_Y),

        # Five-bracket phase.
        "lor_phase_claim_has_five_brackets": "five Poisson brackets" in phase["claim"],
        "lor_phase_claim_has_minus_i": "(1/i)^5=-i" in phase["claim"],
        "status_has_five_bracket_phase": "(1/i)^5=-i" in status,
        "candidate_has_five_bracket_phase": "(1/i)^5=-i" in candidate,

        # Preregistered physical sine HDA evidence.
        "sine_evidence_passed": bool(sine_ev.get("passed", False)),
        "sine_endpoint": abs(float(sine_ev["last_joint_defect_over_D"]) - SINE_ENDPOINT) < 1e-15,
        "sine_cross_exponent": abs(float(sine_ev["fitted_cross_exponent"]) - SINE_PCROSS) < 1e-14,
        "sine_GG_exponent": abs(float(sine_ev["fitted_pure_GG_relative_exponent"]) - SINE_PGG) < 1e-14,
        "sine_joint_exponent": abs(float(sine_ev["fitted_joint_exponent"]) - SINE_PJOINT) < 1e-14,
        "sine_provenance_run": int(sine_ev["provenance"]["workflow_run_id"]) == SINE_RUN,
        "sine_provenance_digest": sine_ev["provenance"]["artifact_digest"] == SINE_DIGEST,
        "status_has_sine_endpoint": contains_number(status, SINE_ENDPOINT),
        "candidate_has_sine_endpoint": contains_number(candidate, SINE_ENDPOINT),
        "start_has_sine_endpoint": contains_number(start, SINE_ENDPOINT),

        # Operator-first quantum route.
        "route_op_claim_has_endpoint": ROUTE_OP_ENDPOINT_TEXT in route_op["claim"],
        "route_op_claim_has_exponent": ROUTE_OP_EXP_TEXT in route_op["claim"],
        "status_selects_operator_first": "R_{op}" in status or "R_op" in status,
        "candidate_selects_operator_first": "R_{op}" in candidate or "R_op" in candidate,
        "start_selects_operator_first": "R_op" in start,

        # Relative normalization.
        "normalization_gate_has_nE": EUNORM_TEXT in norm["claim"],
        "normalization_gate_has_full_beta1": FULL_BETA1_TEXT in norm["claim"],
        "normalization_gate_has_bare_beta1": BARE_BETA1_TEXT in norm["claim"],
        "status_has_normalization": "32" in status and "16" in status and "9" in status,
        "candidate_has_normalization": "32" in candidate and "16" in candidate and "9" in candidate,

        # Joint-cutoff path and frontier.
        "canonical_joint_path_in_status": "epsilon^-1/8" in status or "epsilon^{-1/8}" in status,
        "canonical_joint_path_in_candidate": "epsilon^{-1/8}" in candidate or "epsilon^-1/8" in candidate,
        "frontier_is_full_HDA_in_status": "H_E^sine+(1+beta^2)H_L+R_operator-first" in status or "H_E^{sine}+(1+\\beta^2)H_L+R_{op}" in status,
        "frontier_is_full_HDA_in_candidate": "H_E^{sine}" in candidate and "H_L" in candidate and "R_{op}" in candidate,
    }

    out = {
        "status": "canonical human/machine/evidence consistency",
        "passed": all(checks.values()),
        "anchors": {
            "Delta_aniso_ret": DELTA_ANISO,
            "Lorentzian_raw_Y_abs": RAW_Y,
            "Lorentzian_Jmax": JMAX,
            "Lorentzian_environment_states": ENV_STATES,
            "Lorentzian_nested_bracket_count": 5,
            "Lorentzian_dimensionless_phase": "-i",
            "physical_sine_joint_endpoint": SINE_ENDPOINT,
            "physical_sine_p_cross": SINE_PCROSS,
            "physical_sine_p_GG": SINE_PGG,
            "physical_sine_p_joint": SINE_PJOINT,
            "operator_first_route_endpoint_text": ROUTE_OP_ENDPOINT_TEXT,
            "operator_first_route_exponent_text": ROUTE_OP_EXP_TEXT,
            "Euclidean_nE": "-2/(3 hbar)",
            "full_beta1_Lorentzian_magnitude": "32/(9 hbar^7)",
            "bare_beta1_HL_magnitude": "16/(9 hbar^7)",
            "joint_cutoff_alpha": "1/8",
        },
        "checks": checks,
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
