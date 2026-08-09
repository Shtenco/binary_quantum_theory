#!/usr/bin/env python3
"""Validate the machine-readable proof-obligation ledger."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "theory_gates.json"
ALLOWED_STATUSES = {"proved", "conditional", "tested_finite", "open"}


def main() -> int:
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    allowed = set(data["allowed_statuses"])
    gates = data["gates"]
    ids = [gate["id"] for gate in gates]
    errors: list[str] = []
    if allowed != ALLOWED_STATUSES:
        errors.append("allowed_statuses does not match verifier schema")
    if len(ids) != len(set(ids)):
        errors.append("gate identifiers must be unique")
    for gate in gates:
        if gate["status"] not in allowed:
            errors.append(f"{gate['id']}: invalid status {gate['status']!r}")
        evidence = gate.get("evidence", [])
        if gate["status"] == "proved" and not evidence:
            errors.append(f"{gate['id']}: proved gate has no evidence")
        for relative in evidence:
            if not (ROOT / relative).is_file():
                errors.append(f"{gate['id']}: missing evidence file {relative}")
    counts = {status: sum(gate["status"] == status for gate in gates)
              for status in sorted(ALLOWED_STATUSES)}
    result = {
        "schema_version": data["schema_version"],
        "gate_count": len(gates),
        "status_counts": counts,
        "complete": all(gate["status"] == "proved" for gate in gates),
        "errors": errors,
        "valid": not errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
