#!/usr/bin/env python3
"""Cross-check the canonical human/machine ledgers against frozen evidence.

This gate exists because the repository previously developed status drift: an
older Peter-Weyl anisotropy number remained in THEORY_STATUS after the audited
calculation had changed the canonical value.  The gate intentionally checks a
small set of high-value anchors rather than attempting to parse every equation
from Markdown.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "THEORY_STATUS.md"
CANDIDATE = ROOT / "BCQG_CORE_CANDIDATE_V1.md"
LEDGER = ROOT / "theory_gates.json"
LOR_EVIDENCE = ROOT / "verification_results/PETER_WEYL_LORENTZIAN_ENVTRACE_ORBIT.json"

DELTA_ANISO = 2.738458660882762
RAW_Y = 1.3389293521464034
JMAX = 3.5
ENV_STATES = 16
COV_MAX = 1e-12
LEAK_MAX = 1e-12


def find_gate(gates, gate_id):
    rows = [g for g in gates if g.get("id") == gate_id]
    if len(rows) != 1:
        raise RuntimeError(f"expected exactly one {gate_id} gate, found {len(rows)}")
    return rows[0]


def main() -> int:
    status = STATUS.read_text(encoding="utf-8")
    candidate = CANDIDATE.read_text(encoding="utf-8")
    ledger_text = LEDGER.read_text(encoding="utf-8")
    ledger = json.loads(ledger_text)
    evidence = json.loads(LOR_EVIDENCE.read_text(encoding="utf-8"))
    gates = ledger["gates"]

    pw = find_gate(gates, "PWLOGANISO")
    lor = find_gate(gates, "LORAMPRAW")
    order = find_gate(gates, "LORORDER")
    joint = find_gate(gates, "JOINTDIAG")
    core = find_gate(gates, "CORECERT")

    y_pair = evidence["onebody_Y_coefficient_raw"]
    y_abs = math.hypot(float(y_pair[0]), float(y_pair[1]))

    checks = {
        "pw_gate_status": pw["status"] == "tested_finite",
        "pw_gate_canonical_delta": f"{DELTA_ANISO}" in pw["claim"],
        "retired_delta_absent_from_machine_ledger": "3.6832250321658044" not in ledger_text,
        "lor_raw_gate_status": lor["status"] == "tested_finite",
        "lor_order_gate_open": order["status"] == "open",
        "joint_gate_conditional": joint["status"] == "conditional",
        "core_gate_conditional": core["status"] == "conditional",
        "evidence_passed": bool(evidence.get("passed", False)),
        "evidence_decision": evidence.get("decision") == "NONZERO_TRUE_ONE_BODY_RAW_Y",
        "evidence_jmax": abs(float(evidence["Jmax"]) - JMAX) < 1e-15,
        "evidence_environment_count": int(evidence["environment_states"]) == ENV_STATES,
        "evidence_raw_y": abs(y_abs - RAW_Y) < 1e-12,
        "evidence_covariance": float(evidence["T132_covariance_relative_error"]) < COV_MAX,
        "evidence_leakage": float(evidence["max_physical_basis_volume_leakage"]) < LEAK_MAX,
        "status_has_delta": f"{DELTA_ANISO}" in status,
        "candidate_has_delta": f"{DELTA_ANISO}" in candidate,
        "status_has_raw_y": f"{RAW_Y}" in status,
        "candidate_has_raw_y": f"{RAW_Y}" in candidate,
        "status_marks_old_delta_retired": "3.6832250321658044" in status and "retired" in status.lower(),
        "candidate_excludes_retired_delta": "3.6832250321658044" not in candidate,
        "canonical_joint_path_in_status": "epsilon^-1/8" in status,
        "canonical_joint_path_in_candidate": "epsilon^{-1/8}" in candidate or "epsilon^-1/8" in candidate,
    }

    out = {
        "status": "canonical human/machine/evidence consistency",
        "passed": all(checks.values()),
        "anchors": {
            "Delta_aniso_ret": DELTA_ANISO,
            "Lorentzian_raw_Y_abs": RAW_Y,
            "Lorentzian_Jmax": JMAX,
            "Lorentzian_environment_states": ENV_STATES,
            "joint_cutoff_alpha": "1/8",
        },
        "checks": checks,
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
