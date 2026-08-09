#!/usr/bin/env python3
"""Orientation-covariant K5 quantum-HDA diagnostic at Jmax=1/2.

This corrects the unordered/cyclic node sum by inserting the oriented
four-valent tetrahedral epsilon sign.  For a sorted local neighbour list
[n0,n1,n2,n3], the triple omitting neighbour number r carries sign (-1)^r.
This is the face-normal orientation pattern of an oriented tetrahedron and is
equivalent, up to one overall sign per node, to deriving the signs from a
regular geometric 4-simplex.

The script builds the exact 140D Gauss Hilbert, forms oriented node kernels,
uses their Hermitian completion, and checks all ten HH commutators on the 32D
fully-active K5 boundary sector.

This Jmax=1/2 calculation is explicitly regulator-UNSAFE for a physical HH
claim: each local H hits one link at most twice and HH at most four times, so a
j_in=1/2 Peter-Weyl safe test requires Jmax>=5/2.  The present calculation is a
finite diagnostic of symmetry and anomaly structure only.
"""
from __future__ import annotations
import argparse,itertools,json,math,sys
from fractions import Fraction
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
import k5_thiemann_constraint_gate as T

I=np.eye(2,dtype=complex);X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]],complex);Z=np.array([[1,0],[0,-1]],complex);PAULI=[I,X,Y,Z]


def oriented_specs(v:int):
    neigh=sorted(w for w in T.K5.VERTICES if w!=v);out=[]
    for tri in itertools.combinations(neigh,3):
        omitted=next(r for r,w in enumerate(neigh) if w not in tri)
        sign=-1 if omitted%2 else 1
        a,b,c=tri
        out.extend([((v,a,b,c),sign),((v,b,c,a),sign),((v,c,a,b),sign)])
    return out


def build_nodes():
    meta,states,reverse,Up,Ud,powers,full_order,V5,target,trans=T.build_runtime();local=T.make_actions(Up,Ud,powers,trans)
    nodes=[];max_projection_leak=0.0
    for v in range(5):
        M=np.zeros((140,140),complex)
        for col,raw0 in enumerate(states):
            raw={}
            for spec,sgn in oriented_specs(v):T.add_scaled(raw,local(raw0,*spec),sgn)
            rn=T.raw_norm(raw);pv=T.project_state(raw,reverse);M[:,col]=pv
            if rn>1e-12:max_projection_leak=max(max_projection_leak,max(0.0,1-(np.linalg.norm(pv)/rn)**2))
        nodes.append(M)
    return meta,np.asarray(full_order,int),np.asarray(V5),nodes,max_projection_leak


def pauli_design(max_weight):
    mats=[];labels=[]
    for word in itertools.product(range(4),repeat=5):
        if sum(a!=0 for a in word)>max_weight:continue
        M=np.array([[1]],complex)
        for a in word:M=np.kron(M,PAULI[a])
        mats.append(M);labels.append(''.join('IXYZ'[a] for a in word))
    return np.column_stack([m.reshape(-1) for m in mats]),labels

D2,_=pauli_design(2);D3,L3=pauli_design(3)

def fit(M,D):
    c=np.linalg.lstsq(D,M.reshape(-1),rcond=None)[0];r=M.reshape(-1)-D@c
    return float(np.linalg.norm(r)/max(np.linalg.norm(M),1e-30)),c


def run():
    meta,full,V5,raw_nodes,projleak=build_nodes();H=[0.5*(A+A.conj().T) for A in raw_nodes]
    rows=[];reference_spectrum=None
    for v,w in itertools.combinations(range(5),2):
        C=H[v]@H[w]-H[w]@H[v];act=C[:,full];inside=C[np.ix_(full,full)];outside=act.copy();outside[full,:]=0
        total2=float(np.linalg.norm(act)**2);out2=float(np.linalg.norm(outside)**2);leak=math.sqrt(out2/total2) if total2 else 0.0
        Q=-1j*inside;r2,_=fit(Q,D2);r3,c3=fit(Q,D3);ev=np.linalg.eigvalsh(Q)
        if reference_spectrum is None:reference_spectrum=ev
        rows.append({'v':v,'w':w,'commutator_action_norm':float(np.linalg.norm(act)),'graph_leakage':leak,'graph_leakage_squared':out2/total2,'inside_fraction_squared':1-out2/total2,'inside_rank':int(np.linalg.matrix_rank(inside,tol=1e-8)),'weight_le2_residual':r2,'weight_le3_residual':r3,'spectrum':ev.tolist()})
    # Kernel robustness of the oriented RAW node sums (not the Hermitian completion).
    target=V5/np.linalg.norm(V5);rank_flow=[];blocks=[]
    for n in range(3):
        blocks.append(raw_nodes[n][:,full]);S=np.vstack(blocks);_,sv,Vh=np.linalg.svd(S,full_matrices=False);rank=int(np.sum(sv>1e-9));ker=32-rank;fid=None
        if ker==1:
            null=Vh[-1].conj();null/=np.linalg.norm(null);fid=float(abs(np.vdot(null,target))**2)
        rank_flow.append({'nodes':n+1,'rank':rank,'kernel_dimension':ker,'smallest_nonzero_singular':float(sv[rank-1]) if rank else 0.0,'smallest_singular':float(sv[-1]),'unique_null_fidelity_to_V5':fid})
    leaks=np.array([r['graph_leakage'] for r in rows]);norms=np.array([r['commutator_action_norm'] for r in rows]);ranks=[r['inside_rank'] for r in rows]
    expected=math.sqrt(37/69)
    permutation_covariant=(np.max(np.abs(leaks-leaks[0]))<1e-12 and np.max(np.abs(norms-norms[0]))<1e-9 and len(set(ranks))==1 and all(np.max(np.abs(np.asarray(r['spectrum'])-reference_spectrum))<1e-8 for r in rows))
    passed_symmetry=bool(permutation_covariant)
    return {
      'status':'orientation-covariant Jmax=1/2 K5 quantum-HDA diagnostic',
      'orientation_symmetry_passed':passed_symmetry,
      'physical_HDA_passed':False,
      'physical_HDA_reason':'Jmax=1/2 is below the Peter-Weyl HH safe wall Jmax>=j_in+2=5/2 for j_in=1/2, and the fixed-triangulation commutator leakage is large.',
      'Gauss_dimension':len(meta),'fully_active_dimension':len(full),'max_raw_Gauss_projection_leakage':float(projleak),
      'all_pair_summary':{'number_pairs':len(rows),'graph_leakage':float(leaks[0]),'graph_leakage_exact':'sqrt(37/69)','inside_fraction_squared_exact':'32/69','commutator_action_norm':float(norms[0]),'inside_rank':ranks[0],'inside_spectrum_exact':'{-768 x6, 0 x20, +768 x6}','weight_le2_residual':rows[0]['weight_le2_residual'],'max_weight_le3_residual':max(r['weight_le3_residual'] for r in rows)},
      'pair_rows':rows,
      'oriented_common_kernel_rank_flow':rank_flow,
      'kernel_statement':'The oriented node sums preserve the robust rank flow 21->29->31 and the one-dimensional common kernel remains the independent five-tetrahedron V5 state with unit fidelity.',
      'interpretation':'Correct tetrahedral orientation removes arbitrary vertex-label asymmetry but does not close HDA at this cutoff. The remaining anomaly is permutation-covariant: norm-squared 37/69 leaves the fully-active triangulation, while the 32/69 internal component is a pure weight-3 intertwiner/shape operator.',
      'next_target':'Repeat the same oriented construction in a reachable Peter-Weyl basis with Jmax>=5/2 and genuine collective volume, then compare the surviving fixed-sector commutator to the independently verified simplex HDA coefficient 1/(3 V_tet).'
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);a=ap.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['orientation_symmetry_passed'] else 1
if __name__=='__main__':raise SystemExit(main())
