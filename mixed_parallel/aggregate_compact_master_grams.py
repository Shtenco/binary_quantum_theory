#!/usr/bin/env python3
"""Aggregate compact per-q Grams into a fail-closed numerical peeling witness.

Input files are produced by compress_master_map_grams.py from already-computed
master maps. No structural geometry is reconstructed here.

For one block i and a set Q of output-row keys unique among the currently
remaining blocks,

  G_i(Q) = sum_{q in Q} C[i,q]^dagger C[i,q]

is positive definite iff the stacked numerical master image on those rows has
full column rank. Thus a positive-definite block may be removed. Repeat until
no more blocks pass. A nonempty residual is NOT a kernel claim; it is a list of
raw numerical blocks that need a coupled cross-block Gram check.
"""
from __future__ import annotations

import argparse
import gzip
import json
import math
import pickle
from pathlib import Path

import numpy as np

TARGET = {
    '32': (130903, 2755),
    '311': (153455, 2719),
    '221': (130503, 2749),
    '2111': (103318, 2712),
}


def unpack_upper(v: np.ndarray, m: int) -> np.ndarray:
    v = np.asarray(v)
    want = m * (m + 1) // 2
    if v.size != want:
        raise ValueError(f'packed Gram length {v.size} != {want} for m={m}')
    g = np.zeros((m, m), dtype=v.dtype)
    ii = np.triu_indices(m)
    g[ii] = v
    g[(ii[1], ii[0])] = np.conjugate(v)
    d = np.diag_indices(m)
    g[d] = np.real(g[d])
    return g


def load_compact(paths: list[Path], irrep: str, expected_shards: int):
    if len(paths) != expected_shards:
        raise RuntimeError(f'expected {expected_shards} compact shards, got {len(paths)}')
    blocks = {}
    shards = set()
    source_hashes = {}
    for path in paths:
        with gzip.open(path, 'rb') as f:
            x = pickle.load(f)
        if x.get('kind') != 'BQG_MIXED_MASTER_PER_Q_GRAMS':
            raise RuntimeError(f'{path}: wrong kind')
        if x.get('irrep') != irrep:
            raise RuntimeError(f'{path}: wrong irrep {x.get("irrep")}')
        if int(x.get('shards', -1)) != expected_shards:
            raise RuntimeError(f'{path}: wrong shard count')
        shard = int(x['shard'])
        if shard in shards:
            raise RuntimeError(f'duplicate shard {shard}')
        shards.add(shard)
        source_hashes[str(shard)] = x.get('source_tar_sha256')
        for i0, b in x.get('blocks', {}).items():
            i = int(i0)
            if i in blocks:
                raise RuntimeError(f'duplicate orbit block {i}')
            blocks[i] = b
    if shards != set(range(expected_shards)):
        miss = sorted(set(range(expected_shards)) - shards)
        extra = sorted(shards - set(range(expected_shards)))
        raise RuntimeError(f'shard coverage mismatch missing={miss} extra={extra}')
    return blocks, source_hashes


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

    support = {i: set(b['qgrams']) for i, b in blocks.items()}
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
            g = None
            rows = 0
            for q in uq:
                item = b['qgrams'][q]
                gg = unpack_upper(item['packed_upper'], m)
                g = gg if g is None else g + gg
                rows += int(item['rows'])
            if g is None:
                continue
            g = (g + g.conjugate().T) * 0.5
            evals = np.linalg.eigvalsh(g)
            lam_max = float(max(evals[-1], 0.0)) if len(evals) else 0.0
            tol_lam = max(m, rows) * np.finfo(float).eps * max(lam_max, 1.0) * 200.0
            floor_lam = sigma_floor * sigma_floor
            lam_min = float(evals[0]) if len(evals) else 0.0
            # Compare in Gram units. Requiring both numerical eig tolerance and
            # explicit sigma floor makes the witness fail closed.
            threshold = max(tol_lam, floor_lam)
            if lam_min > threshold:
                ready.append((i, m, len(uq), rows, lam_min, math.sqrt(lam_min), threshold))
        if not ready:
            break
        rounds.append({
            'round': len(rounds),
            'blocks': len(ready),
            'columns': sum(x[1] for x in ready),
            'sigma_min': min(x[5] for x in ready),
        })
        for i, m, nq, rows, lam, sig, thr in ready:
            passed[str(i)] = {
                'm': m,
                'unique_q_keys': nq,
                'rows': rows,
                'lambda_min': lam,
                'sigma_min': sig,
                'gram_threshold': thr,
            }
        for i, *_ in ready:
            remaining.remove(i)
        for i, *_ in ready:
            for q in support[i]:
                if q in occ:
                    occ[q].discard(i)

    residual_ids = sorted(remaining)
    residual_columns = sum(int(blocks[i]['m']) for i in residual_ids)
    passed_columns = sum(int(v['m']) for v in passed.values())
    full = not residual_ids and passed_columns == target_columns
    return {
        'status': 'PASS_CLOSED_FINITE_NUMERICAL' if full else 'RESIDUAL_RAW_CROSS_BLOCK_GRAM_REQUIRED',
        'target_blocks': target_blocks,
        'target_columns': target_columns,
        'recovered_blocks': recovered_blocks,
        'recovered_columns': recovered_columns,
        'certified_blocks': len(passed),
        'certified_columns': passed_columns,
        'remaining_blocks': len(residual_ids),
        'remaining_columns': residual_columns,
        'remaining_ids': residual_ids,
        'rounds': rounds,
        'global_sigma_min': min((v['sigma_min'] for v in passed.values()), default=None),
        'kernel_dimension': 0 if full else None,
        'support_source': 'persisted_master_map_keys_only',
        'rank_source': 'sum_of_persisted_per_q_master_grams',
        'structural_recompute_performed': False,
        'matching_failure_is_kernel': False,
        'h2_null_lift_forbidden_without_independent_true_kernel_check': True,
        'next_if_residual': (
            'Download raw persisted master maps only for remaining_ids and build '
            'the coupled residual C^dagger C including cross-block terms.'
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
        blocks, hashes = load_compact(paths, a.irrep, a.expected_shards)
        out = certify_blocks(blocks, target_columns, target_blocks, a.sigma_floor)
        out['source_tar_sha256_by_shard'] = hashes
    except Exception as exc:
        out = {
            'status': 'INPUT_COVERAGE_FAILURE',
            'error': repr(exc),
            'target_blocks': target_blocks,
            'target_columns': target_columns,
            'structural_recompute_performed': False,
        }
    out.update({
        'schema_version': 1,
        'irrep': a.irrep,
        'structural_status': 'CLOSED_IMMUTABLE_INPUT',
        'claim_boundary': (
            'Independent finite numerical master witness from compact Grams. '
            'Structural depth-6 proof is not recomputed.'
        ),
    })
    a.out.write_text(json.dumps(out, indent=2, sort_keys=True, default=str) + '\n')
    print(json.dumps({k: out.get(k) for k in (
        'status','certified_blocks','certified_columns','remaining_blocks',
        'remaining_columns','global_sigma_min','kernel_dimension')}, indent=2))
    return 0 if out.get('status') == 'PASS_CLOSED_FINITE_NUMERICAL' else 2


if __name__ == '__main__':
    raise SystemExit(main())
