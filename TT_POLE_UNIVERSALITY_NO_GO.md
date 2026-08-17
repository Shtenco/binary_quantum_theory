# TT pole universality: six -> one -> zero

Status: **exact effective-theory symmetry statement under explicitly stated assumptions.**

This document sharpens the interpretation of the six-dimensional `S4` quartic TT space.  The six coefficients are the complete space of parity-even **spatially tetrahedral** order-`k^4` pole deformations.  They are not guaranteed to survive the physical continuum limit.

The hierarchy is

\[
\boxed{
S_4\text{-covariant quartic TT pole space}:\ 6
\supset
SO(3)\text{-invariant spatial pole space}:\ 1
\supset
\text{local Lorentz-invariant metric-only massless pole shift}:\ 0.
}
\]

---

## 1. Start from the already-proved six-dimensional space

For a generic directed spatial momentum and parity-even tetrahedral symmetry, the physical transverse-traceless quotient has

\[
\dim\mathcal W^{(4)}_{TT,S_4}=6.
\]

Write the order-four correction as a real symmetric `2x2` operator on the two physical TT polarizations,

\[
\delta K_{TT}^{(4)}(\mathbf k)
=a_*^2 k^4\,Q(\hat n),
\qquad \hat n=\mathbf k/|\mathbf k|.
\]

The six Wilson coefficients parameterize the most general allowed `Q(n)` in the frozen `S4` class.

---

## 2. Continuous spatial isotropy collapses six coefficients to one

Assume the physical vacuum/background restores `SO(3)` spatial rotations.

For fixed `n`, the little group rotating the two TT polarization axes about `n` acts continuously on the real `(+,x)` polarization plane.  A parity-even real symmetric `2x2` kernel that commutes with all these little-group rotations must be proportional to the identity on TT space.

Homogeneity of degree four then leaves only

\[
\boxed{
\delta K_{TT,SO(3)}^{(4)}
=\eta_s\,a_*^2 |\mathbf k|^4 I_{TT}.
}
\]

Thus

\[
\boxed{\dim\mathcal W^{(4)}_{TT,SO(3)}=1.}
\]

Every tetrahedral anisotropy coefficient and every polarization-splitting coefficient must flow to zero if the physical vacuum is rotationally invariant.

This immediately gives a stronger interpretation of the finite `8.43%` `E/T2` split: it is a UV tetrahedral precursor whose survival is an empirical/RG question, not a required physical observable.

---

## 3. Local Lorentz invariance removes even the one isotropic massless-pole shift

Now impose the stronger assumptions:

1. the infrared vacuum is locally Lorentz invariant;
2. the only gapless spin-2 field in this sector is the metric graviton;
3. the quadratic effective action is expanded locally/analytically in derivatives around flat spacetime;
4. gauge reduction has isolated the two physical TT helicities.

Lorentz invariance permits the TT inverse kernel to depend on four-momentum through

\[
s=-\omega^2+c^2|\mathbf k|^2
\]

(up to the overall unit convention).

A local four-derivative correction therefore has the form

\[
\boxed{
K_{TT}(s)
=I_{TT}\left[Z_T s+\alpha a_*^2 s^2+O(a_*^4s^3)\right].
}
\]

Factorizing,

\[
K_{TT}(s)
=s\,I_{TT}\left[Z_T+\alpha a_*^2s+\cdots\right].
\]

Hence the massless Einstein branch remains

\[
\boxed{s=0}
\]

exactly at this derivative order.

The higher-derivative factor may encode an additional heavy pole if treated beyond EFT order, and curvature-squared terms can modify off-shell Green functions, but they do not generate a perturbative dispersion law

\[
\omega^2=c^2k^2+\text{const}\times a_*^2k^4
\]

for the original massless branch under the assumptions above.

Therefore

\[
\boxed{
(c_1,\ldots,c_6)_{\rm physical\ massless\ pole}=0
}
\]

at order `k^4` if full spatial isotropy **and** local Lorentz invariance are restored with no additional order-parameter field.

---

## 4. Why this is consistent with curvature-squared gravity

A generally covariant local metric action may contain

\[
R^2,\qquad R_{\mu\nu}R^{\mu\nu},\qquad R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}.
\]

Around flat spacetime, their quadratic TT contribution carries additional powers of the Lorentz scalar `s`.  Perturbatively they are equation-of-motion/off-shell corrections to the Einstein massless branch; in four dimensions combinations are also related by the Gauss-Bonnet identity and local field redefinitions.

This is compatible with the repository's earlier on-shell field-redefinition result: terms proportional to the leading TT equation of motion vanish on the leading massless pole.

The important distinction is

```text
higher-derivative effective action != shifted massless light cone.
```

---

## 5. What a nonzero six-vector would physically mean

A nonzero order-`k^4` massless-pole vector is not impossible.  It would, however, require additional physical structure beyond an isotropic Lorentz-invariant metric vacuum.

There are three nested outcomes.

### Outcome A — full GR/Lorentz universality

\[
\boxed{c_1=\cdots=c_6=0.}
\]

The microscopic tetrahedral split is a regulator/UV-state effect that flows away.  Quantum-gravity signatures must then be sought in interactions, nonlocal correlations, extra poles, matter sectors, or higher observables rather than a shifted vacuum GW light cone.

### Outcome B — rotationally invariant preferred foliation

All anisotropic/polarization-splitting combinations vanish, but

\[
\eta_s\ne0.
\]

Then the physical vacuum contains a preferred timelike/foliation structure that distinguishes `omega` from spatial `k` while preserving spatial `SO(3)`.

The theory must derive that structure; it cannot be imported by choosing a lattice time direction.

### Outcome C — surviving tetrahedral order

Generic

\[
(c_1,\ldots,c_6)\ne0.
\]

Then a physical spatial tensor/order parameter survives coarse graining.  The microscopic tetrahedral frame has become observable and the theory predicts anisotropy and possibly birefringence.

Again, the order parameter and its transformation law must be derived.  A regulator orientation alone is not sufficient.

---

## 6. Consequence for HDA tests

The existing HDA result establishes the leading GR hypersurface-deformation structure in its declared limit.  To decide among A/B/C, the next algebraic target is stronger:

\[
\boxed{
[H,H]_{\rm eff}\quad\text{through the same four-derivative order used for the pole extraction}.
}
\]

If the undeformed HDA and isotropic semiclassical vacuum persist through `O(a_*^2)`, Outcome A is the natural metric-only result.

If an order-`a_*^2` deformation remains, its tensors must match the same preferred structures that appear in the TT pole.  This gives an internal consistency test between

```text
constraint algebra deformation
<-> preferred tensor / foliation
<-> six-Wilson pole deformation.
```

A nonzero pole deformation with no corresponding derived structure in the constraint/history sector is a failure, not a prediction.

---

## 7. Revised blind hierarchy

The correct preregistered analysis is therefore

```text
microscopic history / reduced TT kernel
 -> extract full six-vector without symmetry fitting
 -> test C: generic S4 vector?
 -> test B: does it collapse to one SO3 scalar?
 -> test A: does even that scalar vanish on the Lorentz massless pole?
```

No coefficient is tuned to force any level.

This turns `zero` into a genuine candidate prediction rather than treating the existence of Planck-suppressed dispersion as an assumption.
