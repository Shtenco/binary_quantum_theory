#!/usr/bin/env python3
"""Final non-circular aggregator for the current bit -> spacetime -> gravity chain.

This file invents no new physics. It composes three independently executable
gates and keeps repository-regression success separate from full-GR closure.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path

from bcqg_observer_smoothing_unified import run as run_bits
from bcqg_global_manifold_gate import run as run_manifold
from bcqg_quantum_hda_killer import run as run_hda


def run():
    bits=run_bits();man=run_manifold(refinements=2);hda=run_hda()
    # v2 frozen-rule master deliberately uses candidate_all_passed. The
    # fallback keeps compatibility with the superseded v1 schema without ever
    # converting an absent field into a positive result.
    bits_pass=bool(bits.get("candidate_all_passed",bits.get("all_passed",False)))
    man_pass=bool(man.get("passed",False))
    hda_reg=bool(hda.get("regression_passed",False))
    path_hda=bool(hda.get("route_sector_HDA_principal_symbol_closed",False))
    hda_closed=bool(hda.get("full_quantum_HDA_closed",False))
    return {
      "status":"bit-to-gravity final aggregator",
      "repository_regression_passed":bool(bits_pass and man_pass and hda_reg and path_hda),
      "full_bit_to_GR_closed":bool(bits_pass and man_pass and hda_closed),
      "chain":{
        "binary_route_geometrogenesis":bits_pass,
        "canonical_global_PL_3manifold_completion":man_pass,
        "HDA_prerequisites_and_factorization_no_go":hda_reg,
        "route_sector_HDA_principal_symbol":path_hda,
        "route_coupled_Lorentzian_quantum_HDA":hda_closed
      },
      "central_equation":"G_binary_Planck --C_b(r)--> G_eff(r)",
      "current_frontier":"bits -> q=2 -> local S2 shell -> canonical global S3 PL completion -> 3D scaling -> z~1 -> smooth IR -> route-sector HDA; full GR stops at coupling the Lorentzian Peter-Weyl geometry Hamiltonian to the same route-normal domain.",
      "why_not_closed":"The old geometry-only Hamiltonian is exactly ruled out by the path-channel no-go. The square-root route-normal factor has the correct HDA principal symbol, but the joint H_geom+route commutator has not yet been evaluated.",
      "next_single_operator_task":"Construct H_geom+route[N] with gauge-covariant controlled rerouting / square-root path-normal action inside the full H_E+H_L move, then run the frozen densitized HH-D residual without coefficient tuning.",
      "scope":"A green regression certifies internal consistency of the candidate chain, not experimental confirmation of quantum gravity."
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--output",type=Path);ap.add_argument("--strict",action="store_true");a=ap.parse_args()
    out=run();txt=json.dumps(out,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+"\n",encoding="utf-8")
    if a.strict:return 0 if out["full_bit_to_GR_closed"] else 2
    return 0 if out["repository_regression_passed"] else 1

if __name__=="__main__":raise SystemExit(main())
