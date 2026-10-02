#!/usr/bin/env python3
"""Canonical inventory of persisted [3,2] actual-q key metadata.

Only persisted keymeta artifacts are consumed.  Quarantined targeted-retry
artifacts are deliberately excluded because their assignments were reconstructed
from frozen structural machinery rather than read from a persisted assignment
ledger.
"""
from __future__ import annotations

import argparse
import gzip
import io
import json
import pickle
import re
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

from depth6_keymeta_coverage import validate_keymeta_coverage

SINGLE_RE = re.compile(r'^bqg-mixed-32-shard-(\d+)-keymeta$')
SALVAGE_RE = re.compile(r'^bqg-depth6-32-stagea-keymeta-salvage-\d+$')
GITHUB_API_HOST = 'api.github.com'


def is_candidate_keymeta_artifact_name(name: str) -> bool:
    return bool(SINGLE_RE.fullmatch(name) or SALVAGE_RE.fullmatch(name))


def github_headers(token: str) -> dict[str, str]:
    return {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'User-Agent': 'bqg-keymeta-inventory',
    }


def api_json(url: str, token: str) -> dict:
    req = urllib.request.Request(url, headers=github_headers(token))
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)


class StripAuthRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        new = super().redirect_request(req, fp, code, msg, headers, newurl)
        if new is None:
            return None
        old_host = urllib.parse.urlparse(req.full_url).hostname
        new_host = urllib.parse.urlparse(newurl).hostname
        if old_host == GITHUB_API_HOST and new_host != GITHUB_API_HOST:
            new.remove_header('Authorization')
        return new


def download(url: str, token: str, out: Path) -> None:
    req = urllib.request.Request(url, headers=github_headers(token))
    opener = urllib.request.build_opener(StripAuthRedirectHandler())
    with opener.open(req, timeout=180) as r, out.open('wb') as f:
        while True:
            chunk = r.read(1024 * 1024)
            if not chunk:
                break
            f.write(chunk)


def list_run_artifacts(repo: str, run_id: int, token: str) -> list[dict]:
    items: list[dict] = []
    page = 1
    while True:
        payload = api_json(
            f'https://api.github.com/repos/{repo}/actions/runs/{run_id}/artifacts?per_page=100&page={page}',
            token,
        )
        batch = payload.get('artifacts', [])
        items.extend(batch)
        if len(batch) < 100:
            return items
        page += 1


def _load_payload_bytes(raw: bytes, label: str) -> dict:
    with gzip.GzipFile(fileobj=io.BytesIO(raw), mode='rb') as g:
        x = pickle.load(g)
    if x.get('kind') != 'BQG_MIXED_MASTER_KEY_METADATA' or int(x.get('schema_version', -1)) != 1:
        raise RuntimeError(f'{label}: wrong keymeta kind/schema')
    return x


def load_payloads_from_zip(zpath: Path) -> list[dict]:
    with zipfile.ZipFile(zpath) as z:
        names = sorted(n for n in z.namelist() if n.endswith('.pkl.gz'))
        if not names:
            raise RuntimeError(f'{zpath}: expected at least one .pkl.gz')
        return [_load_payload_bytes(z.read(name), f'{zpath}:{name}') for name in names]


def choose_latest_payloads(records: list[tuple[dict, list[dict]]]) -> dict[int, dict]:
    """Deduplicate decoded artifact payloads by shard, keeping newest artifact."""
    chosen: dict[int, dict] = {}
    for artifact, payloads in records:
        created = str(artifact.get('created_at', ''))
        for payload in payloads:
            sid = int(payload['shard'])
            old = chosen.get(sid)
            if old is None or created > old['created_at']:
                chosen[sid] = {
                    'artifact': dict(artifact),
                    'payload': payload,
                    'created_at': created,
                }
    return chosen


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', required=True)
    ap.add_argument('--run-id', action='append', type=int, required=True)
    ap.add_argument('--token', required=True)
    ap.add_argument('--work', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    args.work.mkdir(parents=True, exist_ok=True)

    decoded: list[tuple[dict, list[dict]]] = []
    for run_id in args.run_id:
        for artifact in list_run_artifacts(args.repo, run_id, args.token):
            if artifact.get('expired') or not is_candidate_keymeta_artifact_name(str(artifact.get('name', ''))):
                continue
            zpath = args.work / f"artifact-{artifact['id']}.zip"
            download(artifact['archive_download_url'], args.token, zpath)
            payloads = load_payloads_from_zip(zpath)
            for x in payloads:
                x['_source_keymeta_run_id'] = run_id
            decoded.append((artifact, payloads))
            zpath.unlink(missing_ok=True)

    chosen = choose_latest_payloads(decoded)
    payloads = [chosen[s]['payload'] for s in sorted(chosen)]
    provenance = {}
    for sid in sorted(chosen):
        rec = chosen[sid]
        x = rec['payload']
        artifact = rec['artifact']
        provenance[str(sid)] = {
            'keymeta_artifact_id': artifact.get('id'),
            'keymeta_artifact_name': artifact.get('name'),
            'keymeta_artifact_digest': artifact.get('digest'),
            'keymeta_created_at': artifact.get('created_at'),
            'keymeta_run_id': x.get('_source_keymeta_run_id'),
            'source_raw_run_id': x.get('source_run_id'),
            'source_raw_artifact_id': x.get('source_artifact_id'),
            'source_raw_artifact_digest': x.get('source_artifact_digest'),
            'source_tar_sha256': x.get('source_tar_sha256'),
        }

    coverage = validate_keymeta_coverage(
        payloads,
        irrep='32', expected_shards=112,
        target_blocks=2755, target_columns=130903,
    )
    result = {
        'schema_version': 2,
        'kind': 'BQG_DEPTH6_32_ACTUAL_Q_KEYMETA_INVENTORY',
        'source_keymeta_runs': sorted(set(args.run_id)),
        **coverage,
        'provenance_by_shard': provenance,
        'structural_recompute_performed': False,
        'schedule_started': False,
        'next_action': 'GLOBAL_SCHEDULE_MAY_START' if coverage['schedule_allowed'] else 'RECOVER_MISSING_KEYMETA_SHARDS_ONLY',
        'claim_boundary': (
            'Inventory of persisted actual-q metadata only. Partial coverage is not a rank witness. '
            'Global schedule/SVD remains forbidden until schedule_allowed=true.'
        ),
    }
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
