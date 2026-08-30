#!/usr/bin/env python3
"""Leakage-aware finite active-habitat master-constraint diagnostic.

This research gate uses the same three-node Euclidean graph-changing
Peter-Weyl Hamiltonians as the canonical HDA control.  It constructs the
one-hit active habitat

    P1 = span{psi0, H0 psi0, H1 psi0, H2 psi0}

and compares the safe restricted master quadratic form

    M_full = sum_v (H_v P1)^dagger (H_v P1)

with the potentially dangerous projected shortcut

    M_proj = sum_v (P1 H_v P1)^dagger (P1 H_v P1).

For an orthogonal P1 the exact identity is

    M_full - M_proj = sum_v ((1-P1) H_v P1)^dagger
                               ((1-P1) H_v P1) >= 0.

A PASS certifies only this finite diagnostic and its numerical identities.
Leakage size and kernel counts are measured outputs, not PASS targets.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import k5_peter_weyl_safe_hda_column as PW

NODES = (0, 1, 2)
JMAX2 = 5
PRUNE_TOL = 1e-8
ORTHO_TOL = 2e-9
IDENTITY_TOL = 5e-8
PSD_TOL = 5e-9
HERMITIAN_TOL = 5e-9
LEAKAGE_STATUS_TOL = 1e-8
ZERO_THRESHOLDS = (1e-8, 1e-10, 1e-12)

Sparse = dict[tuple, complex]


def inner(a: Sparse, b: Sparse) -> complex:
    if len(a) > len(b):
        a, b = b, a
        return np.conjugate(inner(a, b))
    return sum(np.conjugate(amp) * b.get(key, 0j) for key, amp in a.items())


def norm2(a: Sparse) -> float:
    return float(max(0.0, inner(a, a).real))


def norm(a: Sparse) -> float:
    return math.sqrt(norm2(a))


def add_scaled(dst: Sparse, src: Sparse, scale: complex) -> None:
    for key, amp in src.items():
        val = dst.get(key, 0j) + scale * amp
        if abs(val) > 1e-13:
            dst[key] = val
        elif key in dst:
            del dst[key]


def scaled(src: Sparse, scale: complex) -> Sparse:
    return {key: scale * amp for key, amp in src.items() if abs(scale * amp) > 1e-13}


def subtract(a: Sparse, b: Sparse) -> Sparse:
    out = dict(a)
    add_scaled(out, b, -1.0)
    return out


def apply_h(state: Sparse, node: int) -> Sparse:
    return PW.prune_state(PW.apply_H_cached_state(state, node, JMAX2), PRUNE_TOL)


def orthonormalize(named_vectors: list[tuple[str, Sparse]]) -> tuple[list[str], list[Sparse], dict[str, object]]:
    labels: list[str] = []
    basis: list[Sparse] = []
    dropped: list[dict[str, object]] = []

    for label, vec in named_vectors:
        w = dict(vec)
        input_norm = norm(w)
        # Two-pass modified Gram-Schmidt is intentional: the active vectors can
        # differ substantially in scale and sparse support.
        for _ in range(2):
            for q in basis:
                add_scaled(w, q, -inner(q, w))
        residual_norm = norm(w)
        if residual_norm <= 1e-11 * max(1.0, input_norm):
            dropped.append({
                "label": label,
                "input_norm": float(input_norm),
                "residual_norm": float(residual_norm),
                "reason": "linearly dependent at frozen Gram-Schmidt tolerance",
            })
            continue
        q = scaled(w, 1.0 / residual_norm)
        labels.append(label)
        basis.append(q)

    if not basis:
        gram = np.zeros((0, 0), complex)
        defect = math.inf
    else:
        gram = np.asarray([[inner(qi, qj) for qj in basis] for qi in basis], complex)
        defect = float(np.linalg.norm(gram - np.eye(len(basis)), 2))

    return labels, basis, {
        "input_vector_count": len(named_vectors),
        "basis_dimension": len(basis),
        "dropped_vectors": dropped,
        "orthonormality_operator_norm_defect": defect,
        "gram_matrix": complex_matrix_json(gram),
    }


def project(state: Sparse, basis: list[Sparse]) -> tuple[np.ndarray, Sparse]:
    coeff = np.asarray([inner(q, state) for q in basis], complex)
    out: Sparse = {}
    for c, q in zip(coeff, basis):
        if abs(c) > 1e-14:
            add_scaled(out, q, c)
    return coeff, out


def state_gram(states: list[Sparse]) -> np.ndarray:
    n = len(states)
    return np.asarray([[inner(states[i], states[j]) for j in range(n)] for i in range(n)], complex)


def hermitize(M: np.ndarray) -> np.ndarray:
    return 0.5 * (M + M.conj().T)


def rel_defect(A: np.ndarray, B: np.ndarray | None = None) -> float:
    if B is None:
        B = np.zeros_like(A)
    scale = max(float(np.linalg.norm(A, 2)) if A.size else 0.0,
                float(np.linalg.norm(B, 2)) if B.size else 0.0,
                1e-300)
    return float(np.linalg.norm(A - B, 2) / scale)


def hermitian_defect(M: np.ndarray) -> float:
    scale = max(float(np.linalg.norm(M, 2)) if M.size else 0.0, 1e-300)
    return float(np.linalg.norm(M - M.conj().T, 2) / scale)


def eigvals_hermitian(M: np.ndarray) -> np.ndarray:
    return np.linalg.eigvalsh(hermitize(M))


def op_norm_from_gram(G: np.ndarray) -> float:
    ev = eigvals_hermitian(G)
    return math.sqrt(max(0.0, float(ev[-1]))) if len(ev) else 0.0


def zero_scan(evals: np.ndarray) -> list[dict[str, object]]:
    scale = max(float(np.max(np.abs(evals))) if len(evals) else 0.0, 1e-300)
    rows = []
    for tau in ZERO_THRESHOLDS:
        rows.append({
            "relative_threshold": tau,
            "zero_count": int(np.sum(np.abs(evals) <= tau * scale)),
            "scale": scale,
        })
    return rows


def complex_matrix_json(M: np.ndarray) -> list[list[list[float]]]:
    A = np.asarray(M, complex)
    return [[[float(z.real), float(z.imag)] for z in row] for row in A]


def float_list(a: np.ndarray) -> list[float]:
    return [float(x) for x in np.asarray(a, float)]


def run() -> dict[str, object]:
    initial_key = PW.basis_full_jhalf()[0]
    seed: Sparse = {initial_key: 1.0 + 0j}

    one_hit = {v: apply_h(seed, v) for v in NODES}
    one_hit_norms = {v: norm(st) for v, st in one_hit.items()}
    one_hit_support = {v: len(st) for v, st in one_hit.items()}

    named = [("seed", seed)] + [(f"H{v}_seed", one_hit[v]) for v in NODES]
    labels, basis, ortho = orthonormalize(named)
    d = len(basis)

    node_rows: list[dict[str, object]] = []
    M_full = np.zeros((d, d), complex)
    M_proj = np.zeros((d, d), complex)
    M_leak = np.zeros((d, d), complex)
    all_finite = True
    projected_constraint_hermitian = True

    for v in NODES:
        images = [apply_h(q, v) for q in basis]
        C = np.zeros((d, d), complex)
        leaks: list[Sparse] = []
        projected_states: list[Sparse] = []

        for j, y in enumerate(images):
            coeff, py = project(y, basis)
            C[:, j] = coeff
            projected_states.append(py)
            leaks.append(subtract(y, py))

        Ygram = hermitize(state_gram(images))
        Lgram = hermitize(state_gram(leaks))
        Cgram = hermitize(C.conj().T @ C)

        node_identity_scale = max(float(np.linalg.norm(Ygram, 2)), 1e-300)
        node_identity_error = float(np.linalg.norm(Ygram - Cgram - Lgram, 2) / node_identity_scale)

        full_norm = op_norm_from_gram(Ygram)
        leak_norm = op_norm_from_gram(Lgram)
        proj_norm = float(np.linalg.norm(C, 2)) if C.size else 0.0
        leak_ratio = leak_norm / max(full_norm, 1e-300)
        c_herm = hermitian_defect(C)

        ev_y = eigvals_hermitian(Ygram)
        ev_l = eigvals_hermitian(Lgram)
        all_finite &= bool(np.isfinite(C).all() and np.isfinite(Ygram).all() and np.isfinite(Lgram).all())
        projected_constraint_hermitian &= bool(c_herm <= HERMITIAN_TOL)

        M_full += Ygram
        M_proj += Cgram
        M_leak += Lgram

        node_rows.append({
            "node": v,
            "image_supports": [len(x) for x in images],
            "projected_constraint_operator_norm": proj_norm,
            "full_action_operator_norm": full_norm,
            "leakage_operator_norm": leak_norm,
            "leakage_to_full_operator_norm_ratio": float(leak_ratio),
            "projected_constraint_Hermiticity_relative_defect": c_herm,
            "full_image_gram_min_eigenvalue": float(ev_y[0]) if len(ev_y) else 0.0,
            "leakage_gram_min_eigenvalue": float(ev_l[0]) if len(ev_l) else 0.0,
            "full_equals_projected_plus_leakage_relative_error": node_identity_error,
            "projected_constraint_matrix": complex_matrix_json(C),
        })

    M_full = hermitize(M_full)
    M_proj = hermitize(M_proj)
    M_leak = hermitize(M_leak)
    delta = hermitize(M_full - M_proj)

    eval_full = eigvals_hermitian(M_full)
    eval_proj = eigvals_hermitian(M_proj)
    eval_leak = eigvals_hermitian(M_leak)
    eval_delta = eigvals_hermitian(delta)

    scale_full = max(float(np.linalg.norm(M_full, 2)) if d else 0.0, 1e-300)
    decomposition_error = float(np.linalg.norm(delta - M_leak, 2) / scale_full)
    master_herm = hermitian_defect(M_full)
    projected_master_herm = hermitian_defect(M_proj)
    leakage_herm = hermitian_defect(M_leak)

    spec_denom = max(float(np.linalg.norm(eval_full)), 1e-300)
    spectral_distortion = float(np.linalg.norm(eval_full - eval_proj) / spec_denom)

    full_scan = zero_scan(eval_full)
    proj_scan = zero_scan(eval_proj)
    additional_projected_zeros = [
        int(p["zero_count"] - f["zero_count"])
        for f, p in zip(full_scan, proj_scan)
    ]

    max_leak_ratio = max((row["leakage_to_full_operator_norm_ratio"] for row in node_rows), default=0.0)
    leakage_present = bool(max_leak_ratio > LEAKAGE_STATUS_TOL)
    spurious_zero_detected = bool(any(x > 0 for x in additional_projected_zeros))

    min_full = float(eval_full[0]) if len(eval_full) else 0.0
    min_leak = float(eval_leak[0]) if len(eval_leak) else 0.0
    min_delta = float(eval_delta[0]) if len(eval_delta) else 0.0

    checks = {
        "active_basis_nonempty": bool(d > 0),
        "all_three_single_node_seed_actions_nonzero": bool(all(one_hit_support[v] > 0 and one_hit_norms[v] > 0 for v in NODES)),
        "active_basis_orthonormal": bool(ortho["orthonormality_operator_norm_defect"] <= ORTHO_TOL),
        "all_matrices_finite": bool(all_finite),
        "projected_constraint_matrices_Hermitian": bool(projected_constraint_hermitian),
        "full_master_Hermitian": bool(master_herm <= HERMITIAN_TOL),
        "projected_master_Hermitian": bool(projected_master_herm <= HERMITIAN_TOL),
        "leakage_master_Hermitian": bool(leakage_herm <= HERMITIAN_TOL),
        "full_master_positive_semidefinite": bool(min_full >= -PSD_TOL * scale_full),
        "leakage_master_positive_semidefinite": bool(min_leak >= -PSD_TOL * scale_full),
        "master_difference_positive_semidefinite": bool(min_delta >= -PSD_TOL * scale_full),
        "exact_master_leakage_decomposition": bool(decomposition_error <= IDENTITY_TOL),
        "all_node_decompositions_hold": bool(all(row["full_equals_projected_plus_leakage_relative_error"] <= IDENTITY_TOL for row in node_rows)),
    }
    passed = bool(all(checks.values()))

    if not passed:
        science_status = "ACTIVE_HABITAT_MASTER_DIAGNOSTIC_NUMERICAL_FAIL"
    elif leakage_present and spurious_zero_detected:
        science_status = "LEAKAGE_PRESENT_PROJECTED_MASTER_CREATES_EXTRA_ZERO_MODES"
    elif leakage_present:
        science_status = "LEAKAGE_PRESENT_PROJECTED_MASTER_NOT_EQUIVALENT"
    else:
        science_status = "ONE_HIT_HABITAT_CLOSED_AT_FROZEN_TOLERANCE"

    return {
        "status": "leakage-aware finite active-habitat master-constraint diagnostic",
        "science_status": science_status,
        "passed": passed,
        "nodes": list(NODES),
        "Jmax": JMAX2 / 2,
        "prune_tolerance": PRUNE_TOL,
        "active_habitat_definition": "span{psi0,H0 psi0,H1 psi0,H2 psi0}",
        "active_basis_labels": labels,
        "active_basis": ortho,
        "one_hit_support": {str(k): int(v) for k, v in one_hit_support.items()},
        "one_hit_norm": {str(k): float(v) for k, v in one_hit_norms.items()},
        "node_diagnostics": node_rows,
        "master": {
            "full_restricted_definition": "sum_v (H_v P1)^dagger (H_v P1)",
            "projected_shortcut_definition": "sum_v (P1 H_v P1)^dagger(P1 H_v P1)",
            "leakage_definition": "sum_v ((1-P1)H_vP1)^dagger((1-P1)H_vP1)",
            "full_eigenvalues": float_list(eval_full),
            "projected_eigenvalues": float_list(eval_proj),
            "leakage_eigenvalues": float_list(eval_leak),
            "difference_eigenvalues": float_list(eval_delta),
            "full_zero_mode_scan": full_scan,
            "projected_zero_mode_scan": proj_scan,
            "additional_projected_zero_modes": additional_projected_zeros,
            "spurious_projected_zero_detected": spurious_zero_detected,
            "spectral_distortion_full_vs_projected": spectral_distortion,
            "max_node_leakage_ratio": float(max_leak_ratio),
            "leakage_present": leakage_present,
            "decomposition_relative_error": decomposition_error,
            "full_Hermiticity_relative_defect": master_herm,
            "projected_Hermiticity_relative_defect": projected_master_herm,
            "leakage_Hermiticity_relative_defect": leakage_herm,
            "M_full": complex_matrix_json(M_full),
            "M_projected": complex_matrix_json(M_proj),
            "M_leakage": complex_matrix_json(M_leak),
        },
        "checks": checks,
        "interpretation": (
            "M_full uses the complete graph/spin-changing H_v images before contraction back to the finite active domain. "
            "M_projected discards orthogonal leakage first. Their difference is an independently accumulated positive leakage Gram matrix."
        ),
        "next_gate": (
            "If leakage is material, enlarge the active habitat with the measured two-hit output directions and repeat the same construction. "
            "Only after leakage and normalized physical matrix elements stabilize across depth/refinement should a theory-specific physical-projector claim be considered."
        ),
        "claim_boundary": (
            "Finite three-node Euclidean one-hit habitat diagnostic only. It is not the full five-node or Lorentzian constraint family, "
            "not a continuum rigging map, not physical time, not a graviton propagator, and not a frozen six-Wilson prediction."
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
