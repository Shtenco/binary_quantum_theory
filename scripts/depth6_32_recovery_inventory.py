#!/usr/bin/env python3
from __future__ import annotations

import gzip
import hashlib
import json
import pickle
from pathlib import Path
from typing import Iterable

from depth6_32_keymeta_aggregate import QKEY_ENCODING, q_key_to_text

PASS_STATUSES = {
    'PASS_KEYMETA_FIRST_SHARD_COMPLETE',
    'PASS_KEYMETA_RECOVERY_CHUNK_COMPLETE',
}


def _find_payload(manifest_path: Path, keymeta_file: str) -> Path:
    direct = manifest_path.parent / 'blocks' / keymeta_file
    if direct.exists():
        return direct
    matches = list(manifest_path.parent.rglob(keymeta_file))
    if len(matches) != 1:
        raise RuntimeError(
            f'cannot resolve keymeta payload for {manifest_path}: {keymeta_file!r} matches={len(matches)}'
        )
    return matches[0]


def _payload_fingerprint(block: dict) -> str:
    q_rows = block.get('q_rows', {})
    if not isinstance(q_rows, dict):
        raise RuntimeError('q_rows must be a dict for payload fingerprint')
    encoded_rows = []
    seen = set()
    for q, n0 in q_rows.items():
        q_text = q_key_to_text(q)
        if q_text in seen:
            raise RuntimeError(f'q-key encoding collision in payload fingerprint: {q_text!r}')
        seen.add(q_text)
        encoded_rows.append((q_text, int(n0)))
    encoded_rows.sort(key=lambda item: item[0])
    payload = {
        'schema': 'BQG_DEPTH6_32_RECOVERY_PAYLOAD_FINGERPRINT_V1',
        'q_key_encoding': QKEY_ENCODING,
        'orbit_id': int(block['orbit_id']),
        'm': int(block['m']),
        'q_rows': encoded_rows,
        'frozen_assignment_sha256': block.get('frozen_assignment_sha256'),
        'kind': block.get('kind'),
        'irrep': block.get('irrep'),
        'irrep_key': block.get('irrep_key'),
    }
    raw = json.dumps(payload, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode('utf-8')
    return hashlib.sha256(raw).hexdigest()


def inventory_keymeta_roots(roots: Iterable[Path]) -> dict:
    manifests = []
    for root0 in roots:
        root = Path(root0)
        if not root.exists():
            raise RuntimeError(f'inventory root does not exist: {root}')
        manifests.extend(sorted(root.rglob('*manifest.json')))

    if not manifests:
        raise RuntimeError('no KEYMETA manifests found')

    by_orbit: dict[int, dict] = {}
    fingerprints: dict[int, str] = {}
    duplicate_orbits_collapsed = 0
    manifest_count = 0

    for mp in manifests:
        m = json.loads(mp.read_text())
        status = m.get('status')
        if status not in PASS_STATUSES:
            raise RuntimeError(f'non-PASS manifest: {mp}: {status!r}')
        if m.get('rank_certified') is True or m.get('numerical_closure_claimed') is True:
            raise RuntimeError(f'manifest crosses claim boundary: {mp}')
        records = m.get('records')
        if not isinstance(records, list):
            raise RuntimeError(f'manifest records must be a list: {mp}')
        declared_blocks = int(m.get('completed_blocks', -1))
        declared_columns = int(m.get('completed_columns', -1))
        if declared_blocks != len(records):
            raise RuntimeError(
                f'manifest completed_blocks mismatch: {mp}: {declared_blocks}!={len(records)}'
            )
        record_columns = sum(int(r['m']) for r in records)
        if declared_columns != record_columns:
            raise RuntimeError(
                f'manifest completed_columns mismatch: {mp}: {declared_columns}!={record_columns}'
            )

        seen_local = set()
        for rec in records:
            oid = int(rec['orbit_id'])
            if oid in seen_local:
                raise RuntimeError(f'duplicate orbit {oid} within manifest {mp}')
            seen_local.add(oid)
            declared_m = int(rec['m'])
            if declared_m <= 0:
                raise RuntimeError(f'orbit {oid}: non-positive manifest m')
            p = _find_payload(mp, str(rec['keymeta_file']))
            actual_sha = hashlib.sha256(p.read_bytes()).hexdigest()
            expected_sha = str(rec['keymeta_sha256'])
            if actual_sha != expected_sha:
                raise RuntimeError(
                    f'keymeta sha mismatch: orbit {oid}: got={actual_sha} expected={expected_sha}'
                )
            with gzip.open(p, 'rb') as f:
                block = pickle.load(f)
            payload_oid = int(block['orbit_id'])
            if payload_oid != oid:
                raise RuntimeError(
                    f'payload orbit_id mismatch: manifest={oid} payload={payload_oid}'
                )
            payload_m = int(block['m'])
            if payload_m != declared_m:
                raise RuntimeError(
                    f'payload m mismatch: orbit {oid}: manifest={declared_m} payload={payload_m}'
                )
            if payload_m <= 0:
                raise RuntimeError(f'orbit {oid}: non-positive payload m')
            q_rows = block.get('q_rows')
            if not isinstance(q_rows, dict):
                raise RuntimeError(f'orbit {oid}: q_rows must be a dict')
            for q, n0 in q_rows.items():
                if int(n0) <= 0:
                    raise RuntimeError(f'orbit {oid}: q={q!r} has non-positive rows')

            fp = _payload_fingerprint(block)
            if oid in by_orbit:
                if fingerprints[oid] != fp:
                    raise RuntimeError(f'conflicting duplicate orbit {oid}')
                duplicate_orbits_collapsed += 1
            else:
                by_orbit[oid] = block
                fingerprints[oid] = fp
        manifest_count += 1

    orbit_ids = sorted(by_orbit)
    columns = sum(int(by_orbit[oid]['m']) for oid in orbit_ids)
    return {
        'schema_version': 1,
        'kind': 'BQG_DEPTH6_32_RECOVERY_KEYMETA_INVENTORY',
        'manifest_count': manifest_count,
        'completed_blocks': len(orbit_ids),
        'completed_columns': columns,
        'completed_orbit_ids': orbit_ids,
        'duplicate_orbits_collapsed': duplicate_orbits_collapsed,
        'rank_certified': False,
        'numerical_closure_claimed': False,
        'claim_boundary': (
            'Inventory of durable KEYMETA payloads only. Duplicate orbit ids are collapsed only when '
            'their validated payload semantics match exactly. No global peeling, rank, kernel, or closure claim.'
        ),
    }
