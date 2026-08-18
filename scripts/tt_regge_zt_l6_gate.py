#!/usr/bin/env python3
"""Reproduce the preregistered L=6 Regge TT-residue continuation.

Scientific scope
----------------
This is a regression/preregistration audit, not a fresh recomputation of the
full Regge Hessian.  The expensive independent calculations that produced the
intensive coefficients Z_L are documented in TT_REGGE_ZT_L6_PREREGISTRATION.md
and TT_REGGE_ZT_L6_RESULT.md.

The rule frozen before opening L=6 was

    Z_L = 1/8 + C/L^2 + D/L^4,

with C,D inferred only from L=3,4,5.  This script reconstructs that prediction,
then opens the already-computed held-out L=6 value and reports the relative
prediction error.  No parameter is refit using L=6.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

TARGET = 1.0 / 8.0
TRAIN_L = np.array([3.0, 4.0, 5.0])
TRAIN_Z = np.array([
    0.1021131745,
    0.1114624530,
    0.1161306996,
])
HELDOUT_L = 6.0
HELDOUT_Z = 0.11876075461190198
FROZEN_PRED_DOCUMENTED = 0.11876923193907167
DOCUMENTED_RELATIVE_ERROR_PERCENT = 0.00714


def fit_without_heldout() -> tuple[float, float]:
    X = np.column_stack((1.0 / TRAIN_L**2, 1.0 / TRAIN_L**4))
    y = TRAIN_Z - TARGET
    C, D = np.linalg.lstsq(X, y, rcond=None)[0]
    return float(C), float(D)


def predict(L: float, C: float, D: float) -> float:
    return TARGET + C / L**2 + D / L**4


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path, default=None)
    args = ap.parse_args()

    C, D = fit_without_heldout()
    z6_pred_reconstructed = predict(HELDOUT_L, C, D)
    rel_error = abs(FROZEN_PRED_DOCUMENTED - HELDOUT_Z) / abs(HELDOUT_Z)
    rel_error_percent = 100.0 * rel_error

    # Rounded README inputs reproduce the preregistered prediction to much
    # better than the scale of the held-out discrepancy.  The canonical frozen
    # value is the more precise number recorded before L=6 was opened.
    reconstruction_delta = abs(z6_pred_reconstructed - FROZEN_PRED_DOCUMENTED)

    passed = (
        reconstruction_delta < 1e-9
        and abs(rel_error_percent - DOCUMENTED_RELATIVE_ERROR_PERCENT) < 5e-5
        and HELDOUT_Z < TARGET
        and FROZEN_PRED_DOCUMENTED < TARGET
    )

    out = {
        "status": "held-out Regge TT residue preregistration regression",
        "passed": bool(passed),
        "continuum_target": TARGET,
        "training_only": {
            "L": TRAIN_L.astype(int).tolist(),
            "Z_L": TRAIN_Z.tolist(),
            "fit_form": "Z_L = 1/8 + C/L^2 + D/L^4",
            "C_from_rounded_public_values": C,
            "D_from_rounded_public_values": D,
        },
        "heldout": {
            "L": int(HELDOUT_L),
            "frozen_prediction_documented": FROZEN_PRED_DOCUMENTED,
            "prediction_reconstructed_from_rounded_values": z6_pred_reconstructed,
            "prediction_reconstruction_delta": reconstruction_delta,
            "observed_independent_value": HELDOUT_Z,
            "relative_prediction_error": rel_error,
            "relative_prediction_error_percent": rel_error_percent,
        },
        "anti_leakage": {
            "heldout_used_in_fit": False,
            "parameters_refit_after_opening_L6": False,
        },
        "scientific_scope": (
            "Reproduces the frozen L=3,4,5 -> L=6 continuation and audits the "
            "documented held-out comparison. It does not recompute the Regge "
            "metric Hessian from simplicial geometry."
        ),
    }

    text = json.dumps(out, indent=2)
    print(text)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")

    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
