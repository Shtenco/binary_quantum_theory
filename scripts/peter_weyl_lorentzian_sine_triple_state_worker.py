#!/usr/bin/env python3
"""Capture one genuine sine-ordered Peter-Weyl Lorentzian triple as a sparse state.

The existing `peter_weyl_lorentzian_sine_ordered_triple_gate.py` already
computes

    T_abc = Tr_aux[C_a(K_sine) C_b(K_sine) C_c(V)]

at the preregistered safe single-H_L wall Jmax=7/2.  Its public JSON reports
norms and diagnostics but not the complete sparse output state.  This worker
wraps that existing implementation without changing its physics and captures
the exact pruned sparse state accumulated by the raw ordered-triple gate.

It is intended for a two-job orientation-reversal test: abc versus bac.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import peter_weyl_lorentzian_ordered_triple_gate as RAW
import peter_weyl_lorentzian_sine_ordered_triple_gate as SINE


def state_norm2(state: dict) -> float:
    return float(sum(abs(z) ** 2 for z in state.values()))


def capture(v: int, a: int, b: int, c: int):
    old_add = RAW.add
    box: dict = {}
    add_calls = 0

    def hooked_add(dst, src, scale=1.0, tol=RAW.TOL):
        nonlocal add_calls
        old_add(dst, src, scale, tol)
        add_calls += 1
        # RAW.run uses its module-level add() to accumulate only the final
        # ordered-triple state.  Keep a copy after every accumulation so the
        # last copy is the exact final sparse state returned implicitly by the
        # existing implementation.
        box.clear()
        box.update(dst)

    RAW.add = hooked_add
    try:
        meta = SINE.run(v, a, b, c)
    finally:
        RAW.add = old_add

    return meta, box, add_calls


def serialize_state(state: dict) -> list[dict[str, object]]:
    rows = []
    for key, amp in sorted(state.items(), key=lambda kv: repr(kv[0])):
        z = complex(amp)
        rows.append({
            "key": repr(key),
            "amp": [float(z.real), float(z.imag)],
            "abs_amp": float(abs(z)),
        })
    return rows


def state_digest(rows: list[dict[str, object]]) -> str:
    payload = json.dumps(rows, separators=(",", ":"), sort_keys=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def run(v: int, a: int, b: int, c: int, label: str) -> dict[str, object]:
    meta, state, add_calls = capture(v, a, b, c)
    rows = serialize_state(state)
    support_matches = int(meta.get("output_support", -1)) == len(rows)
    norm2 = state_norm2(state)
    reported_norm = float(meta.get("output_norm", 0.0))
    norm_matches = abs(norm2 ** 0.5 - reported_norm) <= 2e-9 * max(1.0, reported_norm)

    passed = bool(meta.get("passed", False) and support_matches and norm_matches and len(rows) > 0)
    return {
        "status": "captured genuine sine-ordered Peter-Weyl Lorentzian triple sparse state",
        "passed": passed,
        "label": label,
        "source_node": v,
        "ordered_edges": [a, b, c],
        "definition": "Tr_aux[C_a(K_sine) C_b(K_sine) C_c(V)]",
        "Jmax": 3.5,
        "capture_add_calls": add_calls,
        "captured_support": len(rows),
        "captured_norm": norm2 ** 0.5,
        "reported_support": meta.get("output_support"),
        "reported_norm": reported_norm,
        "support_matches_existing_gate": support_matches,
        "norm_matches_existing_gate": norm_matches,
        "state_sha256": state_digest(rows),
        "state": rows,
        "existing_gate_metadata": meta,
        "claim_boundary": (
            "This is one genuine safe ordered K_sine-K_sine-V Peter-Weyl amplitude. "
            "It is not the full epsilon-oriented Lorentzian node Hamiltonian, not a physical history kernel, and not g_YC^gravity."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--v", type=int, default=0)
    ap.add_argument("--a", type=int, required=True)
    ap.add_argument("--b", type=int, required=True)
    ap.add_argument("--c", type=int, required=True)
    ap.add_argument("--label", required=True)
    ap.add_argument("--output", type=Path, required=True)
    x = ap.parse_args()
    out = run(x.v, x.a, x.b, x.c, x.label)
    text = json.dumps(out, indent=2)
    print(text)
    x.output.parent.mkdir(parents=True, exist_ok=True)
    x.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
