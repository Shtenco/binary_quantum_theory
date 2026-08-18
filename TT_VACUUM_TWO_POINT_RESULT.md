# Reduced TT vacuum two-point result: smoothing is not quantum foam

Status: **exact Gaussian result for the explicit reduced TT propagator; negative control on the old smoothing-to-foam identification**.

## 1. Starting point

The physicalization pass derived the exact free reduced TT kernel

\[
K_E(\omega,\mathbf k)
=4\sin^2\frac\omega2+\Omega_{\mathbf k}^2,
\]

with

\[
\Omega_{\mathbf k}^2
=r^2\sum_i4\sin^2\frac{k_i}{2},
\qquad r=1/\sqrt3.
\]

For Gaussian residue `Z_T`, the Euclidean propagator is

\[
G_E^{TT}(\omega,\mathbf k)
=\frac1{Z_T K_E(\omega,\mathbf k)}.
\]

## 2. Exact equal-time covariance

Integrating the lattice frequency over one Brillouin zone gives

\[
C(\mathbf k)
=\int_{-\pi}^{\pi}\frac{d\omega}{2\pi}
G_E^{TT}(\omega,\mathbf k).
\]

Using

\[
4\sin^2(\omega/2)=2-2\cos\omega,
\]

the integral is exact:

\[
\boxed{
C(\mathbf k)
=\frac1{Z_T\Omega_{\mathbf k}\sqrt{\Omega_{\mathbf k}^2+4}}.
}
\]

As `k -> 0`,

\[
\Omega_{\mathbf k}\sim r|\mathbf k|,
\]

so

\[
\boxed{
C(\mathbf k)
\sim\frac1{2Z_T r|\mathbf k|}.
}
\]

Therefore the equal-time infrared power spectrum is

\[
\boxed{P_{TT}(k)\propto k^{-1}}.
\]

The executable logarithmic fit gives

\[
\boxed{n_{TT}^{num}=-1.000000148}.
\]

Independent numerical frequency integration agrees with the exact closed form at relative error below

\[
\boxed{2.1\times10^{-16}}.
\]

Reproduction:

```bash
python scripts/tt_vacuum_two_point_gate.py
```

## 3. Coarse RMS law

For a stationary 3D equal-time field with

\[
P(k)\sim k^n,
\]

a smooth large-block average has

\[
\operatorname{Var}(h_R)\sim R^{-(3+n)},
\]

and therefore

\[
\operatorname{RMS}(h_R)\sim R^{-(3+n)/2}.
\]

For the actual reduced TT vacuum value `n=-1`,

\[
\boxed{
\operatorname{RMS}(h_R)\sim R^{-1}.
}
\]

## 4. Negative control on the old foam inference

The observer-smoothing calculation independently measured

\[
\delta g_{smooth}\sim b^{-2.001707}.
\]

If one *assumes* that this is itself the RMS of a stationary 3D quantum metric vacuum, the algebra gives

\[
n=2(2.001707)-3=1.003414.
\]

But the first explicit Gaussian TT vacuum derived from the actual reduced propagator instead gives

\[
\boxed{n=-1}.
\]

Therefore

\[
\boxed{
\delta g_{smooth}\sim b^{-2.001707}
\not\Rightarrow
P_{vac}(k)\sim k^{1.003414}
}
\]

for the explicit massless TT vacuum sector.

The old `k^1.003414` statement must remain a rejected/conditional reinterpretation of a smoothing defect, not a current quantum-vacuum prediction.

This is scientifically useful: the `b^-2` law continues to describe observer self-averaging/central-limit smoothing, while the quantum propagator supplies a logically separate correlator.

## 5. What could still change the vacuum exponent

The result is exact only for the reduced Gaussian TT kernel. A full interacting Peter--Weyl/history/RG vacuum could in principle generate a different infrared universality class.

If that occurs, the new exponent must be obtained directly from

\[
\langle0|h^{TT}(x)h^{TT}(y)|0\rangle
\]

of the full frozen theory. It may not be inferred from the observer smoothing exponent.

## New status

```text
observer smoothing exponent      p = 2.001707   retained
old foam spectral inference      n = +1.003414  rejected as TT Gaussian vacuum identification
explicit reduced TT vacuum       n = -1         exact for the reduced free kernel
full interacting history vacuum  open
```

This result strengthens the physicalization programme by separating a real quantum observable from a coarse-graining diagnostic.
