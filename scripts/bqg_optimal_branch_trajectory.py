#!/usr/bin/env python3
"""Exact dynamic-programming optimizer for BQG branch-transfer matrices."""
from __future__ import annotations
import argparse,json,math
from pathlib import Path

def solve(Fs):
    # Fs[k][r][s]
    n0=len(Fs[0])
    prod=[1.0]*n0
    bott=[1.0]*n0
    prod_paths=[[r] for r in range(n0)]
    bott_paths=[[r] for r in range(n0)]

    for F in Fs:
        nt=len(F[0])
        npd=[-1.0]*nt; nb=[-1.0]*nt
        npp=[None]*nt; nbp=[None]*nt
        for s in range(nt):
            for r in range(len(F)):
                p=prod[r]*F[r][s]
                if p>npd[s]:
                    npd[s]=p; npp[s]=prod_paths[r]+[s]
                q=min(bott[r],F[r][s])
                if q>nb[s]:
                    nb[s]=q; nbp[s]=bott_paths[r]+[s]
        prod,bott=npd,nb
        prod_paths,bott_paths=npp,nbp

    ip=max(range(len(prod)),key=lambda i:prod[i])
    ib=max(range(len(bott)),key=lambda i:bott[i])
    ppath=prod_paths[ip]; bpath=bott_paths[ib]

    def per_step(path):
        vals=[]
        for k in range(len(Fs)):
            f=Fs[k][path[k]][path[k+1]]
            vals.append({"F":f,"chi":math.sqrt(max(0.0,1.0-f))})
        return vals

    return {
        "maximum_product_path":ppath,
        "maximum_product_score":prod[ip],
        "maximum_product_action":(-math.log(prod[ip]) if prod[ip]>0 else math.inf),
        "maximum_product_steps":per_step(ppath),
        "maximum_bottleneck_path":bpath,
        "maximum_bottleneck_score":bott[ib],
        "maximum_bottleneck_steps":per_step(bpath),
        "same_path":ppath==bpath,
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("inputs",nargs="+")
    a=ap.parse_args()
    objs=[json.loads(Path(p).read_text()) for p in a.inputs]
    Fs=[o["F_matrix"] for o in objs]
    print(json.dumps(solve(Fs),indent=2))

if __name__=="__main__":
    main()
