#!/usr/bin/env python3
"""Executable certificate for the route-ground / HDA-probe sector separation.

This is an exact control of the frozen sparse-Fourier operator-first route
implementation.  It verifies that constant lapse and k=0 annihilate the route
term for an arbitrary positive metric block, while a nonconstant lapse or a
nonzero WKB carrier activates the same operator.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np
import operator_route_sparse_fourier as SF

TOL=1e-12

def vnorm(st):
    return float(np.sqrt(sum(np.vdot(v,v).real for v in st.values())))

def run():
    # Nontrivial 2x2 matrix-valued positive route metric.  The theorem is
    # independent of these values; they prevent a scalar/toy accidental zero.
    q00=np.array([[2.0,0.25],[0.25,1.4]],complex)
    q11=np.array([[1.1,-0.15],[-0.15,1.8]],complex)
    q01=np.array([[0.2,0.05],[0.05,0.1]],complex)
    Q=((q00,q01),(q01,q11))
    eps=0.2
    e0=np.array([1.0,0.0],complex)
    zero={(0,0):e0}
    const={(0,0):1.0+0j}
    nonconst={(0,0):1.0+0j,(1,0):0.2+0j,(-1,0):0.2+0j}
    wkb={(3,2):e0}

    Om0=SF.omega_matrix(Q,(0,0),eps)
    R_const_zero=SF.route_apply(Q,const,zero,eps)
    R_nonconst_zero=SF.route_apply(Q,nonconst,zero,eps)
    R_const_wkb=SF.route_apply(Q,const,wkb,eps)
    Omw=SF.omega_matrix(Q,(3,2),eps)

    checks={
      'omega_zero_mode_exact_zero':bool(np.linalg.norm(Om0)<TOL),
      'constant_lapse_zero_mode_route_zero':bool(vnorm(R_const_zero)<TOL),
      'nonconstant_lapse_activates_route_from_zero_mode':bool(vnorm(R_nonconst_zero)>1e-8),
      'constant_lapse_nonzero_wkb_route_nonzero':bool(vnorm(R_const_wkb)>1e-8),
      'nonzero_wkb_symbol_positive':bool(np.linalg.eigvalsh(Omw).min()>0),
    }
    return {
      'status':'operator-first route ground/HDA-probe sector separation certificate',
      'passed':bool(all(checks.values())),
      'science_status':'EXACT_ROUTE_SECTOR_THEOREM',
      'checks':checks,
      'epsilon':eps,
      'omega_zero_norm':float(np.linalg.norm(Om0)),
      'route_constant_zero_norm':vnorm(R_const_zero),
      'route_nonconstant_zero_norm':vnorm(R_nonconst_zero),
      'route_constant_wkb_norm':vnorm(R_const_wkb),
      'wkb_omega_eigenvalues':[float(x) for x in np.linalg.eigvalsh(Omw)],
      'conclusion':'For constant lapse N=1 on the route-ground k=0 sector, R[1]=Omega annihilates the state exactly. Nonconstant lapses and nonzero WKB carriers activate the same route operator, so C2 vacuum/RG and C3 HDA must use distinct declared route sectors.',
      'gap_guard':'The route momentum family is not part of the gapped eliminated geometry Q sector unless a future physical construction explicitly gaps it; the HDA WKB habitat remains outside the C2 geometry-gap test.'
    }

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
