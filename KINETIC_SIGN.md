# Kinetic sign convention for linearised Regge tests

## Fact

On the flat 4D Regge background (`FlatRegge4D`), the Hessian of

\[
S_{\mathrm{Regge}}=\sum_h A_h\,\delta_h
\]

has **negative** Rayleigh quotients on continuum TT polarizations that are
known to be positive for Euclidean linearised Einstein–Hilbert.

Finite-difference check on edge lengths with a continuum-positive TT stretch
gives \(d^2S/d\varepsilon^2<0\).

## Convention

Define the **kinetic** quadratic form used for spectrum / graviton tests as

\[
H_{\mathrm{kin}}=-H[S_{\mathrm{Regge}}].
\]

Then, on tested lattice momenta:

| sector | \(H_{\mathrm{kin}}\) Rayleigh |
|---|---|
| TT | \(>0\) |
| pure trace | \(<0\) |

Gauge null vectors and Bianchi residuals are identical for \(H\) and \(-H\).

## Interpretation

This is a **convention choice for continuum matching**, not a proof that the
nonlinear continuum limit is Einstein–Hilbert. Path-integral weighting
(\(e^{iS}\) vs \(e^{-S}\)) and Lorentzian signature remain separate issues.

## Status

- Gauge Ward: pass (independent of overall sign).
- TT kinetic positivity under \(H_{\mathrm{kin}}\): pass on tested \(k\).
- Nonlinear IR Einstein: **open**.
