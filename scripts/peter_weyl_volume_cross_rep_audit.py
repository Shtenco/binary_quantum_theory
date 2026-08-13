#!/usr/bin/env python3
"""Cross-representation audit of the Peter-Weyl four-leg volume operator.

This isolates the current ~1e-9 H_E mismatch before any Lorentzian triple is
built.  For every local spin quartet actually encountered immediately before a
volume insertion in the frozen all-j=1/2 Euclidean H_E word, compare:

  V_magnetic = existing PW.volume123_matrix on legs 1..3 tensor I_4,
  V_block    = direct sum over exact total-(J,M) recoupling blocks,
  V_zeroaware= full-space spectral functional calculus with backward-error
               zero eigenvalues removed before sqrt(abs(.)) .

The operational criterion for the preregistered phrase "dominant nullspace
accounting" is frozen here as >=99% of ||V_magnetic-V_block||_F^2 carried by
its right action on the Q-nullspace.  This script does not alter either volume
implementation or any HDA tolerance.
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
import charged_intertwiner_recoupling_gate as CH
import peter_weyl_covariant_volume_leg_gate as CV
import peter_weyl_covariant_K_leg_gate as CK

EPS = np.finfo(float).eps


def collect_reached_volume_quartets(source_v=0, Jmax2=5):
    initial = PW.basis_full_jhalf()[0]
    base = PW.initial_factorized_oriented(initial)
    quartets = set()
    samples = 0
    for _, spec in PW.oriented_specs(source_v):
        v, a, b, c = spec
        for adj in (False, True):
            for _, seq0 in PW.T_sequences(v, a, b, c):
                seq = PW.adjoint_sequence(seq0) if adj else seq0
                branches = [base]
                for op in seq:
                    if op[0] == 'V':
                        vv = op[1]
                        for spins, _, _ in branches:
                            quartets.add(tuple(PW.local_spins(spins, vv)))
                            samples += 1
                        break
                    nb = []
                    for br in branches:
                        nb.extend(PW.apply_path_branch(br, op[1], op[2], op[3], Jmax2))
                    branches = nb
                    if not branches:
                        break
    return tuple(sorted(quartets)), samples


def kron_leg(op, leg, dims):
    out = np.array([[1.0 + 0j]])
    for r, d in enumerate(dims):
        out = np.kron(out, op if r == leg else np.eye(d, dtype=complex))
    return out


def total_J2_matrix(spins):
    dims = [s + 1 for s in spins]
    Jtot = []
    for axis in range(3):
        A = np.zeros((int(np.prod(dims)),) * 2, complex)
        for leg, s in enumerate(spins):
            A += kron_leg(PW.spin_mats_cached(s)[axis], leg, dims)
        Jtot.append(A)
    return sum(A @ A for A in Jtot)


def old_magnetic_volume(spins):
    V3 = PW.volume123_matrix(spins[0], spins[1], spins[2])
    return np.kron(V3, np.eye(spins[3] + 1, dtype=complex))


def q_full(spins):
    Q3 = CH.q123_matrix(tuple(spins[:3]))
    return np.kron(Q3, np.eye(spins[3] + 1, dtype=complex))


def block_volume(spins):
    D = int(np.prod([s + 1 for s in spins]))
    V = np.zeros((D, D), complex)
    basis_cols = []
    block_dims = {}
    for J2 in CV.all_total_J2(spins):
        rec = CH.allowed_charged_labels(tuple(spins), J2)
        if not rec:
            continue
        Vb = CK.canonical_volume_block_general(tuple(spins), J2)
        block_dims[str(J2 / 2)] = len(rec)
        for M2 in PW.m2vals_t(J2):
            B = np.column_stack([
                CH.charged_tensor(tuple(spins), a, b, J2, M2).reshape(-1)
                for a, b in rec
            ])
            basis_cols.extend(B[:, r] for r in range(B.shape[1]))
            V += B @ Vb @ B.conj().T
    U = np.column_stack(basis_cols) if basis_cols else np.zeros((D, 0), complex)
    gram = U.conj().T @ U
    completeness = U @ U.conj().T
    return (
        0.5 * (V + V.conj().T),
        float(np.linalg.norm(gram - np.eye(gram.shape[0]))),
        float(np.linalg.norm(completeness - np.eye(D))),
        block_dims,
    )


def stable_zeroaware_volume(Q):
    ev, U = np.linalg.eigh(0.5 * (Q + Q.conj().T))
    qnorm = float(np.max(np.abs(ev))) if len(ev) else 0.0
    D = Q.shape[0]
    tau = 1000.0 * EPS * D * max(1.0, qnorm)
    mask = np.abs(ev) > tau
    vals = np.where(mask, np.sqrt(np.abs(ev)), 0.0)
    V = (U * vals) @ U.conj().T
    V = 0.5 * (V + V.conj().T)
    return V, ev, U, tau, mask


def rel_frob(A, B):
    return float(np.linalg.norm(A - B, 'fro') / max(np.linalg.norm(B, 'fro'), 1e-30))


def functional_defect(V, Q):
    V2 = V @ V
    return float(np.linalg.norm(V2 @ V2 - Q @ Q, 'fro') /
                 max(np.linalg.norm(Q @ Q, 'fro'), 1e-30))


def covariance_defect(V, J2):
    C = V @ J2 - J2 @ V
    return float(np.linalg.norm(C, 'fro') /
                 max(np.linalg.norm(V, 'fro') * np.linalg.norm(J2, 'fro'), 1e-30))


def one_quartet(spins):
    spins = tuple(spins)
    Q = q_full(spins)
    J2 = total_J2_matrix(spins)
    Vmag = old_magnetic_volume(spins)
    Vblk, gram_err, comp_err, block_dims = block_volume(spins)
    Vref, ev, Uq, tau, nz = stable_zeroaware_volume(Q)

    zero = ~nz
    P0 = Uq[:, zero] @ Uq[:, zero].conj().T if np.any(zero) else np.zeros_like(Q)
    null_dim = int(np.sum(zero))
    nonzero_abs = np.abs(ev[nz])
    min_nonzero = float(np.min(nonzero_abs)) if len(nonzero_abs) else 0.0
    gap_ratio = min_nonzero / tau if tau > 0 and min_nonzero > 0 else float('inf')

    dmb = Vmag - Vblk
    dmb2 = float(np.linalg.norm(dmb, 'fro') ** 2)
    null_right2 = float(np.linalg.norm(dmb @ P0, 'fro') ** 2)
    null_fraction = null_right2 / max(dmb2, 1e-300)

    def kernel_action(V):
        if not np.any(zero):
            return 0.0
        return float(np.linalg.norm(V @ Uq[:, zero], 'fro'))

    row = {
        'spins': [s / 2 for s in spins],
        'dimension': Q.shape[0],
        'block_multiplicities': block_dims,
        'basis_gram_error': gram_err,
        'basis_completeness_error': comp_err,
        'Q_zero_tolerance': tau,
        'Q_nullity': null_dim,
        'Q_smallest_nonzero_abs_eigenvalue': min_nonzero,
        'Q_gap_over_zero_tolerance': gap_ratio,
        'Vmag_vs_Vblock_relative_frobenius': rel_frob(Vmag, Vblk),
        'Vmag_vs_Vzeroaware_relative_frobenius': rel_frob(Vmag, Vref),
        'Vblock_vs_Vzeroaware_relative_frobenius': rel_frob(Vblk, Vref),
        'Vmag_minus_Vblock_nullspace_right_weight_fraction': null_fraction,
        'Vmag_kernel_action_frobenius': kernel_action(Vmag),
        'Vblock_kernel_action_frobenius': kernel_action(Vblk),
        'Vzeroaware_kernel_action_frobenius': kernel_action(Vref),
        'Vmag_V4_minus_Q2_relative': functional_defect(Vmag, Q),
        'Vblock_V4_minus_Q2_relative': functional_defect(Vblk, Q),
        'Vzeroaware_V4_minus_Q2_relative': functional_defect(Vref, Q),
        'Vmag_SU2_J2_commutator_relative': covariance_defect(Vmag, J2),
        'Vblock_SU2_J2_commutator_relative': covariance_defect(Vblk, J2),
        'Vzeroaware_SU2_J2_commutator_relative': covariance_defect(Vref, J2),
    }
    local_diag = (
        gap_ratio >= 1e8
        and row['Vzeroaware_kernel_action_frobenius'] < 1e-12
        and row['Vzeroaware_SU2_J2_commutator_relative'] < 1e-12
        and row['Vzeroaware_V4_minus_Q2_relative'] < 1e-12
        and gram_err < 1e-12
        and comp_err < 1e-12
        and (dmb2 < 1e-28 or null_fraction >= 0.99)
    )
    row['zero_space_diagnosis_passed'] = bool(local_diag)
    return row


def run():
    quartets, samples = collect_reached_volume_quartets()
    rows = [one_quartet(q) for q in quartets]
    worst = lambda key: max((r[key] for r in rows), default=0.0)
    min_gap = min((r['Q_gap_over_zero_tolerance'] for r in rows), default=float('inf'))
    diagnosed = bool(rows) and all(r['zero_space_diagnosis_passed'] for r in rows)
    return {
        'status': 'local volume cross-representation audit on all H_E-reached quartets',
        'passed': diagnosed,
        'volume_insertion_branch_samples': samples,
        'unique_reached_spin_quartets': len(quartets),
        'rows': rows,
        'minimum_Q_gap_over_zero_tolerance': min_gap,
        'max_Vmag_vs_Vblock_relative_frobenius': worst('Vmag_vs_Vblock_relative_frobenius'),
        'max_Vmag_kernel_action_frobenius': worst('Vmag_kernel_action_frobenius'),
        'max_Vblock_kernel_action_frobenius': worst('Vblock_kernel_action_frobenius'),
        'max_Vzeroaware_kernel_action_frobenius': worst('Vzeroaware_kernel_action_frobenius'),
        'max_Vmag_SU2_J2_commutator_relative': worst('Vmag_SU2_J2_commutator_relative'),
        'max_Vblock_SU2_J2_commutator_relative': worst('Vblock_SU2_J2_commutator_relative'),
        'max_Vzeroaware_SU2_J2_commutator_relative': worst('Vzeroaware_SU2_J2_commutator_relative'),
        'diagnosis': (
            'PASS means the reached Q spectra have a huge backward-error gap, the zero-aware '
            'functional calculus is symmetry/functional-calculus clean, and >=99% of each '
            'non-negligible magnetic-vs-block discrepancy is carried by the exact Q-nullspace. '
            'This is a diagnosis only; it does not migrate the production volume operator.'
        ),
        'next_use': (
            'If PASS, build a separately frozen zero-aware volume migration gate and rerun H_E/K/HH '
            'before accepting C_e(K). If FAIL, search projection/composition instead.'
        ),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path)
    a = ap.parse_args()
    out = run()
    text = json.dumps(out, indent=2)
    print(text)
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(text + '\n', encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
