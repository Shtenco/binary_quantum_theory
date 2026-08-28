# From one q=2 C4 phase plane to dense and continuous U(1)

**Status:** exact arithmetic/representation theorem. This route shows that an infinite exact finite-level root tower is **not necessary** for continuous phase emergence.

The history-refinement branch initially targeted

```text
C4 -> C8 -> C16 -> ... -> U(1).
```

That remains a valid sufficient route if recursive physical carry locking is eventually derived.

But there is a shorter theorem.

The q=2 carrier already gives one real complex structure

\[
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\qquad J^2=-I.
\]

Once ordinary rational coefficients are available, the unit elements of

\[
\mathbb Q[J]
\]

already form a **dense subgroup of the circle**. Archimedean completion then closes that dense subgroup to the full continuous

\[
SO(2)\cong U(1).
\]

So the conceptual route can be

\[
\boxed{
C_4\to J,
\qquad
\text{history}\to\mathbb Z\to\mathbb Q,
\qquad
\mathbb Q[J]\text{ unit phases dense},
\qquad
\mathbb Q\to\mathbb R,
\qquad
U(1).
}
\]

No exact `mu_8`, `mu_16`, ... need be fundamental phase alphabets.

---

## 1. The C4 already gives the entire two-dimensional phase plane

Take

\[
J^2=-I.
\]

For any ordinary scalars `a,b`, define

\[
Z(a,b)=aI+bJ.
\]

Because

\[
J^2=-I,
\]

multiplication gives

\[
Z(a,b)Z(c,d)
=Z(ac-bd,ad+bc).
\]

This is exactly complex multiplication.

Thus

\[
\boxed{
\mathbb R[J]\cong\mathbb C
}
\]

and already

\[
\boxed{
\mathbb Q[J]\cong\mathbb Q(i).
}
\]

The q=2 phase plane does not need new basis directions. It only needs increasingly rich ordinary coefficients along the two existing directions `I` and `J`.

---

## 2. Unit phases are ordinary rotation matrices

For

\[
Z=aI+bJ
=
\begin{pmatrix}
a&-b\\
b&a
\end{pmatrix},
\]

we have

\[
Z^TZ=(a^2+b^2)I
\]

and

\[
\det Z=a^2+b^2.
\]

Therefore

\[
\boxed{
a^2+b^2=1
\iff
Z\in SO(2).
}
\]

So the unit phase group is simply

\[
\boxed{
\{aI+bJ:a^2+b^2=1\}=SO(2)\cong U(1).
}
\]

This contains the original q=2 fourth roots

```text
 1  -> ( 1, 0)
 i  -> ( 0, 1)
-1  -> (-1, 0)
-i  -> ( 0,-1)
```

as four special points.

---

## 3. Rational unit phases exist exactly

For integers `p,q`, not both zero, define

\[
\boxed{
a=\frac{q^2-p^2}{p^2+q^2},
\qquad
b=\frac{2pq}{p^2+q^2}.
}
\]

Then exactly

\[
(q^2-p^2)^2+(2pq)^2=(p^2+q^2)^2,
\]

so

\[
\boxed{a^2+b^2=1}
\]

with

\[
a,b\in\mathbb Q.
\]

Examples:

\[
(p,q)=(1,2)
\Rightarrow
(a,b)=\left(\frac35,\frac45\right),
\]

\[
(p,q)=(2,3)
\Rightarrow
(a,b)=\left(\frac5{13},\frac{12}{13}\right),
\]

\[
(p,q)=(3,5)
\Rightarrow
(a,b)=\left(\frac8{17},\frac{15}{17}\right).
\]

These are exact unit phases generated only by ordinary integer and rational arithmetic plus the already-derived `J`.

---

## 4. Rational phases are dense on the circle

Use stereographic parameter

\[
t=\frac pq\in\mathbb Q.
\]

Then

\[
(a,b)
=\left(
\frac{1-t^2}{1+t^2},
\frac{2t}{1+t^2}
\right).
\]

Because

\[
\mathbb Q
\]

is dense in

\[
\mathbb R
\]

and this map is continuous away from the single missing pole, while that pole itself is the rational point `(-1,0)`, the rational points on the unit circle are dense:

\[
\boxed{
\overline{S^1(\mathbb Q)}=S^1.
}
\]

Equivalently,

\[
\boxed{
\overline{\{aI+bJ:\ a,b\in\mathbb Q,\ a^2+b^2=1\}}
=SO(2).
}
\]

So a continuous-looking phase does not require a primitive continuous complex number at the microscopic level.

---

## 5. The exact finite root tower is therefore optional

This is the key correction.

The history branch found a valid first refinement

\[
C_4\to C_8
\]

in the minimal reversible history dilation.

But to get continuous phase it is **not necessary** to prove

\[
C_8\to C_{16}\to C_{32}\to\cdots
\]

as a literal sequence of physical finite state spaces.

Instead:

1. `C4` supplies the oriented two-plane and `J`;
2. complete history supplies ordinary integer winding;
3. field/rational construction supplies `Q` coefficients;
4. rational unit phases are already dense;
5. Archimedean completion supplies `R` coefficients;
6. the unit shell of `R[J]` is exactly `U(1)`.

Thus

\[
\boxed{
C_4
+\mathbb Q\text{ coefficients}
\to\text{dense }U(1),
}
\]

and

\[
\boxed{
C_4
+\mathbb R\text{ coefficients}
\to U(1)\text{ exactly}.
}
\]

---

## 6. Why `mu8` can still appear without being fundamental

The phase

\[
e^{i\pi/4}
=\frac{1+i}{\sqrt2}
\]

is not a rational point of the circle because `1/sqrt(2)` is irrational.

So exact `mu8` is **not** inside `Q(i)`.

That is useful: it shows the two routes are genuinely different.

### History-spectrum route

The minimal reversible `C8` history dilation contains exact eighth roots at finite history dimension.

### Coefficient-completion route

`Q(i)` contains a dense set of rational phases but not exact `mu8`. After Archimedean completion, `sqrt(2)` exists and exact

\[
\frac{1+i}{\sqrt2}
\]

appears automatically.

Thus finite exact higher roots are not prerequisites for continuous phase; they can emerge either spectrally from enlarged history or analytically from completion.

---

## 7. Connection to history winding

The new history theorem gives

\[
\boxed{
\text{complete oriented cycle history}
\to
n\in\mathbb Z
\to
w\in\mathbb Z.
}
\]

The previous arithmetic bridge gives the canonical field extension

\[
\mathbb Z\to\mathbb Q
\]

and then, after selecting the Archimedean absolute value,

\[
\mathbb Q\to\mathbb R.
\]

Combining with q=2 phase orientation gives

\[
\boxed{
\begin{aligned}
q=2\ C_4&\to J^2=-I,\\
\text{history}&\to\mathbb Z,\\
\operatorname{Frac}(\mathbb Z)&\to\mathbb Q,\\
\overline{\mathbb Q}^{|\cdot|_\infty}&\to\mathbb R,\\
\mathbb R[J]_{|z|=1}&\to U(1).
\end{aligned}
}
\]

This is now the shortest exact mathematical bridge in the project from finite q=2 orientation to continuous complex phase.

---

## 8. Physical claim boundary

The mathematical closure does **not** yet establish that nature chooses this route.

Still open physically:

1. the gravitational physical-history/projector measure must actually retain the path information whose universal cover gives the integer lift;
2. the physical observable algebra must justify the ordinary field/rational operations used to pass from integer counts to rational coefficients;
3. macroscopic rods/clocks or another microscopic principle must select the Archimedean completion rather than a p-adic/profinite completion;
4. the real coefficients must be the physical amplitude coordinates of the derived history theory, not merely available arithmetic numbers.

But one major bottleneck is removed:

\[
\boxed{
\text{recursive exact root doubling is not required for }U(1)\text{ emergence}.
}
\]

---

## 9. Reproduction

```bash
python scripts/q2_rational_phase_dense_u1_gate.py \
  --output verification_results/Q2_RATIONAL_PHASE_DENSE_U1.json
```

The gate verifies exact Pythagorean norm identities, exact `SO(2)` matrices, multiplicative closure, the `a+bi <-> aI+bJ` homomorphism and a finite density control with increasing integer bounds.
