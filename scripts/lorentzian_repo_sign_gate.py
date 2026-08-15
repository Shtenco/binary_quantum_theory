#!/usr/bin/env python3
"""Freeze the signed Lorentzian coefficient in the repository convention.

Already frozen upstream:

    H_E^phys = n_E H_sine^raw,          n_E=-2/(3 hbar)
    K_phys   = -[V,H_E^phys]/(i hbar)
    H_corr   = -8 L(K_phys,K_phys,V)/(i hbar)^3
    H_phase  = -i L_raw
    G        = H_E + (1+beta^2) H_L.

The sign is therefore algebraic, not an HDA fit:

    H_corr/H_phase = -8 n_E^2/hbar^5
                       = -32/(9 hbar^7).

At beta=1, G=H_E+2 H_L, hence

    H_L/H_phase = -16/(9 hbar^7).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

C_L=1.3389293521464034
RAW_PAIR_SPLIT=42.84573926868491


def run(hbar=1.0,beta=1.0):
    if hbar<=0:
        raise ValueError('hbar must be positive')
    nE=-2.0/(3.0*hbar)

    # Kphys/Kraw = -nE/(i hbar) = i*nE/hbar.
    k_phase=1j*nE/hbar

    # Hcorr/Lraw = -8/(i hbar)^3 * (Kphys/Kraw)^2.
    corr_over_lraw=(-8.0/(1j*hbar)**3)*(k_phase**2)

    # Hphase=-i Lraw => Lraw=i Hphase.
    corr_over_phase=corr_over_lraw*1j
    expected_corr=-32.0/(9.0*hbar**7)

    # Repository G=HE+(1+beta^2)HL.
    bare_over_phase=corr_over_phase/(1.0+beta**2)
    expected_bare=expected_corr/(1.0+beta**2)

    local_corr=corr_over_phase*C_L
    local_bare=bare_over_phase*C_L
    pair_corr=corr_over_phase*RAW_PAIR_SPLIT
    pair_bare=bare_over_phase*RAW_PAIR_SPLIT

    checks={
        'nE_signed':abs(nE+2.0/(3.0*hbar))<1e-15,
        'K_phase':abs(k_phase-1j*nE/hbar)<1e-15,
        'Hcorr_over_Lraw_is_plus_i_32_over_9_at_hbar1':(
            abs(corr_over_lraw-32j/9)<1e-14 if hbar==1.0 else True
        ),
        'Hcorr_over_Hphase_signed':abs(corr_over_phase-expected_corr)<1e-14,
        'bare_repo_HL_signed':abs(bare_over_phase-expected_bare)<1e-14,
        'beta1_bare_is_minus_16_over_9':(
            abs(bare_over_phase+16.0/9.0)<1e-14 if hbar==1.0 and beta==1.0 else True
        ),
        'local_coefficients_real':abs(local_corr.imag)<1e-14 and abs(local_bare.imag)<1e-14,
        'pair_coefficients_real':abs(pair_corr.imag)<1e-12 and abs(pair_bare.imag)<1e-12,
    }
    return {
        'status':'conditional signed Lorentzian coefficient in frozen repository convention',
        'passed':all(checks.values()),
        'hbar':hbar,
        'beta':beta,
        'n_E':nE,
        'Hcorr_over_Lraw':[float(corr_over_lraw.real),float(corr_over_lraw.imag)],
        'Hcorr_over_Hphase':float(corr_over_phase.real),
        'Hcorr_over_Hphase_identity':'-32/(9 hbar^7)',
        'bare_HL_over_Hphase':float(bare_over_phase.real),
        'bare_HL_over_Hphase_identity':'-32/[9 hbar^7 (1+beta^2)]',
        'beta1_bare_identity':'-16/(9 hbar^7)',
        'local_phase_completed_raw_cL':C_L,
        'local_full_correction_coefficient':float(local_corr.real),
        'local_bare_HL_coefficient':float(local_bare.real),
        'raw_16cell_pair_split':RAW_PAIR_SPLIT,
        'full_correction_pair_split_signed':float(pair_corr.real),
        'bare_HL_pair_split_signed':float(pair_bare.real),
        'checks':checks,
        'fitting_used':False,
        'scope':(
            'The sign is conditional on the already declared Thiemann correction sign and the repository definition '
            'G=H_E+(1+beta^2)H_L. A common overall sign reversal of the entire Hamiltonian constraint is physically '
            'different from flipping only H_L and does not reopen this relative sign.'
        ),
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--hbar',type=float,default=1.0)
    ap.add_argument('--beta',type=float,default=1.0)
    ap.add_argument('--output',type=Path)
    a=ap.parse_args(); out=run(a.hbar,a.beta); text=json.dumps(out,indent=2,sort_keys=True); print(text)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
