#!/usr/bin/env python3
"""Validate the fail-closed q=2 scalar-effective-action frontier.

A green result means the repository correctly distinguishes the exact local
shape/collective-volume positive controls from the still-open physical scalar
history, gauge reduction, conserved matter-source response, background
cosmology and lensing problem. It is deliberately not a claim that dark
matter or dark energy has been derived.
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
REQUIRED_PHYSICAL={
    "PHYSICAL_VOLUME_HISTORY_SOURCE",
    "PHYSICAL_LAPSE_RESPONSE_SOURCE",
    "PHYSICAL_SCALAR_GAUGE_REDUCTION",
    "PHYSICAL_CONSERVED_MATTER_SOURCE_COUPLING",
    "CONNECTED_SCALAR_INTERBLOCK_HISTORY",
    "PHYSICAL_BQG_SCALAR_KERNEL",
}
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
    for gid in REQUIRED_PHYSICAL & set(rows):
        if rows[gid].get("status") != "open_physical" or rows[gid].get("closure_role") != "physical":
            errors.append(f"{gid}: physical scalar frontier must remain open_physical")

    outputs=data.get("current_outputs",{})
    expected_open=("rho_hist_a","Phi_a_k","Psi_a_k","mu_BQG_a_k","Sigma_BQG_a_k")
    for key in expected_open:
        if outputs.get(key) != "OPEN_PHYSICAL": errors.append(f"{key}: must remain OPEN_PHYSICAL")

    pgates=parent.get("gates",[]) if isinstance(parent.get("gates",[]),list) else []
    prows={g.get("id"):g for g in pgates if isinstance(g,dict) and isinstance(g.get("id"),str)}
    for gid in PARENT_MUST_REMAIN_OPEN:
        if prows.get(gid,{}).get("status") != "open_physical": errors.append(f"parent {gid} must remain open_physical")

    result={
        "schema_version":data.get("schema_version"),
        "valid":not errors,
        "gate_count":len(gates),
        "local_positive_controls":{gid:rows.get(gid,{}).get("status") for gid in sorted(REQUIRED_LOCAL)},
        "required_scalar_physical_gates":{gid:rows.get(gid,{}).get("status") for gid in sorted(REQUIRED_PHYSICAL)},
        "parent_open_guards":{gid:prows.get(gid,{}).get("status") for gid in sorted(PARENT_MUST_REMAIN_OPEN)},
        "cosmology_outputs":{key:outputs.get(key) for key in expected_open},
        "scientific_interpretation":"GREEN means the exact local q=2 shape 1PI and collective volume carrier are recorded without promoting them to physical cosmology. The physical volume-history, lapse-response, scalar gauge reduction, conserved matter-source coupling, connected interblock scalar history, BQG scalar kernel, background cosmology and lensing closure remain open.",
        "errors":errors,
    }
    txt=json.dumps(result,indent=2); print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(txt+"\n",encoding="utf-8")
    return 0 if not errors else 1

if __name__=="__main__":
    raise SystemExit(main())
