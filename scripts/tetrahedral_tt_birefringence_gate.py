#!/usr/bin/env python3
"""Exact TT projection of the unique tetrahedral E/T2 spin-2 splitter.

Checks the high-symmetry spectra and the identity

  (1/2) Tr_TT Q_tet(n) = (1/4) [sum_i n_i^4 - 3/5]

without any microscopic coefficient or external physics input.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import numpy as np

TOL=2e-13


def qop(h):
    d=np.diag(np.diag(h))
    o=h-d
    return (3.0/5.0)*d-(2.0/5.0)*o


def normalize(v):
    v=np.asarray(v,float)
    return v/np.linalg.norm(v)


def tt_basis(n):
    n=normalize(n)
    axes=np.eye(3)
    seed=min(axes,key=lambda a:abs(float(a@n)))
    p=seed-n*(seed@n);p=normalize(p)
    q=np.cross(n,p);q=normalize(q)
    ep=(np.outer(p,p)-np.outer(q,q))/np.sqrt(2.0)
    ex=(np.outer(p,q)+np.outer(q,p))/np.sqrt(2.0)
    return ep,ex


def proj(n):
    basis=tt_basis(n)
    M=np.asarray([[np.trace(a.T@qop(b)) for b in basis] for a in basis],float)
    M=(M+M.T)/2
    ev=np.linalg.eigvalsh(M)[::-1]
    nn=normalize(n)
    q4=float(np.sum(nn**4)-3.0/5.0)
    return M,ev,q4


def run():
    targets={
      '100':np.asarray([3/5,-2/5],float),
      '110':np.asarray([7/20,-2/5],float),
      '111':np.asarray([-1/15,-1/15],float),
    }
    dirs={'100':(1,0,0),'110':(1,1,0),'111':(1,1,1)}
    rows={};max_spec=0.0;max_trace=0.0
    for name,n in dirs.items():
        M,ev,q4=proj(n)
        targ=np.sort(targets[name])[::-1]
        spec=float(np.max(np.abs(ev-targ)));max_spec=max(max_spec,spec)
        tr=float(abs(0.5*np.trace(M)-0.25*q4));max_trace=max(max_trace,tr)
        rows[name]={
          'direction':list(n),'QTT_matrix':M.tolist(),'eigenvalues_desc':ev.tolist(),
          'target_eigenvalues_desc':targ.tolist(),'spectrum_max_abs_error':spec,
          'Q4_cub':q4,'half_TT_trace':float(0.5*np.trace(M)),
          'quarter_Q4':float(0.25*q4),'trace_identity_abs_error':tr,
          'polarization_split':float(ev[0]-ev[1]),
        }
    # Random-direction identity is a stronger test than the three symmetry axes.
    rng=np.random.default_rng(260817);random_rows=[]
    for _ in range(128):
        n=rng.normal(size=3);M,ev,q4=proj(n);err=float(abs(0.5*np.trace(M)-0.25*q4));max_trace=max(max_trace,err)
        random_rows.append({'n':normalize(n).tolist(),'error':err})
    checks={
      'high_symmetry_spectra_exact':max_spec<TOL,
      'TT_trace_equals_Q4_over_4':max_trace<TOL,
      'birefringence_ratio_4_3_0':abs(rows['100']['polarization_split']-1)<TOL and abs(rows['110']['polarization_split']-0.75)<TOL and abs(rows['111']['polarization_split'])<TOL,
    }
    return {
      'status':'exact tetrahedral spin-2 TT birefringence theorem',
      'passed':bool(all(checks.values())),'science_status':'EXACT_TT_REPRESENTATION_THEOREM',
      'normalization':'Q_tet=(3/5)P_E-(2/5)P_T2',
      'rows':rows,'max_spectrum_abs_error':max_spec,'max_trace_identity_abs_error':max_trace,
      'zeta_gamma_relation':'zeta4 = gamma4/4',
      'high_symmetry_Delta_e_in_zeta_units':{'100':4.0,'110':3.0,'111':0.0},
      'checks':checks,
      'scope_note':'Representation/TT kinematics only. The measured local 0.08430036 tangent ratio is not inserted as gamma4_IR.'
    }


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();o=run();t=json.dumps(o,indent=2);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1

if __name__=='__main__':raise SystemExit(main())
