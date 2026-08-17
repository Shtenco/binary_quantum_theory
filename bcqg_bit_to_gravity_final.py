#!/usr/bin/env python3
"""Canonical fixed-cutoff binary quantum geometry -> continuum-GR bridge aggregator.

This executable deliberately separates two questions:

1. Does the declared finite/fixed-cutoff mathematical bridge reproduce its
   registered internal gates?
2. Has full graph-changing, regulator-independent quantum general relativity
   been proved and experimentally validated?

Only the first can currently pass.  Open research gates remain visible in the
machine ledger and are not silently promoted by a successful regression run.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from bcqg_observer_smoothing_unified import run as run_bits
from bcqg_global_manifold_gate import run as run_manifold
from bcqg_quantum_hda_killer import run as run_hda

ROOT = Path(__file__).resolve().parent

# These gates define the fixed-cutoff integration regression.  They are not a
# definition of a complete theory of nature.
REQUIRED_FIXED_CUTOFF_GATES = {
    "BITQ2": {"tested_finite", "proved"},
    "MAN3": {"tested_finite", "proved"},
    "Q2EIN": {"tested_finite", "proved"},
    "REGGEEH": {"tested_finite", "proved"},
    "PLEBANSKI": {"tested_finite", "proved"},
    "PWGEO": {"tested_finite", "proved"},
    "ROUTE": {"tested_finite", "proved"},
    "E2NODE": {"tested_finite", "proved"},
    "LORENTZ": {"tested_finite", "proved"},
    "LHDA_COMP": {"proved"},
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
        ledger_required[gate_id] = {
            "status": status,
            "accepted": bool(status in accepted),
        }

    ledger_pass = all(item["accepted"] for item in ledger_required.values())
    fixed_cutoff_bridge_passed = bool(
        bits_pass
        and manifold_pass
        and hda_prereq_pass
        and route_hda_pass
        and ledger_pass
    )

    open_frontiers = [
        {
            "id": g["id"],
            "claim": g["claim"],
        }
        for g in ledger["gates"]
        if g.get("status") == "open"
    ]

    return {
        "status": "fixed-cutoff binary quantum geometry -> continuum-GR integration regression",
        "fixed_cutoff_bridge_passed": fixed_cutoff_bridge_passed,
        # Backward-compatible key used by older automation.  Its meaning is now
        # explicitly limited to the fixed-cutoff candidate bridge.
        "core_candidate_architecture_closed": fixed_cutoff_bridge_passed,
        "candidate_framework": True,
        "experimentally_confirmed_theory_of_nature": False,
        "full_graph_changing_multi_node_quantum_HDA_closed": False,
        "uniform_joint_regulator_removal_theorem": False,
        "blind_external_physical_prediction_completed": False,
        "runtime_chain": {
            "binary_route_geometrogenesis": bits_pass,
            "recursive_selected_PL_3manifold": manifold_pass,
            "HDA_prerequisites_and_factorization_no_go": hda_prereq_pass,
            "route_sector_HDA_principal_symbol": route_hda_pass,
        },
        "registered_fixed_cutoff_gates": ledger_required,
        "open_research_frontiers": open_frontiers,
        "safe_full_Lorentzian_HH_Jmax_for_all_j_half": 6.5,
        "fixed_cutoff_composition_bound": (
            "Delta_full <= Delta_route + C_cross*epsilon + C_GG*epsilon^2"
        ),
        "canonical_status": "THEORY_STATUS.md",
        "scope": (
            "A passing result certifies internal regression of the declared finite/fixed-cutoff bridge only. "
            "It does not prove microscopic uniqueness, full graph-changing multi-node HDA closure, "
            "uniform regulator removal, physical scale setting or experimental validity."
        ),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path)
    ap.add_argument(
        "--strict",
        action="store_true",
        help="fail unless the declared fixed-cutoff integration regression passes",
    )
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
