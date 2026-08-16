#!/usr/bin/env python3
"""Frozen normalized-state Hessian / DeWitt extractor for the BCQG six-channel carrier.

Three coordinate systems are kept explicit:
  q : orthonormal microscopic tangent coordinates,
  y : directly measured six-component coarse geometric observables,
  h : orthonormal Sym^2 metric coordinates.

A direct response B=dy/dq is mandatory.  The geometric Jacobian y=J h may be
either the edge-squared map (diagnostic) or the BCQG-native coarse face-flux
Gram map (primary science route).  No coordinate convention may replace B.
"""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import numpy as np
TRACE=np.array([1,1,1,0,0,0],float)/math.sqrt(3)
TL=np.column_stack([np.array([1,-1,0,0,0,0],float)/math.sqrt(2),np.array([1,1,-2,0,0,0],float)/math.sqrt(6),np.array([0,0,0,1,0,0],float),np.array([0,0,0,0,1,0],float),np.array([0,0,0,0,0,1],float)])
E2=TL[:,:2];T23=TL[:,2:];SQ2=math.sqrt(2)
J_EDGE=np.array([[0,.5,.5,0,0,SQ2/2],[.5,0,.5,0,SQ2/2,0],[.5,.5,0,SQ2/2,0,0],[.5,.5,0,-SQ2/2,0,0],[.5,0,.5,0,-SQ2/2,0],[0,.5,.5,0,0,-SQ2/2]],float)
J_FLUX=np.array([[-2/3,0,0,0,0,SQ2/3],[0,-2/3,0,0,SQ2/3,0],[0,0,-2/3,SQ2/3,0,0],[0,0,-2/3,-SQ2/3,0,0],[0,-2/3,0,0,-SQ2/3,0],[-2/3,0,0,0,0,-SQ2/3]],float)
JACOBIANS={'edge_squared':J_EDGE,'face_flux_gram':J_FLUX}
def cmat(rows):return np.array([[complex(*z) if isinstance(z,list) else complex(z) for z in row] for row in rows],complex)
def analyze(C,C00,B,coordinate_kind='face_flux_gram'):
    C=np.asarray(C,complex);B=np.asarray(B,float)
    if C.shape!=(6,6) or B.shape!=(6,6):raise ValueError('C and B must be 6x6')
    if coordinate_kind not in JACOBIANS:raise ValueError(f'unknown coordinate_kind {coordinate_kind}')
    J=JACOBIANS[coordinate_kind]
    herm=np.linalg.norm(C-C.conj().T)/max(np.linalg.norm(C),1e-300)
    Kq=2*np.real(.5*(C+C.conj().T))-2*float(np.real(C00))*np.eye(6)
    condB=np.linalg.cond(B)
    if not np.isfinite(condB) or condB>1e12:return {'science_status':'INCOMPLETE_METRIC_CALIBRATION','passed':False,'reason':'metric response B is singular/ill-conditioned','condition_B':float(condB),'coordinate_kind':coordinate_kind}
    Q=np.linalg.solve(B,J);Kh=Q.T@Kq@Q;Kh=.5*(Kh+Kh.T)
    lam_tr=float(TRACE@Kh@TRACE);Ktl=TL.T@Kh@TL;mix=TL.T@Kh@TRACE;eig=np.linalg.eigvalsh(Ktl);lam_tl=float(np.trace(Ktl)/5);scale=max(abs(lam_tl),np.linalg.norm(Ktl)/math.sqrt(5),1e-300)
    anis=float(np.linalg.norm(Ktl-lam_tl*np.eye(5))/scale);mixing=float(np.linalg.norm(mix)/scale);KE=E2.T@Kh@E2;KT=T23.T@Kh@T23;KET=E2.T@Kh@T23;lam_E=float(np.trace(KE)/2);lam_T2=float(np.trace(KT)/3)
    ceff=(1-lam_tr/lam_tl)/3 if abs(lam_tl)>1e-14*max(np.linalg.norm(Kh),1.0) else None
    return {'science_status':'DIRECT_METRIC_HESSIAN_EXTRACTION','passed':bool(herm<1e-10 and ceff is not None),'coordinate_kind':coordinate_kind,'C_Hermiticity_relative_defect':float(herm),'condition_B':float(condB),'det_geometric_J':float(np.linalg.det(J)),'condition_geometric_J':float(np.linalg.cond(J)),'K_q':Kq.tolist(),'K_metric':Kh.tolist(),'lambda_trace':lam_tr,'lambda_TL_mean':lam_tl,'lambda_TL_eigenvalues':eig.tolist(),'c_DeWitt_eff':ceff,'traceless_anisotropy':anis,'trace_TL_mixing':mixing,'tetra_E_mean':lam_E,'tetra_T2_mean':lam_T2,'tetra_E_T2_relative_split':abs(lam_E-lam_T2)/max(abs(lam_tl),1e-300),'tetra_E_T2_mixing':float(np.linalg.norm(KET)/scale),'formula':'K_q=2 Re(C)-2 C00 I; y=Bq=Jh; q=B^-1 J h; K_h=(B^-1 J)^T K_q (B^-1 J); c=(1-lambda_trace/lambda_TL)/3','scope_note':'A c_eff science claim requires direct B on the same BCQG background. face_flux_gram is the primary BCQG-native coordinate route; edge_squared is a geometric diagnostic.'}
def s4_B():
    edges=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)];Aadj=np.zeros((6,6),float)
    for i,e in enumerate(edges):
        for j,f in enumerate(edges):
            if i!=j and len(set(e)&set(f))==1:Aadj[i,j]=1.0
    I=np.eye(6);P1=np.ones((6,6))/6.0;PE=(Aadj-4*I)@Aadj/12.0;PT=(Aadj-4*I)@(Aadj+2*I)/(-8.0)
    return 1.3*P1+.9*PE+.6*PT
def selftest_one(kind):
    A=1.7;c=.5;Kh=2*A*(np.eye(6)-3*c*np.outer(TRACE,TRACE));B=s4_B();J=JACOBIANS[kind];Q=np.linalg.solve(B,J);Kq=np.linalg.solve(Q.T,Kh)@np.linalg.inv(Q);C00=.23;C=.5*Kq+C00*np.eye(6);o=analyze(C,C00,B,kind)
    checks={'recovers_c_half':bool(abs(o['c_DeWitt_eff']-.5)<1e-12),'zero_trace_TL_mix':bool(o['trace_TL_mixing']<1e-12),'zero_tl_anisotropy':bool(o['traceless_anisotropy']<1e-12),'E_T2_equal':bool(o['tetra_E_T2_relative_split']<1e-12),'nontrivial_B_used':bool(abs(np.linalg.cond(B)-1)>1e-3)}
    return checks,o
def selftest():
    rows={};passed=True
    for kind in JACOBIANS:
        checks,o=selftest_one(kind);rows[kind]={'checks':checks,'extraction':o};passed &= all(checks.values())
    return {'status':'collective metric Hessian extractor two-coordinate self-test','passed':bool(passed),'coordinate_routes_tested':list(JACOBIANS),'routes':rows}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input',type=Path);p.add_argument('--output',type=Path);p.add_argument('--selftest',action='store_true');a=p.parse_args()
    if a.selftest:out=selftest()
    elif a.input is None:out={'status':'missing direct BCQG Hessian input','passed':False,'science_status':'INCOMPLETE','required':['C_6x6','C00','metric_response_B_6x6','coordinate_kind'],'reason':'No c_eff is inferred without direct metric calibration B.'}
    else:
        d=json.loads(a.input.read_text());out=analyze(cmat(d['C_6x6']),d['C00'],np.array(d['metric_response_B_6x6'],float),d.get('coordinate_kind','face_flux_gram'))
    txt=json.dumps(out,indent=2);print(txt)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(txt+'\n')
    return 0 if (out.get('passed') or out.get('science_status')=='INCOMPLETE') else 1
if __name__=='__main__':raise SystemExit(main())