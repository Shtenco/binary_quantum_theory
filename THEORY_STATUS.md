# Theory status — BCQG Candidate Theory v1.2 + v1.3 operator-correction frontier

**Frozen working frontier: 2026-08-16.**

BCQG v1.2 is a computable candidate quantum-gravity architecture. It is not experimentally established and does not by itself establish a fifth force, antigravity, a new particle, or an absolute physical scale.

A 2026-08-16 collective audit found one specific finite-operator defect in the historical Lorentzian implementation: a fixed local `q_123` is a valid representation of the four-valent absolute volume on the Gauss `J=0` sector, but is not a tetrahedrally covariant continuation to charged intermediate sectors created inside Thiemann words. The correction is frozen **before any complete PL-S3 Lorentzian science result** and is tracked as the v1.3 operator-correction frontier.

Canonical entry points:

```text
START_HERE.md
BCQG_CANDIDATE_THEORY_V1_2.md
BCQG_CORE_CANDIDATE_V1_2.md
THEORY_STATUS.md
theory_gates.json
PL_16CELL_HERMITIAN_LORENTZIAN_PREREGISTRATION_V2.md
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

## 2. Euclidean geometry — tested finite PASS and stable under the charged-volume correction

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

The new tetrahedral charged-volume audit replaces the intermediate fixed `q_123` extension by

\[
Q_{tet}=\frac14\sum_{r=0}^3(-1)^r q_{\widehat r},
\qquad V_{tet}=\sqrt{|Q_{tet}|},
\]

with the same zero-aware spectral convention. This change leaves the gauge-invariant Euclidean columns unchanged to machine precision:

```text
K5 H_E:      support 37 -> 37, relative error 0
16-cell H_E: support 82 -> 82, relative error ~1.8e-16
K5 Gauss K:  support 37 -> 37, relative error ~1.2e-15
16-cell K:   support 82 -> 82, relative error ~1.5e-15
```

Thus the Euclidean normalization and all E-based route/refinement evidence remain valid.

## 3. Lorentzian sector — Hermitian form retained; finite raw amplitudes under tetrahedral re-audit

The structural definition remains

\[
L_{raw}\sim\mathrm{Tr}[C(K)C(K)C(V)],
\qquad
\boxed{S=-\frac{i}{2}(L_{raw}-L_{raw}^\dagger)},
\]

and at `beta=hbar=1`

\[
\boxed{G=-\frac23E-\frac{32}{9}S}.
\]

The Hermitian projection `S=Herm(-iL_raw)` remains the unique real-linear projection onto the Hermitian subspace with anti-Hermitian kernel and the Hilbert-Schmidt nearest Hermitian operator after the raw stack is fixed.

However, the **historical finite raw-L amplitudes were computed with the preferred-leg charged `q_123` continuation**. The independent charged-volume audit found:

```text
old C_r(V) Frobenius norms on 16-cell seed:
0.6453707252, 0.6453707252, 0.5163939349, 0

new tetrahedral C_r(V_tet) norms:
0.2513477706186925,
0.2513477706186926,
0.2513477706186924,
0.2513477706186924
```

The corrected slot spread is ~`2.2e-16`; complete-basis leakage is ~`4.4e-16`.

Therefore these old finite numbers are now **HISTORICAL / REQUIRES_TETRAHEDRAL_REAUDIT**, not current predictions:

```text
L_raw,1body = i 1.3389293521464034 Y
full one-body correction = -4.760637696520545 Y
diagonal-environment Walsh coefficients from the old charged extension
```

They remain valuable regression targets: the corrected calculation may reproduce them or may predict different finite coefficients. No sign, normalization, cutoff or acceptance threshold may be changed after the corrected result is seen.

## 4. Why the charged-volume correction is forced rather than fitted

On Gauss `J=0` sectors the normalized four-leg operator preserves the old absolute volume with relative error at machine precision. On charged sectors it is not proportional to the fixed `q_123` continuation. Examples at total `J=1/2`:

```text
spins (0,1,1,1): ||q123||=0, ||Q_tet||=0.6123724357
spins (2,1,1,1): best scalar=-2.5, residual=0.5773502692
```

This is a local tetrahedral covariance falsifier. It does not use `D=3`, `c_DeWitt=1/2`, GR constraint ranks, TT counting, HDA residuals, or experimental data.

All Lorentzian jobs launched before this correction are `SUPERSEDED_PRE_RESULT` diagnostics. The corrected 24-forward + 24-adjoint calculation is preregistered in `PL_16CELL_HERMITIAN_LORENTZIAN_PREREGISTRATION_V2.md`.

## 5. Route normal — exhaustive microscopic and collective-E tested finite PASS

Production route operator:

\[
R_{op}[N]=\frac12\{N,\sqrt{\hat Q^{ab}\hat P_a\hat P_b}\},
\qquad \hat Q^{ab}\hat P_a\hat P_b=\sum_iB_i^\dagger B_i\ge0.
\]

Microscopic exhaustive one-step `H_E^sine` result:

```text
H_E basis support                 41
distinct fixed-spin sectors       33
nonzero power-law sectors         30
numerical-zero sectors             3
p_min=0.9997944068141106
p_max=0.9999830934452917
max endpoint=1.405841033798129e-05
```

The independent 16-cell collective-E precursor additionally gives:

```text
E0 support                         82
distinct local spin sectors        26
intertwiner carriers               54
numerical-zero carriers             3
p_min=0.99979440681411
p_max=0.9999830934452917
max endpoint=1.405841033797955e-05
minimum symbol eigenvalue=-1.39e-15
```

Thus operator-first route closure survives all fixed-spin sectors actually generated by the first exact collective Euclidean column, modulo roundoff PSD tolerance.

## 6. Spin-parity structure — regulator scoped

The historical theorem for

\[
\Pi=(-1)^{\sum_e2j_e}
\]

was proved on the K5/triangular-plaquette regulator. There `E` flips parity, `S` is even and the previously stated even/odd channel orthogonality is valid on that declared microscopic habitat.

It is **not universal under refinement**. The exact PL transfer rule is

\[
\Pi_{out}/\Pi_{in}=(-1)^q,
\]

where `q` is the dual-plaquette length / primal-edge valence. The canonical 16-cell and its barycentric refinements have even checked valences, so the collective `E` **preserves** doubled-spin parity. Consequently collective `ES/SE` channels may not be deleted using the old K5 parity argument.

## 7. Spin-cutoff saturation — proved for the frozen microscopic finite-depth habitat

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

The charged-volume correction changes amplitudes on intermediate charged sectors but not the number of fundamental holonomy hits, so this strict representation wall is unchanged for the same operator word.

## 8. Full operator-first HDA — composition theorem remains structurally valid on its declared habitat

For smooth lapse probes `N=Nbar+epsilon*n`, `M=Mbar+epsilon*m`, the pure geometry antisymmetric smear has no zeroth-order term and the dangerous mixed route inverse-epsilon piece cancels before matrix elements.

With `D=O(epsilon^-1)`:

\[
C_{G\times R}/D=O(\epsilon),\qquad C_{GG}/D=O(\epsilon^2).
\]

The proof requires a bounded finite-cutoff Hermitian local `G`; it does not require the historical numerical value of the old charged-`q_123` Lorentzian one-body coefficient. Therefore the composition theorem remains an architecture theorem. The **finite corrected `ES/SE/SS` amplitudes and coefficients must nevertheless be re-audited** before any new precision Lorentzian prediction is promoted.

## 9. Collective/refinement frontier — direct progress

The collective GR killer remains an AND-gate requiring direct measurements of

\[
D_{space}\to3,\quad c_{DeWitt}\to1/2,\quad
(r_G,r_D,r_H,r_{extra})\to(3,3,1,0),\quad N_{phys}\to2,
\quad\Delta_{HH}^{collective}\to0.
\]

It remains `INCOMPLETE`; target controls are never substituted for missing BCQG data.

Direct new collective anchors include:

```text
static maximal-symmetric j=3 barycentric block image rank = 1
one-E coarse-face support = j=0,1/2,...,4
one-S conservative face wall = j<=6
HDA depth-2 conservative face wall = j<=9
exact span{E_v|Omega0>, v=0..15} rank = 16
E sparse union support = 552
seed + E preliminary Krylov dimension = 17
Gram condition number = 1.5536226967
```

The exact XOR translation subgroup is node-transitive:

\[
E_m|\Omega\rangle=(-1)^{popcount(m)}U_mE_0|\Omega\rangle
\]

with max direct amplitude error `4.33e-9` and exact support equality across all 16 masks. The same character is a preregistered prediction for corrected `S`, but production use requires one direct held-out `S_m` validation.

The collective lapse family is frozen as the four `l=1` radial S3 harmonics `N_mu=x_mu`, with primary pair `(0,1)` and five held-out pairs. The intrinsic refinement variable is frozen as `epsilon=h/R`, not as an arbitrary power of the level index.

## 10. Remaining physical falsifiers

Priority order now:

1. corrected tetrahedral charged-volume audit in independent CI;
2. corrected 24+24 PL-S3 Lorentzian node-0 column and Hermitian `S_0`;
3. direct held-out XOR-translated `S_m` node check;
4. extend sparse Krylov `W_E` to `W_{E+S+R}` and then depth-2 images with leakage;
5. direct collective metric dimension from the dynamical block states;
6. raw six-by-six kinetic Hessian -> `c_DeWitt_eff` without target fitting;
7. direct Gauss/diffeomorphism/Hamiltonian rank/reducibility;
8. collective `[H,H]` on the frozen S3 harmonic lapse family across >=4 measured refinement levels;
9. matter coupling, Newton normalization and physical scale;
10. experiment.

Mirror/infoton/foam/GW-resonance branches remain extensions and are not used to certify the gravity core.

## Canonical status statement

> **The BCQG microscopic Euclidean/operator-first HDA architecture remains intact under the 2026-08-16 audit, and the first collective Euclidean Krylov layer is now an exact rank-16 amplitude object. A hidden preferred-leg continuation of the volume on charged intermediate states was falsified before the first complete collective Lorentzian result. The finite Lorentzian sector is therefore being rerun with a target-independent tetrahedrally covariant four-leg volume. Old finite Lorentzian coefficients are historical regression data until that rerun completes. The collective GR universality verdict remains INCOMPLETE by construction.**
