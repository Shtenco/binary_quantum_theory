#!/usr/bin/env python3
"""Provenance-only salvage of the original depth-6 [3,2] Stage-A run.

This script reads GitHub Actions job metadata/logs and the run artifact index. It
never imports BQG mathematics and never recomputes shell/orbits/multiplicities or
Jucys selectors. Its purpose is to distinguish persisted evidence from work
that completed numerically but was lost during pack/upload.
"""
from __future__ import annotations

import argparse
import json
import re
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

LEDGER_RE = re.compile(
    r'LEDGER\s+32\s+(\d+)\s+(\d+)\s+SHARD\s+(\d+)\s+N\s+(\d+)\s+COLS\s+(\d+)\s+PROXY\s+([0-9.eE+-]+)'
)
DONE_RE = re.compile(r'DONE\s+(\d+)\s*/\s*(\d+)\s+ok\s+(\d+)\s+sec\s+([0-9.eE+-]+)')
JOB_RE = re.compile(r'^mixed32_shard \((\d+)\)$')
RAW_ARTIFACT_RE = re.compile(r'^bqg-mixed-32-shard-(\d+)$')
GITHUB_API_HOST = 'api.github.com'


class StripAuthRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Do not leak GitHub Authorization to signed object-storage redirects."""
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        new = super().redirect_request(req, fp, code, msg, headers, newurl)
        if new is None:
            return None
        old_host = urllib.parse.urlparse(req.full_url).hostname
        new_host = urllib.parse.urlparse(newurl).hostname
        if old_host == GITHUB_API_HOST and new_host != GITHUB_API_HOST:
            new.remove_header('Authorization')
        return new


def unavailable_log_record(shard: int, reason: str) -> dict:
    return {
        'shard': int(shard),
        'log_available': False,
        'log_unavailable_reason': str(reason),
        'ledger_seen': None,
        'assigned_blocks': None,
        'assigned_columns': None,
        'proxy': None,
        'done_blocks': None,
        'done_total': None,
        'ok_blocks': None,
        'elapsed_sec': None,
        'numerical_complete': None,
    }


def parse_worker_log(text: str, *, expected_shard: int) -> dict:
    ledgers = LEDGER_RE.findall(text)
    if len(ledgers) > 1:
        raise RuntimeError(f'shard {expected_shard}: multiple LEDGER lines')
    if not ledgers:
        return {
            'shard': expected_shard,
            'log_available': True,
            'log_unavailable_reason': None,
            'ledger_seen': False,
            'assigned_blocks': None,
            'assigned_columns': None,
            'proxy': None,
            'done_blocks': 0,
            'done_total': None,
            'ok_blocks': 0,
            'elapsed_sec': None,
            'numerical_complete': False,
        }
    active, target, shard, n, cols, proxy = ledgers[0]
    shard = int(shard)
    if shard != int(expected_shard):
        raise RuntimeError(f'shard mismatch: log={shard} expected={expected_shard}')
    if int(active) != 2755 or int(target) != 130903:
        raise RuntimeError(f'shard {shard}: frozen target mismatch {active}/{target}')

    done_matches = DONE_RE.findall(text)
    done_blocks = 0
    done_total = int(n)
    ok_blocks = 0
    elapsed = None
    for a, b, ok, sec in done_matches:
        a, b, ok = int(a), int(b), int(ok)
        if b != int(n):
            raise RuntimeError(f'shard {shard}: DONE total {b} disagrees with ledger N={n}')
        if a < done_blocks:
            raise RuntimeError(f'shard {shard}: DONE progress regressed')
        done_blocks, done_total, ok_blocks, elapsed = a, b, ok, float(sec)
    numerical_complete = done_blocks == int(n) and ok_blocks == int(n)
    return {
        'shard': shard,
        'log_available': True,
        'log_unavailable_reason': None,
        'ledger_seen': True,
        'assigned_blocks': int(n),
        'assigned_columns': int(cols),
        'proxy': float(proxy),
        'done_blocks': done_blocks,
        'done_total': done_total,
        'ok_blocks': ok_blocks,
        'elapsed_sec': elapsed,
        'numerical_complete': numerical_complete,
    }


def classify(parsed: dict, *, artifact_present: bool) -> str:
    if artifact_present:
        return 'RAW_PERSISTED'
    if parsed.get('log_available') is False:
        return 'LOG_UNAVAILABLE'
    if parsed.get('numerical_complete'):
        return 'NUMERICAL_COMPLETE_BUT_ARTIFACT_LOST'
    if int(parsed.get('done_blocks') or 0) > 0:
        return 'PARTIAL_NUMERICAL'
    return 'NOT_COMPLETED'


def _headers(token: str) -> dict[str, str]:
    return {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'User-Agent': 'bqg-depth6-stagea-log-salvage',
    }


def _json(url: str, token: str) -> dict:
    req = urllib.request.Request(url, headers=_headers(token))
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)


def _text_or_unavailable(url: str, token: str) -> tuple[str | None, str | None]:
    req = urllib.request.Request(url, headers=_headers(token))
    opener = urllib.request.build_opener(StripAuthRedirectHandler())
    try:
        with opener.open(req, timeout=180) as r:
            return r.read().decode('utf-8', errors='replace'), None
    except urllib.error.HTTPError as exc:
        if exc.code in (404, 410):
            return None, f'HTTP_{exc.code}_LOG_BLOB_UNAVAILABLE'
        raise


def _paginate(url: str, token: str, field: str) -> list[dict]:
    out: list[dict] = []
    page = 1
    while True:
        sep = '&' if '?' in url else '?'
        x = _json(f'{url}{sep}per_page=100&page={page}', token)
        batch = x.get(field, [])
        out.extend(batch)
        if len(batch) < 100:
            return out
        page += 1


def build_inventory(repo: str, run_id: int, token: str) -> dict:
    jobs = _paginate(f'https://api.github.com/repos/{repo}/actions/runs/{run_id}/jobs', token, 'jobs')
    artifacts = _paginate(f'https://api.github.com/repos/{repo}/actions/runs/{run_id}/artifacts', token, 'artifacts')
    raw_by_shard: dict[int, dict] = {}
    for a in artifacts:
        m = RAW_ARTIFACT_RE.fullmatch(str(a.get('name', '')))
        if m:
            sid = int(m.group(1))
            raw_by_shard[sid] = {
                'artifact_id': a.get('id'),
                'artifact_name': a.get('name'),
                'artifact_digest': a.get('digest'),
                'size_in_bytes': a.get('size_in_bytes'),
                'created_at': a.get('created_at'),
                'expired': bool(a.get('expired')),
            }

    records = []
    for job in jobs:
        m = JOB_RE.fullmatch(str(job.get('name', '')))
        if not m:
            continue
        sid = int(m.group(1))
        text, unavailable_reason = _text_or_unavailable(
            f'https://api.github.com/repos/{repo}/actions/jobs/{job["id"]}/logs', token
        )
        if text is None:
            parsed = unavailable_log_record(sid, unavailable_reason or 'UNKNOWN_LOG_UNAVAILABLE')
        else:
            parsed = parse_worker_log(text, expected_shard=sid)
        artifact = raw_by_shard.get(sid)
        status = classify(parsed, artifact_present=artifact is not None)
        records.append({
            **parsed,
            'status': status,
            'job_id': job.get('id'),
            'job_conclusion': job.get('conclusion'),
            'job_started_at': job.get('started_at'),
            'job_completed_at': job.get('completed_at'),
            'artifact': artifact,
        })

    records.sort(key=lambda r: r['shard'])
    shard_ids = [r['shard'] for r in records]
    if shard_ids != list(range(112)):
        raise RuntimeError(f'expected exact Stage-A shards 0..111, got {shard_ids}')

    status_counts: dict[str, int] = {}
    for r in records:
        status_counts[r['status']] = status_counts.get(r['status'], 0) + 1
    assigned_blocks_known = sum(int(r['assigned_blocks'] or 0) for r in records)
    assigned_columns_known = sum(int(r['assigned_columns'] or 0) for r in records)
    completed_lost = [r['shard'] for r in records if r['status'] == 'NUMERICAL_COMPLETE_BUT_ARTIFACT_LOST']
    partial = [r['shard'] for r in records if r['status'] == 'PARTIAL_NUMERICAL']
    persisted = [r['shard'] for r in records if r['status'] == 'RAW_PERSISTED']
    unavailable = [r['shard'] for r in records if r['status'] == 'LOG_UNAVAILABLE']

    return {
        'schema_version': 2,
        'kind': 'BQG_DEPTH6_32_STAGEA_LOG_SALVAGE',
        'source_run_id': int(run_id),
        'irrep': '[3,2]',
        'target_shards': 112,
        'target_blocks': 2755,
        'target_columns': 130903,
        'records': records,
        'status_counts': status_counts,
        'persisted_raw_shards': persisted,
        'numerical_complete_but_artifact_lost_shards': completed_lost,
        'partial_numerical_shards': partial,
        'log_unavailable_shards': unavailable,
        'logs_available_count': sum(bool(r.get('log_available')) for r in records),
        'ledger_lines_recovered': sum(r.get('ledger_seen') is True for r in records),
        'assigned_blocks_from_recovered_ledger_lines': assigned_blocks_known,
        'assigned_columns_from_recovered_ledger_lines': assigned_columns_known,
        'structural_recompute_performed': False,
        'claim_boundary': (
            'Provenance-only reconstruction from immutable GitHub Actions job/artifact metadata and surviving logs. '
            'Unavailable logs remain UNKNOWN and are never interpreted as numerical failure. '
            'NUMERICAL_COMPLETE_BUT_ARTIFACT_LOST means only that the surviving log reported completion; '
            'without persisted matrices it is not reusable rank evidence and does not close [3,2].'
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', required=True)
    ap.add_argument('--run-id', type=int, required=True)
    ap.add_argument('--token', required=True)
    ap.add_argument('--out', type=Path, required=True)
    a = ap.parse_args()
    inv = build_inventory(a.repo, a.run_id, a.token)
    a.out.write_text(json.dumps(inv, indent=2, sort_keys=True) + '\n')
    keys = (
        'status_counts','persisted_raw_shards','numerical_complete_but_artifact_lost_shards',
        'partial_numerical_shards','log_unavailable_shards','logs_available_count',
        'ledger_lines_recovered','assigned_blocks_from_recovered_ledger_lines',
        'assigned_columns_from_recovered_ledger_lines'
    )
    print(json.dumps({k: inv[k] for k in keys}, indent=2, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
