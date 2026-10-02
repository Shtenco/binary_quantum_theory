#!/usr/bin/env python3
"""Fail-closed replay-readiness gate for frozen depth-6 [3,2] assignments.

Assignment identity (orbit, rep, multiplicity) is not enough to replay a missing
master map under the canonical recovery boundary.  A record is replay-ready only
when it points to either a persisted master map or a persisted selector witness
through immutable, content-addressed evidence.
"""
from __future__ import annotations

import re

SHA256_RE = re.compile(r'^[0-9a-f]{64}$')
ALLOWED_KINDS = {'PERSISTED_MASTER_MAP', 'PERSISTED_SELECTOR_WITNESS'}


def _valid_evidence(evidence: dict) -> bool:
    if not isinstance(evidence, dict):
        return False
    if evidence.get('kind') not in ALLOWED_KINDS:
        return False
    if not SHA256_RE.fullmatch(str(evidence.get('sha256', ''))):
        return False
    locator = evidence.get('immutable_locator')
    if not isinstance(locator, str) or not locator.strip():
        return False
    return True


def assess_records(records: list[dict]) -> dict:
    ready = []
    missing = []
    by_kind = {k: 0 for k in sorted(ALLOWED_KINDS)}
    seen = set()

    for record in records:
        orbit = int(record['orbit_id'])
        if orbit in seen:
            raise RuntimeError(f'duplicate orbit_id {orbit} in replay-readiness input')
        seen.add(orbit)
        evidence = record.get('replay_evidence')
        if evidence is None:
            missing.append(orbit)
            continue
        if not _valid_evidence(evidence):
            raise RuntimeError(f'invalid replay evidence for orbit {orbit}')
        ready.append(orbit)
        by_kind[str(evidence['kind'])] += 1

    return {
        'status': 'FULL_REPLAY_READINESS' if records and not missing else 'MISSING_SELECTOR_OR_MASTER_MAP_PROVENANCE',
        'input_blocks': len(records),
        'replay_ready_blocks': len(ready),
        'missing_replay_blocks': len(missing),
        'replay_ready_orbits': sorted(ready),
        'missing_selector_or_map_blocks': sorted(missing),
        'evidence_kind_counts': by_kind,
        'canonical_compute_allowed': bool(records and not missing),
        'rank_certified': False,
        'claim_boundary': (
            'Replay-readiness only. Assignment identity alone does not authorize Jucys/selector reconstruction. '
            'Replay evidence does not certify actual-q coverage, rank, or [3,2] numerical closure.'
        ),
    }
