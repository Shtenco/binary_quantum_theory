#!/usr/bin/env python3
"""Build a candidate peeling schedule from persisted numerical map keys only.

This is deliberately *not* a rank certificate. It proposes, round by round,
which output keys are unique to each remaining orbit block according to actual
persisted master-map keys. Every proposed block must subsequently pass a
numerical SVD/rank check on the original C[i,q] coefficients before removal is
accepted. A failed block invalidates any later removal that depended on its
absence; the final validator must therefore replay uniqueness against only
numerically accepted removals.
"""
from __future__ import annotations

import argparse
import gzip
import json
import pickle
from pathlib import Path

KIND = 'BQG_MIXED_MASTER_KEY_METADATA'
TARGET = {
    '32': (130903, 2755),
    '311': (153455, 2719),
    '221': (130503, 2749),
    '2111': (103318, 2712),
}


def validate_keymeta_coverage(records, *, irrep: str, expected_shards: int,
                              target_blocks: int, target_columns: int) -> dict:
    """Fail-closed gate for actual persisted numerical key metadata.

    Partial metadata is reusable evidence, but it never authorizes construction
    of a global uniqueness schedule.  The gate also rejects duplicate shard IDs,
    incompatible shard counts/irreps, duplicate orbit blocks, and mixed proof
    engine hashes.
    """
    shard_ids = set()
    orbit_ids = set()
    engine_blobs = set()
    recovered_columns = 0
    for x in records:
        if str(x.get('irrep')) != irrep:
            raise RuntimeError(f"wrong irrep {x.get('irrep')} expected {irrep}")
        if int(x.get('shards', -1)) != expected_shards:
            raise RuntimeError(
                f"wrong total shard count {x.get('shards')} expected {expected_shards}"
            )
        sid = int(x['shard'])
        if sid in shard_ids:
            raise RuntimeError(f'duplicate shard {sid}')
        shard_ids.add(sid)
        blob = x.get('engine_git_blob_sha')
        if blob:
            engine_blobs.add(str(blob))
        for i0, b in x.get('blocks', {}).items():
            i = int(i0)
            if i in orbit_ids:
                raise RuntimeError(f'duplicate orbit block {i}')
            orbit_ids.add(i)
            recovered_columns += int(b['m'])

    if len(engine_blobs) > 1:
        raise RuntimeError(f'multiple proof-engine blobs: {sorted(engine_blobs)}')

    expected = set(range(expected_shards))
    extra = sorted(shard_ids - expected)
    if extra:
        raise RuntimeError(f'extra shard ids outside expected range: {extra}')
    missing = sorted(expected - shard_ids)
    recovered_blocks = len(orbit_ids)
    exact_full = (
        not missing
        and recovered_blocks == target_blocks
        and recovered_columns == target_columns
    )
    if not missing and not exact_full:
        raise RuntimeError(
            f'full shard coverage but target mismatch blocks={recovered_blocks}/{target_blocks} '
            f'columns={recovered_columns}/{target_columns}'
        )
    return {
        'status': 'FULL_KEYMETA_COVERAGE' if exact_full else 'INCOMPLETE_KEYMETA_COVERAGE',
        'expected_shards': expected_shards,
        'recovered_shards': sorted(shard_ids),
        'missing_shards': missing,
        'recovered_blocks': recovered_blocks,
        'recovered_columns': recovered_columns,
        'target_blocks': target_blocks,
        'target_columns': target_columns,
        'engine_git_blob_shas': sorted(engine_blobs),
        'schedule_allowed': bool(exact_full),
        'proof_status': 'COVERAGE_GATE_ONLY_NOT_A_RANK_CERTIFICATE',
    }


def load_metadata(paths: list[Path], irrep: str, expected_shards: int):
    records = []
    for p in paths:
        with gzip.open(p, 'rb') as f:
            x = pickle.load(f)
        if x.get('kind') != KIND or int(x.get('schema_version', -1)) != 1:
            raise RuntimeError(f'{p}: wrong metadata schema/kind')
        records.append(x)

    target_columns, target_blocks = TARGET[irrep]
    coverage = validate_keymeta_coverage(
        records,
        irrep=irrep,
        expected_shards=expected_shards,
        target_blocks=target_blocks,
        target_columns=target_columns,
    )
    if not coverage['schedule_allowed']:
        raise RuntimeError(
            f"actual-q coverage incomplete: missing={coverage['missing_shards']} "
            f"blocks={coverage['recovered_blocks']}/{target_blocks} "
            f"columns={coverage['recovered_columns']}/{target_columns}"
        )

    blocks = {}
    provenance = {}
    for x in records:
        sid = int(x['shard'])
        provenance[sid] = {
            'source_run_id': x.get('source_run_id'),
            'source_artifact_id': x.get('source_artifact_id'),
            'source_artifact_digest': x.get('source_artifact_digest'),
            'source_tar_sha256': x.get('source_tar_sha256'),
            'engine_git_blob_sha': x.get('engine_git_blob_sha'),
        }
        for i0, b in x.get('blocks', {}).items():
            i = int(i0)
            blocks[i] = {
                'm': int(b['m']),
                'q_rows': dict(b['q_rows']),
                'source_shard': sid,
            }
    return blocks, provenance, coverage['engine_git_blob_shas']


def build_schedule(blocks: dict[int, dict]) -> dict:
    support = {i: set(b['q_rows']) for i, b in blocks.items()}
    occ = {}
    for i, qs in support.items():
        for q in qs:
            occ.setdefault(q, set()).add(i)
    remaining = set(blocks)
    rounds = []
    while True:
        ready = {}
        for i in sorted(remaining):
            uq = tuple(q for q in support[i] if occ.get(q) == {i})
            if uq:
                ready[i] = uq
        if not ready:
            break
        rounds.append({
            'round': len(rounds),
            'blocks': {
                i: {
                    'm': int(blocks[i]['m']),
                    'source_shard': int(blocks[i]['source_shard']),
                    'unique_q': qs,
                    'unique_rows': sum(int(blocks[i]['q_rows'][q]) for q in qs),
                }
                for i, qs in ready.items()
            },
        })
        for i in ready:
            remaining.remove(i)
        for i in ready:
            for q in support[i]:
                occ[q].discard(i)
    return {
        'rounds': rounds,
        'proposal_blocks': sum(len(r['blocks']) for r in rounds),
        'proposal_columns': sum(
            int(rec['m']) for r in rounds for rec in r['blocks'].values()
        ),
        'proposal_remaining_ids': sorted(remaining),
        'proposal_remaining_columns': sum(int(blocks[i]['m']) for i in remaining),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--irrep', choices=TARGET, required=True)
    ap.add_argument('--metadata-dir', type=Path, required=True)
    ap.add_argument('--expected-shards', type=int, required=True)
    ap.add_argument('--pattern', default='*.pkl.gz')
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--json', type=Path, required=True)
    a = ap.parse_args()
    target_columns, target_blocks = TARGET[a.irrep]
    paths = sorted(a.metadata_dir.rglob(a.pattern))
    blocks, provenance, engine_blobs = load_metadata(paths, a.irrep, a.expected_shards)
    recovered_blocks = len(blocks)
    recovered_columns = sum(int(x['m']) for x in blocks.values())
    proposal = build_schedule(blocks)
    payload = {
        'schema_version': 1,
        'kind': 'BQG_MIXED_MASTER_KEY_CANDIDATE_SCHEDULE',
        'irrep': a.irrep,
        'target_blocks': target_blocks,
        'target_columns': target_columns,
        'recovered_blocks': recovered_blocks,
        'recovered_columns': recovered_columns,
        'engine_git_blob_shas': engine_blobs,
        'source_provenance_by_shard': provenance,
        **proposal,
        'status': (
            'SUPPORT_SCHEDULE_COMPLETE_CANDIDATE_ONLY'
            if not proposal['proposal_remaining_ids']
            else 'SUPPORT_SCHEDULE_HAS_RESIDUAL_CANDIDATE_ONLY'
        ),
        'structural_recompute_performed': False,
        'proof_status': 'NOT_A_NUMERICAL_RANK_CERTIFICATE',
        'validation_rule': (
            'Each proposed removal must pass SVD/full-column-rank on its original persisted C[i,q] '
            'for q unique in the current numerically validated remaining set. Any failed removal '
            'must remain present when uniqueness is replayed for later rounds.'
        ),
        'claim_boundary': (
            'Candidate schedule from actual persisted numerical output keys only. No geometric '
            'structural support, capacity or previously closed depth-6 structural proof is recomputed.'
        ),
    }
    with gzip.open(a.out, 'wb', compresslevel=9) as f:
        pickle.dump(payload, f, protocol=5)
    audit = {k: payload[k] for k in (
        'schema_version','kind','irrep','target_blocks','target_columns',
        'recovered_blocks','recovered_columns','engine_git_blob_shas','status',
        'proposal_blocks','proposal_columns','proposal_remaining_ids',
        'proposal_remaining_columns','structural_recompute_performed',
        'proof_status','validation_rule','claim_boundary')}
    audit['round_summaries'] = [
        {
            'round': r['round'],
            'blocks': len(r['blocks']),
            'columns': sum(int(x['m']) for x in r['blocks'].values()),
            'unique_rows': sum(int(x['unique_rows']) for x in r['blocks'].values()),
        }
        for r in payload['rounds']
    ]
    a.json.write_text(json.dumps(audit, indent=2, sort_keys=True) + '\n')
    print(json.dumps(audit, indent=2, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
