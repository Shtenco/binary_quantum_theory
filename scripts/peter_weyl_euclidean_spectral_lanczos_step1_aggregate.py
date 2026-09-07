#!/usr/bin/env python3
"""Continue the actual Euclidean master block-Lanczos graph from Q1.

Consumes:
  * the persisted Q1 block and B1 from the actual mu2 calculation;
  * one generic fixed-cutoff M_E action Z1_a=M_E Q1_a for every Q1 column;
  * the actual mu2 result containing A0=mu1.

It computes

    A1 = Q1^dag M_E Q1,
    R2 = M_E Q1 - Q0 B1^dag - Q1 A1,
    G2 = R2^dag R2 = B2^dag B2,

with explicit two-pass reorthogonalization against Q0 and Q1.  If G2 has
positive rank it serializes Q2 and B2.  It also builds the partial block-Jacobi
graph and derives boundary moments mu0..mu4.  Those moments are exact algebraic
consequences of A0,B1,A1,B2 up to order four; A2 cannot enter a closed walk of
length <=4 starting and ending on Q0.

A small residual is NOT promoted to finite spectral termination unless an
upstream propagated numerical error bound is explicitly supplied.  This keeps
the actual BQG history fail-closed.
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
import bqg_spectral_history_graph_gate as SPECTRAL


def decode_state(rows):
    out = {}
    for row in rows:
        key = (tuple(int(x) for x in row['spins']), tuple(int(x) for x in row['K_labels']))
        a = row['amp']
        out[key] = complex(float(a[0]), float(a[1]))
    return out


def encode_state(state):
    return [
        {'spins': [int(x) for x in spins], 'K_labels': [int(x) for x in Ks],
         'amp': [float(complex(z).real), float(complex(z).imag)]}
        for (spins, Ks), z in sorted(state.items(), key=lambda kv: repr(kv[0]))
        if complex(z) != 0.0j
    ]


def inner(a, b):
    if len(a) > len(b):
        return np.conj(inner(b, a))
    return sum((np.conj(z) * b.get(k, 0.0j) for k, z in a.items()), 0.0j)


def norm(state):
    return math.sqrt(max(float(inner(state, state).real), 0.0))


def gram(states):
    n = len(states)
    G = np.zeros((n, n), complex)
    for i in range(n):
        for j in range(i, n):
            z = inner(states[i], states[j])
            G[i, j] = z
            G[j, i] = np.conj(z)
    return G


def opnorm(a):
    return float(np.linalg.norm(a, 2)) if a.size else 0.0


def add_scaled(dst, src, scale):
    scale = complex(scale)
    if scale == 0.0j:
        return
    for k, z in src.items():
        v = dst.get(k, 0.0j) + scale * z
        if v == 0.0j:
            dst.pop(k, None)
        else:
            dst[k] = v


def load_q1(root: Path):
    manifests = list(root.rglob('q1_manifest.json'))
    if len(manifests) != 1:
        raise RuntimeError(f'expected one q1_manifest.json, got {len(manifests)}')
    meta = json.loads(manifests[0].read_text(encoding='utf-8'))
    if meta.get('schema') != 'BQG_EUCLIDEAN_MASTER_LANCZOS_Q1_V1':
        raise RuntimeError('unexpected Q1 manifest schema')
    rank = int(meta['rank'])
    B1 = SPECTRAL.decode_array(meta['B1_matrix'])
    if B1.shape != (rank, 32):
        raise RuntimeError(f'B1 shape {B1.shape} incompatible with Q1 rank {rank}')
    files = {}
    for p in root.rglob('q1_*.json'):
        if p.name == 'q1_manifest.json':
            continue
        payload = json.loads(p.read_text(encoding='utf-8'))
        if payload.get('schema') != 'BQG_EUCLIDEAN_MASTER_LANCZOS_Q1_COLUMN_V1':
            continue
        i = int(payload['q1_index'])
        if i in files:
            raise RuntimeError(f'duplicate Q1 column {i}')
        files[i] = decode_state(payload['state'])
    if set(files) != set(range(rank)):
        raise RuntimeError(f'Q1 coverage mismatch: rank={rank}, columns={sorted(files)}')
    return meta, [files[i] for i in range(rank)], B1


def load_actions(root: Path, rank: int):
    rows = {}
    operator_sha = None
    for p in root.rglob('q1_master_*.json'):
        payload = json.loads(p.read_text(encoding='utf-8'))
        if payload.get('schema') != 'BQG_EUCLIDEAN_MASTER_ON_SPARSE_COLUMN_V1':
            continue
        if not payload.get('passed', False):
            raise RuntimeError(f'failed master action in {p}')
        i = int(payload['source_label'])
        if i in rows:
            raise RuntimeError(f'duplicate master action Q1 index {i}')
        sha = str(payload.get('operator_source_sha256', ''))
        if operator_sha is None:
            operator_sha = sha
        elif sha != operator_sha:
            raise RuntimeError('operator SHA mismatch across Q1 master actions')
        rows[i] = decode_state(payload['state'])
    if set(rows) != set(range(rank)):
        raise RuntimeError(f'master-action coverage mismatch: rank={rank}, columns={sorted(rows)}')
    return [rows[i] for i in range(rank)], operator_sha


def load_mu2(path: Path):
    payload = json.loads(path.read_text(encoding='utf-8'))
    if payload.get('schema') != 'BQG_EUCLIDEAN_PROJECTED_HEAT_MU2_V1' or not payload.get('passed', False):
        raise RuntimeError('mu2 result is absent or not certified')
    A0 = SPECTRAL.decode_matrix(payload['mu1']['matrix'])
    mu2 = SPECTRAL.decode_matrix(payload['mu2']['matrix'])
    return payload, A0, mu2


def boundary_overlap(states):
    basis = PW.basis_full_jhalf()
    X = np.zeros((32, len(states)), complex)
    for a, st in enumerate(states):
        for i, key in enumerate(basis):
            X[i, a] = st.get(key, 0.0j)
    return X


def subtract_block(states, block, coeff):
    """states[:,a] -= sum_b block[b] * coeff[b,a]."""
    for a, st in enumerate(states):
        for b, qb in enumerate(block):
            c = coeff[b, a]
            if c != 0.0j:
                add_scaled(st, qb, -c)


def reorthogonalize(residual, q0_keys, q1, passes=2):
    max_before = 0.0
    max_after = 0.0
    correction_max = 0.0
    for ipass in range(passes):
        C0 = np.zeros((32, len(residual)), complex)
        C1 = np.zeros((len(q1), len(residual)), complex)
        for a, st in enumerate(residual):
            for i, key in enumerate(q0_keys):
                C0[i, a] = st.get(key, 0.0j)
            for i, qi in enumerate(q1):
                C1[i, a] = inner(qi, st)
        ov = max(opnorm(C0), opnorm(C1))
        if ipass == 0:
            max_before = ov
        for a, st in enumerate(residual):
            n0 = norm(st)
            for i, key in enumerate(q0_keys):
                c = C0[i, a]
                if c != 0.0j:
                    v = st.get(key, 0.0j) - c
                    if v == 0.0j:
                        st.pop(key, None)
                    else:
                        st[key] = v
            for i, qi in enumerate(q1):
                c = C1[i, a]
                if c != 0.0j:
                    add_scaled(st, qi, -c)
            correction_max = max(correction_max, abs(n0 - norm(st)))
    C0f = np.zeros((32, len(residual)), complex)
    C1f = np.zeros((len(q1), len(residual)), complex)
    for a, st in enumerate(residual):
        for i, key in enumerate(q0_keys):
            C0f[i, a] = st.get(key, 0.0j)
        for i, qi in enumerate(q1):
            C1f[i, a] = inner(qi, st)
    max_after = max(opnorm(C0f), opnorm(C1f))
    return max_before, max_after, correction_max


def factor_block(residual, rank_tol):
    Graw = gram(residual)
    G = 0.5 * (Graw + Graw.conj().T)
    ev, U = np.linalg.eigh(G)
    scale = max(1.0, float(np.max(np.abs(ev))) if ev.size else 1.0)
    tol = rank_tol * scale
    support = ev > tol
    q2 = []
    if np.any(support):
        Ur = U[:, support]
        lr = ev[support]
        for a in range(len(lr)):
            st = {}
            for i, ri in enumerate(residual):
                c = Ur[i, a] / np.sqrt(lr[a])
                if c != 0.0j:
                    add_scaled(st, ri, c)
            q2.append(st)
        B2 = np.sqrt(lr)[:, None] * Ur.conj().T
    else:
        B2 = np.zeros((0, len(residual)), complex)
    return G, ev, tol, q2, B2


def build_partial_jacobi(A0, B1, A1, B2):
    n0, n1, n2 = A0.shape[0], A1.shape[0], B2.shape[0]
    J = np.zeros((n0 + n1 + n2, n0 + n1 + n2), complex)
    J[:n0, :n0] = A0
    J[:n0, n0:n0+n1] = B1.conj().T
    J[n0:n0+n1, :n0] = B1
    J[n0:n0+n1, n0:n0+n1] = A1
    if n2:
        J[n0:n0+n1, n0+n1:] = B2.conj().T
        J[n0+n1:, n0:n0+n1] = B2
    return 0.5 * (J + J.conj().T)


def boundary_moments_from_jacobi(J, n0=32, max_order=4):
    E = np.zeros((J.shape[0], n0), complex)
    E[:n0, :] = np.eye(n0)
    out = {0: np.eye(n0, dtype=complex)}
    P = np.eye(J.shape[0], dtype=complex)
    for n in range(1, max_order + 1):
        P = P @ J
        out[n] = 0.5 * (E.conj().T @ P @ E + (E.conj().T @ P @ E).conj().T)
    return out


def run(q1_root: Path, action_root: Path, mu2_path: Path, termination_error_bound=None):
    meta, q1, B1 = load_q1(q1_root)
    rank = len(q1)
    Z1, operator_sha = load_actions(action_root, rank)
    mu2_payload, A0, mu2_prior = load_mu2(mu2_path)
    if str(meta.get('operator_source_sha256', '')) != str(operator_sha):
        raise RuntimeError('Q1/operator SHA mismatch')
    if str(mu2_payload.get('operator_source_sha256', '')) != str(operator_sha):
        raise RuntimeError('mu2/operator SHA mismatch')

    q0_keys = PW.basis_full_jhalf()
    Q1G = gram(q1)
    q1_orth = opnorm(Q1G - np.eye(rank))
    q0q1 = opnorm(boundary_overlap(q1))

    # Measured block projections of M Q1.
    C01 = boundary_overlap(Z1)                  # Q0^dag M Q1
    A1raw = np.zeros((rank, rank), complex)
    for a, za in enumerate(Z1):
        for b, qb in enumerate(q1):
            A1raw[b, a] = inner(qb, za)
    A1herm_error = opnorm(A1raw - A1raw.conj().T)
    A1 = 0.5 * (A1raw + A1raw.conj().T)
    edge_error = opnorm(C01 - B1.conj().T)

    residual = [dict(z) for z in Z1]
    # Subtract measured old-block projections.  Edge equality to B1^dag is an
    # independent Hermiticity/Lanczos check and is not silently imposed.
    for a, st in enumerate(residual):
        for i, key in enumerate(q0_keys):
            c = C01[i, a]
            if c != 0.0j:
                v = st.get(key, 0.0j) - c
                if v == 0.0j:
                    st.pop(key, None)
                else:
                    st[key] = v
    subtract_block(residual, q1, A1)
    orth_before, orth_after, orth_correction = reorthogonalize(residual, q0_keys, q1, passes=2)

    G2, ev2, rtol_abs, q2, B2 = factor_block(residual, rank_tol=3.0e-9)
    scale2 = max(1.0, float(np.max(np.abs(ev2))) if ev2.size else 1.0)
    min_ev2 = float(np.min(ev2)) if ev2.size else 0.0
    max_ev2 = float(np.max(ev2)) if ev2.size else 0.0
    r2_rank = len(q2)
    residual_norm = math.sqrt(max(max_ev2, 0.0))
    q2_orth = opnorm(gram(q2) - np.eye(r2_rank)) if r2_rank else 0.0
    q0q2 = opnorm(boundary_overlap(q2)) if r2_rank else 0.0
    q1q2 = 0.0
    if r2_rank:
        X12 = np.zeros((rank, r2_rank), complex)
        for a, q2a in enumerate(q2):
            for b, q1b in enumerate(q1):
                X12[b, a] = inner(q1b, q2a)
        q1q2 = opnorm(X12)

    # Reconstruct M Q1 using the measured Jacobi coefficients and Q2 B2.
    recurrence_error = 0.0
    for a, za in enumerate(Z1):
        rec = {}
        for i, key in enumerate(q0_keys):
            c = C01[i, a]
            if c != 0.0j:
                rec[key] = rec.get(key, 0.0j) + c
        for b, qb in enumerate(q1):
            add_scaled(rec, qb, A1[b, a])
        for b, qb in enumerate(q2):
            add_scaled(rec, qb, B2[b, a])
        diff = dict(za)
        add_scaled(diff, rec, -1.0)
        recurrence_error = max(recurrence_error, norm(diff))

    J = build_partial_jacobi(A0, B1, A1, B2)
    j_herm = opnorm(J - J.conj().T)
    mus = boundary_moments_from_jacobi(J, 32, 4)
    mu0_error = opnorm(mus[0] - np.eye(32))
    mu1_error = opnorm(mus[1] - A0)
    mu2_error = opnorm(mus[2] - mu2_prior)

    scale = max(1.0, opnorm(A0), opnorm(A1), opnorm(B1), opnorm(B2))
    numerical_tol = 5.0e-7 * scale
    termination_bound_present = termination_error_bound is not None and np.isfinite(float(termination_error_bound))
    termination_bound = float(termination_error_bound) if termination_bound_present else None
    termination_candidate = residual_norm <= numerical_tol
    termination_certified = bool(
        termination_bound_present
        and residual_norm <= max(numerical_tol, termination_bound)
        and orth_after <= numerical_tol
    )

    checks = {
        'q1_nonempty': rank > 0,
        'q1_orthonormal': q1_orth <= numerical_tol,
        'q0_q1_orthogonal': q0q1 <= numerical_tol,
        'all_q1_master_actions_present': len(Z1) == rank,
        'operator_sha_consistent': bool(operator_sha),
        'A1_hermitian_before_symmetrization': A1herm_error <= numerical_tol,
        'old_edge_Q0dagMQ1_matches_B1dag': edge_error <= numerical_tol,
        'R2_positive_semidefinite': min_ev2 >= -3.0e-9 * scale2,
        'two_pass_reorthogonalization_closed_old_blocks': orth_after <= numerical_tol,
        'Q2_orthonormal_if_present': q2_orth <= numerical_tol,
        'Q0_Q2_orthogonal_if_present': q0q2 <= numerical_tol,
        'Q1_Q2_orthogonal_if_present': q1q2 <= numerical_tol,
        'second_block_recurrence_reconstructs_MQ1': recurrence_error <= 5.0 * numerical_tol,
        'partial_Jacobi_is_Hermitian': j_herm <= numerical_tol,
        'Jacobi_mu0_matches_identity': mu0_error <= numerical_tol,
        'Jacobi_mu1_matches_actual_mu1': mu1_error <= numerical_tol,
        'Jacobi_mu2_matches_actual_mu2': mu2_error <= 5.0 * numerical_tol,
    }

    status = 'CONTINUE_TO_Q2'
    if termination_certified:
        status = 'FIXED_REGULATOR_EUCLIDEAN_SPECTRAL_TERMINATION_CERTIFIED'
    elif termination_candidate:
        status = 'NUMERICAL_TERMINATION_CANDIDATE_NOT_CERTIFIED'

    result = {
        'schema': 'BQG_EUCLIDEAN_SPECTRAL_LANCZOS_STEP1_V1',
        'status': status,
        'q1_rank': rank,
        'q2_rank': r2_rank,
        'operator_source_sha256': operator_sha,
        'A0_matrix': SPECTRAL.encode_matrix(A0),
        'B1_matrix': SPECTRAL.encode_matrix(B1),
        'A1': {
            'matrix': SPECTRAL.encode_matrix(A1),
            'hermiticity_error_before_symmetrization': A1herm_error,
            'eigenvalue_min': float(np.min(np.linalg.eigvalsh(A1))),
            'eigenvalue_max': float(np.max(np.linalg.eigvalsh(A1))),
        },
        'B2_matrix': SPECTRAL.encode_matrix(B2),
        'R2': {
            'definition': 'R2=(I-Q0Q0dag-Q1Q1dag) M_E Q1 after two-pass full reorthogonalization',
            'rank': r2_rank,
            'rank_tolerance': rtol_abs,
            'eigenvalue_min': min_ev2,
            'eigenvalue_max': max_ev2,
            'residual_operator_norm': residual_norm,
            'matrix': SPECTRAL.encode_matrix(G2),
        },
        'orthogonality': {
            'Q1_orthonormality_error': q1_orth,
            'Q0_Q1_overlap_norm': q0q1,
            'pre_reorth_old_block_overlap_norm': orth_before,
            'post_reorth_old_block_overlap_norm': orth_after,
            'max_norm_change_from_reorthogonalization': orth_correction,
            'Q2_orthonormality_error': q2_orth,
            'Q0_Q2_overlap_norm': q0q2,
            'Q1_Q2_overlap_norm': q1q2,
        },
        'recurrence': {
            'Q0dag_MQ1_minus_B1dag_operator_error': edge_error,
            'MQ1_reconstruction_max_sparse_norm_error': recurrence_error,
        },
        'partial_block_jacobi': {
            'dimension': int(J.shape[0]),
            'matrix': SPECTRAL.encode_matrix(J),
            'hermiticity_error': j_herm,
            'meaning': 'actual Euclidean master spectral graph through block edge B2; A2 is intentionally absent/zero because it cannot enter boundary moments through order 4',
        },
        'derived_boundary_moments': {
            str(n): SPECTRAL.encode_matrix(mus[n]) for n in range(5)
        },
        'moment_regression': {
            'mu0_error': mu0_error,
            'mu1_error': mu1_error,
            'mu2_error': mu2_error,
            'mu3_status': 'new actual block-Jacobi consequence',
            'mu4_status': 'new actual block-Jacobi consequence including B2dagB2',
        },
        'termination': {
            'candidate': termination_candidate,
            'certified': termination_certified,
            'residual_norm': residual_norm,
            'propagated_operator_error_bound_supplied': termination_bound_present,
            'propagated_operator_error_bound': termination_bound,
            'rule': 'No exact finite termination is emitted from a small numerical residual without an upstream propagated error certificate.',
        },
        'checks': checks,
        'passed': bool(all(checks.values())),
        'claim_boundary': (
            'Actual fixed-cutoff Euclidean block-Lanczos step only.  Even a certified Euclidean finite termination is not the full physical BQG projector: '
            'the full Lorentzian master and production quantum HDA/Dtarget certificate remain separate physical preconditions.'
        ),
    }

    spectral_packet = {
        'schema': SPECTRAL.SCHEMA,
        'depth': 1,
        'seed_label': 'actual_q2_boundary_Euclidean_master_history_depth1',
        'moments': {str(n): SPECTRAL.encode_matrix(mus[n]) for n in range(5)},
        'termination_certificate': {
            'mode': 'direct_block_residual',
            'residual_norm': residual_norm,
            'certified': termination_certified,
            'reason': status,
        },
        'physical_preconditions': {
            'domain_complete': False,
            'master_constraint_certified': False,
            'quantum_hda_or_explicit_dtarget_certified': False,
            'source_seed_complete_for_claim': False,
        },
        'tolerances': {
            'hermiticity': numerical_tol,
            'mu0_identity': numerical_tol,
            'hankel_rank_rtol': 1e-10,
            'psd': 1e-8,
            'moment_reproduction': 5.0 * numerical_tol,
            'termination_residual': numerical_tol,
            'zero_eigenvalue': 1e-10,
        },
        'heat_sigma': [0.0, 0.001, 0.01, 0.1, 1.0, 10.0],
        'zeta_s': [0.5, 1.0, 2.0],
        'provenance': {
            'mu2_schema': mu2_payload['schema'],
            'q1_schema': meta['schema'],
            'step1_schema': result['schema'],
            'operator_source_sha256': operator_sha,
        },
    }
    return result, spectral_packet, q2


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--q1-root', type=Path, required=True)
    ap.add_argument('--master-actions', type=Path, required=True)
    ap.add_argument('--mu2-result', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--spectral-packet', type=Path, required=True)
    ap.add_argument('--q2-dir', type=Path)
    ap.add_argument('--termination-error-bound', type=float)
    a = ap.parse_args()
    result, packet, q2 = run(a.q1_root, a.master_actions, a.mu2_result, a.termination_error_bound)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    a.spectral_packet.parent.mkdir(parents=True, exist_ok=True)
    a.spectral_packet.write_text(json.dumps(packet, indent=2) + '\n', encoding='utf-8')
    if a.q2_dir is not None:
        a.q2_dir.mkdir(parents=True, exist_ok=True)
        meta = {
            'schema': 'BQG_EUCLIDEAN_MASTER_LANCZOS_Q2_V1',
            'rank': len(q2),
            'B2_matrix': result['B2_matrix'],
            'operator_source_sha256': result['operator_source_sha256'],
            'parent_step_schema': result['schema'],
            'claim_boundary': 'Second Euclidean master-Lanczos block only; no physical-projector claim.',
        }
        (a.q2_dir / 'q2_manifest.json').write_text(json.dumps(meta, indent=2) + '\n', encoding='utf-8')
        for i, st in enumerate(q2):
            payload = {
                'schema': 'BQG_EUCLIDEAN_MASTER_LANCZOS_Q2_COLUMN_V1',
                'q2_index': i,
                'support': len(st),
                'state': encode_state(st),
            }
            (a.q2_dir / f'q2_{i:02d}.json').write_text(json.dumps(payload, separators=(',', ':')) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k not in {'A0_matrix', 'B1_matrix', 'B2_matrix', 'partial_block_jacobi', 'derived_boundary_moments'}}, indent=2))
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
