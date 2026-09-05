#!/usr/bin/env python3
"""Validate the fail-closed q=2 scalar-effective-action frontier.

A green result means the repository correctly distinguishes:
- exact local shape / collective-volume positive controls;
- exact flat/local scalar Ward quotient and Dirac reduction machinery;
- frozen universal conserved external TEST-PROBE convention;
- frozen deterministic connected-history -> scalar-response consumer pipeline;
- still-open theory-specific connected scalar history, physical scalar kernel,
  FLRW/background cosmology and lensing.

GREEN is deliberately not a claim that dark matter, dark energy, a realistic
matter sector or theory-specific Gamma_scalar^(2)(omega,k) has been derived.
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
FROZEN_PHYSICAL={
    "PHYSICAL_CONSERVED_MATTER_SOURCE_COUPLING",
    "SCALAR_CONNECTED_HISTORY_TO_RESPONSE_PIPELINE",
}
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
            errors.append(f"{gid}: frozen scalar physical interface/pipeline status mismatch")

    outputs=data.get("current_outputs",{})
    expected_open=("rho_hist_a","Phi_a_k","Psi_a_k","mu_BQG_a_k","Sigma_BQG_a_k")
    for key in expected_open:
        if outputs.get(key) != "OPEN_PHYSICAL": errors.append(f"{key}: must remain OPEN_PHYSICAL")
    if outputs.get("conserved_external_probe_interface") != "FROZEN_UNIVERSAL_CONVENTION":
        errors.append("conserved_external_probe_interface must equal FROZEN_UNIVERSAL_CONVENTION")
    if outputs.get("scalar_connected_history_consumer_pipeline") != "FROZEN_GCONN_TO_RESPONSE":
        errors.append("scalar connected-history consumer pipeline must be frozen")
    expected_inputs=["G_QQ(omega,k)","G_Qzeta(omega,k)","G_zetazeta(omega,k)"]
    if outputs.get("remaining_scalar_microscopic_inputs") != expected_inputs:
        errors.append("remaining scalar microscopic inputs must be exactly the three connected Ward cumulants")
    if outputs.get("scalar_ADM_log_volume_seed_K_zetaV_zetaV") != "18_EXACT_KINEMATIC_POSITIVE_CONTROL":
        errors.append("exact scalar ADM zeta_V seed must remain recorded as 18 kinematic positive control")
    if outputs.get("flat_scalar_Ward_parameter_count") != 3:
        errors.append("flat scalar Ward quotient must have exactly three kernel functions")
    if outputs.get("flat_scalar_Ward_quotient") != "EXACT_TWO_GAUGE_INVARIANTS_THREE_KERNEL_FUNCTIONS":
        errors.append("flat scalar Ward quotient status mismatch")

    pgates=parent.get("gates",[]) if isinstance(parent.get("gates",[]),list) else []
    prows={g.get("id"):g for g in pgates if isinstance(g,dict) and isinstance(g.get("id"),str)}
    for gid in PARENT_MUST_REMAIN_OPEN:
        if prows.get(gid,{}).get("status") != "open_physical": errors.append(f"parent {gid} must remain open_physical")

    source_gate=rows.get("PHYSICAL_CONSERVED_MATTER_SOURCE_COUPLING",{})
    evidence=set(source_gate.get("evidence",[])) if isinstance(source_gate.get("evidence",[]),list) else set()
    required_source_evidence={"CONSERVED_SCALAR_PROBE_CONVENTION.md","scripts/conserved_scalar_probe_convention_gate.py"}
    if not required_source_evidence <= evidence:
        errors.append("frozen conserved probe gate missing dedicated evidence")
    scope=source_gate.get("hard_scope","").lower()
    if "does not derive" not in scope or "matter sector" not in scope:
        errors.append("frozen probe hard_scope must explicitly say it does not derive a matter sector")
    if "common physical scale" not in scope:
        errors.append("frozen probe hard_scope must keep common physical scale calibration separate")

    gauge_gate=rows.get("PHYSICAL_SCALAR_GAUGE_REDUCTION",{})
    gevidence=set(gauge_gate.get("evidence",[])) if isinstance(gauge_gate.get("evidence",[]),list) else set()
    required_gauge_evidence={"SCALAR_ADM_DIRAC_REDUCTION.md","scripts/scalar_adm_dirac_response_gate.py","SCALAR_ADM_WARD_QUOTIENT.md","scripts/scalar_adm_ward_basis_gate.py"}
    if not required_gauge_evidence <= gevidence:
        errors.append("scalar gauge-reduction gate missing exact Dirac/Ward evidence")
    gscope=gauge_gate.get("hard_scope","").lower()
    if "flrw" not in gscope or "three functions" not in gauge_gate.get("claim","").lower():
        errors.append("scalar gauge-reduction boundary must separate exact flat three-function quotient from open FLRW reduction")

    pipe=rows.get("SCALAR_CONNECTED_HISTORY_TO_RESPONSE_PIPELINE",{})
    pevidence=set(pipe.get("evidence",[])) if isinstance(pipe.get("evidence",[]),list) else set()
    required_pipe_evidence={
        "CONNECTED_SCALAR_HISTORY_EXTRACTION.md",
        "SCALAR_WARD_KERNEL_RESPONSE.md",
        "scripts/scalar_connected_history_extractor_gate.py",
        "scripts/scalar_connected_history_to_response_gate.py",
        "scripts/scalar_ward_kernel_response_gate.py",
        ".github/workflows/scalar-connected-history-closure.yml",
    }
    if not required_pipe_evidence <= pevidence:
        errors.append("frozen connected-history consumer pipeline missing dedicated end-to-end evidence")
    pscope=pipe.get("hard_scope","").lower()
    for phrase in ("does not compute", "pseudoinverse", "physical omega", "synthetic"):
        if phrase not in pscope:
            errors.append(f"connected-history pipeline hard_scope missing boundary phrase: {phrase}")

    hist=rows.get("CONNECTED_SCALAR_INTERBLOCK_HISTORY",{})
    hclaim=hist.get("claim","")
    for token in ("G_QQ", "G_Qzeta", "G_zetazeta"):
        if token not in hclaim:
            errors.append(f"connected scalar history claim must name exact remaining cumulant {token}")

    result={
        "schema_version":data.get("schema_version"),
        "valid":not errors,
        "gate_count":len(gates),
        "local_positive_controls":{gid:rows.get(gid,{}).get("status") for gid in sorted(REQUIRED_LOCAL)},
        "exact_scalar_algebra":{
            "flat_Ward_parameter_count":outputs.get("flat_scalar_Ward_parameter_count"),
            "log_volume_seed":outputs.get("scalar_ADM_log_volume_seed_K_zetaV_zetaV"),
            "connected_history_consumer_pipeline":outputs.get("scalar_connected_history_consumer_pipeline"),
            "remaining_microscopic_inputs":outputs.get("remaining_scalar_microscopic_inputs"),
        },
        "frozen_scalar_interfaces":{gid:rows.get(gid,{}).get("status") for gid in sorted(FROZEN_PHYSICAL)},
        "open_scalar_physical_gates":{gid:rows.get(gid,{}).get("status") for gid in sorted(OPEN_PHYSICAL)},
        "required_scalar_physical_gates":{gid:rows.get(gid,{}).get("status") for gid in sorted(REQUIRED_PHYSICAL)},
        "parent_open_guards":{gid:prows.get(gid,{}).get("status") for gid in sorted(PARENT_MUST_REMAIN_OPEN)},
        "cosmology_outputs":{key:outputs.get(key) for key in expected_open},
        "scientific_interpretation":"GREEN means the scalar algebraic consumer chain is closed and frozen from three physical connected Ward cumulants through Legendre inversion, A/B/C, one-source Phi/Psi response and pole/stability classification. The three cumulants themselves, the theory-specific Gamma_scalar output, FLRW/background cosmology and lensing closure remain open physical calculations.",
        "errors":errors,
    }
    txt=json.dumps(result,indent=2); print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(txt+"\n",encoding="utf-8")
    return 0 if not errors else 1

if __name__=="__main__":
    raise SystemExit(main())
