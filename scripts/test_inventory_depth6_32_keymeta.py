#!/usr/bin/env python3
import gzip
import io
import pickle
import tempfile
import unittest
import zipfile
from pathlib import Path

import inventory_depth6_32_keymeta as I


def payload(shard: int) -> dict:
    return {
        'kind': 'BQG_MIXED_MASTER_KEY_METADATA',
        'schema_version': 1,
        'irrep': '32',
        'shard': shard,
        'shards': 112,
        'source_run_id': '36899125190',
        'source_artifact_id': 1000 + shard,
        'source_artifact_digest': f'sha256:raw-{shard}',
        'source_tar_sha256': f'tar-{shard}',
        'assigned_blocks': 1,
        'assigned_columns': 10 + shard,
        'records': [],
        'stats': {'blocks': 1, 'columns': 10 + shard, 'q_keys': 1, 'output_bytes': 1},
    }


def gz_pickle(x: dict) -> bytes:
    b = io.BytesIO()
    with gzip.GzipFile(fileobj=b, mode='wb') as g:
        pickle.dump(x, g, protocol=pickle.HIGHEST_PROTOCOL)
    return b.getvalue()


class InventoryArtifactTests(unittest.TestCase):
    def test_load_payloads_from_zip_accepts_multi_shard_salvage(self):
        with tempfile.TemporaryDirectory() as td:
            zp = Path(td) / 'salvage.zip'
            with zipfile.ZipFile(zp, 'w') as z:
                z.writestr('stagea32_keymeta/bqg-mixed-32-shard-1-keymeta.pkl.gz', gz_pickle(payload(1)))
                z.writestr('stagea32_keymeta/bqg-mixed-32-shard-2-keymeta.pkl.gz', gz_pickle(payload(2)))
                z.writestr('stagea32_keymeta/manifest.json', '{}')
            got = I.load_payloads_from_zip(zp)
            self.assertEqual([1, 2], sorted(int(x['shard']) for x in got))

    def test_artifact_name_filter_accepts_single_and_salvage(self):
        self.assertTrue(I.is_candidate_keymeta_artifact_name('bqg-mixed-32-shard-17-keymeta'))
        self.assertTrue(I.is_candidate_keymeta_artifact_name('bqg-depth6-32-stagea-keymeta-salvage-36899125190'))
        self.assertFalse(I.is_candidate_keymeta_artifact_name('bqg-mixed-311-shard-17-keymeta'))
        self.assertFalse(I.is_candidate_keymeta_artifact_name('random-artifact'))


if __name__ == '__main__':
    unittest.main()
