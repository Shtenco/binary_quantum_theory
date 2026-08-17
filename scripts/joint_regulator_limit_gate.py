#!/usr/bin/env python3
"""Joint regulator/cutoff gate for the finite HH habitat family.

For a finite word of fundamental holonomies, Peter-Weyl truncation is exactly
inactive once Jmax exceeds the input spin plus one half of the maximum number
of hits accumulated on a link.  This script combines that support theorem with
the measured epsilon scaling from the three-node graph-changing HDA gate.

It therefore tests a genuine simultaneous limit for the declared fixed-input
local HH family:

    epsilon -> 0,
    Jmax(epsilon) >= J_safe.

Above J_safe the cutoff error is exactly zero for this finite word, so every
admissible Jmax(epsilon) path has the same epsilon limit.  The statement does
not yet cover an arbitrary refinement family whose input/coarse spins grow
without a separately controlled Jmax(b) schedule.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from collections import Counter
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import lorentzian_hit_depth_bound as WALL


def max_euclidean_hh_hits() -> tuple[int, tuple[int, int, tuple[int, int]]]:
    profiles = {v: WALL.euclidean_profiles(v) for v in WALL.VERTICES}
    node_max = {}
    for v in WALL.VERTICES:
        node_max[v] = {
            e: max(p.get(e, 0) for _, p in profiles[v])
            for e in WALL.EDGES
        }
    best = -1
    witness = None
    for v, w in itertools.combinations(WALL.VERTICES, 2):
        for e in WALL.EDGES:
            hits = node_max[v][e] + node_max[w][e]
            if hits > best:
                best = hits
                witness = (v, w, e)
    return best, witness


def load_multi(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if "rows" not in data:
        raise ValueError("multi-node JSON has no rows")
    return data


def run(multi: dict) -> dict[str, object]:
    eps = np.asarray([r["epsilon"] for r in multi["rows"]], float)
    joint = np.asarray([r["joint_defect_over_D"] for r in multi["rows"]], float)
    if np.any(eps <= 0) or np.any(joint <= 0):
        raise ValueError("epsilon and joint defects must be positive")
    p_joint = float(np.polyfit(np.log(eps), np.log(joint), 1)[0])

    max_he_hh_hits, witness = max_euclidean_hh_hits()
    input_spin = 0.5
    safe_euclidean_jmax = input_spin + max_he_hh_hits / 2.0

    lor = WALL.run()
    safe_lorentzian_jmax = float(lor["sufficient_Jmax_for_full_Lorentzian_HH"])

    # A representative simultaneous schedule.  Because the support theorem is
    # exact above the wall, choosing a larger or epsilon-dependent Jmax does not
    # alter the finite-word amplitudes on this fixed input family.
    schedule = []
    for e, d in zip(eps, joint):
        schedule.append({
            "epsilon": float(e),
            "euclidean_Jmax": safe_euclidean_jmax,
            "lorentzian_support_safe_Jmax": safe_lorentzian_jmax,
            "Peter_Weyl_truncation_error_bound_above_wall": 0.0,
            "measured_euclidean_joint_defect": float(d),
        })

    checks = {
        "three_node_input_gate_passed": bool(multi.get("passed", False)),
        "euclidean_HH_max_hits_is_4": max_he_hh_hits == 4,
        "euclidean_safe_Jmax_is_2p5": abs(safe_euclidean_jmax - 2.5) < 1e-12,
        "lorentzian_support_wall_passed": bool(lor.get("passed", False)),
        "lorentzian_safe_Jmax_is_6p5": abs(safe_lorentzian_jmax - 6.5) < 1e-12,
        "joint_defect_has_positive_power": p_joint > 0.60,
        "joint_defect_decreases_monotonically": bool(np.all(np.diff(joint) < 0)),
        "smallest_regulator_defect_below_5pct": float(joint[-1]) < 0.05,
    }

    return {
        "status": "joint epsilon/Peter-Weyl limit for the declared fixed-input finite-HH habitat family",
        "passed": bool(all(checks.values())),
        "input_spin": input_spin,
        "euclidean_HH_max_hits_per_link": max_he_hh_hits,
        "euclidean_hit_witness": {"nodes": list(witness[:2]), "edge": list(witness[2])},
        "euclidean_sufficient_Jmax": safe_euclidean_jmax,
        "lorentzian_sufficient_Jmax_support_bound": safe_lorentzian_jmax,
        "measured_joint_regulator_exponent": p_joint,
        "schedule": schedule,
        "checks": checks,
        "theorem": (
            "For any finite fundamental-holonomy word with r hits on a link and input spin j_in, amplitudes are cutoff-exact whenever Jmax >= j_in+r/2. "
            "Hence for this fixed-input HH family, every simultaneous path with Jmax(epsilon) above the stated wall has zero truncation error and the measured epsilon limit is path-independent."
        ),
        "claim_boundary": (
            "This removes the joint-limit ambiguity for the declared local fixed-input HH family. "
            "A uniform theorem for refinement sequences with unbounded collective input spin still requires a controlled growth law Jmax(b) >= j_in(b)+r/2 and remains outside this PASS."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--multi-node-json", type=Path, required=True)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    out = run(load_multi(args.multi_node_json))
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
