#!/usr/bin/env python3
"""Exact 140D K5 quantum-link geometrogenesis and gravity-channel test.

Builds the Gauss-invariant Hilbert space of ten SO(5)-vector SU(2) quantum
links on K5, constructs all ten triangular Wilson-loop operators, and compares
vacuum-generated geometry with the independent j=1/2 five-tetrahedron
4-simplex spin-network vertex.

Main finite results tested here:
  * raw 5^10 link Hilbert -> 140 exact Gauss states;
  * fully active five-tetrahedron sector has dimension 32;
  * P_full (sum W_triangle)^4 |vac> has fidelity^2 = 90/91 with the
    independent 4-simplex vertex tensor;
  * pure-Wilson Krylov histories do not remove the missing 1/91 component;
  * scalar volume does not remove it either;
  * one exact tetrahedral shape operator does, at algebraic word depth 7;
  * in that shortest depth, at least two shape insertions are required.

The K5 complex is a finite algebraic laboratory.  This is not yet a Lorentzian
Hamiltonian-constraint or continuum calculation.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parents[1]
SCRIPTS=Path(__file__).resolve().parent
for p in (ROOT,SCRIPTS):
    if str(p) not in sys.path: sys.path.insert(0,str(p))

from su2_quantum_link_vector5_gate import build as build_vector5  # noqa:E402
from five_tetrahedron_vertex_gate import vertex_tensor  # noqa:E402

VERTICES=range(5)
EDGES=list(itertools.combinations(VERTICES,2))
EDGE_INDEX={e:i for i,e in enumerate(EDGES)}
TRIANGLES=list(itertools.combinations(VERTICES,3))

I2=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.array([[1,0],[0,-1]],complex)


def standard_link_basis(L,R):
    """Columns map standard |mL,mR>=(++,+-,-+,--) plus singlet to C^5."""
    H=L[2]+math.sqrt(2.0)*R[2]
    eig,vec=np.linalg.eigh(H)
    vmm=vec[:,0]
    Lp=L[0]+1j*L[1]; Rp=R[0]+1j*R[1]
    def unit(v): return v/np.linalg.norm(v)
    vpm=unit(Lp@vmm); vmp=unit(Rp@vmm); vpp=unit(Lp@vmp)
    active=np.column_stack([vpp,vpm,vmp,vmm])
    cas=sum(a@a for a in L)
    vals,V=np.linalg.eigh(cas)
    sing=V[:,np.argmin(np.abs(vals))]
    # remove any numerical active component and set one harmless phase
    sing=sing-active@(active.conj().T@sing); sing=unit(sing)
    nz=np.flatnonzero(np.abs(sing)>1e-12)
    if len(nz): sing*=np.exp(-1j*np.angle(sing[nz[0]]))
    S=np.column_stack([active,sing])
    return S


def local_intertwiners():
    z=np.array([1,0],complex); o=np.array([0,1],complex)
    sing=(np.kron(z,o)-np.kron(o,z))/math.sqrt(2)
    i0=np.kron(sing,sing).reshape(2,2,2,2)
    tp=np.kron(z,z); t0=(np.kron(z,o)+np.kron(o,z))/math.sqrt(2); tm=np.kron(o,o)
    i1=((np.kron(tp,tm)-np.kron(t0,t0)+np.kron(tm,tp))/math.sqrt(3)).reshape(2,2,2,2)
    return sing.reshape(2,2),i0,i1

SING,I0,I1=local_intertwiners()


def local_configs(k,label=0):
    if k==0: return [((),1.0+0j)]
    if k==2: arr=SING
    elif k==4: arr=I0 if label==0 else I1
    else: return []
    out=[]
    for bits in itertools.product((0,1),repeat=k):
        val=arr[bits]
        if abs(val)>1e-14: out.append((bits,val))
    return out


def enumerate_basis_meta():
    meta=[]
    for mask in range(1<<len(EDGES)):
        deg=[0]*5
        for ei,(u,v) in enumerate(EDGES):
            if (mask>>ei)&1: deg[u]+=1;deg[v]+=1
        if not all(d in (0,2,4) for d in deg): continue
        k4=[v for v,d in enumerate(deg) if d==4]
        for labs in itertools.product((0,1),repeat=len(k4)):
            meta.append((mask,tuple(deg),{v:l for v,l in zip(k4,labs)}))
    return meta


def build_sparse_state(meta):
    mask,deg,label_by=meta
    node_opts=[]
    for v in VERTICES:
        neigh=[w for w in VERTICES if w!=v and ((mask>>EDGE_INDEX[tuple(sorted((v,w)))])&1)]
        opts=[]
        for bits,amp in local_configs(len(neigh),label_by.get(v,0)):
            opts.append((dict(zip(neigh,bits)),amp))
        node_opts.append(opts)
    state={}
    for choices in itertools.product(*node_opts):
        amp=1+0j; endpoint=[]
        for dct,a in choices: endpoint.append(dct); amp*=a
        digits=[4]*10
        for ei,(u,v) in enumerate(EDGES):
            if (mask>>ei)&1:
                digits[ei]=2*endpoint[u][v]+endpoint[v][u]
        idx=0
        for d in digits: idx=5*idx+d
        state[idx]=state.get(idx,0)+amp
    n=math.sqrt(sum(abs(a)**2 for a in state.values()))
    return {i:a/n for i,a in state.items()}


def build_gauss_basis():
    meta=enumerate_basis_meta()
    states=[build_sparse_state(m) for m in meta]
    reverse={}
    for bi,st in enumerate(states):
        for idx,a in st.items(): reverse.setdefault(idx,[]).append((bi,np.conj(a)))
    return meta,states,reverse


def transformed_link_U():
    L,R,U=build_vector5(); S=standard_link_basis(L,R)
    Up=np.empty((2,2),dtype=object)
    for i in range(2):
        for j in range(2): Up[i,j]=S.conj().T@U[i,j]@S
    Ud=np.empty((2,2),dtype=object)
    for i in range(2):
        for j in range(2): Ud[i,j]=Up[j,i].conj().T
    return Up,Ud


def loop_local_operator(tri,Up,Ud):
    cyc=list(tri)+[tri[0]]; link_ids=[]; mats=[]
    for a,b in zip(cyc[:-1],cyc[1:]):
        link_ids.append(EDGE_INDEX[tuple(sorted((a,b)))])
        mats.append(Up if a<b else Ud)
    O=np.zeros((125,125),complex)
    for i,j,k in itertools.product(range(2),repeat=3):
        O+=np.kron(np.kron(mats[0][i,j],mats[1][j,k]),mats[2][k,i])
    transitions={}
    for inp in itertools.product(range(5),repeat=3):
        col=25*inp[0]+5*inp[1]+inp[2]; arr=[]
        for row in np.flatnonzero(np.abs(O[:,col])>1e-12):
            arr.append(((row//25,(row//5)%5,row%5),O[row,col]))
        transitions[inp]=arr
    return link_ids,transitions


def build_wilson_matrices(states,reverse):
    Up,Ud=transformed_link_U(); powers=[5**(9-e) for e in range(10)]; matrices=[]
    for tri in TRIANGLES:
        links,trans=loop_local_operator(tri,Up,Ud)
        W=np.zeros((140,140),complex)
        for col,st in enumerate(states):
            out={}
            for idx,a in st.items():
                inp=tuple((idx//powers[e])%5 for e in links)
                base=idx-sum(inp[t]*powers[e] for t,e in enumerate(links))
                for od,c in trans[inp]:
                    ni=base+sum(od[t]*powers[e] for t,e in enumerate(links))
                    out[ni]=out.get(ni,0)+c*a
            vec=np.zeros(140,complex)
            for idx,a in out.items():
                for row,ca in reverse.get(idx,[]): vec[row]+=ca*a
            W[:,col]=vec
        matrices.append(W)
    return matrices


def geometry_operators(meta):
    lookup={}
    for i,(mask,deg,labs) in enumerate(meta):
        k4=[v for v,d in enumerate(deg) if d==4]
        lookup[(mask,tuple(labs[v] for v in k4))]=i
    Ztot=np.zeros((140,140),complex); Xtot=np.zeros_like(Ztot); Ytot=np.zeros_like(Ztot); V=np.zeros_like(Ztot)
    for i,(mask,deg,labs) in enumerate(meta):
        k4=[v for v,d in enumerate(deg) if d==4]; V[i,i]=len(k4)
        base=tuple(labs[v] for v in k4)
        for p,v in enumerate(k4):
            lab=labs[v]; Ztot[i,i]+=1 if lab==0 else -1
            other=list(base); other[p]=1-lab; j=lookup[(mask,tuple(other))]
            Xtot[j,i]+=1; Ytot[j,i]+=1j if lab==0 else -1j
    return V,Xtot,Ytot,Ztot


def target_and_sectors(meta):
    vac=next(i for i,m in enumerate(meta) if m[0]==0)
    full=[]; bybits={}
    for i,(mask,deg,labs) in enumerate(meta):
        if mask==(1<<10)-1:
            bits=tuple(labs[v] for v in VERTICES); bybits[bits]=i; full.append(i)
    order=[bybits[b] for b in itertools.product((0,1),repeat=5)]
    V5=vertex_tensor().reshape(-1)
    target=np.zeros(140,complex); target[order]=V5; target/=np.linalg.norm(target)
    return vac,order,V5,target


def stable_span(vectors,target,tol=1e-9):
    Q=[]
    for x in vectors:
        x=x.astype(complex).copy()
        for _ in range(2):
            for q in Q: x-=q*np.vdot(q,x)
        n=np.linalg.norm(x)
        if n>tol: Q.append(x/n)
    err=max(0.0,float(1-sum(abs(np.vdot(q,target))**2 for q in Q)))
    return Q,err


def cyclic_depth(ops,start,target,maxdepth=10,tol=1e-9):
    Q=[start/np.linalg.norm(start)]; frontier=Q.copy(); rows=[]
    rows.append({"depth":0,"dimension":1,"target_defect":1.0})
    for depth in range(1,maxdepth+1):
        new=[]
        for q in frontier:
            for op in ops:
                x=op@q
                for _ in range(2):
                    for b in Q+new: x-=b*np.vdot(b,x)
                n=np.linalg.norm(x)
                if n>tol: new.append(x/n)
        Q.extend(new); frontier=new
        err=max(0.0,float(1-sum(abs(np.vdot(q,target))**2 for q in Q)))
        rows.append({"depth":depth,"dimension":len(Q),"target_defect":err})
        if not new: break
    return Q,rows


def word_vector(word,W,Z,start):
    v=start
    for char in word: v=(W if char=="W" else Z)@v
    return v


def shortest_projected_word_certificate(W,Z,start,full_order,V5):
    words={"":start.copy()}; front={"":start.copy()}
    for _ in range(7):
        nxt={}
        for s,v in front.items():
            nxt[s+"W"]=W@v; nxt[s+"Z"]=Z@v
        words.update(nxt); front=nxt
    target=V5/np.linalg.norm(V5)
    def projection_error(max_depth,max_z=None):
        cols=[]
        for s,v in words.items():
            if len(s)>max_depth: continue
            if max_z is not None and s.count("Z")>max_z: continue
            p=v[full_order]
            if np.linalg.norm(p)>1e-12: cols.append(p)
        if not cols: return 1.0,0
        A=np.column_stack(cols); U,s,_=np.linalg.svd(A,full_matrices=False); r=int(np.sum(s>1e-9))
        err=max(0.0,float(1-np.linalg.norm(U[:,:r].conj().T@target)**2))
        return err,r
    depth=[]
    for d in range(8):
        e,r=projection_error(d); depth.append({"depth":d,"rank":r,"defect":e})
    one_z=projection_error(7,1); two_z=projection_error(7,2)

    # Exhaustive cardinality certificate inside the depth<=7, <=2-Z projected set.
    labels=[]; cols=[]
    for s,v in words.items():
        if len(s)<=7 and s.count("Z")<=2:
            p=v[full_order]; n=np.linalg.norm(p)
            if n>1e-12: labels.append(s); cols.append(p/n)
    A=np.column_stack(cols); min_count=None; witness=None
    for k in range(1,8):
        for comb in itertools.combinations(range(len(labels)),k):
            B=A[:,comb]; c=np.linalg.lstsq(B,target,rcond=1e-11)[0]
            if np.linalg.norm(target-B@c)**2<1e-20:
                min_count=k; witness=[labels[i] for i in comb]; break
        if min_count is not None: break
    return {"depth_scan":depth,"depth7_max1_shape":{"defect":one_z[0],"rank":one_z[1]},"depth7_max2_shape":{"defect":two_z[0],"rank":two_z[1]},"minimal_number_projected_word_states":min_count,"one_exact_witness":witness}


def run():
    meta,states,reverse=build_gauss_basis(); Ws=build_wilson_matrices(states,reverse); W=sum(Ws)
    Vscalar,Xshape,Yshape,Zshape=geometry_operators(meta); vac,full_order,V5,target=target_and_sectors(meta)
    e0=np.zeros(140,complex); e0[vac]=1

    # Minimal W^4 bridge.
    psi=e0.copy()
    for _ in range(4): psi=W@psi
    full=psi[full_order]; vhat=V5/np.linalg.norm(V5); phat=full/np.linalg.norm(full)
    fidelity=float(abs(np.vdot(vhat,phat))**2)
    full_fraction=float(np.linalg.norm(full)**2/np.linalg.norm(psi)**2)
    support=np.abs(V5)>1e-12
    sf=full[support]/np.linalg.norm(full[support]); sv=V5[support]/np.linalg.norm(V5[support])
    support_fidelity=float(abs(np.vdot(sv,sf))**2)

    # Pure-Wilson full-sector Krylov defect.
    pure=[]; rows=[]; p=e0.copy()
    for n in range(1,31):
        p=W@p
        if n>=4 and n%2==0:
            q=np.zeros(140,complex); q[full_order]=p[full_order]; pure.append(q)
            _,err=stable_span(pure,target)
            rows.append({"power":n,"full_sector_span_rank":len(stable_span(pure,target)[0]),"target_defect":err})

    # Scalar volume vs tensorial shape.
    Qv,errv=cyclic_depth([W,Vscalar],e0,target,maxdepth=15)
    Qz,depthz=cyclic_depth([W,Zshape],e0,target,maxdepth=9)
    Qx,errx=cyclic_depth([W,Xshape],e0,target,maxdepth=15)
    Qy,erry=cyclic_depth([W,Yshape],e0,target,maxdepth=15)
    shortest=shortest_projected_word_certificate(W,Zshape,e0,full_order,V5)

    herm=max(float(np.linalg.norm(w-w.conj().T)) for w in Ws)
    occupancy={}
    for _,deg,_ in meta: occupancy[str(tuple(sorted(deg)))]=occupancy.get(str(tuple(sorted(deg))),0)+1
    all_active=sum(1 for m in meta if m[0]==(1<<10)-1)

    pass_condition=(len(meta)==140 and all_active==32 and abs(fidelity-90/91)<1e-10 and abs(support_fidelity-300/301)<1e-10 and abs(rows[-1]["target_defect"]-1/91)<1e-10 and abs(errv[-1]["target_defect"]-1/91)<1e-10 and depthz[7]["target_defect"]<1e-20 and shortest["minimal_number_projected_word_states"]==7)
    return {
        "status":"exact K5 finite quantum-geometry bridge",
        "passed":bool(pass_condition),
        "hilbert":{"raw_vector5_dimension":5**10,"Gauss_dimension":len(meta),"fully_active_dimension":all_active,"basis_max_sparse_support":max(len(s) for s in states),"occupancy_pattern_state_counts":occupancy},
        "wilson":{"triangles":[list(t) for t in TRIANGLES],"max_hermiticity_error":herm,"W4_full_geometry_fraction":full_fraction,"W4_to_4simplex_fidelity":fidelity,"exact_fidelity_target":"90/91","orthogonal_defect":1-fidelity,"support_fidelity":support_fidelity,"exact_support_target":"300/301"},
        "pure_Wilson_Krylov":rows,
        "scalar_volume_cyclic":{"dimension":len(Qv),"final_target_defect":errv[-1]["target_defect"]},
        "Z_shape_cyclic":{"dimension":len(Qz),"depth_scan":depthz},
        "X_shape_cyclic":{"dimension":len(Qx),"final_target_defect":errx[-1]["target_defect"]},
        "Y_shape_cyclic":{"dimension":len(Qy),"final_target_defect":erry[-1]["target_defect"]},
        "shortest_word_certificate":shortest,
        "interpretation":"Pure Wilson curvature reaches 90/91 of the independent 4-simplex vertex and never removes the missing 1/91 in the tested Krylov sector. Scalar volume does not help. A single exact tensorial tetrahedral shape observable closes the missing channel; the first exact projected completion occurs at word depth 7 and needs at least two shape insertions there, consistent with the need for tensorial flux geometry beyond Yang-Mills loop dynamics.",
        "scope_note":"This is an exact finite SU(2) K5 algebra test. It is not yet the real Lorentzian EEF Hamiltonian, HDA closure, a continuum phase, matter, or experiment."
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--output",type=Path); a=ap.parse_args(); out=run(); txt=json.dumps(out,indent=2); print(txt)
    if a.output: a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(txt+"\n",encoding="utf-8")
    return 0 if out["passed"] else 1

if __name__=="__main__": raise SystemExit(main())
