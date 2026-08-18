#!/usr/bin/env python3
"""Exact cubic-symmetry extraction of eta2 and zeta4 from TT quartic poles.

Input is three dimensionless quartic directional coefficients e100, e110, e111
from a frozen TT pole expansion

  omega^2 = c_T^2 k^2 + c_T^2 a_*^2 k^4 e(n) + O(k^6).

For Q_cub(n)=sum_i n_i^4-3/5,
  e(n)=eta2+zeta4 Q_cub(n).

The first two directions determine eta2,zeta4.  The third is an independent
consistency residual; it is not used to add another fit parameter.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def extract(e100: float, e110: float, e111: float) -> dict[str, float | bool | str]:
    zeta_100_110 = 2.0 * (e100 - e110)
    eta_100_110 = 0.2 * e100 + 0.8 * e110
    zeta_110_111 = 6.0 * (e110 - e111)
    identity = e100 - 4.0 * e110 + 3.0 * e111
    scale = max(abs(e100), abs(e110), abs(e111), 1.0e-30)
    rel_identity = abs(identity) / scale
    return {
        "status": "exact S4/cubic TT quartic Wilson extraction",
        "eta2_iso": eta_100_110,
        "zeta4_cub_from_100_110": zeta_100_110,
        "zeta4_cub_from_110_111": zeta_110_111,
        "three_direction_identity": identity,
        "three_direction_identity_relative": rel_identity,
        "identity_expected": "e100 - 4*e110 + 3*e111 = 0",
        "passed_default_consistency": rel_identity < 1.0e-8,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--e100", type=float, required=True)
    ap.add_argument("--e110", type=float, required=True)
    ap.add_argument("--e111", type=float, required=True)
    ap.add_argument("--output", type=Path)
    ap.add_argument("--tol", type=float, default=1.0e-8)
    args = ap.parse_args()
    out = extract(args.e100, args.e110, args.e111)
    out["passed_requested_tolerance"] = out["three_direction_identity_relative"] < args.tol
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed_requested_tolerance"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
