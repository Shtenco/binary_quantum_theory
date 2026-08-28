# Genuine Peter-Weyl Lorentzian reversal falsifier for the q=2 orientation/history frontier

## Question

The preceding q=2 history work identified an exact symmetry-allowed channel

\[
Y_L\otimes C_h,
\qquad
C_h=\frac{U-U^\dagger}{2i},
\]

and showed that the minimal orientation-resolved reversible history lift has
this channel as its exact sine part.  That does **not** prove that the actual
gravitational Peter-Weyl dynamics populates the corresponding orientation-odd
sector.

The cheapest genuine-amplitude falsifier is therefore not the full 24-term
Lorentzian node operator.  It is the ordered-triple reversal test

\[
T_{abc}=\operatorname{Tr}_{aux}
\big[C_a(K_{\sin})C_b(K_{\sin})C_c(V)\big],
\]

versus

\[
T_{bac}=\operatorname{Tr}_{aux}
\big[C_b(K_{\sin})C_a(K_{\sin})C_c(V)\big].
\]

Here

\[
H_E^{\sin}=\frac{T-T^\dagger}{2i},
\qquad
K_{\sin}=[V,H_E^{\sin}],
\]

and the existing implementation works at the preregistered safe single-
Lorentzian wall

\[
J_{\max}=\frac72.
\]

---

## Why this is a killer gate

The antisymmetric component

\[
\boxed{
T_{\rm odd}=\frac{T_{abc}-T_{bac}}{2}
}
\]

is the first place where the synthetic epsilon/sign algebra can either survive
or die in **genuine state-to-state Peter-Weyl amplitudes**.

Two outcomes are both scientifically useful.

### Outcome A: nonzero

If

\[
\|T_{abc}-T_{bac}\|>0
\]

well above numerical tolerance, then the real microscopic ordered triple already
contains an orientation-reversal-odd amplitude.  Only then do we spend the
heavier computation on

\[
\sum_{faces}\sum_{\pi\in S_3}
(-1)^{face}\operatorname{sgn}(\pi)
T_{\pi(a,b,c)}
\]

and project the result onto the frozen logical `Y_L` channel.

### Outcome B: zero

If

\[
T_{abc}=T_{bac}
\]

within preregistered tolerance, then this local reversal-odd channel is absent
on the tested microscopic input.  It must not be promoted to a physical
orientation coupling merely because representation theory permits it.

---

## Preregistered numerical decision

The comparison uses the full pruned sparse output states, not only their norms.
Let

\[
r=\frac{\|T_{abc}-T_{bac}\|}
{\max(\|T_{abc}\|,\|T_{bac}\|)}.
\]

The decision bands are frozen before the amplitudes are computed:

```text
r < 1e-9    -> ZERO_WITHIN_PREREGISTERED_TOLERANCE
r > 1e-6    -> NONZERO_GENUINE_ORIENTATION_ODD_AMPLITUDE
otherwise   -> AMBIGUOUS_NUMERICAL_BAND (CI failure; improve precision)
```

The gate therefore does not encode the desired sign of the answer.

---

## What is captured

Each orientation is evaluated in a separate GitHub Actions matrix job to avoid
serially paying the full Peter-Weyl cost twice.  The worker wraps the already
existing

`scripts/peter_weyl_lorentzian_sine_ordered_triple_gate.py`

without changing its operator definitions, and captures the complete final
sparse state accumulated by the existing ordered-triple engine.

The collector reports:

- complete support sizes;
- full-state norms;
- support intersection/differences;
- normalized overlap;
- even and odd half-sum/half-difference norms;
- relative reversal difference;
- largest state-by-state reversal differences;
- a three-way preregistered classification.

---

## Claim boundary

Even a clean nonzero result would **not** yet be

\[
g_{YC}^{gravity}.
\]

There remain two later arrows:

1. ordered triples must be assembled into the full epsilon-oriented Lorentzian
   node operator and projected onto the logical `Y_L` sector;
2. the resulting constraint amplitude must be converted through the legitimate
   physical-history/rigging-map/boundary construction into a relational history
   kernel, after which projection on
   \(Y_L\otimes C_h\) can define the physical history-lock coefficient.

Therefore the status ladder is

```text
minimal history sine coefficient       = +/-1       EXACT KINEMATIC
Hamming orientation-unresolved coeff    = 0          EXACT KINEMATIC
ordered Peter-Weyl reversal amplitude   = THIS GATE  GENUINE MICROSCOPIC
logical epsilon-Lorentzian Y coefficient= NEXT       OPEN
physical history g_YC^gravity           = LATER      OPEN_PHYSICAL
```
