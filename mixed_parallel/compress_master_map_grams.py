#!/usr/bin/env python3
"""Compress persisted mixed-sector master maps into per-row Hermitian Grams.

For each numerical block i and output-row key q, replace the usually enormous
matrix C[q] (r_q x m_i) by the packed upper triangle of

    G[i,q] = C[q]^† C[q].

For any selected set Q of row keys,

    rank(vstack_q C[q]) == rank(sum_q G[i,q])

up to the same floating-point rank convention. Therefore numerical unique-row
peeling can be replayed without retaining the huge raw row matrices.

This script consumes already-computed master maps only. It does not construct
shells, S5 orbits, Jucys projectors, branch sums, supports, capacities or
structural matchings.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import pickle
import tarfile
from pathlib import Path

import numpy as np


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda: f.read(1024 * 1024), b''):
            h.update(b)
    return h.hexdigest()


def pack_upper(g: np.ndarray) -> np.ndarray:
    ii = np.triu_indices(g.shape[0])
    return np.asarray(g[ii])


def unpack_upper(v: np.ndarray, m: int) -> np.ndarray:
    g = np.zeros((m, m), dtype=v.dtype)
    ii = np.triu_indices(m)
    g[ii] = v
    g[(ii[1], ii[0])] = np.conjugate(v)
    d = np.diag_indices(m)
    g[d] = np.real(g[d])
    return g


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


def compress(src: Path, work: Path, out: Path) -> dict:
    summary_path = extract_tar(src, work)
    summary = json.loads(summary_path.read_text())
    blocks = {}
    raw_matrix_bytes = 0
    packed_bytes = 0
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
        qgrams = {}
        for q, a0 in mp.items():
            a = np.asarray(a0)
            if a.ndim != 2 or a.shape[1] != m:
                raise RuntimeError(f'orbit {i} key {q!r}: bad shape {a.shape}, m={m}')
            raw_matrix_bytes += int(a.nbytes)
            g = a.conjugate().T @ a
            # Hermitian symmetrization suppresses tiny BLAS asymmetry without
            # changing the represented positive Gram beyond roundoff.
            g = (g + g.conjugate().T) * 0.5
            p = pack_upper(g)
            packed_bytes += int(p.nbytes)
            qgrams[q] = {
                'rows': int(a.shape[0]),
                'dtype': str(a.dtype),
                'gram_dtype': str(g.dtype),
                'packed_upper': p,
            }
            q_count += 1
        blocks[i] = {
            'record': rec,
            'm': m,
            'qgrams': qgrams,
        }

    payload = {
        'schema_version': 1,
        'kind': 'BQG_MIXED_MASTER_PER_Q_GRAMS',
        'source_tar': src.name,
        'source_tar_sha256': sha256(src),
        'irrep': summary.get('irrep'),
        'shard': summary.get('shard'),
        'shards': summary.get('shards'),
        'active_blocks': summary.get('active_blocks'),
        'target_columns': summary.get('target_columns'),
        'blocks': blocks,
        'compression_stats': {
            'blocks': len(blocks),
            'q_keys': q_count,
            'raw_matrix_bytes': raw_matrix_bytes,
            'packed_gram_bytes_uncompressed': packed_bytes,
            'algebraic_byte_ratio_before_gzip': (packed_bytes / raw_matrix_bytes) if raw_matrix_bytes else None,
        },
        'claim_boundary': (
            'Compression of already-computed numerical master maps only; '
            'no structural geometry/capacity/matching calculation performed.'
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
    a = ap.parse_args()
    result = compress(a.src, a.work, a.out)
    a.json.write_text(json.dumps({
        'schema_version': result['schema_version'],
        'kind': result['kind'],
        'source_tar': result['source_tar'],
        'source_tar_sha256': result['source_tar_sha256'],
        'irrep': result['irrep'],
        'shard': result['shard'],
        'shards': result['shards'],
        'active_blocks': result['active_blocks'],
        'target_columns': result['target_columns'],
        'compression_stats': result['compression_stats'],
        'claim_boundary': result['claim_boundary'],
    }, indent=2, sort_keys=True) + '\n')
    print(json.dumps(result['compression_stats'], indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
