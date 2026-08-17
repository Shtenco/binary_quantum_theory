#!/usr/bin/env python3
"""Canonical low-energy Schur/gap gate for BCQG collective closure C2.

Input NPZ must contain a Hermitian matrix ``C`` in a basis whose first ``p_dim``
columns are the currently retained low-energy carrier; the first six retained
columns are the frozen coarse metric-edge order (01,02,03,12,13,23).

The gate never inverts a low-energy Q mode.  Stable coupled low modes request
promotion; stable decoupled low modes request classification.  Only a residual
Q sector gapped at all frozen thresholds receives a Schur complement.
"""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import numpy as np

THRESHOLDS=(1e-9,1e-10,1e-11)
HERM_TOL=1e-10
SCHUR_TOL=1e-9
S4_TOL=1e-8
EDGES=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))


def projectors():
    O=np.zeros((6,6),float)
    for i,e in enumerate(EDGES):
        for j,f in enumerate(EDGES):
            if set(e).isdisjoint(f):O[i,j]=1.0
    I=np.eye(6);P1=np.ones((6,6))/6.0
    PE=.5*(I+O)-P1;PT=.5*(I-O)
    return P1,PE,PT,O
P1,PE,PT,OOPP=projectors()


def relnorm(x,scale):return float(np.linalg.norm(x)/max(float(scale),1e-300))

def analyze(C,p_dim=6):
    C=np.asarray(C,complex)
    if C.ndim!=2 or C.shape[0]!=C.shape[1]:
        return {'passed':False,'science_status':'INPUT_FAIL','reason':'C must be square'}
    n=C.shape[0]
    if p_dim<6 or p_dim>=n:
        return {'passed':False,'science_status':'INPUT_FAIL','reason':'require 6 <= p_dim < dim(C)','dimension':n,'p_dim':p_dim}
    scale=max(float(np.linalg.norm(C)),1e-300)
    herm=relnorm(C-C.conj().T,scale)
    if herm>HERM_TOL:
        return {'passed':False,'science_status':'INPUT_FAIL','reason':'input Hermiticity defect exceeds frozen tolerance','C_Hermiticity_relative_defect':herm,'tolerance':HERM_TOL}
    C=.5*(C+C.conj().T)
    A=C[:p_dim,:p_dim];B=C[:p_dim,p_dim:];D=C[p_dim:,p_dim:]
    evals,V=np.linalg.eigh(D)
    qscale=max(float(np.max(np.abs(evals))) if len(evals) else 0.0,1e-300)
    bscale=max(float(np.linalg.norm(B,2)) if B.size else 0.0,1e-300)
    er=np.abs(evals)/qscale
    cr=np.asarray([np.linalg.norm(B@V[:,i])/bscale for i in range(len(evals))],float)
    scan=[]
    for tau in THRESHOLDS:
        low=np.where(er<=tau)[0]
        coupled=[int(i) for i in low if cr[i]>tau]
        decoupled=[int(i) for i in low if cr[i]<=tau]
        scan.append({'relative_threshold':tau,'low_count':int(len(low)),'coupled_low_indices':coupled,'decoupled_low_indices':decoupled})
    counts=[x['low_count'] for x in scan]
    base={
        'dimension':n,'p_dim':int(p_dim),'q_dim':int(n-p_dim),
        'C_Hermiticity_relative_defect':herm,
        'QCQ_eigenvalues':[float(x) for x in evals],
        'QCQ_abs_eigenvalue_ratios':[float(x) for x in er],
        'Q_mode_coupling_ratios_to_P':[float(x) for x in cr],
        'threshold_scan':scan,
        'PCQ_spectral_norm':float(np.linalg.norm(B,2)) if B.size else 0.0,
        'frozen_thresholds':list(THRESHOLDS),
    }
    if len(set(counts))!=1:
        return {**base,'passed':False,'science_status':'THRESHOLD_UNSTABLE','reason':'low-energy Q count changes across frozen threshold scan; do not invert'}
    if counts[0]>0:
        loose=scan[0]
        nc=len(loose['coupled_low_indices']);nd=len(loose['decoupled_low_indices'])
        if nc and nd:status='PROMOTE_AND_CLASSIFY_LOW_ENERGY_MODES'
        elif nc:status='PROMOTE_LOW_ENERGY_MODES'
        else:status='CLASSIFY_DECOUPLED_LOW_ENERGY_MODES'
        return {**base,'passed':False,'science_status':status,
                'reason':'residual Q contains stable low-energy modes; closure inversion is forbidden until they are retained/classified'}

    # Residual Q sector is gapped at the loosest frozen threshold.
    inv=V@np.diag(1.0/evals)@V.conj().T
    Ceff=A-B@inv@B.conj().T
    ce_scale=max(float(np.linalg.norm(Ceff)),1e-300)
    ce_herm=relnorm(Ceff-Ceff.conj().T,ce_scale)
    Ceff=.5*(Ceff+Ceff.conj().T)

    # Exact projected-equation residual for all retained basis vectors at once.
    Qsol=-inv@B.conj().T
    qres=D@Qsol+B.conj().T
    pres=A+B@Qsol-Ceff
    qres_rel=relnorm(qres,max(np.linalg.norm(B.conj().T),1e-300))
    pres_rel=relnorm(pres,max(np.linalg.norm(Ceff),np.linalg.norm(A),1e-300))

    nz=np.abs(evals)
    gap_min=float(np.min(nz));gap_max=float(np.max(nz));gap_ratio=gap_min/max(gap_max,1e-300)
    cond=gap_max/max(gap_min,1e-300)

    M=Ceff[:6,:6]
    extra_mix=float(np.linalg.norm(Ceff[:6,6:])) if p_dim>6 else 0.0
    def kval(P,r):return float(np.trace(P@M).real/r)
    kA,kE,kT=kval(P1,1),kval(PE,2),kval(PT,3)
    Ms4=kA*P1+kE*PE+kT*PT
    s4def=relnorm(M-Ms4,max(np.linalg.norm(M),1e-300))
    imagdef=float(np.linalg.norm(M.imag)/max(np.linalg.norm(M),1e-300))
    mixAE=float(np.linalg.norm(P1@M@PE)+np.linalg.norm(PE@M@P1))
    mixAT=float(np.linalg.norm(P1@M@PT)+np.linalg.norm(PT@M@P1))
    mixET=float(np.linalg.norm(PE@M@PT)+np.linalg.norm(PT@M@PE))
    mscale=max(float(np.linalg.norm(M)),1e-300)
    ratio=None
    if abs(kE)>1e-14*max(abs(kA),abs(kT),1.0):ratio=[kA/kE,1.0,kT/kE]
    target=np.array([-.5,1.,2.])
    shapeerr=None if ratio is None else float(np.linalg.norm(np.asarray(ratio)-target)/np.linalg.norm(target))
    checks={
        'input_Hermitian':herm<=HERM_TOL,
        'residual_Q_gapped':gap_ratio>THRESHOLDS[0],
        'Schur_Q_equation':qres_rel<=SCHUR_TOL,
        'Schur_P_equation':pres_rel<=SCHUR_TOL,
        'Ceff_Hermitian':ce_herm<=HERM_TOL,
        'metric_block_real_Hermitian':imagdef<=HERM_TOL,
        'S4_covariance_metric_block':s4def<=S4_TOL,
    }
    return {**base,'passed':bool(all(checks.values())),'science_status':'SCHUR_GAP_STAGE_PASS' if all(checks.values()) else 'SCHUR_GAP_STAGE_FAIL',
            'checks':checks,'QCQ_min_abs_eigenvalue':gap_min,'QCQ_max_abs_eigenvalue':gap_max,
            'QCQ_normalized_gap':gap_ratio,'QCQ_condition_number':cond,
            'Schur_Q_equation_relative_residual':qres_rel,'Schur_P_equation_relative_residual':pres_rel,
            'Ceff_Hermiticity_relative_defect':ce_herm,'Ceff':[[[float(z.real),float(z.imag)] for z in row] for row in Ceff],
            'metric_nonmetric_retained_mixing_norm':extra_mix,
            'metric_block_S4_relative_defect':s4def,'metric_block_imag_relative_defect':imagdef,
            'metric_irrep_mixing_relative':{'A1_E':mixAE/mscale,'A1_T2':mixAT/mscale,'E_T2':mixET/mscale},
            'raw_metric_channels':{'kappa_A1':kA,'kappa_E':kE,'kappa_T2':kT},
            'blind_raw_ratio_normalized_to_E':ratio,
            'blind_GR_ratio_target_external_only':[-.5,1.,2.],
            'blind_GR_shape_relative_error_diagnostic_only':shapeerr,
            'interpretation':'Only the gapped residual Q sector was inverted. The GR ratio is reported after production and does not enter support, thresholds, inverse or PASS criteria.'}


def synthetic(kind):
    # Six metric P directions + six Q directions; choose a known S4 target.
    target=-.5*P1+1.0*PE+2.0*PT
    B=.4*np.eye(6)
    if kind=='gapped':
        d=np.array([2.,2.5,3.,3.5,4.,5.]);D=np.diag(d)
        A=target+B@np.diag(1/d)@B.T
    elif kind=='coupled_zero':
        d=np.array([0.,2.5,3.,3.5,4.,5.]);D=np.diag(d);A=target.copy()
    elif kind=='decoupled_zero':
        d=np.array([0.,2.5,3.,3.5,4.,5.]);D=np.diag(d);B[:,0]=0;pinv=np.diag([0]+[1/x for x in d[1:]]);A=target+B@pinv@B.T
    else:raise ValueError(kind)
    C=np.block([[A,B],[B.T,D]])
    return C,target


def selftest():
    C,T=synthetic('gapped');pos=analyze(C,6)
    rec=np.asarray([[complex(*z) for z in row] for row in pos['Ceff']]) if pos.get('Ceff') else None
    recovery=float(np.linalg.norm(rec-T)) if rec is not None else math.inf
    c0,_=synthetic('coupled_zero');neg1=analyze(c0,6)
    d0,_=synthetic('decoupled_zero');neg2=analyze(d0,6)
    checks={
        'gapped_control_passes':bool(pos.get('passed')),
        'known_Schur_recovered':recovery<1e-12,
        'known_S4_ratio_recovered':pos.get('blind_raw_ratio_normalized_to_E') is not None and np.linalg.norm(np.asarray(pos['blind_raw_ratio_normalized_to_E'])-np.array([-.5,1,2]))<1e-12,
        'coupled_zero_requests_promotion':neg1.get('science_status')=='PROMOTE_LOW_ENERGY_MODES',
        'decoupled_zero_requires_classification':neg2.get('science_status')=='CLASSIFY_DECOUPLED_LOW_ENERGY_MODES',
    }
    return {'status':'collective Schur-gap closure engine self-test','passed':bool(all(checks.values())),'checks':checks,
            'known_Schur_recovery_norm':recovery,'positive_control':pos,
            'coupled_zero_control_status':neg1.get('science_status'),'decoupled_zero_control_status':neg2.get('science_status')}


def load_npz(path):
    d=np.load(path,allow_pickle=False)
    if 'C' not in d:raise ValueError("NPZ must contain array 'C'")
    p=int(d['p_dim']) if 'p_dim' in d else 6
    return d['C'],p


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input',type=Path,help="NPZ with arrays C and optional scalar p_dim")
    ap.add_argument('--p-dim',type=int,help='override retained P dimension')
    ap.add_argument('--self-test',action='store_true')
    ap.add_argument('--require-closed',action='store_true')
    ap.add_argument('--output',type=Path)
    a=ap.parse_args()
    if a.self_test:out=selftest()
    elif a.input:
        C,p=load_npz(a.input);out=analyze(C,a.p_dim if a.p_dim is not None else p)
    else:out={'passed':False,'science_status':'INPUT_FAIL','reason':'use --self-test or --input'}
    text=json.dumps(out,indent=2,sort_keys=True);print(text)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(text+'\n',encoding='utf-8')
    if a.self_test:return 0 if out.get('passed') else 1
    if a.require_closed:return 0 if out.get('science_status')=='SCHUR_GAP_STAGE_PASS' and out.get('passed') else 1
    return 0 if out.get('science_status') not in ('INPUT_FAIL','SCHUR_GAP_STAGE_FAIL') else 1

if __name__=='__main__':raise SystemExit(main())
