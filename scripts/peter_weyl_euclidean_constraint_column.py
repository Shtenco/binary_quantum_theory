#!/usr/bin/env python3
"""Export one complete Euclidean Peter-Weyl outgoing constraint column.

The output schema matches the complete Gauss-state serialization used by the
Lorentzian epsilon aggregate and can be consumed directly by
bqg_constraint_master_assembler_gate.py.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
import k5_peter_weyl_safe_hda_column as PW


def encode(state):
    rows=[]
    for (spins,Ks),amp in sorted(state.items(),key=lambda kv:repr(kv[0])):
        rows.append({"spins":[int(x) for x in spins],"K_labels":[int(x) for x in Ks],"amp":[float(complex(amp).real),float(complex(amp).imag)]})
    return rows


def norm2(state): return float(sum(abs(z)**2 for z in state.values()))


def run(node,input_index,jmax2=5,prune=1e-8):
    basis=PW.basis_full_jhalf()
    if not (0<=node<5): raise ValueError("node must be 0..4")
    if not (0<=input_index<len(basis)): raise ValueError("bad input index")
    initial=basis[input_index]
    out=PW.apply_H_cached_state({initial:1+0j},node,jmax2); out=PW.prune_state(out,prune)
    rows=encode(out); payload={
        "status":"complete Euclidean Peter-Weyl outgoing constraint column",
        "passed":True,"family":"E","node":node,"input_index":input_index,"input_K_labels":list(initial[1]),
        "Jmax":jmax2/2,"prune_threshold":prune,
        "complete_gauss_outgoing_column":{"support":len(out),"norm":norm2(out)**0.5,"basis":"Peter-Weyl Gauss basis (spins,K_labels)","state":rows},
        "column_sha256":hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(",",":")).encode()).hexdigest(),
        "claim_boundary":"Serialized microscopic H_E column only; no projector or physical observable is inferred."
    }
    return payload


def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--node',type=int,required=True); ap.add_argument('--input-index',type=int,required=True); ap.add_argument('--jmax2',type=int,default=5); ap.add_argument('--prune',type=float,default=1e-8); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args()
    out=run(a.node,a.input_index,a.jmax2,a.prune); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps({k:v for k,v in out.items() if k!='complete_gauss_outgoing_column'},indent=2)); return 0

if __name__=='__main__': raise SystemExit(main())
