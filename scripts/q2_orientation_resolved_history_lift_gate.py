#!/usr/bin/env python3
"""Exact minimal orientation-resolved q=2 history-lift gate.

This gate proves a narrow theorem, not a gravitational coupling calculation.
Given the already-derived minimal reversible C8 history shift U and the logical
geometry orientation pseudoscalar Y_L, classify deterministic nearest-neighbor
permutation lifts that

  * conserve Y_L during one history tick,
  * move one C8 edge per tick,
  * are covariant under simultaneous geometry-orientation and history reversal.

The unique class up to global orientation convention is

    W = P_+ x U + P_- x U^-1,
    P_+/- = (I +/- Y_L)/2.

Its Hermitian even/odd parts are exactly

    (W+W^dagger)/2  = I x (U+U^-1)/2,
    (W-W^dagger)/2i = Y_L x (U-U^-1)/2i.

After two ticks, restriction to the active even C8 sublattice and unresolved
geometry orientation recovers the frozen q=2 Hamming adjacency exactly.

The normalized odd-part coefficient +/-1 is a minimal-lift kinematic result.
It is NOT the still-open coefficient of the full physical Lorentzian/history
kernel.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def shift(n: int) -> sp.Matrix:
    U = sp.zeros(n)
    for k in range(n):
        U[(k + 1) % n, k] = 1
    return U


def reflection(n: int) -> sp.Matrix:
    R = sp.zeros(n)
    for k in range(n):
        R[(-k) % n, k] = 1
    return R


def zero(M: sp.Matrix) -> bool:
    return all(sp.simplify(sp.expand_complex(x)) == 0 for x in M)


def kron(A: sp.Matrix, B: sp.Matrix) -> sp.Matrix:
    return sp.kronecker_product(A, B)


def run() -> dict[str, object]:
    n = 8
    U = shift(n)
    Uh = U.T
    Rh = reflection(n)

    I2 = sp.eye(2)
    I8 = sp.eye(8)
    X = sp.Matrix([[0, 1], [1, 0]])
    Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    Z = sp.diag(1, -1)

    Pp = (I2 + Y) / 2
    Pm = (I2 - Y) / 2

    W = kron(Pp, U) + kron(Pm, Uh)
    Ytot = kron(Y, I8)
    Rtot = kron(Z, Rh)

    Ch = ((U - Uh) / (2 * sp.I)).applyfunc(
        lambda x: sp.simplify(sp.expand_complex(x))
    )
    Heven = ((U + Uh) / 2).applyfunc(
        lambda x: sp.simplify(sp.expand_complex(x))
    )
    Hlock = kron(Y, Ch)

    unitary = zero(W.H * W - sp.eye(16))
    orientation_conserved = zero(W * Ytot - Ytot * W)
    combined_reflection_even = zero(Rtot * W * Rtot - W)

    cosine_exact = zero((W + W.H) / 2 - kron(I2, Heven))
    sine_exact = zero((W - W.H) / (2 * sp.I) - Hlock)

    # Classify all deterministic nearest-neighbor choices U^(s_+) and U^(s_-)
    # in the two geometry-orientation sectors.
    valid_direction_pairs: list[list[int]] = []
    for splus in (+1, -1):
        for sminus in (+1, -1):
            Up = U if splus == 1 else Uh
            Um = U if sminus == 1 else Uh
            Wi = kron(Pp, Up) + kron(Pm, Um)
            if zero(Rtot * Wi * Rtot - Wi):
                valid_direction_pairs.append([splus, sminus])

    deterministic_classification_exact = valid_direction_pairs == [[1, -1], [-1, 1]]

    # Two history ticks map the active even sites 0,2,4,6 back to a C4 shift.
    active = [0, 2, 4, 6]
    S4 = shift(4)
    U2_active = (U ** 2).extract(active, active)
    Um2_active = (Uh ** 2).extract(active, active)
    forward_active_exact = U2_active == S4
    backward_active_exact = Um2_active == S4.T

    # Trace/sum over unresolved geometry orientation after two ticks.
    W2 = W ** 2
    # In the computational geometry basis, partial trace is the sum of the
    # two 8x8 diagonal blocks.
    Tr_geom_W2 = W2[:8, :8] + W2[8:, 8:]
    unresolved_active = Tr_geom_W2.extract(active, active)
    gray_c4_adjacency = S4 + S4.T
    unresolved_recovers_c4 = unresolved_active == gray_c4_adjacency

    # Fixed Gray order 00,01,11,10 -> binary order 00,01,10,11.
    gray_to_binary = [0, 1, 3, 2]
    B = sp.zeros(4)
    for g, b in enumerate(gray_to_binary):
        B[b, g] = 1
    binary_kernel = B * unresolved_active * B.T
    hamming = kron(X, sp.eye(2)) + kron(sp.eye(2), X)
    recovers_frozen_hamming = binary_kernel == hamming

    # Hilbert-Schmidt projection coefficients.  The unresolved even kernel has
    # zero projection on Y x C_h; the normalized sine part equals it exactly.
    denom = sp.simplify(sp.trace(Hlock.H * Hlock))
    g_hamming_num = sp.simplify(sp.trace(Hlock.H * kron(I2, Heven)))
    g_hamming = sp.simplify(g_hamming_num / denom)
    g_minimal_sine_num = sp.simplify(
        sp.trace(Hlock.H * ((W - W.H) / (2 * sp.I)))
    )
    g_minimal_sine = sp.simplify(g_minimal_sine_num / denom)

    hamming_lock_zero = sp.simplify(g_hamming) == 0
    minimal_sine_unit = sp.simplify(g_minimal_sine) == 1

    checks = {
        "controlled_history_step_is_unitary": unitary,
        "controlled_history_step_conserves_geometry_orientation": orientation_conserved,
        "controlled_history_step_is_combined_reflection_even": combined_reflection_even,
        "cosine_part_is_orientation_unresolved_even_kernel": cosine_exact,
        "sine_part_is_exact_geometry_history_lock": sine_exact,
        "deterministic_equivariant_direction_choices_are_only_opposite_pairs": deterministic_classification_exact,
        "two_ticks_forward_restrict_to_C4_shift": forward_active_exact,
        "two_ticks_backward_restrict_to_inverse_C4_shift": backward_active_exact,
        "orientation_unresolved_two_tick_kernel_is_C4_adjacency": unresolved_recovers_c4,
        "gray_to_binary_kernel_is_frozen_q2_Hamming_adjacency": recovers_frozen_hamming,
        "orientation_unresolved_Hamming_lock_coefficient_is_zero": hamming_lock_zero,
        "minimal_one_tick_sine_lock_coefficient_is_plus_one": minimal_sine_unit,
    }

    return {
        "status": "exact minimal orientation-resolved q=2 reversible-history lift",
        "passed": bool(all(checks.values())),
        "valid_deterministic_direction_pairs_splus_sminus": valid_direction_pairs,
        "definitions": {
            "W": "P_+ tensor U8 + P_- tensor U8^-1",
            "P_plus_minus": "(I +/- Y_L)/2",
            "history_even": "(U8+U8^-1)/2",
            "history_current": "(U8-U8^-1)/(2i)",
        },
        "exact_coefficients": {
            "g_YC_Hamming_orientation_unresolved": str(g_hamming),
            "g_YC_minimal_one_tick_sine_normalization": str(g_minimal_sine),
            "g_YC_minimal_absolute_value": "1",
            "g_YC_gravity": "OPEN_PHYSICAL",
        },
        "active_sublattice": active,
        "gray_to_binary_permutation": gray_to_binary,
        "checks": checks,
        "theorem": (
            "Within the deterministic nearest-neighbor permutation class, conservation of the logical geometry orientation and covariance under simultaneous geometry/history reversal force the two orientation sectors to propagate in opposite C8 directions, up to the convention for global orientation. The sine/odd part of this unique minimal lift is exactly Y_L tensor C_h, while its two-tick orientation-unresolved active quotient is exactly the frozen q=2 Hamming adjacency."
        ),
        "senior_boundary": (
            "The coefficient +/-1 belongs only to the normalized one-tick sine part of the minimal reversible history lift. The frozen undirected Hamming seed has zero Y_L tensor C_h coefficient after orientation is unresolved. The genuine gravitational g_YC remains open because the full safe Peter-Weyl Lorentzian C(K)C(K)C(V) physical-history amplitude has not yet been completed."
        ),
        "next_physical_calculation": (
            "Complete the genuine-amplitude safe Lorentzian Peter-Weyl block, construct the relational/history kernel rather than a constraint spectral surrogate, and project that kernel on the already frozen Y_L tensor C_h channel."
        ),
    }


def main() -> int:
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
