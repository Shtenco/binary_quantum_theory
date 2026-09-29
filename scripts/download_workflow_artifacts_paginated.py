#!/usr/bin/env python3
"""Download all matching GitHub Actions artifacts from a workflow run, with pagination.

Designed for large sharded BQG proof runs where artifact counts exceed 100.
Fails closed on duplicate names, incomplete expected counts, HTTP errors, or
malformed ZIP archives.
"""
from __future__ import annotations

import argparse
import io
import json
import os
import urllib.request
import zipfile
from pathlib import Path

API = "https://api.github.com"

def request(url: str, token: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "BQG-artifact-downloader",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, help="owner/name")
    ap.add_argument("--run-id", type=int, required=True)
    ap.add_argument("--prefix", required=True)
    ap.add_argument("--expected", type=int, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GH_TOKEN/GITHUB_TOKEN is required")

    artifacts = []
    page = 1
    while True:
        url = (
            f"{API}/repos/{args.repo}/actions/runs/{args.run_id}/artifacts"
            f"?per_page=100&page={page}"
        )
        payload = json.loads(request(url, token))
        batch = payload.get("artifacts", [])
        artifacts.extend(
            a for a in batch
            if not a.get("expired", False)
            and str(a.get("name", "")).startswith(args.prefix)
        )
        if len(batch) < 100:
            break
        page += 1

    by_name = {}
    for a in artifacts:
        name = str(a["name"])
        if name in by_name:
            raise SystemExit(f"duplicate artifact name: {name}")
        by_name[name] = a

    if len(by_name) != args.expected:
        raise SystemExit(
            f"artifact coverage mismatch for prefix={args.prefix!r}: "
            f"expected {args.expected}, got {len(by_name)}"
        )

    args.out.mkdir(parents=True, exist_ok=True)
    for n, name in enumerate(sorted(by_name), 1):
        a = by_name[name]
        raw = request(
            f"{API}/repos/{args.repo}/actions/artifacts/{int(a['id'])}/zip",
            token,
        )
        dest = args.out / name
        dest.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(io.BytesIO(raw)) as zf:
            zf.extractall(dest)
        if n % 20 == 0 or n == args.expected:
            print(f"downloaded {n}/{args.expected}", flush=True)

    print(json.dumps({
        "repo": args.repo,
        "run_id": args.run_id,
        "prefix": args.prefix,
        "expected": args.expected,
        "downloaded": len(by_name),
        "output": str(args.out),
    }, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
