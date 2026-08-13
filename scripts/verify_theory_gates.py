#!/usr/bin/env python3
"""Validate the machine-readable proof-obligation ledger.

The validator is intentionally conservative: it checks schema integrity, claim
classification and evidence wiring. It does not replace running the evidence
scripts themselves; CI executes a curated regression subset separately.
"""

from __future__ import annotations

import json
import re
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "theory_gates.json"
ALLOWED_STATUSES = {"proved", "conditional", "tested_finite", "open"}
EVIDENCE_REQUIRED = {"proved", "tested_finite"}
ID_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")
REQUIRED_KEYS = {"id", "status", "claim", "evidence"}


def _safe_relative_path(value: str) -> bool:
    path = PurePosixPath(value)
    return bool(value) and not path.is_absolute() and ".." not in path.parts


def main() -> int:
    errors: list[str] = []

    try:
        data = json.loads(LEDGER.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid": False, "errors": [str(exc)]}, indent=2))
        return 1

    if not isinstance(data, dict):
        errors.append("ledger root must be a JSON object")
        data = {}

    if data.get("schema_version") != 1:
        errors.append("schema_version must equal 1")

    allowed_raw = data.get("allowed_statuses", [])
    if not isinstance(allowed_raw, list):
        errors.append("allowed_statuses must be a list")
        allowed_raw = []
    allowed = set(allowed_raw)
    if allowed != ALLOWED_STATUSES:
        errors.append("allowed_statuses does not match verifier schema")

    gates = data.get("gates", [])
    if not isinstance(gates, list):
        errors.append("gates must be a list")
        gates = []

    ids: list[str] = []
    for index, gate in enumerate(gates):
        label = f"gate[{index}]"
        if not isinstance(gate, dict):
            errors.append(f"{label}: gate must be an object")
            continue

        missing = REQUIRED_KEYS - set(gate)
        if missing:
            errors.append(f"{label}: missing keys {sorted(missing)}")

        gate_id = gate.get("id", "")
        if not isinstance(gate_id, str) or not ID_RE.fullmatch(gate_id):
            errors.append(f"{label}: invalid id {gate_id!r}")
        else:
            ids.append(gate_id)
            label = gate_id

        status = gate.get("status")
        if status not in allowed:
            errors.append(f"{label}: invalid status {status!r}")

        claim = gate.get("claim")
        if not isinstance(claim, str) or not claim.strip():
            errors.append(f"{label}: claim must be non-empty text")

        evidence = gate.get("evidence", [])
        if not isinstance(evidence, list) or not all(isinstance(x, str) for x in evidence):
            errors.append(f"{label}: evidence must be a list of paths")
            evidence = []

        if status in EVIDENCE_REQUIRED and not evidence:
            errors.append(f"{label}: {status} gate has no evidence")

        if len(evidence) != len(set(evidence)):
            errors.append(f"{label}: duplicate evidence path")

        for relative in evidence:
            if not _safe_relative_path(relative):
                errors.append(f"{label}: unsafe evidence path {relative!r}")
                continue
            if not (ROOT / relative).is_file():
                errors.append(f"{label}: missing evidence file {relative}")

    if len(ids) != len(set(ids)):
        duplicates = sorted({x for x in ids if ids.count(x) > 1})
        errors.append(f"gate identifiers must be unique; duplicates={duplicates}")

    counts = {
        status: sum(isinstance(g, dict) and g.get("status") == status for g in gates)
        for status in sorted(ALLOWED_STATUSES)
    }
    result = {
        "schema_version": data.get("schema_version"),
        "gate_count": len(gates),
        "status_counts": counts,
        "complete": bool(gates) and all(
            isinstance(g, dict) and g.get("status") == "proved" for g in gates
        ),
        "errors": errors,
        "valid": not errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
