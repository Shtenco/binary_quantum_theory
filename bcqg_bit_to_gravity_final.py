#!/usr/bin/env python3
"""Canonical fixed-cutoff bit -> spacetime -> gravity architecture aggregator.

This file is the executable status surface for the post-certificate repository.
It does not reopen frozen research arrows and it does not claim experimental
confirmation of nature.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from bcqg_observer_smoothing_unified import run as run_bits
from bcqg_global_manifold_gate import run as run_manifold
from bcqg_quantum_hda_killer import run as run_hda

ROOT = Path(__file__).resolve().parent


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
    lorentzian_composition_proved = gates.get("LHDA_COMP", {}).get("status") == "proved"
    open_core = [g["id"] for g in ledger["gates"] if g.get("status") == "open"]

    closed = bool(
        bits_pass
        and manifold_pass
        and hda_prereq_pass
        and route_hda_pass
        and lorentzian_composition_proved
        and not open_core
    )

    return {
        "status": "canonical fixed-cutoff core candidate architecture certificate",
        "core_candidate_architecture_closed": closed,
        "experimentally_confirmed_theory_of_nature": False,
        "uniform_joint_Jmax_infinity_epsilon_zero_theorem": False,
        "direct_11M_state_Lorentzian_HH_matrix_required_for_logic": False,
        "direct_11M_state_Lorentzian_HH_matrix_completed": False,
        "chain": {
            "binary_route_geometrogenesis": bits_pass,
            "recursive_global_PL_3manifold": manifold_pass,
            "HDA_prerequisites_and_factorization_no_go": hda_prereq_pass,
            "route_sector_HDA_principal_symbol": route_hda_pass,
            "fixed_cutoff_Lorentzian_route_composition_theorem": lorentzian_composition_proved,
        },
        "open_core_gate_ids": open_core,
        "safe_full_Lorentzian_HH_Jmax_for_all_j_half": 6.5,
        "full_HDA_bound": "Delta_full <= Delta_route + C_cross*epsilon + C_GG*epsilon^2 -> 0",
        "canonical_certificate": "FINAL_CORE_ARCHITECTURE_CERTIFICATE.md",
        "scope": (
            "Mathematical/computational candidate closure at fixed regulator-safe Peter-Weyl cutoff. "
            "Uniform simultaneous Jmax->infinity control, microscopic uniqueness, quantum measure, "
            "matter and empirical validation remain separate research questions."
        ),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path)
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()
    out = run()
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    if args.strict and not out["core_candidate_architecture_closed"]:
        return 2
    return 0 if out["core_candidate_architecture_closed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
