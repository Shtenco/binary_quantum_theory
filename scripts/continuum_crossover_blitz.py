#!/usr/bin/env python3
"""Estimate when the sine lattice looks smooth at a requested tolerance."""

from __future__ import annotations

import argparse
import json
import math


def dispersion_error(cells_per_wavelength: int) -> float:
    k = 2.0 * math.pi / cells_per_wavelength
    return abs(4.0 * math.sin(k / 2.0) ** 2 / k ** 2 - 1.0)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tolerance", type=float, default=0.01)
    parser.add_argument("--dimension", type=int, default=4)
    args = parser.parse_args()
    if not 0.0 < args.tolerance < 1.0 or args.dimension < 1:
        parser.error("require 0 < tolerance < 1 and dimension >= 1")
    cells = 3
    while dispersion_error(cells) > args.tolerance:
        cells += 1
    # Independent-bit benchmark only; correlations must be measured separately.
    block_side = math.ceil(args.tolerance ** (-2.0 / args.dimension))
    result = {
        "tolerance": args.tolerance,
        "minimum_cells_per_wavelength": cells,
        "exact_sine_dispersion_error": dispersion_error(cells),
        "previous_cell_count_error": dispersion_error(cells - 1),
        "independent_bit_block_side": block_side,
        "independent_bit_relative_fluctuation": block_side ** (-args.dimension / 2.0),
        "interpretation": "kinematic crossover estimate, not proof of GR",
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
