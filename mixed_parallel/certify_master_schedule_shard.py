#!/usr/bin/env python3
"""Numerically certify candidate peeling blocks from persisted raw master maps.

This module never constructs the depth-6 shell, orbit/Jucys decomposition,
geometric structural support, branch capacities or structural matching.  It
loads an already-computed raw shard plus a candidate key schedule and performs
SVD on exactly the persisted C[i,q] matrices requested for blocks assigned to
that shard.

A per-block PASS is only a local numerical fact.  Global acceptance is decided
by replay_master_numerical_certificates.py, which recomputes output-key
uniqueness after *numerically accepted* removals.  Therefore a failed earlier
block cannot silently validate a later speculative schedule round.
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

KIND = 'BQG_MIXED_MASTER_SCHEDULE_SHARD_CERTIFICATES'
SCHEMA_VERSION = 1


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


def certify_one_block(*, orbit_index: int, m: int, master_maps: dict,
                      q_keys, sigma_floor: float = 1e-10) -> dict:
    q_keys = list(q_keys)
    if not q_keys:
        raise ValueError(f'orbit {orbit_index}: empty scheduled q set')
    mats = []
    source_rows = 0
    for q in q_keys:
        if q not in master_maps:
            raise KeyError(f'orbit {orbit_index}: scheduled q missing from persisted master map: {q!r}')
        a = np.asarray(master_maps[q])
        if a.ndim != 2 or a.shape[1] != m:
            raise ValueError(f'orbit {orbit_index}: q={q!r} bad shape {a.shape}, m={m}')
        mats.append(a)
        source_rows += int(a.shape[0])
    a = np.vstack(mats)
    s = np.linalg.svd(a, compute_uv=False)
    smax = float(s[0]) if len(s) else 0.0
    tol = max(a.shape[0], a.shape[1], source_rows) * np.finfo(float).eps * max(smax, 1.0) * 100.0
    threshold = max(float(sigma_floor), float(tol))
    rank = int(np.count_nonzero(s > tol))
    sigma_min = float(s[-1]) if len(s) >= m else 0.0
    passed = bool(a.shape[0] >= m and rank == m and sigma_min > threshold)
    return {
        'orbit_index': int(orbit_index),
        'target': int(m),
        'rank': rank,
        'pass': passed,
        'q_keys': q_keys,
        'q_count': len(q_keys),
        'rows': int(a.shape[0]),
        'sigma_max': smax,
        'sigma_min': sigma_min,
        'rank_tol': float(tol),
        'sigma_floor': float(sigma_floor),
        'threshold': threshold,
        'kernel_dimension_claim': 0 if passed else None,
        'failure_is_kernel_claim': False,
    }


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


def load_schedule(path: Path) -> dict:
    with gzip.open(path, 'rb') as f:
        x = pickle.load(f)
    if x.get('kind') != 'BQG_MIXED_MASTER_KEY_CANDIDATE_SCHEDULE':
        raise RuntimeError(f'wrong schedule kind: {x.get("kind")}')
    if x.get('proof_status') != 'NOT_A_NUMERICAL_RANK_CERTIFICATE':
        raise RuntimeError('candidate schedule claim boundary missing')
    return x


def scheduled_for_shard(schedule: dict, shard: int) -> dict[int, dict]:
    out = {}
    for rnd in schedule.get('rounds', []):
        rno = int(rnd['round'])
        for i0, rec in rnd.get('blocks', {}).items():
            i = int(i0)
            if int(rec['source_shard']) != shard:
                continue
            if i in out:
                raise RuntimeError(f'orbit {i} appears in multiple schedule rounds')
            out[i] = {
                'candidate_round': rno,
                'm': int(rec['m']),
                'q_keys': list(rec['unique_q']),
                'scheduled_unique_rows': int(rec['unique_rows']),
            }
    return out


def certify_shard(raw_tar: Path, schedule_path: Path, work: Path, shard: int,
                  sigma_floor: float, provenance: dict) -> dict:
    summary_path = extract_tar(raw_tar, work)
    summary = json.loads(summary_path.read_text())
    if int(summary.get('shard', -1)) != shard:
        raise RuntimeError(f'raw shard mismatch: {summary.get("shard")} != {shard}')
    schedule = load_schedule(schedule_path)
    if str(schedule.get('irrep')) != str(summary.get('irrep')):
        raise RuntimeError('schedule/raw irrep mismatch')
    if int(schedule.get('target_columns', -1)) != int(summary.get('target_columns', -2)):
        raise RuntimeError('schedule/raw target-column mismatch')

    todo = scheduled_for_shard(schedule, shard)
    records = {int(r['orbit_index']): r for r in summary.get('records', []) if r.get('ok')}
    certs = {}
    for i, spec in sorted(todo.items()):
        if i not in records:
            raise RuntimeError(f'scheduled orbit {i} missing from raw shard summary')
        m = int(records[i]['m'])
        if m != spec['m']:
            raise RuntimeError(f'orbit {i}: schedule m={spec["m"]}, raw m={m}')
        matches = list(work.rglob(f'b{i:05d}.pkl'))
        if len(matches) != 1:
            raise RuntimeError(f'orbit {i}: expected one persisted map pickle, got {len(matches)}')
        with matches[0].open('rb') as f:
            mp = pickle.load(f)
        c = certify_one_block(
            orbit_index=i,
            m=m,
            master_maps=mp,
            q_keys=spec['q_keys'],
            sigma_floor=sigma_floor,
        )
        c['candidate_round'] = spec['candidate_round']
        c['scheduled_unique_rows'] = spec['scheduled_unique_rows']
        certs[i] = c

    result = {
        'schema_version': SCHEMA_VERSION,
        'kind': KIND,
        'irrep': summary.get('irrep'),
        'shard': shard,
        'shards': summary.get('shards'),
        'target_columns': summary.get('target_columns'),
        'raw_tar_sha256': sha256(raw_tar),
        'schedule_sha256': sha256(schedule_path),
        **provenance,
        'environment': numerical_environment(),
        'certificates': certs,
        'stats': {
            'scheduled_blocks': len(certs),
            'scheduled_columns': sum(int(x['target']) for x in certs.values()),
            'local_pass_blocks': sum(bool(x['pass']) for x in certs.values()),
            'local_pass_columns': sum(int(x['target']) for x in certs.values() if x['pass']),
            'local_fail_blocks': sum(not bool(x['pass']) for x in certs.values()),
        },
        'structural_recompute_performed': False,
        'local_pass_is_global_acceptance': False,
        'claim_boundary': (
            'Per-block SVD on persisted raw numerical master maps only. Global removal requires '
            'independent fail-closed uniqueness replay against numerically accepted removals.'
        ),
    }
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--raw-tar', type=Path, required=True)
    ap.add_argument('--schedule', type=Path, required=True)
    ap.add_argument('--work', type=Path, required=True)
    ap.add_argument('--shard', type=int, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--json', type=Path, required=True)
    ap.add_argument('--sigma-floor', type=float, default=1e-10)
    ap.add_argument('--source-run-id')
    ap.add_argument('--source-artifact-id')
    ap.add_argument('--source-artifact-digest')
    ap.add_argument('--engine-git-blob-sha')
    a = ap.parse_args()
    x = certify_shard(
        a.raw_tar, a.schedule, a.work, a.shard, a.sigma_floor,
        {
            'source_run_id': a.source_run_id,
            'source_artifact_id': a.source_artifact_id,
            'source_artifact_digest': a.source_artifact_digest,
            'engine_git_blob_sha': a.engine_git_blob_sha,
        },
    )
    with gzip.open(a.out, 'wb', compresslevel=9) as f:
        pickle.dump(x, f, protocol=5)
    audit = {k: x[k] for k in (
        'schema_version','kind','irrep','shard','shards','target_columns',
        'raw_tar_sha256','schedule_sha256','source_run_id','source_artifact_id',
        'source_artifact_digest','engine_git_blob_sha','environment','stats',
        'structural_recompute_performed','local_pass_is_global_acceptance','claim_boundary')}
    audit['failed_orbits'] = sorted(int(i) for i,c in x['certificates'].items() if not c['pass'])
    audit['min_sigma_local_pass'] = min(
        (float(c['sigma_min']) for c in x['certificates'].values() if c['pass']),
        default=None,
    )
    a.json.write_text(json.dumps(audit, indent=2, sort_keys=True) + '\n')
    print(json.dumps(audit, indent=2, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
