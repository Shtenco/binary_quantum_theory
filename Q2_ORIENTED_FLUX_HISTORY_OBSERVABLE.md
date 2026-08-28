# q=2 logical orientation as a microscopic oriented-flux observable

## Exact identity

For four spin-`1/2` face fluxes define the oriented gauge-scalar triple product

\[
Q_{\rm or}=\epsilon_{abc}J_1^aJ_2^bJ_3^c.
\]

Projecting onto the two-dimensional four-valent singlet basis `(K=0,K=2)` gives

\[
\boxed{
Q_{\rm or}^{\rm logical}
=\frac{\sqrt3}{4}Y_L.
}
\]

Equivalently,

\[
\boxed{
Y_L=\frac4{\sqrt3}Q_{\rm or}.
}
\]

Thus the logical orientation Pauli is not merely a bookkeeping label: within the frozen q=2 local geometry carrier it is proportional to a genuine SU(2)-gauge-scalar oriented flux/volume operator.

The gate independently verifies

\[
[Q_{\rm or},J^a_{\rm total}]=0
\]

for all three total SU(2) generators and verifies sign reversal under an odd face permutation.

---

## History-current coupling in microscopic geometry language

The exact minimal history result was

\[
\frac{W-W^\dagger}{2i}=Y_L\otimes C_h.
\]

Using the oriented-flux identity,

\[
\boxed{
\frac{W-W^\dagger}{2i}
=\frac4{\sqrt3}Q_{\rm or}\otimes C_h.
}
\]

So the orientation/history channel can be represented directly using a microscopic gauge-scalar geometry observable.

---

## Lorentzian epsilon extractor

The exact S4 sign-twirl reduction gives, for a canonical logical ordered-triple matrix `O`,

\[
L_\epsilon^{\rm logical}
=-12\operatorname{Tr}(Y_LO)Y_L.
\]

Since

\[
Q_{\rm or}=\frac{\sqrt3}{4}Y_L,
\qquad
\operatorname{Tr}(Q_{\rm or}^2)=\frac38,
\]

this is exactly equivalent to

\[
\boxed{
L_\epsilon^{\rm logical}
=-64\operatorname{Tr}(Q_{\rm or}O)Q_{\rm or}.
}
\]

If the canonical ordered-triple matrix contains

\[
O=b_QQ_{\rm or}+O_\perp,
\]

then the full 24-term sign orbit gives

\[
\boxed{
L_\epsilon^{\rm logical}
=-24b_QQ_{\rm or}.
}
\]

This provides a direct microscopic extractor for the orientation-odd Lorentzian channel.

---

## Relation to the intrinsic-metric no-go

There is no contradiction with the exact result

\[
\partial g/\partial Y=0.
\]

The intrinsic metric forgets orientation, while `Q_or` retains it.

Therefore the correct chain for an orientation-sensitive gravitational observable is not

```text
Y -> linear intrinsic metric -> TT metric source
```

but rather

```text
oriented flux / triad / connection data
-> orientation-sensitive Lorentzian/history amplitude
-> physical relational observable
```

with metric projection performed only when the target observable is actually metric-even.

---

## Physical boundary

This exact operator identity does not yet show that the genuine sine-ordered Peter–Weyl Lorentzian triple has a nonzero `Q_or` component.

The running microscopic reversal test must decide that.

Even a nonzero local coefficient still requires a legitimate physical history/projector construction before it may be interpreted as `g_YC^gravity`.
