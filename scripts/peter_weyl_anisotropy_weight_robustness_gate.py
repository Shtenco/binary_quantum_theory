#!/usr/bin/env python3
"""Positive-weight robustness of the Peter-Weyl logical anisotropy.

The environment-unbiased structural return kernel can be written as a sum over
intermediate Peter-Weyl basis states n,

    K_ret = sum_n K_n,

where each K_n is positive semidefinite (an outer product of first-action
amplitudes, averaged over the maximally mixed logical environment).

Any state-diagonal positive resolvent/transfer reweighting has the form

    K_w = sum_n w_n K_n,  w_n > 0.

After the exact diagonal S4 twirl, the only pseudospin anisotropy is

    Delta = J_orientation - J_shape
          = c_YY + (c_XX+c_ZZ)/2

in the pre-B-rotation Pauli coefficients. Because Delta is linear in K, define
per-intermediate-state contributions delta_n. If all nonzero delta_n have the
same sign, the anisotropy sign is robust under *every* positive state-diagonal
weighting, without choosing a denominator. If signs are mixed, arbitrary
positive weighting can in principle change the sign and one must derive the
physical resolvent.

The gate also scans broad spin-cost weighting families as diagnostics. It is not
a derivation of the physical constrained-gravity resolvent.
"""
from __future__ import annotations

import argparse
import itertools
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


def delta_from_kernel(K):
    coeff, _ = AN.pauli_decompose(K)
    # B-sublattice Y rotation sends XX->-XX, YY->+YY, ZZ->-ZZ.
    # Thus J_shape=-(cXX+cZZ)/2 and J_orientation=cYY.
    return float((coeff["YY"] + 0.5 * (coeff["XX"] + coeff["ZZ"])).real)


def c0_from_kernel(K):
    coeff, _ = AN.pauli_decompose(K)
    return float(coeff["II"].real)


def state_features(key):
    spins, Ks = key
    spin_cost = float(sum((s - 1) ** 2 for s in spins))
    changed_edges = int(sum(s != 1 for s in spins))
    max_spin2 = int(max(spins))
    min_spin2 = int(min(spins))
    return {
        "spin_cost": spin_cost,
        "changed_edges": changed_edges,
        "max_spin2": max_spin2,
        "min_spin2": min_spin2,
    }


def weighted_delta(contribs, weight_fn):
    K = np.zeros((4, 4), dtype=complex)
    for key, Kn in contribs.items():
        K += float(weight_fn(key)) * Kn
    return delta_from_kernel(K), c0_from_kernel(K)


def build_contributions():
    AN.ZVM.patch_and_clear()
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

        keys = set().union(*(img.keys() for img in images))
        for key in keys:
            a = np.array([img.get(key, 0j) for img in images], dtype=complex)
            # K_ij = conj(a_i) a_j
            contribs[key] += np.outer(np.conj(a), a) / len(AN.ENV_STATES)

    return dict(contribs), first_projection_max


def run():
    contribs, first_projection_max = build_contributions()

    total_K = sum(contribs.values(), np.zeros((4, 4), dtype=complex))
    total_delta = delta_from_kernel(total_K)
    total_c0 = c0_from_kernel(total_K)

    rows = []
    pos_sum = 0.0
    neg_sum = 0.0
    zero_count = 0
    by_class = defaultdict(lambda: {"count": 0, "delta": 0.0, "c0": 0.0})

    for key, Kn in contribs.items():
        d = delta_from_kernel(Kn)
        c0 = c0_from_kernel(Kn)
        f = state_features(key)
        if d > TOL:
            pos_sum += d
            sign = "+"
        elif d < -TOL:
            neg_sum += d
            sign = "-"
        else:
            zero_count += 1
            sign = "0"
        cls = (f["spin_cost"], f["changed_edges"], f["max_spin2"], f["min_spin2"])
        by_class[cls]["count"] += 1
        by_class[cls]["delta"] += d
        by_class[cls]["c0"] += c0
        rows.append({
            "spins2": list(key[0]),
            "Ks2": list(key[1]),
            **f,
            "delta_aniso": d,
            "II_weight": c0,
            "sign": sign,
        })

    rows.sort(key=lambda x: abs(x["delta_aniso"]), reverse=True)

    classes = []
    for cls, rec in sorted(by_class.items()):
        classes.append({
            "spin_cost": cls[0],
            "changed_edges": cls[1],
            "max_spin2": cls[2],
            "min_spin2": cls[3],
            **rec,
        })

    nonzero = [r for r in rows if r["sign"] != "0"]
    all_positive = bool(nonzero) and all(r["sign"] == "+" for r in nonzero)
    all_negative = bool(nonzero) and all(r["sign"] == "-" for r in nonzero)
    sign_definite = all_positive or all_negative

    scans = []
    for family in ("rational", "exponential", "inverse_shift"):
        mus = (0.01, 0.1, 0.3, 1.0, 3.0, 10.0, 100.0) if family != "exponential" else (0.01, 0.1, 0.3, 1.0, 3.0, 5.0)
        for mu in mus:
            if family == "rational":
                fn = lambda k, mu=mu: 1.0 / (1.0 + mu * state_features(k)["spin_cost"])
            elif family == "exponential":
                fn = lambda k, mu=mu: math.exp(-mu * state_features(k)["spin_cost"])
            else:
                fn = lambda k, mu=mu: 1.0 / (mu + state_features(k)["spin_cost"])
            d, c0 = weighted_delta(contribs, fn)
            scans.append({
                "family": family,
                "mu": mu,
                "delta_aniso": d,
                "II_weight": c0,
                "delta_over_II": d / c0 if abs(c0) > 1e-30 else None,
                "same_sign_as_unweighted": d * total_delta > 0,
            })

    max_reconstruction_error = abs((pos_sum + neg_sum) - total_delta)

    passed = (
        first_projection_max < 1e-12
        and abs(total_delta - 3.6832250321658044) < 5e-8
        and max_reconstruction_error < 1e-9
        and all(s["same_sign_as_unweighted"] for s in scans)
    )

    return {
        "status": "Peter-Weyl anisotropy positive-weight robustness gate",
        "passed": bool(passed),
        "intermediate_state_count": len(contribs),
        "first_order_projection_max": first_projection_max,
        "unweighted": {
            "Delta_aniso": total_delta,
            "II_weight": total_c0,
            "Delta_over_II": total_delta / total_c0,
        },
        "per_state_sign_cone": {
            "positive_delta_sum": pos_sum,
            "negative_delta_sum": neg_sum,
            "zero_delta_state_count": zero_count,
            "positive_state_count": sum(r["sign"] == "+" for r in rows),
            "negative_state_count": sum(r["sign"] == "-" for r in rows),
            "sign_definite_under_arbitrary_positive_state_weights": bool(sign_definite),
            "sign": "+" if all_positive else ("-" if all_negative else "mixed"),
            "reconstruction_error": max_reconstruction_error,
        },
        "spin_cost_weight_scans": scans,
        "intermediate_classes": classes,
        "largest_absolute_state_contributions": rows[:40],
        "interpretation": (
            "If sign_definite_under_arbitrary_positive_state_weights is true, every positive state-diagonal "
            "resolvent weighting preserves the anisotropy sign. If it is false, the broad scans report only "
            "diagnostic robustness and the physical constrained resolvent remains decisive."
        ),
        "scope": (
            "This is a denominator-robustness diagnostic. It does not derive the actual Feshbach/Dirac-constraint "
            "resolvent and does not convert the return-kernel Delta into a physical mass gap."
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
