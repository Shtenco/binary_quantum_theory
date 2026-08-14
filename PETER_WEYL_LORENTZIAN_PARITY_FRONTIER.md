# Peter-Weyl Lorentzian parity frontier

Status: **exact operator-grading consequence of the declared Euclidean/Lorentzian construction; direct Lorentzian logical amplitude still separate**.

The Euclidean logical-return analysis established a doubled-spin grading

```text
Pi |{s_e}> = (-1)^(sum_e s_e) |{s_e}>,   s_e=2j_e,
```

for which every primitive `H_E` sequence flips exactly three edge-spin parity bits. Therefore

```text
{Pi,H_E}=0.
```

The Lorentzian operator stack has a different grading and this changes the mirror-range frontier.

---

## 1. Operator parities

The local absolute volume does not change link representations:

```text
V : even.
```

Hence

```text
K=[V,H_E] : odd.
```

For any operator `O`, the covariant leg used by the existing Peter-Weyl code is

```text
C_e(O)=h_e[h_e^-1,O]
      =O-h_e O h_e^-1.
```

Conjugation contains two fundamental representation hits, so it preserves doubled-spin parity. Therefore

```text
C(V) : even
C(K) : odd.
```

The frozen Lorentzian structural triple is

```text
H_L ~ Tr_aux[C(K) C(K) C(V)].
```

Thus

```text
H_L : odd * odd * even = even,
```

or

```text
[Pi,H_L]=0.
```

---

## 2. Exact logical-sector consequence

Let `P` project to the even all-`j=1/2` logical sector. Then

```text
P H_E P=0
```

by grading, but

```text
P H_L P
```

is **not** forbidden by grading.

For

```text
G=H_E+lambda H_L,
lambda=1+beta^2,
```

one gets immediately

```text
P G P=lambda P H_L P.
```

Therefore a direct logical term in the full constraint, if one exists, is Lorentzian at leading order.

---

## 3. Master-constraint separation

The mixed product is odd:

```text
H_E H_L + H_L H_E : odd.
```

Hence

```text
P(H_E H_L+H_L H_E)P=0.
```

So on the even logical sector

```text
P G^2 P
 =P H_E^2 P
 +lambda^2 P H_L^2 P.
```

This cleanly separates the Euclidean and Lorentzian pieces at this grading level.

The independently tested two-shell Euclidean master normalization makes the raw `H_E^2` return kernel approach the identity on the full-rank logical support. That makes the direct Lorentzian projection the next higher-priority full-theory test.

---

## 4. New killer test

The next amplitude question is simply

```text
P H_L P = 0 ?
```

More precisely, the first executable gate evaluates the full 24-term epsilon-oriented raw sine-ordered K-K-V node sum at `Jmax=7/2`, projects its final `J=0` covariant state back to the all-`j=1/2` Gauss logical sector and asks whether any logical matrix element survives.

Outcomes:

```text
P H_L P = 0
  -> leading Lorentzian logical mass is absent at this finite node test;
     normalized Euclidean higher-shell Lambda becomes the next geometric source.

P H_L P != 0
  -> support and genuine amplitudes permit a direct Lorentzian logical term;
     next compute its Hermitian completion, mirror/S4 decomposition and unbiased environment trace.
```

Neither outcome by itself establishes a physical mirror force.

---

## Reproduction

```bash
python scripts/peter_weyl_lorentzian_parity_gate.py
```

The direct amplitude test is separately implemented in

```text
scripts/peter_weyl_lorentzian_logical_projection_gate.py
```

on its research branch until the expensive calculation is complete.

---

## Scientific scope

This is a selection-rule result inside a candidate quantum-gravity construction. It does not establish a physical mirror sector, antigravity, a fifth force or a mediator mass. In particular parity only says that `P H_L P` is allowed; it does not say the amplitude is nonzero.
