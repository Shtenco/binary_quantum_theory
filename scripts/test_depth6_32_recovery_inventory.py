#!/usr/bin/env python3
import gzip
import hashlib
import json
import pickle
import tempfile
import unittest
from pathlib import Path

import depth6_32_recovery_inventory as I


class RecoveryInventoryTests(unittest.TestCase):
    def _write_artifact(self, root: Path, name: str, status: str, blocks):
        d = root / name
        (d / 'blocks').mkdir(parents=True)
        records = []
        for block in blocks:
            p = d / 'blocks' / f"orbit-{int(block['orbit_id']):04d}.keymeta.pkl.gz"
            with gzip.open(p, 'wb') as f:
                pickle.dump(block, f, protocol=pickle.HIGHEST_PROTOCOL)
            sha = hashlib.sha256(p.read_bytes()).hexdigest()
            records.append({
                'orbit_id': int(block['orbit_id']),
                'm': int(block['m']),
                'keymeta_file': p.name,
                'keymeta_sha256': sha,
                'q_key_count': int(block.get('q_key_count', 0)),
                'rows': int(block.get('rows', 0)),
            })
        manifest = {
            'schema_version': 1,
            'status': status,
            'records': records,
            'completed_blocks': len(records),
            'completed_columns': sum(r['m'] for r in records),
            'rank_certified': False,
            'numerical_closure_claimed': False,
        }
        (d / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
        return d / 'manifest.json'

    def test_merges_source_and_recovery_payloads_and_reports_exact_columns(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self._write_artifact(root, 'source', 'PASS_KEYMETA_FIRST_SHARD_COMPLETE', [
                {'orbit_id': 1, 'm': 2, 'q_rows': {('a',): 3}, 'q_key_count': 1, 'rows': 3},
            ])
            self._write_artifact(root, 'recovery', 'PASS_KEYMETA_RECOVERY_CHUNK_COMPLETE', [
                {'orbit_id': 2, 'm': 3, 'q_rows': {('b',): 4}, 'q_key_count': 1, 'rows': 4},
                {'orbit_id': 3, 'm': 5, 'q_rows': {('c',): 6}, 'q_key_count': 1, 'rows': 6},
            ])
            inv = I.inventory_keymeta_roots([root])
            self.assertEqual(inv['completed_blocks'], 3)
            self.assertEqual(inv['completed_columns'], 10)
            self.assertEqual(inv['completed_orbit_ids'], [1, 2, 3])
            self.assertEqual(inv['duplicate_orbits_collapsed'], 0)
            self.assertFalse(inv['rank_certified'])
            self.assertFalse(inv['numerical_closure_claimed'])
            blocks = I.load_unique_keymeta_blocks([root])
            self.assertEqual([int(b['orbit_id']) for b in blocks], [1, 2, 3])
            self.assertEqual(sum(int(b['m']) for b in blocks), 10)

    def test_identical_duplicate_payload_is_collapsed_but_conflict_fails(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            block = {'orbit_id': 7, 'm': 4, 'q_rows': {('q',): 2}, 'q_key_count': 1, 'rows': 2}
            self._write_artifact(root, 'a', 'PASS_KEYMETA_FIRST_SHARD_COMPLETE', [block])
            self._write_artifact(root, 'b', 'PASS_KEYMETA_RECOVERY_CHUNK_COMPLETE', [dict(block)])
            inv = I.inventory_keymeta_roots([root])
            self.assertEqual(inv['completed_blocks'], 1)
            self.assertEqual(inv['completed_columns'], 4)
            self.assertEqual(inv['duplicate_orbits_collapsed'], 1)
            blocks = I.load_unique_keymeta_blocks([root])
            self.assertEqual(len(blocks), 1)
            self.assertEqual(int(blocks[0]['orbit_id']), 7)

            conflict = dict(block)
            conflict['m'] = 5
            self._write_artifact(root, 'c', 'PASS_KEYMETA_RECOVERY_CHUNK_COMPLETE', [conflict])
            with self.assertRaisesRegex(RuntimeError, 'conflicting duplicate orbit 7'):
                I.inventory_keymeta_roots([root])
            with self.assertRaisesRegex(RuntimeError, 'conflicting duplicate orbit 7'):
                I.load_unique_keymeta_blocks([root])

    def test_duplicate_q_rows_order_does_not_create_false_conflict(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            a = {
                'orbit_id': 8,
                'm': 2,
                'q_rows': {('z', 2): 4, ('a', 1): 3},
                'q_key_count': 2,
                'rows': 7,
                'frozen_assignment_sha256': 'abc',
                'kind': 'BQG_DEPTH6_32_KEYMETA_FIRST_BLOCK',
                'irrep': '[3,2]',
                'irrep_key': '32',
            }
            b = dict(a)
            b['q_rows'] = {('a', 1): 3, ('z', 2): 4}
            self._write_artifact(root, 'a', 'PASS_KEYMETA_FIRST_SHARD_COMPLETE', [a])
            self._write_artifact(root, 'b', 'PASS_KEYMETA_RECOVERY_CHUNK_COMPLETE', [b])
            inv = I.inventory_keymeta_roots([root])
            self.assertEqual(inv['completed_orbit_ids'], [8])
            self.assertEqual(inv['duplicate_orbits_collapsed'], 1)
            blocks = I.load_unique_keymeta_blocks([root])
            self.assertEqual(len(blocks), 1)
            self.assertEqual(int(blocks[0]['orbit_id']), 8)

    def test_manifest_sha_mismatch_fails_closed(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            mp = self._write_artifact(root, 'x', 'PASS_KEYMETA_RECOVERY_CHUNK_COMPLETE', [
                {'orbit_id': 9, 'm': 2, 'q_rows': {('x',): 1}, 'q_key_count': 1, 'rows': 1},
            ])
            m = json.loads(mp.read_text())
            m['records'][0]['keymeta_sha256'] = '0' * 64
            mp.write_text(json.dumps(m) + '\n')
            with self.assertRaisesRegex(RuntimeError, 'keymeta sha mismatch'):
                I.inventory_keymeta_roots([root])

    def test_manifest_count_or_column_mismatch_fails_closed(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            mp = self._write_artifact(root, 'x', 'PASS_KEYMETA_FIRST_SHARD_COMPLETE', [
                {'orbit_id': 11, 'm': 3, 'q_rows': {('x',): 1}, 'q_key_count': 1, 'rows': 1},
            ])
            m = json.loads(mp.read_text())
            m['completed_columns'] = 99
            mp.write_text(json.dumps(m) + '\n')
            with self.assertRaisesRegex(RuntimeError, 'manifest completed_columns mismatch'):
                I.inventory_keymeta_roots([root])

    def test_rejects_non_pass_manifest_and_bad_payload_identity(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            mp = self._write_artifact(root, 'x', 'BROKEN', [
                {'orbit_id': 13, 'm': 1, 'q_rows': {('x',): 1}, 'q_key_count': 1, 'rows': 1},
            ])
            with self.assertRaisesRegex(RuntimeError, 'non-PASS manifest'):
                I.inventory_keymeta_roots([root])

            m = json.loads(mp.read_text())
            m['status'] = 'PASS_KEYMETA_RECOVERY_CHUNK_COMPLETE'
            mp.write_text(json.dumps(m) + '\n')
            p = next((mp.parent / 'blocks').glob('*.gz'))
            with gzip.open(p, 'wb') as f:
                pickle.dump({'orbit_id': 14, 'm': 1, 'q_rows': {('x',): 1}}, f)
            m['records'][0]['keymeta_sha256'] = hashlib.sha256(p.read_bytes()).hexdigest()
            mp.write_text(json.dumps(m) + '\n')
            with self.assertRaisesRegex(RuntimeError, 'payload orbit_id mismatch'):
                I.inventory_keymeta_roots([root])


if __name__ == '__main__':
    unittest.main()
