#!/usr/bin/env python3
"""Fail-closed integrity verifier for the canonical depth-6 [3,2] recovery frontier.

Passing this verifier means the recovery state is internally consistent and the
canonical recovery implementation is present.  It does *not* certify numerical
rank closure of [3,2].
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

EXPECTED_SHARDS = [0, 6, 8, 11, 12, 13, 14, 17, 18, 19, 20, 21, 22, 23, 24]
REQUIRED_FILES = (
    'scripts/depth6_keymeta_coverage.py',
    'scripts/inventory_depth6_32_keymeta.py',
)


def _require(cond: bool, msg: str) -> None:
    if not cond:
        raise RuntimeError(msg)


def verify(recovery: dict, depth6: dict, root: Path) -> dict:
    _require(int(recovery.get('schema_version', -1)) >= 5, 'recovery frontier schema must be >= 5')
    _require(recovery.get('irrep') == '[3,2]', 'recovery frontier irrep must be [3,2]')
    _require(recovery.get('structural_status') == 'CLOSED_IMMUTABLE_INPUT', 'structural input must remain immutable')
    _require(recovery.get('numerical_status') == 'RECOVER_OR_FINISH', '[3,2] numerical status must remain RECOVER_OR_FINISH')
    _require(int(recovery.get('target_blocks', -1)) == 2755, 'target blocks drifted from 2755')
    _require(int(recovery.get('target_columns', -1)) == 130903, 'target columns drifted from 130903')

    _require(depth6.get('multiplicities', {}).get('[3,2]') == 130903, 'depth6 [3,2] multiplicity mismatch')
    ss = depth6.get('structural_support', {}).get('[3,2]', {})
    _require(ss.get('status') == 'CLOSED', 'depth6 [3,2] structural support must remain CLOSED')
    _require(ss.get('blocks') == '2755/2755', 'depth6 [3,2] structural block target mismatch')
    _require(ss.get('columns') == '130903/130903', 'depth6 [3,2] structural column target mismatch')
    nw = depth6.get('numerical_master_witnesses', {}).get('[3,2]', {})
    _require(nw.get('status') == 'RECOVER_OR_FINISH', 'depth6 [3,2] numerical frontier was unexpectedly promoted')
    _require(nw.get('dimension') == 130903 and nw.get('blocks') == 2755, 'depth6 [3,2] witness dimensions drifted')
    _require(depth6.get('current_numerical_witness') == '[3,2]', 'current numerical witness must remain [3,2]')
    _require(depth6.get('finite_depth6_theorem_status') == 'NOT_YET_PROVED', 'finite depth-6 theorem cannot be promoted while [3,2] is incomplete')

    raw = recovery.get('raw_present_shards', [])
    keymeta = recovery.get('keymeta_preserved_shards', [])
    _require(raw == EXPECTED_SHARDS, f'raw shard frontier mismatch: {raw}')
    _require(keymeta == EXPECTED_SHARDS, f'keymeta shard frontier mismatch: {keymeta}')
    _require(recovery.get('raw_present_count') == 15, 'raw_present_count must be 15')
    _require(recovery.get('keymeta_preserved_count') == 15, 'keymeta_preserved_count must be 15')

    cov = recovery.get('coverage_inventory', {})
    _require(cov.get('status') == 'INCOMPLETE_KEYMETA_COVERAGE', 'coverage must still be explicitly incomplete')
    _require(cov.get('recovered_shards') == 15, 'coverage recovered_shards must be 15')
    _require(cov.get('recovered_blocks') == 15, 'coverage recovered_blocks must be 15')
    _require(cov.get('recovered_columns') == 7749, 'coverage recovered_columns must be 7749')
    _require(cov.get('schedule_allowed') is False, 'schedule_allowed must remain false until exact complete coverage')
    _require(cov.get('next_action') == 'RECOVER_MISSING_KEYMETA_SHARDS_ONLY', 'coverage next action drifted')

    exact = recovery.get('exact_recovered_identity', {})
    _require(exact.get('blocks') == 15 and exact.get('columns') == 7749, 'exact recovered identity mismatch')

    retry = recovery.get('targeted_retry', {})
    _require(retry.get('disposition') == 'QUARANTINED_NONCANONICAL_FOR_RECOVERY', 'targeted retry must remain quarantined')
    _require(retry.get('required_replacement') == 'LEDGER_DRIVEN_NUMERICAL_RETRY_FROM_PERSISTED_FROZEN_ASSIGNMENTS_ONLY', 'targeted retry replacement contract drifted')

    rules = recovery.get('rules', {})
    false_rules = (
        'structural_recompute_performed',
        'multiplicity_recompute_performed',
        'jucys_recompute_performed',
    )
    true_rules = (
        'forbid_future_recovery_bootstrap_of_shell_orbits_multiplicity_or_jucys',
        'canonical_retry_requires_persisted_assignment_ledger',
        'raw_artifact_presence_is_not_rank_evidence',
        'keymeta_is_not_rank_evidence',
        'subset_q_uniqueness_is_not_rank_evidence',
        'global_candidate_schedule_requires_112_of_112_actual_q_occupancy',
        'svd_removal_requires_full_column_rank_and_sigma_min_threshold',
        'failed_svd_candidate_remains_present_during_fail_closed_replay',
    )
    for k in false_rules:
        _require(rules.get(k) is False, f'{k} must remain false')
    for k in true_rules:
        _require(rules.get(k) is True, f'{k} must remain true')

    for rel in REQUIRED_FILES:
        _require((root / rel).is_file(), f'missing canonical recovery implementation: {rel}')

    claim = str(recovery.get('claim_boundary', ''))
    _require('does not certify rank(C_32)=130903' in claim, 'claim boundary must deny [3,2] rank certification')
    _require('does not close [3,2] numerically' in claim, 'claim boundary must deny [3,2] numerical closure')

    return {
        'status': 'PASS_CANONICAL_RECOVERY_FRONTIER_INCOMPLETE',
        'numerical_closure_claimed': False,
        'schedule_allowed': False,
        'recovered_shards': 15,
        'recovered_blocks': 15,
        'recovered_columns': 7749,
        'target_blocks': 2755,
        'target_columns': 130903,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--recovery', type=Path, default=Path('BQG_DEPTH6_32_RECOVERY_FRONTIER_2026-10-02.json'))
    ap.add_argument('--depth6', type=Path, default=Path('depth6_frontier.json'))
    ap.add_argument('--root', type=Path, default=Path('.'))
    args = ap.parse_args()
    recovery = json.loads(args.recovery.read_text())
    depth6 = json.loads(args.depth6.read_text())
    result = verify(recovery, depth6, args.root)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
