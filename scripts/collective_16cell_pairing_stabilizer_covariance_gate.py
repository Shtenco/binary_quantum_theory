#!/usr/bin/env python3
"""Exact Peter-Weyl transport representation under the order-8 K=0 pairing stabilizer.

The previous version over-constrained the summed Euclidean column by demanding a
one-dimensional pseudoscalar character under every element of the pairing
stabilizer.  The first exact run falsified that extra assumption while preserving
support and norm.  Orbit reduction only needs the Peter-Weyl transport U_h to be
an exact unitary group action; covariance of the corrected Lorentzian ordered
word is then tested directly on held-out production terms before reconstruction.

This gate therefore checks the representation itself:

    U_g U_h = U_{g o h},
    U_{h^{-1}} U_h = I,

on the genuine 82-state E_0|Omega> orbit, together with seed invariance, exact
local K-line recoupling, graph covariance, support and norm preservation.  The
old pseudoscalar comparison is retained only as a diagnostic and is not a hard
criterion.
"""
from __future__ import annotations
import argparse,itertools,json,math,sys,traceback
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

def compose(g,h):
    """Permutation for applying h first and then g."""
    return tuple(g[h[i]] for i in range(4))

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
def inner(a,b):return sum(np.conj(z)*b.get(k,0j) for k,z in a.items())
def state_norm(a):return math.sqrt(sum(abs(z)**2 for z in a.values()))
def residual_to_scalar(x,ref,z):
    keys=set(x)|set(ref)
    return math.sqrt(sum(abs(x.get(k,0j)-z*ref.get(k,0j))**2 for k in keys))/max(state_norm(ref),1e-300)

def setup():
    ZVM.patch_and_clear();D=DualComplex(seed_16cell_boundary());G=PLPeterWeylEuclidean(D);edges=list(G.EDGES);ei={e:i for i,e in enumerate(edges)}
    return D,G,edges,ei

def edge_map_metadata(edges,h):
    reversals=0;m=[]
    for a,b in edges:
        aa,bb=map_node(a,h),map_node(b,h);reversals+=int((a<b)!=(aa<bb));m.append(tuple(sorted((aa,bb))))
    return reversals,m

def mapped_spins(spins,edges,ei,h):
    ns=[0]*len(edges)
    for old,(a,b) in enumerate(edges):
        e=tuple(sorted((map_node(a,h),map_node(b,h))));ns[ei[e]]=spins[old]
    return tuple(ns)

def run():
    D,G,edges,ei=setup();H=pairing_stabilizer();Hset=set(H);seed=((1,)*len(edges),(0,)*16)
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
        if leak>TOL or abs(abs(z)-1)>TOL:raise RuntimeError(('H failed to preserve K line',v,h,oldls,K,z,leak))
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

    struct=[]
    for h in H:
        rev,emap=edge_map_metadata(edges,h)
        neigh=bool(all(map_node(D.neighbor[(v,r)],h)==D.neighbor[(map_node(v,h),h[r])] for v in range(16) for r in range(4)))
        struct.append({'permutation':list(h),'parity':parity(h),'neighbor_slot_covariance':neigh,'dual_edge_orientation_reversals':int(rev),'edge_map_bijective':bool(len(set(emap))==len(edges))})

    seed_rows=[];seed_ok=True
    for h in H:
        sm=map_state({seed:1+0j},h);z=sm.get(seed,0j);err=math.sqrt(sum(abs(a-(1 if k==seed else 0))**2 for k,a in sm.items())+(0 if seed in sm else 1))
        seed_ok=bool(seed_ok and set(sm)=={seed} and abs(z-1)<TOL)
        seed_rows.append({'permutation':list(h),'mapped_seed_amplitude':[float(z.real),float(z.imag)],'seed_error':float(err)})

    E=G.H_sine_basis(seed,0,5,TOL);en=float(G.norm(E));en2=en*en
    orbit={};rows=[];support=True;normdef=0.0;max_parity_err=0.0
    for h in H:
        mapped=map_state(E,h);orbit[h]=mapped
        target={k:parity(h)*a for k,a in E.items()};perr=float(relerr(mapped,target));max_parity_err=max(max_parity_err,perr)
        support=bool(support and set(mapped)==set(E));normdef=max(normdef,float(abs(G.norm(mapped)-en)))
        z=inner(E,mapped)/en2
        rows.append({'permutation':list(h),'parity':parity(h),'support_identical':bool(set(mapped)==set(E)),
                     'relative_error_to_old_pseudoscalar_target':perr,
                     'normalized_overlap_with_E':[float(z.real),float(z.imag)],
                     'best_scalar_residual':float(residual_to_scalar(mapped,E,z)),
                     'mapped_norm':float(G.norm(mapped))})

    # Exact representation law on the genuine reached orbit.
    max_group_err=0.0;group_rows=[];composition_closed=True;node_comp_ok=True
    for g in H:
        for h in H:
            gh=compose(g,h);composition_closed=bool(composition_closed and gh in H)
            node_comp_ok=bool(node_comp_ok and all(map_node(map_node(v,h),g)==map_node(v,gh) for v in range(16)))
            lhs=map_state(orbit[h],g);rhs=orbit[gh];err=float(relerr(lhs,rhs));max_group_err=max(max_group_err,err)
            group_rows.append({'g':list(g),'h':list(h),'g_after_h':list(gh),'relative_error':err})
    max_inverse_err=0.0;inverse_rows=[]
    for h in H:
        inv=inverse_perm(h);back=map_state(orbit[h],inv);err=float(relerr(back,E));max_inverse_err=max(max_inverse_err,err)
        inverse_rows.append({'h':list(h),'inverse':list(inv),'roundtrip_relative_error':err})

    # Orbit Gram: diagnose whether E spans a 1D character or a higher H-irrep.
    Gm=np.zeros((len(H),len(H)),complex)
    for i,h in enumerate(H):
        for j,k in enumerate(H):Gm[i,j]=inner(orbit[h],orbit[k])/en2
    Gm=(Gm+Gm.conj().T)/2
    eig=np.linalg.eigvalsh(Gm);mx=max(float(eig[-1]),1e-300);rank=int(np.sum(eig>1e-10*mx))
    gram_rows=[[[float(Gm[i,j].real),float(Gm[i,j].imag)] for j in range(len(H))] for i in range(len(H))]

    checks={
      'H_order8':bool(len(H)==8),'H_closed_under_composition':bool(composition_closed),
      'graph_neighbor_slot_covariance':bool(all(x['neighbor_slot_covariance'] for x in struct)),
      'coordinate_permutations_preserve_edge_orientation':bool(all(x['dual_edge_orientation_reversals']==0 for x in struct)),
      'edge_maps_bijective':bool(all(x['edge_map_bijective'] for x in struct)),
      'node_permutation_group_law':bool(node_comp_ok),
      'global_K0_seed_invariant':bool(seed_ok),
      'local_K_line_recoupling_exact':bool(max_local_leak<TOL and max_phase_mod<TOL),
      'E_sparse_support_transport_exact':bool(support),
      'E_norm_preserved':bool(normdef<TOL),
      'U_group_law_on_E_orbit':bool(max_group_err<TOL),
      'U_inverse_roundtrip_on_E_orbit':bool(max_inverse_err<TOL),
      'E_orbit_Gram_PSD':bool(float(eig[0])>-1e-9),
    }
    return {
      'status':'exact 16-cell Peter-Weyl transport representation under K0 pairing stabilizer H',
      'passed':bool(all(checks.values())),'science_status':'AMPLITUDE_TRANSPORT_REPRESENTATION_PREREQUISITE',
      'group':'H=(S2 x S2) semidirect S2 preserving pairing (01)(23)','order':int(len(H)),'elements':[list(h) for h in H],
      'checks':checks,'structural_rows':struct,'seed_rows':seed_rows,
      'E_source0_support':int(len(E)),'E_source0_norm':en,'E_transport_rows':rows,
      'E_orbit_gram':gram_rows,'E_orbit_gram_eigenvalues':[float(x) for x in eig],'E_orbit_rank':rank,
      'max_local_intertwiner_line_leakage':float(max_local_leak),'max_local_phase_modulus_defect':float(max_phase_mod),
      'max_E_norm_defect':float(normdef),'max_U_group_law_error':float(max_group_err),'max_U_inverse_roundtrip_error':float(max_inverse_err),
      'old_pseudoscalar_diagnostic':{
        'hard_requirement':False,'passed':bool(max_parity_err<TOL),'max_relative_error':float(max_parity_err),
        'interpretation':'The summed frozen cyclic-frame E column need not furnish a one-dimensional sign character. This diagnostic cannot authorize or veto Lorentzian orbit reduction.'},
      'consequence_if_passed':'U_h is an exact sparse unitary representation on the reached Peter-Weyl orbit. Lorentzian orbit reconstruction is still forbidden until the corrected V2 ordered word itself passes direct held-out covariance checks.',
      'hard_guard':'Do not infer K-K-V covariance from the old E pseudoscalar diagnostic. Production orbit reduction requires direct V2 representative/held-out term agreement under this U_h transport.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args()
    try:o=run();code=0 if o['passed'] else 1
    except Exception as exc:o={'status':'pairing-stabilizer Peter-Weyl transport exception','passed':False,'science_status':'INFRASTRUCTURE_DIAGNOSTIC','error_type':type(exc).__name__,'error':str(exc),'traceback':traceback.format_exc()};code=1
    t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return code
if __name__=='__main__':raise SystemExit(main())
