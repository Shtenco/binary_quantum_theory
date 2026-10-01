#!/usr/bin/env python3
"""Recovery-only numerical certifier for depth-6 mixed master maps.

Scientific boundary:
- consumes already persisted numerical master-map pickles and shard summaries;
- NEVER rebuilds the depth-6 shell, S5 orbits, Jucys selectors, branch sums,
  geometric support, structural matching, or structural peeling;
- derives occupancy only from the actual keys present in persisted master maps;
- uses a positive residual Gram test when unique-row numerical peeling leaves a core;
- never interprets matching/peeling failure as an operator kernel.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import pickle
import platform
import sys
import tarfile
from pathlib import Path
from typing import Callable

import numpy as np

TARGET = {
    "32": (130903, 2755),
    "311": (153455, 2719),
    "221": (130503, 2749),
    "2111": (103318, 2712),
}


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _rank_info(a: np.ndarray, sigma_floor: float) -> tuple[int, float, float]:
    if a.ndim != 2:
        raise ValueError(f"matrix must be 2D, got {a.shape}")
    if a.shape[1] == 0:
        return 0, 0.0, 0.0
    if a.shape[0] < a.shape[1]:
        return min(a.shape), 0.0, math.inf
    s = np.linalg.svd(a, compute_uv=False)
    smax = float(s[0]) if len(s) else 0.0
    tol = max(a.shape) * np.finfo(float).eps * max(smax, 1.0) * 100.0
    rank = int(np.count_nonzero(s > tol))
    sigma_min = float(s[-1]) if len(s) else 0.0
    return rank, sigma_min, max(tol, sigma_floor)


def _residual_gram_from_loaded(
    remaining: list[int],
    rec: dict[int, dict],
    get_map: Callable[[int], dict],
    sigma_floor: float,
    max_residual_columns: int,
) -> dict:
    ncols = sum(int(rec[i]["m"]) for i in remaining)
    if ncols == 0:
        return {
            "status": "EMPTY",
            "columns": 0,
            "lambda_min": None,
            "sigma_min": None,
            "kernel_dimension_estimate": 0,
        }
    if ncols > max_residual_columns:
        return {
            "status": "TOO_LARGE_FOR_CONFIGURED_RESIDUAL_GRAM",
            "columns": ncols,
            "max_residual_columns": max_residual_columns,
            "lambda_min": None,
            "sigma_min": None,
            "kernel_dimension_estimate": None,
        }

    try:
        import scipy
        import scipy.sparse as sp
        import scipy.sparse.linalg as sla
    except Exception as exc:  # pragma: no cover - exercised by CI environment
        return {
            "status": "SCIPY_UNAVAILABLE",
            "columns": ncols,
            "error": repr(exc),
            "lambda_min": None,
            "sigma_min": None,
            "kernel_dimension_estimate": None,
        }

    col_off: dict[int, int] = {}
    c = 0
    for i in remaining:
        col_off[i] = c
        c += int(rec[i]["m"])

    maps: dict[int, dict] = {i: get_map(i) for i in remaining}
    q_to_blocks: dict[object, list[int]] = {}
    for i, mp in maps.items():
        for q in mp:
            q_to_blocks.setdefault(q, []).append(i)

    row_off: dict[object, int] = {}
    row_count = 0
    for q in sorted(q_to_blocks, key=repr):
        dims = {int(np.asarray(maps[i][q]).shape[0]) for i in q_to_blocks[q]}
        if len(dims) != 1:
            return {
                "status": "ROW_DIMENSION_MISMATCH",
                "columns": ncols,
                "row_key": repr(q),
                "row_dimensions": sorted(dims),
                "lambda_min": None,
                "sigma_min": None,
                "kernel_dimension_estimate": None,
            }
        row_off[q] = row_count
        row_count += next(iter(dims))

    rows: list[np.ndarray] = []
    cols: list[np.ndarray] = []
    vals: list[np.ndarray] = []
    nnz = 0
    for i in remaining:
        m = int(rec[i]["m"])
        mp = maps[i]
        for q, aa in mp.items():
            a = np.asarray(aa)
            if a.ndim != 2 or a.shape[1] != m:
                return {
                    "status": "MATRIX_SHAPE_MISMATCH",
                    "columns": ncols,
                    "orbit_index": i,
                    "row_key": repr(q),
                    "shape": list(a.shape),
                    "expected_columns": m,
                    "lambda_min": None,
                    "sigma_min": None,
                    "kernel_dimension_estimate": None,
                }
            rr, cc = np.nonzero(a)
            if len(rr):
                rows.append(rr.astype(np.int64, copy=False) + row_off[q])
                cols.append(cc.astype(np.int64, copy=False) + col_off[i])
                vals.append(a[rr, cc])
                nnz += len(rr)

    dtype = np.result_type(*([v.dtype for v in vals] or [np.float64]))
    if vals:
        r = np.concatenate(rows)
        cidx = np.concatenate(cols)
        v = np.concatenate(vals).astype(dtype, copy=False)
    else:
        r = np.empty(0, dtype=np.int64)
        cidx = np.empty(0, dtype=np.int64)
        v = np.empty(0, dtype=dtype)

    C = sp.coo_matrix((v, (r, cidx)), shape=(row_count, ncols)).tocsr()
    G = (C.conjugate().T @ C).tocsr()

    # For small residuals use dense Hermitian eigensolve, which also gives the
    # complete numerical nullity. For larger residuals use several bottom
    # eigenpairs and fail closed if the lowest mode is not clearly positive.
    if ncols <= 2048:
        gd = G.toarray()
        evals, evecs = np.linalg.eigh(gd)
        order = np.argsort(evals.real)
        evals = np.asarray(evals[order].real, dtype=float)
        evecs = evecs[:, order]
        take = min(6, ncols)
        low = evals[:take]
        vecs = evecs[:, :take]
        kernel_est = int(np.count_nonzero(evals <= sigma_floor * sigma_floor))
    else:
        k = min(6, ncols - 1)
        evals, vecs = sla.eigsh(G, k=k, which="SA", tol=1e-10, maxiter=max(10000, 20 * ncols))
        order = np.argsort(evals.real)
        low = np.asarray(evals[order].real, dtype=float)
        vecs = vecs[:, order]
        kernel_est = None

    residuals = []
    gnorm = float(sla.norm(G)) if G.nnz else 0.0
    denom_norm = max(gnorm, 1.0)
    for j, lam in enumerate(low):
        x = vecs[:, j]
        rr = G @ x - lam * x
        residuals.append(float(np.linalg.norm(rr) / denom_norm))

    lam_min = float(low[0]) if len(low) else 0.0
    sigma_min = math.sqrt(max(lam_min, 0.0))
    positive = (
        lam_min > sigma_floor * sigma_floor
        and residuals
        and residuals[0] < 1e-8
    )
    return {
        "status": "POSITIVE_CERTIFIED" if positive else "NEAR_NULL_OR_INCONCLUSIVE",
        "columns": ncols,
        "rows": row_count,
        "nnz": int(nnz),
        "dtype": str(C.dtype),
        "scipy_version": scipy.__version__,
        "lambda_min": lam_min,
        "sigma_min": sigma_min,
        "smallest_gram_eigenvalues": [float(x) for x in low],
        "eigen_relative_residuals": residuals,
        "kernel_dimension_estimate": kernel_est,
        "sigma_floor": sigma_floor,
    }


def _certify(
    rec: dict[int, dict],
    get_map: Callable[[int], dict],
    support: dict[int, set],
    target_columns: int,
    target_blocks: int,
    sigma_floor: float,
    max_residual_columns: int,
) -> dict:
    recovered_blocks = len(rec)
    recovered_columns = sum(int(r["m"]) for r in rec.values())
    coverage_ok = recovered_blocks == target_blocks and recovered_columns == target_columns
    if not coverage_ok:
        return {
            "status": "INPUT_COVERAGE_FAILURE",
            "target_blocks": target_blocks,
            "target_columns": target_columns,
            "recovered_blocks": recovered_blocks,
            "recovered_columns": recovered_columns,
            "support_source": "persisted_master_map_keys_only",
            "structural_recompute_performed": False,
            "kernel_dimension": None,
            "h2_null_lift_forbidden_without_independent_true_kernel_check": True,
        }

    remaining = set(rec)
    occ: dict[object, set[int]] = {}
    for i, qs in support.items():
        for q in qs:
            occ.setdefault(q, set()).add(i)

    rounds = []
    cert: dict[str, dict] = {}
    while True:
        ready = []
        for i in sorted(remaining):
            mp = None
            uq = [q for q in support[i] if occ.get(q) == {i}]
            if not uq:
                continue
            mp = get_map(i)
            mats = [np.asarray(mp[q]) for q in uq if q in mp]
            if not mats:
                continue
            A = np.vstack(mats)
            m = int(rec[i]["m"])
            if A.shape[1] != m or A.shape[0] < m:
                continue
            rank, sigma_min, threshold = _rank_info(A, sigma_floor)
            if rank == m and sigma_min > threshold:
                ready.append((i, m, len(uq), int(A.shape[0]), sigma_min, threshold))
        if not ready:
            break
        rounds.append({
            "round": len(rounds),
            "blocks": len(ready),
            "columns": sum(x[1] for x in ready),
        })
        for i, m, nq, nr, sig, tol in ready:
            cert[str(i)] = {
                "m": m,
                "unique_master_row_keys": nq,
                "rows": nr,
                "sigma_min": sig,
                "rank_threshold": tol,
            }
        for i, *_ in ready:
            remaining.remove(i)
        for i, *_ in ready:
            for q in support[i]:
                if q in occ:
                    occ[q].discard(i)

    peeled_columns = sum(v["m"] for v in cert.values())
    residual_ids = sorted(remaining)
    residual_columns = sum(int(rec[i]["m"]) for i in residual_ids)
    residual = _residual_gram_from_loaded(
        residual_ids, rec, get_map, sigma_floor, max_residual_columns
    )

    if not residual_ids:
        status = "PASS_CLOSED_FINITE_NUMERICAL"
        kernel_dim = 0
        residual_positive = True
    elif residual.get("status") == "POSITIVE_CERTIFIED":
        status = "PASS_CLOSED_FINITE_NUMERICAL"
        kernel_dim = 0
        residual_positive = True
    elif residual.get("status") == "NEAR_NULL_OR_INCONCLUSIVE":
        status = "RESIDUAL_NEAR_NULL_REQUIRES_INDEPENDENT_CHECK"
        kernel_dim = None
        residual_positive = False
    else:
        status = "NUMERICAL_INCONCLUSIVE"
        kernel_dim = None
        residual_positive = False

    peel_sigmas = [float(v["sigma_min"]) for v in cert.values()]
    global_sigma = min(peel_sigmas) if peel_sigmas else None
    if residual_positive and residual_ids:
        rs = float(residual["sigma_min"])
        global_sigma = rs if global_sigma is None else min(global_sigma, rs)

    return {
        "status": status,
        "target_blocks": target_blocks,
        "target_columns": target_columns,
        "recovered_blocks": recovered_blocks,
        "recovered_columns": recovered_columns,
        "coverage_complete": True,
        "support_source": "persisted_master_map_keys_only",
        "structural_recompute_performed": False,
        "peeled_blocks": len(cert),
        "peeled_columns": peeled_columns,
        "peeling_rounds": rounds,
        "peeling_global_sigma_min": min(peel_sigmas) if peel_sigmas else None,
        "residual_blocks": len(residual_ids),
        "residual_columns": residual_columns,
        "residual_ids": residual_ids,
        "residual_gram": residual,
        "global_sigma_min": global_sigma,
        "kernel_dimension": kernel_dim,
        "h2_null_lift_forbidden_without_independent_true_kernel_check": True,
        "proof_logic": (
            "Numerical master maps are immutable inputs. Full-rank blocks are removed only "
            "using persisted output-row keys unique among the current numerical maps. Any "
            "remaining coupled core is tested by the positive Gram C^dagger C. Failure of "
            "peeling is not interpreted as a kernel."
        ),
    }


def certify_loaded(
    rec: dict[int, dict],
    maps: dict[int, dict],
    target_columns: int,
    target_blocks: int,
    sigma_floor: float = 1e-10,
    max_residual_columns: int = 20000,
) -> dict:
    if set(rec) != set(maps):
        return {
            "status": "INPUT_COVERAGE_FAILURE",
            "target_blocks": target_blocks,
            "target_columns": target_columns,
            "recovered_blocks": len(rec),
            "recovered_maps": len(maps),
            "support_source": "persisted_master_map_keys_only",
            "structural_recompute_performed": False,
            "kernel_dimension": None,
            "h2_null_lift_forbidden_without_independent_true_kernel_check": True,
        }
    support = {i: set(mp.keys()) for i, mp in maps.items()}
    return _certify(
        rec,
        lambda i: maps[i],
        support,
        target_columns,
        target_blocks,
        sigma_floor,
        max_residual_columns,
    )


def extract_and_index(
    artifacts: Path,
    work: Path,
    irrep: str,
    expected_shards: int,
    prefix: str,
) -> tuple[dict[int, dict], dict[int, Path], dict[int, set], dict]:
    tarballs = sorted(artifacts.rglob(f"{prefix}*.tar.gz"))
    manifest = {
        "expected_shards": expected_shards,
        "found_shards": len(tarballs),
        "tarballs": [{"path": str(p), "sha256": _sha256(p)} for p in tarballs],
    }
    if len(tarballs) != expected_shards:
        return {}, {}, {}, manifest

    rec: dict[int, dict] = {}
    paths: dict[int, Path] = {}
    support: dict[int, set] = {}
    work.mkdir(parents=True, exist_ok=True)

    for n, t in enumerate(tarballs):
        d = work / f"shard_{n:04d}"
        d.mkdir(parents=True, exist_ok=True)
        with tarfile.open(t, "r:gz") as tf:
            # GitHub-generated tarballs are trusted workflow outputs, but still
            # prevent path traversal before extraction.
            root = d.resolve()
            for member in tf.getmembers():
                dest = (d / member.name).resolve()
                if root not in dest.parents and dest != root:
                    raise RuntimeError(f"unsafe tar member: {member.name}")
            tf.extractall(d)

        summaries = list(d.rglob("summary.json"))
        if len(summaries) != 1:
            raise RuntimeError(f"expected one summary in {t}, got {len(summaries)}")
        s = json.loads(summaries[0].read_text())
        if s.get("irrep") != irrep:
            raise RuntimeError(f"wrong irrep in {t}: {s.get('irrep')}")
        if int(s.get("active_blocks", -1)) != TARGET[irrep][1]:
            raise RuntimeError(f"active block ledger mismatch in {t}")
        if int(s.get("target_columns", -1)) != TARGET[irrep][0]:
            raise RuntimeError(f"target column ledger mismatch in {t}")
        if int(s.get("failed_blocks", -1)) != 0:
            raise RuntimeError(f"failed numerical blocks in {t}")
        if int(s.get("ok_blocks", -1)) != int(s.get("assigned_blocks", -2)):
            raise RuntimeError(f"incomplete shard in {t}")

        for r in s.get("records", []):
            if not r.get("ok"):
                raise RuntimeError(f"failed record in {t}: {r}")
            i = int(r["orbit_index"])
            if i in rec:
                raise RuntimeError(f"duplicate orbit record {i}")
            p = next(iter(d.rglob(f"b{i:05d}.pkl")), None)
            if p is None:
                raise RuntimeError(f"missing persisted master map for orbit {i}")
            mp = pickle.load(p.open("rb"))
            m = int(r["m"])
            for q, a in mp.items():
                aa = np.asarray(a)
                if aa.ndim != 2 or aa.shape[1] != m:
                    raise RuntimeError(
                        f"bad persisted map shape orbit={i} key={q!r} shape={aa.shape} m={m}"
                    )
            rec[i] = r
            paths[i] = p
            support[i] = set(mp.keys())
            del mp

    return rec, paths, support, manifest


def certify_paths(
    rec: dict[int, dict],
    paths: dict[int, Path],
    support: dict[int, set],
    target_columns: int,
    target_blocks: int,
    sigma_floor: float,
    max_residual_columns: int,
) -> dict:
    def get_map(i: int) -> dict:
        with paths[i].open("rb") as f:
            return pickle.load(f)

    if set(rec) != set(paths) or set(rec) != set(support):
        return {
            "status": "INPUT_COVERAGE_FAILURE",
            "target_blocks": target_blocks,
            "target_columns": target_columns,
            "recovered_blocks": len(rec),
            "persisted_maps": len(paths),
            "support_entries": len(support),
            "support_source": "persisted_master_map_keys_only",
            "structural_recompute_performed": False,
            "kernel_dimension": None,
            "h2_null_lift_forbidden_without_independent_true_kernel_check": True,
        }
    return _certify(
        rec,
        get_map,
        support,
        target_columns,
        target_blocks,
        sigma_floor,
        max_residual_columns,
    )


def environment_manifest() -> dict:
    out = {
        "python": sys.version,
        "numpy": np.__version__,
        "platform": platform.platform(),
        "machine": platform.machine(),
        "OMP_NUM_THREADS": os.environ.get("OMP_NUM_THREADS"),
        "OPENBLAS_NUM_THREADS": os.environ.get("OPENBLAS_NUM_THREADS"),
        "MKL_NUM_THREADS": os.environ.get("MKL_NUM_THREADS"),
    }
    try:
        import scipy
        out["scipy"] = scipy.__version__
    except Exception:
        out["scipy"] = None
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--irrep", choices=TARGET, required=True)
    ap.add_argument("--artifacts", type=Path, required=True)
    ap.add_argument("--expected-shards", type=int, required=True)
    ap.add_argument("--prefix", required=True)
    ap.add_argument("--work", type=Path, default=Path("_mixed_recovery"))
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--source-run-id", type=int)
    ap.add_argument("--sigma-floor", type=float, default=1e-10)
    ap.add_argument("--max-residual-columns", type=int, default=20000)
    a = ap.parse_args()

    target_columns, target_blocks = TARGET[a.irrep]
    rec, paths, support, artifact_manifest = extract_and_index(
        a.artifacts, a.work, a.irrep, a.expected_shards, a.prefix
    )

    if len(artifact_manifest["tarballs"]) != a.expected_shards:
        result = {
            "schema_version": 1,
            "status": "INPUT_COVERAGE_FAILURE",
            "irrep": a.irrep,
            "target_blocks": target_blocks,
            "target_columns": target_columns,
            "source_run_id": a.source_run_id,
            "artifact_manifest": artifact_manifest,
            "support_source": "persisted_master_map_keys_only",
            "structural_recompute_performed": False,
            "structural_status": "CLOSED_IMMUTABLE_INPUT",
            "claim_boundary": "Independent finite numerical master witness only; structural depth-6 proof is not recomputed.",
            "environment": environment_manifest(),
        }
    else:
        result = certify_paths(
            rec,
            paths,
            support,
            target_columns,
            target_blocks,
            a.sigma_floor,
            a.max_residual_columns,
        )
        result.update({
            "schema_version": 1,
            "irrep": a.irrep,
            "source_run_id": a.source_run_id,
            "artifact_manifest": artifact_manifest,
            "structural_status": "CLOSED_IMMUTABLE_INPUT",
            "frozen_structural_ledger": {
                "[3,2]": {"blocks": "2755/2755", "columns": "130903/130903", "remainder": 0},
            } if a.irrep == "32" else None,
            "environment": environment_manifest(),
            "claim_boundary": (
                "Independent finite numerical master witness only. No shell, orbit, Jucys, branch-sum, "
                "geometric support, structural matching, or structural peeling recomputation is performed."
            ),
        })

    a.out.write_text(json.dumps(result, indent=2, sort_keys=True, default=str) + "\n")
    print(json.dumps({
        k: result.get(k) for k in (
            "status", "target_blocks", "target_columns", "recovered_blocks",
            "recovered_columns", "peeled_blocks", "peeled_columns",
            "residual_blocks", "residual_columns", "global_sigma_min", "kernel_dimension"
        )
    }, indent=2))
    return 0 if result.get("status") == "PASS_CLOSED_FINITE_NUMERICAL" else 2


if __name__ == "__main__":
    raise SystemExit(main())
