#!/usr/bin/env python3
"""Exact j=1/2 five-tetrahedron K5 spin-network vertex tensor.

Five four-valent SU(2)-singlet tetrahedral intertwiners are contracted along
the ten K5 links with the spin-1/2 invariant epsilon tensor.  The resulting
32-component tensor is analyzed as causal 1->4 and 2->3 maps.
"""
from __future__ import annotations
import argparse,itertools,json,math
from pathlib import Path
import numpy as np

EPS2=np.array([[0,1],[-1,0]],complex)

def intertwiners():
    z=np.array([1,0],complex);o=np.array([0,1],complex)
    s=(np.kron(z,o)-np.kron(o,z))/math.sqrt(2)
    i0=np.kron(s,s)
    tp=np.kron(z,z);t0=(np.kron(z,o)+np.kron(o,z))/math.sqrt(2);tm=np.kron(o,o)
    i1=(np.kron(tp,tm)-np.kron(t0,t0)+np.kron(tm,tp))/math.sqrt(3)
    return [i0.reshape(2,2,2,2),i1.reshape(2,2,2,2)]

def apply_axis(T,axis,M):
    A=np.moveaxis(T,axis,0);B=np.tensordot(M,A,axes=(1,0));return np.moveaxis(B,0,axis)

def node_tensor(v,iota,I):
    T=I[iota].copy();neighbors=[w for w in range(5) if w!=v]
    for ax,w in enumerate(neighbors):
        if w<v:T=apply_axis(T,ax,EPS2)
    return T

def vertex_tensor():
    I=intertwiners();V=np.zeros((2,)*5,complex)
    for io in itertools.product(range(2),repeat=5):
        T=[node_tensor(v,io[v],I) for v in range(5)]
        V[io]=np.einsum('abcd,aefg,behi,cfhj,dgij->',*T,optimize=True)
    return V

def reduced(psi,keep):
    keep=list(keep);trace=[i for i in range(5) if i not in keep]
    A=np.transpose(psi.reshape((2,)*5),keep+trace).reshape(2**len(keep),-1)
    return A@A.conj().T

def entropy(rho):
    e=np.linalg.eigvalsh(rho);e=e[e>1e-14];return float(-np.sum(e*np.log2(e)))

def run():
    V=vertex_tensor();flat=V.reshape(-1);norm2=float(np.vdot(flat,flat).real);psi=flat/math.sqrt(norm2)
    nz=[]
    for idx,val in enumerate(flat):
        if abs(val)>1e-12:nz.append({"bits":list(np.unravel_index(idx,(2,)*5)),"amplitude":float(val.real)})
    one=[]
    for v in range(5):
        rho=reduced(psi,[v]);one.append({"v":v,"eigenvalues":np.linalg.eigvalsh(rho).tolist(),"entropy_bits":entropy(rho)})
    two=[]
    for pair in itertools.combinations(range(5),2):
        rho=reduced(psi,pair);eig=np.linalg.eigvalsh(rho);two.append({"pair":list(pair),"eigenvalues":eig.tolist(),"entropy_bits":entropy(rho),"Schmidt_condition":float(math.sqrt(eig.max()/eig.min()))})
    # Raw unnormalised map Gram spectra scale by norm2.
    raw_1=[norm2*x for x in one[0]["eigenvalues"]]
    raw_2=[norm2*x for x in two[0]["eigenvalues"]]
    passed=(len(nz)==12 and abs(norm2-7/18)<1e-12 and all(np.max(np.abs(np.asarray(x["eigenvalues"])-0.5))<1e-12 for x in one) and all(np.max(np.abs(np.asarray(x["eigenvalues"])-np.array([1/7,3/14,3/14,3/7])))<1e-12 for x in two))
    return {"status":"exact five-tetrahedron j=1/2 vertex tensor","passed":bool(passed),"nonzero_components":nz,"number_nonzero":len(nz),"tensor_norm_squared":norm2,"exact_norm_squared":"7/18","one_vs_four":one,"raw_1_to_4_Gram_eigenvalues":raw_1,"exact_1_to_4_statement":"M^dag M=(7/36) I, so (6/sqrt(7)) M is an exact isometry","two_vs_three":two,"raw_2_to_3_Gram_eigenvalues":raw_2,"exact_2_to_3_spectrum":"{1/18,1/12,1/12,1/6}; condition number sqrt(3), hence raw 2->3 is not isometric","interpretation":"The same simplicial vertex is exactly isometric for the 1->4 causal partition after one scalar normalization, but not for 2->3. A unitary causal theory must therefore add an environment/history record, use a polar isometry, or not treat the raw 2->3 amplitude as a fundamental isometric step."}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--output",type=Path);a=ap.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+"\n",encoding="utf-8")
    return 0 if o["passed"] else 1
if __name__=="__main__":raise SystemExit(main())
