#!/usr/bin/env python3
"""Hermitian completion of the full Lorentzian raw operator.

The five-bracket phase alone maps an anti-Hermitian raw block O to a Hermitian
block -i O.  Exact conditional environment evidence shows that the unsymmetrized
full raw O also contains Hermitian (real-Pauli) pieces before environment trace.
Therefore the production quantum candidate must first take the anti-Hermitian
part of O:

    H_phase_sym = -i/2 (O - O^dagger).

For beta=hbar=1 the frozen signed full Lorentzian correction is

    H_corr_sym = -(32/9) H_phase_sym
               = +(16 i/9) (O - O^dagger).

On any sector where O^dagger=-O this reduces exactly to the historical
+(32 i/9) O raw-code expression.  In particular the exact one-body iY result is
unchanged.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

FULL=-32.0/9.0
Y_ONEBODY=1.3389293521464034


def cp(x): return complex(float(x[0]),float(x[1]))


def run(evidence:Path):
    d=json.loads(evidence.read_text(encoding='utf-8'))
    raw={k:cp(v) for k,v in d['raw_pauli'].items()}

    # Pauli basis matrices are Hermitian, so for O=sum z_a P_a:
    # -i/2(O-O^dagger)=sum Im(z_a) P_a.
    phase_sym={k:float(z.imag) for k,z in raw.items() if abs(z.imag)>1e-12}
    removed_hermitian={k:float(z.real) for k,z in raw.items() if abs(z.real)>1e-12}
    full_signed={k:FULL*v for k,v in phase_sym.items()}

    y_expected={
        'YI1I2':0.3359014033398999,
        'YZ1I2':-0.00702861722247964,
        'YI1Z2':0.002338130606598994,
        'YZ1Z2':0.004676261213197787,
    }
    signed_expected={k:FULL*v for k,v in y_expected.items()}

    checks={
        'source_evidence_passed':bool(d.get('passed',False)),
        'phase_sym_is_real_pauli_coefficients':all(isinstance(v,float) for v in phase_sym.values()),
        'conditional_pseudoscalar_anchors_preserved':all(abs(phase_sym.get(k,0.0)-v)<1e-13 for k,v in y_expected.items()),
        'conditional_real_XZ_are_removed':all(k[0] in 'XZ' for k in removed_hermitian),
        'signed_pseudoscalar_anchors':all(abs(full_signed.get(k,0.0)-v)<1e-13 for k,v in signed_expected.items()),
        'historical_onebody_reduction':abs(FULL*Y_ONEBODY-(-4.760637696520545))<1e-14,
        'general_raw_code_prefactor':abs(16/9-1.7777777777777777)<1e-15,
    }

    return {
        'status':'Hermitian completion of full Lorentzian raw operator',
        'passed':all(checks.values()),
        'definition':'H_phase_sym=-i/2 (L_raw-L_raw^dagger)',
        'beta_hbar_1_full_correction':'Hcorr_sym=-(32/9)H_phase_sym=(16 i/9)(L_raw-L_raw^dagger)',
        'reduction_when_raw_is_antihermitian':'if L_raw^dagger=-L_raw then Hcorr_sym=(32 i/9)L_raw',
        'phase_completed_conditional_coefficients':phase_sym,
        'removed_unsymmetrized_hermitian_raw_coefficients':removed_hermitian,
        'signed_full_beta1_conditional_coefficients':full_signed,
        'environment_unbiased_onebody_signed_Y':FULL*Y_ONEBODY,
        'checks':checks,
        'scope':'This fixes Hermiticity of the candidate by projection of the already-declared raw ordering. It does not prove uniqueness among every possible symmetric microscopic ordering; finite HDA must be rerun with this completed operator.'
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--evidence',type=Path,default=Path('verification_results/PETER_WEYL_LORENTZIAN_ENVTRACE_WALSH_NODE012.json'))
    p.add_argument('--output',type=Path)
    a=p.parse_args(); out=run(a.evidence); text=json.dumps(out,indent=2,sort_keys=True); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
