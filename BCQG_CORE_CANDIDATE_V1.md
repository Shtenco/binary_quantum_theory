# BCQG Core Candidate v1

**Status:** computable candidate quantum-gravity architecture; not an experimentally established theory of nature.

**Frozen working version:** 2026-08-15.

This document defines the gravity core. Mirror force, `infoton`, foam-spectrum and GW-resonance branches are separate extensions.

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

The local route shell is

\[
\Sigma Q_2\cong S^2.
\]

BCQG v1 promotes the minimal 8-vertex flag completion to the model definition. It is the 16-cell boundary,

\[
(V,E,F,T)=(8,24,32,16),
\qquad
\beta=(1,0,0,1),
\]

a closed orientable PL `S^3`, with checked recursive PL refinements.

The stronger claim that the bare causal graph uniquely forces every possible nonflag globalization is not assumed.

---

## 2. Continuum scaling sector

Frozen anchors are

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

A continuum state must exhibit the same scaling window for

\[
D_{link}\to3,
\quad d_s^{slice}\to3,
\quad z\to1,
\quad d_s^{history}\to4,
\]

while local-manifold, anisotropy and regulator defects vanish.

---

## 3. Physical Euclidean quantum geometry

The production Euclidean ordering is

\[
\boxed{H_E^{sine}=(T-T^\dagger)/(2i)},
\qquad
\boxed{K=[V,H_E^{sine}]}.
\]

The historical `H_plus=(T+T^dagger)/2` branch remains a structural control only.

A physical-sine two-node Euclidean × route test was preregistered before execution. It passed all frozen criteria:

```text
||H0||=||H1||=2.171258176327055
||[H0,H1]||=2.8794538147049544
p_cross=1.0056948923496356
p_GG=2.007490390559045
p_joint=1.0076444430189475
Delta_joint(1/64)=0.020030338775070305.
```

Thus the physical ordering preserves

\[
C_{cross}/D=O(\epsilon),
\qquad
C_{GG}/D=O(\epsilon^2),
\qquad
\Delta_{joint}=O(\epsilon).
\]

This removes the previous `H_plus`/`H_sine` ordering mismatch.

---

## 4. Quantum route-normal operator

The final quantum route operator cannot be expectation-first because a map

\[
\psi\mapsto\sqrt{\langle\psi|Q|\psi\rangle}\psi
\]

is nonlinear on superpositions.

Define on geometry × route Hilbert space

\[
B_i=\sum_aJ_a^i\otimes P_a,
\qquad
A=Q^{ab}\otimes P_aP_b=\sum_iB_i^\dagger B_i\ge0.
\]

Therefore the positive spectral square root exists and the production candidate is

\[
\boxed{
R_{op}[N]
=\frac12\left\{N,
\sqrt{\hat Q^{ab}\hat P_a\hat P_b}
\right\}.
}
\]

For `Omega(p)^2=Q^{ab}p_ap_b`,

\[
\Omega\partial_{p_c}\Omega+(\partial_{p_c}\Omega)\Omega
=2Q^{cb}p_b,
\]

so the operator-valued principal HDA structure function is preserved.

The finite logical matrix gate gives

```text
route defect(epsilon=1/64, carrier=8)=3.837772425e-7
p=0.999960897
```

and is robust across five logical spinors and carriers `2,4,8,16`.

Expectation-first route calculations remain semiclassical regression controls only.

---

## 5. Core Hamiltonian and HDA target

The pure-gravity candidate is

\[
\boxed{
H_{full}[N]
=H_E^{sine}[N]
+(1+\beta^2)H_L[N]
+R_{op}[N].
}
\]

The frozen target is

\[
\boxed{
[H_{full}[N],H_{full}[M]]
\longrightarrow
i\hbar D[\sharp_Q(NdM-MdN)]
}
\]

with the corresponding diffeomorphism and Gauss relations.

At fixed regulator-safe cutoff, the composition theorem gives

\[
C_{cross}/D=O(\epsilon),
\qquad
C_{GG}/D=O(\epsilon^2).
\]

For the declared polynomial cutoff envelope, any

\[
J_{max}\sim\epsilon^{-\alpha},
\qquad 0<\alpha<2/13
\]

suppresses both contaminants. BCQG v1 freezes the explicit interior path

\[
\boxed{J_{max}\sim\epsilon^{-1/8}},
\]

for which

\[
C_{cross}/D=O(\epsilon^{3/16}),
\qquad
C_{GG}/D=O(\epsilon^{3/8}).
\]

This remains a conditional diagonal certificate, not a uniform arbitrary-path theorem.

---

## 6. Lorentzian amplitude, phase and relative normalization

The exact environment-unbiased Peter-Weyl calculation at `Jmax=7/2`, with all 16 logical environments and the complete 24-term S4 orbit, gives

\[
\boxed{L_{raw,1body}=i\,1.3389293521464034\,Y+O(10^{-16})}.
\]

The declared nested Thiemann structure contains five Poisson brackets, hence

\[
\boxed{(1/i)^5=-i}.
\]

Therefore the phase-completed block is Hermitian:

\[
-iL_{raw,1body}=1.3389293521464034Y+O(10^{-16}).
\]

The code-bound tetrahedral normalization audit matches the production oriented specs and forward-minus-reverse loops to the canonical epsilon sum. In the original fundamental-trace convention,

\[
\boxed{H_E^{phys}=-\frac{2}{3\hbar}H_E^{sine,raw}}.
\]

Consequently the Lorentzian magnitude is not an independent HDA knob. The full `beta=1` correction has

\[
\boxed{|g_{corr}|=\frac{32}{9\hbar^7}},
\]

while in the repository decomposition

\[
H_E+(1+\beta^2)H_L
\]

the bare `H_L` magnitude at `beta=1` is

\[
\boxed{|g_{H_L}|=\frac{16}{9\hbar^7}}.
\]

The remaining freedom is the consistent overall real sign and full symmetric factor-ordering of the noncommuting spin-changing operator, not an arbitrary Lorentzian fit coefficient.

---

## 7. Global orientation consequence

The exact 16-cell orientation sign is

\[
\eta_v=(-1)^{popcount(v)}.
\]

The sign-covariant Lorentzian one-body term therefore assembles as

\[
\boxed{H_{L,1body}=g_Rc_L\sum_v\eta_vY_v=16g_Rc_L\Sigma}.
\]

At fixed global orientation it is a longitudinal field conjugate to staggered orientation; it is not a mediator mass or force. Under simultaneous global-orientation reversal and `Y` reversal, `eta_vY_v` is invariant.

---

## 8. Corrected Euclidean logical return

The exact first-order rule remains

\[
P H_E P=0.
\]

The audited environment-unbiased Euclidean return kernel has

```text
A_rel=0.9644798301915488
J_shape=-0.5564630119591318
J_orient=+2.18199564892363
Delta_aniso,ret=2.738458660882762
648 states = 392 positive + 256 negative.
```

The older `Delta_aniso,ret=3.6832250321658044` is retired. The return kernel is a short-time/leakage object, not a static physical mass Hamiltonian.

---

## 9. Single immediate falsifier

The separate Euclidean and route-ordering problems have now collapsed into one next operator task:

\[
\boxed{
[H_E^{sine}+(1+\beta^2)H_L+R_{op},
 H_E^{sine}+(1+\beta^2)H_L+R_{op}]
}
\]

on the same two-node graph-changing Peter-Weyl habitat, using:

```text
full spin-changing H_L amplitudes;
canonical five-bracket phase;
upstream-fixed relative magnitude;
operator-first positive route square root;
nonconstant off-shell lapses;
no channel-dependent subtraction or refit.
```

A PASS would move the core frontier to independent habitats, collective-spin/refinement scaling and a stronger joint-cutoff theorem. A FAIL must be retained and would identify which full Lorentzian channel invalidates the candidate.

---

## 10. IR target and scope

Conditional on first-class continuum HDA and a nondegenerate `D=3` metric sector, the retained DeWitt/Dirac chain targets

\[
\boxed{
\text{one massless spin-2 tensor sector with two TT helicities}
}
\]

and no non-decoupling scalar ghost.

Mirror force, `infoton`, foam-spectrum and GW-resonance hypotheses remain separate extensions. They are not evidence for the gravity core.

---

## Compact definition

\[
\boxed{
q=2
\to S^2_{link}
\to PL\ S^3
\to d_{space}=3
\to z=1
\to 3+1D\ IR
\to H_E^{sine}
\to H_L
\to R_{op}
\to HDA
\to GR\ tensor\ IR.
}
\]

Canonical joint path:

\[
\boxed{\epsilon\to0,\qquad J_{max}\sim\epsilon^{-1/8}\to\infty.}
\]

That is the current scope of **BCQG Core Candidate v1**.
