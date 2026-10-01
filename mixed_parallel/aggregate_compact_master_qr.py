#!/usr/bin/env python3
"""Fail-closed aggregation of compact per-q QR factors.

This certifies only blocks that have output keys unique among the currently
remaining blocks.  For such a block, stacking the stored R_q factors has the
same singular values as stacking the original C_q maps.  A non-empty residual
is never promoted to a kernel claim; raw coupled maps are required for those
residual IDs so inter-block cross terms are retained.
"""
from __future__ import annotations

import argparse
import gzip
import json
import pickle
from pathlib import Path

import numpy as np

TARGET = {
    '32': (130903, 2755),
    '311': (153455, 2719),
    '221': (130503, 2749),
    '2111': (103318, 2712),
}
KIND = 'BQG_MIXED_MASTER_PER_Q_QR'


def load_compact(paths: list[Path], irrep: str, expected_shards: int):
    if len(paths) != expected_shards:
        raise RuntimeError(f'expected {expected_shards} compact shards, got {len(paths)}')
    blocks = {}
    shards = set()
    provenance = {}
    engine_blobs = set()
    for path in paths:
        with gzip.open(path, 'rb') as f:
            x = pickle.load(f)
        if x.get('kind') != KIND or int(x.get('schema_version', -1)) != 2:
            raise RuntimeError(f'{path}: wrong compact schema/kind')
        if x.get('irrep') != irrep:
            raise RuntimeError(f'{path}: wrong irrep {x.get("irrep")}')
        if int(x.get('shards', -1)) != expected_shards:
            raise RuntimeError(f'{path}: wrong shard count')
        shard = int(x['shard'])
        if shard in shards:
            raise RuntimeError(f'duplicate shard {shard}')
        shards.add(shard)
        provenance[str(shard)] = {
            'source_tar_sha256': x.get('source_tar_sha256'),
            'source_run_id': x.get('source_run_id'),
            'source_artifact_id': x.get('source_artifact_id'),
            'source_artifact_digest': x.get('source_artifact_digest'),
            'engine_git_blob_sha': x.get('engine_git_blob_sha'),
        }
        if x.get('engine_git_blob_sha'):
            engine_blobs.add(x['engine_git_blob_sha'])
        for i0, b in x.get('blocks', {}).items():
            i = int(i0)
            if i in blocks:
                raise RuntimeError(f'duplicate orbit block {i}')
            blocks[i] = b
    expected = set(range(expected_shards))
    if shards != expected:
        raise RuntimeError(
            f'shard coverage mismatch missing={sorted(expected-shards)} extra={sorted(shards-expected)}'
        )
    if len(engine_blobs) > 1:
        raise RuntimeError(f'multiple proof-engine blobs: {sorted(engine_blobs)}')
    return blocks, provenance, sorted(engine_blobs)


def certify_blocks(blocks: dict[int, dict], target_columns: int, target_blocks: int,
                   sigma_floor: float = 1e-10) -> dict:
    recovered_blocks = len(blocks)
    recovered_columns = sum(int(b['m']) for b in blocks.values())
    if recovered_blocks != target_blocks or recovered_columns != target_columns:
        return {
            'status': 'INPUT_COVERAGE_FAILURE',
            'target_blocks': target_blocks,
            'target_columns': target_columns,
            'recovered_blocks': recovered_blocks,
            'recovered_columns': recovered_columns,
            'structural_recompute_performed': False,
        }

    support = {i: set(b['qfactors']) for i, b in blocks.items()}
    occ = {}
    for i, qs in support.items():
        for q in qs:
            occ.setdefault(q, set()).add(i)

    remaining = set(blocks)
    passed = {}
    rounds = []
    while True:
        ready = []
        for i in sorted(remaining):
            b = blocks[i]
            m = int(b['m'])
            uq = [q for q in support[i] if occ.get(q) == {i}]
            if not uq:
                continue
            factors = []
            source_rows = 0
            for q in uq:
                item = b['qfactors'][q]
                r = np.asarray(item['R'])
                if r.ndim != 2 or r.shape[1] != m:
                    raise RuntimeError(f'orbit {i}, q={q!r}: bad R shape {r.shape}')
                factors.append(r)
                source_rows += int(item['rows'])
            if not factors:
                continue
            a = np.vstack(factors)
            if a.shape[0] < m:
                continue
            s = np.linalg.svd(a, compute_uv=False)
            smax = float(s[0]) if len(s) else 0.0
            tol = max(a.shape[0], m, source_rows) * np.finfo(float).eps * max(smax, 1.0) * 100.0
            sig = float(s[-1]) if len(s) >= m else 0.0
            rank = int(np.count_nonzero(s > tol))
            threshold = max(tol, sigma_floor)
            if rank == m and sig > threshold:
                ready.append((i, m, len(uq), int(a.shape[0]), source_rows, sig, tol))
        if not ready:
            break
        rounds.append({
            'round': len(rounds),
            'blocks': len(ready),
            'columns': sum(x[1] for x in ready),
            'sigma_min': min(x[5] for x in ready),
        })
        for i, m, nq, qr_rows, source_rows, sig, tol in ready:
            passed[str(i)] = {
                'm': m,
                'unique_q_keys': nq,
                'qr_rows': qr_rows,
                'source_rows': source_rows,
                'sigma_min': sig,
                'rank_tol': tol,
            }
        for i, *_ in ready:
            remaining.remove(i)
        for i, *_ in ready:
            for q in support[i]:
                occ[q].discard(i)

    residual_ids = sorted(remaining)
    residual_columns = sum(int(blocks[i]['m']) for i in residual_ids)
    certified_columns = sum(int(v['m']) for v in passed.values())
    full = not residual_ids and certified_columns == target_columns
    return {
        'status': 'PASS_CLOSED_FINITE_NUMERICAL' if full else 'RESIDUAL_RAW_COUPLED_CHECK_REQUIRED',
        'target_blocks': target_blocks,
        'target_columns': target_columns,
        'recovered_blocks': recovered_blocks,
        'recovered_columns': recovered_columns,
        'certified_blocks': len(passed),
        'certified_columns': certified_columns,
        'remaining_blocks': len(residual_ids),
        'remaining_columns': residual_columns,
        'remaining_ids': residual_ids,
        'rounds': rounds,
        'global_sigma_min': min((v['sigma_min'] for v in passed.values()), default=None),
        'kernel_dimension': 0 if full else None,
        'support_source': 'persisted_master_map_keys_only',
        'rank_source': 'stacked_reduced_QR_factors_of_persisted_master_maps',
        'structural_recompute_performed': False,
        'matching_failure_is_kernel': False,
        'h2_null_lift_forbidden_without_independent_true_kernel_check': True,
        'next_if_residual': (
            'Fetch raw persisted master maps only for remaining_ids and build the coupled residual '
            'master map/Gram including inter-block cross terms on shared q keys.'
        ) if residual_ids else None,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--irrep', choices=TARGET, required=True)
    ap.add_argument('--artifacts', type=Path, required=True)
    ap.add_argument('--expected-shards', type=int, required=True)
    ap.add_argument('--pattern', default='*.pkl.gz')
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--sigma-floor', type=float, default=1e-10)
    a = ap.parse_args()
    target_columns, target_blocks = TARGET[a.irrep]
    paths = sorted(a.artifacts.rglob(a.pattern))
    try:
        blocks, provenance, engine_blobs = load_compact(paths, a.irrep, a.expected_shards)
        out = certify_blocks(blocks, target_columns, target_blocks, a.sigma_floor)
        out['source_provenance_by_shard'] = provenance
        out['engine_git_blob_shas'] = engine_blobs
    except Exception as exc:
        out = {
            'status': 'INPUT_COVERAGE_FAILURE',
            'error': repr(exc),
            'target_blocks': target_blocks,
            'target_columns': target_columns,
            'structural_recompute_performed': False,
        }
    out.update({
        'schema_version': 2,
        'irrep': a.irrep,
        'structural_status': 'CLOSED_IMMUTABLE_INPUT',
        'claim_boundary': (
            'Independent finite numerical master witness from persisted-map QR factors. '
            'The already-closed depth-6 structural proof is not recomputed. A residual is '
            'not a kernel claim and requires raw coupled checking.'
        ),
    })
    a.out.write_text(json.dumps(out, indent=2, sort_keys=True, default=str) + '\n')
    print(json.dumps({k: out.get(k) for k in (
        'status','certified_blocks','certified_columns','remaining_blocks',
        'remaining_columns','global_sigma_min','kernel_dimension')}, indent=2))
    return 0 if out.get('status') == 'PASS_CLOSED_FINITE_NUMERICAL' else 2


if __name__ == '__main__':
    raise SystemExit(main())
