#!/usr/bin/env python3
"""First nontrivial internal Peter-Weyl RG step: j=1 coarse S4 doublet.

The geometry-only PL Galerkin control proves that spatial averaging by itself
cannot move the normalized logical anisotropy.  The next parameter-free source
of flow is representation growth.

This script keeps the same 32-dimensional logical-qubit ordering as the frozen
j=1/2 higher-shell calculation, but replaces each local four-spin j=1/2 singlet
qubit by the unique S4 [2,2] doublet inside the four-spin j=1 singlet space:

    |0>_c = |K=2>,
    |1>_c = (2 |K=0> - sqrt(5) |K=4>) / 3.

That is exactly the symmetry intertwiner certified by
``peter_weyl_j1_s4_block_gate.py``.  All ten K5 edge spins are set to j=1 and
the same H_sine = H_E,0 + H_E,1 engine is used.  Column mode computes H|i>
and H^2|i>; assembly reuses the frozen denominator-free block-Lanczos
construction and reports the first representation-RG change of R_aniso.

Scope: this is an internal representation RG step, not yet the full 24-child
barycentric spatial block.  It is nevertheless non-arbitrary: both the coarse
face irrep and logical doublet projector are fixed by SU(2) x S4 symmetry.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import peter_weyl_higher_shell_lambda_gate as HS
import peter_weyl_logical_anisotropy_gate as AN


NLOGICAL = 32
SPINS_J1 = (2,) * 10  # doubled-spin convention
R_FINE = 0.0897532661805313

# Local coarse logical qubit in K=(0,2,4) recoupling basis.
LOCAL = {
    0: ((2, 1.0),),
    1: ((0, 2.0 / 3.0), (4, -math.sqrt(5.0) / 3.0)),
}


def logical_labels_bits():
    labels = []
    for env in itertools.product((0, 1), repeat=3):
        for pair in itertools.product((0, 1), repeat=2):
            labels.append((pair[0], pair[1], env[0], env[1], env[2]))
    if len(labels) != NLOGICAL:
        raise RuntimeError("logical basis size mismatch")
    return labels


def coarse_state(bits):
    """Product of five symmetry-selected local j=1 S4 doublets."""
    out = {}
    choices = [LOCAL[int(b)] for b in bits]
    for local in itertools.product(*choices):
        Ks = tuple(int(k) for k, _ in local)
        amp = 1.0
        for _, c in local:
            amp *= c
        if abs(amp) > HS.TOL:
            out[(SPINS_J1, Ks)] = complex(amp)
    # Each local vector is normalized; verify product normalization explicitly.
    norm2 = sum(abs(a) ** 2 for a in out.values())
    if abs(norm2 - 1.0) > 2e-12:
        raise RuntimeError(f"coarse logical state not normalized: {norm2}")
    return out


def max_spin(state):
    return HS.max_spin(state)


def compute_column(index: int):
    if not 0 <= index < NLOGICAL:
        raise ValueError(f"column must be in [0,{NLOGICAL-1}]")
    AN.ZVM.patch_and_clear()
    labels = logical_labels_bits()
    bits = labels[index]
    ket = coarse_state(bits)

    a = HS.apply_H_state(ket)
    # Spin parity is stronger than the coarse-P test here: any first-order state
    # with all ten edges back at j=1 would be suspicious.  The exact sine action
    # should have none.
    all_j1 = {k: v for k, v in a.items() if all(s == 2 for s in k[0])}
    first_proj = AN.sparse_norm(all_j1)
    b = HS.apply_H_state(a)

    return {
        "status": "exact j=1 S4-doublet Peter-Weyl higher-shell logical column",
        "column": index,
        "label": {
            "bits_q0_q1_q2_q3_q4": list(bits),
            "environment_bits_q234": list(bits[2:]),
            "pair_bits_q01": list(bits[:2]),
        },
        "coarse_face_spin": 1.0,
        "coarse_local_irrep": "S4 [2,2] doublet in four-j=1 singlet",
        "Jmax_used": HS.JMAX2_SECOND_HIT_SAFE / 2.0,
        "first_order_projection_norm": float(first_proj),
        "first_support": len(a),
        "second_support": len(b),
        "first_max_spin": max_spin(a),
        "second_max_spin": max_spin(b),
        "first_state": HS.state_to_rows(a),
        "second_state": HS.state_to_rows(b),
    }


def assemble(directory: Path):
    out = HS.assemble(directory)
    pair = out["pair_partial_trace_01"]
    raw = pair["raw_pauli_coefficients"]
    c0 = float(raw["II"][0])
    delta = float(pair["Delta_orient_minus_shape"])
    r_coarse = delta / c0

    out["status"] = "actual finite j=1 S4-doublet higher-shell Lambda / first internal representation-RG step"
    out["representation_RG"] = {
        "fine_face_spin": 0.5,
        "coarse_face_spin": 1.0,
        "coarse_projector": "unique multiplicity-one S4 [2,2] doublet",
        "local_basis": {
            "logical_0": "K=2",
            "logical_1": "(2 K=0 - sqrt(5) K=4)/3",
        },
        "R_aniso_fine_jhalf": R_FINE,
        "R_aniso_coarse_j1": r_coarse,
        "Delta_R": r_coarse - R_FINE,
        "ratio_R_coarse_over_fine": r_coarse / R_FINE,
        "discrete_beta_log2": (r_coarse - R_FINE) / math.log(2.0),
        "interpretation": (
            "This is the first non-separable internal representation step after the geometry-only Galerkin no-flow control. "
            "It is a candidate beta-function datum for the logical anisotropy, not yet the full spatial TT zeta4 coefficient."
        ),
    }
    out["support"]["regulator_note"] = (
        "Initial edges are j=1. Two Euclidean sine-H hits can reach at most j=2 per edge in the observed support; "
        "the inherited Jmax=5/2 engine is therefore conservative. Assembly still checks the actual maximum spin."
    )
    out["scientific_scope"] = (
        "Finite Euclidean H_E0+H_E1 calculation on the symmetry-selected j=1 coarse logical carrier. "
        "No external data, energy denominator, fitted projector or fitted RG coefficient is used. "
        "A full physical TT RG still requires embedding this internal step into recursive spatial PL blocking and the Lorentzian/history kernel."
    )
    return out


def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--column", type=int)
    mode.add_argument("--assemble-dir", type=Path)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    if args.column is not None:
        out = compute_column(args.column)
        write_json(args.output, out)
        print(json.dumps({
            "column": out["column"],
            "first_support": out["first_support"],
            "second_support": out["second_support"],
            "first_order_projection_norm": out["first_order_projection_norm"],
            "second_max_spin": out["second_max_spin"],
        }, indent=2))
        return 0 if out["first_order_projection_norm"] < 1e-12 else 1

    out = assemble(args.assemble_dir)
    write_json(args.output, out)
    print(json.dumps({
        "passed": out["passed"],
        "R_aniso_fine": out["representation_RG"]["R_aniso_fine_jhalf"],
        "R_aniso_coarse": out["representation_RG"]["R_aniso_coarse_j1"],
        "Delta_R": out["representation_RG"]["Delta_R"],
        "Lambda_min": out["Lambda"]["eigenvalue_min"],
        "Lambda_max": out["Lambda"]["eigenvalue_max"],
    }, indent=2))
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
