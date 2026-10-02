#!/usr/bin/env python3
"""Deterministic ledger-driven batch planner for depth-6 [3,2].

Canonical planning consumes a *complete* persisted assignment ledger only.
Incomplete ledgers may be inspected with ``diagnostic=True`` but cannot authorize
compute.  Cost estimates use persisted fields only; no structural reconstruction
is available in this module.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

from depth6_assignment_ledger import verify_assignment_ledger


def persisted_cost(record: dict) -> float:
    observed = record.get('observed_sec')
    if observed is not None and float(observed) > 0.0:
        return float(observed)
    # Deterministic persisted-only fallback.  It is an ordering proxy, not a
    # scientific quantity and not a replacement for observed wall time.
    return float(int(record.get('coord_dim', 0)) * int(record['m']))


def _manifest_hash(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode('utf-8')
    return hashlib.sha256(raw).hexdigest()


def plan_batches(ledger: dict, *, batch_count: int, diagnostic: bool = False) -> dict:
    if batch_count <= 0:
        raise RuntimeError('batch_count must be positive')
    verified = verify_assignment_ledger(ledger)
    complete = bool(verified['coverage']['retry_allowed'])
    if not complete and not diagnostic:
        raise RuntimeError('incomplete persisted assignment ledger: canonical planning is forbidden')

    records = copy.deepcopy(verified['records'])
    if not records:
        raise RuntimeError('assignment ledger contains no persisted records')
    count = min(int(batch_count), len(records))
    batches = [
        {'batch_id': i, 'estimated_cost': 0.0, 'orbit_ids': [], 'records': []}
        for i in range(count)
    ]

    # Longest-processing-time-first scheduling.  Orbit ID is a stable tie-break.
    ordered = sorted(records, key=lambda r: (-persisted_cost(r), int(r['orbit_id'])))
    for record in ordered:
        batch = min(batches, key=lambda b: (b['estimated_cost'], b['batch_id']))
        cost = persisted_cost(record)
        batch['estimated_cost'] += cost
        batch['orbit_ids'].append(int(record['orbit_id']))
        batch['records'].append(record)

    for batch in batches:
        pairs = sorted(zip(batch['orbit_ids'], batch['records']), key=lambda x: x[0])
        batch['orbit_ids'] = [x[0] for x in pairs]
        batch['records'] = [x[1] for x in pairs]

    mode = 'CANONICAL_COMPLETE_LEDGER' if complete else 'DIAGNOSTIC_ONLY_INCOMPLETE_LEDGER'
    body = {
        'schema_version': 1,
        'kind': 'BQG_DEPTH6_32_LEDGER_BATCH_MANIFEST',
        'irrep': '[3,2]',
        'mode': mode,
        'canonical_compute_allowed': bool(complete),
        'assignment_ledger_sha256': verified['ledger_sha256'],
        'batch_count': count,
        'persisted_blocks': verified['coverage']['persisted_blocks'],
        'persisted_columns': verified['coverage']['persisted_columns'],
        'cost_policy': 'observed_sec_else_coord_dim_times_m_persisted_only',
        'batches': batches,
        'claim_boundary': (
            'Batching only. A complete assignment ledger authorizes replay of frozen assignments, '
            'not actual-q completeness, rank certification, or [3,2] closure.'
        ),
    }
    body['manifest_sha256'] = _manifest_hash(body)
    return body


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--ledger', type=Path, default=Path('BQG_DEPTH6_32_ASSIGNMENT_LEDGER_2026-10-02.json'))
    ap.add_argument('--batches', type=int, required=True)
    ap.add_argument('--diagnostic', action='store_true')
    ap.add_argument('--out', type=Path)
    args = ap.parse_args()
    ledger = json.loads(args.ledger.read_text())
    result = plan_batches(ledger, batch_count=args.batches, diagnostic=args.diagnostic)
    text = json.dumps(result, indent=2, sort_keys=True) + '\n'
    if args.out:
        args.out.write_text(text)
    else:
        print(text, end='')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
