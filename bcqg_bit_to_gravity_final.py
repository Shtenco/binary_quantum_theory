#!/usr/bin/env python3
"""Canonical binary quantum geometry -> continuum-GR bridge aggregator.

This executable separates finite/exact bridge results from stronger open claims.
A successful run means that the registered internal regression suite is
self-consistent on its declared domains.  It does not promote finite three-node
HDA, fixed-input cutoff control or exact kinematic q=2 carrier maps into an
arbitrary-graph theory of nature.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from bcqg_observer_smoothing_unified import run as run_bits
from bcqg_global_manifold_gate import run as run_manifold
from bcqg_quantum_hda_killer import run as run_hda

ROOT = Path(__file__).resolve().parent

REQUIRED_FIXED_CUTOFF_GATES = {
    "BITQ2": {"tested_finite", "proved"},
    "MAN3": {"tested_finite", "proved"},
    "MICRO_WALSH_TETRA": {"proved"},
    "MICRO_GLOBAL_GLUE": {"proved"},
    "Q2EIN": {"tested_finite", "proved"},
    "REGGEEH": {"tested_finite", "proved"},
    "PLEBANSKI": {"tested_finite", "proved"},
    "PWGEO": {"tested_finite", "proved"},
    "ROUTE": {"tested_finite", "proved"},
    "E2NODE": {"tested_finite", "proved"},
    "HDA_3NODE": {"tested_finite", "proved"},
    "LORENTZ": {"tested_finite", "proved"},
    "LHDA_COMP": {"proved"},
    "JOINT_FIXED_INPUT": {"tested_finite", "proved", "conditional"},
    "DEWITT": {"proved"},
    "CORECERT": {"conditional", "tested_finite", "proved"},
}


def run():
    bits = run_bits()
    manifold = run_manifold(refinements=2)
    hda = run_hda()
    ledger = json.loads((ROOT / "theory_gates.json").read_text(encoding="utf-8"))
    gates = {g["id"]: g for g in ledger["gates"]}

    bits_pass = bool(bits.get("candidate_all_passed", bits.get("all_passed", False)))
    manifold_pass = bool(manifold.get("passed", False))
    hda_prereq_pass = bool(hda.get("regression_passed", False))
    route_hda_pass = bool(hda.get("route_sector_HDA_principal_symbol_closed", False))

    ledger_required = {}
    for gate_id, accepted in REQUIRED_FIXED_CUTOFF_GATES.items():
        status = gates.get(gate_id, {}).get("status")
        ledger_required[gate_id] = {"status": status, "accepted": bool(status in accepted)}

    ledger_pass = all(item["accepted"] for item in ledger_required.values())
    registered_bridge_passed = bool(
        bits_pass and manifold_pass and hda_prereq_pass and route_hda_pass and ledger_pass
    )

    open_frontiers = [
        {"id": g["id"], "claim": g["claim"]}
        for g in ledger["gates"]
        if g.get("status") == "open"
    ]

    return {
        "status": "registered binary quantum geometry -> continuum-GR integration regression",
        "fixed_cutoff_bridge_passed": registered_bridge_passed,
        "core_candidate_architecture_closed": registered_bridge_passed,
        "candidate_framework": True,
        "experimentally_confirmed_theory_of_nature": False,
        "local_q2_geometry_carrier_exact": gates.get("MICRO_WALSH_TETRA", {}).get("status") == "proved",
        "selected_PL_q2_global_carrier_gluing_exact": gates.get("MICRO_GLOBAL_GLUE", {}).get("status") == "proved",
        "three_node_graph_changing_HDA_tested_finite": gates.get("HDA_3NODE", {}).get("status") in {"tested_finite", "proved"},
        "fixed_input_joint_cutoff_limit_controlled": gates.get("JOINT_FIXED_INPUT", {}).get("status") in {"tested_finite", "proved", "conditional"},
        "full_graph_changing_multi_node_quantum_HDA_closed": False,
        "uniform_unbounded_refinement_joint_limit_theorem": False,
        "blind_external_physical_prediction_completed": False,
        "runtime_chain": {
            "binary_route_geometrogenesis": bits_pass,
            "recursive_selected_PL_3manifold": manifold_pass,
            "HDA_prerequisites_and_factorization_no_go": hda_prereq_pass,
            "route_sector_HDA_principal_symbol": route_hda_pass,
        },
        "registered_bridge_gates": ledger_required,
        "open_research_frontiers": open_frontiers,
        "euclidean_three_node_HH_safe_Jmax_for_all_j_half": 2.5,
        "safe_full_Lorentzian_HH_Jmax_for_all_j_half": 6.5,
        "fixed_cutoff_composition_bound": "Delta_full <= Delta_route + C_cross*epsilon + C_GG*epsilon^2",
        "canonical_status": "THEORY_STATUS.md",
        "scope": (
            "A passing result certifies the declared exact/finite bridge subresults only. "
            "It does not prove dynamical microscopic selection of the full Peter-Weyl phase, arbitrary-graph Lorentzian HDA closure, "
            "uniform refinement with growing collective spin, physical scale setting or experimental validity."
        ),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path)
    ap.add_argument("--strict", action="store_true", help="fail unless the registered integration regression passes")
    args = ap.parse_args()
    out = run()
    text = json.dumps(out, indent=2, ensure_ascii=False)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    if args.strict and not out["fixed_cutoff_bridge_passed"]:
        return 2
    return 0 if out["fixed_cutoff_bridge_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
