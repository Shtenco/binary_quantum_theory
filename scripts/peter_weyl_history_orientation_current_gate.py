#!/usr/bin/env python3
"""Microscopic Peter-Weyl history orientation-current gate.

This gate is deliberately narrower than a physical-time claim.

Input dynamics
--------------
Use the production K5 Peter-Weyl Euclidean graph-changing primitives and the
already-corrected sine ordering

    H_E^sine = sum_s sign_s (T_s - T_s^dagger)/(2 i).

On the complete all-j=1/2 Gauss carrier (32 states = two intertwiners on each
of five tetrahedra), retain the forward and reverse microscopic history
branches separately:

    B_+ |psi> = sum_s sign_s T_s |psi>,
    B_- |psi> = sum_s sign_s T_s^dagger |psi>.

The history label is not identified with physical time.  It is only the exact
ordered primitive-history direction already present in the constraint
regularization.

Two active-sector observables are then formed without fitting:

    D_rate  = B_+^dagger B_+ - B_-^dagger B_-,

which detects a forward/reverse history-weight asymmetry, and

    D_phase = (B_+^dagger B_- - B_-^dagger B_+) / (2 i),

which detects coherent orientation-sensitive phase interference even when the
forward and reverse norms are equal.

At the source tetrahedron the exact oriented-volume pseudoscalar is
proportional to the logical Pauli Y,

    Q = sqrt(3)/4 Y_L,

so the pre-registered microscopic locking coefficients are

    g_YC_rate  = Tr(Y_0 D_rate)  / Tr(Y_0^2),
    g_YC_phase = Tr(Y_0 D_phase) / Tr(Y_0^2).

A nonzero coefficient is evidence for a first-history-shell correlation
between geometric orientation and ordered graph-changing history.  A zero is
a genuine no-go for this particular first-shell channel.  Neither outcome by
itself constructs the physical rigging-map/history measure or a physical
frequency propagator.
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
import peter_weyl_euclidean_sine_ordering_gate as SINE
import peter_weyl_zeroaware_volume_migration_experiment as ZVM

TOL = 1e-10
JMAX2 = 3  # exact for one K5 H_E history shell from j=1/2; max reached is j=3/2.


def add(dst, src, scale=1.0, tol=TOL):
    for k, a in src.items():
        z = dst.get(k, 0j) + scale * a
        if abs(z) > tol:
            dst[k] = z
        elif k in dst:
            del dst[k]


def scale_state(src, c):
    return {k: c * a for k, a in src.items() if abs(c * a) > TOL}


def combine(*terms):
    out = {}
    for c, st in terms:
        add(out, st, c)
    return out


def inner(a, b):
    # Sparse exact-basis inner product.
    if len(a) > len(b):
        a, b = b, a
        return np.conj(inner(a, b))
    return sum(np.conj(v) * b.get(k, 0j) for k, v in a.items())


def norm(st):
    return math.sqrt(max(0.0, float(inner(st, st).real)))


def rel_state_error(a, b):
    d = combine((1.0, a), (-1.0, b))
    return norm(d) / max(norm(b), 1e-30)


def history_branches(key, source_v, jmax2=JMAX2):
    fwd = {}
    rev = {}
    ket = {key: 1.0 + 0j}
    for sign, spec in PW.oriented_specs(source_v):
        add(fwd, PW.apply_T_cached_state(ket, spec, jmax2, False), sign)
        add(rev, PW.apply_T_cached_state(ket, spec, jmax2, True), sign)
    return fwd, rev


def gram(states_a, states_b):
    n = len(states_a)
    out = np.zeros((n, n), complex)
    for i in range(n):
        for j in range(n):
            out[i, j] = inner(states_a[i], states_b[j])
    return out


def logical_local_pauli(keys, source_v, which):
    P = {
        "I": np.eye(2, dtype=complex),
        "X": np.array([[0, 1], [1, 0]], complex),
        "Y": np.array([[0, -1j], [1j, 0]], complex),
        "Z": np.array([[1, 0], [0, -1]], complex),
    }[which]
    kval = (0, 2)
    idx = {key[1]: i for i, key in enumerate(keys)}
    M = np.zeros((len(keys), len(keys)), complex)
    for col, key in enumerate(keys):
        ks = list(key[1])
        b = kval.index(ks[source_v])
        for a in range(2):
            c = P[a, b]
            if abs(c) == 0:
                continue
            ko = list(ks)
            ko[source_v] = kval[a]
            row = idx[tuple(ko)]
            M[row, col] += c
    return M


def pauli_projection(O, paulis):
    out = {}
    for name, P in paulis.items():
        den = np.trace(P.conj().T @ P)
        val = np.trace(P.conj().T @ O) / den
        out[name] = [float(val.real), float(val.imag)]
    return out


def hermitian_defect(A):
    return float(np.linalg.norm(A - A.conj().T) / max(np.linalg.norm(A), 1e-30))


def run(source_v=0):
    # Match the zero-aware absolute-volume convention used by the corrected
    # production sine-ordering audit.
    ZVM.patch_and_clear()

    keys = PW.basis_full_jhalf()
    if len(keys) != 32:
        raise AssertionError("expected complete 32-state all-j=1/2 Gauss carrier")

    fwd = []
    rev = []
    sine = []
    sine_reconstruction_errors = []
    max_spin_reached = 0.0

    for key in keys:
        F, R = history_branches(key, source_v, JMAX2)
        H = SINE.safe_H_sine({key: 1.0 + 0j}, source_v, JMAX2)
        H_from_history = combine((-0.5j, F), (+0.5j, R))
        sine_reconstruction_errors.append(rel_state_error(H_from_history, H))
        fwd.append(F)
        rev.append(R)
        sine.append(H)
        for st in (F, R, H):
            for out_key in st:
                max_spin_reached = max(max_spin_reached, max(out_key[0]) / 2.0)

    Gff = gram(fwd, fwd)
    Grr = gram(rev, rev)
    Gfr = gram(fwd, rev)

    D_rate = Gff - Grr
    D_phase = (Gfr - Gfr.conj().T) / (2j)
    G_total = Gff + Grr

    paulis = {p: logical_local_pauli(keys, source_v, p) for p in ("I", "X", "Y", "Z")}
    Y0 = paulis["Y"]
    yden = float(np.trace(Y0.conj().T @ Y0).real)
    g_rate = np.trace(Y0.conj().T @ D_rate) / yden
    g_phase = np.trace(Y0.conj().T @ D_phase) / yden
    avg_history_intensity = float(np.trace(G_total).real / len(keys))

    # Reflection representative on the logical source qubit.  Z Y Z = -Y.
    # This is only a local sign-covariance check, not a derivation that this Z
    # equals every microscopic face reflection used by the PL regulator.
    Z0 = paulis["Z"]
    y_reflection_error = float(np.linalg.norm(Z0 @ Y0 @ Z0 + Y0))

    # The physical sine combination should be exactly reconstructed from the
    # history-resolved T/T^dagger branches.
    sine_gram = gram(sine, sine)
    sine_nonzero = float(np.trace(sine_gram).real) > 1e-14

    # Report both absolute coefficients and dimensionless values relative to
    # the mean total one-shell history intensity.
    rel_rate = float(g_rate.real / max(avg_history_intensity, 1e-30))
    rel_phase = float(g_phase.real / max(avg_history_intensity, 1e-30))

    checks = {
        "complete_active_carrier_dim_32": len(keys) == 32,
        "sine_history_reconstruction": max(sine_reconstruction_errors) < 1e-9,
        "one_shell_cutoff_complete_max_spin_le_3_over_2": max_spin_reached <= 1.5 + 1e-12,
        "D_rate_hermitian": hermitian_defect(D_rate) < 1e-10,
        "D_phase_hermitian": hermitian_defect(D_phase) < 1e-10,
        "logical_Y_is_reflection_odd": y_reflection_error < 1e-12,
        "sine_constraint_channel_nonzero": sine_nonzero,
        "g_rate_is_real": abs(g_rate.imag) < 1e-9,
        "g_phase_is_real": abs(g_phase.imag) < 1e-9,
    }

    scale = max(avg_history_intensity, 1e-30)
    numerical_zero = 1e-10 * scale
    rate_status = "NONZERO_FIRST_SHELL" if abs(g_rate.real) > numerical_zero else "ZERO_FIRST_SHELL_WITHIN_TOL"
    phase_status = "NONZERO_FIRST_SHELL" if abs(g_phase.real) > numerical_zero else "ZERO_FIRST_SHELL_WITHIN_TOL"

    return {
        "status": "microscopic Peter-Weyl geometry/history orientation-current measurement",
        "passed": bool(all(checks.values())),
        "source_node": source_v,
        "Jmax": JMAX2 / 2,
        "active_gauss_dimension": len(keys),
        "max_spin_reached": max_spin_reached,
        "max_sine_history_reconstruction_relative_error": max(sine_reconstruction_errors),
        "mean_total_one_shell_history_intensity": avg_history_intensity,
        "D_rate_hermiticity_relative_defect": hermitian_defect(D_rate),
        "D_phase_hermiticity_relative_defect": hermitian_defect(D_phase),
        "g_YC_rate": [float(g_rate.real), float(g_rate.imag)],
        "g_YC_phase": [float(g_phase.real), float(g_phase.imag)],
        "g_YC_rate_relative_to_mean_history_intensity": rel_rate,
        "g_YC_phase_relative_to_mean_history_intensity": rel_phase,
        "rate_locking_status": rate_status,
        "phase_locking_status": phase_status,
        "local_pauli_projection_D_rate": pauli_projection(D_rate, paulis),
        "local_pauli_projection_D_phase": pauli_projection(D_phase, paulis),
        "checks": checks,
        "definitions": {
            "B_plus": "sum_s sign_s T_s on the complete all-j=1/2 Gauss carrier",
            "B_minus": "sum_s sign_s T_s^dagger on the same carrier",
            "D_rate": "B_plus^dagger B_plus - B_minus^dagger B_minus",
            "D_phase": "(B_plus^dagger B_minus - B_minus^dagger B_plus)/(2i)",
            "Y_geometry": "logical Pauli Y at source tetrahedron, with Q=sqrt(3)/4 Y_L",
        },
        "claim_boundary": (
            "This is an exact finite first-history-shell constraint-dynamics diagnostic on the canonical K5 Peter-Weyl regulator. "
            "A nonzero coefficient would establish microscopic orientation/history correlation in this declared carrier, not a physical-time Hamiltonian, physical projector, continuum U(1) coupling, or experimental observable. "
            "A zero coefficient rules out only this pre-registered first-shell channel; higher-history loops or the Lorentzian constraint may still differ."
        ),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source-node", type=int, default=0)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    out = run(args.source_node)
    text = json.dumps(out, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if out["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
