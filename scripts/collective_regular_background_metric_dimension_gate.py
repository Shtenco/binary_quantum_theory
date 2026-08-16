#!/usr/bin/env python3
"""Metric-dimension precursor for the canonical regular barycentric background.

Use the regular 16-cell tetrahedral realization selected by the static
collective flux Gram and carry its intrinsic piecewise-flat coordinates through
barycentric subdivision. Edge lengths are Euclidean simplex lengths and vertex
masses are one quarter of incident tetrahedral volumes. Weighted 1-skeleton
shortest paths then define a concrete metric ball-volume observable.

Two estimators are reported:
  * fixed volume fraction 5-35%: useful compact/global diagnostic but not a
    local continuum estimator because r/R does not shrink;
  * mesoscopic r*=sqrt(h R), with h=median mesh-edge length and
    R=V_total^(1/3), so h/r* ->0 and r*/R ->0 under refinement. Three fixed
    log-window factors sqrt(2), 1.5 and 2 are reported to avoid tuning one
    window to D=3.

This is a static-background metric precursor. It is not substituted for the
direct dynamical D_space field required by the collective GR killer.
"""
from __future__ import annotations
import argparse,itertools,json,math
from collections import defaultdict
from pathlib import Path
import numpy as np
import scipy.sparse as sp
import scipy.sparse.csgraph as cs


def seed():
    coords=[]
    for i in range(4):
        p=np.zeros(4);p[i]=1;coords.append(p.copy());p[i]=-1;coords.append(p.copy())
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
def tet_volume(coords,t):
    p=coords[list(t)];A=np.stack([p[1]-p[0],p[2]-p[0],p[3]-p[0]],axis=1);G=A.T@A
    return math.sqrt(max(float(np.linalg.det(G)),0.0))/6
def graph(coords,tets):
    E={};mass=np.zeros(len(coords))
    for t in tets:
        v=tet_volume(coords,t)
        for x in t:mass[x]+=v/4
        for a,b in itertools.combinations(t,2):
            if a>b:a,b=b,a
            E.setdefault((a,b),float(np.linalg.norm(coords[a]-coords[b])))
    rows=[];cols=[];data=[]
    for (a,b),w in E.items():rows += [a,b];cols += [b,a];data += [w,w]
    return sp.csr_matrix((data,(rows,cols)),shape=(len(coords),len(coords))),mass,np.array(list(E.values()))
def grouped_points(d,mass,selector):
    order=np.argsort(d);ds=d[order];ms=mass[order];cum=np.cumsum(ms);tot=cum[-1];out=[];i=0
    while i<len(ds):
        j=i+1;tol=1e-10*max(1.0,abs(float(ds[i])))
        while j<len(ds) and abs(float(ds[j]-ds[i]))<=tol:j+=1
        r=float(ds[i]);V=float(cum[j-1]);frac=float(V/tot)
        if r>1e-12 and selector(r,V,frac):out.append((r,V,frac))
        i=j
    return out
def fit(points):
    if len(points)<3:return None
    x=np.log([p[0] for p in points]);y=np.log([p[1] for p in points]);s,b=np.polyfit(x,y,1);pred=s*x+b
    r2=1-float(np.sum((y-pred)**2))/max(float(np.sum((y-y.mean())**2)),1e-30)
    return {'D':float(s),'r2':r2,'n_points':int(len(points))}
def roots(n):
    if n<=100:return np.arange(n,dtype=int)
    return np.unique(np.linspace(0,n-1,32 if n>10000 else 64,dtype=int))
def summarize(fits):
    good=[x for x in fits if x]
    if not good:return None
    D=np.array([x['D'] for x in good]);R=np.array([x['r2'] for x in good])
    return {'roots_fit':int(len(good)),'D_median':float(np.median(D)),'D_mean':float(np.mean(D)),
            'D_min':float(D.min()),'D_max':float(D.max()),'r2_median':float(np.median(R)),
            'points_median':float(np.median([x['n_points'] for x in good]))}
def level(coords,tets,l):
    G,mass,lengths=graph(coords,tets);rr=roots(len(coords));dist=cs.dijkstra(G,directed=False,indices=rr)
    fixed=[fit(grouped_points(d,mass,lambda r,V,f:.05<=f<=.35)) for d in dist]
    h=float(np.median(lengths));R=float(mass.sum()**(1/3));rho=math.sqrt(h*R)
    meso={}
    for f in (math.sqrt(2),1.5,2.0):
        lo=rho/f;hi=rho*f
        rows=[fit(grouped_points(d,mass,lambda r,V,q,lo=lo,hi=hi:lo<=r<=hi)) for d in dist]
        meso[str(f)]={'window':[float(lo),float(hi)],**(summarize(rows) or {})}
    return {'level':int(l),'vertices':int(len(coords)),'tetrahedra':int(len(tets)),'edges':int(G.nnz//2),
            'total_volume':float(mass.sum()),'median_edge_h':h,'macroscopic_R_V13':R,'rho_sqrt_hR':rho,
            'rho_over_h':float(rho/h),'rho_over_R':float(rho/R),'fixed_fraction_5_35':summarize(fixed),'mesoscopic':meso}
def run():
    c,t=seed();clean=[]
    for l in range(1,4):
        c,t=subdivide(c,t);clean.append(level(c,t,l))
    vols=[r['total_volume'] for r in clean]
    vol_rel=float((max(vols)-min(vols))/max(float(np.mean(vols)),1e-30))
    meso2=[float(r['mesoscopic']['2.0']['D_median']) for r in clean]
    fixed=[float(r['fixed_fraction_5_35']['D_median']) for r in clean]
    checks={'barycentric_volume_conserved':bool(vol_rel<1e-12),
            'mesoscopic_scale_separates':bool(clean[-1]['rho_over_h']>clean[0]['rho_over_h'] and clean[-1]['rho_over_R']<clean[0]['rho_over_R']),
            'metric_fits_exist_all_levels':bool(all(r['fixed_fraction_5_35'] and all('D_median' in x for x in r['mesoscopic'].values()) for r in clean)),
            'mesoscopic_dimension_rises_across_refinement':bool(meso2[-1]>meso2[0]),
            'fixed_fraction_dimension_rises_across_refinement':bool(fixed[-1]>fixed[0])}
    passed=bool(all(checks.values()))
    return {'status':'static regular-background metric-dimension precursor','passed':passed,'checks':checks,
            'levels':clean,
            'primary_mesoscopic_factor2_D_medians':meso2,'fixed_fraction_D_medians':fixed,
            'interpretation':'The metric observable is derived from the regular coarse flux background, not bare graph distance. Fixed-fraction balls retain compact-S3 curvature; the mesoscopic sqrt(hR) window increasingly separates lattice and curvature scales and trends toward a local three-dimensional value.',
            'science_status':'PRECURSOR_ONLY',
            'scope_note':'Do not populate D_space_metric in the collective GR killer from this static precursor. The killer requires the same observable on the dynamically enlarged effective block states.'}
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path)
    a=ap.parse_args();o=run();txt=json.dumps(o,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
