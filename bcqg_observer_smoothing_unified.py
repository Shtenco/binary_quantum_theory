#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Unified observer-scale coarse-graining gate for binary Planck spacetime.

Interpretation: distance does not dynamically alter spacetime.  A fixed
angular/causal resolution corresponds to a physical resolution
ell_obs(r)=sqrt(ell_P^2+(theta r)^2); unresolved microscopic bits are integrated
into dyadic b^4 blocks.  The 4D smoothing sector below is conditional on a 4D
scaffold.  A dimension-blind binary-diamond control is included specifically to
show that coarse graining alone does not derive four dimensions.
"""
from __future__ import annotations
import argparse,itertools,json,math
from pathlib import Path
import numpy as np

CHECKS=[]
def ck(name,value,target,ok): CHECKS.append({"name":name,"value":float(value) if np.isscalar(value) and not isinstance(value,(str,bool)) else value,"target":target,"passed":bool(ok)})
def pexp(b,y,start=0): return -float(np.polyfit(np.log(np.asarray(b[start:],float)),np.log(np.asarray(y[start:],float)),1)[0])
def block(a,b):
    sq=a.ndim==4
    if sq:a=a[None,...]
    C,L,*_=a.shape;n=L//b
    z=a.astype(float,copy=False) if b==1 else a.reshape(C,n,b,n,b,n,b,n,b).mean(axis=(2,4,6,8))
    return z[0] if sq else z
PAIRS=[(i,j) for i in range(4) for j in range(i,4)]; PID={p:i for i,p in enumerate(PAIRS)}
def d2(f,i,j,a):
    if i==j:return (np.roll(f,-1,i)+np.roll(f,1,i)-2*f)/a**2
    return (np.roll(np.roll(f,-1,i),-1,j)-np.roll(np.roll(f,-1,i),1,j)-np.roll(np.roll(f,1,i),-1,j)+np.roll(np.roll(f,1,i),1,j))/(4*a*a)
def Rlin(h,a):
    R=np.zeros(h.shape[1:])
    for i in range(4):
        for j in range(4):R+=d2(h[PID[(min(i,j),max(i,j))]],i,j,a)
    tr=sum(h[PID[(i,i)]] for i in range(4))
    for i in range(4):R-=d2(tr,i,i,a)
    return R
def grad_rms(h,a):
    return math.sqrt(sum(float(np.mean(((np.roll(h,-1,mu+1)-np.roll(h,1,mu+1))/(2*a))**2)) for mu in range(4))/4)
def schedule(rs=(0,8,16,32),theta=.25):
    out=[]
    for r in rs:
        ell=math.sqrt(1+(theta*r)**2);b=min(8,2**int(math.floor(math.log2(max(1.,ell)))))
        out.append({"r_over_lp":r,"ell_obs_over_lp":ell,"block":b})
    return out
def metric_smoothing(seed=260813,L=24,eps=.08):
    rng=np.random.default_rng(seed);bits=rng.choice(np.array([-1,1],np.int8),(10,L,L,L,L))
    x=2*np.pi*np.arange(L)/L;X,Y=np.meshgrid(x,x,indexing="ij")
    signal=.020*(np.cos(X)+.5*np.sin(Y));signal=signal[:,:,None,None]*np.ones((1,1,L,L))
    rows=[];bs=[];nr=[];gr=[];rr=[];snr=[]
    for q in schedule():
        b=q["block"];hb=block(bits,b);sb=block(signal,b)
        n=eps*float(np.sqrt(np.mean(hb*hb)));g=eps*grad_rms(hb,b);r=float(np.sqrt(np.mean(Rlin(eps*hb,b)**2)))
        s=float(np.sqrt(np.mean(sb*sb)));ratio=s/max(eps*float(np.sqrt(np.mean(hb[0]**2))),1e-30)
        bs.append(b);nr.append(n);gr.append(g);rr.append(r);snr.append(ratio)
        rows.append({**q,"metric_noise_rms":n,"gradient_roughness_rms":g,"linear_curvature_noise_rms":r,"macro_signal_rms":s,"signal_to_binary_noise":ratio})
    pn,pg,pr=pexp(bs,nr),pexp(bs,gr),pexp(bs,rr)
    ck("metric noise exponent",pn,"2 +/- .15",abs(pn-2)<.15);ck("gradient roughness exponent",pg,"3 +/- .20",abs(pg-3)<.20);ck("curvature noise exponent",pr,"4 +/- .35",abs(pr-4)<.35);ck("far/near SNR gain",snr[-1]/snr[0],">20",snr[-1]/snr[0]>20)
    return {"seed":seed,"L":L,"epsilon":eps,"rows":rows,"exponents":{"metric_noise":pn,"gradient":pg,"curvature":pr}}
def heat(L,d,t):
    n=np.arange(L,dtype=float);lam=2-2*np.cos(2*np.pi*n/L);p=np.array([np.exp(-x*lam).mean() for x in t]);return p**d
def ds(t,p):return -2*np.gradient(np.log(p),np.log(t))
def spectral(scales=(1,2,4,8)):
    rows=[]
    for b in scales:
        t=np.geomspace(2*b*b,8*b*b,80);v=ds(t,heat(256,4,t));m=(t>=3*b*b)&(t<=6*b*b);rows.append({"block":b,"mean_ds":float(v[m].mean()),"std_ds":float(v[m].std())})
    e=abs(rows[-1]["mean_ds"]-4);ck("far conditional spectral dimension",rows[-1]["mean_ds"],"4 +/- .02",e<.02);ck("spectral UV correction decreases",e,"< block1 error",e<abs(rows[0]["mean_ds"]-4))
    return {"scope":"conditional 4D scaffold, not dimension emergence","rows":rows}
def dispersion(scales=(1,2,4,8),L=512):
    rows=[];means=[]
    for b in scales:
        ks=[];ws=[];er=[]
        for n in range(1,max(1,L//(8*b))+1):
            for m in ((1,0,0,0),(1,1,0,0),(1,1,1,0),(1,1,1,1)):
                k=2*np.pi*n*np.asarray(m,float)/L;k2=float(k@k);la=float(np.sum(4*np.sin(k/2)**2));er.append(abs(la-k2)/k2);ks.append(math.sqrt(k2));ws.append(math.sqrt(la))
        z=float(np.polyfit(np.log(ks),np.log(ws),1)[0]);means.append(float(np.mean(er)));rows.append({"block":b,"mean_error":means[-1],"max_error":float(np.max(er)),"z":z})
    p=pexp(scales,means);ck("dispersion error exponent",p,"~2",1.75<p<2.15);ck("far dispersion mean error",means[-1],"<5e-4",means[-1]<5e-4);ck("far z",rows[-1]["z"],"1 +/- .01",abs(rows[-1]["z"]-1)<.01)
    return {"rows":rows,"error_exponent":p}
def levi(n):
    e=np.zeros((n,)*n)
    for p in itertools.permutations(range(n)):e[p]=-1 if sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))%2 else 1
    return e
E3,E4=levi(3),levi(4);TP=[(i,j) for i in range(4) for j in range(i+1,4)]
def wedge(a,b):return np.outer(a,b)-np.outer(b,a)
def selfdual():
    e=np.eye(4);B=np.zeros((3,4,4))
    for i in range(3):
        B[i]+=wedge(e[0],e[i+1])
        for j in range(3):
            for k in range(3):B[i]+=.5*E3[i,j,k]*wedge(e[j+1],e[k+1])
    return B
SIG=selfdual();BASE=np.array([[SIG[a,i,j] for i,j in TP] for a in range(3)])
def makeB(c):
    B=np.zeros((3,4,4))
    for a in range(3):
        for q,(i,j) in enumerate(TP):B[a,i,j]=c[a,q];B[a,j,i]=-c[a,q]
    return B
def simp(B):
    X=.25*np.einsum("abcd,iab,jcd->ij",E4,B,B);T=np.eye(3)*np.trace(X)/3;return float(np.linalg.norm(X-T)/max(np.linalg.norm(X),1e-30))
def urb(B):U=np.einsum("ijk,abcd,ima,jbc,kdn->mn",E3,E4,B,B,B);return .5*(U+U.T)
def normdet(M):return M/abs(float(np.linalg.det(M)))**.25
def uerr(U):a=normdet(U);b=np.eye(4);return float(min(np.linalg.norm(a-b),np.linalg.norm(a+b))/2)
def bfield(seed=260814,L=24,eta=.35,scales=(1,2,4,8)):
    rng=np.random.default_rng(seed);bits=rng.choice(np.array([-1,1],np.int8),(18,L,L,L,L));ss=[];uu=[];rows=[]
    for b in scales:
        av=block(bits,b).reshape(18,-1);ids=np.linspace(0,av.shape[1]-1,min(128,av.shape[1]),dtype=int);sv=[];uv=[]
        for k in ids:
            B=makeB(BASE+eta*av[:,k].reshape(3,6))
            try:sv.append(simp(B));uv.append(uerr(urb(B)))
            except Exception:pass
        ss.append(float(np.mean(sv)));uu.append(float(np.mean(uv)));rows.append({"block":b,"samples":len(sv),"simplicity":ss[-1],"urbantke_metric_error":uu[-1]})
    ps,pu=pexp(scales,ss,1),pexp(scales,uu,1);ck("simplicity smoothing exponent",ps,"~2",1.65<ps<2.35);ck("Urbantke smoothing exponent",pu,"~2",1.65<pu<2.45);ck("far simplicity",ss[-1],"<.02",ss[-1]<.02);ck("far Urbantke error",uu[-1],"<.02",uu[-1]<.02)
    return {"seed":seed,"eta":eta,"rows":rows,"exponents":{"simplicity":ps,"urbantke":pu},"scope":"binary noise around simple self-dual background; not a derivation of simplicity"}
def diamond(g=5):
    edges=[(0,1)];nxt=2;rows=[];prev=None;vals=None
    for gen in range(1,g+1):
        ne=[]
        for u,v in edges:
            ms=range(nxt,nxt+2);nxt+=2
            for m in ms:ne.extend(((u,m),(m,v)))
        edges=ne
        if gen>=2:
            A=np.zeros((nxt,nxt))
            for u,v in edges:A[u,v]=A[v,u]=1
            deg=A.sum(1);inv=np.where(deg>0,1/np.sqrt(deg),0);vals=np.linalg.eigvalsh(np.eye(nxt)-inv[:,None]*A*inv[None,:]);dh=None if prev is None else math.log(nxt/prev,2);rows.append({"generation":gen,"nodes":nxt,"dH":dh,"gap":float(vals[1])});prev=nxt
    t=np.geomspace(.5,40,160);v=ds(t,np.array([np.exp(-x*vals).mean() for x in t]));m=(t>=6)&(t<=12);dsm=float(v[m].mean());dh=float(rows[-1]["dH"]);ck("binary diamond fails 4D",max(abs(dsm-4),abs(dh-4)),"null fail",abs(dsm-4)>1 and abs(dh-4)>1);ck("binary diamond near 2D",dsm,"1.8..2.3",1.8<dsm<2.3)
    return {"rule":"edge -> two two-step paths -> reconvergence","rows":rows,"spectral_dimension":dsm,"conclusion":"binary reconvergence alone ~2D; smoothing is not a 4D derivation"}
def triad_sample(rng):
    while True:
        e=np.eye(3)+.35*rng.normal(size=(3,3))
        if np.linalg.det(e)>.15 and np.linalg.cond(e)<12:break
    K=rng.normal(size=(3,3));return e,.5*(K+K.T)
def lp(e,K,beta):
    q=e@e.T;qi=np.linalg.inv(q);sq=float(np.linalg.det(e));ei=np.linalg.inv(e).T;E=sq*ei;Ka=K@ei;F=beta**2*np.einsum("klm,al,bm->abk",E3,Ka,Ka);HE=float(np.einsum("ijk,ai,bj,abk",E3,E,E,F)/sq);t1=float(np.einsum("ai,bj,ai,bj->",E,E,Ka,Ka));t2=float(np.einsum("bi,aj,ai,bj->",E,E,Ka,Ka));HL=float(-(1+beta**2)*(t1-t2)/sq);Kup=qi@K@qi;HD=float(sq*(np.einsum("ab,ab->",K,Kup)-np.einsum("ab,ab->",qi,K)**2));return HE,HL,HD
def beta_gate(seed=260809):
    rng=np.random.default_rng(seed);mx=0
    for _ in range(32):
        e,K=triad_sample(rng)
        for b in (0,.2,1/np.sqrt(3),1,2,5):
            HE,HL,HD=lp(e,K,float(b));s=max(abs(HD),1e-14);mx=max(mx,abs(HE+HL-HD)/s,abs(HE+b*b*HD)/s,abs(HL-(1+b*b)*HD)/s)
    ck("Lorentzian beta cancellation",mx,"<2e-11",mx<2e-11);return {"max_relative_error":float(mx),"identity":"H_E^kin+H_L^corr=H_DW","scope":"classical kinetic identity, not quantum HDA"}
def run():
    global CHECKS;CHECKS=[]
    sec={"observer_metric_smoothing":metric_smoothing(),"visible_dispersion":dispersion(),"observer_spectral_dimension":spectral(),"dimension_blind_null":diamond(),"B_to_Urbantke":bfield(),"Lorentzian_beta":beta_gate()}
    return {"model":"observer-dependent coarse graining of binary Planck spacetime","observer_map":"ell_obs=sqrt(ell_P^2+(theta r)^2); dyadic b=2^floor(log2(ell_obs/ell_P))","checks_total":len(CHECKS),"checks_passed":sum(x["passed"] for x in CHECKS),"all_passed":all(x["passed"] for x in CHECKS),"checks":CHECKS,"sections":sec,"scope":{"supported":"conditional 4D binary fluctuations self-average in the observer-accessible IR","not_proved":"dimension emergence or full microscopic quantum HDA"}}
def md(o):
    m=o["sections"]["observer_metric_smoothing"];u=o["sections"]["B_to_Urbantke"];d=o["sections"]["observer_spectral_dimension"];n=o["sections"]["dimension_blind_null"];v=o["sections"]["visible_dispersion"]
    s=["# Observer-scale smoothing of binary Planck spacetime","",f"Checks: **{o['checks_passed']}/{o['checks_total']}**","","$$\\ell_{obs}=\\sqrt{\\ell_P^2+(\\theta r)^2},\\qquad b=2^{\\lfloor\\log_2(\\ell_{obs}/\\ell_P)\\rfloor}.$$\1".replace("\1",""),"","This is an observer-resolution map, not a claim that distance itself dynamically changes spacetime.","","## Measured finite scaling","",f"- metric noise exponent: **{m['exponents']['metric_noise']:.6f}**",f"- gradient roughness exponent: **{m['exponents']['gradient']:.6f}**",f"- linear curvature-noise exponent: **{m['exponents']['curvature']:.6f}**",f"- simplicity exponent: **{u['exponents']['simplicity']:.6f}**",f"- Urbantke metric-error exponent: **{u['exponents']['urbantke']:.6f}**",f"- visible dispersion-error exponent: **{v['error_exponent']:.6f}**",f"- far conditional 4D spectral dimension: **{d['rows'][-1]['mean_ds']:.8f}**",f"- dimension-blind binary diamond spectral dimension: **{n['spectral_dimension']:.8f}**","","## Interpretation","","In a 4D block, $N=b^4$ independent zero-mean bits give RMS fluctuations $N^{-1/2}=b^{-2}$. Physical derivatives add inverse block lengths, giving the observed $b^{-3}$ gradient and $b^{-4}$ linear-curvature laws. The separate dimension-blind null remains near 2D, so this is a continuumisation mechanism, not a derivation of 3+1 dimensions.","","| check | value | target | status |","|---|---:|---|---|"]
    for x in o["checks"]:s.append(f"| {x['name']} | `{x['value']}` | {x['target']} | {'PASS' if x['passed'] else 'FAIL'} |")
    return "\n".join(s)+"\n"
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",type=Path,default=Path("verification_results/OBSERVER_SMOOTHING_RESULTS.json"));ap.add_argument("--report",type=Path,default=Path("OBSERVER_SCALE_SMOOTHING.md"));a=ap.parse_args();o=run();a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(o,indent=2,ensure_ascii=False)+"\n",encoding="utf-8");a.report.write_text(md(o),encoding="utf-8");print(json.dumps(o,indent=2,ensure_ascii=False));return 0 if o["all_passed"] else 2
if __name__=="__main__":raise SystemExit(main())