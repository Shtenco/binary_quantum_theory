# Полный аудит `Shtenco/binary_quantum_theory`

**Дата среза:** 29 августа 2026  
**Repository id:** `1293271223`  
**Текущий `main` до этого аудита:** `5822d0085a7ae841f49eaba4b7fc763a2306f765`

Этот документ — технический ledger аудита всех доступных веток, PR, ключевых расчётов, CI и научных claim boundaries. Он намеренно содержит исторические названия и снятые гипотезы. Он не является активной поверхностью теории; активный научный вход — `README.md`.

---

## 1. Главный вывод аудита

Репозиторий содержит не одну линейную историю, а несколько научных эпох:

1. **Ранняя CIMFIG/BCQG эпоха** — широкая информационно-графовая архитектура с большим числом side-sector гипотез и монолитным verifier.
2. **Scope reset / PR #31** — каноническая программа была сознательно сужена до
   `binary/qubit microstructure -> quantum geometry -> refinement -> smooth geometry -> GR/ADM/HDA`.
3. **Structural closure / PR #32–35** — были сведены q=2 geometrogenesis, Peter–Weyl, HDA, Regge, TT и observable dictionary.
4. **Physicalization frontier / PR #29** — важная senior correction: Hamiltonian constraint resolvent не является физическим частотным propagator; generic quartic TT sector имеет шесть Wilson coefficients, а не два.
5. **Arithmetic/history/projector frontier / PR #40–49** — exact representation/topology results для real complex structure, winding, C8 history, relational projector и finite source/Γ² positive control.

Поэтому корректный статус на 29 августа 2026:

```text
structural candidate architecture          = CLOSED in declared exact/finite scopes
complete six-dimensional TT dictionary     = CLOSED algebraically
physical projector/history of gravity      = OPEN
first interacting physical six-Wilson pole = NOT FROZEN
common physical scale                      = OPEN / one global normalization
Maxwell stiffness / alpha                   = NOT DERIVED
Standard-Model matter/masses                = NOT DERIVED
experimental confirmation                   = NO
```

---

## 2. Переименование репозитория и provenance старых run IDs

Старые GitHub Actions logs и artifact references могут показывать имя:

```text
Shtenco/info_graph_theory
```

а текущий репозиторий называется:

```text
Shtenco/binary_quantum_theory
```

Это один и тот же GitHub repository id `1293271223`. Поэтому historical artifact provenance к `info_graph_theory` не является внешней зависимостью от другой теории: это старое имя этого же repository.

---

## 3. Полный branch inventory: 73 refs

### 3.1 Canonical / release / cleanup

```text
main
cleanup/gr-qm-bit-continuum
release/canonical-theory-package-v1
final-squash-base
```

`cleanup/gr-qm-bit-continuum` соответствует ключевому scope reset PR #31. `release/canonical-theory-package-v1` — release branch PR #35. `final-squash-base` — исторический integration base.

### 3.2 Codex historical formalization branches — 17

```text
codex
codex-3g4lb0
codex-4bua2u
codex-4ni6ut
codex-5uocfq
codex-89btph
codex-bwhfkc
codex-e0ee6e
codex-hobdxi
codex-kpnzg2
codex-lppw5h
codex-qgjhgi
codex-ro2602
codex-sjothi
codex-va54l6
codex-vbnn2h
codex-yn178z
```

Эти ветки в основном относятся к июль–август 2026 formalization эпохе: CIMFIG V18, README rewrites, early verifier/gate ledger. Их надо читать как историю эволюции, а не как 17 независимых физических теорий.

### 3.3 NEXUS benchmark branches — 4, не физическая теория

```text
nexus-r74-phi-fix-run
nexus-r74-public-run-20260818
nexus-r74-qwen-instruct-run
nexus-r74-structured-five-run
```

Это изолированный benchmark нейромодели R7.4. Он не должен влиять на физический статус Binary Quantum Gravity.

### 3.4 Research branches — 48

```text
research/bcqg-core-candidate-v1
research/canonical-frontier-v2
research/canonical-ledger-2026-08-15
research/canonical-lorentzian-frontier
research/canonical-prefactor-audit
research/hl-sine-dag
research/k5-covariance-hda
research/logical-s4-sign-twirl
research/lorentzian-composition-fast
research/lorentzian-ordered-triple-fast
research/micro-hda-joint-prediction
research/mirror-anisotropy-audit-v2
research/mirror-orientation-eta
research/modular-complex-arithmetic-bridge
research/operator-micro-dynamics
research/physical-pole-universality
research/physicalization-l1-depth2-metric
research/physicalization-scale-observable-prediction
research/post-hda-physicalization-v2
research/pw-lorentzian-24-collector
research/pw-lorentzian-24-mitm
research/pw-lorentzian-component-fast
research/pw-lorentzian-component-mitm
research/pw-lorentzian-envtrace
research/pw-lorentzian-envtrace-orbit
research/pw-lorentzian-logical-projection
research/pw-lorentzian-lowcut-scout
research/pw-lorentzian-mitm
research/pw-lorentzian-parity
research/pw-lorentzian-single-mitm
research/pw-lorentzian-single-probe
research/pw-lorentzian-ultralow-scout
research/pw-master-32
research/pw-spin-parity-master
research/q2-face-incidence-bridge
research/q2-gravity-gyc-amplitude
research/q2-gravity-gyc-sign-twirl
research/q2-history-directed-laplacian-factorization
research/q2-history-fourier-complex-structure
research/q2-history-gravity-orientation-current
research/q2-history-phase-refinement-winding
research/q2-orientation-intrinsic-metric-nogo
research/q2-oriented-flux-history-observable
research/q2-relational-history-projector
research/q2-relational-metric-source
research/q2-unified-complex-structure
research/sine-kkv-next
research/zeroaware-volume-migration
```

### 3.5 Research-family classification

**Merged / absorbed into canonical main:**

- `research/zeroaware-volume-migration`
- `research/pw-spin-parity-master`
- `research/pw-master-32`
- `research/pw-lorentzian-parity`
- `research/logical-s4-sign-twirl`
- `research/micro-hda-joint-prediction`
- `research/operator-micro-dynamics`
- ряд canonical/HDA/prefactor branches, чьи результаты были перенесены в main.

**Current physically important frontier:**

- `research/physicalization-scale-observable-prediction` — PR #29;
- `research/modular-complex-arithmetic-bridge` — PR #40;
- `research/q2-history-phase-refinement-winding` — PR #41;
- `research/q2-gravity-gyc-amplitude` — PR #42, heavy no-result;
- `research/q2-gravity-gyc-sign-twirl` — PR #43;
- `research/q2-history-fourier-complex-structure` — PR #44;
- `research/q2-history-directed-laplacian-factorization` — PR #45;
- `research/q2-unified-complex-structure` — PR #46;
- `research/q2-relational-history-projector` — PR #47;
- `research/q2-relational-metric-source` — PR #48;
- `research/q2-orientation-intrinsic-metric-nogo` — PR #49;
- `research/q2-oriented-flux-history-observable` — successful exact operator witness, currently without dedicated PR.

**Heavy Lorentzian scouts / computational archaeology:**

`research/pw-lorentzian-*`, `research/lorentzian-*`, `research/sine-kkv-next`, `research/hl-sine-dag` фиксируют разные пути ускорения, decomposition, MITM, component/envtrace/scout calculations. Они полезны как provenance вычислительной эволюции, но отсутствие artifact не превращается в физический результат.

**Historical side-sector research:**

Branches с ранней mirror/chirality/other side-sector nomenclature должны рассматриваться как история. После PR #31 эти интерпретации не являются canonical physical claims, хотя некоторые чистые representation-theory identities были сохранены в переинтерпретированном виде.

---

## 4. PR archaeology: что реально изменяло теорию

### PR #1–18 — CIMFIG formalization era

README, CIMFIG V18, diamond-channel formalism, early proof ledger, monolithic verifier, auxiliary EML/WKB/fermion/critical demos. Большая часть этой поверхности позднее была снята из canonical core.

### PR #19 — zero-aware Peter–Weyl volume migration

Важная numerical correction exact-zero handling. Это не концептуальный scope pivot.

### PR #21–28 — exploratory quantum-geometry/Lorentzian side branches

Некоторые exact representation/parity/orientation identities пережили последующий cleanup, но широкие physical interpretations не должны переноситься автоматически.

### PR #31 — главный scope reset

Удалены из canonical surface:

- broad CIMFIG V18 matter/gauge architecture;
- old infoton/foam/force side sectors;
- WKB tunnelling, EML compression и lattice-fermion side experiments;
- reduced two-Ising TT demo, где две TT polarizations были вставлены конструкцией;
- monolithic ~51k-line `bcqg_unified_verification.py`;
- broad speculative thought-experiment list.

После #31 canonical programme:

```text
binary/qubit microstructure
-> quantum geometry
-> refinement/coarse graining
-> smooth metric/curvature
-> Einstein/ADM/HDA continuum structure
-> physicalization.
```

### PR #32

Закрыл exact local q=2 Walsh carrier/gluing, дал finite three-node graph-changing HDA и fixed-input joint regulator result.

### PR #33

Показал, что 4 active q=2 states сами не являются endpoint `(2,2)` Peter–Weyl carrier; добавление graph-changing no-link state даёт exact `(2,2)+(1,1)` SO(5) vector representation и matrix-unit factorization. Higher-j symmetric blocking — conditional.

### PR #35

Собрал canonical structural package и truth ledger. Важная оговорка аудита: его head workflow `32137546119` завершился FAILURE не на математическом gate, а на artifact provenance rebuild:

```text
RuntimeError: cannot regenerate L1 metric certificate; missing repository archive source path
```

Core algebra/geometry gates перед этим прошли. Поэтому этот run нельзя маркировать GREEN, но и нельзя трактовать как falsification теории.

### PR #29 — physicalization senior correction

Ключевой открытый PR. Установлены две принципиальные поправки:

1. generic nonzero momentum требует полного six-dimensional S4 quartic TT quotient;
2. Hamiltonian constraint spectral variable `z` нельзя переименовать в physical frequency `omega`.

Правильная цепь:

```text
H[N]
-> physical projector/history (или derived relational clock)
-> Z[J]
-> W[J]
-> Gamma[g]
-> Gamma^(2)_metric
-> TT projection
-> physical K_TT(omega,k)
-> six pole Wilson coefficients.
```

### PR #40–49 — arithmetic/history/projector frontier

Эти PR добавляют exact math/representation results, но не закрывают физический gravity projector. Их CI results перечислены ниже.

---

## 5. Current main CI audit

До этого audit-commit `main=5822d008...` запустил workflow run `33182064154`.

| Job | Статус | Аудит |
|---|---|---|
| `directional-regge` | SUCCESS | numerical continuum controls reproduced |
| `l1-q4-metric` | SUCCESS | certified 24-column q4 metric compression reproduced |
| `higher-shell` | SUCCESS | 31 inherited columns + fresh heavy column 28 -> full Lambda reproduced |
| `canonical-core` | FAILURE | scope-audit false positive, не physics/math failure |

Fresh `canonical-core` failure произошёл на первом policy gate:

```text
python scripts/audit_core_scope.py
```

Сканер считал исторические `docs/archive/*` активной theory surface и блокировал repository за сохранение retired vocabulary в архиве. Это policy bug. В рамках текущего аудита scanner исправлен: исторический archive и сам audit ledger quarantined, а active code/docs/ledgers по-прежнему проверяются.

Важно: до исправления `canonical-core` не успел выполнить последующие fast gates, поэтому их свежий статус на commit `5822d008...` не должен автоматически объявляться PASS только по старым runs.

---

## 6. Heavy calculation no-results

### 6.1 Full local block K/A/B production

Run:

```text
32037572477
workflow: collective-l1-block-e-krylov
head: 20f2caaebd3bc10705ae3614991d2293a86d568d
```

Final:

```text
backend-equivalence = CANCELLED
72 metric-orbit shards = SKIPPED
collector = SKIPPED
```

Step `Reference vs exact active-cone backend` не завершился; equivalence certificate не frozen; K/A/B collector artifact отсутствует.

**Статус:** `COMPUTATIONAL NO-RESULT`. Нельзя публиковать придуманные K/A/B values.

### 6.2 Full 24-term Lorentzian logical projection / PR #25

Workflow run `31829341320`: cancelled внутри full epsilon-oriented amplitude step; artifact отсутствует.

**Статус:** `COMPUTATIONAL NO-RESULT`.

### 6.3 Narrow preregistered reversal amplitude / PR #42

Run `33149775494`:

```text
T_123 -> cancelled at ~120 min wall
T_213 -> cancelled at ~120 min wall
collector -> skipped
```

Нет ZERO result и нет NONZERO result.

**Статус:** `UNKNOWN / COMPUTATIONAL NO-RESULT`; `g_YC^gravity = OPEN_PHYSICAL`.

---

## 7. Strong exact / finite results that survived audit

### 7.1 q=2 selector

Within declared binary route family:

```text
q+2=2^q
```

has unique integer solution `q=2` for `q>=1`.

### 7.2 Local topology

q=2 Hamming cycle `C4` plus two causal endpoints gives octahedral simplicial `S2`.

### 7.3 Walsh tetrahedral frame

The three nontrivial real characters of `Z2^2` produce four unit vectors with zero sum and pairwise dot `-1/3`: exact regular tetrahedron normals.

### 7.4 Geometry qubit

Four spin-1/2 face qubits contain a two-dimensional Gauss-singlet sector. Logical `X,Z` encode intrinsic shape directions; logical `Y` is the orientation pseudoscalar.

Latest branch exact witness:

```text
Q_or = epsilon_abc J1^a J2^b J3^c = (sqrt(3)/4) Y_L
```

Run `33156152205`: SUCCESS.

### 7.5 Global PL completion

Selected 16-cell boundary:

```text
(V,E,F,T)=(8,24,32,16)
Betti=(1,0,0,1)
```

with checked PL refinement:

```text
16 -> 384 -> 9216 tetrahedra
```

and no bad simplex links in tested generations. This is existence/stability, not uniqueness of bare graph gluing.

### 7.6 Exact dimension-three fixed point

```text
N_g=(4*8^g+10)/7

d_g=3+log2(1-35/(16*8^(g-1)+40))

d_g < 3,
d_(g+1)>d_g,
d_g -> 3.
```

Sequence:

```text
g=2  2.662965012722429
g=3  2.951744831392779
g=4  2.993853015664851
g=5  2.999229782139151
g=6  2.999903693848493
g=7  2.999987961279020
g=8  2.999998495152814
```

General frozen-q route family has causal-volume fixed point `d*=q+1`.

### 7.7 Observer/dynamical scaling

Frozen finite diagnostics:

```text
d_H = 2.999229782139151
z ≈ 0.998281156
d_eff_slice = d_H/z ≈ 3.004393867
d_eff_history = 1+d_H/z ≈ 4.004393867
```

Do not divide by `z` twice.

Smoothing:

```text
delta g ~ b^-2.001707
grad delta g ~ b^-3.001458
delta R ~ b^-4.000524
```

These are finite controls, not a universal critical theorem for arbitrary ensembles.

### 7.8 Local metric Jacobian

`X/Z` -> two independent tracefree metric tangents, exact rank 2. New frontier no-go:

```text
partial g / partial Y = 0
```

at linear intrinsic-metric level.

### 7.9 L1 q4 metric precursor

```text
lambda_E  = 1.1111917875584736
lambda_T2 = 1.0220278507464782
Delta_ET  = 0.08916393681199541
```

Two normalization conventions appear in repository:

```text
Delta / ((lambda_E+lambda_T2)/2) = 0.08359564595312347  (~8.36%)
Delta / ((2lambda_E+3lambda_T2)/5) = 0.08430036026012608 (~8.430036%)
```

They are not contradictory; denominators differ. Neither number is a physical Lorentz-violation coefficient, `zeta4`, or particle mass ratio.

### 7.10 Three-node HDA finite result

```text
supports = 510, 648, 648
min j=0 graph-change fraction = 0.4440331635
union reduced graph orbits = 31
route power = 0.9999571195
cross power = 1.0024037289
pure geometry power = 2.0061524985
joint power = 1.0064429344
joint defect at 1/64 = 0.02522380789581472
```

Finite diagnostic; arbitrary-graph/unbounded Lorentzian theorem remains stronger and open.

### 7.11 Higher-shell Peter–Weyl

Exact finite constraint data:

```text
rank K = 32
lambda_min(K)=4.306075987001578
lambda_max(K)=13.352781352746604
cond(K)=3.100916331493829

lambda_min(M)=47.97777674967158
lambda_max(M)=186.90234422317016

lambda_min(Lambda)=10.635759878291307
lambda_max(Lambda)=15.059927665966466
mean=12.860443113390883
relative distance from scalar I=0.09440461833276048
block-Lanczos residuals ~1e-13
```

This is constraint spectral/Krylov information, not particle masses and not physical frequency spectrum.

---

## 8. Held-out tests: successes and failures

### 8.1 Regge L=6 — preregistered PASS

Frozen model from L=3,4,5:

```text
Z_L = 1/8 + C/L^2 + D/L^4
```

Prediction:

```text
Z6_pred = 0.11876923193907167
```

Held-out direct result:

```text
Z6_obs = 0.11876075461190198
relative error = 0.00714%
```

Preregistered threshold 1% -> strong PASS.

### 8.2 EPRL coherent j=15/2 — preregistered extrapolation FAIL

Frozen four-point power-law forecast:

```text
epsilon_pred = 0.00026207793589462915
```

Observed:

```text
epsilon_obs = 0.000125031726024738
relative prediction error ≈ 52.3%
```

Preregistered rule `FAIL > 40%` -> finite-window power-law hypothesis FAIL.

Но coherent geometric-ray factorization fidelity remains:

```text
0.9999999999999996
```

Поэтому failed extrapolation не является failure of coherent-simplicity preservation. Correct lesson: no replacement exponent should be fit post hoc.

---

## 9. TT / physical observable audit

Reduced TT positive control has massless leading pole and inverse-momentum equal-time covariance. Bare lattice directional quartic controls:

```text
axis100 = -1/18
face110 = -1/72
body111 = 0
```

Restricted nested scalar-cubic coefficients:

```text
eta2_bare  = -1/45
zeta4_bare = -1/12
```

These are controls, not final interacting IR coefficients.

Generic parity-even directed-momentum S4 quartic TT response has exact physical quotient dimension:

```text
6
```

The old high-symmetry directions `(100),(110),(111)` span rank 5. Adding `(120)` produces full rank 6 with exact determinant:

```text
det A = 1/699840000
```

Therefore the general future pole prediction is:

```text
c_IR=(c1,c2,c3,c4,c5,c6)
```

and `eta/zeta` or single-tetrahedral models are nested hypotheses only.

On-shell local field redefinitions do not enlarge this six-dimensional physical pole quotient.

---

## 10. Mass/constant no-go ledger

Current repository does **not** derive:

- electron/muon/tau masses;
- Standard Model generation structure;
- fine-structure constant;
- observed cosmological constant;
- numeric Newton constant without scale setting.

Schur-lemma analysis blocks the shortcut “one S4-invariant tetrahedral splitter -> three generation masses”. Higher-shell eigenvalues have insufficient spectral range and no derived matter/Yukawa map.

Current compact U(1) carrier provides topology/phase kinematics, not Maxwell stiffness. In the stated convention:

```text
alpha = 1/(4*pi*Z_A)
```

but `Z_A` is open dynamics. Experimental `alpha` determines only a future comparison target, not a current derivation.

---

## 11. Constraint vs physical time — critical correction

The Peter–Weyl object is a Hamiltonian constraint. For exact Feshbach/Krylov data:

```text
G_constraint(z)=Q0^dag (z-H)^-1 Q0
```

`z` is a constraint-spectrum variable unless a physical-time construction is supplied.

Legal physicalization route:

```text
H[N]
-> physical projector / rigging map / history amplitude
   OR derived relational physical Hamiltonian
-> metric sources
-> Z[J]
-> W[J]
-> Gamma[g]
-> Gamma^(2)_metric
-> TT projection
-> K_TT(omega,k)
-> six on-shell Wilson coefficients.
```

HDA is necessary refoliation consistency, not the physical inner product itself.

---

## 12. Arithmetic/history frontier audit

### PR #40 — modular complex / ordinary arithmetic

Run `33098145714`: SUCCESS.

Exact representation results include:

```text
a+bi mod N <-> [[a,-b],[b,a]] mod N
J=[[0,-1],[1,0]], J^2=-I
residue+winding -> Z
bounded reconstruction -> Q
Archimedean completion -> R
C4+Q dense in U(1)
C4+R -> U(1)
```

No preferred physical modulus, Born rule or physical Hamiltonian is derived.

### PR #41 — winding / minimal C8

Run `33149358463`: SUCCESS.

Exact:

```text
closed oriented history -> integer winding
4 active + 4 distinguishable transition channels -> minimal reversible C8
Z4 x Z2 != Z8
untwisted clock/history averaging kills nontrivial character
```

Conditional all-level root-doubling remains conditional.

### PR #43–46

Successful exact reductions/representation audits:

- epsilon sign-twirl;
- history Fourier phase = real SO(2) complex-structure rotation;
- directed difference squared = undirected graph Laplacian;
- same `J` across phase weight / realification / history conventions.

### PR #47–49

Successful finite exact positive controls:

- combined relational projector preserving conditional evolution;
- relational source algebra and finite Γ² tangent response;
- orientation `Y` invisible to linear intrinsic metric.

These do not yet instantiate the genuine gravitational rigging map.

---

## 13. Current reproducibility meaning

A green individual gate means only that its declared mathematical/computational scope reproduced. It does not imply experimental truth.

A red workflow can mean several different things and must be classified:

```text
MATH/PHYSICS FAIL        -> a preregistered scientific test failed
POLICY/CI FAIL           -> scanner/configuration/provenance issue
TIMEOUT/NO-RESULT        -> computation did not finish
ARTIFACT FAIL            -> evidence packaging/retrieval failed
```

This audit found all four patterns in project history, so future README/status files must always record failure class, not only red/green color.

---

## 14. Changes made by this audit

1. Preserve the pre-audit README unchanged in `docs/archive/`.
2. Rewrite `README.md` as the canonical **Binary Quantum Gravity / Теория бинарной квантовой гравитации** scientific book.
3. Add this complete repository/branch/CI ledger.
4. Fix `scripts/audit_core_scope.py` so historical archives do not block active scientific scope while active source/docs remain protected.
5. Record cancelled heavy calculations explicitly as `COMPUTATIONAL NO-RESULT`.
6. Record both held-out PASS and held-out FAIL results.
7. Separate structural closure from physical-history/experimental closure.

---

## 15. Current strongest scientifically correct statement

> `binary_quantum_theory` contains a long, unusually explicit and executable candidate architecture from binary route relations through q=2 tetrahedral quantum geometry, a three-dimensional PL/scaling phase, GR/HDA and Regge controls, finite Peter–Weyl constraint dynamics, and a complete six-dimensional quartic TT observable dictionary. Several exact arithmetic/history/projector representation results extend that architecture. However the genuine gravitational physical projector/history measure, connected interblock physical effective action, first interacting six-Wilson graviton pole vector, common physical scale, Maxwell stiffness, realistic matter sector and blind external validation remain open. No cancelled heavy workflow is promoted to a physics result, and failed preregistered hypotheses remain recorded as failures.
