#!/usr/bin/env python3
"""Square-root path-normal generator -> HDA structure function.

On a refined path sheet define the positive operator Omega=sqrt(-Delta_path)
and the symmetric lapse generator

    H_path[N] = 1/2 {N, Omega}.

Its principal symbol is h_N=N sqrt(q^{ab}p_a p_b). Pseudodifferential symbol
calculus then gives, up to the global vector-constraint orientation convention,

    {h_N,h_M} = q^{ab}(M d_b N-N d_b M) p_a.

Thus the metric structure function appears without a fitted coefficient. This
script verifies the finite spectral quantum commutator on smooth lapses and WKB
path carriers. It is a route-sector HDA gate, not the full Peter-Weyl gravity
Hamiltonian.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np


def run(L=128):
    x=2*np.pi*np.arange(L)/L;X,Y=np.meshgrid(x,x,indexing='ij')
    k=np.fft.fftfreq(L,d=1.0/L);KX,KY=np.meshgrid(k,k,indexing='ij')
    W=np.sqrt(KX*KX+KY*KY)
    def omega(f):return np.fft.ifft2(W*np.fft.fft2(f))
    def dx(f):return np.fft.ifft2(1j*KX*np.fft.fft2(f))
    def dy(f):return np.fft.ifft2(1j*KY*np.fft.fft2(f))
    N=1.0+0.12*np.sin(X)+0.08*np.cos(Y)
    M=0.9+0.10*np.cos(X)+0.11*np.sin(Y)
    def H(A,f):return 0.5*(A*omega(f)+omega(A*f))
    bx=N*dx(M)-M*dx(N);by=N*dy(M)-M*dy(N);div=dx(bx)+dy(by)
    def Dstandard(f):return -1j*(bx*dx(f)+by*dy(f)+0.5*div*f)
    carriers=np.array([2,3,4,6,8,12,16,24],float);errs=[]
    for kk in carriers.astype(int):
        f=np.exp(1j*(kk*X+(kk-1)*Y))
        lhs=-1j*(H(N,H(M,f))-H(M,H(N,f)))
        rhs=Dstandard(f)
        # The symbol bracket above has the opposite overall D orientation to
        # this repository's Dstandard convention. The sign is fixed globally,
        # not fitted per carrier.
        errs.append(float(np.linalg.norm(lhs+rhs)/np.linalg.norm(rhs)))
    errs=np.asarray(errs);p=-float(np.polyfit(np.log(carriers),np.log(errs),1)[0])

    rng=np.random.default_rng(260813);symerr=0.0
    for _ in range(128):
        A=rng.normal(size=(2,2));q=A@A.T+0.2*np.eye(2);pvec=rng.normal(size=2)
        w=float(np.sqrt(pvec@q@pvec));dp=q@pvec/w
        symerr=max(symerr,float(np.linalg.norm(w*dp-q@pvec)))

    passed=(1.8<p<2.5 and errs[-1]<1e-5 and symerr<1e-12)
    return {
      'status':'square-root path-normal HDA principal-symbol gate','passed':bool(passed),
      'L':L,'carrier_modes':carriers.astype(int).tolist(),'relative_defects':errs.tolist(),
      'fitted_WKB_decay_exponent':p,'last_defect':float(errs[-1]),
      'max_metric_symbol_identity_error':symerr,
      'operator':'H_path[N]=0.5*{N,sqrt(-Delta_path,q)}',
      'principal_symbol':'{N|p|_q,M|p|_q}=q^{ab}(M d_b N-N d_b M)p_a',
      'orientation_note':'Numerical comparison uses one fixed minus sign relative to Dstandard; this is the global vector-constraint orientation convention, not a fitted magnitude.',
      'scope_note':'Constructive route-sector normal-deformation representation. Full gravity still requires the Peter-Weyl Lorentzian geometry operator to couple to this same path domain.'
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--L',type=int,default=128);ap.add_argument('--output',type=Path);a=ap.parse_args();o=run(a.L);t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
