#!/usr/bin/env python3
"""Canonical first spatial BCQG block on one barycentrically subdivided tetrahedron.

A barycentric tetrahedron contains 24 fine tetrahedral chambers, one for each
permutation in S4.  Its dual block has 24 four-valent fine nodes, 36 internal
links and 24 boundary links, six on each coarse triangular face.  All fine
links in this gate carry j=1/2.  Each coarse face is projected to the unique
fully symmetric six-qubit irrep j=3.

The gate contracts the exact 24-node spin-network tensor and asks which part of
the seven-dimensional four-j=3 Gauss intertwiner space is populated.  Generic
deterministic fine-intertwiner probes show a rank-one image.  This is a finite
selection/obstruction result: the static all-j=1/2 maximal-symmetric block does
not by itself provide the generic collective metric tangent space required for
GR.  Spin-changing dynamical sectors and/or non-maximal face irreps must be
retained by the direct collective producer.
"""
from __future__ import annotations
import argparse,itertools,json,math,sys
from pathlib import Path
import numpy as np
import opt_einsum as oe

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))
import k5_peter_weyl_safe_hda_column as PW

PERMS=tuple(itertools.permutations(range(4)))
PIDX={p:i for i,p in enumerate(PERMS)}
EPS=PW.epsilon_j(1)
I0=PW.intertwiner_tensor_cached((1,1,1,1),0)
I2=PW.intertwiner_tensor_cached((1,1,1,1),2)


def symmetric_isometry(n=6):
    """Columns are |j=n/2,m=j-k> as normalized Dicke states."""
    W=np.zeros((2**n,n+1),complex)
    for k in range(n+1):
        states=[b for b in itertools.product((0,1),repeat=n) if sum(b)==k]
        a=1/math.sqrt(len(states))
        for bits in states:
            idx=0
            for x in bits:
                idx=(idx<<1)|x
            W[idx,k]=a
    return W


def network_labels():
    edge={}; n=0
    for p in PERMS:
        for i in range(3):
            q=list(p); q[i],q[i+1]=q[i+1],q[i]; q=tuple(q)
            e=tuple(sorted((p,q)))
            if e not in edge:
                edge[e]=n; n+=1
    boundary={p:n+PIDX[p] for p in PERMS}
    coarse={f:n+24+f for f in range(4)}
    return edge,boundary,coarse

EDGE_LABEL,BOUNDARY_LABEL,COARSE_LABEL=network_labels()
W6=symmetric_isometry(6)
P6=W6.conj().T.reshape((7,)+(2,)*6)


def local_tensor(p,alpha,beta):
    T=alpha*I0+beta*I2
    # Every internal dual link is contracted with the SU(2) epsilon metric.
    # Absorb epsilon on the lexicographically larger endpoint to freeze the
    # orientation convention without changing the invariant contraction.
    for i in range(3):
        q=list(p); q[i],q[i+1]=q[i+1],q[i]; q=tuple(q)
        if p>q:
            T=PW.apply_axis_np(T,i,EPS)
    return T


def build_args(coeffs):
    args=[]
    for p,(alpha,beta) in zip(PERMS,coeffs):
        inds=[]
        for i in range(3):
            q=list(p); q[i],q[i+1]=q[i+1],q[i]; q=tuple(q)
            inds.append(EDGE_LABEL[tuple(sorted((p,q)))])
        inds.append(BOUNDARY_LABEL[p])
        args.extend([local_tensor(p,alpha,beta),inds])
    for face in range(4):
        ps=sorted(p for p in PERMS if p[3]==face)
        args.extend([P6,[COARSE_LABEL[face]]+[BOUNDARY_LABEL[p] for p in ps]])
    args.append([COARSE_LABEL[f] for f in range(4)])
    return args


def frozen_path():
    coeffs=[(1+0j,0j)]*24
    path,_=oe.contract_path(*build_args(coeffs),optimize='greedy')
    return path

PATH=frozen_path()
COARSE_INTERTWINERS=tuple(
    PW.intertwiner_tensor_cached((6,6,6,6),K2) for K2 in range(0,13,2)
)
TARGET=np.array([7*math.sqrt(5),0,-24,0,22*math.sqrt(5),0,0],float)/math.sqrt(3241)


def contract(coeffs):
    C=oe.contract(*build_args(coeffs),optimize=PATH)
    amps=np.array([np.vdot(I,C) for I in COARSE_INTERTWINERS])
    return C,amps


def gauss_residual(C):
    n=max(float(np.linalg.norm(C)),1e-300)
    mats=PW.spin_mats_cached(6)
    worst=0.0
    for a in range(3):
        X=np.zeros_like(C)
        for leg in range(4):
            X+=PW.apply_axis_np(C,leg,mats[a])
        worst=max(worst,float(np.linalg.norm(X))/n)
    return worst


def normalized_direction(amps):
    n=np.linalg.norm(amps)
    if n<1e-30:
        return None
    return amps/n


def target_defect(v):
    # Projective comparison: remove arbitrary complex phase/sign.
    z=np.vdot(TARGET,v)
    if abs(z)<1e-30:
        return float('inf')
    phase=z/abs(z)
    return float(np.linalg.norm(v-phase*TARGET))


def generic_coeffs(seed):
    rg=np.random.default_rng(seed)
    out=[]
    for _ in PERMS:
        a=rg.normal()+1j*rg.normal(); b=rg.normal()+1j*rg.normal()
        n=math.sqrt(abs(a)**2+abs(b)**2)
        out.append((a/n,b/n))
    return out


def run(tol=1e-10):
    probes=[]
    structured=[('all_K0',[(1+0j,0j)]*24),('all_K2',[(0j,1+0j)]*24)]
    for name,c in structured:
        C,a=contract(c); v=normalized_direction(a)
        probes.append({
          'name':name,'boundary_norm':float(np.linalg.norm(C)),
          'gauss_relative_residual':gauss_residual(C),
          'singlet_projection_fraction':float(np.vdot(a,a).real/max(np.vdot(C,C).real,1e-300)),
          'target_projective_defect':target_defect(v) if v is not None else None,
          'normalized_K2_0_to_12_amplitudes':[[float(x.real),float(x.imag)] for x in v] if v is not None else None
        })
    dirs=[]
    for seed in range(12):
        C,a=contract(generic_coeffs(seed)); v=normalized_direction(a)
        if v is None:
            continue
        dirs.append(v)
        probes.append({
          'name':f'generic_seed_{seed}','boundary_norm':float(np.linalg.norm(C)),
          'gauss_relative_residual':gauss_residual(C),
          'singlet_projection_fraction':float(np.vdot(a,a).real/max(np.vdot(C,C).real,1e-300)),
          'target_projective_defect':target_defect(v)
        })
    M=np.stack(dirs) if dirs else np.zeros((0,7),complex)
    svals=np.linalg.svd(M,compute_uv=False) if len(M) else np.array([])
    rank=int(np.sum(svals>1e-10))
    max_g=max(r['gauss_relative_residual'] for r in probes)
    max_t=max(r['target_projective_defect'] for r in probes if r['target_projective_defect'] is not None)
    min_frac=min(r['singlet_projection_fraction'] for r in probes)
    passed=(rank==1 and max_g<tol and max_t<tol and abs(min_frac-1)<tol)
    return {
      'status':'canonical barycentric tetrahedron static collective block',
      'passed':bool(passed),'tolerance':tol,
      'fine_chambers':24,'fine_internal_links':36,'fine_boundary_links':24,
      'boundary_links_per_coarse_face':6,
      'fine_link_spin':0.5,'maximal_symmetric_coarse_face_spin':3.0,
      'coarse_four_face_singlet_dimension':7,
      'generic_probe_image_rank':rank,
      'generic_probe_singular_values':svals.tolist(),
      'selected_normalized_coarse_intertwiner':{
        'basis':'K2=0,2,4,6,8,10,12',
        'exact_vector':'(7*sqrt(5), 0, -24, 0, 22*sqrt(5), 0, 0)/sqrt(3241)',
        'numeric':TARGET.tolist()
      },
      'max_gauss_relative_residual':max_g,
      'max_projective_target_defect':max_t,
      'minimum_singlet_projection_fraction':min_frac,
      'probes':probes,
      'conclusion':'The static all-j=1/2 barycentric block projected to fully symmetric j=3 on every coarse face has a rank-one image inside the seven-dimensional coarse Gauss intertwiner space.',
      'required_extension':'The direct collective GR producer must include production spin-changing sectors and/or non-maximal face irreps; otherwise the static maximal-symmetric block has insufficient tangent dimension for a generic GR metric phase.',
      'scope_note':'Finite tensor-network selection result only; it is not a proof that the enlarged dynamical block remains rank one.'
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path)
    ap.add_argument('--tol',type=float,default=1e-10)
    a=ap.parse_args(); o=run(a.tol); t=json.dumps(o,indent=2); print(t)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
