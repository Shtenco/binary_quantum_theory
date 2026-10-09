#!/usr/bin/env python3
"""First theory-specific BQG j=1/2 -> j=1 logical RG return-kernel datum.

This script uses the *same* regulator-safe Peter-Weyl H_01=H_E,0+H_E,1
production action on two symmetry-matched 32D logical carriers:

fine:
    all incident spins j=1/2, local K in {0,2}

coarse:
    all incident spins j=1, local singlet K in {0,2,4},
    but each local logical qubit is embedded through the exact canonical
    S4-[2,2] intertwiner W

        |0_L> -> |K=2>
        |1_L> -> (2/3)|K=0> - (sqrt(5)/3)|K=4>.

For each logical basis vector |q0...q4>, compute H_01|psi>, then the positive
return kernel

    K = A^dagger A = P H_01^2 P

in the common logical coordinates.

The output compares K_coarse against K_fine and reports the normalized
dynamical mismatch. This is a genuine BQG representation-RG datum for the
finite Euclidean return/master-control. It is NOT yet the full graph-changing
master constraint M=C^dagger G C and therefore must not be promoted directly
to continuum physical-projector convergence.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import peter_weyl_logical_anisotropy_gate as AN
import peter_weyl_euclidean_sine_ordering_gate as SINE
import peter_weyl_zeroaware_volume_migration_experiment as ZVM
import k5_peter_weyl_safe_hda_column as PW

TOL = 1e-11
# Fine one-hit safe wall already used by the canonical 32D gate.
JMAX2_FINE = 3
# j=1 input plus one fundamental hit can reach j=3/2, so doubled-spin 3
# is sufficient for one H action; use 5 conservatively to stay aligned with
# the existing regulator-safe Euclidean engine.
JMAX2_COARSE = 5

LOGICAL_BITS = tuple(itertools.product((0, 1), repeat=5))


def sparse_add(dst, src, scale=1.0):
    for k, a in src.items():
        z = dst.get(k, 0j) + scale * a
        if abs(z) > TOL:
            dst[k] = z
        elif k in dst:
            del dst[k]


def sparse_inner(a, b):
    if len(a) > len(b):
        a, b = b, a
        return np.conj(sparse_inner(a, b))
    return sum(np.conj(v) * b.get(k, 0j) for k, v in a.items())


def sparse_norm(a):
    return math.sqrt(float(sum(abs(v) ** 2 for v in a.values())))


def local_coarse_components(bit: int):
    if bit == 0:
        return ((2, 1.0),)
    if bit == 1:
        return ((0, 2.0 / 3.0), (4, -math.sqrt(5.0) / 3.0))
    raise ValueError(bit)


def fine_logical_state(bits):
    # Common logical ordering q0,q1,q2,q3,q4.
    spins = (1,) * len(PW.EDGES)
    Ks = tuple(0 if b == 0 else 2 for b in bits)
    return {(spins, Ks): 1.0 + 0j}


def coarse_logical_state(bits):
    spins = (2,) * len(PW.EDGES)
    out = {}
    choices = [local_coarse_components(int(b)) for b in bits]
    for prod in itertools.product(*choices):
        Ks = tuple(int(K) for K, _ in prod)
        amp = 1.0
        for _, c in prod:
            amp *= c
        if abs(amp) > TOL:
            out[(spins, Ks)] = complex(amp)
    # Exact tensor-product isometry implies unit norm; enforce numerically.
    n = sparse_norm(out)
    if abs(n - 1.0) > 1e-12:
        raise RuntimeError(f"coarse logical state not normalized: {bits} norm={n}")
    return out


def apply_H01(state, jmax2):
    out = {}
    sparse_add(out, SINE.safe_H_sine(state, 0, jmax2))
    sparse_add(out, SINE.safe_H_sine(state, 1, jmax2))
    return {k: a for k, a in out.items() if abs(a) > TOL}


def gram(images):
    n = len(images)
    G = np.zeros((n, n), dtype=complex)
    for i in range(n):
        for j in range(i, n):
            z = sparse_inner(images[i], images[j])
            G[i, j] = z
            G[j, i] = np.conj(z)
    return (G + G.conj().T) / 2


def spectrum_summary(K):
    ev = np.linalg.eigvalsh((K + K.conj().T) / 2).real
    scale = max(float(np.max(np.abs(ev))), 1.0)
    tol = 1e-10 * scale
    pos = ev[ev > tol]
    return {
        "rank": int(np.sum(ev > tol)),
        "nullity": int(np.sum(ev <= tol)),
        "eigenvalue_min": float(np.min(ev)),
        "eigenvalue_max": float(np.max(ev)),
        "smallest_positive_eigenvalue": float(np.min(pos)) if len(pos) else None,
        "condition_number_on_support": float(np.max(pos) / np.min(pos)) if len(pos) else None,
        "eigenvalues": [float(x) for x in ev],
    }


def run():
    ZVM.patch_and_clear()

    fine_images = []
    coarse_images = []
    rows = []

    for bits in LOGICAL_BITS:
        sf = fine_logical_state(bits)
        sc = coarse_logical_state(bits)
        af = apply_H01(sf, JMAX2_FINE)
        ac = apply_H01(sc, JMAX2_COARSE)
        fine_images.append(af)
        coarse_images.append(ac)

        rows.append({
            "logical_bits_q0_to_q4": list(bits),
            "fine_input_support": len(sf),
            "coarse_input_support": len(sc),
            "fine_H01_support": len(af),
            "coarse_H01_support": len(ac),
            "fine_H01_norm": sparse_norm(af),
            "coarse_H01_norm": sparse_norm(ac),
            "fine_max_spin_after_hit": max((max(k[0]) / 2 for k in af), default=0.0),
            "coarse_max_spin_after_hit": max((max(k[0]) / 2 for k in ac), default=0.0),
        })

    Kf = gram(fine_images)
    Kc = gram(coarse_images)
    D = Kc - Kf

    nf = float(np.linalg.norm(Kf, 2))
    nc = float(np.linalg.norm(Kc, 2))
    nd = float(np.linalg.norm(D, 2))
    fro_rel = float(np.linalg.norm(D) / max(np.linalg.norm(Kf), 1e-30))
    op_rel = nd / max(nf, 1e-30)

    sf = spectrum_summary(Kf)
    sc = spectrum_summary(Kc)

    # Symmetry-matched logical coordinates: no fitted basis rotation allowed.
    herm_f = float(np.linalg.norm(Kf - Kf.conj().T))
    herm_c = float(np.linalg.norm(Kc - Kc.conj().T))
    psd_tol_f = 1e-8 * max(nf, 1.0)
    psd_tol_c = 1e-8 * max(nc, 1.0)

    passed = (
        herm_f < 1e-9
        and herm_c < 1e-9
        and sf["eigenvalue_min"] > -psd_tol_f
        and sc["eigenvalue_min"] > -psd_tol_c
        and max(r["fine_max_spin_after_hit"] for r in rows) <= 1.0 + 1e-12
        and max(r["coarse_max_spin_after_hit"] for r in rows) <= 1.5 + 1e-12
    )

    return {
        "status": "first BQG j=1/2 -> j=1 symmetry-matched logical RG return-kernel datum",
        "passed": bool(passed),
        "logical_dimension": 32,
        "logical_basis": "q0,q1,q2,q3,q4 bits; same coordinates at fine/coarse scales",
        "local_embedding": {
            "fine": "bit0->K0, bit1->K2 on j=1/2 singlet",
            "coarse": "bit0->K2; bit1->(2/3)K0-(sqrt5/3)K4 on j=1 singlet",
            "source": "exact canonical S4-[2,2] intertwiner W",
        },
        "operator": "K=P(H_E0^sine+H_E1^sine)^2P = Gram of one-hit images",
        "fine": {
            "face_spin": 0.5,
            "Jmax_one_hit": JMAX2_FINE / 2,
            "spectrum": sf,
            "operator_norm": nf,
            "frobenius_norm": float(np.linalg.norm(Kf)),
        },
        "coarse": {
            "face_spin": 1.0,
            "Jmax_one_hit": JMAX2_COARSE / 2,
            "spectrum": sc,
            "operator_norm": nc,
            "frobenius_norm": float(np.linalg.norm(Kc)),
        },
        "dynamical_mismatch": {
            "definition": "D=K_j1-K_jhalf in canonical symmetry-matched logical coordinates",
            "operator_norm": nd,
            "relative_operator_norm_to_fine": op_rel,
            "relative_frobenius_norm_to_fine": fro_rel,
            "trace_difference": float(np.trace(D).real),
        },
        "columns": rows,
        "claim_boundary": (
            "This compares the same finite Euclidean positive return/master-control across the exact first representation-RG embedding. "
            "It is a genuine theory-specific RG datum but not yet the full master-constraint residual R=M_c W-W M_f; "
            "off-carrier leakage of the full coarse master and the physical master gaps remain separate required calculations."
        ),
    }


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
    return 0 if out["passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
