#!/usr/bin/env python3
"""Parameter-free local bridge from the frozen q=2 route labels to quantum geometry.

The frozen microscopic rule labels the four routes in each q=2 rewrite cell by
Z2^2 bit strings.  Z2^2 has exactly three non-trivial real characters.  Evaluating
those characters on the four route labels gives four vectors in R^3.  This gate
checks that they are exactly the regular-tetrahedron flux frame, encodes those
unit fluxes as face qubits, and applies the exact four-spin Gauss-singlet
projection already used by the canonical spatial geometry gate.

No target tetrahedron, continuous coordinate, fitted angle, random B field or
external physical constant enters this construction.  What is still assumed is
the canonical quantum lift that identifies the three traceless Hermitian Pauli
directions with the three character components; that identification is unique
up to an O(3) basis change/gauge convention.
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

import spatial_qubit_geometry_gate as SQ


def walsh_character(mask: int, bits: tuple[int, int]) -> int:
    """Real character chi_mask(bits)=(-1)^(mask dot bits) for Z2^2."""
    parity = ((mask & 1) * bits[0] + ((mask >> 1) & 1) * bits[1]) & 1
    return 1 if parity == 0 else -1


def route_flux_frame() -> tuple[list[tuple[int, int]], np.ndarray]:
    labels = list(itertools.product((0, 1), repeat=2))
    # The three non-zero character masks of Z2^2.  Any GL(2,2) relabeling only
    # permutes these axes, hence changes the flux frame by an orthogonal basis
    # convention rather than a fitted physical parameter.
    masks = (1, 2, 3)
    raw = np.array([[walsh_character(m, b) for m in masks] for b in labels], float)
    return labels, raw / math.sqrt(3.0)


def spinor_from_bloch(n: np.ndarray) -> np.ndarray:
    op = sum((float(n[a]) * SQ.PAULI[a] for a in range(3)), np.zeros((2, 2), complex))
    values, vectors = np.linalg.eigh(op)
    return vectors[:, int(np.argmax(values))]


def kron_all(vectors: list[np.ndarray]) -> np.ndarray:
    out = np.array([1.0 + 0.0j])
    for v in vectors:
        out = np.kron(out, v)
    return out


def logical_bloch(coeff: np.ndarray) -> np.ndarray:
    rho = np.outer(coeff, coeff.conj())
    return np.array([np.trace(rho @ p).real for p in SQ.PAULI], float)


def run() -> dict[str, object]:
    labels, normals = route_flux_frame()
    gram = normals @ normals.T
    target_gram = np.full((4, 4), -1.0 / 3.0)
    np.fill_diagonal(target_gram, 1.0)
    closure = normals.sum(axis=0)
    frame_cov = normals.T @ normals

    # Four unit Bloch vectors -> four pure face-qubit density matrices.
    rhos = []
    purity_errors = []
    positivity_floor = 1.0
    decoded = []
    spinors = []
    for n in normals:
        rho = 0.5 * (SQ.I2 + sum((n[a] * SQ.PAULI[a] for a in range(3)), np.zeros((2, 2), complex)))
        rhos.append(rho)
        purity_errors.append(float(np.linalg.norm(rho @ rho - rho)))
        positivity_floor = min(positivity_floor, float(np.linalg.eigvalsh(rho).min()))
        decoded.append(np.array([np.trace(rho @ p).real for p in SQ.PAULI]))
        spinors.append(spinor_from_bloch(n))
    decoded = np.asarray(decoded, float)

    # Exact Gauss reduction of the binary-derived coherent product state.
    B = SQ.logical_basis()
    Psinglet = B @ B.conj().T
    psi_product = kron_all(spinors)
    psi_projected = Psinglet @ psi_product
    singlet_weight = float(np.vdot(psi_projected, psi_projected).real)
    if singlet_weight <= 1e-15:
        raise RuntimeError("binary-derived face state has zero Gauss-singlet support")
    coeff = (B.conj().T @ psi_product) / math.sqrt(singlet_weight)
    bloch = logical_bloch(coeff)

    # The exact geometry-qubit volume operator is Q_L=(sqrt(3)/4)Y_L.
    oriented_volume_expectation = float(math.sqrt(3.0) / 4.0 * bloch[1])
    oriented_volume_target = math.sqrt(3.0) / 4.0

    # Interpret the four closed equal-area fluxes as tetrahedral face vectors.
    # The existing exact reconstruction must return a regular tetrahedron.
    A = SQ.reconstruct_edges(normals)
    vertices = [np.zeros(3), A[:, 0], A[:, 1], A[:, 2]]
    lengths = np.array([
        np.linalg.norm(vertices[j] - vertices[i])
        for i, j in itertools.combinations(range(4), 2)
    ])
    edge_spread = float((lengths.max() - lengths.min()) / lengths.mean())

    # A reversed ordering is an explicit orientation control: the geometric
    # shape is unchanged while the logical Y/volume sign flips.
    reversed_spinors = [spinors[0], spinors[2], spinors[1], spinors[3]]
    psi_rev = kron_all(reversed_spinors)
    proj_rev = Psinglet @ psi_rev
    w_rev = float(np.vdot(proj_rev, proj_rev).real)
    coeff_rev = (B.conj().T @ psi_rev) / math.sqrt(w_rev)
    bloch_rev = logical_bloch(coeff_rev)

    checks = {
        "four_route_labels": len(labels) == 4,
        "three_nontrivial_characters": normals.shape == (4, 3),
        "exact_flux_closure": float(np.linalg.norm(closure)) < 1e-14,
        "regular_tetrahedron_gram": float(np.linalg.norm(gram - target_gram)) < 1e-14,
        "isotropic_character_frame": float(np.linalg.norm(frame_cov - (4.0 / 3.0) * np.eye(3))) < 1e-14,
        "face_qubits_pure": max(purity_errors) < 1e-14,
        "face_qubits_positive": positivity_floor > -1e-14,
        "face_qubit_decode_exact": float(np.linalg.norm(decoded - normals)) < 1e-14,
        "nonzero_gauss_singlet_support": abs(singlet_weight - 2.0 / 9.0) < 1e-13,
        "geometry_qubit_is_volume_eigenstate": float(np.linalg.norm(bloch - np.array([0.0, 1.0, 0.0]))) < 1e-12,
        "regular_tetrahedron_reconstruction": edge_spread < 1e-12,
        "orientation_reversal_flips_volume": float(np.linalg.norm(bloch_rev - np.array([0.0, -1.0, 0.0]))) < 1e-12,
    }

    return {
        "status": "exact local q=2 Walsh-character -> tetrahedral face-qubit -> Gauss geometry-qubit bridge",
        "passed": bool(all(checks.values())),
        "microscopic_rule": "same frozen q=2 route labels 00,01,10,11 with Hamming adjacency",
        "route_labels": [list(x) for x in labels],
        "nontrivial_character_masks": [1, 2, 3],
        "unit_flux_vectors": normals.tolist(),
        "flux_closure_norm": float(np.linalg.norm(closure)),
        "flux_gram": gram.tolist(),
        "character_frame_covariance": frame_cov.tolist(),
        "face_qubit_purity_max_error": max(purity_errors),
        "face_qubit_min_eigenvalue": positivity_floor,
        "gauss_singlet_weight": singlet_weight,
        "logical_geometry_bloch": bloch.tolist(),
        "logical_oriented_volume_expectation": oriented_volume_expectation,
        "logical_oriented_volume_target": oriented_volume_target,
        "reconstructed_tetrahedron_edge_lengths": lengths.tolist(),
        "reconstructed_edge_relative_spread": edge_spread,
        "orientation_reversed_logical_bloch": bloch_rev.tolist(),
        "checks": checks,
        "claim_boundary": (
            "This closes the local carrier map inside the declared canonical quantum lift: the q=2 route bits themselves generate the tetrahedral flux frame and a nonzero Gauss-singlet geometry qubit. "
            "It does not yet prove that the full unitary graph-changing dynamics drives arbitrary states into a semiclassical coarse B-field phase."
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
