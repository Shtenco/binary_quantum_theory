# Theory status — canonical ledger

**Frozen working frontier: 2026-08-15.**

This repository develops **BCQG Core Candidate v1**, a computable candidate quantum-gravity architecture. It is not an experimentally established theory of nature and does not by itself establish a mirror force, antigravity or a new particle.

Canonical integrated definition: `BCQG_CORE_CANDIDATE_V1.md`.

---

## 1. Gravity-core chain

```text
binary routes
 -> q=2
 -> octahedral S2 local link
 -> minimal flag / recursive PL S3
 -> d_space~3
 -> z~1
 -> 4D-like history
 -> smooth IR candidate
 -> SU(2)/Peter-Weyl quantum geometry
 -> H_E, V, K=[V,H_E]
 -> Lorentzian K-K-V structure
 -> geometry-dependent route-normal generator
 -> HDA composition certificate
 -> explicit admissible simultaneous-cutoff diagonal.
```

Frozen dimensional anchors:

```text
d_H          = 2.999229782
z            = 0.998281156
d_s(slice)   = 3.004393867
d_s(history) ~ 4.004393867.
```

The canonical minimal flag globalization of the `q=2` shell is the 16-cell boundary,

```text
(V,E,F,T)=(8,24,32,16)
Betti=(1,0,0,1),
```

with checked PL refinements

```text
16 -> 384 -> 9216 tetrahedra.
```

The 16-cell flag completion is part of the candidate definition. The stronger claim that the bare causal graph uniquely forces every possible nonflag global pairing is not asserted.

---

## 2. Route-normal HDA

The factorized ansatz

```text
H_geom tensor I_path
```

is exactly ruled out because it cannot generate the required route derivative.

The canonical route-normal operator is

\[
R[N;Q]=\frac12\{N,\sqrt{Q^{ab}P_aP_b}\}.
\]

Its principal symbol generates the metric structure function

\[
Q^{ab}(M\partial_bN-N\partial_bM)p_a.
\]

The two-node regulator-safe Euclidean geometry x route calculation gives

```text
Delta_joint(1/64)=0.014707752821092098
p_cross = 1.0058917161144039
p_EE    = 2.0074903905590453
p_joint = 1.0071260819282668.
```

At fixed safe cutoff,

```text
C_cross/D = O(epsilon)
C_GG/D    = O(epsilon^2),
```

so the declared full residual tends to zero when combined with the independently convergent route sector.

---

## 3. Simultaneous cutoff

The retained norm envelope is

```text
C_cross/D = O(epsilon Jmax^(13/2))
C_GG/D    = O(epsilon^2 Jmax^13).
```

For

```text
Jmax ~ epsilon^-alpha
```

both bounds decay whenever

```text
0 < alpha < 2/13.
```

BCQG Core Candidate v1 freezes the interior trajectory

```text
alpha=1/8
Jmax~epsilon^-1/8,
```

which yields

```text
C_cross/D = O(epsilon^(3/16))
C_GG/D    = O(epsilon^(3/8)).
```

This is an explicit conditional diagonal certificate, not a uniform theorem for arbitrary joint paths.

Evidence:

```text
JOINT_CUTOFF_DIAGONAL_CERTIFICATE.md
scripts/joint_cutoff_diagonal_gate.py
```

---

## 4. Lorentzian sector — raw amplitude is nonzero

The real-Ashtekar-Barbero relative structure is frozen as

```text
G_v=H_E,v+(1+beta^2)H_L,v.
```

For all-`j=1/2` input the full Lorentzian HH support is finite at the declared safe wall

```text
Jmax=13/2.
```

The old amplitude frontier

```text
P H_L P = 0 ?
```

is superseded at the **raw structural** level.

A completed exact environment-unbiased Peter-Weyl calculation at

```text
Jmax=7/2
16 logical environment states
full 24-term S4 orbit
```

gives

\[
\boxed{
L_{raw,1body}
=i\,1.3389293521464034\,Y+O(10^{-16}).
}
\]

Numerical controls:

```text
S4 covariance relative error = 1.3976239359266602e-15
max physical basis/volume leakage = 6.532094795930893e-16
raw Frobenius norm = 1.8935320488648653.
```

Therefore

```text
P L_raw P != 0
```

is a tested finite amplitude statement, not support counting.

Canonical evidence:

```text
PETER_WEYL_LORENTZIAN_ENVTRACE_RESULT.md
verification_results/PETER_WEYL_LORENTZIAN_ENVTRACE_ORBIT.json
scripts/peter_weyl_lorentzian_envtrace_block_gate.py
scripts/peter_weyl_lorentzian_envtrace_orbit_collector.py
```

---

## 5. Canonical commutator phase selects the nonzero Hermitian branch

The repository's raw Lorentzian stack uses

```text
K_raw=[V,H_E]
C_raw(O)=h[h^-1,O]
L_raw~Tr[C_raw(K_raw) C_raw(K_raw) C_raw(V)].
```

The corresponding declared classical Thiemann structure is

```text
{A,K}{A,K}{A,V}
with K~{V,H_E}.
```

After substituting the two `K` factors there are exactly five Poisson brackets. Under the canonical correspondence

\[
\{\ ,\ \}\to\frac1{i\hbar}[\ ,\ ],
\]

the universal complex phase is

\[
\boxed{(1/i)^5=-i}.
\]

Therefore the phase-completed one-body block is

\[
\boxed{
-iL_{raw,1body}
=1.3389293521464034\,Y+O(10^{-16}),
}
\]

up to the remaining **real** normalization/sign convention.

For the frozen matrix the Hermiticity defect of `-i L_raw` is about

```text
3.2e-16,
```

and its dimensionless structural eigenvalues are

```text
+/-1.3389293521464034.
```

Thus the earlier purely algebraic fork

```text
(L+L^dagger)/2  versus  (L-L^dagger)/(2i)
```

is narrowed by the declared nested-bracket quantization: the missing canonical bracket phase selects the second branch. The even projection performed **before** restoring the missing phase is not the quantization of the declared five-bracket structure.

Evidence:

```text
LORENTZIAN_COMMUTATOR_PHASE_CERTIFICATE.md
scripts/lorentzian_commutator_phase_gate.py
scripts/peter_weyl_lorentzian_onebody_ordering_gate.py
```

What remains open is no longer the complex phase. It is:

```text
real kappa/beta/hbar/regulator normalization
+ overall real sign convention
+ uniqueness/stability of the full symmetric factor ordering
+ complete two-node Lorentzian route-coupled HDA.
```

---

## 6. Corrected Euclidean logical return

Let `P` project to the all-`j=1/2` logical sector. The finite gate verifies

```text
P H_E P = 0
```

on all 32 logical columns.

The first nonzero environment-unbiased Euclidean return kernel is

```text
Kbar=(1/8)Tr_env P(H_E,0+H_E,1)^2P.
```

The current audited canonical values are

```text
II       = 9.04524203998966
A_rel    = 0.9644798301915488
J_shape  = -0.5564630119591318
J_orient = +2.18199564892363
Delta_aniso,ret = 2.738458660882762.
```

Mirror-forbidden odd-`Y` channels are suppressed to relative norm

```text
2.7985693281119945e-33.
```

The earlier values

```text
A_rel=0.9627752706476244
J_shape=-1.0989720235137607
J_orient=2.5842530086520437
Delta_aniso,ret=3.6832250321658044
```

are retired.

The audited 648-state decomposition reconstructs the direct kernel with matrix error

```text
8.606528098114035e-15
```

and has a mixed sign cone

```text
positive states = 392
negative states = 256.
```

Hence arbitrary positive state-diagonal weighting is not sign protected. The old `spin_cost` scan is retired as physical robustness evidence because every one-hit intermediate state has the same `spin_cost=3`.

The Euclidean `Kbar` is a short-time/leakage return kernel, not a static physical mass Hamiltonian.

---

## 7. IR gravity interpretation

Conditional on a first-class continuum HDA and a nondegenerate spatial `D=3` metric sector, the retained DeWitt/HDA uniqueness and Dirac-counting chain gives two local gravitational configuration degrees of freedom.

The IR target is

```text
one massless spin-2 tensor sector
with two TT helicities
and no non-decoupling scalar ghost.
```

The face-qubit/Plebanski/Urbantke and Regge/EH calculations are downstream composability and continuum controls; they do not substitute for the microscopic joint-limit proof.

---

## 8. Mirror / foam extensions are not gravity-core evidence

Mirror conjugation flips logical orientation `Y` while preserving the tested mirror-even intrinsic metric/shape data. Therefore the current metric architecture gives

```text
g00(+chi)=g00(-chi),
```

so orientation reversal alone does not produce metric antigravity.

A positive-kinetic one-particle mirror-force branch remains conditional on a physical nonzero matter matrix element and scale setting. A purely longitudinal Goldstone branch instead begins with a two-Goldstone potential `~r^-3`, hence force `~r^-4`.

The foam law

```text
P_delta_g(k)~k^1.003414
```

is conditional on interpreting the smoothing exponent as a true quantum RMS vacuum exponent. The GW information-mode resonance is conditional on a derived nonzero TT coupling.

Neither extension is used as evidence for the gravity-core HDA.

---

# Primary open problems

```text
1. freeze the remaining real Lorentzian normalization/sign and full symmetric factor ordering;
2. run the completed two-node H_E+H_L+R_Q commutator on the same route habitat;
3. repeat the full HDA on independent WKB/habitat channels and higher collective-spin sectors;
4. extend the simultaneous-cutoff proof beyond the current polynomial envelope / alpha=1/8 trajectory;
5. derive a Lorentzian quantum-history measure with global positivity/unitarity;
6. set the absolute Newton/length/time scale from a microscopic observable;
7. complete realistic chiral/anomaly-safe matter;
8. freeze dimensionless predictions before genuinely held-out and independent tests.
```

---

## Canonical status statement

> **BCQG Core Candidate v1 currently has a frozen q=2 / PL-S3 kinematic sector, 3+1D-like scaling, SU(2) Peter-Weyl quantum geometry, a geometry-dependent route-normal generator, a fixed-cutoff HDA composition certificate, an explicit conditional simultaneous-cutoff path `Jmax~epsilon^-1/8`, a nonzero exact finite Lorentzian raw logical one-body amplitude, and a canonical five-bracket phase completion that converts that raw `iY` block into a Hermitian `Y` block. The principal operator bottleneck is now the remaining real Lorentzian normalization/full factor-ordering freeze followed by the complete two-node Lorentzian route-coupled HDA.**
