#!/usr/bin/env python3
"""Fast single-triple logical return probe for the real sine-ordered Lorentzian stack.

Uses the cached machinery of peter_weyl_lorentzian_logical_projection_gate.py but
applies only one ordered triple (a,b,c)=the first three neighbors of source node
0 to the K=0 all-j=1/2 logical input.  This does not test the full epsilon sum;
it only asks whether one genuine K-K-V amplitude has any all-j=1/2 logical
return component at all.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_lorentzian_logical_projection_gate as LP


def run(source_v=0):
    restore, caches = LP.install_sine_cached_stack()
    try:
        spins = (1,) * len(PW.EDGES)
        Ks = (0,) * len(PW.VERT)
        initial = (spins, Ks)
        a, b, c = PW.NEIG[source_v][:3]
        total, diag = LP.ordered_triple_state(initial, source_v, a, b, c)
        logical = LP.project_all_logical(total, source_v)
        same = logical.get(initial, 0j)
        maxlog = sorted(logical.items(), key=lambda kv: abs(kv[1]), reverse=True)[:16]
        passed = (
            len(total) > 0
            and max(diag.values(), default=0.0) < 1e-8
        )
        return {
            "status": "single real sine-ordered Lorentzian logical-return probe",
            "passed": bool(passed),
            "source_node": source_v,
            "ordered_edges": [a, b, c],
            "full_output_support": len(total),
            "full_output_norm": math.sqrt(LP.norm2(total)),
            "all_jhalf_logical_support": len(logical),
            "all_jhalf_logical_norm": math.sqrt(LP.norm2(logical)),
            "same_input_logical_amplitude": [same.real, same.imag],
            "same_input_logical_abs": abs(same),
            "any_logical_return": bool(logical),
            "largest_logical_returns": [
                {"Ks2": list(key[1]), "amp": [amp.real, amp.imag], "abs_amp": abs(amp)}
                for key, amp in maxlog
            ],
            "max_diagnostics": diag,
            "scope": "One ordered K-K-V triple only; no epsilon sum, no final Hermitian H_L normalization and no physical mass/force claim.",
        }
    finally:
        restore()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    out = run()
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
