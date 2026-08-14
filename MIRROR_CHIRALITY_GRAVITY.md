# Mirror chirality, oriented phase and the antigravity falsifier

Status: **exact finite mirror-geometry gate + exact conjugate-anomaly identity + negative result for antigravity in the current mirror-even metric sector**.

This note tests the idea that a second, mirrored binary branch could encode opposite orientation/chirality and perhaps a different gravitational sign.

The calculation gives a sharp split:

1. a genuine mirror/orientation degree of freedom exists naturally in the logical geometry qubit;
2. the current metric observables are even under that mirror;
3. therefore mirror orientation alone does **not** reverse `g00` or gravity;
4. a gravity-sign difference would require a new parity-odd or multi-metric coupling, which must then pass the HDA again.

The result is useful precisely because it separates a real chirality mechanism from an unsupported identification of antimatter with negative energy.

---

## 1. Exact mirror operation on the logical geometry qubit

The frozen four-face singlet qubit obeys

\[
J_1\!\cdot J_2=-\frac14 I-\frac12 Z_L,
\]

\[
J_1\!\cdot J_3=-\frac14 I+\frac14 Z_L-\frac{\sqrt3}{4}X_L,
\]

and the oriented triple product is

\[
Q=J_1\!\cdot(J_2\times J_3)=\frac{\sqrt3}{4}Y_L.
\]

In the real singlet basis the natural mirror operation is complex conjugation

\[
\mathcal M=K,
\qquad i\mapsto-i.
\]

Therefore

\[
\mathcal M X_L\mathcal M^{-1}=X_L,
\qquad
\mathcal M Z_L\mathcal M^{-1}=Z_L,
\]

but

\[
\boxed{\mathcal M Y_L\mathcal M^{-1}=-Y_L}
\]

and hence

\[
\boxed{\mathcal M Q\mathcal M^{-1}=-Q.}
\]

So the mirror operation flips **oriented volume** while preserving the two intrinsic shape coordinates.

The two exact oriented-volume eigenvalues are

\[
Q_\pm=\pm\frac{\sqrt3}{4}
      =\pm0.433012701892\ldots
\]

and the finite gate finds that complex conjugation swaps the two eigenstates with overlap

```text
0.9999999999999998
```

while the shape expectations agree to machine precision.

This makes the natural orientation bit

\[
\boxed{\chi=\operatorname{sgn}Q\in\{+1,-1\}.}
\]

It is a real binary variable, but it is an **orientation/chirality label**, not a negative-energy label.

---

## 2. A reflected tetrahedron changes orientation but not its metric

Let the three edge vectors from one tetrahedron vertex form

\[
A=(a,b,c).
\]

Its intrinsic Gram metric is

\[
G=A^T A.
\]

Take an improper orthogonal reflection `R` with

\[
R^TR=I,
\qquad \det R=-1,
\]

and define

\[
A'=RA.
\]

Then

\[
G'=(A')^TA'=A^TR^TRA=A^TA=G,
\]

while

\[
\det A'=\det R\,\det A=-\det A.
\]

Therefore

\[
\boxed{\text{orientation flips, metric does not.}}
\]

The absolute volume also remains unchanged:

\[
|\det A'|=|\det A|.
\]

The face-area vectors are pseudovectors.  Their Gram matrix is likewise mirror invariant.

The executable gate checks this on 256 deterministic random non-degenerate tetrahedra and obtains, in double precision,

```text
max metric-Gram error       = 0
max absolute-volume error   = 0
max orientation-flip error  = 0
max face-flux-Gram error    = 0
```

This is the central negative result for the antigravity idea:

> the current geometric variables can distinguish the **sign of orientation**, but the metric built from them is insensitive to that sign.

---

## 3. What “pi runs in the mirror direction” can mean rigorously

The number

\[
\pi=3.14159265\ldots
\]

is not replaced by a reversed decimal expansion in a mirror branch.

The mathematically meaningful reversal is an **oriented phase**:

\[
\theta\mapsto-\theta,
\]

or equivalently

\[
\boxed{e^{i\theta}\mapsto e^{-i\theta}.}
\]

Thus an oriented half-turn may be labelled

\[
\pi_\chi=\chi\pi,
\qquad \chi=\pm1.
\]

The two paths around the phase circle have opposite orientation, but the endpoint is the same:

\[
e^{+i\pi}=e^{-i\pi}=-1.
\]

The finite phase gate verifies complex-conjugation reversal exactly on a grid of phases; the numerical endpoint mismatch at `+pi/-pi` is only floating-point roundoff,

```text
2.45e-16.
```

So the project-local phrase “mirror pi” should mean **opposite phase orientation**, not a new value of pi.

---

## 4. Why current GR/HDA geometry is mirror-even

The classical Hamiltonian selected by the repository's HDA/DeWitt result is

\[
H[N]=\int d^3x\,N\left[
\frac{\pi_{ab}\pi^{ab}-\frac12\pi^2}{\sqrt q}
-\sqrt q\,R
\right].
\]

It is built from the spatial metric `q_ab`, its curvature and parity-even tensor contractions of `pi_ab`.

A spatial reflection changes orientation but does not change scalar metric invariants.  Therefore the standard branch has

\[
H[\chi]=H[-\chi]
\]

at the metric level.

Likewise, in ADM variables

\[
g_{00}=-N^2+q_{ab}N^aN^b
\]

contains no standalone orientation sign.  Hence the current candidate architecture gives

\[
\boxed{g_{00}(+\chi)=g_{00}(-\chi)}
\]

for mirror-related configurations with the same physical metric data.

Therefore

\[
\boxed{\delta g_{00}^{\rm mirror}=0}
\]

in the currently tested mirror-even sector.

This means **no antigravity follows from orientation reversal alone**.

---

## 5. A clean phenomenological threshold for an orientation-odd gravity sector

Suppose a future extension adds an orientation-odd acceleration contribution

\[
\mathbf a_\chi=\mathbf a_{\rm even}+\chi\,\mathbf a_{\rm odd}.
\]

Calibrate the observed `chi=+1` branch to ordinary gravity:

\[
\mathbf a_+=\mathbf g_N.
\]

Define the signed fraction

\[
f=\frac{a_{\rm odd}}{g_N}
\]

along the gravitational direction.  Then the opposite mirror branch obeys

\[
\boxed{\frac{a_-}{g_N}=1-2f.}
\]

Therefore:

```text
f = 0      -> identical gravity in both orientations
f = 1/2    -> complete screening in the mirror branch
f > 1/2    -> mirror branch becomes repulsive
f = 1      -> equal-magnitude opposite acceleration
```

The finite mirror gate finds that the currently reconstructed metric belongs to the first case:

\[
\boxed{f_{\rm current}=0.}
\]

So a nonzero `f` is not already hidden in the existing geometry.  It requires genuinely new dynamics.

---

## 6. The minimal new operator and its danger

On the logical qubit, the simplest mirror-odd geometry operator is `Y_L` itself:

\[
H_{\rm odd}=\lambda_\chi Y_L.
\]

Because

\[
\mathcal M Y_L\mathcal M^{-1}=-Y_L,
\]

this term splits the two orientation states.

But adding it by hand is **not** yet a viable gravity theory.  The full Hamiltonian would be

\[
H=H_0+\lambda_\chi H_\chi
\]

and its constraint algebra becomes

\[
[H,H]
=[H_0,H_0]
+\lambda_\chi\big([H_0,H_\chi]+[H_\chi,H_0]\big)
+\lambda_\chi^2[H_\chi,H_\chi].
\]

Every new term must either reproduce the same diffeomorphism generator or belong to a new consistent first-class constraint.

So the decisive antigravity test is not merely

```text
is lambda_chi nonzero?
```

but

```text
is lambda_chi nonzero AND does the modified HDA remain first class?
```

The current repository has not passed such a parity-odd HDA gate.

---

## 7. Chirality can couple without producing antigravity

There is a more conservative and natural possibility.

For a fermion, the axial density

\[
J_5^0=\bar\psi\gamma^0\gamma^5\psi
\]

is parity odd.  Since the oriented geometry coordinate `Y_L` is also mirror odd, the product

\[
\boxed{H_{\chi\psi}=\lambda_{\chi\psi}Y_L J_5^0}
\]

is parity even.

This provides a possible route

```text
orientation qubit
 -> left/right fermion preference
```

without changing the sign of the metric or gravitational energy.

That distinction is important: **mirror geometry may help explain chirality even if it gives no antigravity at all.**

---

## 8. Exact conjugate-pair anomaly sign

For a left-handed Weyl fermion in representation `R`, the perturbative cubic gauge-anomaly coefficient is proportional to

\[
d_R^{abc}
=\operatorname{Tr}_R\!\left[T^a\{T^b,T^c\}\right].
\]

For the conjugate representation,

\[
T_{\bar R}^a=-(T_R^a)^T.
\]

Therefore

\[
\begin{aligned}
d_{\bar R}^{abc}
&=\operatorname{Tr}\left[T_{\bar R}^a
\{T_{\bar R}^b,T_{\bar R}^c\}\right]\\
&=-\operatorname{Tr}\left[
\left(T_R^a\{T_R^b,T_R^c\}\right)^T
\right]\\
&=-d_R^{abc}.
\end{aligned}
\]

Thus an exact mirror-conjugate pair satisfies

\[
\boxed{d_R^{abc}+d_{\bar R}^{abc}=0.}
\]

The finite gate stress-tests this transpose identity on deterministic noncommuting Hermitian generators and obtains residual

```text
2.26e-15
```

(up to deterministic RNG details, always at machine precision).

This is a genuine anomaly-cancellation mechanism for a paired conjugate sector.

It is **not** yet a derivation of the Standard Model fermion spectrum, hypercharges, global anomalies or the observed absence of light mirror fermions.  A realistic model must explain why the visible low-energy sector remains chiral rather than simply becoming vector-like.

---

## 9. Antimatter is not the same object as the mirror orientation bit

The following operations must not be identified:

```text
C   charge conjugation: particle <-> antiparticle
P   parity: spatial mirror / left <-> right
chi orientation: sign of the project-local oriented geometry coordinate
```

A physical antiparticle has positive excitation energy.  Standard quantum field theory does not interpret observable antimatter as macroscopic negative-energy matter.

This also has a direct experimental gravity check.  The ALPHA Collaboration measured trapped antihydrogen released in the Earth's field and found acceleration directed toward Earth, consistent with ordinary attractive gravity.  Their 2023 result rules out repulsive `1g` gravity for antihydrogen.

Reference:

E. K. Anderson et al. (ALPHA Collaboration), *Observation of the effect of gravity on the motion of antimatter*, Nature 621, 716–722 (2023), DOI `10.1038/s41586-023-06527-1`.

Therefore any CIMFIG mirror-antigravity sector must **not** simply relabel ordinary antimatter as `chi=-1` unless it also confronts this experimental result.

---

## 10. Relation to parity-odd gravity with fermions

Parity-odd structures are not foreign to first-order gravity.  The Holst/Immirzi sector is parity sensitive, and with fermions torsion can generate parity-sensitive contact interactions.  This shows that a chirality-gravity bridge is mathematically plausible.

However known Holst/Einstein-Cartan parity effects do not by themselves imply a reversal of gravitational attraction or negative `g00` response.

Useful primary references include:

- D. Benedetti and S. Speziale, *Perturbative quantum gravity with the Immirzi parameter*, arXiv:1104.4028.
- M. Bojowald and R. Das, *Canonical Gravity with Fermions*, arXiv:0710.5722.

The project therefore treats parity-odd matter coupling as motivation for a new gate, not as evidence that antigravity already exists.

---

## 11. What is now closed and what remains open

### Exact / finite result

- the logical geometry qubit has a mirror operation `K` with `X,Z` even and `Y,Q` odd;
- the two oriented-volume states are exact mirror partners;
- reflected tetrahedra have opposite orientation but identical metric Gram data and absolute volume;
- oriented phase reversal is `theta -> -theta`, not reversal of the digits of pi;
- an exact conjugate representation pair has opposite perturbative cubic gauge-anomaly coefficient.

### Negative result

Within the current mirror-even metric/HDA architecture,

\[
\boxed{\chi\to-\chi\quad\not\Rightarrow\quad g_{00}\to-g_{00}.}
\]

So the present theory does **not** derive antigravity from chirality, mirror geometry or antimatter.

### New falsifiable research branch

To obtain gravity screening or repulsion from mirror orientation one must construct an additional orientation-odd or multi-metric operator and then pass all of the following:

1. nonzero mirror response `a_odd`;
2. `f >= 1/2` for actual screening and `f > 1/2` for repulsion;
3. bounded-below/stable physical Hamiltonian;
4. first-class modified HDA;
5. compatibility with positive-energy matter and existing antimatter-gravity data;
6. a realistic chiral matter spectrum with all local and global anomalies cancelled.

That is the precise antigravity bottleneck after the mirror calculation.

---

## Reproduction

```bash
python scripts/mirror_chirality_gravity_gate.py \
  --trials 256 \
  --output verification_results/MIRROR_CHIRALITY_GRAVITY.json
```
