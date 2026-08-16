#!/usr/bin/env python3
"""Remove the static coarse background from the six-channel L1 boundary carrier.

This gate is chained after ``collective_l1_strict_interior_boundary_rank_gate``.
That theorem establishes the parity-rephased source Gram

  G = d[(1-r) diag(J4,...,J4) + r J24]

with six coarse-edge blocks.  Here we independently compute the static block
boundary norm and its overlap with one representative strict-interior source.
S4 covariance then fixes the overlap with every chamber up to the already
frozen permutation-parity phase.

If d*r = |h|^2 / ||B0||^2, projecting every source vector orthogonally to the
static background exactly removes the inter-edge common component, leaving

  G_perp = d(1-r) diag(J4,...,J4).

Thus the 24 chamber sources reduce to six mutually orthogonal equal-norm edge
channels, four parity-related chambers per coarse edge.  No GR target enters
this orthogonalization: removing the state itself from its tangent space is a
kinematic normalization operation.
"""
from __future__ import annotations
import argparse,itertools,json,math,sys
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

TOL=1e-10
JMAX2=3


def add(dst,src,scale):
    for k,a in src.items():
        z=dst.get(k,0j)+scale*a
        if abs(z)>TOL:dst[k]=z
        elif k in dst:del dst[k]


def representative_column():
    ZVM.patch_and_clear()
    fine,parent=barycentric_with_parent(seed_16cell_boundary());D=DualComplex(fine);G=LocalPLPeterWeylEuclidean(D)
    inside=set(v for v,p in enumerate(parent) if p==0);nodes=sorted(inside);u=nodes[0]
    internal=sorted(e for e in G.EDGES if e[0] in inside and e[1] in inside);IE={e:i for i,e in enumerate(internal)}
    seed=((1,)*len(G.EDGES),(0,)*D.n_tets)
    strict=[]
    for sign,spec in G.oriented_specs(u):
        v,a,b,c=spec;path=D.plaquette_path(v,a,b)
        if len(path)-1==4 and set(path[:-1])<=inside and D.neighbor[(v,c)] in inside:strict.append((sign,spec))
    if len(strict)!=1:raise RuntimeError(('strict source0 spec count',len(strict)))
    sign,spec=strict[0];raw={}
    add(raw,dict(G.T_items(seed,*spec,JMAX2,False)),-.5j*sign);add(raw,dict(G.T_items(seed,*spec,JMAX2,True)),+.5j*sign)
    p4={k:a for k,a in raw.items() if abs(a)>TOL and sum(s!=1 for s in k[0])==4}
    col=defaultdict(complex)
    for (sp,Ks),a in p4.items():
        st=(tuple(sp[G.EIDX[e]] for e in internal),tuple(Ks[v] for v in nodes));col[st]+=a
    col={k:a for k,a in col.items() if abs(a)>TOL}
    return D,nodes,inside,internal,IE,col


def overlap_engine(D,nodes,inside,internal,IE,states):
    @staticmethod
    def _noop():pass
    cache={}
    def tensor(st,u_local):
        key=(st,u_local)
        if key in cache:return cache[key]
        isp,Ks=st;u=nodes[u_local];ls=[]
        for r in range(3):
            w=D.neighbor[(u,r)];ls.append(isp[IE[tuple(sorted((u,w)))]])
        ls.append(1);T=PW.intertwiner_tensor_cached(tuple(ls),Ks[u_local]).copy()
        for r in range(3):
            w=D.neighbor[(u,r)]
            if u>w:T=PW.apply_axis_np(T,r,PW.epsilon_j(ls[r]))
        cache[key]=T;return T
    def ov(a,b):
        args=[]
        for ul,u in enumerate(nodes):
            A=tensor(a,ul);B=tensor(b,ul);X=np.tensordot(A,B.conj(),axes=([3],[3]));X=np.transpose(X,(0,3,1,4,2,5));X=X.reshape([A.shape[r]*B.shape[r] for r in range(3)])
            inds=[IE[tuple(sorted((u,D.neighbor[(u,r)])))] for r in range(3)];args.extend([X,inds])
        args.append([]);return oe.contract(*args,optimize='greedy')
    return ov


def run(strict_result):
    s=json.loads(Path(strict_result).read_text())
    if not s.get('passed') or s.get('structural_boundary_rank')!=6:raise RuntimeError('strict boundary theorem must PASS first')
    d=float(s['d_boundary_norm_square']);r=float(s['r_inter_edge_overlap'])
    D,nodes,inside,internal,IE,col=representative_column();base=(tuple([1]*len(internal)),tuple([0]*24));states=[base]+list(col)
    ov=overlap_engine(D,nodes,inside,internal,IE,states)
    n0=complex(ov(base,base))
    # ov(st,base)=<base|st> with the transfer-tensor convention.
    h=sum(a*ov(st,base) for st,a in col.items())
    # Independent source norm cross-check from the representative 20-state column.
    items=list(col.items());dcalc=0j
    for a,(sa,ca) in enumerate(items):
        for b,(sb,cb) in enumerate(items):dcalc+=np.conjugate(ca)*cb*ov(sb,sa)
    common=abs(h)**2/max(float(n0.real),1e-300)
    relation_rel=abs(d*r-common)/max(abs(d*r),1e-300)
    dperp=d-common
    offperp=d*r-common
    lam=4*dperp
    checks={
        'representative_support_20':len(col)==20,
        'background_norm_positive':n0.real>0 and abs(n0.imag)<1e-20,
        'representative_source_norm_matches_strict_d':abs(dcalc.real-d)/d<1e-10 and abs(dcalc.imag)<1e-20,
        'background_common_component_identity':relation_rel<1e-10,
        'projected_inter_edge_overlap_zero':abs(offperp)/max(dperp,1e-300)<1e-10,
        'projected_edge_norm_positive':dperp>0,
    }
    return {
        'status':'background-orthogonal six-edge L1 metric tangent frame',
        'passed':bool(all(checks.values())),'checks':checks,
        'background_boundary_norm_square':float(n0.real),
        'representative_background_overlap_re':float(h.real),'representative_background_overlap_im':float(h.imag),'representative_background_overlap_abs':float(abs(h)),
        'strict_d':d,'strict_r':r,'common_component_square_over_background_norm':float(common),'common_component_relation_relative_defect':float(relation_rel),
        'projected_per_source_norm_square':float(dperp),'projected_inter_edge_overlap':float(offperp),
        'projected_nonzero_eigenvalue_sixfold':float(lam),'projected_structural_rank':6,
        'projected_24_source_Gram_formula':'D_parity * d_perp * diag(J4,J4,J4,J4,J4,J4) * D_parity',
        'canonical_six_edge_frame_rule':'For each unordered coarse edge {a,b}, choose any chamber p with {p0,p1}={a,b}, multiply its projected boundary vector by permutation parity, and divide by sqrt(d_perp). All four choices are identical; the six resulting vectors are orthonormal.',
        'interpretation':'After removing the static coarse state itself, the strict-interior Euclidean image yields six mutually orthogonal equal-norm coarse-edge tangent directions. The uniform edge combination remains independent, so the trace-like channel is not a pure normalization artifact.',
        'scope_note':'Kinematic tangent normalization only. The full effective scalar must still be applied to these six directions before any kinetic Hessian or DeWitt coefficient is reported.'
    }


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--strict-result',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();o=run(a.strict_result);txt=json.dumps(o,indent=2);print(txt);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+'\n',encoding='utf-8');return 0 if o['passed'] else 1

if __name__=='__main__':raise SystemExit(main())
