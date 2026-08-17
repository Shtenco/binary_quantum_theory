#!/usr/bin/env python3
"""Exact ordered-path shard for the j=1 S4-doublet higher-shell calculation.

For logical column i and s,r in {0,1}, compute

    a_s      = H_s |i>
    b_{r,s}  = H_r H_s |i>.

Linearity reconstructs the original monolithic objects exactly:

    a_i = (H_0+H_1)|i> = a_0+a_1,
    b_i = (H_0+H_1)^2|i> = sum_{r,s} b_{r,s}.

This is only a computational factorization.  Operator ordering, sine
Hamiltonian, j=1 S4 carrier and Jmax=5/2 wall are unchanged.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

import peter_weyl_j1_higher_shell_lambda_gate as J1
import peter_weyl_higher_shell_lambda_gate as HS
import peter_weyl_euclidean_sine_ordering_gate as SINE

TOL=HS.TOL
NODES=(0,1)

def apply_node(state,node):
    return {k:a for k,a in SINE.safe_H_sine(state,node,HS.JMAX2_SECOND_HIT_SAFE).items() if abs(a)>TOL}

def compute(column,first_node,second_node):
    if not 0<=column<J1.NLOGICAL: raise ValueError(column)
    if first_node not in NODES or second_node not in NODES: raise ValueError((first_node,second_node))
    J1.AN.ZVM.patch_and_clear()
    bits=J1.logical_labels_bits()[column]
    ket=J1.coarse_state(bits)
    a=apply_node(ket,first_node)
    b=apply_node(a,second_node)
    all_j1={k:v for k,v in a.items() if all(s==2 for s in k[0])}
    return {
      "status":"exact j=1 higher-shell ordered-path shard",
      "column":column,
      "first_node":first_node,
      "second_node":second_node,
      "label":{"bits_q0_q1_q2_q3_q4":list(bits),"environment_bits_q234":list(bits[2:]),"pair_bits_q01":list(bits[:2])},
      "Jmax_used":HS.JMAX2_SECOND_HIT_SAFE/2.0,
      "first_order_all_j1_projection_norm":float(J1.AN.sparse_norm(all_j1)),
      "first_support":len(a),
      "second_path_support":len(b),
      "first_max_spin":J1.max_spin(a),
      "second_path_max_spin":J1.max_spin(b),
      "first_state":HS.state_to_rows(a),
      "second_path_state":HS.state_to_rows(b),
      "identity":"a_s=H_s|i>; b_rs=H_r H_s|i>; exact column is a=sum_s a_s, b=sum_rs b_rs",
      "scope":"exact computational sharding only; no projector, coupling or RG coefficient is fitted"
    }

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--column',type=int,required=True)
    ap.add_argument('--first-node',type=int,choices=NODES,required=True)
    ap.add_argument('--second-node',type=int,choices=NODES,required=True)
    ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args(); out=compute(a.column,a.first_node,a.second_node)
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:out[k] for k in ('column','first_node','second_node','first_support','second_path_support','first_order_all_j1_projection_norm','second_path_max_spin')},indent=2))
    return 0 if out['first_order_all_j1_projection_norm']<1e-12 else 1
if __name__=='__main__': raise SystemExit(main())
