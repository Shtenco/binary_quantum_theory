# Binary Quantum Gravity — Теория бинарной квантовой гравитации

## От одного различия к геометрии, ограничениям, физической истории и проверяемому гравитону

> **Канонический научный обзор: 29 августа 2026.**  
> **Статус: candidate mathematical/computational theory; experimental confirmation не заявлена.**

Этот репозиторий исследует очень жёсткий вопрос:

> **можно ли начать не с готового пространства-времени, а с минимальных бинарных различий и вывести из их отношений трёхмерную пространственную геометрию, квантовую геометрию, GR/HDA структуру и в конце — физически проверяемый spin-2 propagator?**

Главная дисциплина проекта: **ни одно красивое число не становится законом природы только потому, что оно получилось в конечной матрице.** Между microscopic object и experimental observable должен существовать явный, воспроизводимый мост.

---

# Паспорт теории на 29 августа 2026

```text
STRUCTURAL BINARY -> GEOMETRY CHAIN        : CLOSED in declared scopes
q=2 DIMENSION-THREE FIXED POINT            : EXACT
SELECTED GLOBAL PL 3-MANIFOLD              : EXACT/FINITE existence + stability
QUANTUM GEOMETRY CARRIER                    : EXACT local representation
GR / ADM / HDA STRUCTURAL CONTROLS          : EXACT + FINITE in declared habitats
REGGE L=6 HELD-OUT                          : PASS
EPRL FINITE-WINDOW POWER-LAW HOLDOUT        : FAIL (correctly retained as failure)
PETER-WEYL HIGHER-SHELL                     : FINITE EXACT constraint data
GENERAL PARITY-EVEN S4 QUARTIC TT SPACE     : EXACTLY 6-dimensional
SIX-OBSERVABLE WILSON EXTRACTOR             : EXACT full rank
PHYSICAL GRAVITY PROJECTOR / HISTORY        : OPEN
FIRST INTERACTING PHYSICAL SIX-WILSON VECTOR: NOT FROZEN
COMMON ABSOLUTE PHYSICAL SCALE              : OPEN / one global normalization
DYNAMICAL MAXWELL STIFFNESS                 : OPEN
STANDARD-MODEL MATTER / MASSES              : NOT DERIVED
EXPERIMENTAL CONFIRMATION                    : NO
```

Полный branch/PR/CI audit находится в [`REPOSITORY_AUDIT_2026-08-29.md`](REPOSITORY_AUDIT_2026-08-29.md).

---

# Как читать эту книгу

У каждого результата есть тип.

| Статус | Смысл |
|---|---|
| **EXACT** | точное алгебраическое, комбинаторное или representation-theory утверждение в заявленных предпосылках |
| **FINITE PASS** | воспроизводимый конечный расчёт прошёл заранее определённые проверки |
| **HELD-OUT PASS** | правило/fit было frozen до открытия контрольного результата и выдержало его |
| **HELD-OUT FAIL** | frozen hypothesis не выдержала контроль; failure сохраняется, а не переписывается |
| **CONDITIONAL** | theorem/result зависит от явно заявленного дополнительного условия |
| **OPEN PHYSICAL** | математический словарь уже определён, но физическая dynamical arrow ещё не вычислена |
| **NO-GO** | короткий путь доказанно не работает |
| **COMPUTATIONAL NO-RESULT** | heavy run не завершился; это не zero и не nonzero physics |
| **EXPERIMENT** | внешний тест природы после freezing theory output |

---

# Главная карта путешествия

```text
минимальное различие
        ↓
binary route family
        ↓
q + 2 = 2^q
        ↓
q = 2
        ↓
четыре route labels = Z2^2
        ↓
C4 Hamming adjacency
        ↓
octahedral local S2
        ↓
Walsh characters -> regular tetrahedral normals
        ↓
face qubits -> SU(2) Gauss singlet
        ↓
logical geometry qubit
        ↓
shape X,Z + orientation Y
        ↓
face gluing -> selected global PL S3
        ↓
exact causal-volume fixed point d*=3
        ↓
z ~ 1 and 3+1-like history scaling
        ↓
observer coarse graining -> smooth effective geometry
        ↓
Peter-Weyl quantum geometry / constraint dynamics
        ↓
Plebanski / Urbantke / Regge cross-checks
        ↓
DeWitt / ADM / HDA structure
        ↓
TT spin-2 sector
        ↓
complete six-dimensional quartic pole dictionary
        ↓
PHYSICAL PROJECTOR / RELATIONAL HISTORY   ← current main physical bottleneck
        ↓
Z[J] -> W[J] -> Gamma[g] -> Gamma^(2)
        ↓
physical K_TT(omega,k)
        ↓
(c1,...,c6)_IR
        ↓
one common physical scale
        ↓
velocity / phase / birefringence observables
        ↓
blind experiment
```

Теперь пройдём эту дорогу медленно.

---

# ЧАСТЬ I. До пространства ещё нет пространства

## Глава 1. Бит — не маленький кубик

Если начать с трёхмерной lattice, мы уже тайно вставили три направления. Если начать с длины ребра, мы уже вставили метр. Поэтому microscopic bit здесь означает только **различимость двух альтернатив**:

```text
0 / 1
```

или quantum carrier

```text
|psi> = alpha|0> + beta|1>,
|alpha|^2 + |beta|^2 = 1.
```

Сам qubit ещё не знает ни расстояния, ни угла, ни координаты.

**Статус:** starting ansatz, а не экспериментально найденный voxel пространства.

## Глава 2. Геометрия должна быть отношением

Microscopic rule содержит не готовую систему координат, а:

```text
binary labels
causal endpoints
allowed adjacency
recursive rewrite.
```

Геометрия считается emergent только если длины, площади, объёмы и metric observables появляются позже из этих relations.

## Глава 3. Сколько бинарных различий живёт в локальном causal cell?

Пусть независимых binary choices `q`. Тогда route states:

```text
2^q.
```

Каждый route имеет `q` Hamming-neighbours и два causal endpoints, то есть degree `q+2`. Каждый endpoint видит все `2^q` routes.

Локальная valence homogeneity требует:

```text
q + 2 = 2^q.
```

Для integer `q>=1` единственный ответ:

```text
q=2.
```

**EXACT внутри declared route family.**

---

# ЧАСТЬ II. Четыре binary labels находят локальную геометрию

## Глава 4. q=2 даёт четыре состояния

```text
00, 01, 10, 11.
```

Hamming distance one создаёт cycle `C4`.

## Глава 5. C4 плюс два causal endpoints даёт S2

Suspension cycle образует octahedral shell:

```text
V=6, E=12, F=8,
chi=6-12+8=2.
```

Это simplicial `S2` — именно topology type link внутренней вершины combinatorial three-manifold.

**EXACT local topology.**

## Глава 6. Те же четыре labels являются Z2^2

Это важно, потому что у `Z2^2` есть три nontrivial real Walsh characters. Для каждого label `g` строится vector:

```text
Phi(g)=(chi_01(g), chi_10(g), chi_11(g))/sqrt(3).
```

Character orthogonality даёт:

```text
sum_g Phi(g)=0
|Phi(g)|=1
Phi(g).Phi(h)=-1/3  for g != h.
```

Это exact Gram matrix четырёх unit normals правильного тетраэдра.

## Глава 7. Почему этот тетраэдр не был вставлен руками

Три координаты frame появились не из заранее выбранных x,y,z, а из трёх nontrivial characters самой binary group. Для общего `q` characters дают regular simplex в `R^(2^q-1)`; именно q=2 имеет character space dimension 3.

Это одна из центральных geometrogenesis стрелок:

```text
binary labels -> character algebra -> tetrahedral flux frame.
```

---

# ЧАСТЬ III. Из tetrahedral normals в quantum geometry

## Глава 8. Face qubit

Для derived unit normal `n_f` вводится pure qubit density matrix:

```text
rho_f = (I + n_f.sigma)/2.
```

Continuous direction здесь не fit: Bloch vector frozen Walsh construction.

## Глава 9. Gauss closure

Четыре spin-1/2 faces:

```text
(1/2)^(tensor 4)
```

содержат два независимых total-j=0 states. Следовательно gauge-invariant four-valent node имеет exact two-dimensional singlet carrier:

```text
4 face qubits -> 1 logical geometry qubit.
```

## Глава 10. Почему logical qubit — реально геометрический

В natural singlet basis pairwise flux contractions становятся linear combinations `I, X_L, Z_L`, а oriented triple product — `Y_L`.

Два Bloch coordinates описывают intrinsic shape; третий отвечает за orientation pseudoscalar.

## Глава 11. Exact oriented-volume witness

На четырёх faces определим:

```text
Q_or = epsilon_abc J1^a J2^b J3^c.
```

На logical singlet sector latest exact branch gate даёт:

```text
Q_or = (sqrt(3)/4) Y_L.
```

`Q_or` commutes with total SU(2) и меняет знак при odd face permutation.

Это превращает abstract Pauli `Y_L` в microscopic gauge-scalar oriented-flux observable.

**EXACT branch result; CI run 33156152205 SUCCESS.**

## Глава 12. Важный no-go: orientation не является linear intrinsic metric direction

Exact local reconstruction зависит от `X,Z`, но не от `Y` на linear intrinsic level:

```text
partial g / partial Y = 0.
```

Full logical source Jacobian `(X,Y,Z)` имеет rank 2.

Это не означает, что orientation не физична. Это означает только, что искать её надо в oriented frame/triad, connection, extrinsic curvature, parity-sensitive history или nonlinear response — не притворяться, что она третий linear metric mode.

---

# ЧАСТЬ IV. Как из fluxes получить настоящий tetrahedron

## Глава 13. Closure и Minkowski reconstruction

Closed area vectors могут reconstruct convex polyhedron. Для tetrahedral case project содержит exact finite reconstruction from oriented face vectors.

## Глава 14. Geometry qubit не равен произвольной двухуровневой системе

Logical `X,Z` имеют конкретный geometric dictionary через face contractions; `Y` имеет oriented-volume dictionary. Поэтому qubit здесь не только data storage label.

## Глава 15. Shape matching важнее area matching

Two neighboring quantum polyhedra могут иметь одинаковую shared area и normal, но разные triangle shapes. Такой twisted configuration не является одной Regge geometry.

Repository содержит negative control, где area mismatch zero, а normalized shape defect nonzero.

Следовательно continuum window требует:

```text
closure defect -> 0
shape mismatch -> 0.
```

## Глава 16. Neighbor gluing

На selected PL completion shared-face labels совпадают, neighbor orientations согласованы, outward fluxes cancel pairwise. Это exact kinematic gluing certificate выбранной completion.

---

# ЧАСТЬ V. Глобальный spatial world

## Глава 17. Local S2 ещё не global S3

Local link tells us what neighborhood type is allowed; он не определяет global topology uniquely.

## Глава 18. Selected economical completion: 16-cell boundary

Canonical PL complex:

```text
(V,E,F,T)=(8,24,32,16)
Betti=(1,0,0,1).
```

Vertex links are octahedral `S2`, edge links `S1`, face links `S0`, every triangle belongs to two tetrahedra, orientation equations are consistent.

## Глава 19. Dual graph

Sixteen tetrahedral cells form dual graph `Q4`. Neighboring cells differ by one sign bit, что естественно связывает global cell adjacency с binary structure.

## Глава 20. Recursive PL stability

Checked barycentric refinements:

```text
16 -> 384 -> 9216 tetrahedra.
```

No bad vertex/edge/face links в tested levels, `boundary^2=0`, two-sided codimension-one faces preserved.

**EXACT/FINITE existence and tested stability.**

## Глава 21. Что не доказано

Bare causal graph сам по себе пока не доказанно uniquely forces именно этот global gluing. Поэтому правильная формулировка — selected canonical completion with stability, а не uniqueness theorem for every admissible global graph.

---

# ЧАСТЬ VI. Почему spatial dimension стремится именно к трём

## Глава 22. Dimension нельзя читать только из картинки

Топология и volume-growth должны быть независимыми свидетелями.

## Глава 23. Exact active-edge growth

Для q=2 число route midpoints per active edge `B=4`. Один rewrite создаёт `2B=8` active child edges, а causal depth scale doubles.

## Глава 24. Exact vertex count

```text
N_g = (4*8^g + 10)/7.
```

Никакого continuum fit в этой identity нет.

## Глава 25. Finite-step dimension

```text
d_g = log2(N_g/N_(g-1))
    = 3 + log2(1 - 35/(16*8^(g-1)+40)).
```

Exact consequences:

```text
d_g < 3
d_(g+1) > d_g
lim d_g = 3.
```

## Глава 26. Dimension ladder

```text
g=2  2.662965012722429
g=3  2.951744831392779
g=4  2.993853015664851
g=5  2.999229782139151
g=6  2.999903693848493
g=7  2.999987961279020
g=8  2.999998495152814
```

Historical `d_H=2.999229782...` — это просто g=5 point exact sequence, а не случайное почти-3 число.

## Глава 27. General q fixed point

Для frozen route rule:

```text
d* = q + 1.
```

Независимый selector дал q=2, поэтому fixed point становится 3 без выбора 3D lattice.

---

# ЧАСТЬ VII. Где появляется history/time scaling

## Глава 28. Spatial slice — это ещё не spacetime

Нужен causal rewrite direction и dynamical exponent.

## Глава 29. Frozen finite z

Project diagnostic:

```text
z ≈ 0.998281156.
```

Это близость к unit dynamical scaling, не самостоятельное доказательство exact Lorentz invariance.

## Глава 30. Correct notation

```text
d_eff_slice = d_H / z ≈ 3.004393867

d_eff_history = 1 + d_H/z ≈ 4.004393867.
```

Число `3.004393867` уже включает division by `z`; делить его на `z` снова нельзя.

## Глава 31. Three independent witnesses

```text
local topology: S2 link
selected global topology: S3-like PL complex
causal-volume fixed point: 3
finite dynamical scaling: z ~ 1.
```

Согласие разных observables сильнее повторного измерения одного и того же exponent.

---

# ЧАСТЬ VIII. Почему discrete microgeometry может выглядеть smooth

## Глава 32. Аналогия со стеной

Стена не становится физически гладкой, когда наблюдатель отходит. Микрорельеф просто оказывается внутри одного unresolved pixel.

Так и здесь observer distance/resolution не переписывает microscopic state.

## Глава 33. Observer resolution scale

Model map:

```text
ell_obs(r)=sqrt(ell_*^2 + (theta r)^2).
```

`ell_*` — microscopic cutoff candidate; он не объявляется Planck length без scale bridge.

## Глава 34. Why b^-2 is natural

Если one coarse history block содержит примерно `N(b)~b^4` weakly correlated contributions, central self-averaging gives:

```text
delta g_RMS ~ N^-1/2 ~ b^-2.
```

## Глава 35. Measured smoothing

Frozen q=2 control:

```text
delta g       ~ b^-2.001707
grad delta g  ~ b^-3.001458
delta R_proxy ~ b^-4.000524.
```

## Глава 36. Scope

Это finite candidate-geometrogenesis control. Long-range correlations или другие microscopic ensembles могут менять exponents; universality требует отдельного theorem/test.

---

# ЧАСТЬ IX. От q=2 graph change к Peter-Weyl quantum geometry

## Глава 37. Four active states недостаточно

Exact representation audit показал: четыре active q=2 states сами по себе не являются endpoint `(2,2)` Peter-Weyl bi-doublet.

Это полезный obstruction, а не проблема, которую надо скрывать.

## Глава 38. No-link state

Graph-changing cylindrical Hilbert уже содержит absent/j=0 link state. Поэтому carrier:

```text
4 active + 1 no-link.
```

Exact SO(5) vector decomposition:

```text
(2,2) + (1,1).
```

## Глава 39. Matrix-unit factorization

Transporter identity:

```text
P_g U_a P_0 U_b P_g = |a><b|.
```

Frozen q=2 Hamming adjacency factorizes through graph-changing two-step excursions:

```text
active -> no-link -> active.
```

## Глава 40. Higher-j representation growth

Under explicitly declared fully symmetric endpoint blocking:

```text
Sym^n(C2)_L x Sym^n(C2)_R -> (j=n/2,j=n/2)
```

with dimension `(n+1)^2`.

This reproduces the diagonal Peter-Weyl tower through chosen cutoff.

**CONDITIONAL:** microscopic dynamics selecting exactly this symmetric blocking/occupancy weighting is not yet uniquely derived.

## Глава 41. j=1 coarse carrier

Four j=1 face spins contain a multiplicity-one `[2,2]` S4 doublet that gives an exact coarse representation carrier for RG consistency tests.

---

# ЧАСТЬ X. Shape становится metric

## Глава 42. Exact local intrinsic metric map

At regular point background Gram can be represented as:

```text
g0 = [[2,1,1],
      [1,2,1],
      [1,1,2]].
```

Logical `X,Z` derivatives give two tracefree independent metric tangents.

## Глава 43. Rank-two theorem

Jacobian rank exactly 2; `X,Z` tangents orthogonal and equal norm in declared DeWitt normalization.

Orientation branches share same intrinsic metric Jacobian.

## Глава 44. Почему это важно для TT

Spin-2 traceless metric space under tetrahedral symmetry decomposes as:

```text
5 = E(2) + T2(3).
```

Logical shape doublet supplies a concrete microscopic tangent into this metric sector.

---

# ЧАСТЬ XI. B-field, simplicity и Urbantke route

## Глава 45. Face geometry -> two-form data

Repository содержит independent route from face/flux data to B-field-like variables.

## Глава 46. Simplicity

Not every B-field is metric gravity. Simplicity constraints select gravitational sector from generic BF-like data.

## Глава 47. Urbantke reconstruction

Finite controls reconstruct metric from declared self-dual/two-form data and separate Einstein positive control from non-Einstein negative control.

## Глава 48. Compatible connection and curvature

Separate gate checks compatible connection/curvature chain. A unit-S4 curvature number near 3 is an oracle reconstruction control, **не observed cosmological constant**.

---

# ЧАСТЬ XII. Regge route — независимый continuum witness

## Глава 49. Почему нужен второй путь

Если только один formalism выдаёт Einstein-like answer, можно подозревать circular construction. Поэтому repository имеет independent Regge/Einstein-Hilbert lattice route.

## Глава 50. Directional Hessians

Finite lattice Hessians test axial and diagonal directions, gauge leakage scaling and Fierz-Pauli tensor ratios.

Current main `directional-regge` job on run `33182064154` completed **SUCCESS**.

## Глава 51. Intensive TT residue

Sequence:

```text
L=3  0.1021131745
L=4  0.1114624530
L=5  0.1161306996
L=6  0.1187607546
limit target 1/8 = 0.125.
```

## Глава 52. Held-out L=6

Rule was frozen on L=3,4,5:

```text
Z_L = 1/8 + C/L^2 + D/L^4.
```

Prediction:

```text
Z6_pred = 0.11876923193907167.
```

Observed later:

```text
Z6_obs = 0.11876075461190198.
```

Relative error:

```text
0.00714%.
```

Preregistered PASS threshold was 1%.

**HELD-OUT PASS.**

---

# ЧАСТЬ XIII. Почему теория обязана сохранять и плохие новости

## Глава 53. EPRL coherent-fusion auxiliary route

Repository имеет independent coherent-simplicity/fusion calculation. Это auxiliary control, не обязательная central arrow.

## Глава 54. Frozen finite-window power-law prediction

For `j=15/2` preregistered forecast:

```text
epsilon_pred = 0.00026207793589462915.
```

Exact result:

```text
epsilon_obs = 0.000125031726024738.
```

Relative prediction error about 52.3%.

Frozen rule said FAIL above 40%.

**HELD-OUT FAIL.**

## Глава 55. Что именно failed

Failed hypothesis: single finite-window power-law extrapolation from smaller j.

Не failed: coherent geometric-ray preservation. Raw fusion coherent fidelity remains:

```text
0.9999999999999996.
```

Correct science response — не fit нового exponent на пяти точках, а отказаться от failed extrapolation target и проверять более physical observables.

---

# ЧАСТЬ XIV. ADM, DeWitt и HDA

## Глава 56. Constraint algebra важнее похожести action

GR — не просто tensor kinetic term. Hamiltonian and diffeomorphism constraints должны compose правильно.

## Глава 57. DeWitt structure

Within declared local two-derivative canonical ansatz repository derives/identifies required DeWitt signature/relative trace structure for GR-like first-class closure.

Overall Newton normalization при этом не фиксируется.

## Глава 58. Hypersurface deformation algebra

Continuum target schematically:

```text
[H[N], H[M]] -> i hbar D[sharp(N dM - M dN)].
```

Physical meaning: change slicing order should differ by tangential deformation, а не новым observable process.

## Глава 59. Route-normal construction

Independent graph/path/dual-cell calculations supply discrete route/diffeomorphism target and principal-symbol scaling.

## Глава 60. Two-node -> three-node progression

Project deliberately advanced from simpler fixed graph checks to graph-changing three-node habitat rather than declaring closure from one pair.

## Глава 61. Three-node result

Supports:

```text
510, 648, 648.
```

Minimum `j=0` graph-change norm-squared fraction:

```text
0.4440331635.
```

Union reduced colored-graph orbits:

```text
31.
```

## Глава 62. Regulator hierarchy

Measured powers:

```text
route-only      ~ epsilon^0.9999571195
cross/D         ~ epsilon^1.0024037289
geometry/D      ~ epsilon^2.0061524985
joint defect/D  ~ epsilon^1.0064429344.
```

At `epsilon=1/64`:

```text
joint defect = 0.02522380789581472.
```

**FINITE PASS**, not arbitrary-graph theorem.

---

# ЧАСТЬ XV. Peter-Weyl regulator discipline

## Глава 63. Low cutoff can lie

A truncated representation space may generate fake anomaly or fake zero if operator hits support wall.

## Глава 64. Hit-depth theorem

For finite operator word touching a link `r` half-spin steps:

```text
Jmax >= j_in + r/2
```

is exact support-safety condition in declared setting.

For frozen Euclidean HH all-j=1/2 input:

```text
Jmax = 5/2
```

is safe.

Conservative declared Lorentzian HH wall:

```text
Jmax = 13/2.
```

## Глава 65. Spin parity

Exact doubled-spin grading separates Euclidean/Lorentzian operator parities and kills some mixed logical blocks by selection, not by numerical accident.

## Глава 66. Beta scope

Classical coefficient cancellation and finite parity/support checks do not imply a theorem of full quantum beta-independence.

---

# ЧАСТЬ XVI. Higher-shell constraint dynamics

## Глава 67. First return matrix

For the 32D logical sector:

```text
K = P H_E^2 P.
```

Finite result:

```text
rank K = 32
lambda_min(K)=4.306075987001578
lambda_max(K)=13.352781352746604
cond(K)=3.100916331493829.
```

## Глава 68. Genuine next shell

```text
M = P H_E^4 P - K^2.
```

Spectrum is positive:

```text
47.97777674967158 ... 186.90234422317016.
```

## Глава 69. Normalized Lambda

```text
Lambda = K^(-1/2) M K^(-1/2).
```

Results:

```text
lambda_min = 10.635759878291307
lambda_max = 15.059927665966466
mean       = 12.860443113390883
relative distance from scalar I = 0.09440461833276048.
```

Block-Lanczos reconstruction closes around `1e-13` residual scale.

Current main `higher-shell` job on run `33182064154`: **SUCCESS**.

## Глава 70. Interpretation boundary

These are exact finite **constraint spectral/Krylov data**. They are not:

```text
particle masses
physical graviton frequencies
observed Lorentz violation.
```

---

# ЧАСТЬ XVII. Первый refined metric anisotropy precursor

## Глава 71. S4 compression

First q4 refinement six-edge metric carrier resolves irreps `E` and `T2`:

```text
lambda_E  = 1.1111917875584736
lambda_T2 = 1.0220278507464782
Delta_ET  = 0.08916393681199541.
```

Current main `l1-q4-metric` job: **SUCCESS**.

## Глава 72. Почему встречаются 8.36% и 8.43%

Repository использует два explicit normalization denominators:

```text
Delta / ((lambda_E+lambda_T2)/2)
= 0.08359564595312347
```

и spin-2 dimension weighted:

```text
Delta / ((2lambda_E+3lambda_T2)/5)
= 0.08430036026012608.
```

Это разные normalization conventions одного и того же `Delta_ET`, а не противоречащие calculations.

## Глава 73. Что это число означает

Это **local Euclidean tetrahedral spin-2 anisotropy precursor**.

Оно не является final quartic Wilson coefficient, не является measured speed anisotropy и не является particle mass ratio.

---

# ЧАСТЬ XVIII. Mass shortcut no-go

## Глава 74. S4 spin-2 decomposition

```text
5 = E(2) + T2(3).
```

## Глава 75. Schur lemma

Для одной irreducible S4 triplet generation любое S4-invariant mass operator proportional to identity on that triplet. Поэтому один invariant tetrahedral splitter не создаёт три distinct charged-lepton masses.

## Глава 76. Что реально нужно для matter

```text
matter gauge/chiral representations
flavor representation
symmetry-breaking spurion/operator
Yukawa normalization
physical scale
blind eigenvalue ratios.
```

Ни higher-shell eigenvalues, ни 8% precursor нельзя переименовывать в Standard-Model masses.

---

# ЧАСТЬ XIX. Reduced TT positive control

## Глава 77. Leading massless pole

Reduced exact kernel has massless leading TT propagation and positive residue in declared control.

## Глава 78. Equal-time vacuum scaling

Expected inverse-momentum covariance reproduced:

```text
P_TT(k) ~ k^-1
```

with fitted slope near `-1.000000148`.

## Глава 79. Bare directional quartic controls

```text
(100) -> -1/18
(110) -> -1/72
(111) -> 0.
```

Restricted scalar-cubic decomposition:

```text
eta2_bare  = -1/45
zeta4_bare = -1/12.
```

Это positive-control lattice values, не physical interacting IR prediction.

---

# ЧАСТЬ XX. Generic quartic TT space: senior correction

## Глава 80. Почему onsite aI+bA+cO недостаточно

At `k=0` six-edge kernel может быть decomposed by same/adjacent/opposite edge orbits. At generic directed momentum symmetry law is covariance:

```text
C(g k) = U_g C(k) U_g^-1,
```

а не invariance at fixed generic k.

## Глава 81. Representation count before TT

Traceless spin-2 carrier:

```text
H5 = E + T2.
```

Symmetric quadratic metric products and quartic momentum polynomials produce 13 S4 singlet contractions before physical TT quotient.

## Глава 82. Exact TT quotient

Executable exact polynomial/Reynolds calculation:

```text
ambient h^2 k^4 monomials = 315
nonzero Reynolds invariants = 19
TT ideal rank = 222
invariant + ideal rank = 228
quotient dimension = 228-222 = 6.
```

Therefore:

```text
dim W_TT,S4^(4) = 6.
```

**EXACT.**

## Глава 83. Six Wilson coefficients

General parity-even quartic pole correction is represented by frozen basis `W1...W6`:

```text
delta K_TT^(4) = a_*^2 sum_r c_r W_r.
```

The first general microscopic pole datum is:

```text
c_IR=(c1,c2,c3,c4,c5,c6).
```

---

# ЧАСТЬ XXI. Как извлечь все шесть coefficients без post-hoc fit

## Глава 84. Three high-symmetry directions are insufficient

`(100),(110),(111)` give rank 5 only.

## Глава 85. Pre-registered generic direction

Adding `(120)` closes rank.

Frozen six observables:

```text
(100,+)
(100,x)
(110,+)
(110,x)
(111,+)
(120,+).
```

## Глава 86. Exact determinant

Extraction matrix has:

```text
det A = 1/699840000 != 0.
```

Hence six-vector is uniquely reconstructible before external data.

## Глава 87. Nested eta/zeta model

Old two-coefficient form remains legal **only as nested hypothesis**. If it survives full six-vector test:

```text
zeta4 = 2(e100-e110)
eta2  = (e100+4e110)/5
held-out relation: e100 - 4e110 + 3e111 = 0.
```

## Глава 88. Nested tetrahedral birefringence fingerprint

Single selected tensor splitter predicts a fixed high-symmetry splitting ratio:

```text
4 : 3 : 0.
```

Failure of this nested model does not falsify general six-dimensional S4 quartic sector.

---

# ЧАСТЬ XXII. On-shell observables and field redefinitions

## Глава 89. Off-shell actions contain bookkeeping freedom

Terms proportional to leading equation of motion can be moved by local field redefinition.

## Глава 90. On leading pole they vanish

For leading TT kernel:

```text
K0 = Z_T(-omega^2 + c_T^2 k^2) I_TT,
```

redefinition shifts quartic kernel by terms proportional to `K0`, so on shell they vanish.

## Глава 91. Consequence

Six-dimensional quotient is a physical **quartic pole** target, not arbitrary off-shell coefficient counting.

---

# ЧАСТЬ XXIII. Constraint resolvent is not physical frequency propagator

## Глава 92. Exact Feshbach/Krylov mathematics

For specified Hermitian constraint `H` and carrier `V`, project has exact:

```text
K=V^dag V
Q0=V K^-1/2
G_c(z)=Q0^dag (z-H)^-1 Q0
```

and exact Schur/Feshbach identities for moments `A=V^dag H V`, `B=V^dag H^2 V`.

## Глава 93. Critical no-go

`z` above is a **constraint-spectrum variable**.

```text
z != physical omega
```

by notation alone.

## Глава 94. Why canonical gravity is different

Hamiltonian constraint generates normal deformations of slices; it is not ordinary evolution relative to pre-existing external time.

## Глава 95. HDA is prerequisite, not clock

Correct HDA tells us history amplitudes should respect refoliation consistency. It does not select the physical inner product or probability measure.

---

# ЧАСТЬ XXIV. The physicalization bridge

## Глава 96. Legal route A — derived relational clock

If a physical matter/boundary clock `T` is actually derived and total constraint deparametrizes:

```text
P_T + H_phys = 0,
```

then genuine relational Schrödinger evolution and physical frequency become meaningful.

Current realistic matter clock is not derived.

## Глава 97. Legal route B — physical projector / rigging map

Construct gauge-consistent history amplitude/projector from constraint action, lapse histories, measure and boundary states.

The measure is part of physics, not cosmetic normalization.

## Глава 98. Sources must be inserted into physical history

Correct order:

```text
P_phys[J]
-> Z[J]
-> W[J]=log Z
-> mean metric
-> Gamma[g]
-> Gamma^(2)_metric.
```

## Глава 99. TT projection comes after effective metric response

```text
K_TT(omega,k)=Pi_TT Gamma^(2)_metric Pi_TT.
```

Poles of this object, not raw constraint eigenvalues, define physical gravitational-wave propagation.

## Глава 100. Disconnected vacuum processes

Raw global powers `H^2`, `H^4` can contain distant vacuum processes. Connected `W=log Z` construction is the proper route to remove disconnected bubbles before 1PI interpretation.

---

# ЧАСТЬ XXV. Finite relational positive controls

## Глава 101. Clock-only averaging kills phase

For nontrivial finite cyclic history character, untwisted average of clock shift projects only trivial character.

This is an exact no-go against pretending that a pure-gauge clock phase automatically survives group averaging.

## Глава 102. Combined constraint projector can preserve relational evolution

Finite positive control uses:

```text
G = S_clock tensor R_geom
P_rel = (1/8) sum_tau G^tau.
```

A global gauge-invariant history state survives, while conditioning on clock reading recovers nontrivial system relation.

Run `33155290632`: SUCCESS.

## Глава 103. Physical-history isometry

```text
V^dag V = I
V V^dag = P_rel.
```

## Глава 104. Relational source operators

For geometry operator `O`, history-dressed source commutes with combined constraint and intertwines through `V`.

## Глава 105. Finite Γ2 positive control

For shape source `jx X + jz Z`:

```text
Z(jx,jz)=cosh(sqrt(jx^2+jz^2)).
```

Zero-source connected shape Hessian is `I2` in that finite ensemble.

Push through exact shape-to-metric Jacobian gives:

```text
B^T B = (9/2) I2
metric response rank = 2
inverse tangent response eigenvalue = 2/9.
```

**This is architectural positive control, not physical graviton Gamma^(2).**

---

# ЧАСТЬ XXVI. Arithmetic/history frontier

## Глава 106. Complex number as real 2x2 action

For every modulus `N`:

```text
a+bi  <->  [[a,-b],[b,a]]  mod N
```

is exact ring representation. Determinant is norm; transpose represents conjugation.

## Глава 107. q=2 already contains a real complex structure

Oriented `C4` has a two-dimensional real quarter-turn block:

```text
J = [[0,-1],[1,0]]
J^2 = -I.
```

So multiplication by `i` can be represented as real quarter-turn.

## Глава 108. Residue is not an integer without history

Modulo value loses winding/sheet information. Complete oriented history lifts to universal cover and restores integer winding.

## Глава 109. Closed history -> winding

For nearest-neighbor path on `C_N`:

```text
n_T - n_0 = N w,
w in Z.
```

Subdivision preserves `w`.

## Глава 110. From finite residues to ordinary arithmetic

With winding/CRT bounds:

```text
finite residue data -> bounded Z reconstruction
-> bounded Q reconstruction
-> Archimedean completion -> R.
```

Finite modular arithmetic alone does not contain ordinary ordered real line.

## Глава 111. Dense U(1) does not require infinite root tower

Once `Q` exists, rational Pythagorean points are dense on unit circle. Therefore:

```text
C4 + Q -> dense U(1)
C4 + R -> U(1) exactly.
```

All-level discrete root doubling is sufficient but not necessary and remains a separate conditional microscopic refinement claim.

---

# ЧАСТЬ XXVII. Minimal reversible history and complex phase

## Глава 112. Why 5 instantaneous states are not C8 history

Four active states plus one undifferentiated transition state cannot reversibly remember which oriented edge was traversed.

## Глава 113. Reversibility forces four transition channels

Isometry of transitions requires distinguishable orthogonal edge memories:

```text
4 active + 4 transition = 8 states.
```

This gives minimal reversible `C8` history carrier.

## Глава 114. Independent Z4 x Z2 is not Z8

Adding an unrelated binary clock does not create an order-eight cyclic generator. Carry relation matters.

**EXACT no-go.**

## Глава 115. Orientation-resolved history step

Under narrow frozen minimal assumptions:

```text
W = P_+ tensor U8 + P_- tensor U8^-1.
```

## Глава 116. Fourier character

On `U|theta>=exp(i theta)|theta>`:

```text
W(theta)=cos(theta) I + i sin(theta) Y_L.
```

With `J=-iY_L`:

```text
W(theta)=exp(-theta J).
```

Complex phase and real rotation become two representations of same group element.

## Глава 117. Directed difference factorizes graph Laplacian

```text
Delta_W = W-I
Delta_W^dag Delta_W = I tensor (2I-U-U^dag).
```

Pure odd current has an extra finite-lattice zero at `theta=pi`; complete directed difference contains even term and leaves only trivial graph-Laplacian zero.

This is exact history algebra, **not a derived physical fermion or Dirac equation**.

---

# ЧАСТЬ XXVIII. The same J across layers

## Глава 118. Cross-layer convention audit

Same exact matrix `J` appears in:

```text
q=2 quarter-turn
complex-number realification
history Fourier rotation
quadratic phase weight
finite-dimensional Hermitian dynamics realification
directed-history factorization.
```

Only forward-orientation sign convention differs.

## Глава 119. Unique quadratic phase-weight precursor

For symmetric quadratic form `Q(v)=v^T A v`, `J` invariance:

```text
J^T A J = A
```

forces `A=lambda I`; positivity and normalization give Euclidean norm `|z|^2`.

This is a **Born-weight precursor**, not derivation of full measurement/Born rule.

## Глава 120. Realification of finite-dimensional quantum dynamics

Hermitian complex matrix can be written as real symmetric doubled matrix; Schrödinger flow becomes real skew-symmetric norm-preserving flow using same `J`.

Representation theorem does not solve physical-time problem in gravity.

---

# ЧАСТЬ XXIX. Orientation/history Lorentzian frontier

## Глава 121. Symmetry permits an orientation-current channel

`Y_L` is odd under orientation reversal; finite history current is odd under direction reversal. Product can be even under simultaneous reversal.

Symmetry permission does not determine dynamical coefficient.

## Глава 122. Exact sign-twirl compression

For 24 tetrahedral permutations, epsilon coefficient is sign character up to one global convention. If genuine microscopic ordered triple obeys required covariance, full logical sum compresses to one sign channel:

```text
L_epsilon = -12 Tr(Y_L O) Y_L.
```

Using flux witness:

```text
L_epsilon = -64 Tr(Q_or O) Q_or.
```

This can reduce 24 heavy amplitudes to one canonical matrix **after covariance is actually validated**.

## Глава 123. Heavy full-node attempt did not finish

Old direct full logical projection route ended cancelled inside amplitude step; no artifact.

**COMPUTATIONAL NO-RESULT.**

## Глава 124. Narrow preregistered reversal test also did not finish

Run `33149775494` computed two opposite ordered genuine triples in parallel. Both hit ~120-minute wall before artifact/collector.

Therefore:

```text
ZERO?    UNKNOWN
NONZERO? UNKNOWN
physical orientation-current coupling? OPEN.
```

Timeout is neither zero nor evidence of nonzero physics.

## Глава 125. Correct next implementation move

Optimize exact algebra/caching/sharding without changing operator definition or preregistered thresholds; prove covariance before symmetry transport; then repeat genuine amplitude test.

---

# ЧАСТЬ XXX. Heavy interblock K/A/B campaign audit

## Глава 126. Intended local block decomposition

Research branch decomposed second hit linearly over parent-block chambers to make exact calculation shardable.

## Глава 127. Active-cone backend required equivalence gate

Optimization was fail-closed: no production shards until reference vs local exact equivalence passed.

## Глава 128. Final status

Run `32037572477`:

```text
backend-equivalence: CANCELLED
metric-orbit shards: SKIPPED
collector: SKIPPED.
```

No new legal K/A/B artifact exists from this route.

**COMPUTATIONAL NO-RESULT.**

---

# ЧАСТЬ XXXI. From future six-vector to measurable GW observables

## Глава 129. Physical pole ansatz

Once genuine physical history gives frozen branch:

```text
omega_sigma^2 = c^2 k^2 [1 + a_*^2 k^2 e4_sigma(n) + ...].
```

## Глава 130. Group velocity

```text
(v_g,sigma-c)/c = (3/2) a_*^2 k^2 e4_sigma(n).
```

## Глава 131. Propagation phase

```text
delta_phi_sigma = -(1/2) L a_*^2 (omega/c)^3 e4_sigma(n).
```

## Глава 132. Modified-dispersion notation

Standard form:

```text
E^2=(pc)^2 + A_alpha (pc)^alpha.
```

Quartic BQG correction maps to:

```text
alpha=4.
```

## Глава 133. One common scale convention

```text
a_*^2 = 8 pi lambda_R_eff ell_P^2.
```

Then dimensionless six-vector plus one global scale maps to physical units.

Translator code exists; it is not a fitter.

---

# ЧАСТЬ XXXII. Why only one scale may be calibrated

## Глава 134. Additivity theorem

If integer history count `N` maps additively to dimensionful quantity:

```text
Q(N+M)=Q(N)+Q(M),
```

then on integers:

```text
Q(N)=s N.
```

One slope remains.

## Глава 135. Correct prediction protocol

```text
1. freeze dimensionless microscopic six-vector
2. freeze regulator/refinement prescription
3. derive scale, or calibrate exactly one declared physical datum
4. predict all remaining observables without retuning.
```

## Глава 136. Anti-fit rule

Independent scale fitting for every effect destroys predictive content and is forbidden by project ledger.

---

# ЧАСТЬ XXXIII. Compact U(1) and light

## Глава 137. Hopf/Pancharatnam carrier

Normalized qubit ray has:

```text
U(1) -> S3 -> CP1 ~ S2.
```

Relative link phase transforms as compact lattice U(1) connection; closed loops give Pancharatnam/Berry holonomy.

## Глава 138. Chern number

Declared positive control gives unit first Chern number.

This fixes topology/charge convention, not dynamical coupling strength.

## Глава 139. Why U(1) is not yet physical photon

Need:

```text
dynamical gauge action
deconfined propagating transverse modes
correct physical Hilbert/Gauss law
common causal cone
Maxwell stiffness Z_A.
```

## Глава 140. Fine-structure constant boundary

In stated normalization:

```text
alpha = 1/(4 pi Z_A).
```

Observed alpha determines a future comparison target for `Z_A`; current theory does not derive it.

---

# ЧАСТЬ XXXIV. Constants and anti-numerology

## Глава 141. c in SI is not a fundamental decimal prediction

SI fixes `c=299792458 m/s`. Meaningful BQG target is universality of limiting cone, e.g. gravity/photon speed ratio -> 1 in IR after both sectors are dynamically closed.

## Глава 142. hbar is an action-unit conversion until normalization derived

Overall phase/action slope remains one normalization direction.

## Глава 143. G is not fixed by HDA tensor structure

HDA fixes relative canonical structure, not overall gravitational action normalization.

## Глава 144. Cosmological term

Cosmological term cancels from relevant HDA bracket structure and remains an independent IR coupling in current construction. Observed tiny value is not derived.

## Глава 145. Mass ratios are stronger tests than absolute masses

But realistic matter representations/Yukawa sector must first be derived. Current gravity eigenvalues are not a substitute.

---

# ЧАСТЬ XXXV. CI is evidence, not theology

## Глава 146. Current main workflow structure

Physics workflow `.github/workflows/core-regression.yml` contains four jobs:

```text
canonical-core
directional-regge
l1-q4-metric
higher-shell.
```

Separate NEXUS workflows are unrelated benchmark infrastructure.

## Глава 147. Main run immediately before this audit

Run `33182064154`:

```text
directional-regge : SUCCESS
l1-q4-metric      : SUCCESS
higher-shell      : SUCCESS
canonical-core    : FAILURE.
```

## Глава 148. Why canonical-core was red

It failed at scope-policy scan before fast scientific gates ran. Historical archive was incorrectly scanned as active theory surface. This audit fixes the scanner by quarantining `docs/archive/` while retaining active-code safeguards.

Therefore the red job was a **CI policy failure**, not falsification of equations.

## Глава 149. Earlier canonical package provenance failure

An older release integration run passed its mathematical steps but failed expensive certificate regeneration because expected archive source path was missing. Again: artifact/provenance failure, not scientific negative result.

## Глава 150. Failure taxonomy

```text
scientific held-out FAIL
CI/policy FAIL
artifact/provenance FAIL
timeout/no-result
```

must never be collapsed into one word “failed”.

---

# ЧАСТЬ XXXVI. What is genuinely closed today

## Глава 151. Binary geometrogenesis

```text
q selector
local S2 shell
Walsh tetrahedral frame
Gauss geometry qubit
selected global PL completion
exact d*=3 causal-volume fixed point.
```

## Глава 152. Structural gravity bridge

```text
shape -> metric
B/simplicity/Urbantke controls
Regge/EH controls
DeWitt/ADM structure
finite HDA hierarchy
support-safe Peter-Weyl constraint calculations.
```

## Глава 153. Observable algebra

```text
massless TT control
complete six-dimensional quartic TT quotient
full-rank six-observable extractor
on-shell field-redefinition invariance
physical-units translator once six-vector + one scale exist.
```

## Глава 154. Arithmetic/history representation layer

Exact math includes:

```text
real complex structure J
modular representation
winding lift
minimal reversible C8
U(1) closure after rational/real completion
relational-projector positive controls.
```

---

# ЧАСТЬ XXXVII. What remains open physically

## Глава 155. Genuine gravitational physical projector

Need actual rigging/history measure or derived relational/boundary clock for full graph-changing constraints.

## Глава 156. Connected interblock history

Need connected metric cumulants across neighboring coarse blocks/refinement levels, not only local constraint spectra.

## Глава 157. Physical Gamma^(2)

Finite positive control gives correct architecture, but physical gravitational ensemble/measure must replace toy finite relation.

## Глава 158. First interacting six-Wilson vector

Need freeze:

```text
(c1,c2,c3,c4,c5,c6)_IR
```

from genuine physical pole before looking at external data.

## Глава 159. Regulator/refinement uncertainty

Need demonstrate six-vector stability and provide uncertainty rather than one cutoff number.

## Глава 160. One absolute scale

Derive or calibrate one datum only.

## Глава 161. Dynamical electromagnetic sector

Need `Z_A`, propagating modes and common physical cone.

## Глава 162. Matter sector

Need chiral/gauge representations, anomalies, generations, Yukawa dynamics and physical scale. None is silently imported from gravity eigenvalues.

## Глава 163. Blind external experiment

Only after theory commit, likelihood, scale rule and observables are frozen.

---

# ЧАСТЬ XXXVIII. Falsification rules

## Глава 164. Theory must be allowed to lose

EPRL holdout already demonstrates this principle: frozen extrapolation failed and remains recorded.

## Глава 165. No post-hoc basis selection

Six-Wilson basis/extractor frozen before microscopic momentum data.

## Глава 166. No post-hoc scale proliferation

One global normalization only.

## Глава 167. No timeout interpretation

No artifact -> no measured amplitude.

## Глава 168. No internal-to-external conflation

Reproducing repository algebra is not experimental confirmation of nature.

---

# ЧАСТЬ XXXIX. Atlas of repository evidence

## Binary / topology / dimension

```text
BINARY_TO_GEOMETRY_GATE.md
BIT_TO_SPACETIME_CENTRAL_EQUATION.md
MICRO_WALSH_QGEOM_BRIDGE.md
SPATIAL_QUBIT_GEOMETRY_BRIDGE.md
GLOBAL_MANIFOLD_Q2_COMPLETION.md
Q2_DIMENSION3_FIXED_POINT_CLOSURE.md
OBSERVER_SCALE_SMOOTHING.md
```

## Metric / continuum geometry

```text
LOGICAL_SHAPE_METRIC_JACOBIAN.md
FACE_QUBIT_BFIELD.md
SIMPLICITY_PROJECTOR_THEOREM.md
PLEBANSKI_URBANTKE_BRIDGE.md
PLEBANSKI_CONNECTION_EINSTEIN_GATE.md
REGGE_EH_CUBIC_BRIDGE.md
DEWITT_HDA_UNIQUENESS.md
FLUX_DEWITT_SIGNATURE_THEOREM.md
BF_GR_DIRAC_COUNT_DISCRIMINATOR.md
```

## HDA / Peter-Weyl

```text
K5_QUANTUM_GEOMETRY_BRIDGE.md
K5_ORIENTED_QUANTUM_HDA_RESULT.md
PETER_WEYL_TWO_NODE_EUCLIDEAN_RESULT.md
THREE_NODE_GRAPH_HDA_RESULT.md
FIXED_CUTOFF_COMPOSITION_BOUND.md
JOINT_REGULATOR_LIMIT.md
LORENTZIAN_BETA_CANCELLATION.md
PETER_WEYL_HIGHER_SHELL_LAMBDA_RESULT.md
FESHBACH_INTERBLOCK_EFFECTIVE_KERNEL.md
```

## Independent coherent / fusion route

```text
EPRL_COHERENT_FUSION_SCALING.md
EPRL_COHERENT_J15_OVER2_PREREGISTRATION.md
EPRL_COHERENT_J15_OVER2_RESULT.md
```

## TT / physicalization

```text
TT_PROPAGATOR_FIRST_PASS.md
TT_VACUUM_TWO_POINT_RESULT.md
L1_Q4_S4_METRIC_COMPRESSION_RESULT.md
S4_TT_QUARTIC_COMPLETE_BASIS.md
C6_TO_TT_WILSON_COEFFICIENTS.md
TETRAHEDRAL_TT_BIREFRINGENCE_THEOREM.md
ON_SHELL_TT_WILSON_INVARIANCE.md
TT_TO_REAL_PHYSICS_OBSERVABLES.md
PHYSICALIZATION_SCALE_OBSERVABLE_PREDICTION.md
CONSTANTS_ZERO_FIT_LEDGER.md
PREDICTIONS_AND_EXPERIMENTAL_TESTS.md
```

The strongest constraint-to-history conceptual correction currently lives on physicalization PR #29 in `HAMILTONIAN_CONSTRAINT_TO_EFFECTIVE_ACTION.md`.

## Repository archaeology

[`REPOSITORY_AUDIT_2026-08-29.md`](REPOSITORY_AUDIT_2026-08-29.md) records all 73 refs, PR families, current run IDs and no-result states.

---

# ЧАСТЬ XL. Reproduction protocol

## Глава 169. Install

```bash
python -m pip install -r requirements.txt
```

## Глава 170. Canonical workflow

```text
.github/workflows/core-regression.yml
```

## Глава 171. Key local gates

Examples:

```bash
python scripts/q2_dimension3_fixed_point_gate.py
python scripts/micro_walsh_qgeom_gate.py
python bcqg_global_manifold_gate.py
python scripts/logical_shape_metric_jacobian_gate.py
python scripts/regge_eh_cubic_bridge.py
python scripts/peter_weyl_three_node_graph_hda_gate.py
python scripts/tt_regge_zt_l6_gate.py
python scripts/s4_tt_quartic_complete_basis_gate.py
python scripts/s4_tt_six_wilson_predictor.py --selftest
```

## Глава 172. Green means scoped reproduction

```text
internal declared gate reproduced = YES
nature confirmed candidate theory = NOT IMPLIED.
```

---

# ЧАСТЬ XLI. Compact truth table

| Claim | Status |
|---|---|
| `q+2=2^q` selects q=2 in declared route family | **EXACT** |
| q=2 local shell is octahedral S2 | **EXACT** |
| Walsh q=2 labels form regular tetrahedral normals | **EXACT** |
| four face qubits contain 2D Gauss-singlet geometry carrier | **EXACT** |
| selected 16-cell PL completion is stable in tested refinements | **EXACT/FINITE** |
| causal-volume fixed point is exactly 3 | **EXACT** |
| `z≈1` in frozen finite scaling | **FINITE PASS** |
| smoothing exponents near -2/-3/-4 | **FINITE PASS** |
| q=2 global gluing uniquely follows from every bare graph rule | **OPEN/STRONGER CLAIM** |
| X/Z -> rank-two intrinsic metric tangent | **EXACT** |
| orientation Y is third linear intrinsic metric tangent | **NO-GO** |
| local E/T2 q4 split exists | **FINITE PASS** |
| local split equals final physical Lorentz violation | **NOT CLAIMED** |
| Regge L6 frozen continuation | **HELD-OUT PASS** |
| EPRL finite-window power-law extrapolation at j=15/2 | **HELD-OUT FAIL** |
| higher-shell Lambda is finite positive non-scalar constraint data | **FINITE PASS** |
| Lambda eigenvalues are particle masses | **NO** |
| constraint spectral variable is physical frequency automatically | **NO-GO** |
| parity-even generic S4 quartic TT space dimension = 6 | **EXACT** |
| six-observable extractor full rank | **EXACT** |
| final interacting physical six-vector frozen | **OPEN PHYSICAL** |
| q=2 real complex structure `J^2=-I` | **EXACT** |
| complete oriented history supplies integer winding | **EXACT TOPOLOGICAL** |
| minimal reversible C4 history lift has 8 states | **EXACT under stated model** |
| combined relational-projector positive control works | **FINITE EXACT** |
| finite relational source -> metric Γ2 architecture works | **FINITE EXACT** |
| genuine gravity orientation-current amplitude measured | **OPEN / heavy no-result** |
| compact U(1) carrier exists | **EXACT KINEMATIC** |
| dynamical Maxwell stiffness / alpha derived | **OPEN** |
| realistic matter masses derived | **NO** |
| experimental confirmation | **NO** |

---

# ЧАСТЬ XLII. The next decisive calculations

## Глава 173. Fix reproducibility surface first

Policy/provenance CI must be green for the right reason, without deleting historical evidence.

## Глава 174. Finish genuine Lorentzian ordered amplitude economically

Use exact symmetry only after microscopic covariance gate; shard/checkpoint heavy sparse states; retain preregistered ZERO/NONZERO thresholds.

## Глава 175. Build genuine gravity relational/history projector

Move from finite positive control to actual graph-changing constraints and physical boundary/clock construction.

## Глава 176. Insert connected metric sources

Construct physical `Z[J]`, connected `W[J]`, then `Gamma`.

## Глава 177. Extract full six-vector first

No nested two-parameter shortcut before general answer.

## Глава 178. Prove refinement stability

Run multiple regulators/refinements and report uncertainty.

## Глава 179. Freeze one common scale

Only after dimensionless dynamics frozen.

## Глава 180. Blind comparison

Then — and only then — open held-out gravitational-wave/phase data.

---

# Эпилог. Что такое Binary Quantum Gravity в этом репозитории

Теория бинарной квантовой гравитации здесь — не утверждение, что Вселенная буквально состоит из маленьких нулей и единиц, нарисованных на готовой lattice.

Это более строгая исследовательская программа:

```text
начать с минимальной различимости
и отношений между альтернативами;
не предполагать заранее пространственную dimension;
получить q=2 из локального combinatorial condition;
вывести tetrahedral geometric carrier из binary character algebra;
склеить quantum cells в selected global 3D PL phase;
проверить exact volume-growth fixed point d*=3;
показать smooth coarse geometry;
построить constraint dynamics и GR/HDA controls;
вывести полный observable space spin-2 corrections;
а затем не перепутать constraint spectrum с физическим временем.
```

Самая сильная корректная формулировка на 29 августа 2026:

> **Репозиторий содержит длинную, воспроизводимую и во многих местах точную candidate architecture от binary route relations до tetrahedral quantum geometry, three-dimensional PL/scaling phase, GR/HDA и полного six-dimensional quartic TT observable dictionary. Он также содержит exact arithmetic/history/relational-projector representation results и честные held-out successes/failures. Но full gravitational physical history/inner product, connected physical effective action, first interacting six-Wilson graviton vector, common absolute scale, dynamical Maxwell stiffness, realistic matter sector и blind experimental validation ещё не закрыты.**

Именно эта граница отличает научную теорию-кандидат от красивой нумерологии.

Последнее слово должен сказать не README, а эксперимент.
