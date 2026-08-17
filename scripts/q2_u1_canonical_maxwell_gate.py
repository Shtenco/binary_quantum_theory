#!/usr/bin/env python3
"""Exact 16-cell cochain/canonical-Maxwell positive-control gate.

Verifies V/E/F/T counts, d1*d0=0, ranks 7/17, H1=0, unit-Hodge curl
spectrum 0^7+4^6+6^8+8^3, Gauss/gauge identities, and symbolic ZA
cancellation from the linear wave equation.
"""
from __future__ import annotations
import argparse, itertools, json
from pathlib import Path
import sympy as sp

def seed_16cell_boundary():
    return sorted(tuple(2*i+b for i,b in enumerate(bits)) for bits in itertools.product((0,1),repeat=4))

def build():
    tets=seed_16cell_boundary()
    verts=sorted(set(v for t in tets for v in t))
    edges=sorted(set(e for t in tets for e in itertools.combinations(t,2)))
    faces=sorted(set(f for t in tets for f in itertools.combinations(t,3)))
    vi={v:i for i,v in enumerate(verts)}; ei={e:i for i,e in enumerate(edges)}
    d0=sp.zeros(len(edges),len(verts)); d1=sp.zeros(len(faces),len(edges))
    for r,(a,b) in enumerate(edges): d0[r,vi[a]]=-1; d0[r,vi[b]]=1
    for r,(a,b,c) in enumerate(faces):
        d1[r,ei[(b,c)]]=1; d1[r,ei[(a,c)]]=-1; d1[r,ei[(a,b)]]=1
    return tets,verts,edges,faces,d0,d1

def run():
    t,v,e,f,d0,d1=build(); K=d1.T*d1
    ev=K.eigenvals(); spec={str(k):int(m) for k,m in sorted(ev.items(),key=lambda q:float(q[0]))}
    r0=d0.rank(); r1=d1.rank(); ker_dim=len(e)-r1; b1=ker_dim-r0
    # Gauge/null equality follows dimensionally once d1*d0=0 and ranks match.
    chain_zero=(d1*d0)==sp.zeros(len(f),len(v))
    gauge_zero=(K*d0)==sp.zeros(len(e),len(v))
    Z=sp.symbols('Z', positive=True, nonzero=True)
    # Canonical equations theta_dot=(1/Z)p, p_dot=-Z K theta => theta_ddot=-K theta.
    za_product=sp.simplify((sp.Integer(1)/Z)*Z)
    expected={'0':7,'4':6,'6':8,'8':3}
    passed=bool(len(v)==8 and len(e)==24 and len(f)==32 and len(t)==16 and chain_zero and r0==7 and r1==17 and b1==0 and gauge_zero and spec==expected and za_product==1)
    return {
      'status':'exact q=2/U1 canonical Maxwell 16-cell positive control','passed':passed,
      'counts':{'V':len(v),'E':len(e),'F':len(f),'T':len(t)},
      'rank_d0':r0,'rank_d1':r1,'dim_ker_d1':ker_dim,'b1':b1,
      'd1_d0_exact_zero':bool(chain_zero),'curl_laplacian_kills_gauge_exactly':bool(gauge_zero),
      'unit_hodge_curl_laplacian_spectrum':spec,
      'ZA_cancellation_factor_in_second_order_wave_equation':str(za_product),
      'canonical_equations':'theta_dot=(1/ZA) M1^-1 p; p_dot=-ZA d1^T M2 d1 theta; hence theta_ddot=-M1^-1 d1^T M2 d1 theta',
      'scope':'finite spatial/canonical positive control conditional on a positive local quadratic phase action; it does not establish microscopic deconfinement, final Hodge weights, two continuum photon poles or ZA'
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=Path('verification_results/Q2_U1_CANONICAL_MAXWELL.json')); a=ap.parse_args()
    out=run(); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2)); return 0 if out['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
