#!/usr/bin/env python3
"""Extract the exact S4-reduced two-cell RG seed from higher-shell Lambda.

Input is the JSON emitted by peter_weyl_higher_shell_lambda_gate.py --assemble-dir.
The S4 theorem itself is independently certified in LOGICAL_S4_TWIRL.md:

    Inv_S4(two cells) = span{II, XX+ZZ, YY}.

This script therefore does not fit a symmetry basis. It applies the already
fixed bipartite B-frame convention and reads the symmetry-allowed couplings.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

TOL = 1e-10


def cpair(raw: dict, label: str) -> complex:
    z = raw[label]
    return complex(float(z[0]), float(z[1]))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", type=Path, required=True)
    ap.add_argument("--output", type=Path, default=None)
    args = ap.parse_args()

    data = json.loads(args.input.read_text(encoding="utf-8"))
    pair = data["pair_partial_trace_01"]
    raw = pair["raw_pauli_coefficients"]

    # Canonical B-sublattice rotation: (X,Y,Z)_B -> (-X,+Y,-Z)_B.
    c0 = cpair(raw, "II").real
    jx = -cpair(raw, "XX").real
    jy = +cpair(raw, "YY").real
    jz = -cpair(raw, "ZZ").real
    j_shape = 0.5 * (jx + jz)
    j_orient = jy
    delta = j_orient - j_shape

    # Terms known to be removed by exact one-/two-cell S4 twirling.  They are
    # reported, not used in the invariant seed.
    local_labels = ["IX", "IY", "IZ", "XI", "YI", "ZI"]
    offdiag_labels = ["XY", "XZ", "YX", "YZ", "ZX", "ZY"]
    local_norm2 = sum(abs(cpair(raw, x)) ** 2 for x in local_labels)
    offdiag_norm2 = sum(abs(cpair(raw, x)) ** 2 for x in offdiag_labels)

    # Cross-check against the assembler's independently reported values.
    js_ref = float(pair["S4_shape_coupling_after_B_rotation"])
    jo_ref = float(pair["orientation_coupling_after_B_rotation"])
    d_ref = float(pair["Delta_orient_minus_shape"])

    crosscheck = {
        "shape_abs_error": abs(j_shape - js_ref),
        "orient_abs_error": abs(j_orient - jo_ref),
        "delta_abs_error": abs(delta - d_ref),
    }

    passed = (
        abs(cpair(raw, "II").imag) < TOL
        and max(crosscheck.values()) < TOL
        and abs(c0) > TOL
    )

    out = {
        "status": "exact S4-reduced higher-shell Peter-Weyl RG seed",
        "passed": bool(passed),
        "input_status": data.get("status"),
        "input_gate_passed": bool(data.get("passed", False)),
        "theorem": "Inv_S4(two logical geometry cells)=span{II,XX+ZZ,YY}",
        "B_sublattice_frame": "diag(X,Y,Z)=(-1,+1,-1)",
        "twirled_pair_kernel": {
            "c0_II": c0,
            "J_shape_XX_plus_ZZ": j_shape,
            "J_orient_YY": j_orient,
            "Delta_orient_minus_shape": delta,
        },
        "dimensionless_seed": {
            "J_shape_over_c0": j_shape / c0,
            "J_orient_over_c0": j_orient / c0,
            "Delta_over_c0": delta / c0,
            "J_orient_over_abs_J_shape": j_orient / abs(j_shape),
        },
        "twirled_away_diagnostics_before_twirl": {
            "local_field_coefficient_l2": local_norm2 ** 0.5,
            "offdiagonal_pair_coefficient_l2": offdiag_norm2 ** 0.5,
        },
        "assembler_crosscheck": crosscheck,
        "next_gate": (
            "Track Delta_aniso(b)/|c0(b)| under recursive PL/Peter-Weyl blocking "
            "and derive its map to the spatial TT cubic coefficient zeta4_cub(b)."
        ),
        "scientific_scope": (
            "Exact symmetry reduction of a finite higher-shell artifact. "
            "Delta/c0 is a microscopic RG seed, not yet a physical Lorentz-violation observable."
        ),
    }

    text = json.dumps(out, indent=2)
    print(text)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")

    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
