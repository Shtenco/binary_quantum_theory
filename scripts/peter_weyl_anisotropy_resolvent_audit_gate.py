#!/usr/bin/env python3
"""Audited intermediate-state decomposition of the Peter-Weyl logical return kernel.

This gate has two jobs and deliberately keeps them separate.

1. ACCOUNTING CERTIFICATE
   Reconstruct the environment-unbiased direct kernel

       K_direct = (1/8) sum_env Gram[ H_01 |pair,env> ]

   from individual Peter-Weyl intermediate basis states,

       K_recon = sum_n K_n,

   and require matrix-level equality plus equality of the S4-reduced anisotropy
   and identity coefficient. No cone/fingerprint result is trusted unless these
   identities pass.

2. GEOMETRIC FINGERPRINT
   For each actual intermediate basis state compute the existing local
   Peter-Weyl volume expectation at every K5 node. This is a diagnostic for the
   future constrained resolvent. No volume-dependent weight used below is
   asserted to be the physical Feshbach/Dirac resolvent.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import peter_weyl_logical_anisotropy_gate as AN

TOL = 1e-13
CANONICAL_DELTA = 2.738458660882762


def delta_from_kernel(K):
    c, _ = AN.pauli_decompose(K)
    # B-sublattice pi-Y rotation: XX->-XX, YY->+YY, ZZ->-ZZ.
    # J_shape=-(cXX+cZZ)/2, J_orient=cYY.
    return float((c["YY"] + 0.5 * (c["XX"] + c["ZZ"])).real)


def c0_from_kernel(K):
    c, _ = AN.pauli_decompose(K)
    return float(c["II"].real)


def direct_and_contributions():
    AN.ZVM.patch_and_clear()
    direct = np.zeros((4, 4), dtype=complex)
    contribs = defaultdict(lambda: np.zeros((4, 4), dtype=complex))
    first_projection_max = 0.0

    for env in AN.ENV_STATES:
        images = []
        for pair in AN.PAIR_STATES:
            key = AN.logical_key(pair[0], pair[1], env)
            img = AN.apply_pair_HE(key)
            projected = {k: v for k, v in img.items() if AN.is_all_jhalf(k)}
            first_projection_max = max(first_projection_max, AN.sparse_norm(projected))
            images.append(img)

        direct += AN.kernel_from_images(images) / len(AN.ENV_STATES)
        keys = set().union(*(img.keys() for img in images))
        for key in keys:
            a = np.array([img.get(key, 0j) for img in images], dtype=complex)
            contribs[key] += np.outer(np.conj(a), a) / len(AN.ENV_STATES)

    return direct, dict(contribs), first_projection_max


def local_volume_expectation(key, v):
    spins, Ks = key
    ls = AN.PW.local_spins(spins, v)
    K = Ks[v]
    T = AN.PW.oriented_intertwiner(v, ls, K)
    den = float(np.vdot(T, T).real)
    if den < 1e-30:
        return 0.0
    VT = AN.PW.apply_volume_tensor_oriented(T, ls, v)
    z = np.vdot(T, VT) / den
    if abs(z.imag) > 1e-9:
        raise RuntimeError(f"complex volume expectation at node {v}: {z}")
    return float(z.real)


def state_features(key):
    spins, Ks = key
    vols = [local_volume_expectation(key, v) for v in AN.PW.VERT]
    return {
        "spin_cost": float(sum((s - 1) ** 2 for s in spins)),
        "changed_edges": int(sum(s != 1 for s in spins)),
        "max_spin2": int(max(spins)),
        "min_spin2": int(min(spins)),
        "Ks2": list(Ks),
        "volumes": vols,
        "volume_total": float(sum(vols)),
        "volume_min": float(min(vols)),
        "volume_max": float(max(vols)),
        "volume_pair01": float(vols[0] + vols[1]),
        "zero_volume_nodes": int(sum(abs(v) < 1e-12 for v in vols)),
    }


def weighted_kernel(contribs, weight_fn):
    K = np.zeros((4, 4), dtype=complex)
    for key, Kn in contribs.items():
        K += float(weight_fn(key)) * Kn
    return K


def summarize_group(rows):
    if not rows:
        return {"count": 0}
    ds = np.array([r["delta_aniso"] for r in rows], float)
    vt = np.array([r["volume_total"] for r in rows], float)
    vm = np.array([r["volume_min"] for r in rows], float)
    vp = np.array([r["volume_pair01"] for r in rows], float)
    return {
        "count": len(rows),
        "delta_sum": float(ds.sum()),
        "delta_abs_sum": float(np.abs(ds).sum()),
        "volume_total_min": float(vt.min()),
        "volume_total_mean": float(vt.mean()),
        "volume_total_max": float(vt.max()),
        "volume_min_min": float(vm.min()),
        "volume_min_mean": float(vm.mean()),
        "volume_min_max": float(vm.max()),
        "volume_pair01_mean": float(vp.mean()),
        "states_with_any_zero_volume_node": int(sum(r["zero_volume_nodes"] > 0 for r in rows)),
    }


def run():
    direct, contribs, first_projection_max = direct_and_contributions()
    recon = sum(contribs.values(), np.zeros((4, 4), dtype=complex))

    direct_delta = delta_from_kernel(direct)
    recon_delta = delta_from_kernel(recon)
    direct_c0 = c0_from_kernel(direct)
    recon_c0 = c0_from_kernel(recon)

    matrix_error = float(np.linalg.norm(recon - direct))

    rows = []
    class_acc = defaultdict(lambda: {"count": 0, "delta": 0.0, "c0": 0.0})
    for key, Kn in contribs.items():
        d = delta_from_kernel(Kn)
        c0 = c0_from_kernel(Kn)
        f = state_features(key)
        sign = "+" if d > TOL else ("-" if d < -TOL else "0")
        row = {
            "spins2": list(key[0]),
            **f,
            "delta_aniso": d,
            "II_weight": c0,
            "sign": sign,
        }
        rows.append(row)
        cls = (f["spin_cost"], f["changed_edges"], f["max_spin2"], f["min_spin2"])
        class_acc[cls]["count"] += 1
        class_acc[cls]["delta"] += d
        class_acc[cls]["c0"] += c0

    pos = [r for r in rows if r["sign"] == "+"]
    neg = [r for r in rows if r["sign"] == "-"]
    zero = [r for r in rows if r["sign"] == "0"]

    state_delta_sum = float(sum(r["delta_aniso"] for r in rows))
    state_c0_sum = float(sum(r["II_weight"] for r in rows))
    class_delta_sum = float(sum(x["delta"] for x in class_acc.values()))
    class_c0_sum = float(sum(x["c0"] for x in class_acc.values()))

    accounting = {
        "matrix_reconstruction_error": matrix_error,
        "direct_delta": direct_delta,
        "reconstructed_delta": recon_delta,
        "state_delta_sum": state_delta_sum,
        "class_delta_sum": class_delta_sum,
        "direct_II": direct_c0,
        "reconstructed_II": recon_c0,
        "state_II_sum": state_c0_sum,
        "class_II_sum": class_c0_sum,
        "delta_errors": {
            "recon_vs_direct": abs(recon_delta - direct_delta),
            "states_vs_direct": abs(state_delta_sum - direct_delta),
            "classes_vs_direct": abs(class_delta_sum - direct_delta),
        },
        "II_errors": {
            "recon_vs_direct": abs(recon_c0 - direct_c0),
            "states_vs_direct": abs(state_c0_sum - direct_c0),
            "classes_vs_direct": abs(class_c0_sum - direct_c0),
        },
    }

    accounting_pass = (
        first_projection_max < 1e-12
        and matrix_error < 1e-10
        and abs(direct_delta - CANONICAL_DELTA) < 5e-8
        and max(accounting["delta_errors"].values()) < 1e-10
        and max(accounting["II_errors"].values()) < 1e-10
    )

    # Only publish interpretation-level diagnostics if accounting is certified.
    geometry = None
    scans = None
    classes = None
    all_rows = None
    if accounting_pass:
        classes = [
            {
                "spin_cost": cls[0],
                "changed_edges": cls[1],
                "max_spin2": cls[2],
                "min_spin2": cls[3],
                **rec,
            }
            for cls, rec in sorted(class_acc.items())
        ]
        geometry = {
            "positive_sector": summarize_group(pos),
            "negative_sector": summarize_group(neg),
            "zero_sector": summarize_group(zero),
        }

        # Volume-weight families are diagnostics only, never identified with the physical resolvent.
        scans = []
        for family in ("exp_minus_total_volume", "inverse_shift_total_volume"):
            for mu in (0.0, 0.1, 0.3, 1.0, 3.0, 10.0):
                if family == "exp_minus_total_volume":
                    fn = lambda k, mu=mu: math.exp(-mu * state_features(k)["volume_total"])
                else:
                    fn = lambda k, mu=mu: 1.0 / (1.0 + mu * state_features(k)["volume_total"])
                Kw = weighted_kernel(contribs, fn)
                scans.append({
                    "family": family,
                    "mu": mu,
                    "delta_aniso": delta_from_kernel(Kw),
                    "II_weight": c0_from_kernel(Kw),
                })
        rows.sort(key=lambda r: abs(r["delta_aniso"]), reverse=True)
        all_rows = rows

    return {
        "status": "Peter-Weyl anisotropy constrained-resolvent audit gate",
        "passed": bool(accounting_pass),
        "first_order_projection_max": first_projection_max,
        "intermediate_state_count": len(contribs),
        "accounting": accounting,
        "sign_cone": None if not accounting_pass else {
            "positive_state_count": len(pos),
            "negative_state_count": len(neg),
            "zero_state_count": len(zero),
            "positive_delta_sum": float(sum(r["delta_aniso"] for r in pos)),
            "negative_delta_sum": float(sum(r["delta_aniso"] for r in neg)),
            "mixed": bool(pos and neg),
        },
        "spin_classes": classes,
        "volume_fingerprint": geometry,
        "volume_weight_diagnostics": scans,
        "all_intermediate_states": all_rows,
        "scope": (
            "PASS certifies only the exact finite decomposition and geometric fingerprint. "
            "Volume-dependent diagnostic weights are not the physical constrained Feshbach/Dirac resolvent; "
            "no static mirror mass, fifth force, or antigravity is inferred from them."
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
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
