#!/usr/bin/env python3
"""Validate the fail-closed physicalization ledger.

This validator intentionally keeps two different propositions separate:

1. the declared finite/exact structural candidate recorded in theory_gates.json;
2. the stronger physicalization chain required before an interacting graviton
   pole, six-Wilson vector, common scale or experimental claim can be frozen.

A GREEN result is therefore allowed (and currently required) to report
``structural_candidate_closed=True`` together with
``physicalization_complete=False``.  GREEN means the repository states its
scientific boundary consistently; it does not mean every physical problem is
solved.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "physicalization_gates.json"
STRUCTURAL_LEDGER = ROOT / "theory_gates.json"

ROLE_STATUSES = {
    "reference": {"proved", "tested_finite"},
    "positive_control": {"tested_finite"},
    "physical": {"open_physical", "frozen"},
    "experiment": {"experimental_test"},
}
REQUIRED_KEYS = {"id", "status", "closure_role", "claim", "evidence", "hard_scope"}
ID_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")
EXPECTED_REQUIRED_PHYSICAL = {
    "PHYSICAL_PROJECTOR_HISTORY",
    "CONNECTED_INTERBLOCK_HISTORY",
    "PHYSICAL_TT_KERNEL",
    "IR_SIX_VECTOR",
    "COMMON_SCALE_CALIBRATION",
}
STRUCTURAL_CORE_ACCEPTED = {"proved", "tested_finite", "conditional"}


def safe_relative_path(value: str) -> bool:
    path = PurePosixPath(value)
    return bool(value) and not path.is_absolute() and ".." not in path.parts


def load_json(path: Path, errors: list[str]) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path.name}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{path.name}: root must be an object")
        return {}
    return value


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    errors: list[str] = []
    data = load_json(LEDGER, errors)
    structural = load_json(STRUCTURAL_LEDGER, errors)

    if data.get("schema_version") != 1:
        errors.append("physicalization schema_version must equal 1")

    expected_policy = {role: sorted(values) for role, values in ROLE_STATUSES.items()}
    policy = data.get("status_policy")
    normalized_policy = {
        role: sorted(values) if isinstance(values, list) else values
        for role, values in policy.items()
    } if isinstance(policy, dict) else None
    if normalized_policy != expected_policy:
        errors.append("physicalization status_policy does not match verifier semantics")

    if data.get("structural_status_source") != "theory_gates.json":
        errors.append("structural_status_source must be theory_gates.json")

    gates = data.get("gates", [])
    if not isinstance(gates, list):
        errors.append("gates must be a list")
        gates = []

    rows: dict[str, dict] = {}
    counts_by_role = {role: 0 for role in ROLE_STATUSES}
    counts_by_status: dict[str, int] = {}

    for index, gate in enumerate(gates):
        label = f"gate[{index}]"
        if not isinstance(gate, dict):
            errors.append(f"{label}: gate must be an object")
            continue

        missing = REQUIRED_KEYS - set(gate)
        if missing:
            errors.append(f"{label}: missing keys {sorted(missing)}")

        gate_id = gate.get("id")
        if not isinstance(gate_id, str) or not ID_RE.fullmatch(gate_id):
            errors.append(f"{label}: invalid id {gate_id!r}")
            continue
        if gate_id in rows:
            errors.append(f"duplicate gate id {gate_id}")
            continue

        role = gate.get("closure_role")
        status = gate.get("status")
        if role not in ROLE_STATUSES:
            errors.append(f"{gate_id}: invalid closure_role {role!r}")
        else:
            counts_by_role[role] += 1
            if status not in ROLE_STATUSES[role]:
                errors.append(f"{gate_id}: illegal status {status!r} for role {role!r}")
        counts_by_status[str(status)] = counts_by_status.get(str(status), 0) + 1

        claim = gate.get("claim")
        scope = gate.get("hard_scope")
        if not isinstance(claim, str) or not claim.strip():
            errors.append(f"{gate_id}: claim must be non-empty text")
        if not isinstance(scope, str) or not scope.strip():
            errors.append(f"{gate_id}: hard_scope must be non-empty text")

        evidence = gate.get("evidence", [])
        if not isinstance(evidence, list) or not evidence or not all(isinstance(x, str) for x in evidence):
            errors.append(f"{gate_id}: evidence must be a non-empty list of paths")
            evidence = []
        if len(evidence) != len(set(evidence)):
            errors.append(f"{gate_id}: duplicate evidence path")
        for relative in evidence:
            if not safe_relative_path(relative):
                errors.append(f"{gate_id}: unsafe evidence path {relative!r}")
            elif not (ROOT / relative).is_file():
                errors.append(f"{gate_id}: missing evidence file {relative}")

        rows[gate_id] = gate

    required_declared = data.get("required_physical_gates")
    if not isinstance(required_declared, list) or set(required_declared) != EXPECTED_REQUIRED_PHYSICAL:
        errors.append(
            "required_physical_gates must equal the frozen five-gate physicalization frontier"
        )

    missing_required = sorted(EXPECTED_REQUIRED_PHYSICAL - set(rows))
    if missing_required:
        errors.append(f"missing required physical gates: {missing_required}")

    for gate_id in EXPECTED_REQUIRED_PHYSICAL & set(rows):
        if rows[gate_id].get("closure_role") != "physical":
            errors.append(f"{gate_id}: required physical gate must have role='physical'")

    # Claim-discipline guards against the historically dangerous shortcuts.
    if "CONSTRAINT_FESHBACH" in rows:
        scope = str(rows["CONSTRAINT_FESHBACH"].get("hard_scope", "")).lower()
        if "not physical omega" not in scope:
            errors.append("CONSTRAINT_FESHBACH must state that z is not physical omega")
    if "MASTER_PROJECTOR_FINITE" in rows:
        scope = str(rows["MASTER_PROJECTOR_FINITE"].get("hard_scope", "")).lower()
        if "finite" not in scope or "rigging" not in scope:
            errors.append("MASTER_PROJECTOR_FINITE must preserve finite/rigging-limit scope")
    for gate_id in ("RELATIONAL_HISTORY_POSITIVE_CONTROL", "RELATIONAL_METRIC_SOURCE_POSITIVE_CONTROL"):
        if gate_id in rows and "positive control" not in str(rows[gate_id].get("hard_scope", "")).lower():
            errors.append(f"{gate_id} must be explicitly labelled a positive control")
    if "PHYSICAL_TT_KERNEL" in rows:
        scope = str(rows["PHYSICAL_TT_KERNEL"].get("hard_scope", "")).lower()
        if "not promoted to the physical omega" not in scope:
            errors.append("PHYSICAL_TT_KERNEL must reject spectral/history labels as physical omega")

    # Derive the current physical state from gate statuses rather than prose.
    def frozen(gate_id: str) -> bool:
        return gate_id in rows and rows[gate_id].get("status") == "frozen"

    projector_closed = frozen("PHYSICAL_PROJECTOR_HISTORY")
    tt_kernel_frozen = frozen("PHYSICAL_TT_KERNEL")
    six_vector_frozen = frozen("IR_SIX_VECTOR")
    common_scale_calibrated = frozen("COMMON_SCALE_CALIBRATION")
    physicalization_complete = all(frozen(gate_id) for gate_id in EXPECTED_REQUIRED_PHYSICAL)

    declared_pairs = {
        "physical_projector_history_closed_declared": projector_closed,
        "physical_tt_kernel_frozen_declared": tt_kernel_frozen,
        "ir_six_wilson_vector_frozen_declared": six_vector_frozen,
        "common_physical_scale_calibrated_declared": common_scale_calibrated,
    }
    for key, derived in declared_pairs.items():
        if data.get(key) is not derived:
            errors.append(f"{key}={data.get(key)!r} disagrees with derived value {derived!r}")

    # Structural closure is read independently from the v2 structural ledger.
    structural_gates = structural.get("gates", []) if isinstance(structural.get("gates", []), list) else []
    structural_core = [g for g in structural_gates if isinstance(g, dict) and g.get("closure_role") == "core"]
    structural_candidate_closed = bool(structural_core) and all(
        g.get("status") in STRUCTURAL_CORE_ACCEPTED for g in structural_core
    ) and structural.get("core_theory_closed_declared") is True

    if structural.get("experimentally_confirmed") is not False:
        errors.append("theory_gates.json must keep experimentally_confirmed=false")
    if data.get("experimentally_confirmed") is not False:
        errors.append("physicalization_gates.json must keep experimentally_confirmed=false")

    result = {
        "schema_version": data.get("schema_version"),
        "gate_count": len(gates),
        "counts_by_role": counts_by_role,
        "counts_by_status": counts_by_status,
        "structural_candidate_closed": bool(structural_candidate_closed),
        "physical_projector_history_closed": bool(projector_closed),
        "physical_tt_kernel_frozen": bool(tt_kernel_frozen),
        "ir_six_wilson_vector_frozen": bool(six_vector_frozen),
        "common_physical_scale_calibrated": bool(common_scale_calibrated),
        "physicalization_complete": bool(physicalization_complete),
        "experimentally_confirmed": False,
        "required_physical_gate_statuses": {
            gate_id: rows.get(gate_id, {}).get("status")
            for gate_id in sorted(EXPECTED_REQUIRED_PHYSICAL)
        },
        "scientific_interpretation": (
            "A valid GREEN result certifies truthful separation of the closed structural candidate "
            "from the still-open physical projector/history, interacting TT kernel, IR six-vector "
            "and one-scale calibration. It is not experimental confirmation."
        ),
        "errors": errors,
        "valid": not errors,
    }

    text = json.dumps(result, ensure_ascii=False, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
