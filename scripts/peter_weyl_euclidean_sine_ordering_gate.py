#!/usr/bin/env python3
"""Physical Euclidean ordering audit for the Peter-Weyl Hamiltonian.

The existing structural Peter-Weyl H_E combines a raw oriented trace T and its
adjoint as

    H_plus = (T + T^dagger)/2.

However the standard Thiemann/Yang-Ma Euclidean regularization carries an
external 1/i from Poisson-bracket quantization.  If the antisymmetric curvature
is grouped as h_alpha-h_alpha^{-1}, the symmetric physical operator must take
the adjoint AFTER that imaginary coefficient.  Up to the common positive real
normalization this gives

    H_sine = (T - T^dagger)/(2 i).

This distinction is not cosmetic.  Classically, with

    Y=h_alpha-h_alpha^dagger  (anti-Hermitian),
    X=h_s[h_s^dagger,V]      (Hermitian),

ordinary matrix coefficients satisfy cyclic trace, hence

    Tr Herm(YX) = Tr([Y,X]/2) = 0,

whereas

    Tr[(YX-(YX)^dagger)/(2i)] = -i Tr(YX)

is generically real and nonzero.  Since X itself comes from one quantum
commutator, H_plus adds another commutator and has the wrong naive classical
order in hbar.

This gate does NOT modify production code.  It constructs H_sine independently
in both existing representations:

1. the regulator-safe magnetic Peter-Weyl engine;
2. the symmetry-adapted all-J charged engine projected back to Gauss.

The zero-aware exact-Q-nullspace convention is installed first.  Acceptance
keeps the frozen all-J equivalence threshold 1e-9 and requires support equality.
No Lorentzian coefficient, beta, kappa or HDA fit appears here.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

import k5_peter_weyl_safe_hda_column as PW
import peter_weyl_covariant_K_projection_audit_gate as AUD
import peter_weyl_covariant_K_leg_gate as CK

TOL=1e-10
JMAX2=5


def add(dst,src,scale=1.0,tol=1e-11):
    for key,amp in src.items():
        z=dst.get(key,0j)+scale*amp
        if abs(z)>tol:
            dst[key]=z
        elif key in dst:
            del dst[key]


def norm2(state):
    return float(sum(abs(a)**2 for a in state.values()))


def relerr(a,b):
    keys=set(a)|set(b)
    num=math.sqrt(sum(abs(a.get(k,0j)-b.get(k,0j))**2 for k in keys))
    den=math.sqrt(norm2(b))
    return num/max(den,1e-30)


def inner(a,b):
    return sum(np.conj(a.get(k,0j))*b.get(k,0j) for k in set(a)|set(b))


def safe_H_sine(state,v,Jmax2=JMAX2):
    out={}
    for sign,spec in PW.oriented_specs(v):
        rr=PW.apply_T_cached_state(state,spec,Jmax2,False)
        aa=PW.apply_T_cached_state(state,spec,Jmax2,True)
        # (T-T^dagger)/(2i) = -i T/2 + i T^dagger/2.
        add(out,rr,-0.5j*sign)
        add(out,aa,+0.5j*sign)
    return {k:a for k,a in out.items() if abs(a)>TOL}


def project_gauss_branch(branch,tol=1e-11):
    # Same projection as the frozen invariant audit; copied to make the new
    # ordering implementation independent of the old plus-adjoint helper.
    spins,tensors,amp=branch
    opts=[]
    for v in PW.VERT:
        ls=PW.local_spins(spins,v)
        row=[]
        for K in PW.allowed_k2_t(*ls):
            c=np.vdot(PW.oriented_intertwiner(v,ls,K),tensors[v])
            if abs(c)>1e-13:
                row.append((K,c))
        if not row:
            return {}
        opts.append(tuple(row))
    out={}
    for choice in itertools.product(*opts):
        val=amp; Ks=[]
        for K,c in choice:
            Ks.append(K); val*=c
        if abs(val)>tol:
            key=(spins,tuple(Ks))
            out[key]=out.get(key,0j)+val
    return {k:a for k,a in out.items() if abs(a)>tol}


def allJ_H_sine(initial,source_v,Jmax2=JMAX2):
    base=PW.initial_factorized_oriented(initial)
    out={}; max_vleak=0.0
    for sign,spec in PW.oriented_specs(source_v):
        v,a,b,c=spec
        for adj in (False,True):
            pref=(+0.5j if adj else -0.5j)*sign
            for coef,seq0 in PW.T_sequences(v,a,b,c):
                seq=PW.adjoint_sequence(seq0) if adj else seq0
                branches,vleak=CK.apply_sequence_to_branch(
                    base,seq,source_v,Jmax2
                )
                max_vleak=max(max_vleak,float(vleak))
                for br in branches:
                    add(out,project_gauss_branch(br),pref*coef)
    return {k:a for k,a in out.items() if abs(a)>TOL},max_vleak


def classical_trace_control():
    sx=np.array([[0,1],[1,0]],complex)
    sy=np.array([[0,-1j],[1j,0]],complex)
    sz=np.array([[1,0],[0,-1]],complex)
    sigma=(sx,sy,sz)
    # Fixed deterministic nonparallel vectors; no random acceptance.
    y=np.array([0.7,-1.1,0.4])
    x=np.array([1.3,0.2,-0.8])
    Y=1j*sum(y[i]*sigma[i] for i in range(3))
    X=sum(x[i]*sigma[i] for i in range(3))
    A=Y@X
    old=0.5*(A+A.conj().T)
    sine=(A-A.conj().T)/(2j)
    return {
        'Y_antihermiticity':float(np.linalg.norm(Y.conj().T+Y)),
        'X_hermiticity':float(np.linalg.norm(X.conj().T-X)),
        'raw_trace':[float(np.trace(A).real),float(np.trace(A).imag)],
        'old_plus_trace':[float(np.trace(old).real),float(np.trace(old).imag)],
        'sine_trace':[float(np.trace(sine).real),float(np.trace(sine).imag)],
        'old_plus_trace_abs':float(abs(np.trace(old))),
        'sine_trace_abs':float(abs(np.trace(sine))),
    }


def ranked_diffs(a,b,n=12):
    rows=[]
    for k in set(a)|set(b):
        aa=a.get(k,0j); bb=b.get(k,0j)
        rows.append((abs(aa-bb),k,aa,bb))
    rows.sort(reverse=True,key=lambda x:x[0])
    return [
        {
            'abs_difference':float(d),
            'max_spin':max(k[0])/2,
            'Ks':list(k[1]),
            'safe':[float(bb.real),float(bb.imag)],
            'allJ':[float(aa.real),float(aa.imag)],
        }
        for d,k,aa,bb in rows[:n]
    ]


def run():
    import peter_weyl_zeroaware_volume_migration_experiment as ZVM
    ZVM.patch_and_clear()

    initial=PW.basis_full_jhalf()[0]
    psi={initial:1+0j}
    safe=safe_H_sine(psi,0,JMAX2)
    allj,vleak=allJ_H_sine(initial,0,JMAX2)
    err=relerr(allj,safe)
    support_equal=set(allj)==set(safe)

    old=PW.prune_state(PW.apply_H_cached_state(psi,0,JMAX2),TOL)
    overlap=inner(old,safe)
    nold=math.sqrt(norm2(old)); nnew=math.sqrt(norm2(safe))
    fidelity=abs(overlap)**2/max((nold*nnew)**2,1e-60)

    ctrl=classical_trace_control()
    classical_control_pass=(
        ctrl['Y_antihermiticity']<1e-14
        and ctrl['X_hermiticity']<1e-14
        and ctrl['old_plus_trace_abs']<1e-14
        and ctrl['sine_trace_abs']>1e-3
    )
    passed=(
        classical_control_pass
        and len(safe)>0
        and nnew>1e-10
        and err<1e-9
        and support_equal
        and vleak<1e-10
    )
    return {
        'status':'Peter-Weyl Euclidean sine-Hermitian ordering audit',
        'passed':bool(passed),
        'ordering_definition':'H_sine=sum sign*(T-T^dagger)/(2i)',
        'production_code_modified':False,
        'zeroaware_volume_convention':True,
        'classical_trace_control':ctrl,
        'classical_trace_control_passed':bool(classical_control_pass),
        'safe_support':len(safe),
        'allJ_support':len(allj),
        'support_equal':bool(support_equal),
        'safe_norm':nnew,
        'allJ_norm':math.sqrt(norm2(allj)),
        'allJ_vs_safe_relative_error':err,
        'frozen_relative_error_threshold':1e-9,
        'allJ_internal_volume_sector_leakage':vleak,
        'old_plus_support':len(old),
        'old_plus_norm':nold,
        'old_plus_vs_sine_fidelity_squared':float(fidelity),
        'old_plus_vs_sine_relative_difference':relerr(old,safe),
        'largest_allJ_vs_safe_differences':ranked_diffs(allj,safe),
        'interpretation':'PASS means the physically motivated sine-Hermitian ordering is representation-consistent under the same zero-aware all-J machinery. It does not yet prove HDA or fix the overall kappa/beta/hbar normalization.',
        'next_use':'If PASS, rebuild K=[V,H_sine] and C(K) with the same state-to-state charged representation before any Lorentzian K-K-V triple.',
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path)
    a=ap.parse_args(); out=run(); text=json.dumps(out,indent=2); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
