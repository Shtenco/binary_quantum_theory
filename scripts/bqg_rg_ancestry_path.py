#!/usr/bin/env python3
"""Find the ancestry-consistent maximum-fidelity path through BQG channel-flow matrices."""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import numpy as np

def load(paths):
    mats=[]
    for p in paths:
        x=json.loads(Path(p).read_text(encoding="utf-8"))
        mats.append(x)
    mats.sort(key=lambda x:x["source_s2"])
    for a,b in zip(mats,mats[1:]):
        if a["target_s2"]!=b["source_s2"]:
            raise ValueError("nonconsecutive flow matrices")
    return mats

def solve(mats):
    # initial source channel dimension from first matrix; for j=3/2 this is 1.
    n0=len(mats[0]["source_master_eigenvalues"])
    score=np.full(n0,-np.inf)
    score[:] = 0.0 if n0==1 else -math.log(n0)  # neutral if no unique start
    paths=[[i] for i in range(n0)]

    stages=[]
    for M in mats:
        F=np.asarray(M["channel_flow_matrix"],float)
        if F.shape[0]!=len(score):
            raise ValueError("matrix/source score shape mismatch")
        new=np.full(F.shape[1],-np.inf)
        npaths=[None]*F.shape[1]
        parent=[None]*F.shape[1]
        for b in range(F.shape[1]):
            vals=[]
            for a in range(F.shape[0]):
                f=max(F[a,b],1e-300)
                vals.append(score[a]+math.log(f))
            a=int(np.argmax(vals))
            new[b]=vals[a]
            npaths[b]=paths[a]+[b]
            parent[b]=a
        stages.append({
          "source_j":M["source_j"],"target_j":M["target_j"],
          "flow_matrix":F.tolist(),"best_parent_for_target":parent,
          "best_log_fidelity_to_target":[float(x) for x in new]
        })
        score=new; paths=npaths

    end=int(np.argmax(score))
    path=paths[end]
    best_log=float(score[end])
    best_product=float(math.exp(best_log))

    # per-step overlaps and chosen master eigenvalues
    steps=[]
    for k,M in enumerate(mats):
        a=path[k]; b=path[k+1]
        F=np.asarray(M["channel_flow_matrix"],float)
        steps.append({
          "source_j":M["source_j"],"target_j":M["target_j"],
          "source_channel":int(a),"target_channel":int(b),
          "source_master_eigenvalue":float(M["source_master_eigenvalues"][a]),
          "target_master_eigenvalue":float(M["target_master_eigenvalues"][b]),
          "overlap":float(F[a,b]),
          "mismatch":float(math.sqrt(max(0.0,1-F[a,b]))),
        })

    return {
      "status":"maximum-fidelity ancestry path through BQG multiplicity channels",
      "channel_path":[int(x) for x in path],
      "best_log_fidelity":best_log,
      "best_cumulative_fidelity":best_product,
      "steps":steps,
      "stages":stages,
      "claim_boundary":"This optimizes representation-RG projector overlap, not physical probability or action. It is a preregistered ancestry criterion for selecting a finite microscopic lineage without imposing lowest-eigenvalue choice."
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("inputs",nargs="+")
    ap.add_argument("--output",type=Path)
    a=ap.parse_args()
    out=solve(load(a.inputs))
    txt=json.dumps(out,indent=2); print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(txt+"\n",encoding="utf-8")

if __name__=="__main__":
    main()
