#!/usr/bin/env python3
"""Compress persisted mixed-sector master maps into per-output-key QR factors.

For every already-computed numerical master block C[i,q] with shape (r_q,m_i),
compute a reduced QR factorization

    C[i,q] = Q[i,q] R[i,q]

and persist R[i,q] only.  Because Q has orthonormal columns/rows as appropriate,

    C[i,q]^* C[i,q] = R[i,q]^* R[i,q],

and therefore for any collection Qset of output keys

    singular_values(vstack(C[i,q] for q in Qset))
      == singular_values(vstack(R[i,q] for q in Qset))

up to floating-point QR error.  This retains the numerical rank witness without
forming a normal-equations Gram matrix and therefore avoids deliberately
squaring the condition number.

IMPORTANT CLAIM BOUNDARY
------------------------
This file consumes already-computed master maps only.  It does NOT enumerate
shells/orbits, construct Jucys selectors, derive branch sums, rebuild structural
support/capacity, or repeat the already-closed 130903/130903 structural proof.
Per-q QR factors are sufficient for unique-row numerical peeling.  They are NOT
sufficient for a coupled residual containing multiple orbit blocks that share
an output key, because cross-block products C_i(q)^* C_j(q) are not retained.
Such a residual must be checked from raw persisted master maps for residual IDs
only.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import pickle
import platform
import sys
import tarfile
from pathlib import Path

import numpy as np


KIND = 'BQG_MIXED_MASTER_PER_Q_QR'
SCHEMA_VERSION = 2


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda: f.read(1024 * 1024), b''):
            h.update(b)
    return h.hexdigest()


def numerical_environment() -> dict:
    return {
        'python': sys.version,
        'numpy': np.__version__,
        'platform': platform.platform(),
        'machine': platform.machine(),
        'OMP_NUM_THREADS': os.environ.get('OMP_NUM_THREADS'),
        'OPENBLAS_NUM_THREADS': os.environ.get('OPENBLAS_NUM_THREADS'),
        'MKL_NUM_THREADS': os.environ.get('MKL_NUM_THREADS'),
    }


def canonical_reduced_r(a: np.ndarray) -> np.ndarray:
    """Return a deterministic-phase reduced QR R factor.

    Multiplying each row of R by a unit complex phase leaves R^*R unchanged.
    We use that freedom to make every nonzero diagonal element real-positive,
    which removes the usual QR sign/phase ambiguity and improves reproducible
    hashing across equivalent LAPACK implementations.
    """
    a = np.asarray(a)
    if a.ndim != 2:
        raise ValueError(f'expected 2-D matrix, got {a.shape}')
    if a.shape[0] == 0:
        return np.zeros((0, a.shape[1]), dtype=a.dtype)
    _, r = np.linalg.qr(a, mode='reduced')
    r = np.asarray(r).copy()
    k = min(r.shape)
    for j in range(k):
        d = r[j, j]
        ad = abs(d)
        if ad != 0:
            phase = d / ad
            r[j, :] *= np.conjugate(phase)
            # Suppress an irrelevant tiny imaginary part on the canonical diag.
            if np.iscomplexobj(r):
                r[j, j] = complex(float(ad), 0.0)
            else:
                r[j, j] = float(ad)
    return r


def extract_tar(src: Path, out: Path) -> Path:
    out.mkdir(parents=True, exist_ok=True)
    root = out.resolve()
    with tarfile.open(src, 'r:gz') as tf:
        for member in tf.getmembers():
            dest = (out / member.name).resolve()
            if root not in dest.parents and dest != root:
                raise RuntimeError(f'unsafe tar member: {member.name}')
        tf.extractall(out)
    summaries = list(out.rglob('summary.json'))
    if len(summaries) != 1:
        raise RuntimeError(f'expected one summary.json, got {len(summaries)}')
    return summaries[0]


def compress(
    src: Path,
    work: Path,
    out: Path,
    *,
    source_run_id: str | None = None,
    source_artifact_id: str | None = None,
    source_artifact_digest: str | None = None,
    engine_git_blob_sha: str | None = None,
) -> dict:
    summary_path = extract_tar(src, work)
    summary = json.loads(summary_path.read_text())
    blocks = {}
    raw_matrix_bytes = 0
    qr_factor_bytes = 0
    raw_rows = 0
    factor_rows = 0
    q_count = 0

    for rec in summary.get('records', []):
        if not rec.get('ok'):
            raise RuntimeError(f'non-ok record: {rec}')
        i = int(rec['orbit_index'])
        m = int(rec['m'])
        matches = list(work.rglob(f'b{i:05d}.pkl'))
        if len(matches) != 1:
            raise RuntimeError(f'orbit {i}: expected one pickle, got {len(matches)}')
        with matches[0].open('rb') as f:
            mp = pickle.load(f)
        qfactors = {}
        for q, a0 in mp.items():
            a = np.asarray(a0)
            if a.ndim != 2 or a.shape[1] != m:
                raise RuntimeError(f'orbit {i} key {q!r}: bad shape {a.shape}, m={m}')
            r = canonical_reduced_r(a)
            if r.shape != (min(a.shape[0], m), m):
                raise RuntimeError(f'orbit {i} key {q!r}: unexpected R shape {r.shape}')
            raw_matrix_bytes += int(a.nbytes)
            qr_factor_bytes += int(r.nbytes)
            raw_rows += int(a.shape[0])
            factor_rows += int(r.shape[0])
            qfactors[q] = {
                'rows': int(a.shape[0]),
                'factor_rows': int(r.shape[0]),
                'source_dtype': str(a.dtype),
                'factor_dtype': str(r.dtype),
                'R': r,
            }
            q_count += 1
        blocks[i] = {
            'record': rec,
            'm': m,
            'qfactors': qfactors,
        }

    payload = {
        'schema_version': SCHEMA_VERSION,
        'kind': KIND,
        'source_tar': src.name,
        'source_tar_sha256': sha256(src),
        'source_run_id': source_run_id,
        'source_artifact_id': source_artifact_id,
        'source_artifact_digest': source_artifact_digest,
        'engine_git_blob_sha': engine_git_blob_sha,
        'irrep': summary.get('irrep'),
        'shard': summary.get('shard'),
        'shards': summary.get('shards'),
        'active_blocks': summary.get('active_blocks'),
        'target_columns': summary.get('target_columns'),
        'assigned_blocks': summary.get('assigned_blocks'),
        'assigned_columns': summary.get('assigned_columns'),
        'blocks': blocks,
        'environment': numerical_environment(),
        'compression_stats': {
            'blocks': len(blocks),
            'q_keys': q_count,
            'raw_rows': raw_rows,
            'qr_factor_rows': factor_rows,
            'raw_matrix_bytes': raw_matrix_bytes,
            'qr_factor_bytes_uncompressed': qr_factor_bytes,
            'algebraic_byte_ratio_before_gzip': (
                qr_factor_bytes / raw_matrix_bytes if raw_matrix_bytes else None
            ),
        },
        'mathematical_identity': 'For every q: C_q^* C_q = R_q^* R_q.',
        'residual_boundary': (
            'QR factors may certify blocks only through output keys unique among '
            'the currently remaining orbit blocks. A shared-key residual requires '
            'raw coupled master maps to retain inter-block cross terms.'
        ),
        'claim_boundary': (
            'Post-processing of already-computed numerical master maps only; '
            'no depth-6 structural geometry/capacity/matching calculation performed.'
        ),
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(out, 'wb', compresslevel=6) as f:
        pickle.dump(payload, f, protocol=5)
    payload['compression_stats']['output_gzip_bytes'] = out.stat().st_size
    return payload


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', type=Path, required=True)
    ap.add_argument('--work', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--json', type=Path, required=True)
    ap.add_argument('--source-run-id')
    ap.add_argument('--source-artifact-id')
    ap.add_argument('--source-artifact-digest')
    ap.add_argument('--engine-git-blob-sha')
    a = ap.parse_args()
    result = compress(
        a.src, a.work, a.out,
        source_run_id=a.source_run_id,
        source_artifact_id=a.source_artifact_id,
        source_artifact_digest=a.source_artifact_digest,
        engine_git_blob_sha=a.engine_git_blob_sha,
    )
    audit = {k: result[k] for k in (
        'schema_version', 'kind', 'source_tar', 'source_tar_sha256',
        'source_run_id', 'source_artifact_id', 'source_artifact_digest',
        'engine_git_blob_sha', 'irrep', 'shard', 'shards', 'active_blocks',
        'target_columns', 'assigned_blocks', 'assigned_columns', 'environment',
        'compression_stats', 'mathematical_identity', 'residual_boundary',
        'claim_boundary',
    )}
    a.json.write_text(json.dumps(audit, indent=2, sort_keys=True) + '\n')
    print(json.dumps(result['compression_stats'], indent=2, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
