#!/usr/bin/env python3
"""Direct L1 coarse face-flux metric response of the strict q=4 BCQG carrier.

This finite gate contracts the canonical 24-chamber barycentric block, uses the
static contracted boundary state as background, and inserts coarse total-face
flux Gram operators Z_fg=X_f.X_g on the 24 open boundary legs.  The six tangent
channels are the background-orthogonal strict q=4 Euclidean image, with the
physical real state velocity fixed as -i E|Omega> (Schrodinger complex
structure). S4 reduces the response to same/adjacent/opposite classes.
"""
from __future__ import annotations
import argparse,itertools,json,math,sys,time
from collections import defaultdict
from pathlib import Path
import numpy as np
import opt_einsum as oe
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_zeroaware_volume_migration_experiment as ZVM
from collective_barycentric_E_boundary_support_gate import barycentric_with_parent
from pl_dual_complex import DualComplex,seed_16cell_boundary
from pl_peter_weyl_euclidean_local import LocalPLPeterWeylEuclidean
TOL=1e-10;JMAX2=3
EDGES=list(itertools.combinations(range(4),2))
SQ2=math.sqrt(2)
J_EDGE=np.array([[0,.5,.5,0,0,SQ2/2],[.5,0,.5,0,SQ2/2,0],[.5,.5,0,SQ2/2,0,0],[.5,.5,0,-SQ2/2,0,0],[.5,0,.5,0,-SQ2/2,0],[0,.5,.5,0,0,-SQ2/2]],float)
J_FLUX=np.array([[-2/3,0,0,0,0,SQ2/3],[0,-2/3,0,0,SQ2/3,0],[0,0,-2/3,SQ2/3,0,0],[0,0,-2/3,-SQ2/3,0,0],[0,-2/3,0,0,-SQ2/3,0],[-2/3,0,0,0,0,-SQ2/3]],float)

def parity(p):
    return -1 if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2 else 1

def add(dst,src,scale):
    for k,a in src.items():
        z=dst.get(k,0j)+scale*a
        if abs(z)>TOL:dst[k]=z
        elif k in dst:del dst[k]

def setup():
    ZVM.patch_and_clear();fine,parent=barycentric_with_parent(seed_16cell_boundary());D=DualComplex(fine);G=LocalPLPeterWeylEuclidean(D)
    inside=set(v for v,p in enumerate(parent) if p==0);nodes=sorted(inside);perms=tuple(itertools.permutations(range(4)))
    internal=sorted(e for e in G.EDGES if e[0] in inside and e[1] in inside);IE={e:i for i,e in enumerate(internal)}
    seed=((1,)*len(G.EDGES),(0,)*D.n_tets);edge_li={}
    for i,p in enumerate(perms):edge_li.setdefault(tuple(sorted(p[:2])),i)
    return D,G,inside,nodes,perms,internal,IE,seed,edge_li

def strict_col(D,G,inside,nodes,internal,IE,seed,li):
    u=nodes[li];specs=[]
    for sign,spec in G.oriented_specs(u):
        v,a,b,c=spec;path=D.plaquette_path(v,a,b)
        if len(path)-1==4 and set(path[:-1])<=inside and D.neighbor[(v,c)] in inside:specs.append((sign,spec))
    if len(specs)!=1:raise RuntimeError(('strict q4 spec count',li,len(specs)))
    sign,spec=specs[0];raw={};add(raw,dict(G.T_items(seed,*spec,JMAX2,False)),-.5j*sign);add(raw,dict(G.T_items(seed,*spec,JMAX2,True)),+.5j*sign)
    p4={k:a for k,a in raw.items() if abs(a)>TOL and sum(s!=1 for s in k[0])==4};col=defaultdict(complex)
    for (sp,Ks),a in p4.items():col[(tuple(sp[G.EIDX[e]] for e in internal),tuple(Ks[v] for v in nodes))]+=a
    return {k:a for k,a in col.items() if abs(a)>TOL}

def engine(D,nodes,inside,internal,IE,states):
    cache={};mats=PW.spin_mats_cached(1);perms=tuple(itertools.permutations(range(4)));face_nodes={f:[i for i,p in enumerate(perms) if p[3]==f] for f in range(4)}
    def tensor(st,ul):
        key=(st,ul)
        if key in cache:return cache[key]
        isp,Ks=st;u=nodes[ul];ls=[isp[IE[tuple(sorted((u,D.neighbor[(u,r)])))]] for r in range(3)]+[1]
        T=PW.intertwiner_tensor_cached(tuple(ls),Ks[ul]).copy()
        for r in range(3):
            w=D.neighbor[(u,r)]
            if u>w:T=PW.apply_axis_np(T,r,PW.epsilon_j(ls[r]))
        cache[key]=T;return T
    def transfer(ket,bra,ul,O=None):
        A=tensor(ket,ul);B=tensor(bra,ul)
        if O is not None:A=PW.apply_axis_np(A,3,O)
        X=np.tensordot(A,B.conj(),axes=([3],[3]));X=np.transpose(X,(0,3,1,4,2,5));return X.reshape([A.shape[r]*B.shape[r] for r in range(3)])
    def contract(tr):
        args=[]
        for ul,u in enumerate(nodes):args.extend([tr[ul],[IE[tuple(sorted((u,D.neighbor[(u,r)])))] for r in range(3)]])
        args.append([]);return oe.contract(*args,optimize='greedy')
    def ov(ket,bra):return contract([transfer(ket,bra,u) for u in range(24)])
    def zfg(ket,bra,f,g):
        base=[transfer(ket,bra,u) for u in range(24)];tot=0j
        for u in face_nodes[f]:
            for v in face_nodes[g]:
                for M in mats:
                    tr=base.copy()
                    if u==v:tr[u]=transfer(ket,bra,u,M@M)
                    else:tr[u]=transfer(ket,bra,u,M);tr[v]=transfer(ket,bra,v,M)
                    tot+=contract(tr)
        return tot
    return ov,zfg

def class_kind(a,b):return 'same' if a==b else ('adjacent' if len(set(a)&set(b))==1 else 'opposite')
def response_matrix(vals):return np.array([[vals[class_kind(o,t)] for t in EDGES] for o in EDGES],float)

def run():
    t0=time.perf_counter();D,G,inside,nodes,perms,internal,IE,seed,edge_li=setup();needed={(0,1),(0,2),(2,3),(1,3)};cols={}
    for e in needed:
        li=edge_li[e];cols[e]=strict_col(D,G,inside,nodes,internal,IE,seed,li);G.primitive_items.cache_clear();G.T_items.cache_clear();G.oriented_intertwiner.cache_clear()
    base=(tuple([1]*len(internal)),tuple([0]*24));states=[base]+sum((list(c) for c in cols.values()),[]);ov,zfg=engine(D,nodes,inside,internal,IE,states)
    n0=complex(ov(base,base));z01=complex(zfg(base,base,0,1));c0=complex(zfg(base,base,0,0));c01=cols[(0,1)];items=list(c01.items());d=0j
    for sa,ca in items:
        for sb,cb in items:d+=np.conjugate(ca)*cb*ov(sb,sa)
    hvals={}
    for e,c in cols.items():hvals[e]=parity(perms[edge_li[e]])*sum(a*ov(st,base) for st,a in c.items())
    common=abs(hvals[(0,1)])**2/n0.real;dperp=d.real-common;den=math.sqrt(n0.real*dperp);reps={}
    for out,tagmap in [((0,1),{'same':(0,1),'adjacent':(0,2),'opposite':(2,3)}),((0,2),{'same':(0,2),'adjacent':(0,1),'opposite':(1,3)})]:
        z00=complex(zfg(base,base,*out));rr={}
        for tag,e in tagmap.items():
            z=parity(perms[edge_li[e]])*sum(a*zfg(st,base,*out) for st,a in cols[e].items());zsub=z-(hvals[e]/n0)*z00;raw=zsub/den;deriv=2*((-1j)*raw).real
            rr[tag]={'source_edge':list(e),'raw_operator_image_cross_re':float(raw.real),'raw_operator_image_cross_im':float(raw.imag),'Schrodinger_tangent_derivative':float(deriv)}
        reps[str(out)]=rr
    primary={k:v['Schrodinger_tangent_derivative'] for k,v in reps[str((0,1))].items()};B=response_matrix(primary);rank=int(np.linalg.matrix_rank(B,tol=1e-10));cond=float(np.linalg.cond(B))
    Cface=float((c0/n0).real);Zpair=float((z01/n0).real);Jraw=Cface*J_FLUX;M=np.linalg.solve(Jraw,B);MG=M.T@M;D5=np.zeros((5,6))
    for i in range(5):D5[i,i]=1;D5[i,5]=-1
    Rq=D5@J_EDGE@M;rqrank=int(np.linalg.matrix_rank(Rq,tol=1e-10));null=np.linalg.svd(Rq)[2][-1];null/=np.mean(null)
    rot=max(abs(reps[str((0,1))][k]['Schrodinger_tangent_derivative']-reps[str((0,2))][k]['Schrodinger_tangent_derivative']) for k in primary);sq3def=abs(primary['opposite']+math.sqrt(3));zero=max(abs(primary['same']),abs(primary['adjacent']))
    checks={'L1_closed_384':D.n_tets==384,'four_representative_columns_support20':all(len(c)==20 for c in cols.values()),'background_norm_positive':n0.real>0 and abs(n0.imag)<1e-20,'regular_pair_flux_minus_three_halves':abs(Zpair+1.5)<1e-10,'regular_face_Casimir_nine_halves':abs(Cface-4.5)<1e-10,'coarse_flux_closure':abs(Cface+3*Zpair)<1e-10,'projected_tangent_norm_positive':dperp>0,'same_adjacent_linear_response_zero':zero<1e-10,'opposite_linear_response_nonzero':abs(primary['opposite'])>1e-3,'rotated_S4_class_spotcheck':rot<1e-10,'metric_response_rank6':rank==6,'metric_response_well_conditioned':cond<1.0000001,'metric_map_rank6':np.linalg.matrix_rank(M,tol=1e-10)==6,'photon_balanced_response_rank5':rqrank==5,'photon_response_uniform_null':np.linalg.norm(null-np.ones(6))<1e-10};checks={k:bool(v) for k,v in checks.items()}
    return {'status':'direct L1 coarse face-flux response of BCQG strict q4 carrier','passed':bool(all(checks.values())),'science_status':'DIRECT_L1_METRIC_RESPONSE_PRECURSOR','checks':checks,'background_norm_square':n0.real,'background_face_Casimir':Cface,'background_pair_flux_dot':Zpair,'background_closure_scalar_defect':Cface+3*Zpair,'representative_source_boundary_norm_square':d.real,'background_component_norm_square':common,'background_orthogonal_per_source_norm_square':dperp,'representative_response_classes':reps,'B_flux_raw_6x6':B.tolist(),'B_flux_rank':rank,'B_flux_singular_values':np.linalg.svd(B,compute_uv=False).tolist(),'B_flux_condition_number':cond,'opposite_closed_form_minus_sqrt3_defect_diagnostic':sq3def,'geometric_flux_J_background_scaled':Jraw.tolist(),'q_to_metric_h_map':M.tolist(),'q_to_metric_Gram_eigenvalues':np.linalg.eigvalsh(MG).tolist(),'q_to_metric_condition_number':float(np.linalg.cond(M)),'balanced_photon_phase_response_per_kappa':Rq.tolist(),'balanced_photon_phase_rank':rqrank,'balanced_photon_phase_null_vector_normalized':null.tolist(),'runtime_seconds':time.perf_counter()-t0,'interpretation':'After exact block contraction, the sharp microscopic spin-selection obstruction is removed at the coarse observable level. The Schrodinger tangent -i E|Omega> has a full-rank face-flux Gram response. Same and adjacent channels vanish while the opposite dual edge/face-pair channel is nonzero; numerically it equals -sqrt(3) to roundoff. Combining the measured B_flux with the independent flux->metric and metric->optical maps yields a rank-five balanced photon phase response whose only null direction is the uniform trace mode.','scope_note':'Finite strict-q4 Euclidean precursor. Full E+S+R depth-two effective scalar, leakage, refinement trend and absolute optical scale remain open.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();txt=json.dumps(o,indent=2,default=lambda x:x.item() if hasattr(x,'item') else str(x));print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+'\n')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())