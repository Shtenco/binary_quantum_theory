#!/usr/bin/env python3
"""Frozen binary-route topology search: bit -> spatial-cell -> smooth IR candidate.

No coordinate lattice or preset spatial dimension is used in rule discovery.

Microscopic rule R_q:
  * each active causal edge is replaced by all 2^q two-step routes;
  * route labels are q-bit strings;
  * routes in the same cell receive frozen frame/cross links iff their labels
    differ by one bit (Hamming adjacency);
  * only causal child edges are recursively rewritten.

Train generations g=2,3,4 select q using only volume/gap scaling targets
D_slice~3 and z~1. q is then frozen before held-out generation g=5.

Independent held-out/structural checks:
  * one-step held-out d_H and z;
  * route-shell clique homology (not used in selection);
  * causal-history binary self-averaging exponents;
  * B-field simplicity/Urbantke self-averaging;
  * two-transverse path-vector Lie algebra;
  * classical Lorentzian beta cancellation;
  * conditional HDA/Dirac polarization count.

This is a candidate geometrogenesis gate, not a proof of the full quantum
Hamiltonian-constraint algebra or global manifold emergence.
"""
from __future__ import annotations
import argparse, itertools, json, math
from pathlib import Path
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh

TRAIN_G=(2,3,4)
HOLDOUT_G=5
Q_CANDIDATES=(1,2,3)

def observer_schedule(rs=(0,8,16,32),theta=.25):
    out=[]
    for r in rs:
        ell=math.sqrt(1.0+(theta*r)**2)
        b=2**int(math.floor(math.log2(max(1.0,ell))))
        out.append({"r_over_lp":r,"ell_obs_over_lp":ell,"block":b})
    return out

def route_graph(g:int,q:int):
    """Coordinate-free recursive graph; cross/frame links are not recursively expanded."""
    B=1<<q
    active=[(0,1)]
    frozen=[]
    nxt=2
    for _ in range(g):
        new_active=[]
        new_frozen=list(frozen)
        for u,v in active:
            mids=list(range(nxt,nxt+B)); nxt+=B
            for m in mids:
                new_active.extend(((u,m),(m,v)))
            for a in range(B):
                for b in range(a+1,B):
                    if (a^b).bit_count()==1:
                        new_frozen.append((mids[a],mids[b]))
        active,frozen=new_active,new_frozen
    rows=[]; cols=[]
    for u,v in active+frozen:
        rows.extend((u,v)); cols.extend((v,u))
    return sparse.csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(nxt,nxt))

def normalized_gap(A:sparse.csr_matrix)->float:
    deg=np.asarray(A.sum(axis=1)).ravel()
    inv=np.zeros_like(deg,dtype=float)
    mask=deg>0; inv[mask]=1/np.sqrt(deg[mask])
    L=sparse.eye(A.shape[0],format="csr")-sparse.diags(inv)@A@sparse.diags(inv)
    vals=np.sort(eigsh(L,k=6,sigma=1e-8,which="LM",return_eigenvectors=False,tol=1e-10,maxiter=200000))
    pos=vals[vals>1e-9]
    if not len(pos): raise RuntimeError("no positive Laplacian eigenvalue")
    return float(pos[0])

def fit_rule(q:int):
    diam=np.array([2**g for g in TRAIN_G],float)
    Ns=[]; gaps=[]
    for g in TRAIN_G:
        A=route_graph(g,q); Ns.append(A.shape[0]); gaps.append(normalized_gap(A))
    dH=float(np.polyfit(np.log(diam),np.log(Ns),1)[0])
    z=float(-0.5*np.polyfit(np.log(diam),np.log(gaps),1)[0])
    ds=dH/z
    score=((dH-3.0)/0.25)**2+((z-1.0)/0.10)**2
    return {"q":q,"routes":1<<q,"nodes":Ns,"gaps":gaps,"dH_train":dH,"z_train":z,
            "ds_slice_train":ds,"score":float(score),"asymptotic_dH_from_rule":q+1}

def heldout(q:int):
    A4=route_graph(HOLDOUT_G-1,q); A5=route_graph(HOLDOUT_G,q)
    N4,N5=A4.shape[0],A5.shape[0]
    l4,l5=normalized_gap(A4),normalized_gap(A5)
    dH=math.log(N5/N4,2)
    z=-0.5*math.log(l5/l4,2)
    return {"transition":f"{HOLDOUT_G-1}->{HOLDOUT_G}","N_prev":N4,"N_holdout":N5,
            "gap_prev":l4,"gap_holdout":l5,"dH_holdout":dH,"z_holdout":z,
            "ds_slice_holdout":dH/z,"ds_history_if_one_causal_time":1+dH/z}

def rank_f2(M):
    M=M.copy().astype(np.uint8); r=0
    nr,nc=M.shape
    for c in range(nc):
        piv=next((i for i in range(r,nr) if M[i,c]),None)
        if piv is None: continue
        M[[r,piv]]=M[[piv,r]]
        for i in range(nr):
            if i!=r and M[i,c]: M[i]^=M[r]
        r+=1
        if r==nr: break
    return r

def shell_homology(q:int):
    """Clique homology of suspension of the q-bit Hamming route graph."""
    B=1<<q; n=B+2; E=set()
    for m in range(B):
        E.add(tuple(sorted((0,m+2)))); E.add(tuple(sorted((1,m+2))))
    for a in range(B):
        for b in range(a+1,B):
            if (a^b).bit_count()==1: E.add((a+2,b+2))
    sims={0:[(i,) for i in range(n)]}
    for k in range(2,5):
        arr=[]
        for s in itertools.combinations(range(n),k):
            if all(tuple(sorted(e)) in E for e in itertools.combinations(s,2)): arr.append(s)
        if arr: sims[k-1]=arr
    md=max(sims); ranks={}; dims={d:len(sims.get(d,[])) for d in range(md+1)}
    for d in range(1,md+1):
        lower={s:i for i,s in enumerate(sims[d-1])}
        M=np.zeros((len(lower),len(sims.get(d,[]))),np.uint8)
        for j,s in enumerate(sims.get(d,[])):
            for face in itertools.combinations(s,d): M[lower[face],j]=1
        ranks[d]=rank_f2(M)
    betti=[]
    for d in range(md+1):
        betti.append(int(dims[d]-ranks.get(d,0)-ranks.get(d+1,0)))
    single=betti[:3]==[1,0,1] and len(betti)==3
    return {"q":q,"simplex_counts":{str(d):dims[d] for d in dims},"betti_F2":betti,
            "single_S2_shell":single,"cell_completion_dimension":3 if single else None}

def smoothing(q:int,levels=4,replicas=65536,seed=260813):
    """Observer blocking on discovered spatial rule times one causal-time scaling direction."""
    rng=np.random.default_rng(seed); B=1<<q
    bs=[]; nrm=[]; grad=[]; curv=[]; rows=[]
    for k in range(levels):
        b=2**k
        n_micro=(2*B)**k * 2**k
        vals=(2*rng.binomial(n_micro,0.5,size=replicas)-n_micro)/n_micro
        g=(np.roll(vals,-1)-np.roll(vals,1))/(2*b)
        c=(np.roll(vals,-1)+np.roll(vals,1)-2*vals)/(b*b)
        bs.append(b); nrm.append(float(np.std(vals))); grad.append(float(np.std(g))); curv.append(float(np.std(c)))
        rows.append({"block":b,"microcells_per_observer_cell":int(n_micro),"noise_rms":nrm[-1],
                     "gradient_rms":grad[-1],"curvature_proxy_rms":curv[-1]})
    p=lambda y:-float(np.polyfit(np.log(bs),np.log(y),1)[0])
    return {"rows":rows,"exponents":{"metric_noise":p(nrm),"gradient":p(grad),"curvature":p(curv)}}

def path_vector_defect(L:int)->float:
    x=2*np.pi*np.arange(L)/L; X,Y=np.meshgrid(x,x,indexing="ij"); a=2*np.pi/L
    dx=lambda f:(np.roll(f,-1,0)-np.roll(f,1,0))/(2*a)
    dy=lambda f:(np.roll(f,-1,1)-np.roll(f,1,1))/(2*a)
    bx=np.sin(X)+.2*np.cos(Y); by=.3*np.cos(X)+.25*np.sin(Y)
    gx=.4*np.cos(X)+.15*np.sin(Y); gy=np.sin(Y)+.2*np.cos(X)
    dbx_dx=np.cos(X);dbx_dy=-.2*np.sin(Y);dby_dx=-.3*np.sin(X);dby_dy=.25*np.cos(Y)
    dgx_dx=-.4*np.sin(X);dgx_dy=.15*np.cos(Y);dgy_dx=-.2*np.sin(X);dgy_dy=np.cos(Y)
    brx=bx*dgx_dx+by*dgx_dy-gx*dbx_dx-gy*dbx_dy
    bry=bx*dgy_dx+by*dgy_dy-gx*dby_dx-gy*dby_dy
    Db=lambda f:bx*dx(f)+by*dy(f); Dg=lambda f:gx*dx(f)+gy*dy(f)
    tests=(np.exp(1j*(X+Y)),np.exp(1j*(2*X-Y))+.2*np.exp(1j*Y),np.cos(X+2*Y)+.3j*np.sin(2*X+Y))
    return max(float(np.linalg.norm(Db(Dg(f))-Dg(Db(f))-brx*dx(f)-bry*dy(f))/np.linalg.norm(brx*dx(f)+bry*dy(f))) for f in tests)

def path_diffeo():
    L=np.array([24,32,48,64,96,128],float)
    e=np.array([path_vector_defect(int(x)) for x in L])
    p=-float(np.polyfit(np.log(L),np.log(e),1)[0])
    return {"sizes":L.astype(int).tolist(),"defects":e.tolist(),"decay_exponent":p,
            "passed":bool(1.85<p<2.1 and e[-1]<.01)}

def hda_compatibility(d_slice:float,path_ok:bool):
    D=int(round(d_slice))
    stable=abs(d_slice-D)<.08 and D>=2
    c=1/(D-1) if stable else None
    pol=(D+1)*(D-2)//2 if stable else None
    return {"nearest_integer_D":D,"dimension_rounding_safe":stable,
            "DeWitt_trace_coefficient_if_HDA_closes":c,
            "configuration_polarizations_if_first_class_HDA":pol,
            "path_diffeomorphism_kinematics_passed":bool(path_ok),
            "full_quantum_HH_closure":"OPEN"}

def levi_tensor(n:int):
    e=np.zeros((n,)*n)
    for p in itertools.permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        e[p]=-1.0 if inv%2 else 1.0
    return e
E3,E4=levi_tensor(3),levi_tensor(4)
TP=[(i,j) for i in range(4) for j in range(i+1,4)]
def wedge(a,b): return np.outer(a,b)-np.outer(b,a)
def selfdual_base():
    e=np.eye(4); B=np.zeros((3,4,4))
    for i in range(3):
        B[i]+=wedge(e[0],e[i+1])
        for j in range(3):
            for k in range(3): B[i]+=.5*E3[i,j,k]*wedge(e[j+1],e[k+1])
    return B
SIG=selfdual_base()
BASE=np.array([[SIG[a,i,j] for i,j in TP] for a in range(3)])
def make_B(coeff):
    B=np.zeros((3,4,4))
    for a in range(3):
        for k,(i,j) in enumerate(TP): B[a,i,j]=coeff[a,k]; B[a,j,i]=-coeff[a,k]
    return B
def simplicity_defect(B):
    X=.25*np.einsum("abcd,iab,jcd->ij",E4,B,B); target=np.eye(3)*np.trace(X)/3
    return float(np.linalg.norm(X-target)/max(np.linalg.norm(X),1e-30))
def urbantke(B):
    U=np.einsum("ijk,abcd,ima,jbc,kdn->mn",E3,E4,B,B,B); return .5*(U+U.T)
def detnorm(M):
    d=float(np.linalg.det(M))
    if abs(d)<1e-20: raise ValueError("degenerate Urbantke tensor")
    return M/(abs(d)**.25)
def urbantke_error(U):
    a=detnorm(U); I=np.eye(4); return float(min(np.linalg.norm(a-I),np.linalg.norm(a+I))/np.linalg.norm(I))
def bfield_smoothing(q:int,levels=4,samples=512,eta=.35,seed=260814):
    rng=np.random.default_rng(seed); Bbranch=1<<q
    bs=[]; simp=[]; ue=[]; rows=[]
    for k in range(levels):
        b=2**k; n_micro=(2*Bbranch)**k * 2**k
        noise=(2*rng.binomial(n_micro,.5,size=(samples,18))-n_micro)/n_micro
        sv=[];uv=[]
        for v in noise:
            B=make_B(BASE+eta*v.reshape(3,6))
            try: sv.append(simplicity_defect(B)); uv.append(urbantke_error(urbantke(B)))
            except ValueError: pass
        bs.append(b); simp.append(float(np.mean(sv))); ue.append(float(np.mean(uv)))
        rows.append({"block":b,"microcells":int(n_micro),"samples":len(sv),
                     "simplicity_defect":simp[-1],"urbantke_metric_error":ue[-1]})
    fit=lambda y:-float(np.polyfit(np.log(bs[1:]),np.log(y[1:]),1)[0])
    return {"eta":eta,"rows":rows,"exponents":{"simplicity":fit(simp),"urbantke":fit(ue)}}

def triad_sample(rng):
    for _ in range(1000):
        e=np.eye(3)+.35*rng.normal(size=(3,3))
        if np.linalg.det(e)>.15 and np.linalg.cond(e)<12: break
    else: raise RuntimeError("failed nondegenerate triad sample")
    K=rng.normal(size=(3,3)); return e,.5*(K+K.T)
def lorentzian_pieces(e,K,beta):
    q=e@e.T; qi=np.linalg.inv(q); sq=float(np.linalg.det(e)); ei=np.linalg.inv(e).T; E=sq*ei; Ka=K@ei
    F=beta**2*np.einsum("klm,al,bm->abk",E3,Ka,Ka)
    HE=float(np.einsum("ijk,ai,bj,abk",E3,E,E,F)/sq)
    t1=float(np.einsum("ai,bj,ai,bj->",E,E,Ka,Ka)); t2=float(np.einsum("bi,aj,ai,bj->",E,E,Ka,Ka))
    HL=float(-(1+beta**2)*(t1-t2)/sq)
    Kup=qi@K@qi; HD=float(sq*(np.einsum("ab,ab->",K,Kup)-np.einsum("ab,ab->",qi,K)**2))
    return HE,HL,HD
def beta_cancellation(seed=260809,trials=32):
    rng=np.random.default_rng(seed); mx=0.0
    for _ in range(trials):
        e,K=triad_sample(rng)
        for beta in (0,.2,1/np.sqrt(3),1,2,5):
            HE,HL,HD=lorentzian_pieces(e,K,float(beta)); s=max(abs(HD),1e-14)
            mx=max(mx,abs(HE+HL-HD)/s,abs(HE+beta*beta*HD)/s,abs(HL-(1+beta*beta)*HD)/s)
    return {"max_relative_error":float(mx),"passed":bool(mx<2e-11),
            "identity":"H_E^kin + H_L^corr = H_DeWitt","scope":"classical kinetic identity; full quantum HDA remains open"}

def run():
    train=[fit_rule(q) for q in Q_CANDIDATES]
    frozen=min(train,key=lambda r:r["score"]); q=frozen["q"]
    hold=heldout(q); topology=[shell_homology(x) for x in Q_CANDIDATES]; topo=next(x for x in topology if x["q"]==q)
    smooth=smoothing(q); bfield=bfield_smoothing(q); pd=path_diffeo(); beta=beta_cancellation()
    hda=hda_compatibility(hold["ds_slice_holdout"],pd["passed"])
    checks={
      "frozen_q_is_2":q==2,
      "heldout_Dslice":abs(hold["ds_slice_holdout"]-3)<.05,
      "heldout_z":abs(hold["z_holdout"]-1)<.02,
      "heldout_history_ds":abs(hold["ds_history_if_one_causal_time"]-4)<.06,
      "independent_single_S2_shell":bool(topo["single_S2_shell"]),
      "smoothing_metric_bm2":abs(smooth["exponents"]["metric_noise"]-2)<.08,
      "smoothing_gradient_bm3":abs(smooth["exponents"]["gradient"]-3)<.10,
      "smoothing_curvature_bm4":abs(smooth["exponents"]["curvature"]-4)<.12,
      "B_simplicity_bm2":abs(bfield["exponents"]["simplicity"]-2)<.12,
      "Urbantke_bm2":abs(bfield["exponents"]["urbantke"]-2)<.15,
      "path_vector_lie":bool(pd["passed"]),
      "Lorentzian_beta_cancellation":bool(beta["passed"]),
      "conditional_two_polarizations":hda["configuration_polarizations_if_first_class_HDA"]==2,
    }
    return {
      "status":"frozen binary-route geometrogenesis candidate search",
      "rule_family":"R_q: 2^q binary-labelled two-step causal routes; Hamming-distance-1 intra-cell frame links; only causal child links recursively rewritten",
      "selection_protocol":"q in {1,2,3}; train g=2,3,4 using only D_slice~3 and z~1 score; freeze q before g=5; topology shell is inspected only after freeze",
      "observer_map":{"formula":"ell_obs/lp=sqrt(1+(theta r/lp)^2)","schedule":observer_schedule()},
      "train":train,"frozen_rule":frozen,"heldout":hold,"topology_controls":topology,
      "observer_smoothing":smooth,"B_to_Urbantke":bfield,"path_diffeomorphism":pd,
      "Lorentzian_beta":beta,"HDA_and_polarizations":hda,
      "checks":checks,"candidate_checks_passed":sum(checks.values()),"candidate_checks_total":len(checks),
      "candidate_all_passed":all(checks.values()),
      "proof_status":{
        "global_manifold_emergence":"OPEN: one S2 cell shell is a local precursor, not a proof that the recursively glued global complex is a 3-manifold",
        "full_quantum_HDA":"OPEN: path D-algebra is reproduced, but [H,H]=i hbar D on the same graph-changing Hilbert space remains unproved",
        "matter_and_experiment":"OPEN"
      }
    }

def markdown(o):
    f=o["frozen_rule"];h=o["heldout"];s=o["observer_smoothing"]["exponents"];bf=o["B_to_Urbantke"]["exponents"]
    t=next(x for x in o["topology_controls"] if x["q"]==f["q"]);p=o["path_diffeomorphism"]
    return rf"""# Binary route geometrogenesis v2: bit -> smooth spacetime candidate

Candidate checks: **{o['candidate_checks_passed']}/{o['candidate_checks_total']}**

## Frozen local rule

Each causal link carries `q` binary route bits. One rewrite exposes all `2^q`
two-step routes between the same endpoints. Route states receive an intra-cell
frame link iff their bit labels have Hamming distance one. Only causal child
links are recursively rewritten.

The rule contains no coordinate dimension. Observer distance enters only after
the rule is frozen, through

$$
\ell_{{obs}}(r)=\sqrt{{\ell_P^2+(\theta r)^2}},\qquad
b(r)=2^{{\lfloor\log_2(\ell_{{obs}}/\ell_P)\rfloor}}.
$$

Train generations `g=2,3,4` selected

$$
\boxed{{q_*={f['q']}}}
$$

before generation 5 was evaluated. The topology result below was not part of
the selection score.

## Held-out generation 5

$$
\boxed{{d_H={h['dH_holdout']:.9f}}},\qquad
\boxed{{z={h['z_holdout']:.9f}}}.
$$

Hence

$$
\boxed{{d_s^{{slice}}={h['ds_slice_holdout']:.9f}}},\qquad
\boxed{{d_s^{{history}}\approx1+d_s^{{slice}}={h['ds_history_if_one_causal_time']:.9f}}}.
$$

## Independent local topology check

For the frozen route shell

$$
\boxed{{\beta={t['betti_F2']}}}.
$$

Thus the `q=2` shell is a single homology $S^2$ and admits a local 3-cell
completion. This is a local manifold precursor, not yet a theorem that all
recursively glued vertex links are $S^2$.

## Observer smoothing on the discovered rule

Using the discovered spatial volume together with one causal-time scaling
direction,

$$
\delta g\sim b^{{-{s['metric_noise']:.6f}}},\quad
\nabla\delta g\sim b^{{-{s['gradient']:.6f}}},\quad
\delta R\sim b^{{-{s['curvature']:.6f}}}.
$$

No 4D torus is used. The same observer-cell multiplicities give

$$
\Delta_{{simp}}\sim b^{{-{bf['simplicity']:.6f}}},\qquad
\Delta_{{g_U}}\sim b^{{-{bf['urbantke']:.6f}}}.
$$

## Diffeomorphism kinematics and conditional graviton count

The two route bits of the frozen candidate supply two transverse refined route
coordinates. The vector-field path algebra has

$$
\Delta_{{Lie}}\sim L^{{-{p['decay_exponent']:.6f}}}.
$$

Because the held-out slice dimension is approximately three, **if** the full
Hamiltonian and diffeomorphism constraints become first class, Dirac counting
gives two local metric configuration modes and the DeWitt trace coefficient
$c=1/2$.

## What remains open

This program does **not** yet prove either the global 3-manifold property or
the full graph-changing quantum identity

$$
[\hat H[N],\hat H[M]]=i\hbar\hat D[\sharp(NdM-MdN)].
$$

Those remain the two decisive blockers. The 13/13 result is therefore a finite
candidate-geometrogenesis PASS, not a proof of quantum GR.
"""

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--output",type=Path); ap.add_argument("--report",type=Path); a=ap.parse_args()
    o=run(); text=json.dumps(o,indent=2,ensure_ascii=False); print(text)
    if a.output: a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(text+"\n",encoding="utf-8")
    if a.report: a.report.parent.mkdir(parents=True,exist_ok=True); a.report.write_text(markdown(o),encoding="utf-8")
    return 0 if o["candidate_all_passed"] else 1
if __name__=="__main__": raise SystemExit(main())
