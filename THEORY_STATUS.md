# Theory status — canonical ledger

**Frozen 2026-08-15.** This file supersedes historical frontier wording elsewhere in the repository.

The project is a **candidate quantum-gravity architecture**, not an experimentally established theory of nature.

Canonical integrated definition: `BCQG_CORE_CANDIDATE_V1.md`.

---

## 1. Frozen gravity-core chain

```text
bits
 -> q=2
 -> local octahedral S2
 -> minimal flag / recursive PL S3
 -> 3D slice scaling
 -> z~1
 -> 4D-like history
 -> smooth IR candidate
 -> SU(2)/Peter-Weyl quantum geometry
 -> H_E
 -> K=[V,H_E]
 -> C(V), C(K)
 -> H_E+(1+beta^2)H_L
 -> geometry-dependent route-normal generator
 -> fixed-cutoff HDA composition certificate
 -> explicit admissible simultaneous-cutoff diagonal.
```

Frozen numerical anchors:

```text
d_H          = 2.999229782
z            = 0.998281156
d_s(slice)   = 3.004393867
d_s(history) ~ 4.004393867
```

The preregistered two-node Euclidean geometry x route result is

```text
Delta_joint(1/64)=0.014707752821092098
p_cross = 1.0058917161144039
p_EE    = 2.0074903905590453
p_joint = 1.0071260819282668.
```

For all-`j=1/2` input, a full Lorentzian HH support pair is cutoff-safe at

```text
Jmax=13/2.
```

At fixed safe cutoff,

```text
C_cross/D = O(epsilon)
C_GG/D    = O(epsilon^2)
```

and therefore

```text
Delta_full
 <= Delta_route
  + C_cross epsilon
  + C_GG epsilon^2
 -> 0.
```

This is the frozen fixed-cutoff core certificate.

---

## 2. Explicit simultaneous-cutoff diagonal

The retained norm envelope is

```text
C_cross/D = O(epsilon * Jmax^(13/2))
C_GG/D    = O(epsilon^2 * Jmax^13).
```

For

```text
Jmax(epsilon) ~ epsilon^-alpha
```

both declared contamination bounds vanish whenever

```text
0 < alpha < 2/13.
```

BCQG Core Candidate v1 freezes the simple interior trajectory

```text
alpha = 1/8
Jmax  ~ epsilon^-1/8.
```

It gives

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

## 3. Global q=2 manifold scope

The canonical minimal flag globalization of the q=2 shell is the 16-cell boundary,

```text
(V,E,F,T)=(8,24,32,16)
Betti=(1,0,0,1),
```

with octahedral vertex links and stable checked barycentric PL refinements

```text
16 -> 384 -> 9216 tetrahedra.
```

BCQG Core Candidate v1 promotes this minimal flag completion to part of the candidate definition.

The stronger claim

```text
the bare causal graph uniquely forces every possible global face pairing
```

remains unproved and is not required by the frozen candidate definition.

---

## 4. Route-normal HDA result

The old factorized form

```text
H_geom[N] tensor I_path
```

is exactly ruled out because its commutator has no path-derivative component.

The canonical route-normal completion is

```text
R[N;Q]
 = 1/2 {N, sqrt(Q^{ab} P_a P_b)}.
```

Its principal symbol generates

```text
Q^{ab}(M d_b N-N d_b M) p_a,
```

which is the required metric structure function up to the frozen global orientation convention.

The route metric is geometry dependent; it is not an externally fixed background metric.

---

## 5. Lorentzian operator status

The classical real-Ashtekar-Barbero coefficient is frozen as

```text
G_v = H_E,v + (1+beta^2) H_L,v.
```

The support wall and fixed-cutoff composition theorem are retained.

A distinct amplitude question remains open:

```text
P H_L P = 0 ?
```

The doubled-spin grading gives

```text
P H_E P = 0
```

exactly, while `P H_L P` is allowed by grading. Therefore a direct logical term in the complete constraint, if nonzero, is Lorentzian at leading order.

The heavy direct epsilon-oriented `K-K-V` logical-projection gate exists on the research branch but has not yet produced a completed canonical result. It must not be replaced by support counting or by the fixed-cutoff composition theorem; those are different statements.

Primary next calculation:

```text
full Hermitian/prefactor-correct P H_L P
 -> S4/mirror decomposition
 -> route-coupled two-node Lorentzian habitat test.
```

---

## 6. DeWitt / graviton interpretation

Conditional on a first-class continuum HDA and a nondegenerate spatial `D=3` metric sector, the retained DeWitt/HDA uniqueness and Dirac-counting chain gives the GR kinetic structure and two local gravitational configuration degrees of freedom.

The physical IR target is therefore

```text
one massless spin-2 tensor sector
with two TT helicities
and no non-decoupling scalar ghost.
```

Four microscopic spin-`1/2` qubits contain exactly one `j=2` irrep. The extremal `m=+/-2` states form an exact finite two-state carrier inside that irrep. This is a representation-theory bridge, not by itself a proof that the interacting microscopic theory produces a physical graviton.

---

## 7. Canonical Peter-Weyl logical anisotropy — corrected

Let `P` project to the all-`j=1/2` logical sector. The finite gate verifies

```text
P H_E P = 0
```

exactly on all 32 logical columns.

The first nonzero environment-unbiased structural return kernel is

```text
Kbar_01
 = (1/8) Tr_env P(H_E,0+H_E,1)^2 P.
```

The **current audited canonical values** are

```text
II       = 9.04524203998966
A_rel    = 0.9644798301915488
J_shape  = -0.5564630119591318
J_orient = +2.18199564892363
Delta_aniso,ret = 2.738458660882762.
```

The mirror-forbidden odd-`Y` channels are suppressed to relative norm

```text
2.7985693281119945e-33.
```

Thus

```text
mirror Z2         -> survives
Bell-parent SU(2) -> strongly broken in the raw Euclidean return kernel.
```

The earlier canonical-ledger values

```text
A_rel=0.9627752706476244
J_shape=-1.0989720235137607
J_orient=2.5842530086520437
Delta_aniso,ret=3.6832250321658044
```

are **retired**. They came from an older artifact and must not be used for current claims.

The audited 648-state decomposition reconstructs the direct kernel to matrix error

```text
8.606528098114035e-15
```

with

```text
positive states = 392
negative states = 256
zero states     = 0
sum positive Delta = +4.052816595873667
sum negative Delta = -1.3143579349909067.
```

Therefore arbitrary positive state-diagonal weighting is not sign protected. The old spin-cost robustness scan is vacuous because all one-hit intermediate states have the same `spin_cost=3`; it is retired as physical evidence.

`Kbar_01` remains a short-time/leakage return kernel, not a proved static mass Hamiltonian.

Canonical evidence:

```text
PETER_WEYL_LOGICAL_ANISOTROPY.md
PETER_WEYL_ANISOTROPY_WEIGHT_ROBUSTNESS.md
scripts/peter_weyl_logical_anisotropy_gate.py
scripts/peter_weyl_anisotropy_resolvent_audit_fast_gate.py
```

---

## 8. Exact S4 coarse symmetry

The exact diagonal tetrahedral face-permutation twirl gives

```text
one-cell invariant space: span{I}
two-cell invariant space: span{II, XX+ZZ, YY}.
```

Therefore tetrahedral symmetry permits one scalar pseudospin split

```text
Delta_aniso = J_orientation-J_shape
```

and does not force pseudospin SU(2).

---

## 9. Mirror/chirality extension — separate from gravity core

On the logical geometry qubit,

```text
X -> +X
Z -> +Z
Y -> -Y
Q_orientation=(sqrt(3)/4)Y.
```

Mirror conjugation reverses orientation while preserving intrinsic shape, metric data and absolute volume. Therefore the tested mirror-even metric architecture gives

```text
g00(+chi)=g00(-chi).
```

Mirror orientation alone does **not** produce metric antigravity.

A healthy positive-kinetic one-particle mirror branch remains conditional. For a light mode,

```text
V_sigma(r)
 = - beta_1 beta_2 m1 m2 chi1 chi2
   exp(-m_sigma r)/(4*pi*Z_sigma*r)
```

with

```text
alpha=beta_m^2/(4*pi*G*Z_sigma)
alpha_crit(x)=exp(x)/(1+x), x=m_sigma r.
```

Pure geometry has no automatic linear matter charge:

```text
beta_geometry=0.
```

A realistic nonzero `beta_m` and physical scale remain open.

---

## 10. Mirror-order / range frontier

The 16-cell tetrahedron dual graph is `Q4`. The staggered logical orientation variable gives exact finite mirror vacua and persists through the checked PL refinements.

The Bell-gluing parent maps exactly to an antiferromagnetic Heisenberg pseudospin model on the bipartite dual graph, but this pseudospin SU(2) is not a symmetry of the complete tested geometry dynamics: the corrected Peter-Weyl return kernel is strongly anisotropic.

The primary mirror dynamical question is therefore

```text
Delta_aniso^eff
 = J_orientation^eff-J_shape^eff
 -> 0 ?
```

under the physically derived constrained intermediate-state operator and PL/RG flow.

If the IR is a purely longitudinal Goldstone branch, the leading free two-Goldstone potential is

```text
V_2G(r)=-Q1Q2/(32*pi^3*v^2*r^3),
```

so the force scales as `r^-4`, not Newton-like `r^-2`.

A `1/r` mirror potential therefore still requires a light one-particle pole or a microscopic source with linear coupling to a transverse mode.

---

## 11. Foam / information-mode extension

The inference

```text
P_foam(k) ~ k^1.003414
```

is conditional on identifying the frozen metric smoothing exponent with a true quantum RMS vacuum exponent.

The GW-driven information-mode Mathieu resonance is also conditional on a nonzero microscopic TT route/information coupling.

Neither extension is evidence for the gravity-core HDA result.

---

# Current primary frontiers

## Gravity core

```text
1. finish direct physical P H_L P amplitude calculation;
2. test the complete Lorentzian route-coupled HDA on multiple independent habitats;
3. replace diagonal flux-metric expectations with the required operator-valued metric where feasible;
4. enlarge the proved simultaneous-cutoff class beyond the canonical alpha=1/8 path;
5. prove a uniform joint limit or explicitly characterize its domain of validity;
6. derive a Lorentzian quantum/history measure and global unitarity/positivity;
7. set the absolute Newton/length/time scale from a microscopic observable;
8. preregister blind dimensionless predictions and obtain independent replication.
```

## Matter / beyond pure gravity

```text
1. realistic gauge group and chiral matter;
2. all local and global anomaly cancellation;
3. physical Yukawa/mass structure;
4. derived beta_m rather than an input coupling;
5. complete matter x route x Peter-Weyl HDA.
```

---

## Canonical status statement

The repository now supports the following precise wording:

> **BCQG Core Candidate v1 is a computable candidate quantum-gravity architecture with a frozen q=2 / PL-S3 kinematic sector, 3+1D-like scaling, SU(2) Peter-Weyl quantum geometry, a geometry-dependent square-root route-normal generator, a fixed-cutoff HDA composition certificate, and an explicit conditional simultaneous-cutoff trajectory `Jmax~epsilon^-1/8`. It is not yet an experimentally established theory of nature, a uniform all-cutoff theorem, or a completed theory of realistic matter.**
