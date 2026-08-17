#!/usr/bin/env python3
"""Dimensionless optical readout of the BCQG traceless metric E/T2 sectors.

This gate combines only symmetry and the exact tetrahedral edge->metric optical
response.  It does NOT identify the current q4 tangent Gram with the physical
Lorentzian propagator.

For the six unoriented tetrahedral edge directions the fractional squared-length
response is y=J h.  Balanced optical phases are proportional to y and eliminate
the common trace mode.  S4 gives 6=A1+E+T2.  The exact squared transfer gains
from orthonormal metric components to edge-phase components are

    g_A1^2=2,  g_E^2=1/2,  g_T2^2=1.

Therefore the gain-corrected ratio

    R_gamma = (phase power per E mode / g_E^2)
              /(phase power per T2 mode / g_T2^2)

is dimensionless and independent of laser wave number, common path length,
absolute metric amplitude and the overall Maxwell normalization.  In an SO(3)
IR limit R_gamma->1.  A nonunit fixed value is a direct optical signature of a
surviving tetrahedral spin-2 anisotropy, once a physical metric covariance is
provided by the Lorentzian theory.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


EDGES=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
SQ2=np.sqrt(2.0)
J=np.array([
    [0,   .5, .5, 0,      0,      SQ2/2],
    [.5,  0,  .5, 0,      SQ2/2,  0],
    [.5,  .5, 0,  SQ2/2,  0,      0],
    [.5,  .5, 0, -SQ2/2,  0,      0],
    [.5,  0,  .5, 0,     -SQ2/2,  0],
    [0,   .5, .5, 0,      0,     -SQ2/2],
],float)


def edge_commutant():
    I=np.eye(6); A=np.zeros((6,6)); O=np.zeros((6,6))
    for i,e in enumerate(EDGES):
        for j,f in enumerate(EDGES):
            if i==j: continue
            shared=len(set(e)&set(f))
            if shared==1: A[i,j]=1.0
            elif shared==0: O[i,j]=1.0
    P1=(I+A+O)/6.0
    PE=I/3.0-A/6.0+O/3.0
    PT=(I-O)/2.0
    return I,A,O,P1,PE,PT


def gain(JJ,P):
    rank=float(np.trace(P))
    return float(np.trace(P@JJ).real/rank)


def load_precursor(path: Path|None):
    if path is None: return None
    d=json.loads(path.read_text(encoding='utf-8'))
    o=d.get('S4_orbit_fit',d)
    if 'lambda_E' not in o or 'lambda_T2' not in o:
        raise ValueError('input JSON must contain lambda_E and lambda_T2')
    le=float(o['lambda_E']); lt=float(o['lambda_T2'])
    kiso=(2*le+3*lt)/5.0
    return {
        'lambda_E':le,
        'lambda_T2':lt,
        'kappa_iso_dimension_weighted':kiso,
        'Delta_ET':le-lt,
        'A_tet_kernel':(le-lt)/kiso,
        'static_Gaussian_R_gamma_if_and_only_if_this_kernel_were_physical':lt/le,
        'warning':'The current q4 tangent Gram is a precursor, not the physical Lorentzian kernel. The last ratio is a pipeline control, not an experimental prediction.'
    }


def run(path=None):
    I,A,O,P1,PE,PT=edge_commutant()
    JJ=J@J.T
    # Five simple balanced differences against channel 5.
    D=np.zeros((5,6))
    for i in range(5): D[i,i]=1.0; D[i,5]=-1.0
    trace_h=np.array([1,1,1,0,0,0],float)/np.sqrt(3.0)
    gains={'A1':gain(JJ,P1),'E':gain(JJ,PE),'T2':gain(JJ,PT)}
    checks={
        'rank_J_6':np.linalg.matrix_rank(J)==6,
        'rank_balanced_D_5':np.linalg.matrix_rank(D)==5,
        'rank_balanced_metric_response_5':np.linalg.matrix_rank(D@J)==5,
        'balanced_trace_null':np.linalg.norm(D@J@trace_h)<1e-12,
        'projectors_sum_identity':np.linalg.norm(P1+PE+PT-I)<1e-12,
        'projectors_orthogonal':max(np.linalg.norm(P1@PE),np.linalg.norm(P1@PT),np.linalg.norm(PE@PT))<1e-12,
        'gain_A1_exact_2':abs(gains['A1']-2.0)<1e-12,
        'gain_E_exact_half':abs(gains['E']-.5)<1e-12,
        'gain_T2_exact_1':abs(gains['T2']-1.0)<1e-12,
    }
    return {
        'status':'exact dimensionless optical readout bridge for BCQG traceless metric anisotropy',
        'passed':bool(all(checks.values())),
        'science_status':'STRUCTURAL_BLIND_OPTICAL_OBSERVABLE',
        'edge_order':[list(e) for e in EDGES],
        'metric_basis':['xx','yy','zz','sqrt2_xy','sqrt2_xz','sqrt2_yz'],
        'edge_to_metric_J':J.tolist(),
        'balanced_D':D.tolist(),
        'S4_decomposition':'6=A1+E+T2; traceless spin-2 carrier is E+T2',
        'squared_optical_transfer_gains':gains,
        'blind_observable':{
            'definition':'R_gamma=(S_E_per_mode/g_E^2)/(S_T2_per_mode/g_T2^2)',
            'equivalent_with_gains':'R_gamma=2*S_E_per_mode/S_T2_per_mode',
            'SO3_IR_target':1.0,
            'kernel_anisotropy':'A_tet=(lambda_E-lambda_T2)/((2 lambda_E+3 lambda_T2)/5)',
            'experimental_note':'Estimate the six phase/cavity-frequency channels, remove common mode, project with P_E and P_T2, divide their per-mode spectra by the exact gains, and take the ratio. Overall optical and metric normalization cancels.'
        },
        'single_photon_interference':{
            'state':'(|gamma_1>+|gamma_2>)/sqrt(2)',
            'ideal_probabilities':'P_plus/minus=(1 +/- cos Delta_phi)/2',
            'geometry_phase':'Delta_phi=k Delta_L; for y=delta(ell^2)/ell^2, delta_phi=(k ell/2)y',
            'quantum_geometry_generalization':'visibility V=|<exp(i Delta_phi_hat)>|; for zero-mean Gaussian phase noise V=exp(-Var(Delta_phi)/2)'
        },
        'checks':checks,
        'precursor_control':load_precursor(path),
        'interpretation':'This closes the normalization-free experimental readout map. It does not by itself prove a propagating photon or supply the physical metric covariance; those require the Lorentzian U(1) and metric dynamics.',
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--metric-json',type=Path,default=None)
    ap.add_argument('--output',type=Path,default=None)
    a=ap.parse_args(); out=run(a.metric_json); text=json.dumps(out,indent=2); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__=='__main__': raise SystemExit(main())
