#!/usr/bin/env python3
"""Graph-independent PL Peter-Weyl prerequisite K_v=[V_v,E_v^sine].

This is the first amplitude-level Lorentzian bridge on an arbitrary closed
tetrahedral PL dual complex. It reuses the graph-independent physical-sine
Euclidean engine and the production zero-aware four-valent absolute-volume
convention used by the canonical Lorentzian stack.

The gate first reduces to the historical K5 sine-K implementation on the
boundary of a 4-simplex (up to the independently fixed tetrahedron orientation
sign), then evaluates a genuine 16-cell PL-S3 K column. No Lorentzian
coefficient, beta fit or GR target enters.
"""
from __future__ import annotations
import argparse,functools,json,math,sys
from collections import Counter
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_euclidean_sine_ordering_gate as SINE
import peter_weyl_lorentzian_K_block_gate as K5K
import peter_weyl_zeroaware_volume_migration_experiment as ZVM
from pl_dual_complex import DualComplex,boundary_4simplex,seed_16cell_boundary
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean

TOL=1e-10

def json_default(x):
    if isinstance(x,np.generic):return x.item()
    raise TypeError(f'Object of type {type(x).__name__} is not JSON serializable')

def add(dst,src,scale=1.0,tol=TOL):
    for k,a in src.items():
        z=dst.get(k,0j)+scale*a
        if abs(z)>tol:dst[k]=z
        elif k in dst:del dst[k]

def make_volume_ops(G):
    @functools.lru_cache(None)
    def local_volume_column(key,v):
        spins,Ks=key;ls=G.local_spins(spins,v);Tin=G.oriented_intertwiner(v,ls,Ks[v])
        Tout=G.apply_volume_tensor_oriented(Tin,ls,v);out={}
        for Ko in PW.allowed_k2_t(*ls):
            c=np.vdot(G.oriented_intertwiner(v,ls,Ko),Tout)
            if abs(c)>1e-12:
                out[(spins,tuple(Ko if u==v else Ks[u] for u in G.VERT))]=complex(c)
        return tuple(out.items())
    def apply_V(state,v):
        out={}
        for key,a0 in state.items():add(out,dict(local_volume_column(key,v)),a0)
        return {k:a for k,a in out.items() if abs(a)>TOL}
    return local_volume_column,apply_V

def apply_K(G,state,v,Jmax2,local_volume_column,apply_V):
    HE=G.H_sine_state(state,v,Jmax2,TOL)
    VH=apply_V(HE,v)
    Vin=apply_V(state,v)
    HV=G.H_sine_state(Vin,v,Jmax2,TOL)
    out={};add(out,VH,+1,1e-9);add(out,HV,-1,1e-9)
    return {k:a for k,a in out.items() if abs(a)>1e-9},HE

def k5_reference(state,v,Jmax2):
    H=SINE.safe_H_sine(state,v,Jmax2)
    VH=K5K.apply_V_local(H,v)
    Vin=K5K.apply_V_local(state,v)
    HV=SINE.safe_H_sine(Vin,v,Jmax2)
    out={};PW.add_dict(out,VH,+1);PW.add_dict(out,HV,-1)
    return PW.prune_state(out,1e-9)

def relerr(a,b,scale=1.0):
    keys=set(a)|set(b)
    num=math.sqrt(sum(abs(a.get(k,0j)-scale*b.get(k,0j))**2 for k in keys))
    den=math.sqrt(sum(abs(x)**2 for x in b.values()))
    return num/max(den,1e-30)

def run(node=0):
    ZVM.patch_and_clear()
    JMAX2=5
    KD=DualComplex(boundary_4simplex());KG=PLPeterWeylEuclidean(KD)
    initial=PW.basis_full_jhalf()[0];kv,KV=make_volume_ops(KG)
    knew,_=apply_K(KG,{initial:1+0j},node,JMAX2,kv,KV)
    kold=k5_reference({initial:1+0j},node,JMAX2)
    k5_error=relerr(knew,kold,KD.orientation[node])

    D=DualComplex(seed_16cell_boundary());G=PLPeterWeylEuclidean(D)
    seed=((1,)*len(G.EDGES),(0,)*D.n_tets);vcol,V=make_volume_ops(G)
    K,H=apply_K(G,{seed:1+0j},node,JMAX2,vcol,V)
    Knorm=G.norm(K);Hnorm=G.norm(H)
    max_spin=max((max(k[0]) for k in K),default=0)/2
    changed=Counter(sum(s!=1 for s in k[0]) for k in K)
    parity=Counter(sum(k[0])%2 for k in K)

    max_V_herm=0.0
    for key in {seed,*H.keys()}:
        col=dict(vcol(key,node))
        for ko,a in col.items():
            rev=dict(vcol(ko,node)).get(key,0j)
            max_V_herm=max(max_V_herm,abs(a-np.conjugate(rev)))

    edge_valences=sorted(len(x) for x in D.edge_incidence.values())
    all_even=bool(all(q%2==0 for q in edge_valences))
    expected_parity=sum(seed[0])%2 if all_even else None
    parity_ok=bool(expected_parity is not None and all((sum(k[0])%2)==expected_parity for k in K))

    checks={
      'production_zeroaware_volume_installed':bool(PW.volume123_matrix is ZVM.zeroaware_volume123_matrix),
      'K5_sine_reduction':bool(k5_error<5e-8),
      'sixteen_cell_E_nonzero':bool(len(H)>0 and Hnorm>1e-10),
      'sixteen_cell_K_nonzero':bool(len(K)>0 and Knorm>1e-10),
      'local_volume_hermitian_on_reached_blocks':bool(max_V_herm<1e-10),
      'even_valence_collective_regulator':all_even,
      'K_preserves_expected_PL_parity':parity_ok,
      'K_does_not_exceed_E_spin_wall':bool(max_spin<=1.0+1e-12),
    }
    return {
      'status':'production-consistent graph-independent PL amplitude prerequisite K=[V,H_E^sine]',
      'passed':bool(all(checks.values())),'checks':checks,'node':node,'Jmax':JMAX2/2,
      'volume_convention':'zero-aware sqrt(abs(Q)); tau=1000 eps dim(Q) max(1,||Q||)',
      'K5_regression':{'orientation_sign':int(KD.orientation[node]),'relative_error':float(k5_error),
                       'new_support':len(knew),'old_support':len(kold),
                       'new_norm':float(KG.norm(knew)),'old_norm':float(KG.norm(kold))},
      'sixteen_cell':{'nodes':D.n_tets,'dual_edges':len(G.EDGES),'edge_valences':[int(x) for x in edge_valences],
                      'E_support':len(H),'E_norm':float(Hnorm),'K_support':len(K),'K_norm':float(Knorm),
                      'max_spin_reached':float(max_spin),
                      'changed_edge_count_distribution':{str(k):int(v) for k,v in sorted(changed.items())},
                      'output_sum_doubled_spin_parity':{str(k):int(v) for k,v in sorted(parity.items())},
                      'max_local_volume_hermiticity_error':float(max_V_herm),
                      'seed_diagonal_K_amplitude':[float(K.get(seed,0j).real),float(K.get(seed,0j).imag)]},
      'definition':'K_v=[V_v,H_E,v^sine], H_E^sine=(T-T^dagger)/(2i)',
      'interpretation':'The graph-dependent Euclidean ingredient of the production Lorentzian stack is lifted from K5 to the independent 16-cell PL-S3 regulator with the same zero-aware volume convention and genuine complex Peter-Weyl amplitudes.',
      'scope_note':'K prerequisite only. It is not yet the Hermitian Lorentzian S amplitude, an effective collective W0, or a collective HDA result.'
    }

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--node',type=int,default=0);ap.add_argument('--output',type=Path)
    a=ap.parse_args();o=run(a.node);t=json.dumps(o,indent=2,default=json_default);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
