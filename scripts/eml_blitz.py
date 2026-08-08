#!/usr/bin/env python3
"""Blitz estimate for the project-local Edge--Message--Law primitive."""

from __future__ import annotations

import argparse
import json
import math


def width(cardinality: int) -> int:
    """Bits required for one value from a finite alphabet."""
    if cardinality < 1:
        raise ValueError("cardinality must be positive")
    return 0 if cardinality == 1 else math.ceil(math.log2(cardinality))


def estimate(vertices: int, degree: int, messages: int, laws: int,
             phase_bits: int) -> dict[str, int | float | bool]:
    if vertices < 2 or degree < 1 or degree >= vertices:
        raise ValueError("require vertices >= 2 and 1 <= degree < vertices")
    if vertices * degree % 2:
        raise ValueError("vertices * degree must be even for a regular graph")
    if phase_bits < 0:
        raise ValueError("phase_bits must be non-negative")

    edges = vertices * degree // 2
    endpoint_bits = width(vertices)
    state_bits = width(messages) + width(laws) + phase_bits
    primitive_bits = 2 * endpoint_bits + state_bits
    eml_bits = edges * primitive_bits
    dense_bits = vertices * vertices + edges * state_bits
    return {
        "vertices": vertices,
        "degree": degree,
        "edges": edges,
        "endpoint_bits": endpoint_bits,
        "state_bits": state_bits,
        "bits_per_eml_primitive": primitive_bits,
        "eml_total_bits": eml_bits,
        "dense_total_bits": dense_bits,
        "compression_ratio_dense_over_eml": dense_bits / eml_bits,
        "eml_is_smaller": eml_bits < dense_bits,
        "physics_derived": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vertices", type=int, default=1024)
    parser.add_argument("--degree", type=int, default=6)
    parser.add_argument("--messages", type=int, default=16)
    parser.add_argument("--laws", type=int, default=8)
    parser.add_argument("--phase-bits", type=int, default=12)
    args = parser.parse_args()
    try:
        result = estimate(args.vertices, args.degree, args.messages,
                          args.laws, args.phase_bits)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
