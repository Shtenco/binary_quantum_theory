#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,pickle,tarfile
from pathlib import Path
import numpy as np
import bqg_depth6_41 as Z
import bqg_safe_boundary_master_gate as R

TARGET_BLOCKS=11956
TARGET_COLUMNS=130112
SHELL_STATES=264962

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
                if gauss_ok(z): out.add(Z.canon4(z)[0])
    return out

def extract_all(root,work,expected):
    work.mkdir(parents=True,exist_ok=True)
    tars=sorted(root.rglob("*shard-*.tar.gz"))
    if len(tars)!=expected: raise SystemExit(f"expected {expected} tarballs, got {len(tars)}")
    dirs=[]
    for n,t in enumerate(tars):
        d=work/f"shard_{n:03d}"; d.mkdir(exist_ok=True)
        with tarfile.open(t,"r:gz") as tf: tf.extractall(d)
        dirs.append(d)
    return dirs

def index_artifacts(dirs,expected):
    summaries=[]; records={}; maps={}
    for d in dirs:
        ss=list(d.rglob("summary.json"))
        if len(ss)!=1: raise SystemExit(f"bad summary count in {d}: {len(ss)}")
        s=json.load(open(ss[0])); summaries.append(s)
        if (int(s["shell_states"]),int(s["s4sign_blocks"]),int(s["s4sign_dim"]))!=(SHELL_STATES,TARGET_BLOCKS,TARGET_COLUMNS):
            raise SystemExit(f"ledger mismatch shard {s['shard']}")
        if int(s["failed_blocks"])!=0 or int(s["ok_blocks"])!=int(s["assigned_blocks"]):
            raise SystemExit(f"incomplete shard {s['shard']}")
        for r in s["records"]:
            i=int(r["i"])
            if i in records: raise SystemExit(f"duplicate record {i}")
            records[i]=r
        for p in d.rglob("b*.pkl"):
            try: i=int(p.stem[1:])
            except: continue
            if i in maps: raise SystemExit(f"duplicate map {i}")
            maps[i]=p
    shards=sorted(int(s["shard"]) for s in summaries)
    if shards!=list(range(expected)): raise SystemExit("shard coverage incomplete")
    if sorted(records)!=list(range(TARGET_BLOCKS)): raise SystemExit("record coverage incomplete")
    if sorted(maps)!=list(range(TARGET_BLOCKS)): raise SystemExit("map coverage incomplete")
    if sum(int(r["d"]) for r in records.values())!=TARGET_COLUMNS: raise SystemExit("column total mismatch")
    return records,maps

def block_cert(i,uq,records,maps):
    with open(maps[i],"rb") as f: block=pickle.load(f)
    mats=[block[q] for q in uq if q in block]
    if not mats: return None
    M=np.vstack(mats); d=int(records[i]["d"])
    if M.shape[0]<d: return None
    s=np.linalg.svd(M,compute_uv=False)
    if len(s)<d: return None
    smax=float(s[0]) if len(s) else 0.0
    tol=max(M.shape)*np.finfo(float).eps*max(smax,1.0)*100.0
    rank=int((s>tol).sum()); sigma=float(s[d-1])
    if rank!=d or sigma<=max(tol,1e-10): return None
    return {"d":d,"unique_q":len(uq),"rows":int(M.shape[0]),"sigma_min":sigma,"rank_tol":float(tol)}

def certify(records,maps,positive_q,outfile):
    remaining=set(records); support={}; occ={}
    edges_raw=0; edges_kept=0
    for n,i in enumerate(sorted(records),1):
        raw=geometric_outs(tuple(records[i]["qin"]))
        ss=raw & positive_q
        edges_raw+=len(raw); edges_kept+=len(ss)
        support[i]=ss
        for q in ss: occ.setdefault(q,set()).add(i)
        if n%1000==0:
            print("GEOM",n,"raw_edges",edges_raw,"kept",edges_kept,"q",len(occ),flush=True)
    print("PRUNE_SUMMARY",json.dumps({"raw_edges":edges_raw,"kept_edges":edges_kept,"removed_edges":edges_raw-edges_kept,"positive_q":len(positive_q)}),flush=True)

    rounds=[]; cert={}; rnd=0
    while True:
        cand=[]
        for i in sorted(remaining):
            uq=[q for q in support[i] if occ[q]=={i}]
            if uq: cand.append((i,uq))
        print("ROUND_START",rnd,"remaining",len(remaining),"candidates",len(cand),flush=True)
        ready=[]
        for n,(i,uq) in enumerate(cand,1):
            c=block_cert(i,uq,records,maps)
            if c: ready.append((i,c))
            if n%250==0: print("ROUND_SCAN",rnd,n,"/",len(cand),"pass",len(ready),flush=True)
        if not ready: break
        info={"round":rnd,"blocks":len(ready),"columns":sum(c["d"] for _,c in ready)}
        rounds.append(info); print("ROUND_PASS",info,flush=True)
        for i,c in ready: cert[str(i)]=c
        for i,_ in ready: remaining.remove(i)
        for i,_ in ready:
            for q in support[i]: occ[q].discard(i)
        partial={"status":"IN_PROGRESS","certified_blocks":len(cert),"certified_columns":sum(v["d"] for v in cert.values()),"remaining_blocks":len(remaining),"remaining_columns":sum(int(records[i]["d"]) for i in remaining),"rounds":rounds}
        outfile.with_suffix(".partial.json").write_text(json.dumps(partial,indent=2)+"\n")
        rnd+=1

    result={
      "status":"PASS" if not remaining else "RESIDUAL_CORE",
      "scope":"depth6 S4-sign input=[1^5]+[2,1,1,1], exact S4-trivial-capacity-pruned support",
      "target_blocks":TARGET_BLOCKS,"target_columns":TARGET_COLUMNS,
      "certified_blocks":len(cert),"certified_columns":sum(v["d"] for v in cert.values()),
      "remaining_blocks":len(remaining),"remaining_columns":sum(int(records[i]["d"]) for i in remaining),
      "rounds":rounds,
      "global_sigma_min":min((v["sigma_min"] for v in cert.values()),default=None),
      "remaining_ids":sorted(remaining),
      "positive_output_q":len(positive_q),
      "raw_geometric_edges":edges_raw,"capacity_pruned_edges":edges_kept,
      "proof_logic":"Only output q with exact positive S4-trivial capacity are retained. Peeling then uses conservative geometric occupancy inside that exact representation-theoretic support; every removed block is certified by full-column-rank numeric H0 on rows unique at removal."
    }
    outfile.write_text(json.dumps(result,indent=2)+"\n")
    print("FINAL_SUMMARY",json.dumps({k:result[k] for k in ["status","certified_blocks","certified_columns","remaining_blocks","remaining_columns","global_sigma_min","raw_geometric_edges","capacity_pruned_edges"]}),flush=True)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--artifacts",type=Path,required=True)
    ap.add_argument("--capacity",type=Path,required=True)
    ap.add_argument("--expected-shards",type=int,default=128)
    ap.add_argument("--work",type=Path,default=Path("_aggregate_capacity_work"))
    ap.add_argument("--out",type=Path,required=True)
    a=ap.parse_args()
    positive_q={tuple(q) for q in json.load(open(a.capacity))["positive_q"]}
    if len(positive_q)!=29761: raise SystemExit(f"positive_q mismatch {len(positive_q)}")
    dirs=extract_all(a.artifacts,a.work,a.expected_shards)
    records,maps=index_artifacts(dirs,a.expected_shards)
    print("AUDIT",json.dumps({"shards":a.expected_shards,"blocks":len(records),"maps":len(maps),"columns":sum(int(r["d"]) for r in records.values()),"positive_q":len(positive_q)}),flush=True)
    certify(records,maps,positive_q,a.out)

if __name__=="__main__": main()
