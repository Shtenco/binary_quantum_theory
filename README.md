# От бита к пространству-времени

## Binary Causal / Information-Graph Quantum Gravity — candidate theory

> **Канонический статус на 17 августа 2026.** Репозиторий содержит вычислительно проверяемую кандидатную архитектуру перехода от бинарной микроструктуры к 3D/4D-like геометрии, SU(2)/Peter–Weyl квантовой геометрии, spin-2 TT-сектору и HDA/ADM-гравитации. Это **не экспериментально установленная теория природы**. Главный frontier теперь не очередной внутренний HDA-gate, а physicalization: абсолютная нормировка → TT propagator → frozen dimensionless coefficient → blind external test.
>
> Важная поправка к старым версиям README: smoothing law `delta g ~ b^-2.001707` **не является quantum-vacuum spectrum**. Прямой reduced TT two-point calculation даёт `P_TT(k) ~ k^-1`. Старое условное `k^+1.003414` считается отвергнутой интерпретацией smoothing defect для Gaussian TT vacuum.

---

# 0. Проект в одной лестнице

```text
BITS
 -> q=2 binary selector
 -> C4 route shell
 -> octahedral S2 vertex link
 -> minimal flag 16-cell globalization
 -> recursive PL S3
 -> d_H ~ 3
 -> d_s(slice) ~ 3
 -> z ~ 1
 -> d_s(history) ~ 4
 -> smooth IR metric
 -> face qubits / adjoint B-field
 -> SU(2) Peter-Weyl geometry
 -> unique j=2 collective sector
 -> TT helicity +2/-2
 -> H_E + (1+beta^2) H_L
 -> route-normal generator
 -> sharp(N dM - M dN)
 -> HDA / ADM family
 -> Plebanski-Urbantke / Regge-EH cross-checks
 -> exact reduced TT propagator
 -> exact higher-shell Peter-Weyl Lambda
 -> recursive TT RG
 -> eta_2^IR and zeta_4^IR
 -> one scale calibration
 -> preregistered external prediction
 -> blind comparison with experiment
```

Параллельная orientation/mirror ветвь:

```text
logical Y_L / oriented volume Q
 -> chi = +/-1
 -> dual Q4 mirror order on the 16-cell
 -> staggered Sigma = +/-1
 -> coarse sigma(x)
 -> positive-kinetic mirror mediator candidate
 -> orientation-dependent fifth force
```

Главное правило проекта:

> **структурное совпадение, finite gate и физическое предсказание — три разных уровня доказательности.**

---

# 1. Как бинарность выбирает локальную геометрию

Пусть локальный переход содержит `q` независимых бинарных различий. Число route-состояний равно

\[
2^q.
\]

Route-вершина связана с `q` соседними routes и двумя полюсами, поэтому её степень

\[
q+2.
\]

Локальная однородность требует

\[
q+2=2^q.
\]

Для целых `q >= 1` единственное решение:

\[
\boxed{q=2}.
\]

Тогда routes

```text
00, 01, 10, 11
```

образуют `C4`, а добавление двух полюсов даёт октаэдральный граф. Его simplicial surface имеет

```text
V=6, E=12, F=8, chi=2
```

и потому является `S2` — правильной vertex link для внутренней точки 3-manifold.

Это первая нетривиальная стрелка:

```text
binary local rule -> S2 link
```

без заранее заданной координатной сетки.

---

# 2. Глобальное трёхмерное пространство

Каноническая minimal+flag globalization — boundary четырёхмерного cross-polytope, то есть 16-cell:

```text
(V,E,F,T) = (8,24,32,16)
Betti     = (1,0,0,1)
```

У каждой вершины ровно одна antipodal вершина, поэтому 1-skeleton равен

```text
K8 minus 4 antipodal edges.
```

Flag closure выбирает по одной вершине из каждой antipodal pair, следовательно число tetrahedra

\[
2^4=16.
\]

Recursive PL gates проверяют:

- vertex/edge/face links;
- orientability;
- two-sided triangle incidence;
- `boundary^2=0`;
- homology;
- сохранение manifold structure при refinement.

В доказанном scope minimal 8-vertex flag completion уникальна с точностью до relabeling. Произвольная nonflag bare-causal globalization отдельно не объявляется уникальной.

---

# 3. Размерность и релятивистский scaling

Независимые finite/held-out observables дают

\[
\boxed{d_H=2.999229782},
\]

\[
\boxed{d_s^{slice}=3.004393867},
\]

а динамический показатель

\[
\boxed{z=0.998281156}.
\]

Для history geometry получено

\[
\boxed{d_s^{history}\simeq4.004393867}.
\]

То есть frozen chain имеет вид

```text
S2 local link
 -> recursive S3-like spatial phase
 -> d_space ~ 3
 -> z ~ 1
 -> 3+1-like history
```

Это не означает, что bare binary reconvergence автоматически создаёт четыре измерения. В dimension-blind negative control минимальная reconvergence-модель давала примерно двухмерную структуру. Четырёхмерность требует общей геометрической/двухформенной фазы, а не одного факта бинарности.

---

# 4. Почему дискретная геометрия выглядит гладкой

Observer/coarse-graining gates дают

```text
delta g       ~ b^-2.001707
grad(delta g) ~ b^-3.001458
delta R       ~ b^-4.000524
simplicity    ~ b^-1.994838
Urbantke g    ~ b^-2.019746
```

Эти показатели относятся к **сглаживанию/дефектам реконструкции**.

Ранее была предложена условная интерпретация

```text
delta g_RMS ~ R^-2.001707
=> P(k) ~ k^+1.003414.
```

Она больше **не является актуальным quantum-vacuum prediction**.

Прямой reduced TT Gaussian calculation даёт точную equal-time covariance

\[
C(\mathbf k)
=\frac{1}{Z_T\Omega_{\mathbf k}\sqrt{\Omega_{\mathbf k}^2+4}},
\]

где

\[
\Omega_{\mathbf k}^2
=r^2\sum_i4\sin^2\frac{k_i}{2},
\qquad r=1/\sqrt3.
\]

При `k -> 0`

\[
\boxed{C(k)\sim\frac{1}{2Z_Tr|k|}},
\]

следовательно

\[
\boxed{P_{TT}(k)\propto k^{-1}}.
\]

Numerical slope:

```text
n_TT = -1.000000148
```

а closed-form и независимое numerical frequency integration совпадают с relative error ниже `2.1e-16`.

Итак:

```text
observer smoothing exponent       p = 2.001707      retained
old foam inference                n = +1.003414     rejected as TT vacuum
explicit reduced TT vacuum        n = -1            exact for reduced Gaussian kernel
full interacting history vacuum   open
```

---

# 5. От qubits к SU(2) квантовой геометрии

Face/link sectors используют Peter–Weyl/SU(2) representation theory, flux operators, intertwiners и volume operator.

Ключевые объекты:

```text
E / flux
V
H_E
K = [V,H_E]
C(V)=h[h^-1,V]
C(K)=h[h^-1,K]
H_L
```

Finite gates проверяют gauge covariance, Gauss sector, recoupling, support walls и regulator-safe cutoff ladders.

Четыре `spin-1/2` qubits разлагаются как

\[
(1/2)^4=2\times j=0+3\times j=1+1\times j=2.
\]

Следовательно в 16-dimensional Hilbert space имеется **ровно один `j=2` irrep**.

Для massless spin-2 TT reduction остаются две helicity:

```text
h=+2
h=-2
```

то есть polarization space является logical qubit, тогда как полная bosonic mode space остаётся Fock-space × helicity-space.

---

# 6. Plebanski / Urbantke bridge и независимый Regge route

Gravity programme имеет две downstream ветви.

Первая:

```text
B^i
 -> simplicity
 -> Urbantke metric
 -> compatible connection
 -> curvature
 -> Einstein criterion
```

Вторая:

```text
metric
 -> Regge
 -> Fierz-Pauli quadratic kernel
 -> Einstein-Hilbert cubic structure
 -> nonlinear Ward restoration
```

Single-data-path positive control на Euclidean `S4` восстанавливает curvature scale с относительной ошибкой порядка `3.4e-8`, тогда как smooth non-Einstein negative control отделяется по ASD criterion примерно на восемь порядков.

Regge family показывает примерно `O(a^2)` approach к GR по нескольким независимым observable families.

Важно: эти ветви являются сильными consistency/universality tests, но не заменяют physical scale setting.

---

# 7. Lorentzian Hamiltonian и beta cancellation

Для real Ashtekar–Barbero variables

\[
A_a^i=\Gamma_a^i+\beta K_a^i.
\]

Derivative-free kinetic pieces удовлетворяют

\[
H_E^{kin}=-\beta^2Q_{DW},
\]

\[
H_L^{corr}=(1+\beta^2)Q_{DW},
\]

поэтому

\[
\boxed{H_E^{kin}+H_L^{corr}=Q_{DW}}.
\]

Это classical control: он фиксирует правильное сочетание Euclidean/Lorentzian terms, но сам по себе не доказывает quantum beta-independence.

Для all-`j=1/2` input полный Lorentzian HH support безопасен в объявленном проходе при

```text
Jmax = 13/2.
```

---

# 8. HDA — главный structural gravity test

Целевая algebra:

\[
[\hat H[N],\hat H[M]]
\rightarrow
i\hbar\hat D[\sharp(NdM-MdN)].
\]

Route-normal sector строит `sharp(N dM-M dN)` независимо через cochain/Hodge/flux map.

Для frozen habitat используются scalings

```text
N = Nbar + epsilon*n
M = Mbar + epsilon*m
Omega_Q = epsilon^-1 OmegaTilde_Q.
```

Получено

```text
C_cross = O(1)
C_GG    = O(epsilon)
D       = O(epsilon^-1)
```

и потому

```text
C_cross/D = O(epsilon)
C_GG/D    = O(epsilon^2).
```

То есть

\[
\boxed{
\Delta_{full}
\le
\Delta_{route}
+C_1\epsilon
+C_2\epsilon^2
\to0
}
\]

в заявленном fixed-cutoff scope.

При simultaneous cutoff growth существует admissible family

\[
\boxed{J_{max}=o(\epsilon^{-2/13})},
\]

например `Jmax = epsilon^-1/8`, вдоль которой лишние Lorentzian channels также убывают. Uniform theorem для абсолютно произвольного joint path остаётся open.

---

# 9. Что именно HDA выбирает — и чего она не выбирает

Для локальной ADM-family

\[
H_{A,B,c,\Lambda}[N]
=\int N\left[
A\frac{\pi_{ab}\pi^{ab}-c\pi^2}{\sqrt q}
-B\sqrt q(R-2\Lambda)
\right]
\]

closure даёт

\[
\boxed{c=1/2},
\qquad
\boxed{AB=1}.
\]

То есть DeWitt trace structure и relative kinetic/curvature normalization фиксируются.

Но остаются familiar GR freedoms:

\[
\boxed{G\ \text{и}\ \Lambda}.
\]

Это принципиально: **Newton constant нельзя честно “вытащить из HDA”**, потому что HDA допускает общий gravitational normalization.

---

# 10. Physicalization: оставшаяся одна action-normalization freedom

Growth/composition equations для microscopic phase были пересчитаны как linear system.

Для `M=8`:

```text
matrix shape = 184 x 16
rank         = 15
nullity      = 1
```

Единственное направление ядра совпадает с

\[
\boxed{f(n)=s n}.
\]

Разные slopes

```text
0.1, 0.5, 1, sqrt(2), pi
```

удовлетворяют composition equations с residual ниже `1e-14`.

Следовательно форма фазы фиксирована, но

\[
\boxed{s\ \text{остаётся одним свободным overall slope}}.
\]

Это не десятки fitting parameters. Это **одна абсолютная action/Newton/time normalization freedom**, которую нужно либо вывести из дополнительного microscopic principle, либо объявить единственным scale-setting calibration datum.

---

# 11. Regge TT residue: held-out prediction

Полный Regge metric Hessian даёт intensive coefficient

\[
Z_L=c_1(L)/L^4.
\]

Для `L=3,4,5`:

```text
0.1021131745
0.1114624530
0.1161306996
```

Continuum target от Regge/EH normalization:

\[
\boxed{Z_\infty=1/8=0.125}.
\]

До открытия `L=6` был frozen ansatz

\[
Z_L=\frac18+\frac{C}{L^2}+\frac{D}{L^4},
\]

который дал blind continuation

```text
Z6_pred = 0.11876923193907167
```

После вычисления:

```text
Z6_obs  = 0.11876075461190198
```

Relative prediction error:

\[
\boxed{0.00714\%}.
\]

Это один из наиболее чистых held-out finite-size tests репозитория.

---

# 12. Первый явный connected TT propagator

Frozen reduced causal transfer имеет exact pole

\[
\boxed{
4\sin^2\frac\omega2
=r^2\sum_i4\sin^2\frac{k_i}{2},
\qquad r=1/\sqrt3.
}
\]

Для двух TT polarizations:

\[
\boxed{
G^{TT}_{AB}(\omega,\mathbf k)
=
\frac{\delta_{AB}}
{Z_T\left[
4\sin^2(\omega/2)
-r^2\sum_i4\sin^2(k_i/2)
+i0
\right]}.
}
\]

Это exact reduced propagator. Он ещё **не** считается final full Peter–Weyl/history/RG propagator.

В этом reduced sector pole mass равна нулю:

\[
\boxed{m_g=0}.
\]

---

# 13. Первые dimensionless dispersion coefficients

Small-momentum expansion:

\[
\omega^2
=r^2k^2
+\frac{r^2}{12}
\left[r^2(k^2)^2-\sum_i k_i^4\right]
+O(k^6).
\]

Directional coefficient:

\[
\boxed{
\eta(\hat n)=\frac{r^2-\sum_i n_i^4}{12}.
}
\]

При `r^2=1/3`:

| direction | bare `eta` |
|---|---:|
| `(100)` | `-1/18` |
| `(110)` | `-1/72` |
| `(111)` | `0` |

Разделяем scalar и cubic invariants:

\[
Q_4^{cub}=\sum_i k_i^4-\frac35(k^2)^2.
\]

Получаем

\[
\boxed{\eta_{2,bare}^{iso}=-1/45},
\]

\[
\boxed{\zeta_{4,bare}^{cub}=-1/12}.
\]

Это **bare candidate coefficients**, а не уже измеренные свойства природы.

Решающий вопрос теперь:

\[
\zeta_4^{IR}\to0?
\]

Если да — rotational symmetry восстанавливается и остаётся scalar `eta_2^IR`.

Если нет, но coefficient стабилизируется при RG — модель предсказывает specific cubic anisotropic propagation law.

Если coefficient не сходится или зависит от regulator after extrapolation — physicalization gate fails.

---

# 14. Exact Peter–Weyl higher-shell Lambda

Самый важный новый finite result был полностью досчитан GitHub Actions.

Из spin-parity

\[
P H_E P=0.
\]

Определяем

\[
K=P H_E^2P
\]

и genuine second-shell observable

\[
\boxed{
\Lambda
=K^{-1/2}
\left(PH_E^4P-K^2\right)
K^{-1/2}.
}
\]

Calculation scope:

```text
logical dimension = 32
Jmax second-hit   = 5/2
all 32 columns    = completed
CI gate           = PASS
```

First-return matrix:

```text
rank(K)       = 32
lambda_min(K) = 4.306075987001578
lambda_max(K) = 13.352781352746604
cond(K)       = 3.100916331493829
```

Higher-shell positive matrix

\[
M=PH_E^4P-K^2
\]

имеет

```text
lambda_min(M) = 47.97777674967158
lambda_max(M) = 186.90234422317016
```

и reconstruction error `5.685e-14`.

Для `Lambda`:

\[
\boxed{\lambda_{min}=10.635759878291307},
\]

\[
\boxed{\lambda_{max}=15.059927665966466},
\]

\[
\boxed{\bar\lambda=12.860443113390883},
\]

\[
\boxed{\sigma_\lambda=1.21953176104}.
\]

Spectral ratio:

\[
\boxed{\lambda_{max}/\lambda_{min}=1.41597101084}.
\]

Distance from scalar identity:

\[
\boxed{
\frac{\|\Lambda-\bar\lambda I\|_F}{\|\Lambda\|_F}
=0.09440461833.
}
\]

То есть normalized higher-shell dynamics **не схлопывается в identity**.

После pair partial trace:

```text
shape coupling       = -0.3629900150598623
orientation coupling = +0.7912767588958898
Delta                = +1.1542667739557522
```

Самый большой nonidentity Pauli coefficient:

\[
\boxed{c_{IIIYY}=0.7912767588958898}.
\]

Это означает, что orientation/shape structure переживает first-return normalization и реально присутствует на следующем shell.

Полный certificate:

```text
PETER_WEYL_HIGHER_SHELL_LAMBDA_RESULT.md
```

---

# 15. Block-Lanczos bridge: от finite Hamiltonian к resolvent

Higher-shell calculation имеет прямую block-Lanczos интерпретацию:

\[
B_1^\dagger B_1=K,
\qquad
B_2^\dagger B_2=\Lambda.
\]

Numerical reconstruction errors:

```text
||B1^dag B1-K||      = 1.616e-13
||B2^dag B2-Lambda|| = 1.645e-13
```

Поэтому local logical resolvent естественно продолжается как matrix continued fraction:

\[
G_0(z)=
\left[
 zI-B_1^\dagger
 \left(zI-B_2^\dagger G_2(z)B_2\right)^{-1}
 B_1
\right]^{-1}.
\]

Это важнее, чем ещё одна локальная матрица: появляется точная дорога

```text
finite Peter-Weyl Hamiltonian
 -> shell recursion
 -> resolvent
 -> propagator
 -> pole structure.
```

---

# 16. Physical scale map

Для Regge convention

\[
\frac{S_R}{\hbar}
=\frac{1}{8\pi\ell_P^2}\sum_h A_h\delta_h.
\]

Пусть

\[
A_h=a_*^2\widetilde A_h.
\]

Определяем renormalized coefficient `lambda_R_eff` как coefficient перед

\[
\sum_h\widetilde A_h\delta_h
\]

в `S_eff/hbar`.

Тогда

\[
\boxed{
\lambda_R^{eff}=\frac{a_*^2}{8\pi\ell_P^2}
}
\]

и

\[
\boxed{
\frac{a_*}{\ell_P}=\sqrt{8\pi\lambda_R^{eff}}.
}
\]

Это **scale map**, но не число, пока remaining action slope не выведен или не откалиброван одним datum.

---

# 17. Первый внешний modified-dispersion observable

После full RG, если cubic anisotropy исчезает, пишем

\[
E^2=p^2c^2+A_4p^4c^4+\cdots.
\]

Тогда

\[
\boxed{
A_4
=\frac{\eta_2^{IR}a_*^2}{(\hbar c)^2}
=\frac{8\pi\eta_2^{IR}\lambda_R^{eff}}{E_P^2}.
}
\]

Ключевой anti-overfitting rule:

> `eta_2^IR`, `zeta_4^IR`, regulator sequence, fit window и uncertainty должны быть committed **до** открытия выбранного external posterior.

Это уже formalized в

```text
TT_RG_PHYSICAL_PREDICTION_PREREGISTRATION.md
```

---

# 18. Что теория уже может и чего пока не может предсказывать

| Observable | Current status |
|---|---|
| `q=2` | exact binary selector |
| local `S2` link | exact combinatorial result |
| minimal flag `S3` globalization | finite/exact in declared semantics |
| `d_H ~ 3` | held-out numerical result |
| `d_s(slice) ~ 3` | numerical spectral result |
| `z ~ 1` | frozen dynamical result |
| `d_s(history) ~ 4` | derived history scaling |
| DeWitt `c=1/2` | selected by HDA |
| `AB=1` | selected by HDA |
| TT helicities | structural continuum result |
| reduced `m_g=0` | exact reduced pole |
| Regge `Z_TT -> 1/8` | held-out L=6 PASS |
| reduced `P_TT(k) ~ k^-1` | exact Gaussian result |
| `eta_2,bare^iso=-1/45` | exact reduced bare coefficient |
| `zeta_4,bare=-1/12` | exact reduced bare coefficient |
| exact 32D higher-shell `Lambda` | finite CI PASS |
| `G` | one remaining common normalization / scale datum |
| cosmological `Lambda` | not derived |
| `alpha_EM` | not derived |
| electron/muon/tau masses | not derived |
| quark masses | not derived |
| `m_W,m_Z,m_H` | not derived |
| three generations | not derived |
| Yukawa matrices | not derived |

---

# 19. Почему нельзя сейчас «получить 137» или массы частиц

Текущий matter file является Wilson–Dirac carrier, а не Standard Model derivation.

В нём ещё открыты:

```text
realistic gauge group
chiral spectrum
three generations
Higgs/Yukawa sector
anomaly completion
first-principles matter coupling normalization
```

Поэтому поиск чисел вроде

```text
137.036
206.768...
3477...
```

среди комбинаций `32`, `1/8`, `1/45` или eigenvalues `Lambda` был бы post-hoc numerology.

Есть даже полезный negative result: full higher-shell spectrum имеет dynamic range всего

\[
\frac{\lambda_{max}}{\lambda_{min}}\approx1.416,
\]

поэтому простое

```text
mass_i proportional to lambda_i
```

или

```text
mass_i proportional to sqrt(lambda_i)
```

не может объяснить огромную charged-lepton hierarchy.

Matter programme должен идти в правильном порядке:

```text
microscopic algebra
 -> physical gauge group
 -> chiral representations
 -> generations
 -> symmetry breaking / Yukawa operator
 -> mass matrix
 -> eigenvalue ratios
 -> only then compare to particle masses.
```

---

# 20. Mirror / chirality sector — отдельная ветвь, не подмена gravity prediction

В logical singlet geometry sector

\[
Q=\frac{\sqrt3}{4}Y_L.
\]

Complex conjugation меняет

```text
X_L -> +X_L
Z_L -> +Z_L
Y_L -> -Y_L
Q   -> -Q
```

при сохранении metric/absolute-volume data.

Следовательно

```text
mirror orientation != negative gravitational mass.
```

Direct `H -> -H` лишь меняет time/normal orientation, а negative Einstein-Hilbert coefficient создаёт ghost tensor sector.

На dual graph минимального 16-cell tetrahedra образуют `Q4`, и staggered variable

\[
\Sigma=\frac1{16}\sum_v\eta_vY_v
\]

имеет две mirror branches `Sigma=+/-1`.

Finite 16-qubit transverse-field gate показывает strong order при `h/J=0.2`:

```text
<Sigma^2> = 0.9976539474
<|Sigma|> = 0.9987478253
```

и destruction of order при `h/J=4`:

```text
<Sigma^2> = 0.1462741385.
```

Positive-kinetic continuum extension допускает orientation-dependent Yukawa fifth force с threshold

\[
\boxed{
\alpha_{crit}(x)=\frac{e^x}{1+x},
\qquad x=m_\phi r.
}
\]

Это **healthy mirror-force candidate**, а не доказанная антигравитация и не обычная antimatter gravity.

---

# 21. Три класса результатов

## Exact / algebraic

- `q=2` selector;
- octahedral `S2` shell;
- SU(2) representation identities;
- unique `j=2` in four spin-1/2 qubits;
- mirror parity of `X,Y,Z,Q`;
- HDA parameter selection `c=1/2`, `AB=1` within stated ADM ansatz;
- reduced TT pole formula;
- reduced vacuum `P_TT(k)~k^-1`;
- bare quartic tensor decomposition;
- exact definition of higher-shell `Lambda` and block-Lanczos identities.

## Tested finite / held-out

- recursive PL manifold gates;
- dimension/scaling gates;
- two-node and multi-node Peter–Weyl/HDA regressions;
- Regge/Fierz-Pauli/EH scaling;
- held-out `Z_6` continuation with `0.00714%` relative error;
- exact 32-column higher-shell CI assembly;
- mirror-order `2^16` diagonalization;
- canonical mirror matter-HDA identity.

## Conditional / physical frontier

- full Peter–Weyl/history/RG TT propagator;
- final `eta_2^IR`, `zeta_4^IR`;
- absolute `lambda_R_eff` from first principles;
- external `A_4` blind prediction;
- interacting quantum-vacuum exponent;
- physical infoton mode/coupling;
- Standard-Model gauge/matter derivation;
- particle masses and fundamental gauge couplings;
- physical mirror mediator coupling/range.

---

# 22. Решающий следующий расчёт

После завершённой local higher-shell `Lambda` следующий bottleneck один:

\[
\boxed{
\Lambda_{local}
\rightarrow
\text{recursive PL/Peter--Weyl blocking}
\rightarrow
K_{RG}^{TT}(\omega,\mathbf k)
\rightarrow
\eta_2^{IR},\zeta_4^{IR}.
}
\]

Preregistered outcomes:

### A. Rotational restoration

\[
\zeta_4^{IR}\to0,
\qquad
\eta_2^{IR}\to\eta_2^*.
\]

Тогда first external prediction — scalar quartic modified dispersion.

### B. Cubic fixed point

\[
\zeta_4^{IR}\to\zeta_4^*\neq0.
\]

Тогда более сильное prediction — directional gravitational propagation tensor.

### C. Failure

Если coefficients:

- не стабилизируются;
- требуют retuning;
- зависят от arbitrary regulator после continuum extrapolation;
- создают ghost/tachyon TT pole;

то physicalization branch получает `FAIL`, даже если прежние finite HDA gates остаются корректными в своём scope.

Это и есть нормальная falsifiability.

---

# 23. Anti-overfitting protocol

Перед external comparison должны быть committed:

```text
microscopic commit SHA
operator ordering
regulator sequence
blocking prescription
momentum directions
fit window
c_TT(b)
eta2_iso(b)
zeta4_cub(b)
continuum extrapolation
finite-size/RG uncertainty
lambda_R_eff
A4 or directional tensor
PASS / TENSION / FAIL rule
```

После этого запрещено менять coefficient из-за того, что experiment posterior оказался неудобным.

Repository уже использовал такую дисциплину в held-out Regge continuation; physical prediction должен использовать тот же принцип.

---

# 24. Что считать успехом проекта

Не достаточно получить ещё один красивый finite overlap.

Минимальный физический success criterion:

```text
ONE frozen microscopic rule
 -> common scaling phase
 -> anomaly-safe HDA/GR sector
 -> full TT propagator
 -> one dimensionless coefficient not used in calibration
 -> physical scale from one declared datum or internal derivation
 -> preregistered external observable
 -> blind comparison
 -> survives without retuning.
```

После этого имеет смысл говорить, что candidate architecture стала **физически проверенной в одном канале**.

Для претензии на более полную fundamental theory дополнительно потребуются realistic matter/gauge sector и независимая replication.

---

# 25. Основные документы

## Gravity / geometry

- `THEORY_STATUS.md` — канонический human-readable ledger;
- `theory_gates.json` — machine-readable gate ledger;
- `FINAL_CORE_ARCHITECTURE_CERTIFICATE.md` — fixed-cutoff HDA architecture;
- `ALL_ARROWS_GRAVITY_CERTIFICATE.md` — composed gravity arrows and scope;
- `GLOBAL_MANIFOLD_Q2_COMPLETION.md` — global q=2 PL completion;
- `SPATIAL_QUBIT_GEOMETRY_BRIDGE.md` — face-qubit geometry bridge;
- `PLEBANSKI_URBANTKE_BRIDGE.md` — simple B → metric;
- `PLEBANSKI_CONNECTION_EINSTEIN_GATE.md` — connection/curvature → Einstein criterion;
- `REGGE_EH_CUBIC_BRIDGE.md` — independent Regge/EH branch;
- `ADM_HDA_PARAMETER_SELECTION.md` — HDA selection of ADM parameters;
- `LORENTZIAN_BETA_CANCELLATION.md` — kinetic beta-cancellation control.

## Physicalization / propagator

- `PHYSICALIZATION_SCALE_OBSERVABLE_PREDICTION.md` — scale → observable → blind prediction programme;
- `PHYSICALIZATION_PASS_01_RESULTS.md` — first quantitative pass;
- `TT_PROPAGATOR_FIRST_PASS.md` — exact reduced TT propagator;
- `TT_VACUUM_TWO_POINT_RESULT.md` — exact reduced TT vacuum spectrum and smoothing negative control;
- `TT_REGGE_ZT_L6_PREREGISTRATION.md` — held-out L=6 preregistration;
- `TT_REGGE_ZT_L6_RESULT.md` — held-out residue result;
- `PETER_WEYL_HIGHER_SHELL_LAMBDA_RESULT.md` — exact completed 32D higher-shell result;
- `TT_RG_PHYSICAL_PREDICTION_PREREGISTRATION.md` — next recursive RG killer gate.

## Mirror / matter support

- `MIRROR_CHIRALITY_GRAVITY.md`;
- `MICROSCOPIC_MIRROR_ORDER.md`;
- `ORIENTATION_ODD_HDA_CONSTRUCTION.md`;
- `MIRROR_WILSON_MATTER.md`.

---

# 26. Основные воспроизводимые команды

Canonical status:

```bash
python bcqg_bit_to_gravity_final.py --strict
```

Unified verification:

```bash
python bcqg_unified_verification.py
```

Reduced TT propagator:

```bash
python scripts/tt_propagator_first_pass.py
```

Reduced TT vacuum two-point function:

```bash
python scripts/tt_vacuum_two_point_gate.py
```

Regge held-out residue:

```bash
python scripts/tt_regge_zt_l6_gate.py
```

Higher-shell Peter–Weyl columns:

```bash
python scripts/peter_weyl_higher_shell_lambda_gate.py \
  --column 0 \
  --output verification_results/columns/column_0.json
```

Assembly after all 32 columns:

```bash
python scripts/peter_weyl_higher_shell_lambda_gate.py \
  --assemble-dir verification_results/columns \
  --output verification_results/PETER_WEYL_HIGHER_SHELL_LAMBDA.json
```

Physical scale bridge:

```bash
python scripts/physical_scale_prediction_bridge.py --help
```

Mirror/chirality:

```bash
python scripts/mirror_chirality_gravity_gate.py \
  --trials 256 \
  --output verification_results/MIRROR_CHIRALITY_GRAVITY.json
```

Microscopic mirror order:

```bash
python scripts/mirror_order_16cell_gate.py \
  --output verification_results/MIRROR_ORDER_16CELL.json
```

---

# 27. Короткий scientific status

Наиболее сильная корректная формулировка проекта сейчас:

> **Binary Causal / Information-Graph Quantum Gravity — это кандидатная квантово-гравитационная архитектура, в которой бинарная route-комбинаторика выбирает q=2, формирует локальную S2 link и minimal flag S3-like PL globalization; независимые scaling gates дают 3D spatial и z≈1/4D-like history behaviour; SU(2)/Peter–Weyl sector содержит контролируемую quantum geometry и spin-2 TT channel; HDA выбирает GR/ADM tensor structure up to the familiar overall gravitational normalization and cosmological term; independent Regge/Plebanski branches reproduce Einstein structures in their tested scope. Physicalization pass уже дал held-out TT residue, exact reduced massless TT propagator, exact reduced vacuum `P(k)~k^-1`, bare quartic coefficients и completed non-scalar 32D higher-shell Lambda. Следующий falsifiable bottleneck — recursive TT RG, freezing `eta_2^IR`/`zeta_4^IR`, one-scale normalization и blind external comparison. Standard-Model couplings and particle masses пока не являются derived outputs.**

Если

```text
core_candidate_architecture_closed: true
```

это означает закрытие **заявленного математического/finite scope**, а не доказательство окончательной теории природы.
