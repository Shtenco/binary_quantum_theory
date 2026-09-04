#!/usr/bin/env python3
"""Validate the fail-closed cosmology/interference/lensing frontier ledger."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "cosmology_interference_gates.json"
ID_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")
ROLE_STATUSES = {
    "reference": {"tested_finite"},
    "physical": {"open_physical", "frozen"},
    "experiment": {"experimental_test"},
}
REQUIRED_PHYSICAL = {
    "DYNAMICAL_MAXWELL_KERNEL",
    "PHYSICAL_BACKGROUND_COSMOLOGY",
    "PHYSICAL_SCALAR_COSMOLOGY",
    "LENSING_DYNAMICS_CLOSURE",
}
REQUIRED_REFERENCE = {
    "HISTORY_INTERFERENCE_REFERENCE",
    "GRAVITATIONAL_WAVE_OPTICS_REFERENCE",
    "BACKGROUND_FLUID_INFERENCE_REFERENCE",
    "SCALAR_LENSING_CONSISTENCY_REFERENCE",
}


def safe_path(value: str) -> bool:
    p = PurePosixPath(value)
    return bool(value) and not p.is_absolute() and ".." not in p.parts


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    errors: list[str] = []
    try:
        data = json.loads(LEDGER.read_text(encoding="utf-8"))
    except Exception as exc:
        data = {}
        errors.append(f"ledger load failed: {exc}")

    if data.get("schema_version") != 1:
        errors.append("schema_version must equal 1")
    if data.get("experimentally_confirmed") is not False:
        errors.append("experimentally_confirmed must remain false")

    rows = {}
    for idx, gate in enumerate(data.get("gates", [])):
        if not isinstance(gate, dict):
            errors.append(f"gate[{idx}] must be object")
            continue
        gid = gate.get("id")
        role = gate.get("closure_role")
        status = gate.get("status")
        if not isinstance(gid, str) or not ID_RE.fullmatch(gid):
            errors.append(f"gate[{idx}] invalid id")
            continue
        if gid in rows:
            errors.append(f"duplicate gate {gid}")
        rows[gid] = gate
        if role not in ROLE_STATUSES or status not in ROLE_STATUSES.get(role, set()):
            errors.append(f"{gid}: invalid role/status {role}/{status}")
        for key in ("claim", "hard_scope"):
            if not isinstance(gate.get(key), str) or not gate[key].strip():
                errors.append(f"{gid}: missing {key}")
        ev = gate.get("evidence")
        if not isinstance(ev, list) or not ev:
            errors.append(f"{gid}: evidence must be non-empty list")
            continue
        for rel in ev:
            if not isinstance(rel, str) or not safe_path(rel):
                errors.append(f"{gid}: unsafe evidence path {rel!r}")
            elif not (ROOT / rel).is_file():
                errors.append(f"{gid}: missing evidence {rel}")

    for gid in sorted(REQUIRED_REFERENCE):
        if rows.get(gid, {}).get("status") != "tested_finite":
            errors.append(f"{gid}: reference must remain tested_finite")
    for gid in sorted(REQUIRED_PHYSICAL):
        if gid not in rows:
            errors.append(f"missing physical gate {gid}")
        elif rows[gid].get("closure_role") != "physical":
            errors.append(f"{gid}: must be physical")

    frozen = {gid: rows.get(gid, {}).get("status") == "frozen" for gid in REQUIRED_PHYSICAL}
    complete = all(frozen.values())
    if data.get("physical_outputs_frozen") is not complete:
        errors.append("physical_outputs_frozen disagrees with derived physical gate state")

    # Hard anti-shortcut language checks.
    if "PHYSICAL_BACKGROUND_COSMOLOGY" in rows and "no bqg background" not in rows["PHYSICAL_BACKGROUND_COSMOLOGY"]["hard_scope"].lower():
        errors.append("PHYSICAL_BACKGROUND_COSMOLOGY must state that no BQG background component is yet derived")
    if "LENSING_DYNAMICS_CLOSURE" in rows and "prerequisites only" not in rows["LENSING_DYNAMICS_CLOSURE"]["hard_scope"].lower():
        errors.append("LENSING_DYNAMICS_CLOSURE must preserve reference-vs-physical boundary")

    result = {
        "schema_version": 1,
        "valid": not errors,
        "reference_gate_statuses": {gid: rows.get(gid, {}).get("status") for gid in sorted(REQUIRED_REFERENCE)},
        "physical_gate_statuses": {gid: rows.get(gid, {}).get("status") for gid in sorted(REQUIRED_PHYSICAL)},
        "physical_outputs_frozen": complete,
        "experimentally_confirmed": False,
        "errors": errors,
    }
    text = json.dumps(result, indent=2, ensure_ascii=False)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
