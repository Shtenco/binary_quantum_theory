#!/usr/bin/env python3
"""Full signed spin-changing G x operator-first route cross on the two-node habitat.

For structural beta=hbar=1 use the already frozen local geometry generator

    G_v = a_E E_v + b_L L_raw,v,
    a_E=-2/3, b_L=+32 i/9.

The route sector is the positive operator-first spectral square root on complete
fixed-spin K0 x K1 blocks.  With frozen lapse functions N,M this gate evaluates
exactly on the initial all-j=1/2 K=0 carrier state

    C_cross = G_N R_M + R_N G_M - G_M R_N - R_M G_N,

where G_N=N_0 G_0 + N_1 G_1 and similarly for M.  R_op preserves fixed spin
sectors but mixes the complete K0 x K1 block, so the gate precomputes G0/G1 on
all four keys of the initial route sector.  R after G is then evaluated on every
genuine spin-changed output sector using the generic block engine.

The pure GG term is intentionally kept separate.  This gate returns exact RR,
D, route residual and GxR cross states for later assembly with the independently
computed signed [G0,G1].
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import time
from pathlib import Path

import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import k5_peter_weyl_safe_hda_column as PW
import operator_route_sparse_fourier as SF
import peter_weyl_full_geometry_superposition_optimized_gate as FG
import peter_weyl_logical_anisotropy_gate as ANISO
import peter_weyl_lorentzian_logical_projection_gate as LP
import peter_weyl_operator_route_block_engine as BLK
import peter_weyl_operator_route_block_gate as RBG
import peter_weyl_zeroaware_volume_migration_experiment as ZVM

EPS=(0.25,0.125,0.0625,0.03125,0.015625)
CARRIER=8
TOL=1e-12
A=FG.A
B=FG.B


def normg(s): return math.sqrt(BLK.global_norm2(s))


def gauss_norm(s): return math.sqrt(float(sum(abs(a)**2 for a in s.values())))


def add_gauss(dst,src,scale=1.0,tol=1e-10):
    for k,a in src.items():
        z=dst.get(k,0j)+scale*a
        if abs(z)>tol: dst[k]=z
        elif k in dst: del dst[k]


def combine_G(E,L):
    out={}; add_gauss(out,E,A); add_gauss(out,L,B); return out


def analytic_node_weights(epsilon):
    def nvar(y,z): return 0.13*math.sin(y)+0.07*math.cos(z)
    def mvar(y,z): return 0.11*math.cos(y)+0.09*math.sin(z)
    return (
        0.9+epsilon*nvar(0.0,0.0),
        0.9+epsilon*nvar(1.0,0.0),
        1.1+epsilon*mvar(0.0,0.0),
        1.1+epsilon*mvar(1.0,0.0),
    )


def precompute_G_columns(initial_sector):
    basis=BLK.sector_basis(initial_sector)
    if len(basis)!=4:
        raise RuntimeError(f'frozen initial route sector must have dimension 4, got {len(basis)}')
    columns={0:{},1:{}}; diagnostics={0:[],1:[]}
    for node in (0,1):
        print(f'[G columns] node {node}: {len(basis)} initial-sector K columns',flush=True)
        restore,caches=LP.install_sine_cached_stack()
        try:
            for n,key in enumerate(basis):
                t0=time.time()
                E=FG.E({key:1+0j},node,5)
                L,cov,rows,diag,acc,rej=FG.L_whole_installed({key:1+0j},node,7)
                G=combine_G(E,L)
                physical=max(
                    float(diag.get('CV_complete_basis_leakage',0.0)),
                    float(diag.get('CK_outer_complete_basis_leakage',0.0)),
                    float(diag.get('CK_internal_volume_sector_leakage',0.0)),
                )
                scalar_fraction=acc/max(acc+rej,1e-300)
                row={
                    'input_key':repr(key),'column_index':n,
                    'E_support':len(E),'E_norm':gauss_norm(E),
                    'L_support':len(L),'L_norm':gauss_norm(L),
                    'G_support':len(G),'G_norm':gauss_norm(G),
                    'L_covariant_support':len(cov),'L_scalar_fraction':scalar_fraction,
                    'L_nonscalar_rejected_norm':math.sqrt(max(rej,0.0)),
                    'max_physical_basis_volume_leakage':physical,
                    'orientation_terms':len(rows),'elapsed_seconds':time.time()-t0,
                }
                row['passed']=(
                    len(rows)==24 and physical<1e-8 and scalar_fraction>1-1e-10
                    and row['L_nonscalar_rejected_norm']<1e-8
                    and all(np.isfinite([z.real,z.imag]).all() for z in G.values())
                )
                columns[node][key]=G; diagnostics[node].append(row)
                print(f'[G columns] node={node} col={n} E={len(E)} L={len(L)} G={len(G)} pass={row["passed"]} elapsed={row["elapsed_seconds"]:.3f}s',flush=True)
        finally:
            cache_info={
                name:{'hits':fn.cache_info().hits,'misses':fn.cache_info().misses,'currsize':fn.cache_info().currsize}
                for name,fn in caches.items()
            }
            restore()
        diagnostics[node].append({'shared_cache_info':cache_info})
    return basis,columns,diagnostics


def geometry_on_initial_route(state,w0,w1,columns,initial_sector):
    """Apply w0 G0+w1 G1 to a global route state in the initial fixed-spin sector."""
    out={}
    for key,modes in state.items():
        if BLK.sector_id(key)!=initial_sector:
            raise RuntimeError('G-after-route input escaped initial fixed-spin sector')
        for node,w in ((0,w0),(1,w1)):
            col=columns[node].get(key)
            if col is None:
                raise RuntimeError(f'missing G{node} column for route-mixed key {key}')
            for ko,gamp in col.items():
                dest=out.setdefault(ko,{})
                for mode,ramp in modes.items():
                    z=dest.get(mode,0j)+w*gamp*ramp
                    if abs(z)>TOL: dest[mode]=z
                    elif mode in dest: del dest[mode]
                if not dest: out.pop(ko,None)
    return out


def geometry_on_seed(initial,mode,w0,w1,columns):
    return geometry_on_initial_route({initial:{mode:1+0j}},w0,w1,columns,BLK.sector_id(initial))


def global_copy(s): return {k:dict(v) for k,v in s.items()}


def fit(vals):
    return float(np.polyfit(np.log(np.asarray(EPS,float)),np.log(np.asarray(vals,float)),1)[0])


def decreasing(vals): return all(b<a for a,b in zip(vals,vals[1:]))


def save_global(path,state):
    rows=[]
    for key,modes in state.items():
        for mode,amp in modes.items(): rows.append((key,mode,amp))
    rows.sort(key=lambda x:(repr(x[0]),x[1]))
    if rows:
        spins=np.asarray([r[0][0] for r in rows],dtype=np.int16)
        Ks=np.asarray([r[0][1] for r in rows],dtype=np.int16)
        modes=np.asarray([r[1] for r in rows],dtype=np.int32)
        amp=np.asarray([r[2] for r in rows],dtype=np.complex128)
    else:
        spins=np.zeros((0,len(PW.EDGES)),np.int16); Ks=np.zeros((0,len(PW.VERT)),np.int16)
        modes=np.zeros((0,2),np.int32); amp=np.zeros((0,),np.complex128)
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    np.savez_compressed(path,spins=spins,Ks=Ks,modes=modes,amp=amp)


def run(output_dir=None,carrier=CARRIER):
    ZVM.patch_and_clear()
    t0=time.time()

    print('[preflight] generic operator-first route block gate on genuine spin-changed E sectors',flush=True)
    route_preflight=RBG.run(n_sectors=3)
    if not route_preflight.get('passed',False):
        raise RuntimeError('generic operator-first route-block preflight failed')

    initial=PW.basis_full_jhalf()[0]
    sec0=BLK.sector_id(initial)
    basis,columns,column_diag=precompute_G_columns(sec0)
    columns_pass=all(r.get('passed',True) for rows in column_diag.values() for r in rows)
    if not columns_pass:
        raise RuntimeError('one or more signed G columns failed structural checks')

    mode=(int(carrier),int(carrier-1))
    psi=BLK.carrier_global_state(initial,carrier)
    rows=[]; cross_vals=[]; route_vals=[]
    saved={}

    for epsilon in EPS:
        print(f'[epsilon] {epsilon}',flush=True)
        N,M=SF.frozen_lapses(epsilon)
        a,b,c,d=analytic_node_weights(epsilon)

        RN=BLK.route_apply_global(N,psi,epsilon)
        RM=BLK.route_apply_global(M,psi,epsilon)
        RR=BLK.route_commutator_global(N,M,psi,epsilon)
        D=BLK.route_target_global(N,M,psi,epsilon)
        route_res=global_copy(RR); BLK.add_global(route_res,D,+1)

        GN_RM=geometry_on_initial_route(RM,a,b,columns,sec0)
        GM_RN=geometry_on_initial_route(RN,c,d,columns,sec0)
        GM_seed=geometry_on_seed(initial,mode,c,d,columns)
        GN_seed=geometry_on_seed(initial,mode,a,b,columns)
        RN_GM=BLK.route_apply_global(N,GM_seed,epsilon)
        RM_GN=BLK.route_apply_global(M,GN_seed,epsilon)

        cross={}
        BLK.add_global(cross,GN_RM,+1)
        BLK.add_global(cross,RN_GM,+1)
        BLK.add_global(cross,GM_RN,-1)
        BLK.add_global(cross,RM_GN,-1)

        Dn=normg(D); route_ratio=normg(route_res)/max(Dn,1e-30); cross_ratio=normg(cross)/max(Dn,1e-30)
        smear=a*d-b*c
        row={
            'epsilon':epsilon,
            'node_lapse_weights':{'a_N0':a,'b_N1':b,'c_M0':c,'d_M1':d},
            'antisymmetric_geometry_smear':smear,
            'D_norm':Dn,
            'RR_support':len(RR),'D_support':len(D),
            'route_residual_support':len(route_res),'cross_support':len(cross),
            'route_only_defect':route_ratio,'cross_over_D':cross_ratio,
            'cross_norm':normg(cross),
        }
        rows.append(row); route_vals.append(route_ratio); cross_vals.append(cross_ratio)
        saved[epsilon]=(cross,route_res,D,RR)
        print(f'[epsilon] route={route_ratio:.12g} cross/D={cross_ratio:.12g} cross_support={len(cross)}',flush=True)

    p_route=fit(route_vals); p_cross=fit(cross_vals)
    checks={
        'route_preflight':bool(route_preflight.get('passed',False)),
        'initial_route_sector_dimension_four':len(basis)==4,
        'all_G_columns_passed':columns_pass,
        'route_endpoint_small':route_vals[-1]<1e-4,
        'route_defect_decreasing':decreasing(route_vals),
        'cross_defect_decreasing':decreasing(cross_vals),
        'route_exponent_near_one':0.98<p_route<1.02,
        'cross_exponent_HDA_window':0.75<p_cross<1.25,
        'finite_cross_values':all(math.isfinite(x) for x in cross_vals),
        'no_channel_fit':True,
    }
    out={
        'status':'full signed spin-changing G x operator-first route cross on frozen two-node habitat',
        'passed':all(checks.values()),
        'input':'all ten links j=1/2, all five K=0; sparse Fourier carrier',
        'carrier':carrier,'epsilons':list(EPS),
        'geometry_coefficients':{'a_E':A,'b_L_raw':[B.real,B.imag]},
        'initial_route_sector_basis':[{'Ks2':list(k[1])} for k in basis],
        'route_preflight':route_preflight,
        'G_column_diagnostics':column_diag,
        'rows':rows,
        'fitted_route_residual_exponent':p_route,
        'fitted_GxR_cross_exponent':p_cross,
        'last_route_only_defect':route_vals[-1],
        'last_GxR_cross_over_D':cross_vals[-1],
        'checks':checks,
        'elapsed_seconds':time.time()-t0,
        'next_assembly':'Add (a*d-b*c) times the independently computed signed [G0,G1] state to route_residual + cross at each epsilon; then evaluate the full joint residual against D.',
    }
    if output_dir is not None:
        d0=Path(output_dir); d0.mkdir(parents=True,exist_ok=True)
        for epsilon,(cross,route_res,D,RR) in saved.items():
            tag=str(epsilon).replace('.','p')
            save_global(d0/f'CROSS_{tag}.npz',cross)
            save_global(d0/f'ROUTE_RESIDUAL_{tag}.npz',route_res)
            save_global(d0/f'D_{tag}.npz',D)
            save_global(d0/f'RR_{tag}.npz',RR)
        (d0/'RESULT.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--carrier',type=int,default=CARRIER)
    p.add_argument('--output-dir',type=Path,default=Path('verification_results/full_signed_geometry_route_cross'))
    a=p.parse_args(); out=run(a.output_dir,a.carrier); print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if out['passed'] else 1

if __name__=='__main__': raise SystemExit(main())
