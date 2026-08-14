# Peter–Weyl Lorentzian logical return — safe-cutoff raw certificate

**Status:** finite structural certificate at the single-`H_L` safe wall `Jmax=7/2`.

This note records a completed amplitude calculation.  It does **not** yet claim a fully normalized Hermitian physical Lorentzian Hamiltonian, a mirror-particle mass, antigravity, or a fifth force.

## 1. Operator being tested

The existing sine-ordered Peter–Weyl stack supplies

```text
H_E^sine=(T-T^dagger)/(2i),
K_raw=[V,H_E^sine],
C_e(O)=h_e[h_e^-1,O],
```

and the raw Lorentzian structural ordered triple

```text
T_abc = P Tr_aux[C_a(K_raw) C_b(K_raw) C_c(V)] P.
```

`K_raw` is anti-Hermitian.  Overall `kappa`, `beta`, `hbar` and the final canonical `i`/ordering convention are not inserted in this structural gate.

The doubled-spin parity grading already proves

```text
H_E : odd,
V   : even,
K   : odd,
C(V): even,
C(K): odd,
H_L : even.
```

Therefore

```text
P H_E P=0,
P H_L P is not support-forbidden.
```

## 2. Exact meet-in-the-middle contraction

For raw anti-Hermitian `K`,

```text
C(K)_ij^dagger = -C(K)_ji.
```

Hence the last expensive `C(K)` action can be moved to the bra.  This gives an exact meet-in-the-middle matrix-element contraction and avoids a third full sparse forward expansion.

For one genuine auxiliary path,

```text
(a,b,c)=(1,2,3)
(i,j,k)=(0,0,0)
source K=0 -> K=0
```

the safe-cutoff amplitude is

```text
-0.025487238437494765 + 1.74e-17 i.
```

An independent outer-`C(K)` implementation reproduces this number to about `1.63e-16`.

The physical basis/volume leakage is below `6.7e-16`.

Thus a genuine `C(K) C(K) C(V)` path can return to the logical all-`j=1/2` sector.

## 3. Full auxiliary trace of one ordered triple

For `(a,b,c)=(1,2,3)`,

```text
T_123^log =
[
  [-0.172264469874, -0.089573383497],
  [+0.018688393681, -0.325339605273]
]
+ O(1e-16 i).
```

Its Frobenius norm is

```text
0.379333037620.
```

Raw Pauli coefficients are approximately

```text
I = -0.248802037574
X = -0.035442494908
Z = +0.076537567700
Y = -0.054130888589 i.
```

So the auxiliary trace does not cancel the logical return.

## 4. Complete 24-term epsilon assembly on the frozen logical environment

The complete oriented source-node sum contains

```text
4 omitted faces x 6 signed permutations = 24 ordered triples.
```

All 24 terms were computed independently at `Jmax=7/2` and then assembled by a separate evidence collector.

Machine accounting:

```text
artifact_count        = 24
nonzero triples       = 6
zero triples          = 18
max physical leakage  = 6.694456401674905e-16.
```

The six nonzero triples are exactly the permutations of

```text
(1,2,3).
```

All 18 triples containing edge `4` vanish in this frozen-environment projection.

The complete raw epsilon-oriented source-node logical matrix is

```text
L_raw,eps^log =
[
  [-2.77555756156e-16 +1.92982413038e-16 i,
   +0.36549936197909355 +8.325260015e-17 i],

  [-0.30627499389534 +2.32919722562e-16 i,
   +4.44089209850e-16 -2.46526081707e-16 i]
].
```

Its Frobenius norm is

```text
||L_raw,eps^log||_F = 0.47685863260794076.
```

Raw Pauli coefficients are

```text
I ~ 0
X = +0.029612184041876766
Y = +0.3358871779372168 i
Z ~ 0.
```

Therefore the complete 24-term epsilon assembly does **not** cancel the logical Lorentzian structural return on this frozen boundary.

## 5. Exact orientation/sign projection

The independently proved logical `S4` sign projector has

```text
T_sgn(Y)=Y,
T_sgn(I)=T_sgn(X)=T_sgn(Z)=0.
```

Therefore the orientation-covariant component of the completed frozen-boundary return is solely

```text
c_Y = +0.3358871779372168 i.
```

Its sign-sector matrix is

```text
[
  [0, +0.3358871779372168],
  [-0.3358871779372168, 0]
]
```

up to machine-scale imaginary contamination, with norm

```text
0.475016202466037.
```

The residual raw `X` term is not in the sign irrep and is removed by the exact sign projection.

## 6. Critical environment caveat

The matrix above was evaluated with the other four logical K5 nodes frozen in

```text
K_1=K_2=K_3=K_4=0.
```

It therefore proves a nonzero **frozen-environment raw structural return**, but it does not by itself establish an environment-independent one-body term.

The decisive one-body observable is

```text
Lbar_0
 = (1/16) sum_{K_1,...,K_4 in {0,2}}
   <K_1...K_4| L_raw,eps |K_1...K_4>,
```

with

```text
ell_Y^1body
 = (1/2) Tr[Y Lbar_0].
```

Equivalently on the full five-logical-qubit space,

```text
ell_Y^1body
 = (1/32) Tr[(Y_0 tensor I_env) L_raw,eps].
```

This partial trace is the current killer test.

## 7. Why this matters for mirror order

On the minimal oriented 16-cell, an independent exact gate proves

```text
facet orientation sign
 = (-1)^popcount(v)
 = eta_v.
```

Thus **if and only if** a genuine physical one-body coefficient survives the logical-environment trace and the final Lorentzian normalization/order restoration, its global one-cell pattern has the form

```text
ell_L sum_v eta_v Y_v
 = N ell_L Sigma.
```

For fixed global orientation this is a longitudinal staggered field for the mirror order, not a mediator mass term.  It would lift the ideal `Sigma=+/-1` pair by `2N|ell_L|`.

No such physical splitting is claimed until `ell_Y^1body` and the final canonical prefactor are both closed.

## 8. Current conclusion

What is now established at finite safe cutoff:

```text
individual Lorentzian return path != 0
auxiliary trace of an ordered triple != 0
complete 24-term epsilon sum on frozen environment != 0
orientation/sign component != 0.
```

What remains immediately open:

```text
environment-unbiased one-body Y trace
final canonical Lorentzian prefactor / Hermitian ordering
refinement and continuum behavior.
```

Only after these gates can the result be promoted from a raw structural amplitude to a physical effective Lorentzian logical term.
