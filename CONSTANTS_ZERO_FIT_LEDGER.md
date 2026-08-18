# Zero-fit constants ledger

Status: **parameter-counting and comparison ledger; no claim that the listed experimental targets have already been derived**.

The purpose is to prevent a common failure mode of candidate fundamental theories: fitting familiar numbers after the fact and calling the fit a prediction.

## 1. Which constants are legitimate microscopic numerical targets?

A useful split is

```text
dimensionful / unit-setting:
    c, hbar, G, Lambda in a chosen unit convention, absolute masses

dimensionless / zero-fit:
    alpha, mass ratios, mixing angles, coupling ratios,
    eta2_IR, zeta4_IR, optical E/T2 ratios, critical exponents
```

Dimensionful quantities can become predictions only after the theory fixes an absolute physical ruler/clock/action scale. A dimensionless quantity can be compared without that freedom.

## 2. Speed of light

The modern SI fixes

```text
c = 299792458 m/s
```

exactly. Reproducing this decimal number is therefore not a meaningful fundamental-theory test.

The physical dimensionless statement is instead the universality of the limiting cone. In the present gravity+Maxwell closure this becomes

\[
\boxed{\lim_{k\to0}c_T/c_\gamma=1.}
\]

A leading nonzero E/T2 anisotropy in the k^2 kernel would violate this Lorentz/rotation-restoration requirement.

## 3. hbar

`hbar` converts action to quantum phase. In the current composition analysis the overall phase/action slope remains one normalization direction. Therefore the decimal SI value of `hbar` is not an independent zero-fit target of the present dimensionless microscopic theory.

## 4. Newton constant

HDA fixes the DeWitt trace coefficient and the relative kinetic/curvature structure, not the overall gravitational action normalization. The remaining scale can be parameterized by `G` or by

\[
\lambda_R^{eff}=\frac{a_*^2}{8\pi\ell_P^2}.
\]

One physical length/action calibration is therefore still required.

## 5. Cosmological constant

The cosmological term cancels out of the HDA bracket. It remains a separate relevant infrared coupling in the present construction. Its observed small value is not currently derived.

## 6. Fine-structure constant: one-scalar gate

The q=2 Hopf/Pancharatnam bridge fixes the compact U(1) topology and minimal integer charge convention. Write the infrared gauge action in that convention as

\[
-\frac{Z_A}{4}F^2,
\qquad
D_\mu=\partial_\mu+iA_\mu.
\]

After canonical normalization, the physical minimal charge is

\[
e=Z_A^{-1/2}
\]

and

\[
\boxed{\alpha=\frac1{4\pi Z_A}.}
\]

The current 2022 CODATA recommended value is

\[
\alpha^{-1}=137.035999177(21),
\]

which corresponds to the comparison target

\[
\boxed{
Z_A^{obs}=\frac{\alpha^{-1}}{4\pi}
=10.9049783252782\pm1.67\times10^{-9}.
}
\]

This number is **not an input allowed in the microscopic calculation**. The future calculation must freeze the q=2 phase dynamics, regulator, blocking and normalization first, compute `Z_A`, and only then perform this comparison.

Gauge invariance and the Chern number do not select `Z_A`; they select the form of the connection and quantization convention. A new dynamical phase stiffness is therefore genuinely necessary.

## 7. Particle masses

Absolute masses require the physical scale. Mass ratios do not, and are consequently stronger fundamental tests.

The present gravitational/Peter-Weyl higher-shell eigenvalues must not be assigned to electron, muon or tau masses. Their direct spectral dynamic range is far too small for the charged-lepton hierarchy, and no Standard-Model representation/Yukawa map has been derived.

The correct zero-fit sequence is

```text
compact gauge dynamics
 -> realistic gauge group and chiral representations
 -> anomaly cancellation
 -> generation structure
 -> Higgs/Yukawa operator
 -> dimensionless Yukawa eigenvalue ratios
 -> compare to particle mass ratios.
```

## 8. Current strongest parameter-free gravitational targets

The present project already has quantities that do not require `G`:

```text
d_H ~ 3
z ~ 1
Fierz-Pauli/DeWitt tensor structure
TT residue continuum ratio / shape
massless leading TT pole
E/T2 rotational-restoration condition
eta2_IR and zeta4_IR once the recursive kernel is completed
R_gamma(omega) optical channel ratio
```

The strongest prospective prediction is not a decimal SI constant. It is a dimensionless coefficient or function frozen from the microscopic RG and then tested without retuning.

## 9. Anti-numerology rule

A number counts as a prediction only if all of the following are true before comparison:

1. its microscopic observable is defined;
2. the operator ordering and regulator are frozen;
3. all allowed calibration parameters are declared;
4. the target number was not used to select among microscopic routes;
5. uncertainty from finite cutoff/RG extrapolation is supplied;
6. failure is permitted.

By this rule `alpha`, particle mass ratios and the future `eta2_IR,zeta4_IR` can become meaningful tests. Coincidences between unrelated higher-shell eigenvalues and known constants cannot.
