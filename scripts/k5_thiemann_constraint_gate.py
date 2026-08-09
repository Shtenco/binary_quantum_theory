#!/usr/bin/env python3
"""Exact finite K5 Thiemann-type Hamiltonian-constraint kernel test.

On the 32-dimensional fully-active five-tetrahedron sector of the exact 140D
SO(5)-vector quantum-link K5 model, build local graph-changing constraint
kernels

  T(v;a,b|c) = Tr[(U_ab_loop-U_ab_loop^dag) U_c [U_c^dag,V_v]]

with V_v the exact projector that all four links incident at v are in the
active geometric bi-doublet.  No target-state coefficient enters the operator.

The independent j=1/2 five-tetrahedron 4-simplex vertex tensor is then tested
against the common kernel of all local constraints.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from pathlib import Path

import numpy as np

SCRIPTS=Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path: sys.path.insert(0,str(SCRIPTS))

import k5_quantum_geometry_bridge as K5  # noqa:E402


def op_transitions(op):
    out={}
    for d in range(5):
        out[d]=[(int(od),op[od,d]) for od in np.flatnonzero(np.abs(op[:,d])>1e-12)]
    return out


def build_runtime():
    meta,states,reverse=K5.build_gauss_basis()
    Up,Ud=K5.transformed_link_U()
    powers=[5**(9-e) for e in range(10)]
    vac,full_order,V5,target=K5.target_and_sectors(meta)
    trans_cache={}
    def trans(op):
        key=id(op)
        if key not in trans_cache: trans_cache[key]=op_transitions(op)
        return trans_cache[key]
    return meta,states,reverse,Up,Ud,powers,full_order,V5,target,trans


def project_state(raw,reverse):
    vec=np.zeros(140,complex)
    for idx,a in raw.items():
        for row,ca in reverse.get(idx,[]): vec[row]+=ca*a
    return vec


def raw_norm(raw):
    return math.sqrt(sum(abs(a)**2 for a in raw.values()))


def add_scaled(dst,src,scale=1.0):
    for idx,a in src.items(): dst[idx]=dst.get(idx,0)+scale*a


def make_actions(Up,Ud,powers,trans):
    def Udir(x,y): return Up if x<y else Ud

    def single(raw,e,op):
        t=trans(op); p=powers[e]; out={}
        for idx,a in raw.items():
            d=(idx//p)%5; base=idx-d*p
            for od,c in t[d]: out[base+od*p]=out.get(base+od*p,0)+c*a
        return out

    def path_component(raw,path,iout,iin):
        m=len(path)-1
        if m==1:
            e=K5.EDGE_INDEX[tuple(sorted((path[0],path[1])))]
            return single(raw,e,Udir(path[0],path[1])[iout,iin])
        out={}
        for mids in itertools.product(range(2),repeat=m-1):
            colors=(iout,)+mids+(iin,); tmp=raw
            for r,(x,y) in enumerate(zip(path[:-1],path[1:])):
                e=K5.EDGE_INDEX[tuple(sorted((x,y)))]
                tmp=single(tmp,e,Udir(x,y)[colors[r],colors[r+1]])
                if not tmp: break
            add_scaled(out,tmp)
        return out

    def volume(raw,v):
        inc=[K5.EDGE_INDEX[tuple(sorted((v,w)))] for w in K5.VERTICES if w!=v]
        return {idx:a for idx,a in raw.items() if all(((idx//powers[e])%5)<4 for e in inc)}

    def comm_segment_volume(raw,v,c,k,i):
        # [U(c->v)_{ki}, V_v] = U^dag V - V U^dag in the chosen orientation.
        first=path_component(volume(raw,v),[c,v],k,i)
        second=volume(path_component(raw,[c,v],k,i),v)
        out={}; add_scaled(out,first,1); add_scaled(out,second,-1); return out

    def local_constraint(raw,v,a,b,c):
        # Tr[(P(vabv)-P(vbav)) U(v,c) [U(c,v),V_v]].
        out={}
        for i,j,k in itertools.product(range(2),repeat=3):
            tmp=comm_segment_volume(raw,v,c,k,i)
            if not tmp: continue
            tmp=path_component(tmp,[v,c],j,k)
            if not tmp: continue
            fwd=path_component(tmp,[v,a,b,v],i,j)
            rev=path_component(tmp,[v,b,a,v],i,j)
            add_scaled(out,fwd,1); add_scaled(out,rev,-1)
        return out

    return local_constraint


def local_specs():
    specs=[]
    for v in K5.VERTICES:
        neigh=sorted(w for w in K5.VERTICES if w!=v)
        for triple in itertools.combinations(neigh,3):
            a,b,c=triple
            # Cyclic representatives of the antisymmetric IJK sum.
            specs.extend([(v,a,b,c),(v,b,c,a),(v,c,a,b)])
    return specs


def run():
    meta,states,reverse,Up,Ud,powers,full_order,V5,target,trans=build_runtime()
    local=make_actions(Up,Ud,powers,trans)
    specs=local_specs()

    # Sparse raw representation of the independent four-simplex target.
    raw_target={}
    target32=V5/np.linalg.norm(V5)
    for coeff,bi in zip(target32,full_order):
        for idx,a in states[bi].items(): raw_target[idx]=raw_target.get(idx,0)+coeff*a

    # First show that all 60 local constraints annihilate the target itself.
    target_residuals=[]
    for spec in specs:
        target_residuals.append(raw_norm(local(raw_target,*spec)))

    # Build full-sector maps only for the first three nodes.  They already leave
    # a one-dimensional common kernel, so the remaining nodes cannot reduce it
    # further if the target residual above is zero within numerical tolerance.
    rank_rows=[]; blocks=[]; max_projection_leakage=0.0
    for node in (0,1,2):
        for spec in [s for s in specs if s[0]==node]:
            M=np.zeros((140,32),complex)
            for col,bi in enumerate(full_order):
                raw=local(states[bi],*spec)
                raw_n=raw_norm(raw)
                pv=project_state(raw,reverse); M[:,col]=pv
                if raw_n>1e-13:
                    leak=max(0.0,1.0-(np.linalg.norm(pv)/raw_n)**2)
                    max_projection_leakage=max(max_projection_leakage,leak)
            blocks.append(M)
        stack=np.vstack(blocks)
        _,sv,Vh=np.linalg.svd(stack,full_matrices=False)
        rank=int(np.sum(sv>1e-9)); kernel=32-rank
        null_fidelity=None
        if kernel==1:
            null=Vh[-1].conj(); null/=np.linalg.norm(null)
            null_fidelity=float(abs(np.vdot(null,target32))**2)
        rank_rows.append({"nodes_included":list(range(node+1)),"number_local_constraints":len(blocks),"rank":rank,"kernel_dimension":kernel,"smallest_nonzero_singular":float(sv[rank-1]) if rank else 0.0,"smallest_singular":float(sv[-1]),"unique_null_fidelity_to_4simplex":null_fidelity})

    final=rank_rows[-1]
    passed=(len(meta)==140 and len(full_order)==32 and len(specs)==60 and final["kernel_dimension"]==1 and final["unique_null_fidelity_to_4simplex"] is not None and abs(final["unique_null_fidelity_to_4simplex"]-1)<1e-10 and max(target_residuals)<1e-10 and max_projection_leakage<1e-10)

    return {
        "status":"exact finite K5 Thiemann-type common-kernel constraint gate",
        "passed":bool(passed),
        "Gauss_hilbert_dimension":len(meta),
        "fully_active_intertwiner_dimension":len(full_order),
        "number_local_constraint_kernels":len(specs),
        "target_max_raw_constraint_residual":float(max(target_residuals)),
        "target_mean_raw_constraint_residual":float(np.mean(target_residuals)),
        "max_Gauss_projection_leakage_first_three_nodes":float(max_projection_leakage),
        "common_kernel_rank_flow":rank_rows,
        "final_statement":"The 36 local constraints attached to the first three tetrahedral nodes already leave a one-dimensional common kernel, and that unique vector is the independently constructed 4-simplex vertex with unit fidelity. The remaining 24 local constraints also annihilate that target, so all 60 share the same one-dimensional physical kernel in the tested sector.",
        "operator_definition":"T(v;a,b|c)=Tr[(U(vabv)-U(vbav)) U(v,c) [U(c,v),P_{k_v=4}]]",
        "scope_note":"This is a Euclidean/canonical finite regularization with the microscopic j=1/2 nondegenerate-volume projector. It is a Wheeler-DeWitt-like kernel test, not yet the full real Lorentzian Hamiltonian, HDA closure, continuum universality, matter or experiment."
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--output",type=Path); a=ap.parse_args(); out=run(); txt=json.dumps(out,indent=2); print(txt)
    if a.output: a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(txt+"\n",encoding="utf-8")
    return 0 if out["passed"] else 1

if __name__=="__main__": raise SystemExit(main())
