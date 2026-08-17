#!/usr/bin/env python3
"""Exact full-E depth-two worker for one coarse metric edge of an L1 block.

For one unordered parent edge e define the normalized coarse source

    |u_e> = (1/2) sum_{4 chambers c -> e} H_c |Omega>.

Then apply the full parent-block Euclidean Hamiltonian

    H_B = sum_{w in the 24 fine chambers} H_w,
    |v_e> = H_B |u_e>.

Edges 01, 02 and 23 are direct representatives of same/adjacent/opposite S4
orbits.  H is the production physical-sine Peter-Weyl operator on the complete
384-node / 768-link L1 habitat; no q4 projection is used in this depth-two run.
"""
from __future__ import annotations
import argparse,itertools,json,math,time,traceback
from collections import Counter
from pathlib import Path
import numpy as np
import peter_weyl_zeroaware_volume_migration_experiment as ZVM
from pl_dual_complex import DualComplex,seed_16cell_boundary
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean
from collective_barycentric_E_boundary_support_gate import barycentric_with_parent

JMAX2=5
TOL=1e-10
PERMS=list(itertools.permutations(range(4)))
EDGES=list(itertools.combinations(range(4),2))
REPRESENTATIVES=(0,1,5)

def add(dst,src,scale=1.0):
    for k,a in src.items():
        z=dst.get(k,0j)+scale*a
        if abs(z)>TOL: dst[k]=z
        elif k in dst: del dst[k]

def norm(s): return math.sqrt(sum(abs(a)**2 for a in s.values()))
def maxspin(s): return max((max(k[0]) for k in s),default=0)/2.0

def save(path,state,nedges,nverts):
    rows=sorted(state.items(),key=lambda kv:repr(kv[0])); path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    if rows:
        spins=np.asarray([k[0] for k,_ in rows],np.int16); Ks=np.asarray([k[1] for k,_ in rows],np.int16); amp=np.asarray([a for _,a in rows],np.complex128)
    else:
        spins=np.zeros((0,nedges),np.int16); Ks=np.zeros((0,nverts),np.int16); amp=np.zeros((0,),np.complex128)
    np.savez_compressed(path,spins=spins,Ks=Ks,amp=amp)

def diag(state,seed):
    changed=Counter(sum(a!=b for a,b in zip(key[0],seed[0])) for key in state)
    parity=Counter(sum(key[0])%2 for key in state)
    return {'support':len(state),'norm':norm(state),'max_spin':maxspin(state),
            'changed_edge_count_distribution':{str(k):v for k,v in sorted(changed.items())},
            'sum_doubled_spin_parity_distribution':{str(k):v for k,v in sorted(parity.items())}}

def run(edge_index,parent_id=0):
    if edge_index not in REPRESENTATIVES: raise ValueError(edge_index)
    ZVM.patch_and_clear(); coarse=seed_16cell_boundary(); fine,parent=barycentric_with_parent(coarse); D=DualComplex(fine); G=PLPeterWeylEuclidean(D)
    inside=sorted(v for v,p in enumerate(parent) if p==parent_id)
    if len(inside)!=24: raise RuntimeError(('parent block size',len(inside)))
    edge=EDGES[edge_index]
    local=[i for i,p in enumerate(PERMS) if tuple(sorted(p[:2]))==edge]
    if len(local)!=4: raise RuntimeError(('chambers per edge',edge,local))
    seed=((1,)*len(G.EDGES),(0,)*D.n_tets)

    t0=time.time(); u={}; first=[]
    for li in local:
        node=inside[li]; col=G.H_sine_basis(seed,node,JMAX2,TOL); first.append({'local_index':li,'global_node':node,'support':len(col),'norm':norm(col)}); add(u,col,0.5)
    t_first=time.time()-t0

    t1=time.time(); v={}; second_support=[]
    for node in inside:
        col=G.H_sine_state(u,node,JMAX2,TOL); second_support.append(len(col)); add(v,col,1.0)
    t_second=time.time()-t1

    finite=all(np.isfinite([z.real,z.imag]).all() for st in (u,v) for z in st.values())
    seedpar=sum(seed[0])%2; wrong=sum(1 for key in v if sum(key[0])%2!=seedpar)
    checks={'L1_nodes_384':D.n_tets==384,'L1_dual_links_768':len(G.EDGES)==768,'parent_has_24_fine_nodes':len(inside)==24,
            'edge_has_four_barycentric_chambers':len(local)==4,'first_edge_state_nonzero':len(u)>0 and norm(u)>TOL,
            'depth2_block_state_nonzero':len(v)>0 and norm(v)>TOL,'finite_amplitudes':finite,
            'depth2_spin_wall_j_le_5_over_2':maxspin(v)<=2.5+1e-12,'depth2_seed_parity_restored':wrong==0}
    return u,v,{'status':'exact L1 full-E coarse-edge depth-two block column','passed':bool(all(checks.values())),'science_status':'L1_METRIC_EDGE_DEPTH2_PILOT',
        'parent_coarse_tetra':parent_id,'edge_index':edge_index,'edge':list(edge),'local_chamber_indices':local,'global_chamber_nodes':[inside[i] for i in local],
        'Jmax':JMAX2/2,'first_columns':first,'first_edge_state':diag(u,seed),'depth2_block_state':diag(v,seed),'second_action_support_by_block_node':second_support,
        'first_seconds':t_first,'second_seconds':t_second,'second_wrong_seed_parity_outputs':wrong,'checks':checks,
        'definition':'u_e=(1/2) sum_{4 chambers->e} H_c|Omega>; v_e=(sum_{w in parent block} H_w)u_e',
        'scope_note':'Full Euclidean E on the closed L1 habitat. No Lorentzian term, energy denominator, TT projector or external datum.'}

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--edge-index',type=int,choices=REPRESENTATIVES,required=True); p.add_argument('--out-dir',type=Path,required=True); a=p.parse_args(); a.out_dir.mkdir(parents=True,exist_ok=True)
    try: u,v,o=run(a.edge_index); code=0 if o['passed'] else 1
    except Exception as exc: u=v={}; o={'status':'worker exception','passed':False,'science_status':'INFRASTRUCTURE_DIAGNOSTIC','edge_index':a.edge_index,'error_type':type(exc).__name__,'error':str(exc),'traceback':traceback.format_exc()}; code=1
    fine,_=barycentric_with_parent(seed_16cell_boundary()); D=DualComplex(fine); save(a.out_dir/f'u_{a.edge_index}.npz',u,len(D.dual_edges()),D.n_tets); save(a.out_dir/f'v_{a.edge_index}.npz',v,len(D.dual_edges()),D.n_tets)
    (a.out_dir/f'edge_{a.edge_index}.json').write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8'); print(json.dumps(o,indent=2)); return code
if __name__=='__main__': raise SystemExit(main())
