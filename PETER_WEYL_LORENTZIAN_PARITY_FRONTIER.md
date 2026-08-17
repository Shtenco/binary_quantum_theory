# Peter-Weyl Lorentzian parity frontier

Status: **exact operator-grading consequence of the declared Euclidean/Lorentzian construction; direct Lorentzian logical amplitude remains a separate calculation**.

The Euclidean logical-return analysis uses the doubled-spin grading

```text
Pi |{s_e}> = (-1)^(sum_e s_e) |{s_e}>,   s_e=2j_e,
```

for which every primitive `H_E` sequence flips exactly three edge-spin parity bits. Therefore

```text
{Pi,H_E}=0.
```

The purpose of this note is only to classify which logical operator channels are permitted by that grading.

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

For any operator `O`, the covariant leg used by the Peter-Weyl code is

```text
C_e(O)=h_e[h_e^-1,O]
      =O-h_e O h_e^-1.
```

Conjugation contains two fundamental representation hits and therefore preserves doubled-spin parity:

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

by grading, whereas

```text
P H_L P
```

is **allowed** by grading.

For

```text
G=H_E+lambda H_L,
lambda=1+beta^2,
```

one obtains

```text
P G P=lambda P H_L P.
```

This does not imply that the matrix element is nonzero; it only says parity does not force it to vanish.

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

Therefore on the even logical sector

```text
P G^2 P
 =P H_E^2 P
 +lambda^2 P H_L^2 P.
```

This separates Euclidean and Lorentzian contributions at the level of the declared grading.

---

## 4. Next amplitude test

The next finite operator question is simply

```text
P H_L P = 0 ?
```

A direct calculation must evaluate the epsilon-oriented Lorentzian node sum, project the result back to the all-`j=1/2` Gauss/logical sector and report the matrix elements without interpreting a nonzero coefficient as a new degree of freedom.

Possible outcomes:

```text
P H_L P = 0
  -> this direct logical Lorentzian channel vanishes at the tested cutoff.

P H_L P != 0
  -> parity and support permit a direct Lorentzian logical term;
     its Hermitian completion, S4 decomposition and regulator dependence
     must then be computed.
```

Neither outcome by itself changes the physical particle content of the model.

---

## Reproduction

```bash
python scripts/peter_weyl_lorentzian_parity_gate.py
```

---

## Scientific scope

This is a selection-rule result inside a candidate quantum-gravity construction. It establishes only the `Z2` grading of the declared finite operators. It does not establish a nonzero Lorentzian logical amplitude, an additional particle, a mediator, a new long-range interaction, or a physical scale.
