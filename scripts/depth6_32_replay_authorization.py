#!/usr/bin/env python3
"""Fail-closed authorization gate for depth-6 [3,2] numerical replay.

This gate authorizes an *attempt* to replay the already-frozen 2755-block
assignment identity through the pinned Stage-A numerical engine and the
frozen-m / KEYMETA-first contracts.  It does not certify actual-q coverage,
rank, kernel, or numerical closure.
"""
from __future__ import annotations

import hashlib
import json

TARGET_BLOCKS = 2755
TARGET_COLUMNS = 130903
NSHARDS = 112
SOURCE_STAGE_A_RUN_ID = 36899125190
FROZEN_ENGINE_COMMIT = '887e76fba5210524650002da0b54653d2c5b37fd'
FROZEN_ENGINE_BLOB_SHA = 'cbbaa80f6b6b61d353458db1fa1f03f824730532'
IDENTITY_SOURCE = 'DETERMINISTIC_REMATERIALIZATION_FROM_FROZEN_STAGE_A_ENGINE'
FROZEN_BASIS_CONTRACT = 'PASS_FROZEN_M_NUMERICAL_BASIS_ONLY'
KEYMETA_CONTRACT = 'BQG_DEPTH6_32_KEYMETA_FIRST_BLOCK'


def _require(cond: bool, msg: str) -> None:
    if not cond:
        raise RuntimeError(msg)


def _records_sha(records: list[dict]) -> str:
    raw = json.dumps(records, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode('utf-8')
    return hashlib.sha256(raw).hexdigest()


def authorize_replay(ledger: dict, gate: dict) -> dict:
    _require(isinstance(ledger, dict), 'rematerialized ledger must be an object')
    _require(isinstance(gate, dict), 'identity gate must be an object')
    _require(ledger.get('kind') == 'BQG_DEPTH6_32_REMATERIALIZED_ASSIGNMENT_LEDGER', 'wrong rematerialized ledger kind')
    _require(ledger.get('status') == 'COMPLETE_IDENTITY_REMATERIALIZATION_ONLY', 'identity is not complete/frozen')
    _require(int(ledger.get('target_blocks', -1)) == TARGET_BLOCKS, 'target block count mismatch')
    _require(int(ledger.get('target_columns', -1)) == TARGET_COLUMNS, 'target column count mismatch')
    _require(int(ledger.get('source_stage_a_run_id', -1)) == SOURCE_STAGE_A_RUN_ID, 'Stage-A run provenance mismatch')
    _require(ledger.get('frozen_engine_commit') == FROZEN_ENGINE_COMMIT, 'frozen engine commit mismatch')
    _require(ledger.get('frozen_bundle_blob_sha') == FROZEN_ENGINE_BLOB_SHA, 'frozen bundle blob mismatch')

    records = ledger.get('records', [])
    _require(isinstance(records, list) and len(records) == TARGET_BLOCKS, 'full identity must contain 2755 records')
    ids = set()
    columns = 0
    shards = set()
    for rec in records:
        oid = int(rec['orbit_id'])
        _require(oid not in ids, f'duplicate orbit {oid}')
        ids.add(oid)
        rep = rec.get('rep', [])
        _require(isinstance(rep, list) and len(rep) == 10, f'orbit {oid}: invalid rep')
        m = int(rec.get('m', 0))
        d = int(rec.get('coord_dim', 0))
        shard = int(rec.get('source_shard', -1))
        _require(m > 0 and d > 0, f'orbit {oid}: non-positive dimensions')
        _require(0 <= shard < NSHARDS, f'orbit {oid}: invalid source_shard')
        _require(rec.get('identity_source') == IDENTITY_SOURCE, f'orbit {oid}: identity source mismatch')
        _require(rec.get('frozen_engine_commit') == FROZEN_ENGINE_COMMIT, f'orbit {oid}: frozen engine commit mismatch')
        _require(rec.get('frozen_bundle_blob_sha') == FROZEN_ENGINE_BLOB_SHA, f'orbit {oid}: frozen bundle blob mismatch')
        _require(int(rec.get('source_stage_a_run_id', -1)) == SOURCE_STAGE_A_RUN_ID, f'orbit {oid}: Stage-A run mismatch')
        columns += m
        shards.add(shard)

    _require(columns == TARGET_COLUMNS, f'column sum mismatch {columns}!={TARGET_COLUMNS}')
    _require(shards == set(range(NSHARDS)), f'112-shard coverage mismatch: got {len(shards)} shards')
    if ledger.get('identity_sha256') is not None:
        _require(ledger['identity_sha256'] == _records_sha(records), 'rematerialized identity SHA mismatch')

    _require(gate.get('kind') == 'BQG_DEPTH6_32_IDENTITY_REMATERIALIZATION_GATE', 'wrong identity gate kind')
    _require(gate.get('status') == 'PASS_IDENTITY_REMATERIALIZATION_ONLY', 'identity gate did not pass')
    _require(int(gate.get('blocks', -1)) == TARGET_BLOCKS and int(gate.get('columns', -1)) == TARGET_COLUMNS, 'identity gate target mismatch')
    _require(int(gate.get('persisted_identity_matches', -1)) == 15, 'persisted identity cross-check mismatch')
    _require(int(gate.get('historical_batch_matches', -1)) == 102, 'historical batch cross-check mismatch')
    _require(gate.get('rank_certified') is False, 'identity gate must not claim rank')
    _require(gate.get('actual_q_coverage_certified') is False, 'identity gate must not claim actual-q coverage')
    _require(gate.get('numerical_closure_claimed') is False, 'identity gate must not claim numerical closure')
    _require(ledger.get('rank_certified') is False, 'identity ledger must not claim rank')
    _require(ledger.get('actual_q_coverage_certified') is False, 'identity ledger must not claim actual-q coverage')
    _require(ledger.get('numerical_closure_claimed') is False, 'identity ledger must not claim numerical closure')

    return {
        'schema_version': 1,
        'kind': 'BQG_DEPTH6_32_NUMERICAL_REPLAY_AUTHORIZATION',
        'status': 'AUTHORIZED_NUMERICAL_REPLAY_ATTEMPT',
        'numerical_replay_authorized': True,
        'blocks': TARGET_BLOCKS,
        'columns': TARGET_COLUMNS,
        'nshards': NSHARDS,
        'covered_shards': len(shards),
        'source_stage_a_run_id': SOURCE_STAGE_A_RUN_ID,
        'frozen_engine_commit': FROZEN_ENGINE_COMMIT,
        'frozen_bundle_blob_sha': FROZEN_ENGINE_BLOB_SHA,
        'identity_sha256': ledger.get('identity_sha256'),
        'frozen_basis_contract': FROZEN_BASIS_CONTRACT,
        'keymeta_first_contract': KEYMETA_CONTRACT,
        'structural_recompute_authorized': False,
        'multiplicity_recompute_authorized': False,
        'actual_q_coverage_certified': False,
        'rank_certified': False,
        'numerical_closure_claimed': False,
        'claim_boundary': (
            'Authorizes only a fail-closed numerical replay attempt from the complete frozen '
            'assignment identity through the pinned Stage-A engine and frozen-m/KEYMETA-first '
            'contracts. It does not certify successful replay, actual-q coverage, rank, kernel, '
            'or numerical closure of [3,2].'
        ),
    }
