# BCQG Core Candidate v1

**Status:** computable candidate quantum-gravity architecture; not an experimentally established theory of nature.

**Frozen working version:** 2026-08-15.

Mirror force, `infoton`, foam-spectrum and GW-resonance branches are separate extensions and are not used as evidence for the gravity core.

---

## 1. Microscopic spatial sector

Local route homogeneity requires

\[
q+2=2^q,
\]

whose unique integer solution for `q>=1` is

\[
\boxed{q=2}.
\]

The local route shell is `S^2`. BCQG v1 promotes the minimal 8-vertex flag completion to the model definition: the 16-cell boundary,

\[
(V,E,F,T)=(8,24,32,16),
\qquad
\beta=(1,0,0,1),
\]

a closed orientable PL `S^3`, with checked recursive refinements.

---

## 2. Continuum scaling sector

Frozen anchors:

\[
\boxed{d_H=2.999229782},
\qquad
\boxed{z=0.998281156},
\]

\[
\boxed{d_s^{slice}=3.004393867},
\qquad
\boxed{d_s^{history}\simeq4.004393867}.
\]

A continuum state must exhibit the same scaling window while manifold-link, anisotropy and regulator defects vanish.

---

## 3. Physical Euclidean quantum geometry

The production Euclidean ordering is

\[
\boxed{H_E^{sine}=(T-T^\dagger)/(2i)},
\qquad
\boxed{K=[V,H_E^{sine}]}.
\]

The preregistered physical two-node test passed:

```text
||H0||=||H1||=2.171258176327055
||[H0,H1]||=2.8794538147049544
p_cross=1.0056948923496356
p_GG=2.007490390559045
p_joint=1.0076444430189475
Delta_joint(1/64)=0.020030338775070305
```

so the physical ordering preserves

\[
C_{cross}/D=O(\epsilon),
\qquad
C_{GG}/D=O(\epsilon^2),
\qquad
\Delta_{joint}=O(\epsilon).
\]

---

## 4. Quantum route-normal operator

The final route operator is operator-first because expectation-first square-root maps are nonlinear on superpositions.

Define

\[
A=Q^{ab}\otimes P_aP_b=\sum_iB_i^\dagger B_i\ge0.
\]

Then

\[
\boxed{R_{op}[N]=\frac12\left\{N,\sqrt{\hat Q^{ab}\hat P_a\hat P_b}\right\}}.
\]

The exact matrix Sylvester identity preserves the HDA principal structure function. The canonical logical finite gate gives

```text
endpoint(1/64, carrier=8)=3.837772425e-7
p=0.999960897.
```

An independent two-node 4×4 reference gives `8.205159710207801e-7`, `p=0.9999594708960342`, and sparse-Fourier/48×48-FFT agreement at `5.74e-8` relative difference; it remains non-canonical pending its branch CI.

---

## 5. Core Hamiltonian and regulator target

The pure-gravity candidate is

\[
\boxed{H_{full}[N]=H_E^{sine}[N]+(1+\beta^2)H_L[N]+R_{op}[N]}.
\]

The target is

\[
\boxed{[H_{full}[N],H_{full}[M]]\longrightarrow i\hbar D[\sharp_Q(NdM-MdN)]}.
\]

At fixed cutoff,

\[
C_{cross}/D=O(\epsilon),
\qquad
C_{GG}/D=O(\epsilon^2).
\]

For the retained norm envelope, `Jmax~epsilon^-alpha` works for `0<alpha<2/13`. BCQG v1 freezes

\[
\boxed{J_{max}\sim\epsilon^{-1/8}},
\]

which yields `epsilon^(3/16)` and `epsilon^(3/8)` suppression of the declared contaminants.

---

## 6. Lorentzian amplitude and phase

The exact environment-unbiased Peter-Weyl calculation at `Jmax=7/2`, all 16 logical environments and the full 24-term S4 orbit gives

\[
\boxed{L_{raw,1body}=i\,1.3389293521464034Y+O(10^{-16})}.
\]

The nested Thiemann construction has five Poisson brackets after substituting both `K` factors, hence

\[
\boxed{(1/i)^5=-i},
\qquad
\boxed{H_{phase}=-iL_{raw}}.
\]

Therefore the frozen logical phase-completed block is Hermitian.

---

## 7. Signed relative Lorentzian normalization

The code-bound tetrahedral audit fixes

\[
\boxed{H_E^{phys}=-\frac{2}{3\hbar}H_E^{sine,raw}}.
\]

Keeping the declared Thiemann correction sign fixes

\[
\boxed{H_{corr}=-\frac{32}{9\hbar^7}H_{phase}}.
\]

In repository convention

\[
G=H_E+(1+\beta^2)H_L,
\]

so

\[
\boxed{H_L=-\frac{32}{9\hbar^7(1+\beta^2)}H_{phase}}.
\]

For `beta=hbar=1`:

\[
\boxed{G_v=-\frac23E_v+\frac{32i}{9}L_{raw,v}}.
\]

Independent CI verifies this signed relation (`lorentzian-repo-sign`, run `31857722477`, artifact digest `sha256:10f538abd68dc8945a46ec03410b5e4490a5d8e1fbbb05d56a10a56fd6220101`, `fitting_used=false`).

Thus **neither Lorentzian magnitude nor relative sign is an HDA tuning parameter**.

---

## 8. Signed logical Lorentzian-route regression

For the operator-first logical route average,

\[
-i[c_LY,\Omega_{op}]
=0.0536574847984X+0.0929374897107Z.
\]

With the full `beta=1` correction coefficient, the signed regression target is

\[
\boxed{-0.1907821681721X-0.3304444078603Z},
\]

shape norm `0.3815643358315`.

This is a subchannel regression for the future exact graph-changing cross, not a full HDA result.

---

## 9. Corrected Euclidean logical return

The exact first-order rule remains `P H_E P=0`. The audited return kernel has

```text
A_rel=0.9644798301915488
J_shape=-0.5564630119591318
J_orient=+2.18199564892363
Delta_aniso,ret=2.738458660882762
648 states = 392 positive + 256 negative.
```

The older `Delta_aniso,ret=3.6832250321658044` is retired.

---

## 10. Single immediate falsifier

The remaining principal operator task is the exact two-node graph-changing commutator

\[
\boxed{[H_E^{sine}+(1+\beta^2)H_L+R_{op},\ H_E^{sine}+(1+\beta^2)H_L+R_{op}]}.
\]

At `beta=hbar=1`, the raw-code geometry operator is frozen as

```text
G_v=(-2/3) E_v + (32 i/9) L_raw,v.
```

The geometry commutator is preregistered channel-by-channel:

```text
EE = E0E1-E1E0       wall 5/2
EL = E0L1-E1L0       wall 9/2
LE = L0E1-L1E0       wall 9/2
LL = L0L1-L1L0       wall 13/2
```

with no post-hoc sign flip, coefficient refit, channel subtraction or threshold retuning.

The branch now contains:

- a general covariant-to-Gauss full `L_raw` adapter;
- a 24-way exact full-state Lorentzian column pipeline;
- distributed `EE/EL/LE/LL` workers plus exact signed collector;
- exact sparse-Fourier operator-first route algebra;
- generic spin-changing `K0×K1` route blocks.

A PASS moves the frontier to independent habitats, collective-spin/refinement scaling and a stronger joint-cutoff theorem. A FAIL is retained and identifies the anomalous channel.

---

## 11. IR target and scope

Conditional on first-class continuum HDA and a nondegenerate `D=3` metric sector, the retained DeWitt/Dirac chain targets one massless spin-2 tensor sector with two TT helicities and no non-decoupling scalar ghost.

Mirror force, `infoton`, foam-spectrum and GW-resonance hypotheses remain separate extensions.

---

## Compact definition

\[
\boxed{q=2\to S^2_{link}\to PL\ S^3\to3+1D\ IR\to H_E^{sine}\to H_L\to R_{op}\to HDA\to GR\ tensor\ IR}
\]

with canonical joint path

\[
\boxed{\epsilon\to0,\qquad J_{max}\sim\epsilon^{-1/8}\to\infty}.
\]
