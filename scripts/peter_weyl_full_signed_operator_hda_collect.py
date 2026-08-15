#!/usr/bin/env python3
"""Final collector for the full signed G + operator-first route HDA.

Inputs are two independently computed exact artifacts:

1. full_geometry_optimized/SIGNED.npz = [G0,G1]|psi> with
       G_v=(-2/3)E_v+(32 i/9)L_raw,v;
2. full_signed_geometry_route_cross/{RESULT,CROSS,ROUTE_RESIDUAL,D}_eps
   containing [R_N,R_M]+D and the exact full GxR cross.

For each frozen epsilon, assemble

    residual = ([R_N,R_M] + D)
             + C_GxR
             + (a*d-b*c) [G0,G1],

using the same node lapse weights and HDA acceptance windows preregistered for
the physical sine two-node gate.  No channel normalization, subtraction or
post-hoc fit is allowed.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

EPS=(0.25,0.125,0.0625,0.03125,0.015625)
CARRIER=8
TOL=1e-12


def load_gauss(path):
    z=np.load(path,allow_pickle=False); out={}
    for spins,Ks,amp in zip(z['spins'],z['Ks'],z['amp']):
        c=complex(amp)
        if abs(c)>TOL:
            out[(tuple(int(x) for x in spins),tuple(int(x) for x in Ks))]=c
    return out


def load_global(path):
    z=np.load(path,allow_pickle=False); out={}
    for spins,Ks,mode,amp in zip(z['spins'],z['Ks'],z['modes'],z['amp']):
        c=complex(amp)
        if abs(c)<=TOL: continue
        key=(tuple(int(x) for x in spins),tuple(int(x) for x in Ks))
        md=(int(mode[0]),int(mode[1]))
        out.setdefault(key,{})[md]=out.setdefault(key,{}).get(md,0j)+c
    return out


def add_global(dst,src,scale=1.0,tol=TOL):
    for key,modes in src.items():
        d=dst.setdefault(key,{})
        for mode,amp in modes.items():
            z=d.get(mode,0j)+scale*amp
            if abs(z)>tol: d[mode]=z
            elif mode in d: del d[mode]
        if not d: dst.pop(key,None)
    return dst


def norm2(s): return float(sum(abs(a)**2 for modes in s.values() for a in modes.values()))
def norm(s): return math.sqrt(norm2(s))


def gauss_to_global(s,mode,scale=1.0):
    return {k:{mode:scale*a} for k,a in s.items() if abs(scale*a)>TOL}


def fit(vals):
    return float(np.polyfit(np.log(np.asarray(EPS,float)),np.log(np.asarray(vals,float)),1)[0])


def decreasing(vals): return all(b<a for a,b in zip(vals,vals[1:]))


def save_global(path,state):
    rows=[]
    for key,modes in state.items():
        for mode,amp in modes.items(): rows.append((key,mode,amp))
    rows.sort(key=lambda x:(repr(x[0]),x[1]))
    if rows:
        spins=np.asarray([r[0][0] for r in rows],np.int16)
        Ks=np.asarray([r[0][1] for r in rows],np.int16)
        modes=np.asarray([r[1] for r in rows],np.int32)
        amp=np.asarray([r[2] for r in rows],np.complex128)
    else:
        spins=np.zeros((0,10),np.int16); Ks=np.zeros((0,5),np.int16); modes=np.zeros((0,2),np.int32); amp=np.zeros((0,),np.complex128)
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    np.savez_compressed(path,spins=spins,Ks=Ks,modes=modes,amp=amp)


def run(geometry_dir,route_dir,output_dir,carrier=CARRIER):
    gd=Path(geometry_dir); rd=Path(route_dir); od=Path(output_dir); od.mkdir(parents=True,exist_ok=True)
    geom_meta=json.loads((gd/'RESULT.json').read_text(encoding='utf-8'))
    route_meta=json.loads((rd/'RESULT.json').read_text(encoding='utf-8'))
    signed=load_gauss(gd/'SIGNED.npz')
    if not geom_meta.get('passed',False): raise RuntimeError('full signed geometry artifact did not pass')
    if not route_meta.get('passed',False): raise RuntimeError('full GxR route artifact did not pass')

    route_rows={float(r['epsilon']):r for r in route_meta['rows']}
    mode=(int(carrier),int(carrier-1))
    rows=[]; route_vals=[]; cross_vals=[]; gg_vals=[]; joint_vals=[]

    for eps in EPS:
        tag=str(eps).replace('.','p')
        rr=route_rows[eps]
        cross=load_global(rd/f'CROSS_{tag}.npz')
        route_res=load_global(rd/f'ROUTE_RESIDUAL_{tag}.npz')
        D=load_global(rd/f'D_{tag}.npz')
        Dn=norm(D)
        smear=float(rr['antisymmetric_geometry_smear'])
        gg=gauss_to_global(signed,mode,smear)
        residual={}; add_global(residual,route_res,+1); add_global(residual,cross,+1); add_global(residual,gg,+1)

        route_ratio=norm(route_res)/max(Dn,1e-30)
        cross_ratio=norm(cross)/max(Dn,1e-30)
        gg_ratio=norm(gg)/max(Dn,1e-30)
        joint=norm(residual)/max(Dn,1e-30)
        route_vals.append(route_ratio); cross_vals.append(cross_ratio); gg_vals.append(gg_ratio); joint_vals.append(joint)
        row={
            'epsilon':eps,'antisymmetric_geometry_smear':smear,'D_norm':Dn,
            'route_only_defect':route_ratio,'cross_over_D':cross_ratio,
            'pure_GG_over_D':gg_ratio,'joint_defect_over_D':joint,
            'route_residual_support':len(route_res),'cross_support':len(cross),
            'GG_support':len(gg),'joint_support':len(residual),
        }
        rows.append(row); save_global(od/f'FULL_RESIDUAL_{tag}.npz',residual)
        print(json.dumps(row,sort_keys=True),flush=True)

    p_cross=fit(cross_vals); p_gg=fit(gg_vals); p_joint=fit(joint_vals)
    checks={
        'geometry_input_passed':bool(geom_meta.get('passed',False)),
        'route_cross_input_passed':bool(route_meta.get('passed',False)),
        'route_endpoint':route_vals[-1]<1e-4,
        'cross_exponent':0.75<=p_cross<=1.25,
        'GG_exponent':1.75<=p_gg<=2.25,
        'joint_exponent':0.75<=p_joint<=1.25,
        'cross_strictly_decreasing':decreasing(cross_vals),
        'GG_strictly_decreasing':decreasing(gg_vals),
        'joint_strictly_decreasing':decreasing(joint_vals),
        'joint_endpoint':joint_vals[-1]<0.05,
        'no_channel_dependent_normalization':True,
        'no_posthoc_subtraction':True,
    }
    out={
        'status':'final full signed H_E^sine+(1+beta^2)H_L+R_operator-first two-node HDA verdict',
        'passed':all(checks.values()),
        'beta':1.0,'hbar':1.0,'carrier':carrier,'epsilons':list(EPS),
        'geometry_formula':'G_v=(-2/3)E_v+(32 i/9)L_raw,v',
        'assembly':'([R_N,R_M]+D) + C_GxR + (a*d-b*c)[G0,G1]',
        'rows':rows,
        'fitted_cross_exponent':p_cross,
        'fitted_pure_GG_relative_exponent':p_gg,
        'fitted_joint_exponent':p_joint,
        'last_route_only_defect':route_vals[-1],
        'last_cross_over_D':cross_vals[-1],
        'last_pure_GG_over_D':gg_vals[-1],
        'last_joint_defect_over_D':joint_vals[-1],
        'checks':checks,
        'scope':'One frozen two-node off-shell sparse-Fourier habitat/probe with upstream-fixed signed coefficients and no channel refit. PASS advances the frontier to independent habitats and joint-cutoff strengthening; FAIL is retained as the channel-resolved falsifier.',
    }
    (od/'FINAL_HDA_RESULT.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--geometry-dir',type=Path,required=True)
    p.add_argument('--route-dir',type=Path,required=True)
    p.add_argument('--output-dir',type=Path,required=True)
    p.add_argument('--carrier',type=int,default=CARRIER)
    a=p.parse_args(); out=run(a.geometry_dir,a.route_dir,a.output_dir,a.carrier); print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if out['passed'] else 1

if __name__=='__main__': raise SystemExit(main())
