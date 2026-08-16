#!/usr/bin/env python3
"""Preregistered AND-gate for BCQG collective GR universality.

A science PASS requires direct BCQG measurements on >=4 increasing refinement
levels. Classical ADM/DeWitt target controls and PL topology controls are kept
separate and can never fill missing BCQG fields.

Required per-level direct fields:
  level, epsilon, D_space_metric,
  either c_DeWitt_eff or kinetic_hessian_sym6,
  r_G, r_D, r_H, r_extra, r_secondclass,
  delta_HH_collective.

The sym6 Hessian convention is the orthonormal basis
(xx, yy, zz, sqrt(2)xy, sqrt(2)xz, sqrt(2)yz). For an isotropic ADM kinetic
quadratic form A(pi:pi-c tr(pi)^2), the Hessian has traceless eigenvalue 2A and
trace eigenvalue 2A(1-3c), hence c=(1-lambda_trace/lambda_TL)/3. This extracts
c without fixing it to 1/2.
"""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import numpy as np

CRITERIA={
 'minimum_levels':4,
 'D_space_abs_error_max':0.10,
 'c_DeWitt_abs_error_max':0.05,
 'kinetic_traceless_anisotropy_max':0.05,
 'rank_target':{'r_G':3,'r_D':3,'r_H':1,'r_extra':0,'r_secondclass':0},
 'N_phys_target':2.0,
 'delta_HH_finest_max':0.05,
 'delta_HH_power_min':0.50,
}


def sym6_c_from_hessian(raw):
    H=np.asarray(raw,dtype=float)
    if H.shape!=(6,6):
        raise ValueError('kinetic_hessian_sym6 must be 6x6')
    H=.5*(H+H.T)
    t=np.array([1,1,1,0,0,0],float)/math.sqrt(3)
    _,_,Vh=np.linalg.svd(t.reshape(1,6))
    B=Vh[1:].T
    Htl=B.T@H@B
    evals=np.linalg.eigvalsh(Htl)
    lam_t=float(t@H@t)
    lam_tl=float(np.mean(evals))
    if abs(lam_tl)<1e-14:
        raise ValueError('degenerate traceless kinetic Hessian')
    c=(1-lam_t/lam_tl)/3
    anis=float(np.std(evals)/max(abs(lam_tl),1e-30))
    mix=float(np.linalg.norm(B.T@H@t)/max(abs(lam_tl),1e-30))
    return {
      'c_DeWitt_eff':float(c),
      'trace_eigenvalue':lam_t,
      'traceless_eigenvalue_mean':lam_tl,
      'traceless_anisotropy':anis,
      'trace_traceless_mixing':mix,
      'traceless_eigenvalues':evals.tolist()
    }


def power_fit(eps,vals):
    x=np.asarray(eps,float); y=np.asarray(vals,float)
    mask=(x>0)&(y>0)&np.isfinite(x)&np.isfinite(y)
    if mask.sum()<3:
        return None
    p,b=np.polyfit(np.log(x[mask]),np.log(y[mask]),1)
    pred=p*np.log(x[mask])+b
    ssr=float(np.sum((np.log(y[mask])-pred)**2))
    sst=float(np.sum((np.log(y[mask])-np.mean(np.log(y[mask])))**2))
    r2=1-ssr/max(sst,1e-30)
    return {'power':float(p),'r2':float(r2),'prefactor':float(math.exp(b))}


def nonworsening(errors):
    if len(errors)<4:
        return False
    return float(np.mean(errors[-2:])) <= float(np.mean(errors[:2]))+1e-15


def analyze_levels(levels):
    levels=sorted(levels,key=lambda r:r['level'])
    complete_fields=[]; processed=[]
    for r0 in levels:
        r=dict(r0)
        if 'c_DeWitt_eff' not in r and 'kinetic_hessian_sym6' in r:
            r.update(sym6_c_from_hessian(r['kinetic_hessian_sym6']))
        required=['level','epsilon','D_space_metric','c_DeWitt_eff',
                  'r_G','r_D','r_H','r_extra','r_secondclass',
                  'delta_HH_collective']
        missing=[k for k in required if k not in r]
        r['missing_fields']=missing
        if not missing:
            rf=r['r_G']+r['r_D']+r['r_H']+r['r_extra']
            r['N_phys_config']=(18-2*rf-r['r_secondclass'])/2
            complete_fields.append(True)
        else:
            complete_fields.append(False)
        processed.append(r)
    if len(processed)<CRITERIA['minimum_levels'] or not all(complete_fields):
        return {
          'science_status':'INCOMPLETE','science_passed':False,
          'levels':processed,
          'missing_reason':'Need >=4 direct BCQG refinement levels with every required measurement; target controls do not substitute for them.'
        }

    finest=processed[-1]; last2=processed[-2:]
    D_err=[abs(r['D_space_metric']-3) for r in processed]
    c_err=[abs(r['c_DeWitt_eff']-.5) for r in processed]
    rank_ok=lambda r: all(int(r[k])==v for k,v in CRITERIA['rank_target'].items())
    hh=power_fit([r['epsilon'] for r in processed],
                 [r['delta_HH_collective'] for r in processed])
    checks={
      'D_space_to_3':bool(D_err[-1]<=CRITERIA['D_space_abs_error_max'] and nonworsening(D_err)),
      'c_DeWitt_to_half':bool(c_err[-1]<=CRITERIA['c_DeWitt_abs_error_max'] and nonworsening(c_err)),
      'constraint_ranks_GR':bool(all(rank_ok(r) for r in last2)),
      'N_phys_to_2':bool(all(abs(r['N_phys_config']-2)<=1e-12 for r in last2)),
      'Delta_HH_collective_to_0':bool(hh is not None and hh['power']>=CRITERIA['delta_HH_power_min'] and finest['delta_HH_collective']<CRITERIA['delta_HH_finest_max']),
    }
    hrows=[r for r in last2 if 'traceless_anisotropy' in r]
    if hrows:
        checks['kinetic_Hessian_isotropic_guard']=bool(all(
            r['traceless_anisotropy']<=CRITERIA['kinetic_traceless_anisotropy_max'] and
            r['trace_traceless_mixing']<=CRITERIA['kinetic_traceless_anisotropy_max']
            for r in hrows))
    passed=all(checks.values())
    return {
      'science_status':'PASS' if passed else 'FAIL',
      'science_passed':bool(passed),'checks':checks,
      'D_errors':D_err,'c_errors':c_err,'HH_power_fit':hh,
      'levels':processed
    }


def hessian_for(A,c):
    u=np.array([1,1,1,0,0,0.],float)
    return (2*A*(np.eye(6)-c*np.outer(u,u))).tolist()


def self_test():
    levels=[]
    for l in range(4):
        e=2.0**(-l)
        levels.append({
          'level':l,'epsilon':e,'D_space_metric':3+.08*e,
          'kinetic_hessian_sym6':hessian_for(1.3,.5+.02*e),
          'r_G':3,'r_D':3,'r_H':1,'r_extra':0,'r_secondclass':0,
          'delta_HH_collective':.04*e**.9
        })
    pos=analyze_levels(levels)
    bad=json.loads(json.dumps(levels)); bad[-1]['r_extra']=1
    neg=analyze_levels(bad)
    return {
      'positive_control_passed':pos['science_passed'],
      'negative_control_rejected':not neg['science_passed'],
      'positive':pos,'negative':neg,
      'passed':bool(pos['science_passed'] and not neg['science_passed'])
    }


def bootstrap(controls):
    return {
      'protocol':'BCQG collective GR universality AND-gate',
      'criteria':CRITERIA,'target_controls':controls,
      'direct_BCQG_measurements':[],
      **analyze_levels([]),
      'interpretation':'The refinement/topology and ADM/DeWitt controls can be green while the science verdict remains INCOMPLETE until direct collective BCQG level data exist.'
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input',type=Path,
                    help="JSON with {'levels':[...]} direct BCQG measurements")
    ap.add_argument('--bootstrap-controls',type=Path,
                    help='JSON summary of non-science target/topology controls')
    ap.add_argument('--self-test',action='store_true')
    ap.add_argument('--require-complete',action='store_true')
    ap.add_argument('--output',type=Path)
    a=ap.parse_args()
    if a.self_test:
        out={'mode':'self-test','criteria':CRITERIA,**self_test()}
    elif a.input:
        payload=json.loads(a.input.read_text(encoding='utf-8'))
        out={'mode':'direct','criteria':CRITERIA,
             **analyze_levels(payload.get('levels',[]))}
    else:
        controls={}
        if a.bootstrap_controls:
            controls=json.loads(a.bootstrap_controls.read_text(encoding='utf-8'))
        out={'mode':'bootstrap',**bootstrap(controls)}
    text=json.dumps(out,indent=2); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(text+'\n',encoding='utf-8')
    if a.self_test:
        return 0 if out['passed'] else 1
    if a.require_complete:
        return 0 if out.get('science_passed') else 1
    return 0

if __name__=='__main__':
    raise SystemExit(main())
