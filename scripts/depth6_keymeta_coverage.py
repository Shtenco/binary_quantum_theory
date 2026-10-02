#!/usr/bin/env python3
"""Fail-closed coverage validation for persisted depth-6 master-map key metadata.

This module operates only on persisted ``BQG_MIXED_MASTER_KEY_METADATA``
payloads.  It does not import or call shell/orbit/multiplicity/Jucys builders.
Coverage is a prerequisite for a later global actual-q schedule; it is never a
numerical rank certificate by itself.
"""
from __future__ import annotations


def validate_keymeta_coverage(
    records,
    *,
    irrep: str,
    expected_shards: int,
    target_blocks: int,
    target_columns: int,
) -> dict:
    shard_ids: set[int] = set()
    orbit_ids: set[int] = set()
    engine_blobs: set[str] = set()
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

        blocks = x.get('blocks', {})
        if not isinstance(blocks, dict):
            raise RuntimeError(f'shard {sid}: blocks must be an object')
        for i0, b in blocks.items():
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
            'full shard coverage but target mismatch '
            f'blocks={recovered_blocks}/{target_blocks} '
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
