# Joint cutoff diagonal certificate

Status: **conditional analytic certificate + executable finite staircase check**.

The fixed-cutoff Lorentzian-route composition theorem leaves one higher-level question: can the spin cutoff grow while the regulator is removed without losing suppression of the non-route channels?

The retained norm envelope is

\[
\frac{C_{cross}}{D}=O(\epsilon J_{max}^{13/2}),
\qquad
\frac{C_{GG}}{D}=O(\epsilon^2J_{max}^{13}).
\]

Set

\[
J_{max}(\epsilon)\sim\epsilon^{-\alpha}.
\]

Then

\[
\frac{C_{cross}}{D}=O\!\left(\epsilon^{1-13\alpha/2}\right),
\qquad
\frac{C_{GG}}{D}=O\!\left(\epsilon^{2-13\alpha}\right).
\]

Both exponents are strictly positive iff

\[
\boxed{0<\alpha<2/13}.
\]

Thus the fixed-cutoff certificate already supplies a nonempty cone of admissible power-law diagonals, conditional on the stated polynomial norm envelope.

## Canonical interior trajectory

Freeze

\[
\boxed{\alpha=1/8}.
\]

Then

\[
1-\frac{13}{2}\frac18=\frac{3}{16},
\qquad
2-13\frac18=\frac38,
\]

so

\[
\boxed{
C_{cross}/D=O(\epsilon^{3/16}),
\qquad
C_{GG}/D=O(\epsilon^{3/8}).
}
\]

The trajectory

\[
\boxed{J_{max}\sim\epsilon^{-1/8}}
\]

therefore sends `epsilon -> 0` and `Jmax -> infinity` simultaneously while preserving decay of both declared contamination bounds.

## Negative controls

At the boundary

\[
\alpha=2/13,
\]

both exponents are exactly zero. The bound alone therefore does not imply decay.

For the supercritical example

\[
\alpha=1/6,
\]

the exponents become

\[
-1/12,
\qquad
-1/6,
\]

so the declared envelope grows rather than decays.

These controls prevent the certificate from being misread as permission to take an arbitrary joint cutoff path.

## Reproduction

```bash
python scripts/joint_cutoff_diagonal_gate.py \
  --output verification_results/JOINT_CUTOFF_DIAGONAL.json
```

The executable also quantizes `Jmax` to a half-integer staircase and verifies that both finite-window envelopes decrease along the canonical path.

## Scope

This result establishes an explicit admissible simultaneous-cutoff trajectory and, more generally, the conditional power-law cone `0<alpha<2/13`.

It is **not** a uniform theorem over arbitrary `Jmax(epsilon)`, arbitrary input spin sectors, arbitrary beta, or arbitrary operator norms. A full uniform bound remains open.
