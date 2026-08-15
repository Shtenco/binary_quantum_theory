#!/usr/bin/env python3
"""Symbolic normalization ledger for the declared Thiemann K-K-V stack.

Let

    H_E^phys = n_E H_sine^raw,
    K_raw    = [V,H_sine^raw],
    L_raw    = L(K_raw,K_raw,V).

Using the canonical identities

    K^phys = -[V,H_E^phys]/(i hbar),
    H_corr = -8 L(K^phys,K^phys,V)/(i hbar)^3,

this script verifies

    K^phys = i n_E K_raw / hbar,
    H_corr = 8 i n_E^2 L_raw / hbar^5,

and, for L_raw=i cY Y,

    H_corr = -8 n_E^2 cY Y / hbar^5.

No numerical n_E is chosen.  Its value must come from an independent Euclidean
small-loop/combinatorial normalization audit, not from an HDA fit.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

C_Y = 1.3389293521464034


def complex_pair(z: complex):
    return [float(z.real), float(z.imag)]


def run():
    # Track only dimensionless complex phases and powers of n_E/hbar.
    # Kphys/Kraw = -n_E/i * hbar^-1 = i n_E hbar^-1.
    k_phase = -1.0 / 1j
    k_nE_power = 1
    k_hbar_power = -1

    # Hcorr/Lraw = -8 * (1/i)^3 * (Kphys/Kraw)^2 * hbar^-3.
    outer_phase = -8.0 * (1.0 / 1j) ** 3
    corr_phase = outer_phase * k_phase ** 2
    corr_nE_power = 2 * k_nE_power
    corr_hbar_power = -3 + 2 * k_hbar_power

    # Lraw one-body = i cY Y.
    physical_y_phase = corr_phase * 1j
    physical_y_coeff_over_nE2_hbar5 = physical_y_phase * C_Y

    checks = {
        "K_phase_is_plus_i": abs(k_phase - 1j) < 1e-15,
        "K_nE_power_is_one": k_nE_power == 1,
        "K_hbar_power_is_minus_one": k_hbar_power == -1,
        "correction_phase_is_plus_8i": abs(corr_phase - 8j) < 1e-15,
        "correction_nE_power_is_two": corr_nE_power == 2,
        "correction_hbar_power_is_minus_five": corr_hbar_power == -5,
        "raw_iY_becomes_real_negative_Y": abs(physical_y_phase + 8.0) < 1e-15,
        "frozen_Y_magnitude": abs(abs(physical_y_coeff_over_nE2_hbar5) - 8.0*C_Y) < 1e-12,
    }

    return {
        "status": "conditional symbolic real-normalization relation",
        "passed": all(checks.values()),
        "definitions": {
            "H_E_phys": "n_E * H_sine_raw",
            "K_raw": "[V,H_sine_raw]",
            "L_raw": "L(K_raw,K_raw,V)",
        },
        "canonical_relations": {
            "K_phys": "-[V,H_E_phys]/(i hbar)",
            "H_corr": "-8 L(K_phys,K_phys,V)/(i hbar)^3",
        },
        "K_phys_over_K_raw": {
            "phase": complex_pair(k_phase),
            "n_E_power": k_nE_power,
            "hbar_power": k_hbar_power,
        },
        "H_corr_over_L_raw": {
            "phase_and_real_factor": complex_pair(corr_phase),
            "n_E_power": corr_nE_power,
            "hbar_power": corr_hbar_power,
            "identity": "8 i n_E^2 / hbar^5",
        },
        "raw_onebody": "L_raw=i*c_Y*Y",
        "c_Y": C_Y,
        "physical_onebody_coefficient": "-8*n_E^2*c_Y/hbar^5",
        "coefficient_per_nE2_hbar_minus5": float(physical_y_coeff_over_nE2_hbar5.real),
        "absolute_coefficient_per_nE2_hbar_minus5": float(abs(physical_y_coeff_over_nE2_hbar5)),
        "independent_unknown": "n_E only; determine by Euclidean continuum/combinatorial normalization audit",
        "checks": checks,
        "scope": (
            "Original Thiemann beta=1 sign convention for the declared nested-bracket stack. "
            "General real-beta bookkeeping additionally uses the repository's frozen beta-cancellation identity. "
            "No numerical Euclidean scale, Newton constant or physical energy is inferred here."
        ),
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    out=run(); text=json.dumps(out,indent=2,sort_keys=True); print(text)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text+'\n',encoding='utf-8')
    return 0 if out['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
