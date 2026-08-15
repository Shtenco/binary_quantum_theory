# Theory status — canonical ledger

**Frozen working frontier: 2026-08-15.**

The repository develops **BCQG Core Candidate v1**, a computable candidate quantum-gravity architecture. It is not an experimentally established theory of nature and does not by itself establish a mirror force, antigravity or a new particle.

Canonical entry points:

```text
START_HERE.md
BCQG_CORE_CANDIDATE_V1.md
THEORY_STATUS.md
theory_gates.json
```

---

## 1. Frozen kinematic / dimensional core

```text
binary routes
 -> q=2
 -> octahedral S2 local link
 -> minimal flag / recursive PL S3
 -> d_space~3
 -> z~1
 -> 4D-like history
 -> smooth IR candidate.
```

Frozen anchors:

```text
d_H          = 2.999229782
z            = 0.998281156
d_s(slice)   = 3.004393867
d_s(history) ~ 4.004393867
16-cell seed Betti=(1,0,0,1)
PL tetrahedra: 16 -> 384 -> 9216.
```

The minimal 8-vertex flag globalization is part of the candidate definition. The stronger statement that the bare causal graph uniquely fixes every possible nonflag global pairing is not asserted.

---

## 2. Physical Euclidean Peter-Weyl ordering is now calibrated

The physical Euclidean/Lorentzian stack uses

\[
\boxed{H_E^{sine}=(T-T^\dagger)/(2i)}
\]

and

\[
K_{sine}=[V,H_E^{sine}].
\]

The older

\[
H_+=(T+T^\dagger)/2
\]

two-node result remains only a historical structural control.

A dedicated physical-sine two-node Euclidean × route gate was preregistered **before execution**. GitHub Actions run `31855735615` completed successfully with artifact digest

```text
sha256:21e2da508fd583d9007a5bd400d074e8cee39990656e6c75e5968d2601323526.
```

Finite physical-sine anchors:

```text
support(H0)=support(H1)=37
||H0||=2.1712581763270546
||H1||=2.171258176327055
support([H0,H1])=514
||[H0,H1]||=2.8794538147049544
```

Frozen regulator fit:

```text
p_cross = 1.0056948923496356
p_GG    = 2.007490390559045
p_joint = 1.0076444430189475
```

and

```text
Delta_joint(1/64)=0.020030338775070305 < 0.05.
```

All preregistered conditions passed without channel-dependent normalization, subtraction or post-hoc threshold changes.

Therefore the physical sine ordering preserves

\[
\boxed{C_{cross}/D=O(\epsilon)},
\qquad
\boxed{C_{GG}/D=O(\epsilon^2)},
\qquad
\boxed{\Delta_{joint}=O(\epsilon)}.
\]

Canonical evidence:

```text
PETER_WEYL_TWO_NODE_SINE_HDA_PREREGISTRATION.md
PETER_WEYL_TWO_NODE_SINE_HDA_RESULT.md
verification_results/PETER_WEYL_TWO_NODE_SINE_HDA.json
scripts/peter_weyl_two_node_euclidean_sine_joint_gate.py
```

---

## 3. Quantum route normal: operator-first is the production candidate

Expectation-first maps such as

\[
\psi\mapsto\sqrt{\langle\psi|Q|\psi\rangle}\,\psi
\]

are nonlinear on superpositions and therefore cannot define the final quantum Hamiltonian constraint. They remain useful semiclassical surrogates.

On geometry × route Hilbert space define

\[
B_i=\sum_a J_a^i\otimes P_a,
\qquad
A=Q^{ab}\otimes P_aP_b=\sum_iB_i^\dagger B_i\ge0.
\]

Hence the unique positive spectral square root exists:

\[
\boxed{\Omega=A^{1/2}},
\qquad
\boxed{R_{op}[N]=\frac12\{N,\Omega\}}.
\]

For the matrix symbol `Omega(p)^2=Q^{ab}p_ap_b`, differentiation gives the exact Sylvester identity

\[
\boxed{\Omega\partial_{p_c}\Omega+(\partial_{p_c}\Omega)\Omega=2Q^{cb}p_b},
\]

which supplies the same operator-valued HDA principal structure function.

The exact logical 2×2 finite gate gives, for carrier 8 and `epsilon=1/64`,

```text
operator-first route defect = 3.837772425e-7
fitted epsilon exponent     = 0.999960897.
```

Five independent logical spinors give endpoint defects about `3.56e-7...3.84e-7`, all with exponent approximately one. Carrier checks `k=2,4,8,16` also retain exponent approximately one and improve with carrier.

Therefore the production quantum route sector is frozen as

\[
\boxed{
R_{op}[N]=\frac12\left\{N,\sqrt{\hat Q^{ab}\hat P_a\hat P_b}\right\}.
}
\]

Evidence:

```text
ROUTE_OPERATOR_FIRST_QUANTUM_SELECTION.md
scripts/operator_first_route_hda_gate.py
```

---

## 4. Fixed-cutoff and simultaneous-cutoff HDA structure

For the bounded local geometry sector at fixed regulator-safe cutoff,

```text
C_cross/D = O(epsilon)
C_GG/D    = O(epsilon^2).
```

This composition statement is independent of the historical plus versus physical sine finite calibration; the new sine gate now verifies the same hierarchy numerically for the physical Euclidean ordering.

The retained simultaneous-cutoff envelope is

```text
C_cross/D = O(epsilon Jmax^(13/2))
C_GG/D    = O(epsilon^2 Jmax^13).
```

For

```text
Jmax~epsilon^-alpha
```

both bounds decay for

```text
0 < alpha < 2/13.
```

BCQG v1 freezes the explicit interior path

```text
alpha=1/8
Jmax~epsilon^-1/8
```

with

```text
C_cross/D = O(epsilon^(3/16))
C_GG/D    = O(epsilon^(3/8)).
```

This is a conditional diagonal certificate, not a uniform arbitrary-path theorem.

---

## 5. Lorentzian raw amplitude is nonzero

For all-`j=1/2` input, full Lorentzian HH support is finite at the declared wall

```text
Jmax=13/2.
```

The exact environment-unbiased logical amplitude at `Jmax=7/2`, with all 16 logical environments and the full 24-term S4 orbit, is

\[
\boxed{L_{raw,1body}=i\,1.3389293521464034\,Y+O(10^{-16})}.
\]

Controls:

```text
S4 covariance defect = 1.3976239359266602e-15
physical basis/volume leakage = 6.532094795930893e-16
raw Frobenius norm = 1.8935320488648653.
```

Thus `P L_raw P != 0` is a tested amplitude result, not support counting.

---

## 6. Canonical phase and relative real normalization

The declared Lorentzian nested structure is

```text
{A,{V,H_E}} {A,{V,H_E}} {A,V},
```

so after substituting both `K~{V,H_E}` factors there are five Poisson brackets. Under

\[
\{\ ,\ \}\to\frac1{i\hbar}[\ ,\ ],
\]

the universal complex phase is

\[
\boxed{(1/i)^5=-i}.
\]

Therefore

\[
-iL_{raw,1body}
=1.3389293521464034Y+O(10^{-16})
\]

is Hermitian.

The Euclidean tetrahedral normalization audit matches the repository's production `4 face blocks × 3 cyclic specs` and the forward-minus-reverse `T_sequences` to the canonical six epsilon permutations. In the original fundamental-trace convention,

\[
\boxed{H_E^{phys}=n_EH_E^{sine,raw}},
\qquad
\boxed{n_E=-\frac{2}{3\hbar}}.
\]

Hence the Lorentzian K-K-V magnitude is not an independent HDA fit parameter. The full `beta=1` correction has

\[
\boxed{|g_{corr}|=\frac{32}{9\hbar^7}},
\]

while in the repository convention

\[
G=H_E+(1+\beta^2)H_L
\]

the **bare** `H_L` magnitude at `beta=1` is

\[
\boxed{|g_{H_L}|=\frac{16}{9\hbar^7}}.
\]

In structural `hbar=1` units this gives:

```text
bare H_L local |Y| coefficient = 2.3803188482602727
full beta=1 correction          = 4.760637696520545.
```

These are relative dimensionless operator coefficients, not eV/Joule predictions. The remaining real sign and full noncommuting factor-ordering convention must still be frozen consistently.

Evidence:

```text
EUCLIDEAN_SINE_NORMALIZATION_MATCH.md
LORENTZIAN_REAL_NORMALIZATION_LEDGER.md
LORENTZIAN_COMMUTATOR_PHASE_CERTIFICATE.md
scripts/euclidean_sine_normalization_match_gate.py
scripts/lorentzian_real_normalization_gate.py
```

---

## 7. Global 16-cell Lorentzian orientation field

Exact facet orientation is

\[
\eta_v=(-1)^{popcount(v)}.
\]

Together with Lorentzian S4 sign covariance, the phase-completed one-body term assembles as

\[
\boxed{H_{L,1body}=g_Rc_L\sum_v\eta_vY_v=16g_Rc_L\Sigma}.
\]

Raw fixed-orientation ideal mirror-pair splitting:

```text
42.84573926868491 * |g_R|.
```

With the conditional canonical `hbar=1` normalization:

```text
bare repository H_L pair split at beta=1 = 76.17020314432873
full beta=1 correction pair split         = 152.34040628865745.
```

This is a longitudinal field conjugate to staggered orientation, not a mediator mass or force. Under simultaneous global-orientation reversal and `Y` reversal, `eta_vY_v` is invariant.

---

## 8. Lorentzian × operator-first route cross is nonzero

The logical operator-first route average is approximately

\[
\Omega_{op}=0.8197716816I-0.0347058975X+0.0200374593Z.
\]

For the phase-completed raw Lorentzian `c_LY`,

\[
-i[c_LY,\Omega_{op}]
=0.0536574848X+0.0929374897Z
\]

per unit raw real normalization, with shape coefficient norm `0.10731496945`.

Expectation-first isotropic averaging would erase this cross, another reason it cannot be used as the final quantum operator. The operator-first route HDA PASS shows the nonzero cross is a legitimate finite candidate channel whose regulator scaling must be tested in the complete Hamiltonian.

---

## 9. Corrected Euclidean logical return

The exact first-order selection rule remains

```text
P H_E P=0.
```

The audited Euclidean return kernel has

```text
II       = 9.04524203998966
A_rel    = 0.9644798301915488
J_shape  = -0.5564630119591318
J_orient = +2.18199564892363
Delta_aniso,ret = 2.738458660882762
forbidden odd-Y norm = 2.7985693281119945e-33.
```

The 648-state decomposition has `392 positive / 256 negative` contributions and matrix reconstruction error `8.606528098114035e-15`.

The older `Delta_aniso,ret=3.6832250321658044` value is retired. The Euclidean return kernel is a short-time/leakage object, not a static physical mass Hamiltonian.

---

## 10. Current single gravity-operator frontier

The separate Euclidean-ordering and route-ordering bottlenecks are now closed enough to define one next operator unambiguously:

\[
\boxed{
H_{full}[N]
=
H_E^{sine}[N]
+(1+\beta^2)H_L[N]
+R_{op}[N].
}
\]

The **single immediate killer calculation** is

\[
\boxed{
[H_{full}[N],H_{full}[M]]
\stackrel{?}{\longrightarrow}
i\hbar D[\sharp_Q(NdM-MdN)]
}
\]

on the same two-node graph-changing Peter-Weyl habitat, with:

```text
physical H_E^sine;
full spin-changing H_L amplitudes;
canonical five-bracket phase;
upstream-fixed relative magnitude;
operator-first positive route square root;
no channel-dependent subtraction/refit.
```

Only after this passes should the calculation be expanded to multiple WKB/habitat probes, collective-spin/refinement scaling and a stronger simultaneous-cutoff theorem.

---

## 11. IR interpretation and separate extensions

Conditional on first-class continuum HDA and a nondegenerate `D=3` metric sector, the retained DeWitt/Dirac chain gives the GR target:

```text
one massless spin-2 tensor sector
with two TT helicities
and no non-decoupling scalar ghost.
```

Mirror force, `infoton`, the conditional `P_delta_g(k)~k^1.003414` foam spectrum and GW-driven route-mode resonance remain separate extensions and are not evidence for the gravity-core HDA.

---

## Canonical status statement

> **BCQG Core Candidate v1 now has a frozen q=2/PL-S3 kinematic sector, 3+1D-like scaling, a physically consistent sine-Hermitian Peter-Weyl Euclidean ordering with a preregistered two-node HDA PASS, a linear positive operator-first route-normal candidate with matrix-HDA PASS, a fixed-cutoff HDA composition theorem, an explicit conditional `Jmax~epsilon^-1/8` joint path, a nonzero exact Lorentzian raw logical amplitude, a five-bracket phase completion and an upstream conditional relative normalization. The principal operator bottleneck has collapsed to one calculation: the full spin-changing two-node `H_E^sine+(1+beta^2)H_L+R_operator-first` HDA.**
