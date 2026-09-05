#!/usr/bin/env python3
"""Finite reference gate linking binary-history interference to gravitational wave optics.

This is deliberately a reference/architecture test, not a derivation of the physical BQG
photon kernel. It checks four identities that a future physical history measure must recover:

1. coherent alternatives add as amplitudes and reproduce the two-path interference term;
2. which-path distinguishability suppresses the cross term through an environment overlap;
3. ordinary quadratic/Born composition has zero Sorkin third-order interference I3;
4. in a standard point-lens wave-optics control, the same Fermat potential produces both
   stationary geometric images and their relative propagation phase.

A negative control intentionally uses a different phase potential and must fail stationarity,
preventing an independent post-hoc 'lensing potential' from being fitted to light alone.
"""
from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path
from typing import Iterable, Sequence

TOL = 1e-11


def coherent_intensity(amplitudes: Iterable[complex]) -> float:
    total = sum(amplitudes, 0j)
    return float((total.conjugate() * total).real)


def two_path_environment_intensity(a1: complex, a2: complex, overlap: complex) -> float:
    return float(
        abs(a1) ** 2
        + abs(a2) ** 2
        + 2.0 * (a1 * a2.conjugate() * overlap).real
    )


def sorkin_i3(amplitudes: Sequence[complex]) -> float:
    if len(amplitudes) != 3:
        raise ValueError("I3 control requires exactly three alternatives")
    a, b, c = amplitudes
    i_abc = coherent_intensity([a, b, c])
    i_ab = coherent_intensity([a, b])
    i_ac = coherent_intensity([a, c])
    i_bc = coherent_intensity([b, c])
    i_a = coherent_intensity([a])
    i_b = coherent_intensity([b])
    i_c = coherent_intensity([c])
    i_0 = 0.0
    return i_abc - i_ab - i_ac - i_bc + i_a + i_b + i_c - i_0


def point_lens_fermat(x: float, y: float, potential_scale: float = 1.0) -> float:
    if x == 0.0:
        raise ValueError("point lens Fermat potential is singular at x=0")
    return 0.5 * (x - y) ** 2 - potential_scale * math.log(abs(x))


def point_lens_fermat_grad(x: float, y: float, potential_scale: float = 1.0) -> float:
    return (x - y) - potential_scale / x


def point_lens_images(y: float) -> tuple[float, float]:
    root = math.sqrt(y * y + 4.0)
    return 0.5 * (y + root), 0.5 * (y - root)


def point_lens_signed_magnification(x: float) -> float:
    # Standard axisymmetric point-lens Jacobian in Einstein-radius units.
    return 1.0 / (1.0 - x ** -4)


def wave_optics_two_image_amplitude(y: float, omega_hat: float) -> tuple[complex, dict]:
    xp, xm = point_lens_images(y)
    tp = point_lens_fermat(xp, y)
    tm = point_lens_fermat(xm, y)
    mup = point_lens_signed_magnification(xp)
    mum = point_lens_signed_magnification(xm)

    # The negative-parity image receives the standard Morse phase -pi/2.
    ap = math.sqrt(abs(mup)) * cmath.exp(1j * omega_hat * tp)
    am = math.sqrt(abs(mum)) * cmath.exp(1j * omega_hat * tm - 0.5j * math.pi)
    return ap + am, {
        "x_plus": xp,
        "x_minus": xm,
        "tau_plus": tp,
        "tau_minus": tm,
        "delta_tau": tp - tm,
        "mu_plus_signed": mup,
        "mu_minus_signed": mum,
    }


def run_gate() -> dict:
    # Binary-history two-route control.
    amp1 = math.sqrt(0.37) * cmath.exp(1j * 0.4)
    amp2 = math.sqrt(0.63) * cmath.exp(1j * 1.7)
    direct = coherent_intensity([amp1, amp2])
    expanded = (
        abs(amp1) ** 2
        + abs(amp2) ** 2
        + 2.0 * (amp1 * amp2.conjugate()).real
    )
    two_path_identity_error = abs(direct - expanded)

    coherent_env = two_path_environment_intensity(amp1, amp2, 1.0 + 0j)
    decohered_env = two_path_environment_intensity(amp1, amp2, 0.0 + 0j)
    incoherent_sum = abs(amp1) ** 2 + abs(amp2) ** 2
    decoherence_error = abs(decohered_env - incoherent_sum)
    visibility_loss = abs(coherent_env - decohered_env)

    i3 = sorkin_i3(
        [
            0.6 * cmath.exp(0.2j),
            0.5 * cmath.exp(1.1j),
            0.4 * cmath.exp(-0.7j),
        ]
    )

    # Gravitational wave-optics control: one Fermat potential must control both
    # image positions and phases.
    y = 0.73
    omega_hat = 17.0
    xp, xm = point_lens_images(y)
    grad_p = point_lens_fermat_grad(xp, y)
    grad_m = point_lens_fermat_grad(xm, y)
    stationary_residual = max(abs(grad_p), abs(grad_m))

    amp, lens = wave_optics_two_image_amplitude(y, omega_hat)
    wave_intensity = abs(amp) ** 2
    incoherent_lens_intensity = abs(lens["mu_plus_signed"]) + abs(lens["mu_minus_signed"])
    wave_interference_term = wave_intensity - incoherent_lens_intensity

    # Negative control: keep geometric images from potential_scale=1 but compute
    # the optical phase using a separately fitted scale. Those same image points
    # are no longer stationary points of the phase potential.
    phase_scale_bad = 1.12
    bad_residual = max(
        abs(point_lens_fermat_grad(xp, y, phase_scale_bad)),
        abs(point_lens_fermat_grad(xm, y, phase_scale_bad)),
    )

    passed = all(
        [
            two_path_identity_error < TOL,
            decoherence_error < TOL,
            visibility_loss > 1e-3,
            abs(i3) < TOL,
            stationary_residual < TOL,
            math.isfinite(wave_intensity) and wave_intensity > 0.0,
            abs(wave_interference_term) > 1e-4,
            bad_residual > 1e-3,
        ]
    )

    return {
        "schema_version": 1,
        "passed": passed,
        "status": "tested_finite_reference" if passed else "failed_reference",
        "two_path_identity_error": two_path_identity_error,
        "decoherence_to_incoherent_error": decoherence_error,
        "coherent_minus_decohered_intensity": visibility_loss,
        "sorkin_I3": i3,
        "point_lens_stationary_residual": stationary_residual,
        "point_lens_bad_split_potential_residual": bad_residual,
        "point_lens_wave_intensity": wave_intensity,
        "point_lens_incoherent_intensity": incoherent_lens_intensity,
        "point_lens_interference_term": wave_interference_term,
        "point_lens": lens,
        "scientific_boundary": (
            "This gate proves only reference identities connecting coherent history sums, "
            "decoherence, zero third-order Sorkin interference under a quadratic Born rule, "
            "and the standard wave-optics fact that one Fermat/Weyl potential controls both "
            "lensing stationary paths and their phase. It does not derive the BQG Maxwell "
            "kernel, Born rule, physical photon state, or a theory-specific lensing potential."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    result = run_gate()
    text = json.dumps(result, indent=2, ensure_ascii=False)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
