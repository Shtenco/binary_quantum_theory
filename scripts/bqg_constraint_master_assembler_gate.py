#!/usr/bin/env python3
"""Reusable BQG Euclidean/Lorentzian constraint-master assembler.

Expensive microscopic actions are serialized as sparse outgoing columns.  Given
one column for every declared domain basis vector and every separately labelled
node constraint, this module assembles

    M(lambda) = M_EE + lambda M_EL + lambda^2 M_LL

without re-running Peter-Weyl actions.  Only a manifest declaring the supplied
domain to be the complete finite regulated habitat may receive a spectral
physical-projector output.  Restricted boundary/Krylov domains are reported only
as diagnostics.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import numpy as np


def sparse_inner(a: dict, b: dict) -> complex:
    if len(a) > len(b):
        return np.conj(sparse_inner(b, a))
    return sum(np.conj(x) * b.get(k, 0j) for k, x in a.items())


def gram(images: list[dict]) -> np.ndarray:
    n=len(images); G=np.zeros((n,n),complex)
    for i in range(n):
        for j in range(i,n):
            z=sparse_inner(images[i],images[j]); G[i,j]=z; G[j,i]=np.conj(z)
    return G


def cross_gram(left: list[dict], right: list[dict]) -> np.ndarray:
    if len(left)!=len(right): raise ValueError("left/right domain dimensions differ")
    n=len(left); G=np.zeros((n,n),complex)
    for i in range(n):
        for j in range(n): G[i,j]=sparse_inner(left[i],right[j])
    return G


def spectral_audit(M: np.ndarray, rtol=1e-10):
    M=0.5*(M+M.conj().T)
    ev,U=np.linalg.eigh(M)
    scale=max(float(np.max(np.abs(ev))),1.0); thr=rtol*scale
    zero=np.abs(ev)<=thr; pos=ev[ev>thr]; Q=U[:,zero]
    return {"matrix":M,"eigenvalues":ev,"rank_tolerance":thr,
            "rank":int(np.sum(ev>thr)),"nullity":int(np.sum(zero)),
            "smallest_positive":float(np.min(pos)) if pos.size else None,
            "condition_number_on_support":float(np.max(pos)/np.min(pos)) if pos.size else None,
            "Q0":Q,"P0":Q@Q.conj().T}


def assemble(node_E, node_L, lam):
    nodes=sorted(set(node_E)|set(node_L))
    if set(node_E)!=set(node_L): raise ValueError("E/L node labels do not match")
    if not nodes: raise ValueError("empty constraint family")
    n=len(node_E[nodes[0]])
    if any(len(node_E[v])!=n or len(node_L[v])!=n for v in nodes):
        raise ValueError("each node must contain every domain column")
    MEE=np.zeros((n,n),complex); MLL=np.zeros_like(MEE); MEL=np.zeros_like(MEE); rows=[]
    for v in nodes:
        EE=gram(node_E[v]); LL=gram(node_L[v]); X=cross_gram(node_E[v],node_L[v]); mixed=X+X.conj().T
        MEE+=EE; MLL+=LL; MEL+=mixed
        rows.append({"node":v,"EE_trace":float(np.trace(EE).real),"LL_trace":float(np.trace(LL).real),
                     "EL_cross_frobenius_norm":float(np.linalg.norm(X)),"mixed_frobenius_norm":float(np.linalg.norm(mixed))})
    M=MEE+lam*MEL+lam*lam*MLL
    return MEE,MEL,MLL,0.5*(M+M.conj().T),rows


def hash_arrays(*arrs):
    h=hashlib.sha256()
    for A in arrs:
        x=np.ascontiguousarray(A); h.update(str(x.shape).encode()); h.update(x.view(np.uint8))
    return h.hexdigest()


def decode_state_rows(rows):
    state={}
    for r in rows:
        if "K_labels" in r:
            key=(tuple(int(x) for x in r["spins"]),tuple(int(x) for x in r["K_labels"]))
        elif "Kother" in r:
            # Covariant form is accepted only if explicitly requested upstream;
            # production master should normally use the Gauss serialization.
            key=(tuple(int(x) for x in r["spins"]),tuple(int(x) for x in r["Kother"]),
                 int(r["J2"]),int(r["M2"]),int(r["K12"]),int(r["K34"]))
        elif "basis_index" in r:
            key=(int(r["basis_index"]),)
        else:
            raise ValueError("unrecognized sparse-state row schema")
        z=complex(float(r["amp"][0]),float(r["amp"][1])); state[key]=state.get(key,0j)+z
    return state


def load_column(path: Path):
    data=json.loads(path.read_text(encoding="utf-8"))
    if "complete_gauss_outgoing_column" in data:
        rows=data["complete_gauss_outgoing_column"]["state"]
    elif "state" in data:
        rows=data["state"]
    else:
        raise ValueError(f"{path}: no complete_gauss_outgoing_column/state")
    return decode_state_rows(rows),data


def assemble_manifest(manifest_path: Path):
    m=json.loads(manifest_path.read_text(encoding="utf-8")); base=manifest_path.parent
    dim=int(m["domain_dimension"]); nodes=[int(x) for x in m["nodes"]]; lam=float(m["lambda_L"])
    domain_complete=bool(m.get("domain_complete",False))
    E={v:[None]*dim for v in nodes}; L={v:[None]*dim for v in nodes}; hashes=[]
    for row in m["columns"]:
        fam=str(row["family"]); v=int(row["node"]); i=int(row["input_index"])
        if fam not in ("E","L") or v not in E or not (0<=i<dim): raise ValueError(f"bad column descriptor {row}")
        p=(base/row["path"]).resolve(); st,data=load_column(p); hashes.append(hashlib.sha256(p.read_bytes()).hexdigest())
        target=E if fam=="E" else L
        if target[v][i] is not None: raise ValueError(f"duplicate {fam},node={v},input={i}")
        target[v][i]=st
    missing=[]
    for fam,target in (("E",E),("L",L)):
        for v in nodes:
            for i,x in enumerate(target[v]):
                if x is None: missing.append([fam,v,i])
    if missing: raise ValueError(f"missing columns ({len(missing)}): {missing[:12]}")
    MEE,MEL,MLL,M,rows=assemble(E,L,lam); a=spectral_audit(M)
    mixed_ratio=float(np.linalg.norm(MEL)/max(np.linalg.norm(MEE)+lam*lam*np.linalg.norm(MLL),1e-300))
    result={
        "status":"COMPLETE_FINITE_HABITAT_MASTER" if domain_complete else "RESTRICTED_DOMAIN_MASTER_DIAGNOSTIC",
        "passed":True,"domain_label":m.get("domain_label"),"domain_dimension":dim,"domain_complete":domain_complete,
        "nodes":nodes,"lambda_L":lam,"master_pencil_hash":hash_arrays(MEE,MEL,MLL),
        "column_file_hashes":hashes,"per_node":rows,"mixed_block_relative_norm":mixed_ratio,
        "spectrum":{"rank":a["rank"],"nullity":a["nullity"],"rank_tolerance":a["rank_tolerance"],
                    "eigenvalue_min":float(np.min(a["eigenvalues"])),"eigenvalue_max":float(np.max(a["eigenvalues"])),
                    "smallest_positive":a["smallest_positive"],"condition_number_on_support":a["condition_number_on_support"],
                    "eigenvalues":[float(x) for x in a["eigenvalues"]]},
        "physical_projector_emitted":domain_complete,
        "claim_boundary":"A restricted-domain nullity is never a statement about the full physical Hilbert space. Independent D_target/HDA certification remains separate."
    }
    if domain_complete:
        P=a["P0"]
        result["physical_projector"]=[[[float(z.real),float(z.imag)] for z in row] for row in P]
    return result


def matrix_columns(A):
    out=[]
    for j in range(A.shape[1]): out.append({(i,):complex(A[i,j]) for i in range(A.shape[0]) if abs(A[i,j])>1e-14})
    return out


def selftest():
    rng=np.random.default_rng(5092026); dim=6; E={};L={};dE={};dL={}
    for v in range(3):
        A=rng.normal(size=(5,5))+1j*rng.normal(size=(5,5)); A=.5*(A+A.conj().T)+(2+.25*v)*np.eye(5)
        B=rng.normal(size=(5,5))+1j*rng.normal(size=(5,5)); B=.5*(B+B.conj().T)+(1.3+.17*v)*np.eye(5)
        Ae=np.zeros((dim,dim),complex); Bl=np.zeros_like(Ae); Ae[1:,1:]=A; Bl[1:,1:]=B
        dE[v]=Ae;dL[v]=Bl;E[v]=matrix_columns(Ae);L[v]=matrix_columns(Bl)
    lam=.73; MEE,MEL,MLL,M,_=assemble(E,L,lam)
    direct=sum((dE[v]+lam*dL[v]).conj().T@(dE[v]+lam*dL[v]) for v in range(3)); a=spectral_audit(M)
    e0=np.zeros(dim);e0[0]=1
    full_ok=np.linalg.norm(M-direct)<2e-10 and a["nullity"]==1 and np.linalg.norm(a["P0"]-np.outer(e0,e0))<2e-10
    Mfull=np.diag([1.,0.]); B=np.array([[1.],[0.]]); ar=spectral_audit(B.T@Mfull@B); af=spectral_audit(Mfull)
    neg_ok=ar["nullity"]==0 and af["nullity"]==1
    return {"status":"BQG E/L outgoing-column master assembler regression","passed":bool(full_ok and neg_ok),
            "formula":"M(lambda)=M_EE+lambda M_EL+lambda^2 M_LL",
            "complete_habitat_control":{"passed":bool(full_ok),"nullity":a["nullity"],"master_hash":hash_arrays(MEE,MEL,MLL)},
            "restricted_domain_negative_control":{"passed":bool(neg_ok),"restricted_nullity":ar["nullity"],"full_nullity":af["nullity"]},
            "production_rule":"Only --manifest with domain_complete=true emits P_phys; D_target/HDA certification is an independent required gate."}


def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--manifest",type=Path); ap.add_argument("--output",type=Path,default=Path("verification_results/BQG_CONSTRAINT_MASTER_ASSEMBLER.json")); a=ap.parse_args()
    out=assemble_manifest(a.manifest) if a.manifest else selftest(); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8"); print(json.dumps({k:v for k,v in out.items() if k!="physical_projector"},indent=2)); return 0 if out["passed"] else 1

if __name__=="__main__": raise SystemExit(main())
