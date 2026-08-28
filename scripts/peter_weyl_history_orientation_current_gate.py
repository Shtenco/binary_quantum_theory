#!/usr/bin/env python3
"""Microscopic Peter-Weyl history orientation-current gate.

This gate is deliberately narrower than a physical-time claim.

Input dynamics
--------------
Use the production K5 Peter-Weyl Euclidean graph-changing primitives and the
already-corrected sine ordering

    H_E^sine = sum_s sign_s (T_s - T_s^dagger)/(2 i).

On the complete all-j=1/2 Gauss carrier (32 states = two intertwiners on each
of five tetrahedra), retain forward and reverse microscopic history branches:

    B_+ |psi> = sum_s sign_s T_s |psi>,
    B_- |psi> = sum_s sign_s T_s^dagger |psi>.

The history label is not identified with physical time. It is only the exact
ordered primitive-history direction already present in the constraint
regularization.

Two active-sector observables are formed without fitting:

    D_rate  = B_+^dagger B_+ - B_-^dagger B_-,

which detects forward/reverse history-weight asymmetry, and

    D_phase = (B_+^dagger B_- - B_-^dagger B_+) / (2 i),

which detects coherent orientation-sensitive phase interference even when the
forward and reverse norms are equal.

At the source tetrahedron the exact oriented-volume pseudoscalar is
proportional to logical Pauli Y,

    Q = sqrt(3)/4 Y_L.

The gate exhausts three increasingly general levels.

1. Intrinsic/environment-unbiased: source Y tensor identity on the four other
   logical qubits.
2. Fixed-K environment conditioned: each of the 16 diagonal environment
   blocks in the frozen K=(0,2) basis.
3. Complete source-Y Pauli sector: all 4^4=256 strings

       Y_source tensor P_1 tensor P_2 tensor P_3 tensor P_4,
       P_i in {I,X,Y,Z}.

The third level prevents a false no-go when locking exists only for coherent
environment superpositions such as Y tensor X or Y tensor YZ.

Only if every source-Y Pauli coefficient vanishes within the preregistered
relative tolerance is a complete first-shell no-go claimed on this 32D active
carrier. Neither outcome constructs a physical rigging-map/history measure or
physical frequency propagator.
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

import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_euclidean_sine_ordering_gate as SINE
import peter_weyl_zeroaware_volume_migration_experiment as ZVM

TOL = 1e-10
JMAX2 = 3  # exact for one K5 H_E history shell from j=1/2; max reached is j=3/2.
PAULI2 = {
    "I": np.eye(2, dtype=complex),
    "X": np.array([[0, 1], [1, 0]], complex),
    "Y": np.array([[0, -1j], [1j, 0]], complex),
    "Z": np.array([[1, 0], [0, -1]], complex),
}


def add(dst, src, scale=1.0, tol=TOL):
    for k, a in src.items():
        z = dst.get(k, 0j) + scale * a
        if abs(z) > tol:
            dst[k] = z
        elif k in dst:
            del dst[k]


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


def logical_local_pauli(keys, node, which):
    P = PAULI2[which]
    kval = (0, 2)
    idx = {key[1]: i for i, key in enumerate(keys)}
    M = np.zeros((len(keys), len(keys)), complex)
    for col, key in enumerate(keys):
        ks = list(key[1])
        b = kval.index(ks[node])
        for a in range(2):
            c = P[a, b]
            if abs(c) == 0:
                continue
            ko = list(ks)
            ko[node] = kval[a]
            row = idx[tuple(ko)]
            M[row, col] += c
    return M


def local_pauli_projection(O, paulis):
    out = {}
    for name, P in paulis.items():
        den = np.trace(P.conj().T @ P)
        val = np.trace(P.conj().T @ O) / den
        out[name] = [float(val.real), float(val.imag)]
    return out


def hermitian_defect(A):
    return float(np.linalg.norm(A - A.conj().T) / max(np.linalg.norm(A), 1e-30))


def source_environment_blocks(O, G_total, keys, source_v):
    """Return all 16 fixed-environment 2x2 source-qubit Y projections."""
    others = tuple(v for v in PW.VERT if v != source_v)
    idx = {key[1]: i for i, key in enumerate(keys)}
    Y = PAULI2["Y"]
    rows = []
    for env in itertools.product((0, 2), repeat=len(others)):
        inds = []
        for ks_source in (0, 2):
            ks = [0] * len(PW.VERT)
            ks[source_v] = ks_source
            for v, kval in zip(others, env):
                ks[v] = kval
            inds.append(idx[tuple(ks)])
        block = O[np.ix_(inds, inds)]
        gblock = G_total[np.ix_(inds, inds)]
        gy = np.trace(Y.conj().T @ block) / np.trace(Y.conj().T @ Y)
        intensity = float(np.trace(gblock).real / 2.0)
        rows.append({
            "environment_nodes": list(others),
            "environment_K": list(env),
            "source_indices_K0_K2": inds,
            "g_Y": [float(gy.real), float(gy.imag)],
            "mean_history_intensity": intensity,
            "g_Y_relative_to_history_intensity": float(gy.real / max(intensity, 1e-30)),
            "block": [[[float(block[i, j].real), float(block[i, j].imag)] for j in range(2)] for i in range(2)],
        })
    return rows


def complete_source_y_pauli_audit(O, keys, source_v, coefficient_tol):
    """Exhaust all 256 Pauli strings with Y on the source logical qubit."""
    local = {
        v: {p: logical_local_pauli(keys, v, p) for p in "IXYZ"}
        for v in PW.VERT
    }
    dim = len(keys)
    rows = []
    others = tuple(v for v in PW.VERT if v != source_v)
    for env_word in itertools.product("IXYZ", repeat=len(others)):
        word = [None] * len(PW.VERT)
        word[source_v] = "Y"
        for v, p in zip(others, env_word):
            word[v] = p
        P = np.eye(dim, dtype=complex)
        for v, p in enumerate(word):
            P = P @ local[v][p]
        c = np.trace(P.conj().T @ O) / dim
        rows.append({
            "word": "".join(word),
            "coefficient": [float(c.real), float(c.imag)],
            "abs_coefficient": float(abs(c)),
            "environment_is_K_diagonal": all(p in ("I", "Z") for p in env_word),
        })
    rows.sort(key=lambda r: r["abs_coefficient"], reverse=True)
    all_vals = [r["abs_coefficient"] for r in rows]
    diag_vals = [r["abs_coefficient"] for r in rows if r["environment_is_K_diagonal"]]
    intrinsic_word = "".join("Y" if v == source_v else "I" for v in PW.VERT)
    intrinsic = next(r for r in rows if r["word"] == intrinsic_word)
    coeff_norm = math.sqrt(sum(x * x for x in all_vals))
    nonzero = [r for r in rows if r["abs_coefficient"] > coefficient_tol]
    return {
        "source_Y_string_count": len(rows),
        "intrinsic_word": intrinsic_word,
        "intrinsic_coefficient": intrinsic["coefficient"],
        "max_abs_source_Y_coefficient": max(all_vals, default=0.0),
        "max_abs_K_diagonal_environment_source_Y_coefficient": max(diag_vals, default=0.0),
        "source_Y_coefficient_l2_norm": coeff_norm,
        "coefficient_zero_tolerance": coefficient_tol,
        "nonzero_source_Y_string_count": len(nonzero),
        "top_source_Y_terms": rows[:24],
    }


def classify_complete_locking(audit):
    tol = audit["coefficient_zero_tolerance"]
    intrinsic = abs(complex(*audit["intrinsic_coefficient"])) if False else abs(audit["intrinsic_coefficient"][0] + 1j * audit["intrinsic_coefficient"][1])
    max_diag = audit["max_abs_K_diagonal_environment_source_Y_coefficient"]
    max_all = audit["max_abs_source_Y_coefficient"]
    if intrinsic > tol:
        return "INTRINSIC_NONZERO_FIRST_SHELL"
    if max_diag > tol:
        return "K_BASIS_ENVIRONMENT_CONDITIONED_FIRST_SHELL"
    if max_all > tol:
        return "COHERENT_ENVIRONMENT_CONDITIONED_FIRST_SHELL"
    return "ZERO_ALL_SOURCE_Y_PAULI_CHANNELS_FIRST_SHELL_WITHIN_TOL"


def run(source_v=0):
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

    paulis_source = {p: logical_local_pauli(keys, source_v, p) for p in "IXYZ"}
    Y0 = paulis_source["Y"]
    yden = float(np.trace(Y0.conj().T @ Y0).real)
    g_rate = np.trace(Y0.conj().T @ D_rate) / yden
    g_phase = np.trace(Y0.conj().T @ D_phase) / yden
    avg_history_intensity = float(np.trace(G_total).real / len(keys))

    rate_env = source_environment_blocks(D_rate, G_total, keys, source_v)
    phase_env = source_environment_blocks(D_phase, G_total, keys, source_v)

    coefficient_tol = 1e-10 * max(avg_history_intensity, 1e-30)
    rate_pauli = complete_source_y_pauli_audit(D_rate, keys, source_v, coefficient_tol)
    phase_pauli = complete_source_y_pauli_audit(D_phase, keys, source_v, coefficient_tol)
    rate_status = classify_complete_locking(rate_pauli)
    phase_status = classify_complete_locking(phase_pauli)

    Z0 = paulis_source["Z"]
    y_reflection_error = float(np.linalg.norm(Z0 @ Y0 @ Z0 + Y0))

    sine_gram = gram(sine, sine)
    sine_nonzero = float(np.trace(sine_gram).real) > 1e-14

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
        "all_environment_rate_gY_real": max((abs(r["g_Y"][1]) for r in rate_env), default=0.0) < 1e-9,
        "all_environment_phase_gY_real": max((abs(r["g_Y"][1]) for r in phase_env), default=0.0) < 1e-9,
        "complete_rate_source_Y_pauli_count_256": rate_pauli["source_Y_string_count"] == 256,
        "complete_phase_source_Y_pauli_count_256": phase_pauli["source_Y_string_count"] == 256,
    }

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
        "intrinsic_environment_unbiased": {
            "definition": "source Y tensor identity on all four non-source logical qubits",
            "g_YC_rate": [float(g_rate.real), float(g_rate.imag)],
            "g_YC_phase": [float(g_phase.real), float(g_phase.imag)],
            "g_YC_rate_relative_to_mean_history_intensity": rel_rate,
            "g_YC_phase_relative_to_mean_history_intensity": rel_phase,
        },
        "fixed_K_environment_conditioned": {
            "environment_count": len(rate_env),
            "max_abs_rate_gY": max((abs(r["g_Y"][0]) for r in rate_env), default=0.0),
            "max_abs_phase_gY": max((abs(r["g_Y"][0]) for r in phase_env), default=0.0),
            "rate_rows": rate_env,
            "phase_rows": phase_env,
        },
        "complete_source_Y_pauli_sector": {
            "rate": rate_pauli,
            "phase": phase_pauli,
            "rate_locking_status": rate_status,
            "phase_locking_status": phase_status,
        },
        "local_pauli_projection_D_rate_after_full_environment_trace": local_pauli_projection(D_rate, paulis_source),
        "local_pauli_projection_D_phase_after_full_environment_trace": local_pauli_projection(D_phase, paulis_source),
        "checks": checks,
        "definitions": {
            "B_plus": "sum_s sign_s T_s on the complete all-j=1/2 Gauss carrier",
            "B_minus": "sum_s sign_s T_s^dagger on the same carrier",
            "D_rate": "B_plus^dagger B_plus - B_minus^dagger B_minus",
            "D_phase": "(B_plus^dagger B_minus - B_minus^dagger B_plus)/(2i)",
            "Y_geometry": "logical Pauli Y at source tetrahedron, with Q=sqrt(3)/4 Y_L",
        },
        "claim_boundary": (
            "This is an exact finite first-history-shell constraint-dynamics diagnostic on the canonical K5 Peter-Weyl regulator, not a physical-time Hamiltonian. "
            "The complete 256-string source-Y Pauli audit exhausts every operator component containing the source oriented-geometry pseudoscalar inside the declared 32D all-j=1/2 active carrier. "
            "Only ZERO_ALL_SOURCE_Y_PAULI_CHANNELS_FIRST_SHELL_WITHIN_TOL is therefore a complete source-Y first-shell no-go in this carrier; it still does not exclude higher-history shells, the Lorentzian constraint, a physical projector, continuum U(1) coupling, or experimental effects."
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
