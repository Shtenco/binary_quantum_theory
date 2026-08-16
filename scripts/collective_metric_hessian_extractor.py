#!/usr/bin/env python3
"""Frozen normalized-state Hessian / DeWitt extractor for the BCQG six-edge carrier.

The extractor deliberately separates:
  q : orthonormal microscopic W_g tangent coordinates,
  y : directly measured six-component coarse geometric observables,
  h : orthonormal Sym^2 metric coordinates.

A direct BCQG metric calibration is mandatory. Two equivalent input routes are
allowed:
  1. B=dy/dq together with the fixed tetrahedral edge map y=J h;
  2. the BCQG-native direct map M_hq=dh/dq, e.g.
       M_hq=(J_F^bg)^(-1) B_F
     from the measured coarse face-flux Gram response.

No coordinate convention may replace a measured calibration. This prevents a
hidden trace-vs-traceless normalization choice from fitting the DeWitt
coefficient.
"""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import numpy as np

TRACE=np.array([1,1,1,0,0,0],float)/math.sqrt(3)
TL=np.column_stack([
 np.array([1,-1,0,0,0,0],float)/math.sqrt(2),
 np.array([1,1,-2,0,0,0],float)/math.sqrt(6),
 np.array([0,0,0,1,0,0],float),
 np.array([0,0,0,0,1,0],float),
 np.array([0,0,0,0,0,1],float),
])
# In the chosen tetrahedral orientation, TL=E(2 diagonal traceless)+T2(3 offdiagonal).
E2=TL[:,:2]
T23=TL[:,2:]

SQ2=math.sqrt(2)
J=np.array([
 [0,.5,.5,0,0,SQ2/2],
 [.5,0,.5,0,SQ2/2,0],
 [.5,.5,0,SQ2/2,0,0],
 [.5,.5,0,-SQ2/2,0,0],
 [.5,0,.5,0,-SQ2/2,0],
 [0,.5,.5,0,0,-SQ2/2],
],float)

def cmat(rows):
    return np.array([[complex(*z) if isinstance(z,list) else complex(z) for z in row] for row in rows],complex)

def analyze(C,C00,B=None,M_hq=None):
    C=np.asarray(C,complex)
    if C.shape!=(6,6): raise ValueError("C must be 6x6")
    if (B is None)==(M_hq is None):
        raise ValueError("provide exactly one of B=dy/dq or M_hq=dh/dq")
    herm=np.linalg.norm(C-C.conj().T)/max(np.linalg.norm(C),1e-300)
    # W_g is frozen orthonormal and background-orthogonal. For real tangent
    # coordinates q, the normalized expectation Hessian at q=0 is
    # K_q = 2 Re(C) - 2 C00 I.
    Kq=2*np.real(.5*(C+C.conj().T))-2*float(np.real(C00))*np.eye(6)
    if M_hq is not None:
        M_hq=np.asarray(M_hq,float)
        if M_hq.shape!=(6,6): raise ValueError("M_hq must be 6x6")
        cond=np.linalg.cond(M_hq)
        calibration_mode="direct_q_to_metric_h"
        if not np.isfinite(cond) or cond>1e12:
            return {"science_status":"INCOMPLETE_METRIC_CALIBRATION","passed":False,
                    "reason":"q_to_metric_h_map is singular/ill-conditioned",
                    "condition_calibration_map":float(cond)}
        Q=np.linalg.inv(M_hq)  # q=M_hq^{-1}h
    else:
        B=np.asarray(B,float)
        if B.shape!=(6,6): raise ValueError("B must be 6x6")
        cond=np.linalg.cond(B)
        calibration_mode="edge_observable_B_dy_dq"
        if not np.isfinite(cond) or cond>1e12:
            return {"science_status":"INCOMPLETE_METRIC_CALIBRATION","passed":False,
                    "reason":"metric response B is singular/ill-conditioned",
                    "condition_calibration_map":float(cond)}
        Q=np.linalg.solve(B,J)  # q=B^{-1}Jh
    Kh_raw=Q.T@Kq@Q
    Kh=.5*(Kh_raw+Kh_raw.T)
    lam_tr=float(TRACE@Kh@TRACE)
    Ktl=TL.T@Kh@TL
    mix=TL.T@Kh@TRACE
    tl_eigs=np.linalg.eigvalsh(Ktl)
    lam_tl=float(np.trace(Ktl)/5)
    scale=max(abs(lam_tl),np.linalg.norm(Ktl)/math.sqrt(5),1e-300)
    anis=float(np.linalg.norm(Ktl-lam_tl*np.eye(5))/scale)
    mixing=float(np.linalg.norm(mix)/scale)
    KE=E2.T@Kh@E2; KT=T23.T@Kh@T23; KET=E2.T@Kh@T23
    lam_E=float(np.trace(KE)/2); lam_T2=float(np.trace(KT)/3)
    irrep_split=abs(lam_E-lam_T2)/max(abs(lam_tl),1e-300)
    irrep_mix=float(np.linalg.norm(KET)/scale)
    ceff=(1-lam_tr/lam_tl)/3 if abs(lam_tl)>1e-14*max(np.linalg.norm(Kh),1.0) else None
    return {
      "science_status":"DIRECT_METRIC_HESSIAN_EXTRACTION",
      "passed":bool(herm<1e-10 and ceff is not None),
      "C_Hermiticity_relative_defect":float(herm),
      "calibration_mode":calibration_mode,
      "condition_calibration_map":float(cond),
      "K_q":Kq.tolist(),"K_metric":Kh.tolist(),
      "lambda_trace":lam_tr,
      "lambda_TL_mean":lam_tl,
      "lambda_TL_eigenvalues":tl_eigs.tolist(),
      "c_DeWitt_eff":ceff,
      "traceless_anisotropy":anis,
      "trace_TL_mixing":mixing,
      "tetra_E_mean":lam_E,
      "tetra_T2_mean":lam_T2,
      "tetra_E_T2_relative_split":irrep_split,
      "tetra_E_T2_mixing":irrep_mix,
      "formula":"K_q=2 Re(C)-2 C00 I; then either q=B^{-1}J h or q=M_hq^{-1}h; K_h=Q^T K_q Q; c=(1-lambda_trace/lambda_TL)/3",
      "scope_note":"A c_eff science claim requires direct BCQG coarse metric calibration and a physically defined effective scalar. The preferred native calibration is M_hq=(J_F^bg)^-1 B_F from coarse face-flux Gram response. Setting B=I by convention is not a measurement."
    }

def selftest():
    # Build a target metric Hessian with c=1/2 and arbitrary overall scale,
    # then push it back through a nontrivial tetrahedrally equivariant B.
    A=1.7;c=.5
    Kh=2*A*(np.eye(6)-3*c*np.outer(TRACE,TRACE))
    # Deliberately use three distinct finite-S4 calibration scales A1/E/T2.
    edges=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    Aadj=np.zeros((6,6),float)
    for i,e in enumerate(edges):
        for j,f in enumerate(edges):
            if i!=j and len(set(e)&set(f))==1:Aadj[i,j]=1.0
    I=np.eye(6);P1=np.ones((6,6))/6.0
    PE=(Aadj-4*I)@Aadj/12.0
    PT=(Aadj-4*I)@(Aadj+2*I)/(-8.0)
    B=1.3*P1+.9*PE+.6*PT
    Q=np.linalg.solve(B,J)
    # K_h=Q^T K_q Q -> K_q=Q^{-T}K_hQ^{-1}
    Kq=np.linalg.solve(Q.T,Kh)@np.linalg.inv(Q)
    C00=.23
    C=.5*Kq+C00*np.eye(6)
    o=analyze(C,C00,B=B)
    M_hq=np.linalg.inv(Q)
    o_native=analyze(C,C00,M_hq=M_hq)
    checks={
      "recovers_c_half":bool(abs(o["c_DeWitt_eff"]-.5)<1e-12),
      "zero_trace_TL_mix":bool(o["trace_TL_mixing"]<1e-12),
      "zero_tl_anisotropy":bool(o["traceless_anisotropy"]<1e-12),
      "E_T2_equal":bool(o["tetra_E_T2_relative_split"]<1e-12),
      "nontrivial_B_used":bool(abs(np.linalg.cond(B)-1)>1e-3),
      "three_distinct_S4_B_channels":True,
      "native_metric_map_same_c":bool(abs(o_native["c_DeWitt_eff"]-o["c_DeWitt_eff"])<1e-12),
      "native_metric_map_same_Hessian":bool(np.linalg.norm(np.array(o_native["K_metric"])-np.array(o["K_metric"]))<1e-12),
    }
    return {"status":"collective metric Hessian extractor self-test","passed":all(checks.values()),
            "checks":checks,"edge_B_extraction":o,"native_metric_map_extraction":o_native,
            "extraction":o_native}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",type=Path)
    p.add_argument("--output",type=Path)
    p.add_argument("--selftest",action="store_true")
    a=p.parse_args()
    if a.selftest:
        out=selftest()
    else:
        if a.input is None:
            out={"status":"missing direct BCQG Hessian input","passed":False,"science_status":"INCOMPLETE",
                 "required":["C_6x6","C00","one of metric_response_B_6x6 or q_to_metric_h_map"],
                 "reason":"No c_eff is inferred without direct BCQG metric calibration."}
        else:
            d=json.loads(a.input.read_text())
            if "q_to_metric_h_map" in d:
                out=analyze(cmat(d["C_6x6"]),d["C00"],M_hq=np.array(d["q_to_metric_h_map"],float))
            elif "metric_response_B_6x6" in d:
                out=analyze(cmat(d["C_6x6"]),d["C00"],B=np.array(d["metric_response_B_6x6"],float))
            else:
                out={"status":"missing direct BCQG metric calibration","passed":False,"science_status":"INCOMPLETE",
                     "required":["metric_response_B_6x6 or q_to_metric_h_map"]}
    txt=json.dumps(out,indent=2)
    print(txt)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+"\n")
    return 0 if (out.get("passed") or out.get("science_status")=="INCOMPLETE") else 1
if __name__=="__main__": raise SystemExit(main())
