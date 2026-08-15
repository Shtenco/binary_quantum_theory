#!/usr/bin/env python3
"""Preregistered physical sine-ordering two-node Peter-Weyl x route HDA gate.

Preregistration:
  PETER_WEYL_TWO_NODE_SINE_HDA_PREREGISTRATION.md

This is the ordering-consistent successor to the historical plus-Hermitian
Euclidean two-node gate. It keeps the route/lapse/WKB/metric protocol fixed and
changes only

    H_plus=(T+T^dagger)/2

into the independently validated physical ordering

    H_sine=(T-T^dagger)/(2i).

No channel-dependent normalization or post-hoc subtraction is allowed.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_route_dressed_local_gate as LOCAL
import peter_weyl_euclidean_sine_ordering_gate as SINE
import peter_weyl_zeroaware_volume_migration_experiment as ZVM

PRUNE=1e-8


def shared_metric(key):
    q0=LOCAL.flux_gram2(key,0,1,2)
    q1=LOCAL.flux_gram2(key,1,1,2)
    return 0.5*(q0+q1)


def add_array(dst,key,arr):
    if key in dst:
        dst[key]=dst[key]+arr
    else:
        dst[key]=arr.copy()


def sparse_array_norm2(state):
    return float(sum(np.vdot(v,v).real for v in state.values()))


def Hsine(state,node,JMAX2=5):
    return PW.prune_state(SINE.safe_H_sine(state,node,JMAX2),PRUNE)


def compose_sine(state,target_v,JMAX2=5):
    out={}
    for key,amp in state.items():
        rr=Hsine({key:1+0j},target_v,JMAX2)
        for ko,c in rr.items():
            out[ko]=out.get(ko,0j)+amp*c
    return PW.prune_state(out,PRUNE)


def commutator_geometry(initial,JMAX2=5):
    psi0={initial:1+0j}
    h0=Hsine(psi0,0,JMAX2)
    h1=Hsine(psi0,1,JMAX2)
    h1h0=compose_sine(h0,1,JMAX2)
    h0h1=compose_sine(h1,0,JMAX2)
    comm={}
    PW.add_dict(comm,h0h1,+1)
    PW.add_dict(comm,h1h0,-1)
    return h0,h1,PW.prune_state(comm,PRUNE)


def analytic_node_weights(epsilon):
    def nvar(y,z):
        return 0.13*math.sin(y)+0.07*math.cos(z)
    def mvar(y,z):
        return 0.11*math.cos(y)+0.09*math.sin(z)
    a=0.9+epsilon*nvar(0.0,0.0)
    b=0.9+epsilon*nvar(1.0,0.0)
    c=1.1+epsilon*mvar(0.0,0.0)
    d=1.1+epsilon*mvar(1.0,0.0)
    return a,b,c,d


def one_epsilon(initial,h0,h1,geom_comm,metrics,epsilon,L=48,carrier=8):
    Y,Z,KY,KZ,dphys=LOCAL.spectral_setup(L,epsilon)
    N=0.9+epsilon*(0.13*np.sin(Y)+0.07*np.cos(Z))
    M=1.1+epsilon*(0.11*np.cos(Y)+0.09*np.sin(Z))
    f=np.exp(1j*(carrier*Y+(carrier-1)*Z))
    a,b,c,d=analytic_node_weights(epsilon)

    Q0=metrics[initial]
    RN0=LOCAL.route_apply(N,f,Q0,KY,KZ,epsilon)
    RM0=LOCAL.route_apply(M,f,Q0,KY,KZ,epsilon)
    RR=(LOCAL.route_apply(N,RM0,Q0,KY,KZ,epsilon)
        -LOCAL.route_apply(M,RN0,Q0,KY,KZ,epsilon))
    D=LOCAL.route_target(N,M,f,Q0,dphys)
    Dnorm=float(np.linalg.norm(D))

    route_residual=RR+D
    route_ratio=float(np.linalg.norm(route_residual)/max(Dnorm,1e-30))

    cross={}
    for ko,amp in h0.items():
        Qg=metrics[ko]
        RMg=LOCAL.route_apply(M,f,Qg,KY,KZ,epsilon)
        RNg=LOCAL.route_apply(N,f,Qg,KY,KZ,epsilon)
        val=amp*(a*(RM0-RMg)+c*(RNg-RN0))
        if np.linalg.norm(val)>1e-12:
            add_array(cross,ko,val)
    for ko,amp in h1.items():
        Qg=metrics[ko]
        RMg=LOCAL.route_apply(M,f,Qg,KY,KZ,epsilon)
        RNg=LOCAL.route_apply(N,f,Qg,KY,KZ,epsilon)
        val=amp*(b*(RM0-RMg)+d*(RNg-RN0))
        if np.linalg.norm(val)>1e-12:
            add_array(cross,ko,val)

    smear=a*d-b*c
    gg={}
    for ko,amp in geom_comm.items():
        val=(smear*amp)*f
        if np.linalg.norm(val)>1e-12:
            add_array(gg,ko,val)

    residual={initial:route_residual.copy()}
    for k,v in cross.items(): add_array(residual,k,v)
    for k,v in gg.items(): add_array(residual,k,v)

    return {
        'epsilon':epsilon,
        'node_lapse_weights':{'a_N0':a,'b_N1':b,'c_M0':c,'d_M1':d},
        'antisymmetric_geometry_smear':smear,
        'route_only_defect':route_ratio,
        'cross_over_D':math.sqrt(sparse_array_norm2(cross))/max(Dnorm,1e-30),
        'pure_GG_over_D':math.sqrt(sparse_array_norm2(gg))/max(Dnorm,1e-30),
        'joint_defect_over_D':math.sqrt(sparse_array_norm2(residual))/max(Dnorm,1e-30),
        'D_norm':Dnorm,
        'cross_support':len(cross),
        'GG_support':len(gg),
        'residual_support':len(residual),
    }


def fit_power(eps,vals):
    return float(np.polyfit(np.log(np.asarray(eps,float)),np.log(np.asarray(vals,float)),1)[0])


def strictly_decreasing(vals):
    return all(b<a for a,b in zip(vals,vals[1:]))


def run(L=48,carrier=8):
    ZVM.patch_and_clear()
    JMAX2=5
    initial=PW.basis_full_jhalf()[0]
    h0,h1,geom_comm=commutator_geometry(initial,JMAX2)
    h0norm=math.sqrt(PW.norm2_state(h0)); h1norm=math.sqrt(PW.norm2_state(h1))
    comm_norm=math.sqrt(PW.norm2_state(geom_comm))

    metric_keys={initial,*h0.keys(),*h1.keys()}
    metrics={key:shared_metric(key) for key in metric_keys}
    Q0=metrics[initial]
    eigmins=[float(np.linalg.eigvalsh(Q).min()) for Q in metrics.values()]

    eps=[0.25,0.125,0.0625,0.03125,0.015625]
    rows=[one_epsilon(initial,h0,h1,geom_comm,metrics,e,L,carrier) for e in eps]
    route=[r['route_only_defect'] for r in rows]
    cross=[r['cross_over_D'] for r in rows]
    gg=[r['pure_GG_over_D'] for r in rows]
    joint=[r['joint_defect_over_D'] for r in rows]
    p_cross=fit_power(eps,cross)
    p_gg=fit_power(eps,gg)
    p_joint=fit_power(eps,joint)

    checks={
        'H0_nonzero':len(h0)>0 and h0norm>1e-10,
        'H1_nonzero':len(h1)>0 and h1norm>1e-10,
        'GG_commutator_nonzero':len(geom_comm)>0 and comm_norm>1e-10,
        'route_endpoint':route[-1]<1e-4,
        'cross_exponent':0.75<=p_cross<=1.25,
        'GG_exponent':1.75<=p_gg<=2.25,
        'joint_exponent':0.75<=p_joint<=1.25,
        'cross_strictly_decreasing':strictly_decreasing(cross),
        'GG_strictly_decreasing':strictly_decreasing(gg),
        'joint_strictly_decreasing':strictly_decreasing(joint),
        'joint_endpoint':joint[-1]<0.05,
    }
    return {
        'status':'preregistered physical sine-ordering two-node Euclidean Peter-Weyl x route HDA gate',
        'passed':all(checks.values()),
        'preregistration':'PETER_WEYL_TWO_NODE_SINE_HDA_PREREGISTRATION.md',
        'euclidean_ordering':'H_sine=(T-T^dagger)/(2i)',
        'zeroaware_volume_convention':True,
        'state_prune_tolerance':PRUNE,
        'Jmax':2.5,
        'nodes':[0,1],
        'input':'all ten links j=1/2; all five K=0',
        'H0_support':len(h0),'H0_norm':h0norm,
        'H1_support':len(h1),'H1_norm':h1norm,
        'raw_sine_GG_commutator_support':len(geom_comm),
        'raw_sine_GG_commutator_norm':comm_norm,
        'shared_initial_Q':Q0.tolist(),
        'minimum_shared_metric_eigenvalue':min(eigmins),
        'L':L,'carrier':carrier,'rows':rows,
        'fitted_cross_exponent':p_cross,
        'fitted_pure_GG_relative_exponent':p_gg,
        'fitted_joint_exponent':p_joint,
        'last_route_only_defect':route[-1],
        'last_cross_over_D':cross[-1],
        'last_pure_GG_over_D':gg[-1],
        'last_joint_defect_over_D':joint[-1],
        'checks':checks,
        'exact_decomposition':'[H[N],H[M]]=[R_N,R_M]+C_cross+(ad-bc)[H0^sine,H1^sine]',
        'historical_plus_gate':'scripts/peter_weyl_two_node_euclidean_joint_gate.py',
        'scope_note':(
            'Physical sine-ordering Euclidean two-node off-shell scaling control on one frozen WKB route probe. '
            'No fitted channel normalization. It still does not include H_L amplitudes, multiple habitat probes, '
            'the full operator-valued flux metric or collective-spin scaling.'
        ),
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--L',type=int,default=48)
    ap.add_argument('--carrier',type=int,default=8)
    ap.add_argument('--output',type=Path)
    a=ap.parse_args(); out=run(a.L,a.carrier); text=json.dumps(out,indent=2); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__=='__main__': raise SystemExit(main())
