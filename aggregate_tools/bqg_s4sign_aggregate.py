#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, pickle, tarfile
from pathlib import Path
import numpy as np
import bqg_depth6_41 as Z
import bqg_safe_boundary_master_gate as R

def gauss_ok(sp):
    return all(R.allowed_k2_t(*R.local_spins(sp,v)) for v in R.VERT)

def geometric_outs(sp):
    import itertools
    sp=tuple(sp); J=max(sp)+1; out=set()
    for a,b in itertools.combinations(R.NEIG[0],2):
        es=[R.EIDX[tuple(sorted((0,a)))],
            R.EIDX[tuple(sorted((a,b)))],
            R.EIDX[tuple(sorted((b,0)))]]
        for ds in itertools.product((-1,1),repeat=3):
            z=list(sp); ok=True
            for e,dd in zip(es,ds):
                z[e]+=dd
                if z[e]<0 or z[e]>J:
                    ok=False; break
            if ok:
                z=tuple(z)
                if gauss_ok(z):
                    out.add(Z.canon4(z)[0])
    return out

def extract_artifacts(root: Path, work: Path, expected_shards: int):
    work.mkdir(parents=True,exist_ok=True)
    tars=sorted(root.rglob("bqg-s4sign-shard-*.tar.gz"))
    if len(tars)!=expected_shards:
        raise SystemExit(f"expected {expected_shards} shard tarballs, got {len(tars)}")
    dirs=[]
    for t in tars:
        d=work/t.stem.replace(".tar","")
        d.mkdir(exist_ok=True)
        with tarfile.open(t,"r:gz") as tf:
            tf.extractall(d)
        dirs.append(d)
    return dirs

def load_all(dirs, expected_shards: int):
    summaries=[]; maps={}; records={}
    for d in dirs:
        ss=list(d.rglob("summary.json"))
        if len(ss)!=1:
            raise SystemExit(f"bad summary count in {d}: {len(ss)}")
        s=json.load(open(ss[0])); summaries.append(s)
        if (s["shell_states"],s["s4sign_blocks"],s["s4sign_dim"])!=(264962,11956,130112):
            raise SystemExit(f"ledger mismatch shard {s['shard']}: {s}")
        if s["failed_blocks"]!=0 or s["ok_blocks"]!=s["assigned_blocks"]:
            raise SystemExit(f"incomplete shard {s['shard']}: {s['ok_blocks']}/{s['assigned_blocks']}")
        for r in s["records"]:
            i=int(r["i"])
            if i in records: raise SystemExit(f"duplicate block {i}")
            records[i]=r
        for p in d.rglob("b*.pkl"):
            i=int(p.stem[1:])
            if i in maps: raise SystemExit(f"duplicate map {i}")
            maps[i]=pickle.load(open(p,"rb"))
    shards=sorted(int(s["shard"]) for s in summaries)
    if shards!=list(range(expected_shards)):
        raise SystemExit(f"bad shard coverage: {shards[:8]} ... {shards[-8:] if shards else []}")
    if sorted(records)!=list(range(11956)):
        raise SystemExit("block coverage incomplete")
    if sorted(maps)!=list(range(11956)):
        raise SystemExit("map coverage incomplete")
    if sum(int(r["d"]) for r in records.values())!=130112:
        raise SystemExit("column total mismatch")
    return summaries,records,maps

def certify(records,maps,outfile):
    # Conservative occupancy uses full combinatorial geometric support.
    # Numeric maps are used only to certify full rank on rows that are
    # geometrically unique at the block's removal step.
    remaining=set(records)
    support={}; occ={}
    for i,r in records.items():
        qin=tuple(r["qin"])
        ss=geometric_outs(qin)
        support[i]=ss
        for q in ss:
            occ.setdefault(q,set()).add(i)
    rounds=[]; cert={}
    while True:
        ready=[]
        for i in sorted(remaining):
            uq=[q for q in support[i] if occ[q]=={i}]
            if not uq: continue
            block=maps[i]
            mats=[block[q] for q in uq if q in block]
            if not mats: continue
            M=np.vstack(mats); d=int(records[i]["d"])
            if M.shape[0]<d: continue
            s=np.linalg.svd(M,compute_uv=False)
            smax=float(s[0]) if len(s) else 0.0
            tol=max(M.shape)*np.finfo(float).eps*max(smax,1.0)*100
            rank=int((s>tol).sum())
            sigma=float(s[-1]) if len(s)>=d else 0.0
            if rank==d and sigma>max(tol,1e-10):
                ready.append((i,d,len(uq),M.shape[0],sigma,tol))
        if not ready: break
        rounds.append({
            "round":len(rounds),
            "blocks":len(ready),
            "columns":sum(x[1] for x in ready)
        })
        for i,d,nq,nrows,sigma,tol in ready:
            cert[str(i)]={
                "d":d,"unique_q":nq,"rows":nrows,
                "sigma_min":sigma,"rank_tol":tol
            }
        for i,*_ in ready:
            remaining.remove(i)
        for i,*_ in ready:
            for q in support[i]:
                occ[q].discard(i)
        print("ROUND",rounds[-1],"remaining",len(remaining),flush=True)
    result={
      "status":"PASS" if not remaining else "RESIDUAL_CORE",
      "scope":"depth6 S4-sign input = [1^5] + [2,1,1,1]",
      "target_blocks":11956,
      "target_columns":130112,
      "certified_blocks":len(cert),
      "certified_columns":sum(v["d"] for v in cert.values()),
      "remaining_blocks":len(remaining),
      "remaining_columns":sum(int(records[i]["d"]) for i in remaining),
      "rounds":rounds,
      "global_sigma_min":min((v["sigma_min"] for v in cert.values()),default=None),
      "remaining_ids":sorted(remaining),
      "proof_logic":"Geometric-support occupancy is a conservative superset; each removed input block has a full-column-rank numeric H0 image on rows geometrically unique at its removal step."
    }
    Path(outfile).write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({
        k:result[k] for k in [
            "status","certified_blocks","certified_columns",
            "remaining_blocks","remaining_columns","global_sigma_min"
        ]},indent=2),flush=True)
    return result

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--artifacts",type=Path,required=True)
    ap.add_argument("--expected-shards",type=int,required=True)
    ap.add_argument("--work",type=Path,default=Path("_aggregate_work"))
    ap.add_argument("--out",type=Path,default=Path("bqg_depth6_s4sign_distributed_certificate.json"))
    a=ap.parse_args()
    dirs=extract_artifacts(a.artifacts,a.work,a.expected_shards)
    _,records,maps=load_all(dirs,a.expected_shards)
    certify(records,maps,a.out)

if __name__=="__main__":
    main()
