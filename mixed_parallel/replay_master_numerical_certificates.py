#!/usr/bin/env python3
"""Fail-closed global replay of distributed mixed-sector SVD certificates.

The replay starts with every recovered orbit block present. A block is removed
only when BOTH conditions hold in the current remaining set:

1. every output key used by its local SVD certificate is actually unique to
   that block among currently remaining blocks; and
2. the local persisted-map SVD certificate is full-column-rank and above its
   recorded numerical threshold.

Only numerically accepted removals alter occupancy. Thus a failed earlier block
cannot create fictitious uniqueness for a later block. A non-empty residual is
reported as unresolved, never as an operator kernel.
"""
from __future__ import annotations

import argparse
import gzip
import json
import pickle
from pathlib import Path

KIND_META = 'BQG_MIXED_MASTER_KEY_METADATA'
KIND_CERT = 'BQG_MIXED_MASTER_SCHEDULE_SHARD_CERTIFICATES'
TARGET = {
    '32': (130903, 2755),
    '311': (153455, 2719),
    '221': (130503, 2749),
    '2111': (103318, 2712),
}


def replay(metadata: dict[int, dict], certs: dict[int, dict], sigma_floor: float = 1e-10) -> dict:
    support = {int(i): set(b['q_rows']) for i, b in metadata.items()}
    remaining = set(support)
    accepted = []
    rounds = []
    rejected_local = sorted(
        int(i) for i,c in certs.items()
        if not bool(c.get('pass'))
    )

    while True:
        occ = {}
        for i in remaining:
            for q in support[i]:
                occ.setdefault(q, set()).add(i)
        ready = []
        for i in sorted(remaining):
            c = certs.get(i)
            if not c or not bool(c.get('pass')):
                continue
            m = int(metadata[i]['m'])
            if int(c.get('target', -1)) != m or int(c.get('rank', -1)) != m:
                continue
            sig = float(c.get('sigma_min', 0.0))
            threshold = max(float(c.get('threshold', sigma_floor)), float(sigma_floor))
            if not sig > threshold:
                continue
            q_keys = list(c.get('q_keys') or [])
            if not q_keys:
                continue
            if any(q not in support[i] for q in q_keys):
                continue
            if not all(occ.get(q) == {i} for q in q_keys):
                continue
            ready.append(i)
        if not ready:
            break
        rounds.append({
            'round': len(rounds),
            'accepted_ids': ready,
            'blocks': len(ready),
            'columns': sum(int(metadata[i]['m']) for i in ready),
            'sigma_min': min(float(certs[i]['sigma_min']) for i in ready),
        })
        for i in ready:
            remaining.remove(i)
            accepted.append(i)

    remaining_ids = sorted(remaining)
    accepted_ids = accepted
    accepted_columns = sum(int(metadata[i]['m']) for i in accepted_ids)
    remaining_columns = sum(int(metadata[i]['m']) for i in remaining_ids)
    closed = not remaining_ids
    return {
        'status': 'PASS_CLOSED_FINITE_NUMERICAL' if closed else 'NUMERICAL_RESIDUAL_REQUIRES_FURTHER_CHECK',
        'accepted_ids': accepted_ids,
        'accepted_blocks': len(accepted_ids),
        'accepted_columns': accepted_columns,
        'remaining_ids': remaining_ids,
        'remaining_blocks': len(remaining_ids),
        'remaining_columns': remaining_columns,
        'rounds': rounds,
        'locally_failed_certificate_ids': rejected_local,
        'kernel_dimension': 0 if closed else None,
        'kernel_claim': False,
        'structural_recompute_performed': False,
        'matching_failure_is_kernel': False,
        'h2_null_lift_allowed': False,
        'next_if_residual': (
            'Generate new persisted-map SVD certificates for keys unique in the actual current residual; '
            'if no unique-key progress remains, build raw coupled residual master map/Gram for remaining IDs only.'
            if remaining_ids else None
        ),
    }


def load_metadata(paths: list[Path], irrep: str, expected_shards: int):
    blocks = {}
    shards = set()
    engine_blobs = set()
    provenance = {}
    for p in paths:
        with gzip.open(p, 'rb') as f:
            x = pickle.load(f)
        if x.get('kind') != KIND_META:
            raise RuntimeError(f'{p}: wrong metadata kind')
        if str(x.get('irrep')) != irrep or int(x.get('shards', -1)) != expected_shards:
            raise RuntimeError(f'{p}: metadata identity mismatch')
        sid = int(x['shard'])
        if sid in shards:
            raise RuntimeError(f'duplicate metadata shard {sid}')
        shards.add(sid)
        provenance[str(sid)] = {
            'source_artifact_id': x.get('source_artifact_id'),
            'source_artifact_digest': x.get('source_artifact_digest'),
            'source_tar_sha256': x.get('source_tar_sha256'),
            'engine_git_blob_sha': x.get('engine_git_blob_sha'),
        }
        if x.get('engine_git_blob_sha'):
            engine_blobs.add(x['engine_git_blob_sha'])
        for i0,b in x.get('blocks', {}).items():
            i = int(i0)
            if i in blocks:
                raise RuntimeError(f'duplicate metadata orbit {i}')
            blocks[i] = {
                'm': int(b['m']),
                'q_rows': dict(b['q_rows']),
                'source_shard': sid,
            }
    expected = set(range(expected_shards))
    if shards != expected:
        raise RuntimeError(f'metadata shard coverage mismatch missing={sorted(expected-shards)} extra={sorted(shards-expected)}')
    if len(engine_blobs) > 1:
        raise RuntimeError(f'multiple metadata engine blobs: {sorted(engine_blobs)}')
    return blocks, provenance, engine_blobs


def load_certificates(paths: list[Path], irrep: str, expected_shards: int):
    certs = {}
    seen_shards = set()
    engine_blobs = set()
    provenance = {}
    for p in paths:
        with gzip.open(p, 'rb') as f:
            x = pickle.load(f)
        if x.get('kind') != KIND_CERT:
            raise RuntimeError(f'{p}: wrong certificate kind')
        if str(x.get('irrep')) != irrep or int(x.get('shards', -1)) != expected_shards:
            raise RuntimeError(f'{p}: certificate identity mismatch')
        sid = int(x['shard'])
        if sid in seen_shards:
            raise RuntimeError(f'duplicate certificate shard {sid}')
        seen_shards.add(sid)
        provenance[str(sid)] = {
            'source_artifact_id': x.get('source_artifact_id'),
            'source_artifact_digest': x.get('source_artifact_digest'),
            'raw_tar_sha256': x.get('raw_tar_sha256'),
            'schedule_sha256': x.get('schedule_sha256'),
            'engine_git_blob_sha': x.get('engine_git_blob_sha'),
        }
        if x.get('engine_git_blob_sha'):
            engine_blobs.add(x['engine_git_blob_sha'])
        for i0,c in x.get('certificates', {}).items():
            i = int(i0)
            if i in certs:
                raise RuntimeError(f'duplicate orbit certificate {i}')
            certs[i] = c
    if len(engine_blobs) > 1:
        raise RuntimeError(f'multiple certificate engine blobs: {sorted(engine_blobs)}')
    return certs, seen_shards, provenance, engine_blobs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--irrep', choices=TARGET, required=True)
    ap.add_argument('--metadata-dir', type=Path, required=True)
    ap.add_argument('--cert-dir', type=Path, required=True)
    ap.add_argument('--expected-shards', type=int, required=True)
    ap.add_argument('--metadata-pattern', default='*-keymeta.pkl.gz')
    ap.add_argument('--cert-pattern', default='*-svdcert.pkl.gz')
    ap.add_argument('--sigma-floor', type=float, default=1e-10)
    ap.add_argument('--out', type=Path, required=True)
    a = ap.parse_args()
    target_columns, target_blocks = TARGET[a.irrep]
    try:
        metadata, meta_prov, meta_engines = load_metadata(
            sorted(a.metadata_dir.rglob(a.metadata_pattern)), a.irrep, a.expected_shards)
        recovered_columns = sum(int(x['m']) for x in metadata.values())
        if len(metadata) != target_blocks or recovered_columns != target_columns:
            raise RuntimeError(
                f'metadata coverage {len(metadata)}/{target_blocks} blocks, '
                f'{recovered_columns}/{target_columns} columns')
        certs, cert_shards, cert_prov, cert_engines = load_certificates(
            sorted(a.cert_dir.rglob(a.cert_pattern)), a.irrep, a.expected_shards)
        if meta_engines and cert_engines and meta_engines != cert_engines:
            raise RuntimeError(f'metadata/certificate engine mismatch: {meta_engines} vs {cert_engines}')
        for i,c in certs.items():
            if i not in metadata:
                raise RuntimeError(f'certificate for unknown orbit {i}')
            if int(c.get('target', -1)) != int(metadata[i]['m']):
                raise RuntimeError(f'orbit {i}: certificate target mismatch')
        out = replay(metadata, certs, a.sigma_floor)
        out.update({
            'metadata_recovered_blocks': len(metadata),
            'metadata_recovered_columns': recovered_columns,
            'certificate_blocks_available': len(certs),
            'certificate_shards_available': sorted(cert_shards),
            'metadata_engine_git_blob_shas': sorted(meta_engines),
            'certificate_engine_git_blob_shas': sorted(cert_engines),
            'metadata_provenance_by_shard': meta_prov,
            'certificate_provenance_by_shard': cert_prov,
        })
    except Exception as exc:
        out = {
            'status': 'INPUT_COVERAGE_FAILURE',
            'error': repr(exc),
            'kernel_dimension': None,
            'kernel_claim': False,
            'structural_recompute_performed': False,
        }
    out.update({
        'schema_version': 1,
        'irrep': a.irrep,
        'target_blocks': target_blocks,
        'target_columns': target_columns,
        'structural_status': 'CLOSED_IMMUTABLE_INPUT',
        'claim_boundary': (
            'Finite numerical replay from persisted master-map metadata and SVD certificates only. '
            'Structural depth-6 [3,2] proof is immutable input. Nonempty residual is not a kernel claim.'
        ),
    })
    a.out.write_text(json.dumps(out, indent=2, sort_keys=True, default=str) + '\n')
    print(json.dumps({k: out.get(k) for k in (
        'status','accepted_blocks','accepted_columns','remaining_blocks',
        'remaining_columns','kernel_dimension','kernel_claim')}, indent=2))
    return 0 if out.get('status') == 'PASS_CLOSED_FINITE_NUMERICAL' else 2


if __name__ == '__main__':
    raise SystemExit(main())
