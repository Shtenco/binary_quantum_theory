#!/usr/bin/env python3
"""Diagnose M-dependent recoupling-basis gauge in all-J volume blocks.

Frozen logic stated before inspecting general-J block differences:
- old magnetic Q and CH explicit Q must agree to machine precision;
- reconstruct Q and V from each individual (J,M) block, with no M averaging;
- compare to current M-averaged block reconstruction;
- accept the M-averaging diagnosis only if per-M Q/V reconstruction is <1e-12
  on every H_E-reached quartet while averaged V is >1e-6 wrong somewhere and
  a fixed-J M-block matrix differs by >1e-8.
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
import k5_peter_weyl_safe_hda_column as PW
import charged_intertwiner_recoupling_gate as CH
import peter_weyl_covariant_volume_leg_gate as CV
import peter_weyl_covariant_K_leg_gate as CK
import peter_weyl_volume_cross_rep_audit as VA


def full_q_old(spins):
    mats=[PW.spin_mats_cached(s) for s in spins[:3]]
    d=(spins[0]+1)*(spins[1]+1)*(spins[2]+1)
    Q=np.zeros((d,d),complex)
    import itertools
    for a,b,c in itertools.product(range(3),repeat=3):
        e=PW.EPS3[a,b,c]
        if e: Q += e*np.kron(np.kron(mats[0][a],mats[1][b]),mats[2][c])
    Q=.5*(Q+Q.conj().T)
    return np.kron(Q,np.eye(spins[3]+1,dtype=complex))

def block_basis(spins,J2,M2):
    rec=CH.allowed_charged_labels(tuple(spins),J2)
    if not rec: return rec,np.zeros((int(np.prod([s+1 for s in spins])),0),complex)
    B=np.column_stack([CH.charged_tensor(tuple(spins),a,b,J2,M2).reshape(-1) for a,b in rec])
    return rec,B

def sqrt_abs(H,zeroaware=False):
    H=.5*(H+H.conj().T); ev,U=np.linalg.eigh(H)
    if zeroaware:
        tau=1000*np.finfo(float).eps*H.shape[0]*max(1.0,float(np.max(np.abs(ev))) if len(ev) else 0.0)
        ev=np.where(np.abs(ev)>tau,ev,0.0)
    return (U*np.sqrt(np.abs(ev)))@U.conj().T

def rel(A,B): return float(np.linalg.norm(A-B,'fro')/max(np.linalg.norm(B,'fro'),1e-30))

def audit_one(spins):
    spins=tuple(spins); D=int(np.prod([s+1 for s in spins]))
    Qold=full_q_old(spins)
    Qch=np.kron(CH.q123_matrix(tuple(spins[:3])),np.eye(spins[3]+1,dtype=complex))
    Qpm=np.zeros((D,D),complex); Vpm=np.zeros((D,D),complex); Qavg=np.zeros((D,D),complex); Vavg=np.zeros((D,D),complex)
    max_mdiff=0.0; mdiffs={}
    for J2 in CV.all_total_J2(spins):
        rec=CH.allowed_charged_labels(spins,J2)
        if not rec: continue
        qlist=[]; blocks=[]
        for M2 in PW.m2vals_t(J2):
            _,Qb,_,_=CH.q_block(spins,J2,M2)
            _,B=block_basis(spins,J2,M2)
            qlist.append(Qb); blocks.append((M2,B,Qb))
            Qpm += B@Qb@B.conj().T
            Vpm += B@sqrt_abs(Qb,zeroaware=True)@B.conj().T
        if len(qlist)>1:
            for a in range(len(qlist)):
                for b in range(a+1,len(qlist)):
                    max_mdiff=max(max_mdiff,float(np.linalg.norm(qlist[a]-qlist[b],'fro')))
        Qbar=sum(qlist)/len(qlist)
        Vbar=sqrt_abs(Qbar,zeroaware=True)
        for _,B,_ in blocks:
            Qavg += B@Qbar@B.conj().T
            Vavg += B@Vbar@B.conj().T
        mdiffs[str(J2/2)]=max((float(np.linalg.norm(A-B,'fro')) for A in qlist for B in qlist),default=0.0)
    Vref=sqrt_abs(Qold,zeroaware=True)
    return {
      'spins':[s/2 for s in spins],
      'Qold_vs_CH_relative':rel(Qch,Qold),
      'Q_perM_reconstruction_relative':rel(Qpm,Qold),
      'V_perM_reconstruction_relative':rel(Vpm,Vref),
      'Q_Mavg_reconstruction_relative':rel(Qavg,Qold),
      'V_Mavg_reconstruction_relative':rel(Vavg,Vref),
      'max_fixedJ_M_block_difference':max_mdiff,
      'fixedJ_M_block_differences':mdiffs,
    }

def run():
    quartets,_=VA.collect_reached_volume_quartets()
    rows=[audit_one(q) for q in quartets]
    maxv=lambda k:max((r[k] for r in rows),default=0.0)
    diagnosis=(
      bool(rows)
      and maxv('Qold_vs_CH_relative')<1e-12
      and maxv('Q_perM_reconstruction_relative')<1e-12
      and maxv('V_perM_reconstruction_relative')<1e-12
      and maxv('V_Mavg_reconstruction_relative')>1e-6
      and maxv('max_fixedJ_M_block_difference')>1e-8
    )
    return {
      'status':'Q block magnetic-sublevel gauge audit',
      'passed':bool(diagnosis),
      'unique_reached_spin_quartets':len(rows),
      'rows':rows,
      'max_Qold_vs_CH_relative':maxv('Qold_vs_CH_relative'),
      'max_Q_perM_reconstruction_relative':maxv('Q_perM_reconstruction_relative'),
      'max_V_perM_reconstruction_relative':maxv('V_perM_reconstruction_relative'),
      'max_Q_Mavg_reconstruction_relative':maxv('Q_Mavg_reconstruction_relative'),
      'max_V_Mavg_reconstruction_relative':maxv('V_Mavg_reconstruction_relative'),
      'max_fixedJ_M_block_difference':maxv('max_fixedJ_M_block_difference'),
      'diagnosis':'PASS means current general-J averaging mixes M-dependent recoupling-basis gauges; physical Q is correct and per-M functional calculus reconstructs magnetic V.',
      'next_use':'If PASS, remove M averaging from general-J volume blocks, then rerun volume, H_E, K and covariant-K audits before any H_L triple.'
    }

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--output',type=Path); a=ap.parse_args(); out=run(); text=json.dumps(out,indent=2); print(text)
    if a.output: a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1
if __name__=='__main__': raise SystemExit(main())
