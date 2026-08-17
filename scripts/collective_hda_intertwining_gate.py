#!/usr/bin/env python3
"""Executable theorem controls for BCQG collective HDA inheritance C3.

PASS certifies the exact compression identity, leakage bound, support of the
existing asymptotic HDA theorem, and matrix-valued/noncommuting operator-first
route construction.  It does NOT supply queued production collective residuals.
"""
from __future__ import annotations
import argparse,json,math,sys
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
import operator_route_sparse_fourier as SF


def opnorm(A):return float(np.linalg.norm(A,2))

def compression_control():
    rng=np.random.default_rng(314159)
    n=7;p=3
    X=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));A=.5*(X+X.conj().T)
    X=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));B=.5*(X+X.conj().T)
    X=rng.normal(size=(n,p))+1j*rng.normal(size=(n,p));W=np.linalg.qr(X)[0][:,:p]
    P=W@W.conj().T;Q=np.eye(n)-P
    Ae=W.conj().T@A@W;Be=W.conj().T@B@W
    lhs=Ae@Be-Be@Ae-W.conj().T@(A@B-B@A)@W
    rhs=-W.conj().T@A@Q@B@W+W.conj().T@B@Q@A@W
    identity=opnorm(lhs-rhs)
    etaA=opnorm(Q@A@W);etaB=opnorm(Q@B@W);bound=2*etaA*etaB
    lhsnorm=opnorm(lhs)
    # Exact-invariant control: block diagonal A,B with W canonical first p cols.
    W0=np.eye(n,dtype=complex)[:,:p]
    A0=np.diag(np.arange(1,n+1.0));B0=np.diag(np.arange(n,0,-1.0))
    Q0=np.eye(n)-W0@W0.conj().T
    inv_eta=max(opnorm(Q0@A0@W0),opnorm(Q0@B0@W0))
    inv_def=opnorm((W0.conj().T@A0@W0)@(W0.conj().T@B0@W0)-(W0.conj().T@B0@W0)@(W0.conj().T@A0@W0)-W0.conj().T@(A0@B0-B0@A0)@W0)
    return {'identity_defect':identity,'compressed_algebra_difference_norm':lhsnorm,'leakage_bound':bound,'bound_margin':bound-lhsnorm,
            'eta_A':etaA,'eta_B':etaB,'exact_invariant_max_leakage':inv_eta,'exact_invariant_algebra_defect':inv_def}


def noncommuting_route_control():
    # Q_ab from B_a^dag B_b symmetrization, so A(k)=(sum k_a B_a)^dag(sum k_b B_b)>=0.
    B0=np.array([[1.2,.3],[.3,2.0]],complex)
    B1=np.array([[.8,.35j],[-.35j,1.5]],complex)
    Bs=(B0,B1)
    Q=[[None,None],[None,None]]
    for a in range(2):
      for b in range(2):
        Q[a][b]=.5*(Bs[a].conj().T@Bs[b]+Bs[b].conj().T@Bs[a])
    comm=opnorm(Q[0][0]@Q[1][1]-Q[1][1]@Q[0][0])
    modes=((1,0),(0,1),(1,1),(2,-1))
    rows=[];worst_recon=0.0;mineig=math.inf
    eps=.125
    for k in modes:
        A=(k[0]*k[0]*Q[0][0]+k[0]*k[1]*(Q[0][1]+Q[1][0])+k[1]*k[1]*Q[1][1])
        A=.5*(A+A.conj().T);mineig=min(mineig,float(np.linalg.eigvalsh(A).min()))
        Om=SF.omega_matrix(Q,k,eps)
        recon=opnorm((eps*Om)@(eps*Om)-A)/max(opnorm(A),1e-300);worst_recon=max(worst_recon,recon)
        rows.append({'mode':list(k),'A_min_eigenvalue':float(np.linalg.eigvalsh(A).min()),'sqrt_reconstruction_relative_defect':recon})
    # Execute route and matrix-valued target on a nontrivial Fourier state.
    N,M=SF.frozen_lapses(eps);psi=SF.carrier_state(2,4,0)
    rc=SF.route_commutator(Q,N,M,psi,eps);rt=SF.route_target(Q,N,M,psi,eps)
    finite=all(np.isfinite(np.asarray(v)).all() for d in (rc,rt) for v in d.values())
    return {'Q_entry_noncommutator_norm':comm,'minimum_symbol_eigenvalue':mineig,'worst_spectral_sqrt_reconstruction_relative_defect':worst_recon,
            'route_commutator_modes':len(rc),'matrix_target_modes':len(rt),'finite':bool(finite),'rows':rows}


def load(path):return json.loads(Path(path).read_text(encoding='utf-8'))
def run(hda_path):
    old=load(hda_path);c=compression_control();r=noncommuting_route_control()
    checks={
      'historical_asymptotic_HDA_theorem_passed':bool(old.get('passed')),
      'historical_geometry_smear_no_O1':bool(old.get('checks',{}).get('geometry_smear_has_no_O1')),
      'historical_cross_inverse_epsilon_cancellation':bool(old.get('checks',{}).get('dangerous_cross_inverse_epsilon_cancels')),
      'historical_route_spinchanged_evidence_passes':bool(old.get('checks',{}).get('spinchanged_operator_first_route_evidence_passes')),
      'compression_identity_machine_zero':c['identity_defect']<1e-12,
      'leakage_bound_holds':c['bound_margin']>-1e-12,
      'exact_invariant_subspace_inherits_exactly':c['exact_invariant_max_leakage']<1e-14 and c['exact_invariant_algebra_defect']<1e-14,
      'route_Q_entries_genuinely_noncommuting':r['Q_entry_noncommutator_norm']>1e-4,
      'noncommuting_route_symbol_positive':r['minimum_symbol_eigenvalue']>-1e-12,
      'spectral_sqrt_reconstructs_symbol':r['worst_spectral_sqrt_reconstruction_relative_defect']<1e-12,
      'noncommuting_route_and_target_execute_finitely':r['finite'] and r['route_commutator_modes']>0 and r['matrix_target_modes']>0,
    }
    passed=all(checks.values())
    return {'status':'BCQG collective HDA intertwining theorem controls','passed':bool(passed),
      'science_status':'CONDITIONAL_COLLECTIVE_HDA_INTERTWINING_THEOREM' if passed else 'THEOREM_GATE_FAIL',
      'checks':checks,'compression_identity_control':c,'noncommuting_matrix_route_control':r,
      'v13_geometry_definition':'G_v=-(2/3)E_v-(32/9)S_v, S_v=-i/2(L_raw-L_raw^dagger)',
      'historical_HDA_evidence_scope_note':'Loaded evidence uses the pre-v1.3 L_raw shorthand. This gate reuses only its smear/power-counting/route results, whose proof assumptions are bounded local geometry and operator-first route; it does not certify corrected V2 Lorentzian amplitudes.',
      'collective_bound':'||[H_eff[N],H_eff[M]]-i hbar D_eff[beta_eff]|| <= delta_micro + 2 eta_N eta_M + hbar delta_structure',
      'production_quantities_still_required':['delta_micro/||D_eff||','eta_N*eta_M/||D_eff||','hbar*delta_structure/||D_eff||','direct held-out collective HDA residual','second-class/completeness guard'],
      'interpretation':'PASS proves how HDA errors propagate through an isometric coarse map and that the route definition accepts noncommuting finite matrix-valued geometry blocks. Production convergence is still a measurement.'}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--hda-evidence',default='verification_results/FULL_OPERATOR_FIRST_HDA_THEOREM.json')
    ap.add_argument('--output',type=Path);a=ap.parse_args();o=run(a.hda_evidence);t=json.dumps(o,indent=2,sort_keys=True);print(t)
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(t+'\n',encoding='utf-8')
    return 0 if o['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
