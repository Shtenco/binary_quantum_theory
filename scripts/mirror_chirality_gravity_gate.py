#!/usr/bin/env python3
"""Finite mirror/chirality gate for the binary SU(2) geometry branch.

The gate separates four distinct statements that are often conflated:

1. mirror/orientation reversal of the logical geometry qubit;
2. invariance of metric/shape observables under that reversal;
3. conjugation of an oriented phase theta -> -theta (including +/- pi);
4. anomaly sign reversal for a conjugate representation.

It deliberately does NOT claim that antimatter has negative energy or that the
current candidate theory produces antigravity.  Instead it provides a sharp
falsifier: in the present mirror-even geometry sector, orientation alone does
not change the metric.  A gravity-sign flip would require an additional
parity-odd gravitational response that must separately preserve the HDA.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def cubic_anomaly_tensor(generators: list[np.ndarray]) -> np.ndarray:
    """d^{abc}=Tr[T^a {T^b,T^c}] for an arbitrary finite representation."""
    n = len(generators)
    out = np.empty((n, n, n), dtype=complex)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                TbTc = generators[b] @ generators[c] + generators[c] @ generators[b]
                out[a, b, c] = np.trace(generators[a] @ TbTc)
    return out


def run(trials: int = 256, seed: int = 20260814) -> dict:
    rng = np.random.default_rng(seed)

    I = np.eye(2, dtype=complex)
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)

    # Frozen exact logical-qubit geometry relations from
    # SPATIAL_QUBIT_GEOMETRY_BRIDGE.md.
    Q = (math.sqrt(3.0) / 4.0) * Y
    S12 = -0.25 * I - 0.5 * Z
    S13 = -0.25 * I + 0.25 * Z - (math.sqrt(3.0) / 4.0) * X

    # In the real singlet basis, mirror is represented by complex conjugation.
    # It reverses oriented phases i->-i, hence Y->-Y, while X,Z are even.
    mirror = np.conjugate
    algebra_errors = {
        "X_even": float(np.linalg.norm(mirror(X) - X)),
        "Z_even": float(np.linalg.norm(mirror(Z) - Z)),
        "Y_odd": float(np.linalg.norm(mirror(Y) + Y)),
        "Q_oriented_volume_odd": float(np.linalg.norm(mirror(Q) + Q)),
        "S12_shape_even": float(np.linalg.norm(mirror(S12) - S12)),
        "S13_shape_even": float(np.linalg.norm(mirror(S13) - S13)),
        "Q_squared_even": float(np.linalg.norm(mirror(Q @ Q) - Q @ Q)),
    }

    evals, evecs = np.linalg.eigh(Q)
    v_minus = evecs[:, 0]
    v_plus = evecs[:, 1]
    mirror_state_swap_overlap = float(abs(np.vdot(v_minus, np.conjugate(v_plus))))
    shape_pair_errors = {
        "S12": float(abs(np.vdot(v_plus, S12 @ v_plus) - np.vdot(v_minus, S12 @ v_minus))),
        "S13": float(abs(np.vdot(v_plus, S13 @ v_plus) - np.vdot(v_minus, S13 @ v_minus))),
        "absolute_Q": float(
            abs(abs(np.vdot(v_plus, Q @ v_plus)) - abs(np.vdot(v_minus, Q @ v_minus)))
        ),
    }

    # Independent geometric mirror check on random tetrahedra.
    # A' = R A with det R=-1 flips orientation but leaves A^T A invariant.
    R = np.diag([-1.0, 1.0, 1.0])
    max_metric_gram_error = 0.0
    max_abs_volume_error = 0.0
    max_orientation_flip_error = 0.0
    max_face_flux_gram_error = 0.0
    valid = 0
    attempts = 0
    while valid < trials and attempts < 20 * trials:
        attempts += 1
        A = rng.normal(size=(3, 3))
        detA = float(np.linalg.det(A))
        if abs(detA) < 0.15:
            continue
        Ap = R @ A

        G = A.T @ A
        Gp = Ap.T @ Ap
        max_metric_gram_error = max(max_metric_gram_error, float(np.linalg.norm(Gp - G)))
        max_abs_volume_error = max(
            max_abs_volume_error,
            float(abs(abs(np.linalg.det(Ap)) - abs(detA))),
        )
        max_orientation_flip_error = max(
            max_orientation_flip_error,
            float(abs(np.linalg.det(Ap) + detA)),
        )

        a, b, c = A[:, 0], A[:, 1], A[:, 2]
        ap, bp, cp = Ap[:, 0], Ap[:, 1], Ap[:, 2]
        E = np.column_stack(
            [0.5 * np.cross(b, c), 0.5 * np.cross(c, a), 0.5 * np.cross(a, b)]
        )
        Ep = np.column_stack(
            [0.5 * np.cross(bp, cp), 0.5 * np.cross(cp, ap), 0.5 * np.cross(ap, bp)]
        )
        max_face_flux_gram_error = max(
            max_face_flux_gram_error,
            float(np.linalg.norm(Ep.T @ Ep - E.T @ E)),
        )
        valid += 1

    # "Mirror pi" has a precise interpretation as orientation of phase, not a
    # reversed decimal expansion.  Complex conjugation sends theta -> -theta.
    thetas = np.linspace(-math.pi, math.pi, 33)
    phase_conjugation_error = float(
        max(abs(np.conjugate(np.exp(1j * t)) - np.exp(-1j * t)) for t in thetas)
    )
    pi_endpoint_error = float(abs(np.exp(1j * math.pi) - np.exp(-1j * math.pi)))

    # Exact anomaly-sign identity, stress-tested on deterministic Hermitian
    # matrices: for T_bar^a = -(T_R^a)^T, d_bar^{abc} = -d_R^{abc}.
    generators: list[np.ndarray] = []
    for _ in range(3):
        M = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
        generators.append(0.5 * (M + M.conj().T))
    anomaly_R = cubic_anomaly_tensor(generators)
    conjugate_generators = [-T.T for T in generators]
    anomaly_Rbar = cubic_anomaly_tensor(conjugate_generators)
    conjugate_pair_anomaly_cancel_error = float(np.linalg.norm(anomaly_R + anomaly_Rbar))

    # Phenomenological orientation-odd gravity bookkeeping.
    # a_+ = a_even + a_odd is calibrated to the observed same-branch g_N.
    # Therefore a_- / g_N = 1 - 2 f, f=a_odd/g_N.
    # Existing mirror-even geometry corresponds to f=0.
    antigravity_thresholds = {
        "definition": "f = a_odd / g_N after calibrating a_plus = g_N",
        "existing_mirror_even_geometry_f": 0.0,
        "mirror_branch_ratio_at_f0": 1.0,
        "complete_screening_f": 0.5,
        "repulsion_requires_f_greater_than": 0.5,
        "equal_magnitude_repulsion_f": 1.0,
        "formula": "a_minus/g_N = 1 - 2 f",
    }

    passed = (
        valid == trials
        and max(algebra_errors.values()) < 1e-12
        and mirror_state_swap_overlap > 1.0 - 1e-12
        and max(shape_pair_errors.values()) < 1e-12
        and max_metric_gram_error < 1e-12
        and max_abs_volume_error < 1e-12
        and max_orientation_flip_error < 1e-12
        and max_face_flux_gram_error < 1e-12
        and phase_conjugation_error < 1e-14
        and pi_endpoint_error < 1e-14
        and conjugate_pair_anomaly_cancel_error < 1e-11
    )

    return {
        "status": "mirror/chirality finite geometry and anomaly sign gate",
        "passed": bool(passed),
        "seed": seed,
        "trials": trials,
        "logical_qubit": {
            "Q_eigenvalues": [float(x) for x in evals],
            "algebra_errors": algebra_errors,
            "mirror_state_swap_overlap": mirror_state_swap_overlap,
            "shape_pair_errors": shape_pair_errors,
            "interpretation": (
                "Mirror complex conjugation flips the oriented Y/Q coordinate while preserving "
                "the two shape coordinates and absolute-volume information."
            ),
        },
        "tetrahedral_mirror": {
            "max_metric_gram_error": max_metric_gram_error,
            "max_abs_volume_error": max_abs_volume_error,
            "max_orientation_flip_error": max_orientation_flip_error,
            "max_face_flux_gram_error": max_face_flux_gram_error,
            "interpretation": (
                "An improper orthogonal reflection reverses det(A) but preserves the metric Gram "
                "matrix, absolute volume and face-flux Gram matrix."
            ),
        },
        "oriented_phase": {
            "phase_conjugation_error": phase_conjugation_error,
            "pi_endpoint_error": pi_endpoint_error,
            "interpretation": (
                "The rigorous mirror analogue of 'pi runs the other way' is theta->-theta or "
                "exp(i theta)->exp(-i theta); pi itself and its decimal digits do not change."
            ),
        },
        "conjugate_representation_anomaly": {
            "cubic_anomaly_cancel_error": conjugate_pair_anomaly_cancel_error,
            "identity": "d(Rbar) = -d(R), so an exact R plus Rbar mirror pair cancels the perturbative cubic gauge anomaly.",
            "scope": "This is not a derivation of the Standard Model spectrum or of all global anomalies.",
        },
        "orientation_odd_gravity_bookkeeping": antigravity_thresholds,
        "gravity_result": (
            "Within the currently tested mirror-even metric sector, orientation reversal alone gives "
            "no g00 sign flip and hence no antigravity.  Antigravity requires a new parity-odd or "
            "multi-metric response and a separate HDA-closure test."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trials", type=int, default=256)
    parser.add_argument("--seed", type=int, default=20260814)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    out = run(args.trials, args.seed)
    text = json.dumps(out, ensure_ascii=False, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
