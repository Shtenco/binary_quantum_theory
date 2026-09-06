# Physical TT 1PI kernel at leading IR order — derived from the existing BQG structure

Status: **derivation / consolidation, not a new axiom, gate, microscopic sector or history postulate.**

This note answers one narrow question:

\[
\boxed{\text{what part of }\Gamma^{(2)}_{TT}(\omega,\mathbf k)\text{ is already fixed by the existing BQG?}}
\]

The answer is: the complete **leading two-derivative TT kernel** is already fixed, up to the ordinary overall Newton normalization. The full interacting higher-derivative kernel is not fixed by this argument.

No constraint spectral parameter is renamed as a physical frequency, and no reduced lattice transfer coefficient is promoted to a physical Wilson coefficient.

---

## 1. Inputs already present in the repository

The existing ADM/HDA selection result uses

\[
H[N]=\int d^3x\,N\left[
A\frac{\pi_{ab}\pi^{ab}-c\pi^2}{\sqrt q}
-B\sqrt q(R-2\Lambda)
\right]
\]

and proves, inside the declared local two-derivative ADM family,

\[
\boxed{c=\frac12,\qquad AB=1.}
\]

The remaining classical normalization freedom may be written

\[
A=16\pi G,\qquad B=(16\pi G)^{-1}.
\]

The existing BQG TT sector has two physical tensor polarizations. We denote orthonormal TT amplitudes by

\[
h_A,\qquad A=1,2.
\]

Nothing new is introduced here.

---

## 2. TT Hamiltonian

Expanding the selected two-derivative ADM Hamiltonian about the homogeneous flat/locally inertial background and restricting to the physical TT quotient gives the already registered form

\[
\boxed{
H^{(2)}_{TT}
=\sum_{A=1}^{2}\int d^3x\left[
A\,\pi_A^2+\frac B4(\partial_i h_A)(\partial_i h_A)
\right].
}
\]

The Hamilton equation is

\[
\dot h_A=\frac{\delta H}{\delta\pi_A}=2A\pi_A,
\]

hence

\[
\boxed{\pi_A=\frac{\dot h_A}{2A}.}
\]

---

## 3. Exact Legendre transform at quadratic order

For each TT polarization,

\[
\mathcal L_A
=\pi_A\dot h_A-\mathcal H_A.
\]

Substituting \(\pi_A=\dot h_A/(2A)\),

\[
\mathcal L_A
=\frac{\dot h_A^2}{2A}
-\frac{\dot h_A^2}{4A}
-\frac B4(\nabla h_A)^2,
\]

so

\[
\boxed{
S^{(2)}_{TT}
=\frac1{4A}\sum_{A=1}^{2}\int d^4x\left[
\dot h_A^2-AB(\nabla h_A)^2
\right].
}
\]

The HDA result \(AB=1\) therefore gives

\[
\boxed{
S^{(2)}_{TT}
=\frac1{4A}\sum_{A=1}^{2}\int d^4x\left[
\dot h_A^2-(\nabla h_A)^2
\right].
}
\]

Thus the leading light cone is not a fitted transfer parameter:

\[
\boxed{c_T^2=AB=1.}
\]

---

## 4. Euclidean physical 1PI Hessian

The sign convention is unambiguous after Wick rotation. Write the quadratic Euclidean action as

\[
S^{(2)}_{E,TT}
=\frac12\int\frac{d\omega_E\,d^3k}{(2\pi)^4}
\,h_A(-p)\,\Gamma^{(2)}_{E,AB}(p)\,h_B(p).
\]

Then

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

Using the ordinary GR normalization \(A=16\pi G\),

\[
\boxed{Z_T=\frac1{32\pi G}}
\]

for the orthonormal polarization convention used above.

The corresponding leading Euclidean connected two-point function is

\[
\boxed{
G^{TT}_{E}(\omega_E,\mathbf k)
=\frac{1}{Z_T}\frac{I_2}{\omega_E^2+\mathbf k^2}
+O(\partial^0/\Lambda_{UV}^2).
}
\]

---

## 5. Lorentzian kernel

Using the Lorentzian sign convention already employed by `C6_PHYSICAL_KERNEL_CLOSURE.md`, analytic continuation gives

\[
\boxed{
\Gamma^{(2)}_{TT}(\omega,\mathbf k)
=Z_T\left[-(\omega+i0)^2+\mathbf k^2\right]I_2
+O(\partial^4).
}
\]

An opposite overall Hessian-sign convention changes the displayed overall sign but not the pole, relative kinetic/gradient sign or residue criterion.

The physical statements are convention independent:

\[
\boxed{m_{TT}^2=0,}
\]

\[
\boxed{\omega^2=\mathbf k^2+O(k^4/\Lambda_{UV}^2),}
\]

\[
\boxed{N_{TT}=2,}
\]

and for \(G>0\),

\[
\boxed{Z_T>0.}
\]

So the leading infrared physical graviton is massless, has two polarizations and a common relativistic light cone.

---

## 6. Relation to the existing six-Wilson TT shell

The existing physical C6 analysis proves that the leading parity-even **spatial quartic** TT correction has six independent tetrahedral/S4 structures. Therefore the existing notation may be attached directly to the derived leading kernel:

\[
\Gamma^{(2)}_{TT}
=Z_T[-\omega^2+k^2]I_2
+Z_Ta_*^2\sum_{r=1}^{6}c_r^{IR}W_r(\mathbf k)
+\text{other allowed }O(\partial^4)\text{ frequency terms}
+O(\partial^6).
\]

The first term is fixed by the existing HDA/ADM structure.

The vector

\[
(c_1,\ldots,c_6)^{IR}
\]

is **not** fixed by the present derivation. Neither are possible independent \(\omega^4\) or \(\omega^2k^2\) coefficients before the full physical history/quantum effective action is computed.

This distinction prevents the reduced transfer kernel or a constraint resolvent from being silently promoted to the interacting physical 1PI kernel.

---

## 7. What the physical-history calculation is still needed for

The existing theory-specific physical-history frontier is now narrower than the phrase “derive the TT kernel” suggests.

It is still needed to determine, from the actual BQG rather than by fitting:

1. the microscopic value / scale matching of the overall residue \(Z_T\) or equivalently \(G\);
2. the complete connected interblock quantum covariance beyond the universal two-derivative limit;
3. the six spatial quartic coefficients \((c_1,\ldots,c_6)^{IR}\);
4. any independent quartic frequency structures and their unitarity/causality constraints;
5. loop/non-Gaussian corrections and the full interacting vacuum;
6. the controlled regulator/refinement limit of those quantities.

It is **not** needed to re-derive the leading facts

\[
m_{TT}=0,\qquad c_T=1,\qquad N_{TT}=2
\]

once the already-declared BQG ADM/HDA premises hold.

---

## 8. Relation to the reduced TT lattice propagator

`TT_VACUUM_TWO_POINT_RESULT.md` contains the exact reduced Gaussian lattice kernel

\[
K_E^{red}=4\sin^2(\omega/2)+r^2\sum_i4\sin^2(k_i/2),
\qquad r=1/\sqrt3.
\]

That object remains a reduced positive control. Its specific finite-lattice coefficient \(r\) is **not** used in the derivation above.

At small momentum the physical leading kernel is instead fixed by HDA normalization to the common relativistic form after physical time/space units are chosen consistently:

\[
\Gamma^{(2)}_{E,TT}=Z_T(\omega_E^2+k^2)I_2+O(\partial^4).
\]

Thus no constraint spectral coordinate, reduced clock-control frequency or finite transfer velocity has been renamed as a physical frequency/velocity.

---

## 9. Exact scientific status

This derivation closes one narrower statement:

> **Given the already registered BQG local two-derivative ADM/HDA sector, the leading physical TT 1PI kernel is fixed up to the ordinary Newton normalization.**

It does **not** claim that the full source-derived interacting BQG history functional has been constructed. Therefore the repository-level flag `physical_TT_kernel_frozen=false` should remain false if that flag means the complete interacting kernel including microscopic higher-derivative coefficients and scale matching.

The useful corrected decomposition is

```text
leading physical TT kernel shape at O(partial^2): DERIVED
absolute Newton/residue scale from microscopic matching: OPEN
full physical connected history: OPEN
quartic TT Wilson vector: OPEN
full interacting Gamma_TT^(2)(omega,k): OPEN
```

No new microscopic entity is required for the first line.
