#!/usr/bin/env python3
"""Two upstream geometrogenesis controls.

1. Exact four-link SO(5)-vector plaquette: Gauss projection leaves a two-state
   space |all-singlet> and |all-geometric>; the Wilson loop flips them.
2. Combinatorial no-go for the one-rishon SO(5)-spinor representation on the
   minimal closed four-valent K5 dual graph: average endpoint occupancy is 2,
   so an everywhere k=4 volumetric phase is impossible.
"""
from __future__ import annotations
import argparse,itertools,json,math,collections
from pathlib import Path
import numpy as np
from su2_quantum_link_vector5_gate import build


def emb(op,l,n=4,d=5):
    out=np.array([[1]],complex);I=np.eye(d)
    for m in range(n):out=np.kron(out,op if m==l else I)
    return out

def vector_plaquette():
    L,R,U=build();D=5**4
    LE=[[emb(L[a],l) for a in range(3)] for l in range(4)];RE=[[emb(R[a],l) for a in range(3)] for l in range(4)]
    UE=[]
    for l in range(4):
        um=np.empty((2,2),dtype=object)
        for i in range(2):
            for j in range(2):um[i,j]=emb(U[i,j],l)
        UE.append(um)
    G2=np.zeros((D,D),complex)
    for v in range(4):
        prev=(v-1)%4;nxt=v
        for a in range(3):
            g=RE[prev][a]+LE[nxt][a];G2+=g@g
    ev,B=np.linalg.eigh(G2);mask=np.abs(ev)<1e-9;P=B[:,mask]
    W=np.zeros((D,D),complex)
    for i,j,k,l in itertools.product(range(2),repeat=4):W+=UE[0][i,j]@UE[1][j,k]@UE[2][k,l]@UE[3][l,i]
    Wp=P.conj().T@W@P
    CL=sum(x@x for x in L);Pg=(4/3)*CL
    Ng=np.zeros((D,D),complex);Pall=np.eye(D,dtype=complex);Psall=np.eye(D,dtype=complex);Ps=np.eye(5)-Pg
    for l in range(4):
        p=emb(Pg,l);s=emb(Ps,l);Ng+=p;Pall=Pall@p;Psall=Psall@s
    return {"full_dimension":D,"Gauss_dimension":int(mask.sum()),"Gauss_gap":float(np.min(ev[~mask])),"Wilson_gauge_error":float(np.linalg.norm(G2@W-W@G2)),"Wilson_physical_matrix":np.real_if_close(Wp).tolist(),"Wilson_physical_spectrum":np.linalg.eigvalsh(Wp).tolist(),"N_geometric_spectrum":np.linalg.eigvalsh(P.conj().T@Ng@P).tolist(),"all_geometric_projector_spectrum":np.linalg.eigvalsh(P.conj().T@Pall@P).tolist(),"all_singlet_projector_spectrum":np.linalg.eigvalsh(P.conj().T@Psall@P).tolist()}

def spinor_k5_count():
    vertices=range(5);edges=list(itertools.combinations(vertices,2));mult={0:1,2:1,4:2};counts=collections.Counter();weighted=collections.Counter();dim=0;valid=0
    for bits in itertools.product((0,1),repeat=len(edges)):
        k=[0]*5
        for bit,(u,v) in zip(bits,edges):k[v if bit else u]+=1
        if all(x%2==0 for x in k):
            valid+=1;p=tuple(sorted(k));m=math.prod(mult[x] for x in k);counts[p]+=1;weighted[p]+=m;dim+=m
    return {"vertices":5,"links":10,"raw_link_hilbert_dimension":4**10,"valid_endpoint_orientations":valid,"Gauss_dimension_with_intertwiner_multiplicity":dim,"compression_raw_over_Gauss":4**10/dim,"occupancy_pattern_counts":{str(k):v for k,v in counts.items()},"weighted_state_counts":{str(k):v for k,v in weighted.items()},"all_nodes_k4_possible":False,"counting_reason":"one rishon/link gives total endpoint occupancy E=2V on any closed 4-valent graph, hence average k=2; all nodes k=4 would require two rishons/link"}

def run():
    p=vector_plaquette();n=spinor_k5_count();passed=p["Gauss_dimension"]==2 and np.allclose(p["Wilson_physical_spectrum"],[-16,16]) and n["Gauss_dimension_with_intertwiner_multiplicity"]==104
    return {"status":"finite geometrogenesis carrier tests","passed":bool(passed),"vector5_plaquette":p,"spinor4_K5_no_go":n,"conclusion":"The SO(5) vector link supports exact closed-loop creation between singlet vacuum and active geometric links, while the one-rishon spinor link cannot support an everywhere-volumetric closed four-valent geometry."}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--output",type=Path);a=ap.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+"\n",encoding="utf-8")
    return 0 if o["passed"] else 1
if __name__=="__main__":raise SystemExit(main())
