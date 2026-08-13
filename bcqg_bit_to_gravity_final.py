#!/usr/bin/env python3
"""Final non-circular aggregator for the current bit -> spacetime -> gravity chain.

This file does not invent a new calculation. It composes three independently
executable gates:
  1. frozen binary-route geometrogenesis / observer smoothing;
  2. canonical q=2 global PL-manifold completion;
  3. off-shell quantum-HDA structural killer.

A successful repository regression is distinct from a successful theory. The
full theory is marked closed only when the route-coupled Lorentzian HDA gate is
actually nontrivially satisfied.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path

from bcqg_observer_smoothing_unified import run as run_bits
from bcqg_global_manifold_gate import run as run_manifold
from bcqg_quantum_hda_killer import run as run_hda


def run():
    bits=run_bits();man=run_manifold(refinements=2);hda=run_hda()
    bits_pass=bool(bits.get("all_passed",False))
    man_pass=bool(man.get("passed",False))
    hda_reg=bool(hda.get("regression_passed",False))
    hda_closed=bool(hda.get("full_quantum_HDA_closed",False))
    return {
      "status":"bit-to-gravity final aggregator",
      "repository_regression_passed":bool(bits_pass and man_pass and hda_reg),
      "full_bit_to_GR_closed":bool(bits_pass and man_pass and hda_closed),
      "chain":{
        "binary_route_geometrogenesis":bits_pass,
        "canonical_global_PL_3manifold_completion":man_pass,
        "off_shell_HDA_prerequisites_and_no_go_diagnostic":hda_reg,
        "route_coupled_Lorentzian_quantum_HDA":hda_closed
      },
      "central_equation":"G_binary_Planck --C_b(r)--> G_eff(r)",
      "current_frontier":"bits -> q=2 -> local S2 shell -> canonical global S3 PL completion -> 3D scaling -> z~1 -> smooth IR; full GR stops at the missing route-coupled Lorentzian Hamiltonian.",
      "why_not_closed":"The current geometry-only Peter-Weyl Hamiltonian factorises with I_path and is therefore structurally unable to reproduce a nonzero D_path RHS off shell.",
      "next_single_operator_task":"Implement gauge-covariant controlled rerouting inside H_E+H_L itself, then run the preregistered densitized HH-D residual without coefficient tuning.",
      "scope":"A green regression certifies internal consistency of the candidate chain, not experimental confirmation of quantum gravity."
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--output",type=Path);ap.add_argument("--strict",action="store_true");a=ap.parse_args()
    out=run();txt=json.dumps(out,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+"\n",encoding="utf-8")
    if a.strict:return 0 if out["full_bit_to_GR_closed"] else 2
    return 0 if out["repository_regression_passed"] else 1


if __name__=="__main__":raise SystemExit(main())
