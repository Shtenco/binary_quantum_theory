#!/usr/bin/env python3
"""Serialization-safe runner for peter_weyl_history_orientation_current_gate.

No physics, thresholds, operators or classifications are modified here.  This
wrapper only converts NumPy scalar objects in the already-computed result to
plain Python scalars before JSON serialization so scientific failures remain
visible as `passed=false` rather than being masked by a TypeError.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

import peter_weyl_history_orientation_current_gate as GATE


def plain(x):
    if isinstance(x, dict):
        return {str(k): plain(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [plain(v) for v in x]
    if isinstance(x, np.generic):
        return x.item()
    return x


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source-node", type=int, default=0)
    ap.add_argument("--output", type=Path, required=True)
    a = ap.parse_args()
    out = plain(GATE.run(a.source_node))
    text = json.dumps(out, indent=2)
    print(text)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out.get("passed") is True else 1


if __name__ == "__main__":
    raise SystemExit(main())
