#!/usr/bin/env python3
"""Independent FEM spectral-dimension precursor on barycentric PL-S3 refinement.

This is deliberately NOT a direct dynamical BCQG collective measurement and
must not populate D_space_metric in the collective GR killer. It tests the
static regular PL-S3 carrier with an intrinsic tetrahedral finite-element
Laplacian, independent of the weighted-graph metric precursor.

L0-L2 are diagonalised exactly. L3 is held out: its diffusion-time window is
predicted from the exact L2 peak using only h^2 refinement scaling,
  t3_pred = t2_peak * (h3/h2)^2,
and then scanned over the fixed factor interval [1/4, 2]. No target dimension
is used to choose the L3 window or peak.
"""
from __future__ import annotations
import argparse,itertools,json,math
from collections import defaultdict
from pathlib import Path
import numpy as np
import scipy.linalg as la
import scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply


def seed():
    coords=[]
    for i in range(4):
        p=np.zeros(4);p[i]=1;coords.append(p.copy())
        p=np.zeros(4);p[i]=-1;coords.append(p.copy())
    tets=sorted(tuple(2*i+b for i,b in enumerate(bits)) for bits in itertools.product((0,1),repeat=4))
    return np.array(coords,float),tets


def faces(tets):
    out=defaultdict(set)
    for t in tets:
        for n in range(1,5):
            for f in itertools.combinations(t,n):out[n-1].add(tuple(sorted(f)))
    return out


def subdivide(coords,tets):
    F=faces(tets);allf=sorted(set().union(*F.values()),key=lambda x:(len(x),x));fid={f:i for i,f in enumerate(allf)}
    nc=np.array([coords[list(f)].mean(axis=0) for f in allf]);nt=set()
    for t in tets:
        for p in itertools.permutations(t):
            cur=[];chain=[]
            for v in p:cur.append(v);chain.append(fid[tuple(sorted(cur))])
            nt.add(tuple(chain))
    return nc,sorted(nt)


def edge_stats(coords,tets):
    E=set()
    for t in tets:
        for a,b in itertools.combinations(t,2):E.add((min(a,b),max(a,b)))
    x=np.array([np.linalg.norm(coords[a]-coords[b]) for a,b in E])
    return {'edges':len(E),'h_median':float(np.median(x)),'h_min':float(x.min()),'h_max':float(x.max())}


def fem_laplacian(coords,tets):
    n=len(coords);rows=[];cols=[];data=[];mass=np.zeros(n)
    grad_ref=np.array([[-1,-1,-1],[1,0,0],[0,1,0],[0,0,1]],float)
    for tet in tets:
        p=coords[list(tet)]
        B=np.stack([p[1]-p[0],p[2]-p[0],p[3]-p[0]],axis=1)
        G=B.T@B;det=float(np.linalg.det(G))
        if det<=0:raise RuntimeError(('degenerate tetrahedron',tet,det))
        vol=math.sqrt(det)/6.0;invG=np.linalg.inv(G)
        kl=vol*(grad_ref@invG@grad_ref.T)
        for i,a in enumerate(tet):
            mass[a]+=vol/4.0
            for j,b in enumerate(tet):rows.append(a);cols.append(b);data.append(float(kl[i,j]))
    K=sp.coo_matrix((data,(rows,cols)),shape=(n,n)).tocsr()
    d=1.0/np.sqrt(mass);L=(sp.diags(d)@K@sp.diags(d)).tocsr()
    return L,mass


def spectral_dimension(times,P):
    return -2*np.gradient(np.log(P),np.log(times),axis=0)


def exact_level(coords,tets,level):
    L,m=fem_laplacian(coords,tets);ev=la.eigvalsh(L.toarray());pos=ev[ev>1e-10]
    times=np.geomspace(0.02/float(pos.max()),2.0/float(pos.min()),500)
    P=np.array([np.exp(-tt*ev).mean() for tt in times]);ds=spectral_dimension(times,P)
    i=int(np.argmax(ds));es=edge_stats(coords,tets)
    return {'level':level,'vertices':len(coords),'tetrahedra':len(tets),**es,
            'total_volume':float(m.sum()),'lambda_gap':float(pos.min()),'lambda_max':float(pos.max()),
            'peak_time':float(times[i]),'D_spectral_peak':float(ds[i]),'heat_return_at_peak':float(P[i])}


def stochastic_l3(coords,tets,prev,probes=24,seed_value=424242,points=12):
    L,m=fem_laplacian(coords,tets);es=edge_stats(coords,tets)
    center=prev['peak_time']*(es['h_median']/prev['h_median'])**2
    times=np.linspace(center/4.0,center*2.0,points)
    rg=np.random.default_rng(seed_value);Z=rg.choice((-1.0,1.0),size=(len(coords),probes))
    Y=expm_multiply(-L,Z,start=float(times[0]),stop=float(times[-1]),num=points,endpoint=True)
    Pprobe=np.einsum('ni,tni->ti',Z,Y)/len(coords)
    dsprobe=spectral_dimension(times,Pprobe)
    means=dsprobe.mean(axis=1);ses=dsprobe.std(axis=1,ddof=1)/math.sqrt(probes)
    pmeans=Pprobe.mean(axis=1);i=int(np.argmax(means))
    rows=[{'time':float(t),'D_mean':float(d),'D_standard_error':float(s),'heat_return_mean':float(p)}
          for t,d,s,p in zip(times,means,ses,pmeans)]
    return {'level':3,'vertices':len(coords),'tetrahedra':len(tets),**es,'total_volume':float(m.sum()),
            'heldout_window_rule':'t3_pred=t2_peak*(h3/h2)^2; scan [t3_pred/4,2*t3_pred]',
            'predicted_center_time':float(center),'probes':int(probes),'rng_seed':int(seed_value),'scan_points':int(points),
            'D_spectral_peak_mean':float(means[i]),'D_spectral_peak_standard_error':float(ses[i]),
            'peak_time':float(times[i]),'rows':rows}


def run(probes=24):
    c,t=seed();exact=[];vols=[]
    for l in range(3):
        r=exact_level(c,t,l);exact.append(r);vols.append(r['total_volume']);c,t=subdivide(c,t)
    l3=stochastic_l3(c,t,exact[-1],probes=probes);vols.append(l3['total_volume'])
    D=[r['D_spectral_peak'] for r in exact]+[l3['D_spectral_peak_mean']]
    vol_rel=(max(vols)-min(vols))/max(abs(float(np.mean(vols))),1e-30)
    static_abs_error=abs(D[-1]-3.0)
    checks={'volume_conserved':bool(vol_rel<1e-11),'exact_peaks_strictly_rise_L0_L2':bool(D[0]<D[1]<D[2]),
            'heldout_L3_peak_exceeds_L2':bool(D[3]>D[2]),'finite_L3_uncertainty':bool(np.isfinite(l3['D_spectral_peak_standard_error']))}
    return {'status':'independent intrinsic-FEM spectral-dimension precursor','passed':bool(all(checks.values())),
            'science_status':'PRECURSOR_ONLY','checks':checks,'levels_exact':exact,'level3_heldout':l3,
            'D_peak_sequence':D,'volume_relative_spread':float(vol_rel),
            'GR_target_comparison_only':{'target_D_space':3.0,'L3_abs_error':float(static_abs_error),
                'killer_static_threshold_0p10_met':bool(static_abs_error<=0.10)},
            'interpretation':'An intrinsic tetrahedral FEM Laplacian, independent of bare/weighted graph-distance fitting, shows monotone spectral-dimension growth across the canonical PL-S3 barycentric refinement. The held-out L3 value is not promoted to the collective killer because it is a static background, not a dynamically enlarged effective BCQG block state.',
            'scope_note':'Do not copy this D into D_space_metric. The direct collective producer must recompute the same kind of metric observable after E/S/R support enlargement and operator compression.'}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--probes',type=int,default=24);ap.add_argument('--output',type=Path);a=ap.parse_args()
    if a.probes<4:ap.error('--probes must be >=4')
    o=run(a.probes);txt=json.dumps(o,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
