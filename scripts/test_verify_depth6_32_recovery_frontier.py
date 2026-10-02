#!/usr/bin/env python3
import json
import tempfile
import unittest
from pathlib import Path

import depth6_assignment_ledger as L
import verify_depth6_32_recovery_frontier as V


def recovery() -> dict:
    return {
        'schema_version': 5,
        'irrep': '[3,2]',
        'structural_status': 'CLOSED_IMMUTABLE_INPUT',
        'numerical_status': 'RECOVER_OR_FINISH',
        'target_blocks': 2755,
        'target_columns': 130903,
        'source_stage_a_run_id': 36899125190,
        'source_engine_git_blob_sha': 'cbbaa80f6b6b61d353458db1fa1f03f824730532',
        'coverage_inventory': {
            'status': 'INCOMPLETE_KEYMETA_COVERAGE',
            'recovered_shards': 15,
            'recovered_blocks': 15,
            'recovered_columns': 7749,
            'schedule_allowed': False,
            'next_action': 'RECOVER_MISSING_KEYMETA_SHARDS_ONLY',
        },
        'targeted_retry': {
            'disposition': 'QUARANTINED_NONCANONICAL_FOR_RECOVERY',
            'required_replacement': 'LEDGER_DRIVEN_NUMERICAL_RETRY_FROM_PERSISTED_FROZEN_ASSIGNMENTS_ONLY',
        },
        'raw_present_shards': [0,6,8,11,12,13,14,17,18,19,20,21,22,23,24],
        'raw_present_count': 15,
        'keymeta_preserved_shards': [0,6,8,11,12,13,14,17,18,19,20,21,22,23,24],
        'keymeta_preserved_count': 15,
        'exact_recovered_identity': {'blocks': 15, 'columns': 7749},
        'rules': {
            'structural_recompute_performed': False,
            'multiplicity_recompute_performed': False,
            'jucys_recompute_performed': False,
            'forbid_future_recovery_bootstrap_of_shell_orbits_multiplicity_or_jucys': True,
            'canonical_retry_requires_persisted_assignment_ledger': True,
            'raw_artifact_presence_is_not_rank_evidence': True,
            'keymeta_is_not_rank_evidence': True,
            'subset_q_uniqueness_is_not_rank_evidence': True,
            'global_candidate_schedule_requires_112_of_112_actual_q_occupancy': True,
            'svd_removal_requires_full_column_rank_and_sigma_min_threshold': True,
            'failed_svd_candidate_remains_present_during_fail_closed_replay': True,
        },
        'claim_boundary': 'Recovery/provenance snapshot only. It does not certify rank(C_32)=130903 and does not close [3,2] numerically.',
    }


def depth6() -> dict:
    return {
        'multiplicities': {'[3,2]': 130903},
        'structural_support': {'[3,2]': {'status': 'CLOSED', 'blocks': '2755/2755', 'columns': '130903/130903'}},
        'numerical_master_witnesses': {'[3,2]': {'status': 'RECOVER_OR_FINISH', 'dimension': 130903, 'blocks': 2755}},
        'current_numerical_witness': '[3,2]',
        'finite_depth6_theorem_status': 'NOT_YET_PROVED',
    }


def assignment_record(i: int, m: int) -> dict:
    return {
        'orbit_id': 1000 + i,
        'rep': [1,2,3,4,3,2,3,4,3,2],
        'm': m,
        'coord_dim': 4*m,
        'source_shard': i,
        'source_keymeta_payload_sha256': f'{i:064x}',
        'source_raw_run_id': '36899125190',
        'source_raw_artifact_id': str(2000+i),
        'source_raw_artifact_digest': 'sha256:' + f'{3000+i:064x}',
        'source_tar_sha256': f'{4000+i:064x}',
        'engine_git_blob_sha': 'c'*40,
    }


def setup_root(root: Path, *, include_inventory=True, include_assignment=True) -> None:
    (root / 'scripts').mkdir()
    (root / 'scripts' / 'depth6_keymeta_coverage.py').write_text('# canonical\n')
    (root / 'scripts' / 'depth6_assignment_ledger.py').write_text('# canonical\n')
    if include_inventory:
        (root / 'scripts' / 'inventory_depth6_32_keymeta.py').write_text('# canonical\n')
    if include_assignment:
        records = [assignment_record(i, 500) for i in range(14)] + [assignment_record(14, 749)]
        ledger = L.build_assignment_ledger(records, target_blocks=2755, target_columns=130903)
        (root / 'BQG_DEPTH6_32_ASSIGNMENT_LEDGER_2026-10-02.json').write_text(json.dumps(ledger))


class RecoveryFrontierTests(unittest.TestCase):
    def test_valid_incomplete_frontier_passes_integrity_gate_without_closing_32(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); setup_root(root)
            got = V.verify(recovery(), depth6(), root)
            self.assertEqual('PASS_CANONICAL_RECOVERY_FRONTIER_INCOMPLETE', got['status'])
            self.assertFalse(got['schedule_allowed'])
            self.assertFalse(got['numerical_closure_claimed'])
            self.assertFalse(got['assignment_retry_allowed'])

    def test_schedule_true_on_15_shards_fails_closed(self):
        r = recovery(); r['coverage_inventory']['schedule_allowed'] = True
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); setup_root(root)
            with self.assertRaisesRegex(RuntimeError, 'schedule_allowed must remain false'):
                V.verify(r, depth6(), root)

    def test_non_quarantined_targeted_retry_fails(self):
        r = recovery(); r['targeted_retry']['disposition'] = 'ADMITTED'
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); setup_root(root)
            with self.assertRaisesRegex(RuntimeError, 'targeted retry'):
                V.verify(r, depth6(), root)

    def test_missing_canonical_inventory_file_fails(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); setup_root(root, include_inventory=False)
            with self.assertRaisesRegex(RuntimeError, 'missing canonical recovery implementation'):
                V.verify(recovery(), depth6(), root)

    def test_missing_assignment_ledger_fails(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); setup_root(root, include_assignment=False)
            with self.assertRaisesRegex(RuntimeError, 'missing persisted assignment ledger'):
                V.verify(recovery(), depth6(), root)

    def test_assignment_coverage_must_match_recovery_identity(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); setup_root(root)
            ledger_path = root / 'BQG_DEPTH6_32_ASSIGNMENT_LEDGER_2026-10-02.json'
            ledger = json.loads(ledger_path.read_text())
            ledger['coverage']['persisted_columns'] = 7000
            ledger_path.write_text(json.dumps(ledger))
            with self.assertRaisesRegex(RuntimeError, 'assignment ledger'):
                V.verify(recovery(), depth6(), root)

    def test_promoted_depth6_theorem_fails_while_32_incomplete(self):
        d = depth6(); d['finite_depth6_theorem_status'] = 'PROVED'
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); setup_root(root)
            with self.assertRaisesRegex(RuntimeError, 'finite depth-6 theorem'):
                V.verify(recovery(), d, root)


if __name__ == '__main__':
    unittest.main()
