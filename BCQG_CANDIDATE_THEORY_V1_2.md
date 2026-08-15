# BCQG Candidate Theory v1.2 — Hermitian, cutoff-saturated operator-first core

**Status:** mathematically/computationally specified candidate quantum-gravity architecture. It is not experimentally established and does not by itself establish a new force, particle, antigravity, or an absolute energy/length scale.

This version supersedes v1.1 as the canonical theory statement. The decisive changes are:

1. the full Lorentzian sector is defined by its Hermitian completion, not by treating unsymmetrized `L_raw` as globally anti-Hermitian;
2. the preregistered all-`j=1/2` finite-depth two-node HDA has a strict support wall `Jmax=13/2`, so the spin-cutoff remainder is exactly zero above that wall;
3. the operator-first route regression has been exhausted over all 33 distinct one-step `H_E^sine`-reached fixed-spin sectors;
4. doubled-spin parity separates even and odd anomaly channels, preventing hidden cancellations between them.

---

## 1. Epistemic levels

BCQG v1.2 uses four labels and does not mix them:

- **definition** — a frozen model choice;
- **proved** — an algebraic/topological statement under explicitly stated assumptions;
- **tested finite** — a completed finite computation/regression;
- **conditional** — an IR/continuum consequence requiring additional hypotheses.

A finite PASS is not an experiment. A conditional HDA-to-GR inference is not a proof that nature realizes BCQG.

---

## 2. Microscopic kinematics and spatial completion

The frozen binary-route family obeys

\[
q+2=2^q,
\]

with the nontrivial integer solution

\[
\boxed{q=2}.
\]

For the route rewrite family the asymptotic volume exponent is

\[
d_H=q+1,
\]

so `q=2` selects spatial scaling near three. The route labels form `Q_2=C_4`; suspension by the two causal endpoints gives an octahedral local link

\[
\boxed{\Sigma Q_2\cong S^2}.
\]

BCQG **defines** its canonical globalization to be the minimal flag completion: the boundary of the 16-cell,

\[
(V,E,F,T)=(8,24,32,16),\qquad \beta=(1,0,0,1),
\]

a closed orientable PL `S^3`. Barycentric refinements preserve the PL-manifold class and have been explicitly rechecked through the stored finite levels.

This is an existence/stability result for the frozen completion rule. BCQG does **not** claim that the bare causal graph uniquely forces this gluing among every conceivable nonflag completion.

---

## 3. Dimensional and relativistic scaling

Held-out finite scaling anchors are

\[
\boxed{d_H=2.999229782},\qquad
\boxed{z=0.998281156},
\]

\[
\boxed{d_s^{slice}=3.004393867},\qquad
\boxed{d_s^{history}\simeq4.004393867}.
\]

These numbers support a `3+1`-like continuum window; they are not by themselves a derivation of Einstein dynamics.

Independently, under the binary-adjoint assumptions, the traceless qubit observable algebra is

\[
su(2)\simeq\mathbb R^3,
\]

and `SU(2)/Z_2 ~= SO(3)` supplies full three-dimensional rotational freedom. This gives a structural reason why the qubit is special. The claim remains conditional on flux geometry, closure, and restoration of full local isotropy.

---

## 4. Peter-Weyl quantum geometry

The production Euclidean operator is

\[
\boxed{E_v\equiv H_{E,v}^{sine}=\frac{T_v-T_v^\dagger}{2i}},
\]

and

\[
\boxed{K=[V,E]}.
\]

The preregistered physical-sine two-node finite HDA gate passed:

```text
||H0||=||H1||=2.171258176327055
||[H0,H1]||=2.8794538147049544
p_cross=1.0056948923496356
p_GG=2.007490390559045
p_joint=1.0076444430189475
Delta_joint(1/64)=0.020030338775070305
```

On the all-`j=1/2` logical sector,

\[
\boxed{P E_v P=0},
\]

so first-order logical return is not Euclidean.

---

## 5. Lorentzian raw stack and mandatory Hermitian completion

The structural Lorentzian raw operator is the epsilon-oriented sum built from

\[
L_{raw}\sim \mathrm{Tr}_{aux}[C(K)C(K)C(V)].
\]

The environment-unbiased one-body calculation gives

\[
\boxed{L_{raw,1body}=i\,1.3389293521464034\,Y+O(10^{-16})}.
\]

The nested Thiemann stack contains five Poisson brackets, giving the universal phase

\[
(1/i)^5=-i.
\]

However, exact fixed-environment MITM blocks contain real `X/Z` components in addition to imaginary pseudoscalar components. Therefore the unsymmetrized full `L_raw` is **not globally anti-Hermitian**.

The physical Lorentzian structural block is consequently defined by the minimal Hermitian completion

\[
\boxed{
S_v=-\frac{i}{2}\left(L_{raw,v}-L_{raw,v}^\dagger\right)
}
\]

with

\[
S_v^\dagger=S_v.
\]

If a sector already satisfies `L_raw^dagger=-L_raw`, then `S=-iL_raw`; hence every accepted pure-`iY` one-body result is preserved exactly.

The upstream Euclidean/Thiemann normalization fixes the relative coefficient. At `beta=hbar=1`, the **production geometry operator** is

\[
\boxed{
G_v=-\frac23E_v-\frac{32}{9}S_v
}
\]

or equivalently

\[
\boxed{
G_v=-\frac23E_v+\frac{16i}{9}(L_{raw,v}-L_{raw,v}^\dagger).
}
\]

The historical shorthand `(-2/3)E+(32i/9)L_raw` is retained only as the exact reduction on already anti-Hermitian raw sectors. It is not the full production definition.

For the environment-unbiased one-body block the signed correction remains

\[
\boxed{-4.760637696520545\,Y}
\]

in repository structural units.

---

## 6. Finite Lorentzian multi-node structure

Before environment tracing, the exact diagonal logical Walsh reconstruction with nodes `3,4` fixed at `K=0` contains surviving pseudoscalar correlations

```text
Y I I    = +i 0.3359014033398999
Y Z1 I   = -i 0.00702861722247964
Y I Z2   = +i 0.002338130606598994
Y Z1 Z2  = +i 0.004676261213197787
```

before the Hermitian phase completion. The Hermitian projection removes the real unsymmetrized `X/Z` pieces and preserves these imaginary pseudoscalar components.

This proves a finite neighbor-dependent diagonal correlation hierarchy. It does not yet specify the complete multi-qubit Lorentzian Hamiltonian because off-diagonal environment transitions were not contained in the historical trace workers.

---

## 7. Exact doubled-spin grading

Define

\[
\Pi=(-1)^{\sum_e 2j_e}.
\]

For the declared Peter-Weyl operators,

```text
E        : odd
V        : even
K=[V,E]  : odd
C(V)     : even
C(K)     : odd
L_raw    : even
S        : even
R_op     : spin-preserving / even
D target : spin-preserving / even.
```

Thus on the even all-`j=1/2` seed the full HDA channels split into orthogonal parity sectors:

```text
even: EE, SS, S×R, route residual / D target
odd : ES, SE, E×R.
```

Because `Pi` is Hermitian, even and odd outputs are orthogonal. Therefore an odd mixed anomaly cannot be hidden by destructive interference with the even diffeomorphism target or the even `EE/SS` channels.

---

## 8. Operator-first route normal

Expectation-first square-root maps are nonlinear on superpositions and are not the production quantum constraint.

The route symbol is

\[
A=\hat Q^{ab}\hat P_a\hat P_b=\sum_iB_i^\dagger B_i\ge0,
\]

so its unique positive spectral square root defines

\[
\boxed{
R_{op}[N]=\frac12\{N,A^{1/2}\}.
}
\]

The matrix Sylvester identity gives the required operator-valued HDA principal structure function.

The exhaustive finite implementation audit now covers the complete one-step `H_E^sine` support of the frozen seed:

```text
H_E basis outputs                     41
distinct fixed-spin route sectors     33
nonzero power-law sectors             30
numerical-zero sectors                 3
p range                  0.999794406814 .. 0.999983093445
max endpoint defect       1.405841033798129e-05
minimum symbol eigenvalue -1.0658141036401503e-14  (roundoff zero)
```

Thus no one-step Euclidean-reached fixed-spin route sector is omitted from this finite regression.

---

## 9. Full Hamiltonian and cutoff-saturated HDA theorem

The production pure-gravity constraint is

\[
\boxed{H[N]=G[N]+R_{op}[N]}
\]

with the Hermitian `G` above.

For

\[
N=\bar N+\epsilon n,\qquad M=\bar M+\epsilon m,
\]

the antisymmetric two-node geometry smear is exactly

\[
N_0M_1-N_1M_0=O(\epsilon),
\]

with no zeroth-order term.

For a geometry change in the route operator, the apparent `1/epsilon` piece of

\[
N_v\Delta R_M-M_v\Delta R_N
\]

cancels algebraically before any matrix element is taken. Since the WKB diffeomorphism target is `O(epsilon^-1)`, any bounded local geometry gives

\[
\frac{C_{G\times R}}{D}=O(\epsilon),\qquad
\frac{C_{GG}}{D}=O(\epsilon^2).
\]

The remaining question is whether the cutoff itself introduces an epsilon-dependent remainder. On the frozen all-`j=1/2` finite-depth two-node habitat the exact hit-depth bound gives

```text
max HE hits per physical link = 2
max one-L hits per link        = 6
max full HH hits per link      = 12
```

and therefore

\[
\boxed{J_{max}^{safe}=\frac12+\frac{12}{2}=\frac{13}{2}.}
\]

`S` uses `L` and `L^dagger` with the same support wall, while `R_op` does not change link irreducible representations. Consequently, for this frozen finite-depth habitat,

\[
\boxed{
J_{max}\ge13/2\quad\Longrightarrow\quad
\text{spin-cutoff remainder}=0.
}
\]

Combining this exact saturation with the exhaustive route regression gives

\[
\boxed{
\Delta_{full}=O(\epsilon^{\min(p,1)})\to0,
\qquad p\simeq1,
}
\]

on the preregistered two-node WKB habitat.

This is the strongest v1.2 closure statement. The older conditional trajectory `Jmax~epsilon^-1/8` is **not required for this fixed seed and finite operator depth**. It remains an extension certificate for families in which initial spins, collective blocking scale, or operator depth grow with refinement.

---

## 10. Hermitian channel-resolved finite falsifier

For

\[
G=aE+cS,\qquad a=-2/3,\quad c=-32/9,
\]

the physical geometry commutator is frozen as

\[
\boxed{
[G_0,G_1]
=\frac49EE
+\frac{64}{27}(ES+SE)
+\frac{1024}{81}SS.
}
\]

with sufficient walls

```text
EE : 5/2
ES : 9/2
SE : 9/2
SS : 13/2.
```

A completed `ES/SE/SS` calculation is still a high-value finite falsifier for implementation errors, large finite coefficients, scalar-projection problems, or a habitat-specific obstruction. It is **not** a logical prerequisite for the asymptotic composition theorem above.

The preregistered acceptance bands remain frozen; no sign fit, coefficient fit, channel deletion, subtraction, or threshold widening is permitted after observing results.

---

## 11. Infrared GR universality — conditional

If the continuum limit has a nondegenerate local three-metric and the standard first-class HDA, the classical HDA identity fixes the inverse-DeWitt trace coefficient

\[
\boxed{c_{DW}=1/2}.
\]

The corresponding GR first-class rank gives

\[
3_G+3_D+1_H,
\]

leaving two local gravitational configuration degrees of freedom. In a local two-derivative metric phase these become the two helicities of a massless spin-2 tensor field, and the HDA normalization fixes the relativistic tensor cone (`z=1`).

This IR conclusion is conditional. An anomaly-free flow into a BF/topological rank structure would still be a FAIL. Independent continuum checks must therefore include first-class rank/reducibility, not only a spectral-dimension plateau.

---

## 12. What is closed and what remains open

### Closed on the frozen core habitat

- canonical q=2 binary route rule and chosen PL-S3 globalization;
- physical sine Euclidean ordering and finite two-node HDA regression;
- mandatory Hermitian Lorentzian completion and upstream relative normalization;
- exact doubled-spin parity bookkeeping;
- strict `Jmax=13/2` support saturation for the finite-depth all-`j=1/2` HH test;
- positive linear operator-first route definition;
- exhaustive route regression over all 33 one-step Euclidean-reached sectors;
- algebraic cancellation of the dangerous mixed inverse-epsilon term;
- fixed-habitat full-HDA asymptotic composition.

### Still open / deliberately not overclaimed

- uniqueness of the microscopic Hermitian factor ordering beyond the minimal completion;
- exhaustive finite route regression over every `S`-reached sector;
- full off-diagonal multi-node Lorentzian logical matrix;
- direct channel-resolved `ES/SE/SS` finite calibration;
- independent habitats and collective states;
- a uniform refinement theorem when initial spin/operator depth grows;
- dynamical demonstration of the GR first-class rank in the collective IR;
- matter coupling, Newton normalization and physical scale setting;
- experimental validation.

Mirror-force, infoton, foam-spectrum and GW-resonance constructions are extensions and are not evidence for the gravity core.

---

## Canonical statement

> **BCQG Candidate Theory v1.2 is a Hermitian, operator-first, cutoff-saturated candidate gravity architecture on its preregistered all-j=1/2 finite-depth two-node habitat. The spin cutoff is exactly removed above Jmax=13/2, the route sector is exhaustively finite-regressed on all one-step Euclidean-reached fixed-spin sectors, and the full HDA residual converges by exact lapse identities plus bounded Hermitian geometry. The extension from this controlled habitat to a uniform collective continuum and then to experimentally realized GR remains conditional and falsifiable.**
