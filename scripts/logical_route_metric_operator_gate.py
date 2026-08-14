#!/usr/bin/env python3
"""Logical geometry-qubit content of the route-normal flux metric.

The current route-normal gates reconstruct a positive metric from flux Gram
expectation values. In the all-j=1/2 four-valent singlet sector the relevant
flux scalar operators can be represented exactly on one logical geometry qubit.

This gate computes the 2x2 logical matrix of J_leg0.J_leg2 directly from the
Peter-Weyl intertwiners, decomposes it into I,X,Y,Z, and constructs

    Q(p) = p_a Q^{ab} p_b

for the two route legs used by peter_weyl_route_dressed_local_gate.py.

It then compares:

A. expectation-first route normal:
       omega_K(theta)=sqrt(<K|Q(p)|K>)
   which mirrors the current finite gate's diagonal-metric expectation logic;

B. operator-first route normal:
       Omega(theta)=sqrt_operator(Q(p))
   followed by angular averaging over route direction theta.

The operator-first branch is a kinematic ordering control, not yet the frozen
route Hamiltonian ordering. The result is intentionally asymmetric between the
two orderings: the current expectation-first isotropic angular average restores
K=0/K=2 equality, whereas the operator-first square-root average retains a
finite X/Z shape-plane component. This makes operator ordering a genuine open
quantized-route question rather than evidence that the frozen route gate is
already anisotropic.
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


PAULI = {
    "I": np.eye(2, dtype=complex),
    "X": np.array([[0, 1], [1, 0]], dtype=complex),
    "Y": np.array([[0, -1j], [1j, 0]], dtype=complex),
    "Z": np.array([[1, 0], [0, -1]], dtype=complex),
}


def normalize(v):
    n = math.sqrt(float(np.vdot(v, v).real))
    if n < 1e-15:
        raise RuntimeError("zero norm intertwiner")
    return v / n


def local_basis(v=0):
    ls = (1, 1, 1, 1)
    return [normalize(PW.oriented_intertwiner(v, ls, K)) for K in (0, 2)]


def apply_dot(T, leg_a, leg_b, ls=(1, 1, 1, 1)):
    out = np.zeros_like(T, dtype=complex)
    ma = PW.spin_mats_cached(ls[leg_a])
    mb = PW.spin_mats_cached(ls[leg_b])
    for c in range(3):
        tmp = PW.apply_axis_np(T, leg_b, mb[c])
        tmp = PW.apply_axis_np(tmp, leg_a, ma[c])
        out += tmp
    return out


def logical_operator(leg_a, leg_b):
    basis = local_basis()
    M = np.zeros((2, 2), dtype=complex)
    for j, ket in enumerate(basis):
        acted = apply_dot(ket, leg_a, leg_b)
        for i, bra in enumerate(basis):
            M[i, j] = np.vdot(bra, acted)
    return M


def pauli_coeff(M):
    return {name: np.trace(P @ M) / 2.0 for name, P in PAULI.items()}


def sqrt_psd(M):
    Mh = 0.5 * (M + M.conj().T)
    vals, vecs = np.linalg.eigh(Mh)
    if vals.min() < -1e-10:
        raise RuntimeError(f"Q(p) lost positivity: {vals}")
    vals = np.maximum(vals, 0.0)
    return (vecs * np.sqrt(vals)) @ vecs.conj().T


def cjson(z):
    z = complex(z)
    return [float(z.real), float(z.imag)]


def run(n_theta=8192):
    S02 = logical_operator(0, 2)
    S00 = logical_operator(0, 0)
    S22 = logical_operator(2, 2)
    c02 = pauli_coeff(S02)

    theta = 2.0 * np.pi * np.arange(n_theta) / n_theta
    linear_avg = np.zeros((2, 2), dtype=complex)
    sqrt_avg = np.zeros((2, 2), dtype=complex)
    expectation_averages = np.zeros(2, dtype=float)
    min_q_eig = float("inf")

    basis = local_basis()
    for th in theta:
        p0, p1 = math.cos(float(th)), math.sin(float(th))
        Qp = p0 * p0 * S00 + 2.0 * p0 * p1 * S02 + p1 * p1 * S22
        Qp = 0.5 * (Qp + Qp.conj().T)
        vals = np.linalg.eigvalsh(Qp)
        min_q_eig = min(min_q_eig, float(vals.min()))
        linear_avg += Qp
        sqrt_avg += sqrt_psd(Qp)
        for i, ket in enumerate(basis):
            q = float(np.vdot(ket, Qp @ ket).real)
            expectation_averages[i] += math.sqrt(max(q, 0.0))

    linear_avg /= n_theta
    sqrt_avg /= n_theta
    expectation_averages /= n_theta

    clinear = pauli_coeff(linear_avg)
    csqrt = pauli_coeff(sqrt_avg)

    expected_S02 = (
        -0.25 * PAULI["I"]
        - (math.sqrt(3.0) / 4.0) * PAULI["X"]
        + 0.25 * PAULI["Z"]
    )
    exact_formula_error = float(np.linalg.norm(S02 - expected_S02))
    casimir_error = max(
        float(np.linalg.norm(S00 - 0.75 * PAULI["I"])),
        float(np.linalg.norm(S22 - 0.75 * PAULI["I"])),
    )

    mirror_y_norm = math.sqrt(
        abs(c02["Y"]) ** 2 + abs(clinear["Y"]) ** 2 + abs(csqrt["Y"]) ** 2
    )
    nonlinear_shape_norm = math.sqrt(abs(csqrt["X"]) ** 2 + abs(csqrt["Z"]) ** 2)
    linear_shape_norm = math.sqrt(abs(clinear["X"]) ** 2 + abs(clinear["Z"]) ** 2)
    expectation_difference = float(abs(expectation_averages[0] - expectation_averages[1]))

    passed = (
        exact_formula_error < 1e-12
        and casimir_error < 1e-12
        and min_q_eig > -1e-10
        and mirror_y_norm < 1e-12
        and linear_shape_norm < 1e-12
        and expectation_difference < 1e-12
        and nonlinear_shape_norm > 1e-4
    )

    return {
        "status": "logical route flux-metric operator gate",
        "passed": bool(passed),
        "selected_local_legs": [0, 2],
        "J0_dot_J2_matrix": [[cjson(S02[i, j]) for j in range(2)] for i in range(2)],
        "J0_dot_J2_pauli": {k: cjson(v) for k, v in c02.items()},
        "expected_exact_formula": "-1/4 I - sqrt(3)/4 X + 1/4 Z",
        "exact_formula_error": exact_formula_error,
        "diagonal_Casimir_error": casimir_error,
        "minimum_Qp_eigenvalue": min_q_eig,
        "linear_angular_average_Qp_pauli": {k: cjson(v) for k, v in clinear.items()},
        "operator_first_angular_average_sqrtQp_pauli": {k: cjson(v) for k, v in csqrt.items()},
        "expectation_first_average_omega_K0_K2": expectation_averages.tolist(),
        "expectation_first_branch_difference": expectation_difference,
        "linear_shape_anisotropy_norm": float(linear_shape_norm),
        "nonlinear_operator_sqrt_shape_anisotropy_norm": float(nonlinear_shape_norm),
        "mirror_Y_norm": float(mirror_y_norm),
        "interpretation": (
            "The flux metric is exactly mirror-even: its logical content lies in I/X/Z and contains no orientation Y. "
            "Isotropic angular averaging makes the linear Q(p) contraction scalar. In the current expectation-first "
            "ordering the angularly averaged route normal is also exactly equal on the K=0 and K=2 basis states in "
            "this control. By contrast, the operator-first spectral square root retains a finite X/Z component. "
            "Therefore route pseudospin anisotropy is ordering-dependent and is not established by the frozen "
            "expectation-first route gate alone."
        ),
        "scope": (
            "The operator-first square root is an ordering diagnostic, not yet the frozen route constraint. The "
            "current route gates use geometry expectations. A full operator-valued route/HDA construction must "
            "choose and test an ordering before the nonlinear X/Z component can be promoted to a dynamical claim."
        ),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--n-theta", type=int, default=8192)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    out = run(args.n_theta)
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
