#!/usr/bin/env python3
"""Aggregate serial BQG multiplicity-master scale results without overclaiming.

Reads one or more JSON outputs from bqg_serial_multiplicity_master_scan.py and
creates a canonical RG table.  Only quantities actually present in finite
scale calculations are filled.  eta_j and epsilon_j^sf are deliberately left
OPEN until a cross-scale channel transport and full-master/off-channel leakage
calculation exists.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

def load_rows(paths):
    rows=[]
    for p in paths:
        obj=json.loads(Path(p).read_text(encoding="utf-8"))
        rows.extend(obj.get("rows",[]))
    uniq={}
    for r in rows:
        uniq[int(r["s2"])]=r
    return [uniq[k] for k in sorted(uniq)]

def run(paths):
    rows=load_rows(paths)
    table=[]
    for r in rows:
        table.append({
            "j":r["j"],
            "s2":r["s2"],
            "m22":r["m22"],
            "A_j_eigenvalues":r["A_j_eigenvalues"],
            "gamma_j_low":r["gamma_low"],
            "pair_spread_max":r["pair_spread_max"],
            "twirled_S4_commutator_max":r["twirled_S4_commutator_max"],
            "twirl_relative_change":r["twirl_relative_change"],
            "eta_j_status":"OPEN_REQUIRES_CROSS_SCALE_SELECTED_CHANNEL_TRANSPORT",
            "epsilon_j_sf_status":"OPEN_REQUIRES_FULL_MASTER_OFF_CHANNEL_LEAKAGE_AND_GAPS",
        })
    return {
        "status":"canonical BQG RG convergence table - finite data only",
        "rows":table,
        "closed_columns":[
            "j","m22","A_j_eigenvalues","gamma_j_low",
            "pair_spread_max","twirled_S4_commutator_max","twirl_relative_change"
        ],
        "open_columns":[
            "eta_j","epsilon_j_sf"
        ],
        "claim_boundary":{
            "eta_j":"Must come from a defined cross-scale selected-channel transport/perturbation, not eigenvalue-list subtraction.",
            "epsilon_j_sf":"Must come from a full master comparison that retains off-channel leakage and physical gaps; a scalar restriction to one isolated irrep copy can be rescaled trivially."
        }
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("inputs",nargs="+")
    ap.add_argument("--output",type=Path)
    a=ap.parse_args()
    out=run(a.inputs)
    txt=json.dumps(out,indent=2)
    print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(txt+"\n",encoding="utf-8")
if __name__=="__main__":
    main()
