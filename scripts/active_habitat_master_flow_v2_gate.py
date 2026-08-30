#!/usr/bin/env python3
"""Preregistered depth-2 leakage-aware master-gap flow.

The construction is frozen by ACTIVE_HABITAT_MASTER_FLOW_V2_PREREGISTRATION.md.
It uses nested finite habitats P0 subset P1 subset P2 and evaluates the master
quadratic form from complete graph-changing images H_v q_i before any projection.

A PASS certifies numerical identities, nesting, positivity and Rayleigh-Ritz
structure only. Gap closure, zero modes and leakage reduction are measured
outputs and are deliberately not acceptance targets.
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

import active_habitat_master_constraint_gate as V1
import k5_peter_weyl_safe_hda_column as PW

NODES = V1.NODES
ORTHO_TOL = V1.ORTHO_TOL
IDENTITY_TOL = V1.IDENTITY_TOL
PSD_TOL = V1.PSD_TOL
HERMITIAN_TOL = V1.HERMITIAN_TOL
LEAKAGE_STATUS_TOL = V1.LEAKAGE_STATUS_TOL
ZERO_THRESHOLDS = V1.ZERO_THRESHOLDS
RITZ_TOL = 5e-8
CONSTRUCTION_TOL = 5e-8

Sparse = V1.Sparse


def matrix_json(M: np.ndarray) -> list[list[list[float]]]:
    return V1.complex_matrix_json(M)


def float_list(a: np.ndarray) -> list[float]:
    return V1.float_list(a)


def zero_scan(evals: np.ndarray) -> list[dict[str, object]]:
    return V1.zero_scan(evals)


def orthonormal_defect(basis: list[Sparse]) -> float:
    if not basis:
        return math.inf
    G = V1.state_gram(basis)
    return float(np.linalg.norm(G - np.eye(len(basis)), 2))


def depth_master(labels: list[str], basis: list[Sparse]) -> dict[str, object]:
    d = len(basis)
    M_full = np.zeros((d, d), complex)
    M_proj = np.zeros((d, d), complex)
    M_leak = np.zeros((d, d), complex)
    node_rows: list[dict[str, object]] = []
    all_finite = True

    for v in NODES:
        images = [V1.apply_h(q, v) for q in basis]
        C = np.zeros((d, d), complex)
        leaks: list[Sparse] = []

        for j, y in enumerate(images):
            coeff, py = V1.project(y, basis)
            C[:, j] = coeff
            leaks.append(V1.subtract(y, py))

        Ygram = V1.hermitize(V1.state_gram(images))
        Cgram = V1.hermitize(C.conj().T @ C)
        Lgram = V1.hermitize(V1.state_gram(leaks))

        full_norm = V1.op_norm_from_gram(Ygram)
        leak_norm = V1.op_norm_from_gram(Lgram)
        proj_norm = float(np.linalg.norm(C, 2)) if C.size else 0.0
        leakage_ratio = leak_norm / max(full_norm, 1e-300)
        identity_scale = max(float(np.linalg.norm(Ygram, 2)), 1e-300)
        identity_error = float(np.linalg.norm(Ygram - Cgram - Lgram, 2) / identity_scale)

        ev_y = V1.eigvals_hermitian(Ygram)
        ev_l = V1.eigvals_hermitian(Lgram)
        all_finite &= bool(np.isfinite(C).all() and np.isfinite(Ygram).all() and np.isfinite(Lgram).all())

        M_full += Ygram
        M_proj += Cgram
        M_leak += Lgram

        node_rows.append({
            "node": int(v),
            "image_supports": [len(x) for x in images],
            "full_action_operator_norm": float(full_norm),
            "projected_constraint_operator_norm": float(proj_norm),
            "leakage_operator_norm": float(leak_norm),
            "leakage_to_full_operator_norm_ratio": float(leakage_ratio),
            "projected_constraint_Hermiticity_relative_defect": V1.hermitian_defect(C),
            "full_image_gram_min_eigenvalue": float(ev_y[0]) if len(ev_y) else 0.0,
            "leakage_gram_min_eigenvalue": float(ev_l[0]) if len(ev_l) else 0.0,
            "full_equals_projected_plus_leakage_relative_error": identity_error,
        })

    M_full = V1.hermitize(M_full)
    M_proj = V1.hermitize(M_proj)
    M_leak = V1.hermitize(M_leak)
    delta = V1.hermitize(M_full - M_proj)

    eval_full = V1.eigvals_hermitian(M_full)
    eval_proj = V1.eigvals_hermitian(M_proj)
    eval_leak = V1.eigvals_hermitian(M_leak)
    eval_delta = V1.eigvals_hermitian(delta)

    scale = max(float(np.linalg.norm(M_full, 2)) if d else 0.0, 1e-300)
    decomposition_error = float(np.linalg.norm(delta - M_leak, 2) / scale)
    spectral_denom = max(float(np.linalg.norm(eval_full)), 1e-300)
    spectral_distortion = float(np.linalg.norm(eval_full - eval_proj) / spectral_denom)
    max_leakage_ratio = max((r["leakage_to_full_operator_norm_ratio"] for r in node_rows), default=0.0)

    checks = {
        "all_matrices_finite": bool(all_finite),
        "full_master_Hermitian": bool(V1.hermitian_defect(M_full) <= HERMITIAN_TOL),
        "projected_master_Hermitian": bool(V1.hermitian_defect(M_proj) <= HERMITIAN_TOL),
        "leakage_master_Hermitian": bool(V1.hermitian_defect(M_leak) <= HERMITIAN_TOL),
        "full_master_positive_semidefinite": bool((float(eval_full[0]) if len(eval_full) else 0.0) >= -PSD_TOL * scale),
        "leakage_master_positive_semidefinite": bool((float(eval_leak[0]) if len(eval_leak) else 0.0) >= -PSD_TOL * scale),
        "master_difference_positive_semidefinite": bool((float(eval_delta[0]) if len(eval_delta) else 0.0) >= -PSD_TOL * scale),
        "exact_master_leakage_decomposition": bool(decomposition_error <= IDENTITY_TOL),
        "all_node_decompositions_hold": bool(all(r["full_equals_projected_plus_leakage_relative_error"] <= IDENTITY_TOL for r in node_rows)),
    }

    return {
        "dimension": d,
        "basis_labels": labels,
        "orthonormality_operator_norm_defect": orthonormal_defect(basis),
        "node_diagnostics": node_rows,
        "full_eigenvalues": float_list(eval_full),
        "projected_eigenvalues": float_list(eval_proj),
        "leakage_eigenvalues": float_list(eval_leak),
        "difference_eigenvalues": float_list(eval_delta),
        "full_zero_mode_scan": zero_scan(eval_full),
        "projected_zero_mode_scan": zero_scan(eval_proj),
        "minimum_full_eigenvalue": float(eval_full[0]) if len(eval_full) else 0.0,
        "maximum_full_eigenvalue": float(eval_full[-1]) if len(eval_full) else 0.0,
        "spectral_distortion_full_vs_projected": spectral_distortion,
        "max_node_leakage_ratio": float(max_leakage_ratio),
        "leakage_present": bool(max_leakage_ratio > LEAKAGE_STATUS_TOL),
        "decomposition_relative_error": decomposition_error,
        "M_full": matrix_json(M_full),
        "M_projected": matrix_json(M_proj),
        "M_leakage": matrix_json(M_leak),
        "checks": checks,
        "_M_full_array": M_full,
    }


def run() -> dict[str, object]:
    initial_key = PW.basis_full_jhalf()[0]
    seed: Sparse = {initial_key: 1.0 + 0j}

    # P0 is fixed by the seed.
    labels0, basis0, ortho0 = V1.orthonormalize([("seed", seed)])

    # P1 exactly reproduces the preregistered one-hit construction.
    one_hit = {v: V1.apply_h(seed, v) for v in NODES}
    named1 = [("seed", seed)] + [(f"H{v}_seed", one_hit[v]) for v in NODES]
    labels1, basis1, ortho1 = V1.orthonormalize(named1)

    # P2 is deterministic: retain the full ordered P1 basis first, then append
    # every H_v q_i^(1) in basis order and node order. No spectral selection.
    named2: list[tuple[str, Sparse]] = [(f"P1::{label}", q) for label, q in zip(labels1, basis1)]
    construction_images: list[tuple[str, Sparse]] = []
    for i, (label, q) in enumerate(zip(labels1, basis1)):
        for v in NODES:
            y = V1.apply_h(q, v)
            image_label = f"H{v}_P1[{i}]::{label}"
            construction_images.append((image_label, y))
            named2.append((image_label, y))
    labels2, basis2, ortho2 = V1.orthonormalize(named2)

    depth0 = depth_master(labels0, basis0)
    depth1 = depth_master(labels1, basis1)
    depth2 = depth_master(labels2, basis2)

    # Because P1 vectors are inserted first, the first dim(P1) P2 basis vectors
    # must reproduce P1 up to roundoff.
    d1 = len(basis1)
    leading_overlap = np.asarray(
        [[V1.inner(basis1[i], basis2[j]) for j in range(d1)] for i in range(d1)],
        complex,
    )
    retained_basis_defect = float(np.linalg.norm(leading_overlap - np.eye(d1), 2))

    M1 = depth1.pop("_M_full_array")
    M2 = depth2.pop("_M_full_array")
    depth0.pop("_M_full_array")
    principal_scale = max(float(np.linalg.norm(M1, 2)), 1e-300)
    principal_block_defect = float(np.linalg.norm(M2[:d1, :d1] - M1, 2) / principal_scale)

    # Every H_v q_i^(1) was explicitly included in the spanning list for P2.
    construction_rows = []
    max_construction_relative_residual = 0.0
    for label, y in construction_images:
        _, py = V1.project(y, basis2)
        residual = V1.subtract(y, py)
        rel = V1.norm(residual) / max(V1.norm(y), 1e-300)
        max_construction_relative_residual = max(max_construction_relative_residual, rel)
        construction_rows.append({
            "label": label,
            "support": len(y),
            "relative_residual_against_P2": float(rel),
        })

    lam0 = float(depth0["minimum_full_eigenvalue"])
    lam1 = float(depth1["minimum_full_eigenvalue"])
    lam2 = float(depth2["minimum_full_eigenvalue"])
    ritz_scale = max(abs(lam1), abs(lam2), 1e-300)
    ritz_relative_violation = max(0.0, lam2 - lam1) / ritz_scale

    ratio10 = lam1 / lam0 if abs(lam0) > 1e-300 else None
    ratio21 = lam2 / lam1 if abs(lam1) > 1e-300 else None

    checks = {
        "P0_nonempty_and_orthonormal": bool(len(basis0) > 0 and ortho0["orthonormality_operator_norm_defect"] <= ORTHO_TOL),
        "P1_nonempty_and_orthonormal": bool(len(basis1) > 0 and ortho1["orthonormality_operator_norm_defect"] <= ORTHO_TOL),
        "P2_nonempty_and_orthonormal": bool(len(basis2) > 0 and ortho2["orthonormality_operator_norm_defect"] <= ORTHO_TOL),
        "P1_retained_as_leading_P2_basis": bool(retained_basis_defect <= IDENTITY_TOL),
        "P1_full_master_is_P2_principal_block": bool(principal_block_defect <= IDENTITY_TOL),
        "all_P1_one_step_images_lie_in_P2_by_construction": bool(max_construction_relative_residual <= CONSTRUCTION_TOL),
        "rayleigh_ritz_minimum_nonincreasing": bool(ritz_relative_violation <= RITZ_TOL),
        "P0_master_checks_pass": bool(all(depth0["checks"].values())),
        "P1_master_checks_pass": bool(all(depth1["checks"].values())),
        "P2_master_checks_pass": bool(all(depth2["checks"].values())),
    }
    passed = bool(all(checks.values()))

    zero2 = int(depth2["full_zero_mode_scan"][1]["zero_count"]) > 0
    leak2 = bool(depth2["leakage_present"])
    if not passed:
        science_status = "DEPTH2_MASTER_FLOW_NUMERICAL_OR_VARIATIONAL_FAIL"
    elif zero2 and leak2:
        science_status = "DEPTH2_LEAKAGE_PRESENT_FINITE_ZERO_CANDIDATE_NOT_PHYSICAL"
    elif zero2:
        science_status = "DEPTH2_CLOSED_FINITE_ZERO_CANDIDATE_NOT_PHYSICAL"
    elif leak2:
        science_status = "DEPTH2_LEAKAGE_PRESENT_GAPPED"
    else:
        science_status = "DEPTH2_CLOSED_GAPPED"

    return {
        "status": "preregistered deterministic depth-2 active-habitat master-gap flow",
        "science_status": science_status,
        "passed": passed,
        "nodes": list(NODES),
        "Jmax": V1.JMAX2 / 2,
        "prune_tolerance": V1.PRUNE_TOL,
        "habitat_definitions": {
            "P0": "span{psi0}",
            "P1": "span{psi0,H0 psi0,H1 psi0,H2 psi0}",
            "P2": "span(P1 union {H_v q_i^(1) for every q_i^(1) in P1 and v=0,1,2})",
        },
        "basis_construction": {
            "P0": ortho0,
            "P1": ortho1,
            "P2": ortho2,
            "P1_retained_basis_overlap_defect": retained_basis_defect,
            "P1_to_P2_construction_image_max_relative_residual": max_construction_relative_residual,
            "P1_to_P2_construction_images": construction_rows,
        },
        "depths": {
            "P0": depth0,
            "P1": depth1,
            "P2": depth2,
        },
        "master_gap_flow": {
            "lambda_min_P0": lam0,
            "lambda_min_P1": lam1,
            "lambda_min_P2": lam2,
            "lambda_min_ratio_P1_over_P0": ratio10,
            "lambda_min_ratio_P2_over_P1": ratio21,
            "rayleigh_ritz_relative_violation": float(ritz_relative_violation),
            "P1_master_principal_block_relative_defect": principal_block_defect,
        },
        "checks": checks,
        "interpretation": (
            "The full-image master quadratic form is followed across a deterministic nested active cone. "
            "The minimum Ritz value may decrease with depth; neither gap closure nor leakage reduction is required for PASS."
        ),
        "next_gate": (
            "If depth-2 remains materially leaky, preregister a depth-3 or compressed Krylov-cone extension before inspecting its result. "
            "A physical-projector claim additionally requires the intended Lorentzian/full-node constraint family and refinement stability."
        ),
        "claim_boundary": (
            "Finite three-node Euclidean depth-2 Ritz diagnostic only; not a continuum rigging map, not physical time, not a graviton propagator, "
            "not a six-Wilson prediction, and no Hamiltonian-constraint eigenvalue is identified with physical omega."
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
