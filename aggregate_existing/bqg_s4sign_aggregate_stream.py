#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import pickle
import tarfile
from pathlib import Path

import numpy as np

import bqg_depth6_41 as Z
import bqg_safe_boundary_master_gate as R


TARGET_BLOCKS = 11956
TARGET_COLUMNS = 130112
SHELL_STATES = 264962


def gauss_ok(sp):
    return all(R.allowed_k2_t(*R.local_spins(sp, v)) for v in R.VERT)


def geometric_outs(sp):
    import itertools
    sp = tuple(sp)
    J = max(sp) + 1
    out = set()
    for a, b in itertools.combinations(R.NEIG[0], 2):
        es = [
            R.EIDX[tuple(sorted((0, a)))],
            R.EIDX[tuple(sorted((a, b)))],
            R.EIDX[tuple(sorted((b, 0)))],
        ]
        for ds in itertools.product((-1, 1), repeat=3):
            z = list(sp)
            ok = True
            for e, dd in zip(es, ds):
                z[e] += dd
                if z[e] < 0 or z[e] > J:
                    ok = False
                    break
            if ok:
                z = tuple(z)
                if gauss_ok(z):
                    out.add(Z.canon4(z)[0])
    return out


def extract_all(root: Path, work: Path, expected_shards: int):
    work.mkdir(parents=True, exist_ok=True)
    tars = sorted(root.rglob("*shard-*.tar.gz"))
    if len(tars) != expected_shards:
        raise SystemExit(f"expected {expected_shards} shard tarballs, got {len(tars)}")

    dirs = []
    for n, t in enumerate(tars):
        d = work / f"shard_{n:03d}"
        d.mkdir(exist_ok=True)
        with tarfile.open(t, "r:gz") as tf:
            tf.extractall(d)
        dirs.append(d)
    return dirs


def index_artifacts(dirs, expected_shards: int):
    summaries = []
    records = {}
    map_paths = {}

    for d in dirs:
        ss = list(d.rglob("summary.json"))
        if len(ss) != 1:
            raise SystemExit(f"bad summary count in {d}: {len(ss)}")
        s = json.load(open(ss[0]))
        summaries.append(s)

        ledger = (int(s["shell_states"]), int(s["s4sign_blocks"]), int(s["s4sign_dim"]))
        if ledger != (SHELL_STATES, TARGET_BLOCKS, TARGET_COLUMNS):
            raise SystemExit(f"ledger mismatch shard {s['shard']}: {ledger}")

        if int(s["failed_blocks"]) != 0:
            raise SystemExit(f"failed blocks in shard {s['shard']}: {s['failed_blocks']}")
        if int(s["ok_blocks"]) != int(s["assigned_blocks"]):
            raise SystemExit(
                f"incomplete shard {s['shard']}: {s['ok_blocks']}/{s['assigned_blocks']}"
            )

        for r in s["records"]:
            i = int(r["i"])
            if i in records:
                raise SystemExit(f"duplicate block record {i}")
            records[i] = r

        for p in d.rglob("b*.pkl"):
            try:
                i = int(p.stem[1:])
            except ValueError:
                continue
            if i in map_paths:
                raise SystemExit(f"duplicate map {i}")
            map_paths[i] = p

    shards = sorted(int(s["shard"]) for s in summaries)
    if shards != list(range(expected_shards)):
        missing = sorted(set(range(expected_shards)) - set(shards))
        raise SystemExit(f"bad shard coverage, missing={missing}")

    if sorted(records) != list(range(TARGET_BLOCKS)):
        missing = sorted(set(range(TARGET_BLOCKS)) - set(records))
        raise SystemExit(f"block record coverage incomplete, first_missing={missing[:20]}")

    if sorted(map_paths) != list(range(TARGET_BLOCKS)):
        missing = sorted(set(range(TARGET_BLOCKS)) - set(map_paths))
        raise SystemExit(f"map coverage incomplete, first_missing={missing[:20]}")

    colsum = sum(int(r["d"]) for r in records.values())
    if colsum != TARGET_COLUMNS:
        raise SystemExit(f"column total mismatch: {colsum} != {TARGET_COLUMNS}")

    return summaries, records, map_paths


def build_geometric_graph(records):
    support = {}
    occ = {}
    for n, i in enumerate(sorted(records), 1):
        qin = tuple(records[i]["qin"])
        ss = geometric_outs(qin)
        support[i] = ss
        for q in ss:
            occ.setdefault(q, set()).add(i)
        if n % 1000 == 0:
            print("GEOM", n, "/", TARGET_BLOCKS, "q", len(occ), flush=True)
    return support, occ


def block_certificate(i, unique_q, records, map_paths):
    with open(map_paths[i], "rb") as f:
        block = pickle.load(f)

    mats = [block[q] for q in unique_q if q in block]
    if not mats:
        return None

    M = np.vstack(mats)
    d = int(records[i]["d"])
    if M.shape[0] < d:
        return None

    s = np.linalg.svd(M, compute_uv=False)
    if len(s) < d:
        return None

    smax = float(s[0]) if len(s) else 0.0
    tol = max(M.shape) * np.finfo(float).eps * max(smax, 1.0) * 100.0
    rank = int((s > tol).sum())
    sigma = float(s[d - 1])

    if rank != d or sigma <= max(tol, 1e-10):
        return None

    return {
        "d": d,
        "unique_q": len(unique_q),
        "rows": int(M.shape[0]),
        "sigma_min": sigma,
        "rank_tol": float(tol),
    }


def certify(records, map_paths, outfile: Path):
    support, occ = build_geometric_graph(records)
    remaining = set(records)
    cert = {}
    rounds = []

    round_idx = 0
    while True:
        candidates = []
        for i in sorted(remaining):
            uq = [q for q in support[i] if occ[q] == {i}]
            if uq:
                candidates.append((i, uq))

        print(
            "ROUND_START", round_idx,
            "remaining", len(remaining),
            "candidates", len(candidates),
            flush=True,
        )

        ready = []
        for n, (i, uq) in enumerate(candidates, 1):
            c = block_certificate(i, uq, records, map_paths)
            if c is not None:
                ready.append((i, c))
            if n % 250 == 0:
                print(
                    "ROUND_SCAN", round_idx,
                    n, "/", len(candidates),
                    "pass", len(ready),
                    flush=True,
                )

        if not ready:
            break

        info = {
            "round": round_idx,
            "blocks": len(ready),
            "columns": sum(c["d"] for _, c in ready),
        }
        rounds.append(info)
        print("ROUND_PASS", info, flush=True)

        for i, c in ready:
            cert[str(i)] = c

        for i, _ in ready:
            remaining.remove(i)

        for i, _ in ready:
            for q in support[i]:
                occ[q].discard(i)

        partial = {
            "status": "IN_PROGRESS",
            "certified_blocks": len(cert),
            "certified_columns": sum(v["d"] for v in cert.values()),
            "remaining_blocks": len(remaining),
            "remaining_columns": sum(int(records[i]["d"]) for i in remaining),
            "rounds": rounds,
        }
        outfile.with_suffix(".partial.json").write_text(json.dumps(partial, indent=2) + "\n")
        round_idx += 1

    result = {
        "status": "PASS" if not remaining else "RESIDUAL_CORE",
        "scope": "depth6 S4-sign input = [1^5] + [2,1,1,1]",
        "target_blocks": TARGET_BLOCKS,
        "target_columns": TARGET_COLUMNS,
        "certified_blocks": len(cert),
        "certified_columns": sum(v["d"] for v in cert.values()),
        "remaining_blocks": len(remaining),
        "remaining_columns": sum(int(records[i]["d"]) for i in remaining),
        "rounds": rounds,
        "global_sigma_min": min((v["sigma_min"] for v in cert.values()), default=None),
        "remaining_ids": sorted(remaining),
        "proof_logic": (
            "Conservative geometric support determines row occupancy. "
            "A block is removed only when its actual numeric H0 map restricted "
            "to rows geometrically unique at that removal step has full column rank."
        ),
    }
    outfile.write_text(json.dumps(result, indent=2) + "\n")
    print("FINAL", json.dumps(result, separators=(",", ":")), flush=True)
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--artifacts", type=Path, required=True)
    ap.add_argument("--expected-shards", type=int, default=128)
    ap.add_argument("--work", type=Path, default=Path("_aggregate_work"))
    ap.add_argument(
        "--out",
        type=Path,
        default=Path("bqg_depth6_s4sign_distributed_certificate.json"),
    )
    a = ap.parse_args()

    dirs = extract_all(a.artifacts, a.work, a.expected_shards)
    summaries, records, map_paths = index_artifacts(dirs, a.expected_shards)

    audit = {
        "expected_shards": a.expected_shards,
        "shards": len(summaries),
        "shell_states_each": sorted(set(int(s["shell_states"]) for s in summaries)),
        "s4sign_blocks_each": sorted(set(int(s["s4sign_blocks"]) for s in summaries)),
        "s4sign_dim_each": sorted(set(int(s["s4sign_dim"]) for s in summaries)),
        "block_records": len(records),
        "map_files": len(map_paths),
        "column_total": sum(int(r["d"]) for r in records.values()),
    }
    print("AUDIT", json.dumps(audit, separators=(",", ":")), flush=True)
    certify(records, map_paths, a.out)


if __name__ == "__main__":
    main()
