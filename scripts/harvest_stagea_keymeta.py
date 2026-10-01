#!/usr/bin/env python3
"""Sequentially salvage tiny key metadata from a Stage-A Actions run.

The script intentionally never downloads all raw artifacts at once. It lists
matching shard artifacts, downloads ONE ZIP, extracts its one raw tar, runs the
persisted-map key metadata extractor, then deletes the multi-GB temporary data
before moving to the next shard.

It accepts partial runs: every successfully harvested shard is preserved and a
manifest records missing/expired/failed shards. Full numerical scheduling still
requires exact 112/112 metadata coverage.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path


def api_json(url: str, token: str):
    req = urllib.request.Request(url, headers={
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'User-Agent': 'bqg-stagea-keymeta-harvester',
    })
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)


def list_artifacts(repo: str, run_id: str, token: str):
    out = []
    page = 1
    while True:
        x = api_json(
            f'https://api.github.com/repos/{repo}/actions/runs/{run_id}/artifacts?per_page=100&page={page}',
            token,
        )
        batch = x.get('artifacts', [])
        out.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return out


def download(url: str, token: str, dst: Path):
    req = urllib.request.Request(url, headers={
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'User-Agent': 'bqg-stagea-keymeta-harvester',
    })
    with urllib.request.urlopen(req, timeout=180) as r, dst.open('wb') as f:
        shutil.copyfileobj(r, f, length=8 * 1024 * 1024)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', required=True)
    ap.add_argument('--run-id', required=True)
    ap.add_argument('--token-env', default='GH_TOKEN')
    ap.add_argument('--prefix', default='bqg-mixed-32-shard-')
    ap.add_argument('--expected-shards', type=int, default=112)
    ap.add_argument('--extractor', type=Path, required=True)
    ap.add_argument('--out-dir', type=Path, required=True)
    ap.add_argument('--engine-git-blob-sha', required=True)
    a = ap.parse_args()
    token = os.environ.get(a.token_env)
    if not token:
        raise RuntimeError(f'missing token env {a.token_env}')
    a.out_dir.mkdir(parents=True, exist_ok=True)

    rx = re.compile(r'^' + re.escape(a.prefix) + r'(\d+)$')
    artifacts = list_artifacts(a.repo, a.run_id, token)
    selected = {}
    duplicate = {}
    for art in artifacts:
        m = rx.match(str(art.get('name', '')))
        if not m:
            continue
        shard = int(m.group(1))
        if shard in selected:
            duplicate.setdefault(shard, []).append(int(art['id']))
            # Keep the newest artifact deterministically.
            old = selected[shard]
            if str(art.get('created_at', '')) > str(old.get('created_at', '')):
                selected[shard] = art
        else:
            selected[shard] = art

    manifest = {
        'schema_version': 1,
        'kind': 'BQG_STAGEA_KEYMETA_SALVAGE_MANIFEST',
        'repo': a.repo,
        'source_run_id': str(a.run_id),
        'prefix': a.prefix,
        'expected_shards': a.expected_shards,
        'discovered_shards': sorted(selected),
        'duplicates': duplicate,
        'harvested': {},
        'errors': {},
    }

    for shard in sorted(selected):
        art = selected[shard]
        if art.get('expired'):
            manifest['errors'][str(shard)] = 'artifact_expired_before_harvest'
            continue
        tmp_root = Path(tempfile.mkdtemp(prefix=f'bqg-keymeta-{shard}-'))
        try:
            zpath = tmp_root / f'shard-{shard}.zip'
            download(str(art['archive_download_url']), token, zpath)
            zdir = tmp_root / 'zip'
            zdir.mkdir()
            with zipfile.ZipFile(zpath) as zf:
                bad = [n for n in zf.namelist() if Path(n).is_absolute() or '..' in Path(n).parts]
                if bad:
                    raise RuntimeError(f'unsafe zip members: {bad[:3]}')
                zf.extractall(zdir)
            raw = zdir / f'{a.prefix}{shard}.tar.gz'
            if not raw.is_file():
                matches = list(zdir.rglob(f'{a.prefix}{shard}.tar.gz'))
                if len(matches) != 1:
                    raise RuntimeError(f'expected one raw tar for shard {shard}, got {len(matches)}')
                raw = matches[0]
            out_pkl = a.out_dir / f'{a.prefix}{shard}-keymeta.pkl.gz'
            out_json = a.out_dir / f'{a.prefix}{shard}-keymeta-stats.json'
            work = tmp_root / 'work'
            cmd = [
                sys.executable, str(a.extractor),
                '--src', str(raw), '--work', str(work),
                '--out', str(out_pkl), '--json', str(out_json),
                '--source-run-id', str(a.run_id),
                '--source-artifact-id', str(art['id']),
                '--source-artifact-digest', str(art.get('digest') or ''),
                '--engine-git-blob-sha', a.engine_git_blob_sha,
            ]
            subprocess.run(cmd, check=True)
            stats = json.loads(out_json.read_text())
            manifest['harvested'][str(shard)] = {
                'artifact_id': int(art['id']),
                'artifact_digest': art.get('digest'),
                'artifact_size_bytes': int(art.get('size_in_bytes') or 0),
                'artifact_expires_at': art.get('expires_at'),
                'blocks': int(stats['stats']['blocks']),
                'columns': int(stats['stats']['columns']),
                'q_keys': int(stats['stats']['q_keys']),
                'keymeta_bytes': int(stats['stats']['output_bytes']),
                'source_tar_sha256': stats['source_tar_sha256'],
            }
            print('HARVESTED', shard, manifest['harvested'][str(shard)], flush=True)
        except Exception as exc:
            manifest['errors'][str(shard)] = repr(exc)
            print('HARVEST_ERROR', shard, repr(exc), flush=True)
        finally:
            shutil.rmtree(tmp_root, ignore_errors=True)

    expected = set(range(a.expected_shards))
    harvested = {int(x) for x in manifest['harvested']}
    manifest['harvested_shards'] = sorted(harvested)
    manifest['missing_shards'] = sorted(expected - harvested)
    manifest['harvested_count'] = len(harvested)
    manifest['harvested_blocks'] = sum(x['blocks'] for x in manifest['harvested'].values())
    manifest['harvested_columns'] = sum(x['columns'] for x in manifest['harvested'].values())
    manifest['status'] = 'COMPLETE_112_OF_112' if harvested == expected else 'PARTIAL_REUSABLE_KEYMETA'
    manifest['claim_boundary'] = (
        'Salvage of actual persisted numerical master-map key metadata only. '
        'Partial coverage is reusable but cannot prove [3,2] numerical closure.'
    )
    (a.out_dir / 'manifest.json').write_text(json.dumps(manifest, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: manifest[k] for k in (
        'status','harvested_count','harvested_blocks','harvested_columns','missing_shards')}, indent=2))
    # Partial salvage is a successful preservation operation. Exact closure is
    # enforced later by the schedule builder's 112-shard coverage check.
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
