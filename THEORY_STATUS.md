# Theory status — BCQG Candidate Theory v1.2

**Frozen working frontier: 2026-08-15.**

BCQG v1.2 is a computable candidate quantum-gravity architecture. It is not experimentally established and does not by itself establish a fifth force, antigravity, a new particle, or an absolute physical scale.

Canonical entry points:

```text
START_HERE.md
BCQG_CANDIDATE_THEORY_V1_2.md
BCQG_CORE_CANDIDATE_V1_2.md
THEORY_STATUS.md
theory_gates.json
```

## 1. Kinematics / topology — definition + tested finite

The frozen chain is

```text
binary route family -> q=2 -> octahedral S2 local link
-> chosen minimal flag 16-cell boundary -> closed orientable PL S3
-> recursive PL refinements.
```

The PL completion is part of the candidate definition; uniqueness from the bare causal graph is not claimed.

Finite scaling anchors:

```text
d_H=2.999229782
z=0.998281156
d_s(slice)=3.004393867
d_s(history)~4.004393867
```

## 2. Euclidean geometry — tested finite PASS

\[
E=H_E^{sine}=(T-T^\dagger)/(2i),\qquad K=[V,E].
\]

Preregistered two-node result:

```text
||H0||=||H1||=2.171258176327055
||[H0,H1]||=2.8794538147049544
p_cross=1.0056948923496356
p_GG=2.007490390559045
p_joint=1.0076444430189475
Delta_joint(1/64)=0.020030338775070305
```

The logical selection rule `P E P=0` remains exact on the tested all-`j=1/2` logical sector.

## 3. Lorentzian sector — corrected production definition

Raw structural operator:

\[
L_{raw}\sim\mathrm{Tr}[C(K)C(K)C(V)].
\]

Environment-unbiased one-body result:

\[
L_{raw,1body}=i\,1.3389293521464034Y+O(10^{-16}).
\]

The five nested Poisson brackets fix the universal `(1/i)^5=-i` phase. But exact conditional MITM blocks demonstrate that full unsymmetrized `L_raw` is not globally anti-Hermitian. Therefore v1.2 defines

\[
\boxed{S=-\frac{i}{2}(L_{raw}-L_{raw}^\dagger)}
\]

and at `beta=hbar=1`

\[
\boxed{G=-\frac23E-\frac{32}{9}S}.
\]

The historical `G=(-2/3)E+(32i/9)L_raw` is only the reduction on already anti-Hermitian raw sectors. The accepted one-body correction remains `-4.760637696520545 Y` in structural units.

The projection `S=Herm(-iL_raw)` is itself unique as the linear projection with Hermitian range and anti-Hermitian kernel, and is the unique Hilbert-Schmidt closest Hermitian operator. Broader pre-projection ordering uniqueness is not claimed.

## 4. Multi-node Lorentzian evidence — tested finite

The recovered diagonal-environment Walsh block contains finite pseudoscalar neighbor correlations. With nodes 3,4 fixed at K=0:

```text
YII    = +i 0.3359014033398999
YZ1I   = -i 0.00702861722247964
YIZ2   = +i 0.002338130606598994
YZ1Z2  = +i 0.004676261213197787
```

The Hermitian completion removes the real unsymmetrized X/Z pieces and keeps the imaginary pseudoscalar sector. Off-diagonal environment transitions remain open.

## 5. Route normal — exhaustive tested finite PASS

Production route operator:

\[
R_{op}[N]=\frac12\{N,\sqrt{\hat Q^{ab}\hat P_a\hat P_b}\},
\qquad \hat Q^{ab}\hat P_a\hat P_b=\sum_iB_i^\dagger B_i\ge0.
\]

The old five-sector sample has now been superseded by an exhaustive one-step `H_E^sine`-reached regression:

```text
H_E basis support                 41
distinct fixed-spin sectors       33
nonzero power-law sectors         30
numerical-zero sectors             3
p_min=0.9997944068141106
p_max=0.9999830934452917
max endpoint=1.405841033798129e-05
minimum symbol eigenvalue=-1.0658141036401503e-14
```

All 33 distinct sectors pass the frozen criteria; the negative minimum is roundoff-consistent with zero.

## 6. Exact parity structure — proved inside declared operator algebra

For

\[
\Pi=(-1)^{\sum_e2j_e}
\]

we have

```text
E odd
S even
R_op even
D even.
```

Therefore on the even seed:

```text
even: EE, SS, SxR, route/D
odd : ES, SE, ExR.
```

Even and odd outputs are orthogonal. Consequently a mixed odd anomaly cannot be concealed by destructive interference with the even target.

## 7. Spin-cutoff saturation — proved for the frozen finite-depth habitat

The exact support count gives

```text
max HE hits/link = 2
max L hits/link  = 6
max HH hits/link = 12
```

starting from `j=1/2`, hence

\[
\boxed{J_{max}^{safe}=13/2}.
\]

`S` inherits the same L/L-dagger support and `R_op` preserves link irreps. Thus for the preregistered all-`j=1/2` finite-depth two-node calculation

\[
\boxed{J_{max}\ge13/2\Rightarrow\text{spin-cutoff remainder}=0.}
\]

This is stronger than the old conditional `Jmax~epsilon^-1/8` envelope for this habitat. The latter is now an extension tool for growing-spin/depth/refinement families.

## 8. Full operator-first HDA — cutoff-saturated conditional closure

For smooth lapse probes `N=Nbar+epsilon*n`, `M=Mbar+epsilon*m`, the pure geometry antisymmetric smear has no zeroth-order term. The dangerous mixed route inverse-epsilon piece cancels exactly before matrix elements.

With the frozen WKB target `D=O(epsilon^-1)`:

\[
C_{G\times R}/D=O(\epsilon),\qquad C_{GG}/D=O(\epsilon^2).
\]

Since the exhaustive route regression has `p~1` and the cutoff remainder is zero above `13/2`, the v1.2 core result is

\[
\boxed{\Delta_{full}=O(\epsilon^{\min(p,1)})\to0}
\]

on the declared two-node WKB habitat.

This closes the principal HDA bridge **on that controlled habitat**. It is not a uniform theorem for arbitrary initial spins, growing operator depth, arbitrary beta, or all collective states.

## 9. Remaining physical finite channel falsifier

The Hermitian geometry commutator is preregistered as

\[
\boxed{[G_0,G_1]=\frac49EE+\frac{64}{27}(ES+SE)+\frac{1024}{81}SS}
\]

with sufficient walls

```text
EE 5/2
ES 9/2
SE 9/2
SS 13/2.
```

Completing `ES/SE/SS` remains valuable for detecting factor-ordering/scalar-projection/implementation anomalies and unusually large finite coefficients. It is an independent finite falsifier, not the logical foundation of the asymptotic theorem. A timeout is not a physics FAIL.

## 10. Conditional GR universality

If the collective IR has a nondegenerate local D=3 metric and the standard first-class HDA, then HDA fixes the inverse-DeWitt coefficient `c=1/2`; GR constraint rank is `3_G+3_D+1_H`; Dirac counting leaves two local configuration modes; and a local two-derivative tensor phase has the relativistic cone.

This remains conditional. A BF/topological first-class rank is a FAIL even if a subset of commutators closes.

## 11. Open frontier

Still open:

1. uniqueness among alternative microscopic factor orderings used to define `L_raw` before the unique Hermitian projection;
2. exhaustive finite route test for all `S`-reached sectors;
3. off-diagonal multi-node Lorentzian blocks;
4. direct `ES/SE/SS` finite calibration;
5. independent habitats and collective states;
6. uniform refinement theorem with growing spin/depth;
7. collective IR first-class rank/reducibility;
8. matter coupling, Newton normalization and physical scale;
9. experiment.

Mirror/infoton/foam/GW-resonance branches remain extensions and are not used to certify the gravity core.

## Canonical status statement

> **BCQG Candidate Theory v1.2 has a single Hermitian production Hamiltonian, an exact finite spin wall at Jmax=13/2 for the preregistered all-j=1/2 two-node habitat, exhaustive route evidence over all 33 one-step Euclidean-reached sectors, a unique minimal Hermitian projection of the fixed raw stack, and a cutoff-saturated operator-first HDA composition theorem on that habitat. The remaining frontier is extension and falsification — not invention of another core Hamiltonian.**
