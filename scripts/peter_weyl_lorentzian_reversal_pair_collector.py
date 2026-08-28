#!/usr/bin/env python3
"""Compare genuine Peter-Weyl Lorentzian ordered triples under a<->b reversal.

Input workers contain complete pruned sparse states for

    T_abc = Tr_aux[C_a(K_sine) C_b(K_sine) C_c(V)]
    T_bac = Tr_aux[C_b(K_sine) C_a(K_sine) C_c(V)].

The orientation-odd amplitude is their antisymmetric part

    T_odd = (T_abc - T_bac)/2.

This is a cheap genuine-amplitude falsifier before assembling all 24 epsilon
terms.  A nonzero result licenses the expensive epsilon/Y projection.  A zero
result kills this local reversal-odd channel on the tested microscopic input.
Neither outcome is yet g_YC^gravity because no relational/physical-history
kernel has been constructed.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

ZERO_REL = 1e-9
NONZERO_REL = 1e-6


def load_state(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    state = {
        row["key"]: complex(float(row["amp"][0]), float(row["amp"][1]))
        for row in data["state"]
    }
    return data, state


def norm2(state: dict[str, complex]) -> float:
    return float(sum(abs(z) ** 2 for z in state.values()))


def combine(A, B, ca, cb, tol=1e-13):
    out = {}
    for k in set(A) | set(B):
        z = ca * A.get(k, 0j) + cb * B.get(k, 0j)
        if abs(z) > tol:
            out[k] = z
    return out


def overlap(A, B):
    return sum(A.get(k, 0j).conjugate() * B.get(k, 0j) for k in set(A) | set(B))


def run(path_abc: Path, path_bac: Path):
    da, A = load_state(path_abc)
    db, B = load_state(path_bac)

    nA = math.sqrt(norm2(A))
    nB = math.sqrt(norm2(B))
    scale = max(nA, nB, 1e-30)

    diff = combine(A, B, +1.0, -1.0)
    summ = combine(A, B, +1.0, +1.0)
    odd = combine(A, B, +0.5, -0.5)
    even = combine(A, B, +0.5, +0.5)

    nd = math.sqrt(norm2(diff))
    ns = math.sqrt(norm2(summ))
    no = math.sqrt(norm2(odd))
    ne = math.sqrt(norm2(even))
    rel = nd / scale

    ov = overlap(A, B)
    ovn = ov / (nA * nB) if nA > 0 and nB > 0 else 0j

    only_a = len(set(A) - set(B))
    only_b = len(set(B) - set(A))
    common = len(set(A) & set(B))

    if rel < ZERO_REL:
        classification = "ZERO_WITHIN_PREREGISTERED_TOLERANCE"
    elif rel > NONZERO_REL:
        classification = "NONZERO_GENUINE_ORIENTATION_ODD_AMPLITUDE"
    else:
        classification = "AMBIGUOUS_NUMERICAL_BAND"

    denom = no * no + ne * ne
    odd_weight_fraction = (no * no / denom) if denom > 0 else 0.0

    workers_ok = bool(da.get("passed") and db.get("passed"))
    ordering_ok = (
        da.get("source_node") == db.get("source_node")
        and da.get("ordered_edges") == [1, 2, 3]
        and db.get("ordered_edges") == [2, 1, 3]
    )
    resolved = classification != "AMBIGUOUS_NUMERICAL_BAND"
    passed = bool(workers_ok and ordering_ok and resolved and nA > 1e-12 and nB > 1e-12)

    ranked = sorted(diff.items(), key=lambda kv: abs(kv[1]), reverse=True)[:16]

    return {
        "status": "genuine sine-ordered Peter-Weyl Lorentzian a<->b reversal amplitude test",
        "passed": passed,
        "preregistered_relative_thresholds": {
            "zero_if_below": ZERO_REL,
            "nonzero_if_above": NONZERO_REL,
            "between_is": "AMBIGUOUS_NUMERICAL_BAND",
        },
        "classification": classification,
        "T_abc": {
            "support": len(A),
            "norm": nA,
            "state_sha256": da.get("state_sha256"),
        },
        "T_bac": {
            "support": len(B),
            "norm": nB,
            "state_sha256": db.get("state_sha256"),
        },
        "support_comparison": {
            "common": common,
            "only_abc": only_a,
            "only_bac": only_b,
        },
        "reversal_difference_norm": nd,
        "reversal_sum_norm": ns,
        "relative_reversal_difference": rel,
        "orientation_odd_half_difference_norm": no,
        "orientation_even_half_sum_norm": ne,
        "orientation_odd_weight_fraction_in_even_plus_odd_norm2": odd_weight_fraction,
        "normalized_overlap": [float(complex(ovn).real), float(complex(ovn).imag)],
        "largest_difference_amplitudes": [
            {
                "key": k,
                "amp_abc_minus_bac": [float(z.real), float(z.imag)],
                "abs": float(abs(z)),
            }
            for k, z in ranked
        ],
        "interpretation_if_nonzero": (
            "The real safe Peter-Weyl K_sine-K_sine-V amplitude already contains a reversal-odd component. This licenses the next expensive calculation: the full four-face, 24-permutation epsilon sum followed by logical Y projection."
        ),
        "interpretation_if_zero": (
            "On this preregistered microscopic input the tested a<->b reversal-odd ordered-triple channel vanishes within tolerance; the corresponding local orientation-odd route must not be promoted to a physical coupling without a different explicitly justified operator/history sector."
        ),
        "physical_g_YC": "OPEN_PHYSICAL",
        "claim_boundary": (
            "This compares genuine safe ordered Lorentzian Peter-Weyl amplitudes. It is not the full epsilon-oriented H_L node operator, not its logical Y coefficient, and not the relational/history coefficient g_YC^gravity."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--abc", type=Path, required=True)
    ap.add_argument("--bac", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    x = ap.parse_args()
    out = run(x.abc, x.bac)
    text = json.dumps(out, indent=2)
    print(text)
    x.output.parent.mkdir(parents=True, exist_ok=True)
    x.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
