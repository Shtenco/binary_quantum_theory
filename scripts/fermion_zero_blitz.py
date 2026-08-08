#!/usr/bin/env python3
"""Count exact Brillouin-corner zeros of naive and Wilson lattice fermions."""

from __future__ import annotations

import argparse
import itertools
import json
import math


def count_zeros(dimension: int, wilson_r: float) -> dict[str, object]:
    corners = list(itertools.product((0.0, math.pi), repeat=dimension))
    naive = [k for k in corners if all(abs(math.sin(x)) < 1e-12 for x in k)]
    wilson = [
        k for k in corners
        if sum(math.sin(x) ** 2 for x in k) < 1e-24
        and abs(wilson_r * sum(1.0 - math.cos(x) for x in k)) < 1e-12
    ]
    return {
        "dimension": dimension,
        "brillouin_corners": len(corners),
        "naive_zero_count": len(naive),
        "expected_naive_zero_count": 2 ** dimension,
        "wilson_zero_count": len(wilson),
        "naive_doublers": len(naive) - 1,
        "wilson_removes_corner_doublers": len(wilson) == 1,
        "wilson_tradeoff": "removes doublers but breaks naive chiral symmetry at finite spacing",
        "matter_gate_closed": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dimension", type=int, default=4)
    parser.add_argument("--wilson-r", type=float, default=1.0)
    args = parser.parse_args()
    if args.dimension < 1 or args.wilson_r == 0.0 or not math.isfinite(args.wilson_r):
        parser.error("require dimension >= 1 and finite nonzero Wilson r")
    result = count_zeros(args.dimension, args.wilson_r)
    result["passed"] = (
        result["naive_zero_count"] == result["expected_naive_zero_count"]
        and result["wilson_zero_count"] == 1
    )
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
