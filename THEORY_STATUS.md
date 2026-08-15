# Theory status — canonical ledger

**Frozen working frontier: 2026-08-15.**

This repository develops **BCQG Core Candidate v1**, a computable candidate quantum-gravity architecture. It is not an experimentally established theory of nature and does not by itself establish a mirror force, antigravity or a new particle.

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
binary routes -> q=2 -> octahedral S2 local link
-> minimal flag / recursive PL S3
-> d_space~3 -> z~1 -> 4D-like history -> smooth IR candidate.
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

The minimal 8-vertex flag globalization is part of the candidate definition. The stronger statement that the bare causal graph uniquely fixes every possible nonflag globalization is not asserted.

---

## 2. Physical Euclidean Peter-Weyl ordering — preregistered PASS

The physical stack uses

\[
\boxed{H_E^{sine}=(T-T^\dagger)/(2i)},
\qquad
\boxed{K_{sine}=[V,H_E^{sine}]}.
\]

The older `H_plus=(T+T^dagger)/2` result is historical only.

Preregistered physical-sine two-node result:

```text
support(H0)=support(H1)=37
||H0||=2.1712581763270546
||H1||=2.171258176327055
support([H0,H1])=514
||[H0,H1]||=2.8794538147049544
p_cross=1.0056948923496356
p_GG=2.007490390559045
p_joint=1.0076444430189475
Delta_joint(1/64)=0.020030338775070305
```

GitHub Actions provenance:

```text
run 31855735615
artifact digest sha256:21e2da508fd583d9007a5bd400d074e8cee39990656e6c75e5968d2601323526
```

Thus the physical sine ordering preserves

\[
C_{cross}/D=O(\epsilon),
\qquad
C_{GG}/D=O(\epsilon^2),
\qquad
\Delta_{joint}=O(\epsilon).
\]

---

## 3. Quantum route normal — operator-first

Expectation-first square-root maps are state dependent and nonlinear on superpositions, so they remain semiclassical controls only.

On geometry × route Hilbert space,

\[
A=Q^{ab}\otimes P_aP_b=\sum_iB_i^\dagger B_i\ge0,
\]

hence the production route candidate is the positive linear operator

\[
\boxed{R_{op}[N]=\frac12\left\{N,\sqrt{\hat Q^{ab}\hat P_a\hat P_b}\right\}}.
\]

The matrix Sylvester identity

\[
\Omega\partial_{p_c}\Omega+(\partial_{p_c}\Omega)\Omega=2Q^{cb}p_b
\]

preserves the operator-valued HDA principal structure function.

Canonical one-node/logical finite gate:

```text
endpoint(epsilon=1/64, carrier=8)=3.837772425e-7
p=0.999960897
```

An independent two-node 4×4 reference additionally gives

```text
K0K0 endpoint(1/64)=8.205159710207801e-7
p=0.9999594708960342
sparse-Fourier vs 48x48 FFT max relative difference=5.74e-8
```

but that two-node reference remains non-canonical until its branch CI completes.

---

## 4. Fixed-cutoff and simultaneous-cutoff structure

At fixed regulator-safe cutoff,

```text
C_cross/D = O(epsilon)
C_GG/D    = O(epsilon^2).
```

The retained simultaneous-cutoff envelope is

```text
C_cross/D = O(epsilon Jmax^(13/2))
C_GG/D    = O(epsilon^2 Jmax^13).
```

For `Jmax~epsilon^-alpha`, both decay for `0<alpha<2/13`. BCQG v1 freezes

```text
alpha=1/8
Jmax~epsilon^-1/8
```

which gives

```text
C_cross/D = O(epsilon^(3/16))
C_GG/D    = O(epsilon^(3/8)).
```

This is a conditional diagonal certificate, not a uniform arbitrary-path theorem.

---

## 5. Lorentzian raw amplitude and five-bracket phase

The exact environment-unbiased Peter-Weyl amplitude at `Jmax=7/2`, all 16 logical environments and the full 24-term S4 orbit is

\[
\boxed{L_{raw,1body}=i\,1.3389293521464034\,Y+O(10^{-16})}.
\]

Controls:

```text
S4 covariance defect = 1.3976239359266602e-15
physical basis/volume leakage = 6.532094795930893e-16
raw Frobenius norm = 1.8935320488648653.
```

The nested Thiemann structure contains five Poisson brackets after substituting both `K~{V,H_E}` factors, hence

\[
\boxed{(1/i)^5=-i},
\qquad
\boxed{H_{phase}=-iL_{raw}}.
\]

Thus the frozen logical phase-completed block is Hermitian:

\[
H_{phase,1body}=1.3389293521464034Y+O(10^{-16}).
\]

---

## 6. Euclidean normalization and Lorentzian **signed** relative coefficient

The production tetrahedral combinatorics fixes

\[
\boxed{H_E^{phys}=n_EH_E^{sine,raw}},
\qquad
\boxed{n_E=-\frac{2}{3\hbar}}.
\]

Keeping the declared Thiemann correction sign gives

\[
\boxed{H_{corr}=-\frac{32}{9\hbar^7}H_{phase}}.
\]

The repository writes

\[
G=H_E+(1+\beta^2)H_L,
\]

therefore

\[
\boxed{H_L=-\frac{32}{9\hbar^7(1+\beta^2)}H_{phase}}.
\]

At `beta=hbar=1`:

```text
H_E^phys / E_raw       = -2/3
bare H_L / H_phase     = -16/9
full correction/Hphase = -32/9
full correction/L_raw  = +32 i/9
```

so the raw-code geometry operator is frozen as

\[
\boxed{G_v=-\frac23E_v+\frac{32i}{9}L_{raw,v}}.
\]

Independent CI evidence:

```text
workflow: lorentzian-repo-sign
run: 31857722477
artifact digest: sha256:10f538abd68dc8945a46ec03410b5e4490a5d8e1fbbb05d56a10a56fd6220101
fitting_used=false
```

Signed structural consequences at `beta=hbar=1`:

```text
local bare H_L Y        = -2.3803188482602726
local full correction Y = -4.760637696520545
16-cell bare pair coeff  = -76.17020314432872
16-cell full pair coeff  = -152.34040628865745
```

These are relative dimensionless operator coefficients, not physical energies. **The Lorentzian relative sign is no longer open.**

---

## 7. Signed Lorentzian × operator-first route regression

For the logical operator-first route average,

\[
-i[c_LY,\Omega_{op}]
=0.0536574847984X+0.0929374897107Z.
\]

With the frozen full `beta=1` correction coefficient `-32/9`, the signed regression target is

\[
\boxed{-0.1907821681721X-0.3304444078603Z},
\]

with shape coefficient norm

```text
0.3815643358315.
```

Expectation-first isotropic averaging erases this cross exactly, reinforcing why it is not the final quantum ordering.

This is a logical subchannel regression, not the full graph-changing HDA.

---

## 8. Corrected Euclidean logical return

The exact first-order rule remains

```text
P H_E P=0.
```

The audited return kernel has

```text
A_rel=0.9644798301915488
J_shape=-0.5564630119591318
J_orient=+2.18199564892363
Delta_aniso,ret=2.738458660882762
648 states = 392 positive + 256 negative
forbidden odd-Y norm = 2.7985693281119945e-33.
```

The older `Delta_aniso,ret=3.6832250321658044` is retired.

---

## 9. Current single gravity-operator frontier

The current full operator is

\[
\boxed{H_{full}[N]=H_E^{sine}[N]+(1+\beta^2)H_L[N]+R_{op}[N]}.
\]

The next killer calculation is

\[
\boxed{[H_{full}[N],H_{full}[M]]\stackrel{?}{\longrightarrow}i\hbar D[\sharp_Q(NdM-MdN)]}.
\]

It is now preregistered with:

```text
physical H_E^sine
full spin-changing 24-term L_raw
five-bracket phase
signed upstream coefficient: G_v=(-2/3)E_v+(32i/9)L_raw,v at beta=hbar=1
operator-first positive route square root
nonconstant off-shell lapses
no channel subtraction, sign flip, coefficient refit or threshold retuning.
```

Exact geometry channels are decomposed as

```text
EE = E0E1-E1E0
EL = E0L1-E1L0
LE = L0E1-L1E0
LL = L0L1-L1L0
```

with frozen walls `5/2`, `9/2`, `9/2`, `13/2` respectively. A distributed 24-way full-state Lorentzian column pipeline and an exact sparse-Fourier operator-route engine are now in the branch to make the off-shell calculation computationally feasible.

No full-HDA result is promoted until those exact artifacts complete.

---

## 10. IR target and extensions

Conditional on first-class continuum HDA and a nondegenerate `D=3` metric sector, the retained DeWitt/Dirac chain targets one massless spin-2 tensor sector with two TT helicities and no non-decoupling scalar ghost.

Mirror force, `infoton`, the conditional foam spectrum and GW-resonance ideas remain separate extensions and are not evidence for the gravity-core HDA.

---

## Canonical status statement

> **BCQG Core Candidate v1 now has q=2/PL-S3 kinematics, 3+1D-like scaling, a physical sine-Hermitian Peter-Weyl Euclidean ordering with preregistered two-node HDA PASS, a linear positive operator-first route candidate with matrix-HDA PASS, fixed-cutoff and explicit conditional joint-cutoff control, a nonzero exact Lorentzian raw logical amplitude, a five-bracket phase completion, and an upstream CI-verified signed relative Lorentzian coefficient. The remaining principal operator bottleneck is the exact full spin-changing two-node `H_E^sine+(1+beta^2)H_L+R_operator-first` HDA; sign and relative magnitude are no longer fit freedoms.**
