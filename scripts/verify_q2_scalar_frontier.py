#!/usr/bin/env python3
"""Validate the fail-closed q=2 scalar-effective-action frontier.

A green result means the repository correctly distinguishes:
- exact local shape / collective-volume positive controls;
- the frozen universal conserved external TEST-PROBE convention;
- still-open theory-specific volume-history, lapse/shift response, connected
  scalar history, physical scalar kernel, background cosmology and lensing.

GREEN is deliberately not a claim that dark matter, dark energy, a realistic
matter sector or Gamma_scalar^(2)(omega,k) has been derived.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath

ROOT=Path(__file__).resolve().parents[1]
LEDGER=ROOT/"q2_scalar_frontier.json"
PARENT=ROOT/"physicalization_gates.json"

ALLOWED={
    "positive_control":{"tested_finite"},
    "physical":{"open_physical","frozen"},
}
REQUIRED_LOCAL={"Q2_LOCAL_SHAPE_1PI","Q2_COLLECTIVE_CONFORMAL_VOLUME_CARRIER"}
FROZEN_PHYSICAL={"PHYSICAL_CONSERVED_MATTER_SOURCE_COUPLING"}
OPEN_PHYSICAL={
    "PHYSICAL_VOLUME_HISTORY_SOURCE",
    "PHYSICAL_LAPSE_RESPONSE_SOURCE",
    "PHYSICAL_SCALAR_GAUGE_REDUCTION",
    "CONNECTED_SCALAR_INTERBLOCK_HISTORY",
    "PHYSICAL_BQG_SCALAR_KERNEL",
}
REQUIRED_PHYSICAL=OPEN_PHYSICAL|FROZEN_PHYSICAL
PARENT_MUST_REMAIN_OPEN={
    "CONNECTED_INTERBLOCK_HISTORY",
    "PHYSICAL_BACKGROUND_COSMOLOGY",
    "PHYSICAL_SCALAR_COSMOLOGY",
    "LENSING_DYNAMICS_CLOSURE",
}


def load(path:Path,errors:list[str])->dict:
    try:
        x=json.loads(path.read_text(encoding="utf-8"))
    except (OSError,json.JSONDecodeError) as exc:
        errors.append(f"{path.name}: {exc}"); return {}
    if not isinstance(x,dict): errors.append(f"{path.name}: root must be object"); return {}
    return x


def safe_path(s:str)->bool:
    p=PurePosixPath(s)
    return bool(s) and not p.is_absolute() and ".." not in p.parts


def main()->int:
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--output",type=Path); a=ap.parse_args()
    errors:list[str]=[]
    data=load(LEDGER,errors); parent=load(PARENT,errors)
    if data.get("schema_version") != 1: errors.append("q2 scalar schema_version must equal 1")
    if data.get("parent_physicalization_ledger") != "physicalization_gates.json": errors.append("parent ledger path mismatch")

    gates=data.get("gates",[])
    if not isinstance(gates,list): errors.append("gates must be list"); gates=[]
    rows={}
    for i,g in enumerate(gates):
        if not isinstance(g,dict): errors.append(f"gate[{i}] must be object"); continue
        gid=g.get("id"); role=g.get("closure_role"); status=g.get("status")
        if not isinstance(gid,str) or not gid: errors.append(f"gate[{i}] invalid id"); continue
        if gid in rows: errors.append(f"duplicate gate id {gid}"); continue
        rows[gid]=g
        if role not in ALLOWED: errors.append(f"{gid}: invalid role {role!r}")
        elif status not in ALLOWED[role]: errors.append(f"{gid}: illegal status {status!r} for {role}")
        for key in ("claim","hard_scope"):
            if not isinstance(g.get(key),str) or not g[key].strip(): errors.append(f"{gid}: missing {key}")
        evidence=g.get("evidence",[])
        if not isinstance(evidence,list) or not evidence: errors.append(f"{gid}: evidence must be nonempty list"); evidence=[]
        for rel in evidence:
            if not isinstance(rel,str) or not safe_path(rel): errors.append(f"{gid}: unsafe evidence {rel!r}")
            elif not (ROOT/rel).is_file(): errors.append(f"{gid}: missing evidence {rel}")

    if not REQUIRED_LOCAL <= set(rows): errors.append(f"missing local gates {sorted(REQUIRED_LOCAL-set(rows))}")
    if not REQUIRED_PHYSICAL <= set(rows): errors.append(f"missing physical gates {sorted(REQUIRED_PHYSICAL-set(rows))}")
    for gid in REQUIRED_LOCAL & set(rows):
        if rows[gid].get("status") != "tested_finite" or rows[gid].get("closure_role") != "positive_control":
            errors.append(f"{gid}: local result must remain tested_finite positive_control")
    for gid in OPEN_PHYSICAL & set(rows):
        if rows[gid].get("status") != "open_physical" or rows[gid].get("closure_role") != "physical":
            errors.append(f"{gid}: unresolved scalar physical gate must remain open_physical")
    for gid in FROZEN_PHYSICAL & set(rows):
        if rows[gid].get("status") != "frozen" or rows[gid].get("closure_role") != "physical":
            errors.append(f"{gid}: conserved external probe interface must be frozen physical")

    outputs=data.get("current_outputs",{})
    expected_open=("rho_hist_a","Phi_a_k","Psi_a_k","mu_BQG_a_k","Sigma_BQG_a_k")
    for key in expected_open:
        if outputs.get(key) != "OPEN_PHYSICAL": errors.append(f"{key}: must remain OPEN_PHYSICAL")
    if outputs.get("conserved_external_probe_interface") != "FROZEN_UNIVERSAL_CONVENTION":
        errors.append("conserved_external_probe_interface must equal FROZEN_UNIVERSAL_CONVENTION")
    if outputs.get("scalar_ADM_log_volume_seed_K_zetaV_zetaV") != "18_EXACT_KINEMATIC_POSITIVE_CONTROL":
        errors.append("exact scalar ADM zeta_V seed must remain recorded as 18 kinematic positive control")

    pgates=parent.get("gates",[]) if isinstance(parent.get("gates",[]),list) else []
    prows={g.get("id"):g for g in pgates if isinstance(g,dict) and isinstance(g.get("id"),str)}
    for gid in PARENT_MUST_REMAIN_OPEN:
        if prows.get(gid,{}).get("status") != "open_physical": errors.append(f"parent {gid} must remain open_physical")

    source_gate=rows.get("PHYSICAL_CONSERVED_MATTER_SOURCE_COUPLING",{})
    evidence=set(source_gate.get("evidence",[])) if isinstance(source_gate.get("evidence",[]),list) else set()
    required_source_evidence={"CONSERVED_SCALAR_PROBE_CONVENTION.md","scripts/conserved_scalar_probe_convention_gate.py"}
    if not required_source_evidence <= evidence:
        errors.append("frozen conserved probe gate missing dedicated evidence")
    if "realistic matter sector" not in source_gate.get("hard_scope",""):
        errors.append("frozen probe hard_scope must explicitly keep realistic matter sector un-derived")

    result={
        "schema_version":data.get("schema_version"),
        "valid":not errors,
        "gate_count":len(gates),
        "local_positive_controls":{gid:rows.get(gid,{}).get("status") for gid in sorted(REQUIRED_LOCAL)},
        "frozen_scalar_interfaces":{gid:rows.get(gid,{}).get("status") for gid in sorted(FROZEN_PHYSICAL)},
        "open_scalar_physical_gates":{gid:rows.get(gid,{}).get("status") for gid in sorted(OPEN_PHYSICAL)},
        "required_scalar_physical_gates":{gid:rows.get(gid,{}).get("status") for gid in sorted(REQUIRED_PHYSICAL)},
        "parent_open_guards":{gid:prows.get(gid,{}).get("status") for gid in sorted(PARENT_MUST_REMAIN_OPEN)},
        "cosmology_outputs":{key:outputs.get(key) for key in expected_open},
        "scientific_interpretation":"GREEN means the local q=2 shape/volume controls, exact ADM reduction machinery and universal conserved external test-probe convention are recorded without promoting them to physical scalar cosmology. The theory-specific volume-history, lapse/shift response, connected scalar history, physical Gamma_scalar, background cosmology and lensing closure remain open.",
        "errors":errors,
    }
    txt=json.dumps(result,indent=2); print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(txt+"\n",encoding="utf-8")
    return 0 if not errors else 1

if __name__=="__main__":
    raise SystemExit(main())
