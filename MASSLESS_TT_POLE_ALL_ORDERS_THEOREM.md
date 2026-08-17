# Massless TT pole universality to all local derivative orders

Status: **conditional effective-theory theorem.**

Assumptions:

1. the physical vacuum is Poincare/Lorentz invariant;
2. diffeomorphism symmetry is unbroken in the physical metric sector;
3. the relevant gapless spin-2 excitation is the metric graviton;
4. the quadratic 1PI effective action admits a local analytic derivative expansion around flat spacetime;
5. no additional physical tensor/foliation order parameter is inserted.

Under these assumptions the original massless graviton light cone is not perturbatively shifted by any finite order of local higher-derivative metric operators.

---

## 1. Physical TT kernel

After gauge reduction, the two helicities form the physical TT sector.  Lorentz invariance permits the scalar momentum dependence to depend only on

\[
s=-\omega^2+c^2\mathbf k^2.
\]

Continuous rotations/little-group covariance make the parity-even quadratic kernel scalar on the two physical polarizations:

\[
K_{TT}^{ab}(s)=\delta^{ab}f(s).
\]

Unbroken massless diffeomorphism symmetry excludes a graviton mass term in the flat vacuum, so

\[
f(0)=0.
\]

For a local analytic derivative expansion,

\[
f(s)=Z_Ts+\alpha_2a_*^2s^2+\alpha_3a_*^4s^3+\cdots.
\]

Therefore

\[
\boxed{
K_{TT}(s)=s\,I_{TT}\,F(a_*^2s),
\qquad F(0)=Z_T>0.
}
\]

---

## 2. The original massless branch is exact in the derivative expansion

The pole equation is

\[
sF(a_*^2s)=0.
\]

One branch is always

\[
\boxed{s=0}
\]

and hence

\[
\boxed{\omega^2=c^2k^2.}
\]

No finite collection of local Lorentz-invariant higher-derivative metric terms can turn this branch into

\[
\omega^2=c^2k^2+\beta_4a_*^2k^4+\beta_6a_*^4k^6+\cdots.
\]

This is stronger than the quartic `6 -> 1 -> 0` result: the zero persists at every local analytic derivative order under the stated assumptions.

---

## 3. What higher derivatives can do

The form factor `F` is physical off shell and in interactions.  Its additional zeros can generate extra massive/complex poles if one extrapolates the higher-derivative action beyond its EFT domain.  Higher-curvature operators also change scattering amplitudes, nonlinear propagation on curved backgrounds and contact/interacting observables.

Thus

```text
no shifted vacuum massless light cone
```

does **not** mean

```text
no quantum-gravity effects.
```

It means vacuum dispersion of the original massless graviton is not forced by Lorentz-invariant metric EFT.

---

## 4. Ways to evade the theorem physically

A nonzero modified vacuum pole requires at least one assumption above to fail.  Examples include:

- a physical timelike vector/clock/foliation order parameter;
- a spatial tensor condensate such as the tetrahedral `T^(4)` order parameter;
- extra gapless fields that mix with the graviton;
- explicit/spontaneous Lorentz breaking;
- genuinely nonlocal structures whose pole equation is not an analytic function solely of the Lorentz scalar `s`;
- a background other than the Poincare-invariant vacuum.

Each evasion must be derived as physical structure.  A regulator orientation is not an evasion.

---

## 5. Consequence for this candidate theory

The microscopic tetrahedral geometry permits a six-dimensional quartic TT deformation space at finite regulator.  The physical continuum calculation must determine whether the microscopic tensor memory

```text
flows away completely -> Lorentz/metric universality;
leaves one SO3 scalar -> physical preferred foliation;
leaves generic six     -> physical spatial orientational order.
```

If the physical history/projector calculation restores the assumptions of this theorem, the blind prediction for vacuum massless GW dispersion is

\[
\boxed{c_1=\cdots=c_6=0}
\]

and, more generally, all local analytic vacuum-dispersion coefficients of the same massless branch vanish.

Quantum-gravity observables must then be sought in nonlocal correlations, interactions, extra poles/sectors, curved-background effects, matter couplings or other higher-point functions.

---

## 6. Relation to the project's older reduced TT lattice pole

The bare reduced lattice propagator contains direction-dependent `k^4` corrections because the finite regulator is not continuously Lorentz invariant.  That result is a valid regulator positive control.

The present theorem says that such bare coefficients are **not automatically infrared observables**.  If Lorentz symmetry emerges, they must renormalize away from the physical massless pole.

This makes the bare `eta2=-1/45`, `zeta4=-1/12` values useful as a UV lattice benchmark but not physical predictions.
