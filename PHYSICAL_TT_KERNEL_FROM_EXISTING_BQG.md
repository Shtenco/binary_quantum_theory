# Physical TT 1PI kernel from existing BQG

Status: **leading two-derivative TT kernel derived from the already registered BQG ADM/HDA sector; higher-derivative coefficients remain microscopic outputs.**

## 1. No new microscopic input

This derivation introduces no new clock, history operator, transfer coefficient or microscopic degree of freedom. It uses only the already registered local ADM family

\[
H[N]=\int d^3x\,N\left[
A\frac{\pi_{ab}\pi^{ab}-c\pi^2}{\sqrt q}
-B\sqrt q(R-2\Lambda)
\right]+O(\partial^4/\Lambda_{UV}^2)
\]

and the existing HDA implication

\[
\boxed{c=\frac12,\qquad AB=1.}
\]

The TT reduction therefore belongs to the same physical low-energy sector already selected by BQG's HDA analysis.

## 2. TT Hamiltonian

On a flat/nondegenerate background, choose two orthonormal physical TT polarizations `h_A`, `A=1,2`, with conjugate momenta `pi_A`. The registered ADM normalization gives

\[
\boxed{
H_{TT}^{(2)}
=\sum_{A=1}^2\int d^3x\left[
A\pi_A^2+\frac B4(\partial_i h_A)(\partial_i h_A)
\right]
+O(\partial^4).
}
\]

The canonical equation is

\[
\dot h_A=\frac{\delta H}{\delta\pi_A}=2A\pi_A,
\]

so

\[
\boxed{\pi_A=\frac{\dot h_A}{2A}.}
\]

No constraint-resolvent spectral parameter is identified with physical frequency in this step.

## 3. Quadratic physical action

The ordinary Legendre transform gives

\[
\begin{aligned}
\mathcal L_{TT}^{(2)}
&=\sum_A\left(\pi_A\dot h_A
-A\pi_A^2
-\frac B4(\nabla h_A)^2\right)\\
&=\frac1{4A}\sum_A\left[
\dot h_A^2-AB(\nabla h_A)^2
\right].
\end{aligned}
\]

Since the existing HDA result fixes `AB=1`,

\[
\boxed{
S_{TT}^{(2)}
=\frac1{4A}\sum_{A=1}^2\int d^4x
\left[
\dot h_A^2-(\nabla h_A)^2
\right]
+O(\partial^4).
}
\]

Thus the leading TT light cone is not an additional fit:

\[
\boxed{c_T^2=1.}
\]

## 4. Euclidean 1PI Hessian

For a quadratic Euclidean action written as

\[
S_E^{(2)}=\frac12\int\frac{d\omega_Ed^3k}{(2\pi)^4}\,
h_A(-p)\,\Gamma^{(2)}_{E,AB}(p)\,h_B(p),
\]

the result is

\[
\boxed{
\Gamma^{(2)}_{E,TT}(\omega_E,\mathbf k)
=Z_T(\omega_E^2+\mathbf k^2)I_2
+O(\partial^4),
}
\]

with

\[
\boxed{Z_T=\frac1{2A}.}
\]

Under the standard ADM parametrization already used in the repository,

\[
A=16\pi G,\qquad B=(16\pi G)^{-1},
\]

so in the stated orthonormal polarization convention

\[
\boxed{Z_T=\frac1{32\pi G}.}
\]

The corresponding Gaussian Euclidean connected propagator is

\[
\boxed{
G^{TT}_E(\omega_E,\mathbf k)
=32\pi G\,\frac{I_2}{\omega_E^2+\mathbf k^2}
+O(\Lambda_{UV}^{-2}).
}
\]

## 5. Lorentzian causal kernel

Using the repository's Lorentzian convention and the usual causal continuation,

\[
\boxed{
\Gamma^{(2)}_{TT}(\omega,\mathbf k)
=Z_T\left[-(\omega+i0)^2+\mathbf k^2\right]I_2
+O(\partial^4).
}
\]

An overall sign can move with a different global Lorentzian Hessian convention, but the physical content is invariant:

\[
\boxed{
\omega^2=\mathbf k^2+O(k^4/\Lambda_{UV}^2),
\qquad m_g^2=0,
\qquad N_{pol}=2,
\qquad c_T=1.
}
\]

For `G>0`, the Gaussian TT residue in this convention is positive.

## 6. Why this does not silently identify a constraint resolvent with a propagator

The forbidden shortcut remains forbidden:

\[
z_{constraint}\ne\omega_{physical}
\]

unless a separate physical construction establishes such an equality.

The result above follows instead from the already physical canonical ADM/HDA infrared sector and its Legendre transform after TT reduction. Therefore it does not use a Lanczos eigenvalue, master-constraint gap, C8 character or other internal spectral coordinate as physical frequency.

The full interacting physical history is still required for genuinely microscopic nonlocal/frequency-dependent corrections beyond the leading local ADM sector.

## 7. Relation to the reduced lattice TT propagator

The repository also contains a reduced Gaussian lattice control with a discrete kernel such as

\[
4\sin^2(\omega/2)+\Omega_{\mathbf k}^2.
\]

That object remains a finite reduced/control propagator. Its bare finite-lattice velocity or quartic Taylor coefficients are **not** imported into the physical BQG kernel derived here.

Only its long-wavelength massless-Gaussian structure can be used as a consistency control after conventions are aligned.

## 8. The true remaining spin-2 frontier

The leading two-derivative shape is therefore fixed:

\[
\boxed{
\Gamma^{(2)}_{TT}
=Z_T[-\omega^2+k^2]I_2
+\Gamma^{(4)}_{TT}
+O(\partial^6).
}
\]

At generic nonzero vector momentum the repository has already proved that the complete parity-even tetrahedral TT spatial quartic sector is six-dimensional. Hence

\[
\boxed{
\Gamma^{(4)}_{TT,spatial}
=Z_Ta_*^2\sum_{r=1}^6c_r^{IR}W_r(\mathbf k).
}
\]

The six numbers

\[
\boxed{\mathbf c^{IR}=(c_1,c_2,c_3,c_4,c_5,c_6)}
\]

must be produced by the actual interblock/multi-block BQG dynamics. They may not be replaced by:

- the local first-refinement `E/T2` splitting;
- the reduced bare lattice `eta2/zeta4` values;
- a constraint spectral parameter;
- an externally fitted dispersion coefficient.

Independent quartic structures involving physical frequency, such as `omega^4` or `omega^2 k^2` when allowed by the final effective action, also remain outputs of the full physical/microscopic calculation and are not determined by the spatial six-vector alone.

## 9. Absolute normalization versus shape

The derivation fixes the leading kernel in terms of the remaining ADM normalization `A`, equivalently `G`.

Therefore two statements must be kept separate:

1. **shape already derived:** massless two-polarization relativistic TT pole at two-derivative order;
2. **absolute microscopic scale still open:** deriving/matching the physical value of `G` from the microscopic BQG scale rather than supplying it externally.

The latter is still part of BQG physicalization and is not solved by the HDA identity `AB=1` alone.

## 10. Current status

The old statement “the physical TT kernel is entirely open until a full history is built” is too broad.

The correct frontier is now

```text
existing BQG ADM/HDA
    -> leading physical Gamma_TT^(2): CLOSED CONDITIONALLY ON THE REGISTERED IR HYPOTHESES
    -> absolute microscopic G: OPEN
    -> actual interblock six spatial quartic Wilson coefficients: OPEN
    -> independent quartic frequency structures: OPEN
    -> full interacting physical history / nonlocal self-energy: OPEN
```

No experimental confirmation is claimed by this derivation.
