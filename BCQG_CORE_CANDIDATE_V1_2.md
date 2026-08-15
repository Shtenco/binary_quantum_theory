# BCQG Core Candidate v1.2

**Canonical compact gravity definition.** Not experimentally established.

## 1. Kinematics

Frozen microscopic route rule:

\[
q+2=2^q\Rightarrow q=2,
\qquad \Sigma Q_2\cong S^2.
\]

The candidate **defines** the minimal flag globalization as the 16-cell boundary, a closed orientable PL `S^3`, and uses recursive PL refinements. This is a model choice with tested topology/stability, not a uniqueness theorem from the bare graph.

Held-out scaling:

```text
d_H=2.999229782
z=0.998281156
d_s(slice)=3.004393867
d_s(history)~4.004393867
```

## 2. Quantum geometry

\[
E_v=H_{E,v}^{sine}=\frac{T_v-T_v^\dagger}{2i},
\qquad K=[V,E].
\]

Physical-sine two-node finite HDA:

```text
p_cross=1.0056948923496356
p_GG=2.007490390559045
p_joint=1.0076444430189475
Delta_joint(1/64)=0.020030338775070305
```

and on the all-`j=1/2` logical sector `P E P=0`.

## 3. Hermitian Lorentzian sector

The raw structural stack is `L_raw~Tr[C(K)C(K)C(V)]`. Exact finite environment blocks show that unsymmetrized `L_raw` is not globally anti-Hermitian. Therefore define

\[
\boxed{S_v=-\frac{i}{2}(L_{raw,v}-L_{raw,v}^\dagger)}.
\]

At `beta=hbar=1` the production geometry operator is

\[
\boxed{G_v=-\frac23E_v-\frac{32}{9}S_v}
\]

or

\[
G_v=-\frac23E_v+\frac{16i}{9}(L_{raw,v}-L_{raw,v}^\dagger).
\]

The old `(-2/3)E+(32i/9)L_raw` formula is only the exact reduction on sectors where `L_raw^dagger=-L_raw`.

Environment-unbiased one-body anchor:

\[
L_{raw,1body}=i\,1.3389293521464034Y,
\qquad H_{corr,1body}=-4.760637696520545Y.
\]

## 4. Route operator

\[
A=\hat Q^{ab}\hat P_a\hat P_b=\sum_iB_i^\dagger B_i\ge0,
\]

\[
\boxed{R_{op}[N]=\frac12\{N,A^{1/2}\}}.
\]

Exhaustive one-step Euclidean-reached finite regression:

```text
41 H_E outputs
33 distinct fixed-spin sectors
30 power-law sectors: p=0.999794406814..0.999983093445
3 numerical-zero sectors
max endpoint=1.405841033798129e-05
min symbol eigenvalue=-1.0658141036401503e-14 (roundoff zero)
```

## 5. Exact parity split

For `Pi=(-1)^(sum_e 2j_e)`:

```text
E odd
S even
R_op even
D even.
```

Hence on the even seed:

```text
even: EE, SS, SxR, route/D
odd : ES, SE, ExR.
```

The even and odd anomaly outputs are orthogonal and cannot cancel each other.

## 6. Cutoff-saturated full HDA

The finite-depth all-`j=1/2` two-node HH support has at most 12 fundamental hits on one link, so

\[
\boxed{J_{max}\ge13/2}
\]

is support-exact. `S` does not enlarge this wall and `R_op` does not change link irreps.

For smooth lapses the pure geometry antisymmetric smear is `O(epsilon)` and the apparently dangerous mixed route `1/epsilon` term cancels exactly. With the WKB diffeo target `O(epsilon^-1)`, therefore

\[
C_{G\times R}/D=O(\epsilon),
\qquad C_{GG}/D=O(\epsilon^2).
\]

Combining with route `p~1` gives on this frozen habitat

\[
\boxed{\Delta_{full}=O(\epsilon^{\min(p,1)})\to0}
\]

with **zero spin-cutoff remainder** for `Jmax>=13/2`.

The old `Jmax~epsilon^-1/8` certificate is retained only for growing-spin/depth extension families; it is not required for this finite-depth core habitat.

## 7. Physical finite channel falsifier

With `G=aE+cS`, `a=-2/3`, `c=-32/9`,

\[
\boxed{
[G_0,G_1]=\frac49EE+\frac{64}{27}(ES+SE)+\frac{1024}{81}SS.
}
\]

Sufficient walls:

```text
EE 5/2
ES 9/2
SE 9/2
SS 13/2.
```

This channel calculation remains a strong finite implementation/factor-ordering falsifier, not a prerequisite for the asymptotic composition theorem.

## 8. Conditional IR target

If the collective continuum produces a nondegenerate local 3-metric and the standard first-class HDA, then

\[
c_{DW}=1/2,
\]

GR first-class rank is `3_G+3_D+1_H`, and Dirac counting leaves two local gravitational configuration modes. A BF/topological rank is a FAIL even if some algebra closes.

## 9. Open frontier

Open rather than hidden:

- uniqueness among alternative microscopic factor orderings used to define `L_raw` before the unique Hermitian projection;
- all `S`-reached route sectors as an exhaustive finite regression;
- off-diagonal multi-node Lorentzian blocks;
- direct `ES/SE/SS` finite calibration;
- independent habitats/collective refinement;
- uniform theorem for growing initial spin/operator depth;
- IR first-class rank demonstration;
- matter, Newton scale setting, experiments.

Canonical detailed statement: `BCQG_CANDIDATE_THEORY_V1_2.md`.
