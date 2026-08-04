# CIMFIG — Causal-Invariant Multiway Frame-Infograph Gravity

**Status: research candidate architecture. Not a proven theory of nature.**

This repository keeps only the parts that survived independent numerical audit:

- discrete rewrite / multiway kinematics (Gates C1–C2, Q1–Q2);
- Regge geometry on finite complexes;
- flat 4D Regge gauge structure (discrete diffeomorphisms, Bianchi);
- lattice continuum diagnostics (spectral dimension, blocking).

**Removed / rejected:** numerological fits of particle masses, BIP39 "physics",
Watts–Strogatz \(Kp=N^{-1/3}\) as a derivation of fundamental constants, and
any claim that the code already proves continuum Einstein gravity.

## What is verified (finite, reproducible)

| Check | Result |
|---|---|
| Sine-bridge lattice identities | machine precision |
| Regge action on regular 5-simplex boundary | \(S=21.781786497901\) |
| Off-shell frame/connection gauge (Gate C2) | pass |
| Flat Regge: 8 gauge nulls, Bianchi \(\sim10^{-8}\) | pass |
| Spurious nulls lifted by \(R^2\) term | pass |
| Spectral dimension on 4D torus graph | \(d_s(\infty)\approx 4\) |

## What is **not** claimed

- continuum limit = 4D Einstein–Hilbert;
- quantum measure uniqueness;
- TT kinetic positivity for the *default* sign of \(\sum A\delta\) without convention fix;
- any fit of Standard Model constants from graph parameters.

## Kinetic sign convention (important)

The classical Regge sum \(S=\sum_h A_h\,\delta_h\) as implemented in
`FlatRegge4D.action` yields a Fourier-mode Hessian whose Rayleigh quotient on
continuum-positive TT polarizations is **negative**.

For Euclidean continuum matching (TT kinetic \(\propto +k^2\), conformal
trace \(\propto -k^2\)) use the **kinetic Hessian**

\[
H_{\mathrm{kin}} = -\,H_{\mathrm{Regge}}
\]

in linearised spectrum tests. With this convention:

- TT Rayleigh quotients are positive;
- pure-trace Rayleigh quotients are negative;
- gauge null space and Bianchi identities are unchanged.

See `KINETIC_SIGN.md` and `scripts/test_kinetic_sign.py`.

## Layout

```
CIMFIG_V18_CANDIDATE_THEORY.md   honest candidate text (gates, open problems)
bcqg_unified_verification.py    finite verification suite
bcqg_critical_phase_demo.py     reduced critical-phase demo
scripts/verify_sine_bridge.py   lattice identities
scripts/test_kinetic_sign.py    TT / trace sign after H → −H
KINETIC_SIGN.md                 convention note
```

## Run

```bash
pip install -r requirements.txt
python bcqg_unified_verification.py --profile quick --skip-hda
python scripts/verify_sine_bridge.py
python scripts/test_kinetic_sign.py
```

## Scientific scope (one line)

Finite discrete geometry + gauge + rewrite kinematics, with an explicit
kinetic-sign convention for linearised tests. **Not** a completed quantum
gravity theory and **not** a derivation of continuum Einstein gravity.
