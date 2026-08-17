#!/usr/bin/env python3
"""Exact Peter-Weyl covariance under the order-8 K=0 pairing stabilizer.

For the 16-cell dual hypercube, coordinate permutations map old local slot r to
new slot h(r) and preserve every canonical dual-edge orientation (bit 0->1).
Restrict to the order-8 subgroup H preserving the unordered coupling partition
{{0,1},{2,3}}.  For any Gauss four-valent Peter-Weyl basis state this subgroup
preserves the intermediate K label; only the exact CG recoupling phase changes.

The gate constructs U_h directly from oriented intertwiner overlaps, verifies
that the 16-node all-j=1/2 K=0 seed is invariant, and then verifies the actual
sparse amplitude equation

    U_h E_0|Omega> = sgn(h) E_0|Omega>

for all h in H.  Passing this gate is the amplitude-level prerequisite for the
24->3 Lorentzian ordered-term orbit reduction.  It does not itself assume that
the corrected K-K-V word has been validated on held-out V2 terms.
"""
from __future__ import annotations
import argparse,itertools,json,math,sys
from functools import lru_cache
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
import peter_weyl_zeroaware_volume_migration_experiment as ZVM
from pl_dual_complex import DualComplex,seed_16cell_boundary
from pl_peter_weyl_euclidean import PLPeterWeylEuclidean

TOL=1e-9

def parity(p):return -1 if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2 else 1

def pairing_stabilizer():
    pairs={frozenset((0,1)),frozenset((2,3))}
    return tuple(p for p in itertools.permutations(range(4)) if {frozenset((p[0],p[1])),frozenset((p[2],p[3]))}==pairs)

def map_node(v,h):
    bits=[(v>>(3-i))&1 for i in range(4)];nb=[0]*4
    for i in range(4):nb[h[i]]=bits[i]
    out=0
    for i,b in enumerate(nb):out|=b<<(3-i)
    return out

def inverse_perm(h):
    q=[0]*4
    for i,x in enumerate(h):q[x]=i
    return tuple(q)

def relerr(a,b):
    keys=set(a)|set(b);num=math.sqrt(sum(abs(a.get(k,0j)-b.get(k,0j))**2 for k in keys));den=math.sqrt(sum(abs(z)**2 for z in b.values()))
    return num/max(den,1e-300)

def setup():
    ZVM.patch_and_clear();D=DualComplex(seed_16cell_boundary());G=PLPeterWeylEuclidean(D);edges=list(G.EDGES);ei={e:i for i,e in enumerate(edges)}
    return D,G,edges,ei

def edge_map_metadata(edges,h):
    reversals=0;m=[]
    for i,(a,b) in enumerate(edges):
        aa,bb=map_node(a,h),map_node(b,h);reversals+=int((a<b)!=(aa<bb));m.append(tuple(sorted((aa,bb))))
    return reversals,m

def mapped_spins(spins,edges,ei,h):
    ns=[0]*len(edges)
    for old,(a,b) in enumerate(edges):
        e=tuple(sorted((map_node(a,h),map_node(b,h))));ns[ei[e]]=spins[old]
    return tuple(ns)

def run():
    D,G,edges,ei=setup();H=pairing_stabilizer();seed=((1,)*len(edges),(0,)*16)
    invs={h:inverse_perm(h) for h in H}
    local_cache={};max_local_leak=0.0;max_phase_mod=0.0
    def local_phase(v,spins,K,h,newspins):
        nonlocal max_local_leak,max_phase_mod
        key=(v,spins,K,h,newspins)
        if key in local_cache:return local_cache[key]
        t=map_node(v,h);oldls=G.local_spins(spins,v);newls=G.local_spins(newspins,t)
        expected=[None]*4
        for r in range(4):expected[h[r]]=oldls[r]
        if tuple(expected)!=tuple(newls):raise RuntimeError(('local spin permutation mismatch',v,h,oldls,newls,expected))
        T=G.oriented_intertwiner(v,oldls,K);Tp=np.transpose(T,axes=invs[h]);U=G.oriented_intertwiner(t,newls,K)
        z=np.vdot(U,Tp);leak=float(np.linalg.norm(Tp-z*U));max_local_leak=max(max_local_leak,leak);max_phase_mod=max(max_phase_mod,float(abs(abs(z)-1)))
        if leak>1e-9 or abs(abs(z)-1)>1e-9:raise RuntimeError(('H failed to preserve K line',v,h,oldls,K,z,leak))
        local_cache[key]=z;return z
    def map_key_amp(key,h):
        spins,Ks=key;ns=mapped_spins(spins,edges,ei,h);nk=[None]*16;phase=1+0j
        for v,K in enumerate(Ks):
            t=map_node(v,h);nk[t]=K;phase*=local_phase(v,spins,K,h,ns)
        if any(x is None for x in nk):raise RuntimeError('node permutation incomplete')
        return (ns,tuple(nk)),phase
    def map_state(st,h):
        out={}
        for key,a in st.items():
            k,z=map_key_amp(key,h);out[k]=out.get(k,0j)+a*z
        return {k:a for k,a in out.items() if abs(a)>1e-11}
    # Structural graph checks.
    struct=[]
    for h in H:
        rev,emap=edge_map_metadata(edges,h)
        neigh=bool(all(map_node(D.neighbor[(v,r)],h)==D.neighbor[(map_node(v,h),h[r])] for v in range(16) for r in range(4)))
        struct.append({'permutation':list(h),'parity':parity(h),'neighbor_slot_covariance':neigh,'dual_edge_orientation_reversals':int(rev),'edge_map_bijective':bool(len(set(emap))==len(edges))})
    # Seed must be exactly invariant under all H after 16 local phases multiply.
    seed_rows=[];seed_ok=True
    for h in H:
        sm=map_state({seed:1+0j},h);z=sm.get(seed,0j);err=math.sqrt(sum(abs(a-(1 if k==seed else 0))**2 for k,a in sm.items())+ (0 if seed in sm else 1))
        seed_ok=bool(seed_ok and set(sm)=={seed} and abs(z-1)<TOL)
        seed_rows.append({'permutation':list(h),'mapped_seed_amplitude':[float(z.real),float(z.imag)],'seed_error':float(err)})
    # Genuine exact E amplitude at source 0.
    E=G.H_sine_basis(seed,0,5,TOL);en=float(G.norm(E));rows=[];maxerr=0.0;support=True;normdef=0.0
    for h in H:
        mapped=map_state(E,h);target={k:parity(h)*a for k,a in E.items()};err=float(relerr(mapped,target));maxerr=max(maxerr,err);support=bool(support and set(mapped)==set(target));normdef=max(normdef,float(abs(G.norm(mapped)-en)))
        rows.append({'permutation':list(h),'parity':parity(h),'support_identical':bool(set(mapped)==set(target)),'relative_E_covariance_error':err,'mapped_norm':float(G.norm(mapped))})
    checks={
      'H_order8':bool(len(H)==8),
      'graph_neighbor_slot_covariance':bool(all(x['neighbor_slot_covariance'] for x in struct)),
      'coordinate_permutations_preserve_edge_orientation':bool(all(x['dual_edge_orientation_reversals']==0 for x in struct)),
      'edge_maps_bijective':bool(all(x['edge_map_bijective'] for x in struct)),
      'global_K0_seed_invariant':bool(seed_ok),
      'local_K_line_recoupling_exact':bool(max_local_leak<TOL and max_phase_mod<TOL),
      'E_sparse_support_covariant':bool(support),
      'E_pseudoscalar_amplitude_covariance':bool(maxerr<TOL),
      'E_norm_preserved':bool(normdef<TOL),
    }
    return {'status':'exact 16-cell Peter-Weyl covariance under K0 pairing stabilizer H','passed':bool(all(checks.values())),'science_status':'AMPLITUDE_ORBIT_REDUCTION_PREREQUISITE',
      'group':'H=(S2 x S2) semidirect S2 preserving pairing (01)(23)','order':int(len(H)),'elements':[list(h) for h in H],
      'checks':checks,'structural_rows':struct,'seed_rows':seed_rows,'E_source0_support':int(len(E)),'E_source0_norm':en,'E_covariance_rows':rows,
      'max_local_intertwiner_line_leakage':float(max_local_leak),'max_local_phase_modulus_defect':float(max_phase_mod),'max_E_relative_covariance_error':float(maxerr),'max_E_norm_defect':float(normdef),
      'consequence_if_passed':'The exact sparse state action U_h is available for the same order-8 subgroup that partitions the 24 ordered Lorentzian slots into three orbits. Corrected Lorentzian production may use 3 representatives per forward/adjoint mode only after direct held-out V2 ordered-term covariance checks pass.',
      'hard_guard':'This E gate alone does not certify the K-K-V V2 ordered word. At least one independently computed non-representative V2 term in every orbit and mode must agree with U_h transport before replacing the 48-term collector input.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
