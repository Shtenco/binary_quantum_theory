# От бита пространства-времени к геометрии, гравитации, свету и реальному эксперименту

## Большая научная сказка-путешествие — от дискретной микроструктуры к гладкому миру наблюдателя

> **Канонический статус: 21 августа 2026. Candidate theory.**
>
> Этот репозиторий не объявляет «теорию всего» доказанной. Он строит длинную вычислимую цепочку, в которой исходный объект не является заранее заданным пространством, метрикой или четырёхмерной решёткой. Стартовая гипотеза намного беднее: существуют локальные бинарные различия и причинные маршруты. Дальше геометрия, размерность, гладкость, spin-2, constraint algebra, physical projector, свет и наблюдаемые должны появиться как последовательно проверяемые уровни описания.
>
> Главный принцип проекта: **красивое совпадение не становится физическим предсказанием, пока между объектами не построен явный мост.** Поэтому здесь сохраняются positive results, negative controls, no-go theorems, исправления прежних интерпретаций и открытые bottlenecks.

---

## Как читать репозиторий

- **README.md** — главная научная книга-путешествие: максимально человеческое объяснение, но с формулами и строгими границами claims.
- **CANONICAL_THEORY_PACKAGE.md** — сухой evidence index без литературной части.
- **BIT_TO_SPACETIME_CENTRAL_EQUATION.md** — центральная техническая цепь `binary microstructure -> smooth spacetime`.
- **OBSERVER_SCALE_SMOOTHING.md** — finite observer/coarse-graining gate.
- **GLOBAL_MANIFOLD_Q2_COMPLETION.md** — локальная `S2` и глобальная PL `S3` completion.
- **MICRO_WALSH_QGEOM_BRIDGE.md** — exact bridge `Z2^2 route labels -> tetrahedral flux frame -> face qubits`.
- **LOGICAL_SHAPE_METRIC_JACOBIAN.md** — exact shape-to-metric Jacobian.
- **THEORY_STATUS.md** — human-readable status ledger.
- **theory_gates.json** и physicalization ledgers — machine-readable truth surface.
- **PREDICTIONS_AND_EXPERIMENTAL_TESTS.md** — внешний слой проверок.

Исторические README не потеряны:

- [подробный урок 14 августа 2026](docs/archive/README_LESSON_2026-08-14.md);
- [исходная научная сказка 17 августа 2026](docs/archive/README_STORY_2026-08-17.md);
- [42-главная physicalization-версия 21 августа](docs/archive/README_STORY_2026-08-21_v42.md).

Нынешний README объединяет их сильнейшие объяснения и сохраняет более поздние научные коррекции.

### Ярлыки доказательности

- **EXACT** — алгебраический или комбинаторный результат в явно заявленных предпосылках.
- **CI / FINITE PASS** — воспроизводимый конечномерный computation.
- **HELD-OUT** — prediction была frozen до открытия проверочного результата.
- **CONDITIONAL** — вывод зависит от явно записанной дополнительной физической гипотезы.
- **OPEN PHYSICAL** — математический объект определён, но physical bridge или microscopic number ещё не получен.
- **NO-GO** — доказано, что привлекательный shortcut не работает.

---

# Пролог. Вселенная, у которой сначала нет ни координат, ни гладкой стены

Представьте, что нам запрещено начинать с `x,y,z`.

Нет метров.

Нет линейки.

Нет гладкой координатной сетки.

Нет заранее выбранной размерности.

Нет готовой метрики `g_mu_nu`.

Нет света.

Нет частиц.

Нет даже обещания, что понятие «расстояние» на самом глубоком уровне уже существует в привычном смысле.

Есть только **различимость**: локальное событие может различать несколько альтернатив, а причинный переход может иметь несколько маршрутов.

Самая маленькая такая различимость бинарна:

```text
0  или  1
```

Но это очень важно понимать правильно.

В этой программе «бит пространства-времени» — **не маленький классический кубик пространства**, который уже лежит где-то внутри готовой трёхмерной коробки. Если бы мы начали с таких кубиков, пространство было бы вставлено в модель заранее.

Бит здесь — минимальная локальная степень различимости. Только после того как множество таких различий образует устойчивые отношения, появляются объекты, которые можно интерпретировать как направления, площади, объёмы, соседство, метрику и пространство.

Поэтому главная дорога проекта выглядит так:

```text
binary distinction
 -> local route algebra
 -> q = 2
 -> octahedral S2 link
 -> Z2^2 Walsh characters
 -> regular tetrahedral flux frame
 -> face qubits / geometry qubit
 -> globally glued PL S3
 -> exact causal-volume d* = 3
 -> z ~ 1
 -> 3+1-like history
 -> observer coarse graining
 -> discrete rough microgeometry becomes smooth IR geometry
 -> quantum geometric tensor
      Re Q -> distinguishability / geometry
      Im Q -> Berry / Hopf phase
 -> SU(2) quantum geometry + compact U(1) phase
 -> spin-2 carrier
 -> logical shape -> metric
 -> Peter-Weyl constraint dynamics
 -> Lorentzian completion + HDA/ADM
 -> physical projector
 -> relational / boundary time
 -> physical history generating functional
 -> 1PI effective action Gamma[g,A,...]
 -> graviton and photon physical kernels
 -> S4 -> SO(3) -> Lorentz universality
 -> G, Lambda, Z_A
 -> pole observables + connected fluctuations
 -> blind experiment
```

У этой истории есть важная особенность: несколько раз она сама запрещает нам слишком лёгкий финал. Именно это делает её научной.

---

# Часть I. Как бинарное различие начинает становиться геометрией

# Глава 1. Один бит ещё ничего не знает о пространстве

Один бит различает два состояния. Он не знает, что такое «слева», «справа», «рядом», «далеко», «угол» или «объём».

Поэтому первый вопрос проекта не «какова метрика?», а гораздо более фундаментальный:

> сколько независимых бинарных различий должен содержать локальный причинный переход, чтобы все его route states могли быть локально однородными?

Пусть таких независимых binary labels `q`.

Тогда число маршрутов

$$
2^q.
$$

Пока это чистая комбинаторика. Геометрии ещё нет.

---

# Глава 2. Почему локальная однородность сама выбирает q = 2

**[EXACT]**

Каждый route state отличается ровно одним битом от `q` Hamming-neighbours и связан ещё с двумя causal poles. Его degree равен

$$
q+2.
$$

Каждый causal pole связан со всеми route states, то есть имеет degree

$$
2^q.
$$

Если потребовать минимальную локальную однородность — одинаковую valence у этих двух типов вершин — получаем

$$
q+2=2^q.
$$

Для целых `q>=1` единственное решение

$$
q=2.
$$

Проверка почти школьная:

```text
q=1: 3 != 2
q=2: 4  = 4
q=3: 5 != 8
q=4: 6 != 16
...
```

После `q=2` экспонента `2^q` растёт быстрее линейной части, поэтому новых пересечений нет.

Это первая точка, где число появляется **не как fitted parameter**, а как следствие локального правила.

Получаются четыре route labels:

```text
00  01  10  11
```

и их Hamming graph

```text
Q2 = C4.
```

---

# Глава 3. Четыре бинарных маршрута строят сферу вокруг точки

**[EXACT]**

Добавим к `C4` два causal endpoints. Получается suspension

$$
Sigma(C4),
$$

то есть combinatorial graph октаэдра.

Его simplicial surface имеет

```text
V = 6
E = 12
F = 8
chi = 2
```

и является

$$
S^2.
$$

Почему это важнее, чем просто красивый многогранник?

В обычном трёхмерном PL-manifold маленькая link-sphere вокруг внутренней точки должна быть двумерной сферой:

$$
Link(v) = S^2.
$$

То есть локальный binary route object приобретает **ровно тот topology precursor, который нужен внутренней точке трёхмерного пространства**.

Это ещё не доказательство глобального пространства. Но это уже не произвольный граф.

Есть и полезная combinatorial связь: octahedral graph является line graph тетраэдра `K4`. Его шесть вершин можно читать как шесть рёбер tetrahedron. Поэтому route shell и minimal tetrahedral geometry встречаются уже на уровне одной и той же шестисостоянийной структуры.

---

# Глава 4. Биты получают направления: exact Walsh bridge

**[EXACT]**

Вот одна из самых важных стрелок, которая в коротких README раньше почти исчезла.

Четыре route labels при `q=2` — это элементы группы

$$
G=Z_2^2={00,01,10,11}.
$$

У `Z2^2` есть ровно три нетривиальных real Walsh characters. Используем их как координаты:

$$
Phi(g) = (chi_01(g), chi_10(g), chi_11(g))/sqrt(3).
$$

Character orthogonality даёт точно

$$
sum_g Phi(g)=0,
$$

а для разных labels

$$
Phi(g) dot Phi(h)=-1/3.
$$

У каждого вектора norm равна единице.

Но четыре единичных вектора в `R3`, сумма которых равна нулю и все взаимные скалярные произведения равны `-1/3`, — это именно четыре нормали правильного тетраэдра.

Итак:

```text
00,01,10,11
 -> three nontrivial Walsh characters
 -> four vectors in R3
 -> exact regular tetrahedral frame
```

Никакого target angle `arccos(-1/3)` мы не подгоняем. Он получается из character orthogonality.

Это сильнее фразы «qubit имеет три Pauli components». Здесь конкретные binary route labels сами дают конкретную regular tetrahedral geometry carrier.

Подробнее: `MICRO_WALSH_QGEOM_BRIDGE.md`.

---

# Глава 5. Когда направление становится квантовым face flux

Для каждого derived unit normal `n_f` вводится pure face-qubit state

$$
rho_f = (I + n_f^i sigma_i)/2.
$$

Bloch vector теперь не выбирается из continuum вручную: он уже пришёл из `Z2^2` Walsh map.

Четыре face fluxes regular tetrahedron удовлетворяют closure:

$$
sum_f E_f = 0.
$$

В finite gate получено:

```text
flux closure norm                  = 0
regular tetrahedron Gram error     < 1e-14
Gauss-singlet weight               = 2/9
logical oriented volume            = sqrt(3)/4
reconstructed edge relative spread = 0
```

Это и есть точка, где фраза «бит пространства» начинает приобретать буквальный geometric content:

```text
binary label
 -> direction
 -> face flux
 -> quantum face state
 -> closed tetrahedral quantum geometry
```

Но всё ещё нельзя говорить, что один qubit сам по себе «является метром пространства». Геометрия возникает из **отношений между несколькими carriers**.

---

# Глава 6. Четыре face qubits дают один gauge-invariant geometry qubit

**[EXACT FINITE REPRESENTATION THEORY]**

Четыре spin-1/2 раскладываются как

$$
(1/2)^4 = 2 x j=0 + 3 x j=1 + 1 x j=2.
$$

Gauss-invariant singlet sector имеет dimension two.

То есть

```text
4 face qubits
 -> impose total SU(2) Gauss closure
 -> 2D invariant Hilbert space
 -> one logical geometry qubit
```

Это другой объект, чем unique collective `j=2` sector, который позже будет использоваться как spin-2 carrier. Важно не смешивать их:

- `j=0` multiplicity-two sector кодирует intrinsic tetrahedral geometry;
- unique `j=2` sector — отдельный collective spin-2 representation channel.

В natural singlet basis logical Pauli operators имеют geometric meaning. Например,

```text
Z_L, X_L -> independent shape/dihedral observables
Y_L      -> oriented volume pseudoscalar
```

и exact oriented-volume eigenvalues равны

$$
+sqrt(3)/4, -sqrt(3)/4.
$$

Таким образом «geometry qubit» — не поэтическое название. Его Bloch sphere параметризует конкретные gauge-invariant shape/orientation observables.

---

# Глава 7. Из face fluxes можно восстановить настоящий тетраэдр

Пусть `a,b,c` — три edge vectors из одной вершины тетраэдра, а oriented face-area vectors

$$
E_1=(b x c)/2,
$$

$$
E_2=(c x a)/2,
$$

$$
E_3=(a x b)/2.
$$

Соберём

$$
C=(2E_1,2E_2,2E_3).
$$

Тогда

$$
C = det(A) A^{-T},
$$

где `A=(a,b,c)`, и поэтому

$$
A = sqrt(|det C|) C^{-T}.
$$

Finite control реконструирует non-degenerate tetrahedra до machine precision.

Это даёт прямой смысл цепочке

```text
quantum flux expectations
 -> face normals / areas
 -> edge geometry
 -> intrinsic metric data
```

и одновременно даёт falsifier: если closure или shape matching не сходятся при blocking, набор quantum polyhedra нельзя называть одним smooth space.

---

# Глава 8. Почему склеивание клеток важнее самих клеток

Один идеальный тетраэдр — ещё не пространство.

Нужно, чтобы соседние cells согласовали общую грань. Площадь и normal недостаточны: два triangles могут иметь одинаковую площадь и нормаль, но разную intrinsic shape. Это известная опасность twisted geometry.

Поэтому проект отслеживает минимум два дефекта:

```text
closure defect -> 0
shape mismatch -> 0
```

Старый independent Bell-gluing control показал, что для двух logical geometry qubits состояние `Phi+` имеет корреляции

```text
<X X> = +1
<Z Z> = +1
<Y Y> = -1
```

то есть intrinsic shape совпадает, а orientation/normal разворачивается на общей face, как и должно быть у outward normals соседних cells.

В современной canonical q=2 global gluing ветке используется ещё более жёсткая combinatorial проверка: обе incident tetrahedra получают один и тот же q=2 face label, соседние cells отличаются одним sign bit, а outward Walsh fluxes сокращаются на каждой shared face.

---

# Часть II. Как локальные геометрии становятся пространством

# Глава 9. Локальная S2 ещё не глобальная Вселенная

Чтобы говорить о spatial manifold, надо склеить local cells без края и singular seams.

Canonical minimal+flag globalization q=2 shell — boundary четырёхмерного cross-polytope, то есть 16-cell:

```text
(V,E,F,T) = (8,24,32,16)
Betti     = (1,0,0,1)
```

У него:

```text
vertex links   = S2
edge links     = S1
triangle links = S0
```

каждый triangle two-sided, complex orientable и `boundary^2=0`.

Следовательно в canonical completion

$$
M^3 = S^3.
$$

Это глобальный closed spatial manifold, а не просто набор несвязанных tetrahedra.

---

# Глава 10. Почему minimal+flag completion ведёт именно к 16-cell

В старой подробной версии README был красивый короткий argument, который стоит сохранить.

Предположим declared semantics:

```text
minimal 8 vertices
+ every vertex link is octahedral S2
+ flag/clique closure
```

У каждой вершины среди остальных семи должно быть ровно шесть neighbours, потому что octahedral vertex link имеет шесть vertices.

Значит у каждой вершины есть ровно один antipode, с которым edge отсутствует.

Граф missing edges — четыре disjoint pairs:

```text
4 antipodal pairs.
```

Следовательно 1-skeleton

```text
K8 minus 4 antipodal edges.
```

Flag tetrahedron выбирает ровно по одной вершине из каждой antipodal pair. Таких choices

$$
2^4=16.
$$

Получается exactly boundary 16-cell.

**Scope:** это uniqueness в minimal eight-vertex flag semantics. Это не доказательство уникальности любого nonflag global causal gluing.

---

# Глава 11. Пространство выдерживает refinement

Barycentric refinement даёт

```text
g=0: 16 tetrahedra
g=1: 384 tetrahedra
g=2: 9216 tetrahedra
```

и executable gate заново проверяет simplex links, хотя PL topology already guarantees homeomorphism.

На проверенных уровнях:

```text
bad vertex links = 0
bad edge links   = 0
bad face links   = 0
boundary^2       = 0
orientable       = true
all faces        = two-sided
```

То есть пространство не «рассыпается» при subdivision.

Это важная разница между красивой seed картинкой и recursive spatial phase.

---

# Глава 12. Геометрия и топология — не одно и то же

Topology отвечает на вопрос «как всё склеено».

Metric geometry отвечает на вопросы «какие длины, углы, площади и объёмы».

Dimension отвечает на вопрос «как растёт число доступных состояний с масштабом».

Dynamics отвечает на вопрос «как spatial state меняется и как появляется causal time».

Поэтому в проекте специально не используется аргумент вида

```text
S3 topology -> therefore physical 3+1 GR.
```

Нужны независимые dimension и dynamics gates.

---

# Часть III. Почему пространство оказывается трёхмерным, а история — 3+1-like

# Глава 13. Exact causal-volume fixed point равен трём

При `q=2` число route midpoints `B=2^q=4`. Каждый active causal edge при следующем rewrite создаёт восемь active child edges, а causal linear scale удваивается.

Exact vertex count после `g` generations:

$$
N_g=(4*8^g+10)/7.
$$

One-step causal-volume exponent

$$
d_g=log_2(N_g/N_{g-1})
$$

имеет closed form

$$
d_g=3+log_2(1-35/(16*8^(g-1)+40)).
$$

Отсюда exactly:

```text
d_g < 3
d_{g+1} > d_g
d_g -> 3
```

и потому

$$
d_* = 3.
$$

Последовательность:

```text
g=2  2.6629650127
g=3  2.9517448314
g=4  2.9938530157
g=5  2.9992297821
g=6  2.9999036938
g=7  2.9999879613
g=8  2.9999984952
```

Исторический `d_H=2.999229782...` оказался просто `g=5` point exact monotone sequence.

---

# Глава 14. Почему одного «почти 3» было бы недостаточно

Есть несколько независимых witnesses:

```text
local topology:           S2 vertex link -> 3-manifold precursor
canonical global phase:   S3
causal-volume fixed point d* = 3
dynamical scaling:        z ~ 1
```

Frozen dynamics даёт

$$
d_H=2.999229782139151,
$$

$$
z approximately 0.998281156.
$$

Важная notation correction: число `3.004393867`, исторически называвшееся `ds_slice_holdout`, уже включает division by `z`:

$$
d_eff(slice)=d_H/z=3.004393867.
$$

Нельзя делить его на `z` второй раз.

---

# Глава 15. Откуда в истории появляется четвёртое направление

Spatial topology и volume scaling дают three-dimensional slice.

Dynamics имеет characteristic scaling

$$
tau -> lambda^z tau.
$$

Для relativistic scaling требуется

$$
z -> 1.
$$

Frozen result близок к единице, поэтому one-causal-time history имеет effective scaling

$$
d_eff(history)=1+d_H/z approximately 4.004393867.
$$

Правильная формулировка:

```text
spatial topology -> 3
causal-volume fixed point -> 3
z -> 1
history -> 3+1-like scaling
```

Это ещё не statement, что finite constraint eigenvalue является physical time frequency. Намного позже physical time потребует projector/history conditioning.

---

# Часть IV. Наблюдатель, расстояние и рождение гладкого пространства

# Глава 16. Главное различие: пространство не становится гладким — микроструктура становится неразрешимой

Это один из центральных смыслов проекта.

Представьте кирпичную или оштукатуренную стену.

Вплотную вы видите:

```text
поры
царапины
песчинки
шероховатости
края кристаллов
```

Отойдите на несколько метров — и глаз уже видит гладкую плоскость.

Но стена **физически не перестроилась** из шероховатой в гладкую, когда вы сделали шаг назад.

Изменилось отношение

```text
размер микродетали / размер разрешаемого элемента наблюдения.
```

То же различие принципиально для нашей spacetime picture.

Microscopic state остаётся дискретным. Но наблюдатель с конечным resolution не может разрешить отдельные binary cells и видит их coarse collective observables.

Поэтому фраза

> «с удалением наблюдателя пространство-время становится гладким»

в строгой форме означает

> **с увеличением physical resolution scale один observable pixel содержит всё больше microscopic spacetime degrees of freedom, и их unresolved fluctuations self-average.**

---

# Глава 17. Математическая версия аналогии со стеной

Пусть fundamental microscopic cutoff

$$
ell_*.
$$

Его possible identification с Planck length `ell_P` является physical hypothesis, а не уже доказанной частью construction.

Для наблюдателя с characteristic angular/causal resolution `theta` на separation `r` вводится effective resolved length

$$
ell_obs(r)=sqrt(ell_*^2+(theta*r)^2).
$$

Это expression имеет два естественных режима.

### Очень близко к микроскопике

Если

```text
theta*r << ell_*
```

то

$$
ell_obs approximately ell_*.
$$

Наблюдатель может различать отдельные microscopic structures.

### Макроскопический режим

Если

```text
theta*r >> ell_*
```

то

$$
ell_obs approximately theta*r.
$$

Один resolution element покрывает уже множество microscopic cells.

Для dyadic coarse graining используем

$$
b(r)=2^{floor(log_2(ell_obs/ell_*))}.
$$

`b=1` означает microscopic resolution. Большой `b` означает, что один observable cell является collective block большого числа microscopic degrees of freedom.

---

# Глава 18. Почему в четырёхмерной history шероховатость падает как b^-2

Предположим на данном coarse regime, что один history block содержит примерно

$$
N(b) proportional to b^4
$$

weakly correlated zero-mean microscopic contributions.

Тогда центральное self-averaging даёт

$$
delta g_RMS proportional to 1/sqrt(N) proportional to b^-2.
$$

Это ключ к «стене».

Если один pixel усредняет не одну неровность, а `N` примерно независимых микронеровностей, случайная часть уменьшается как `1/sqrt(N)`.

Derivative добавляет inverse length:

```text
metric roughness      ~ b^-2
one derivative        ~ b^-3
two derivatives       ~ b^-4
```

Именно поэтому curvature-like defect убывает быстрее самой metric roughness.

Важно: это self-averaging reasoning требует контроля correlations. Если microscopic contributions long-range correlated, exponent может измениться. Поэтому measured scaling — finite diagnostic, не универсальный theorem без RG correlation proof.

---

# Глава 19. Что реально измерил observer-smoothing gate

На frozen q=2 route family получено

$$
delta g approximately b^-2.001707,
$$

$$
grad(delta g) approximately b^-3.001458,
$$

$$
delta R_proxy approximately b^-4.000524.
$$

В two-form / reconstructed metric sector:

$$
Delta_simp approximately b^-1.994838,
$$

$$
Delta_gU approximately b^-2.019746.
$$

То есть несколько независимых measures roughness показывают одну и ту же картину:

```text
microscopic binary/discrete detail
 -> block averaging
 -> rapidly decreasing geometric defects
 -> smooth observer-accessible IR description
```

Это не команда `make_smooth()`. Smoothness появляется как property coarse observables.

---

# Глава 20. Почему gradient и curvature выглядят ещё гладче

Пусть coarse metric fluctuation amplitude

$$
delta g(b) ~ b^-2.
$$

Physical derivative на block scale приносит ещё factor `1/b`, поэтому

$$
partial(delta g) ~ b^-3.
$$

Linearized curvature содержит roughly two derivatives:

$$
delta R ~ partial^2(delta g) ~ b^-4.
$$

Это означает, что macroscopic observer может видеть не только visually smooth metric, но и ещё более быстро стабилизирующуюся curvature description.

Аналогия со стеной становится сильнее:

- средняя высота стены стабилизируется;
- её local slope fluctuations уменьшаются ещё быстрее;
- curvature of visible surface ещё менее чувствительна к отдельным песчинкам.

---

# Глава 21. Очень важный negative control: coarse-graining само по себе не создаёт 3+1 измерения

Старая fixed-4D smoothing ветвь имела independent dimension-blind binary diamond control.

Он оставался около spectral dimension

```text
~2.07,
```

а не magically превращался в четыре dimensions после averaging.

Это критично.

Нельзя рассуждать так:

```text
много битов усреднились
 -> поэтому обязательно возникли 3+1 dimensions.
```

Нет.

У проекта две разные стрелки:

```text
binary combinatorics / topology / growth -> dimension
observer coarse graining                -> smoothness
```

Dimension выбирается structural dynamics q=2 family. Smoothness объясняет, почему уже возникшая effective geometry может выглядеть continuous.

---

# Глава 22. Дискретность и непрерывность не противоречат друг другу

В этой картине microscopic и macroscopic statements могут одновременно быть истинны:

```text
UV: discrete quantum degrees of freedom
IR: smooth differentiable effective metric
```

Это обычная логика emergence.

Кристалл состоит из discrete atoms, но elastic medium описывается continuous displacement field.

Вода состоит из molecules, но hydrodynamics использует smooth density and velocity fields.

Изображение состоит из pixels, но после достаточного resolution scale воспринимается continuous.

Здесь гипотеза аналогична:

```text
spacetime microstructure: binary / quantum / combinatorial
spacetime IR: smooth metric / connection / curvature
```

Разница в том, что для spacetime сама geometry должна быть reconstructed из microstate, поэтому требования намного строже, чем для жидкости на уже заданном пространстве.

---

# Глава 23. Квантовая пена — это не обязательный макроскопический хаос

Smooth mean geometry не требует zero microscopic variance.

Можно иметь

```text
<delta g> = 0
<delta g^2> > 0.
```

То есть:

```text
smooth mean geometry
+ quantum fluctuations
= microscopic quantum foam
```

Но здесь есть важная коррекция старой версии README.

Smoothing law `delta g ~ b^-2` сам по себе **не является quantum vacuum power spectrum**. Старый shortcut, превращавший его в `P(k) ~ k^+1`, был отвергнут.

Прямой reduced TT Gaussian calculation позже дал

$$
P_TT(k) proportional to k^-1.
$$

Поэтому observer smoothing и physical quantum two-point function — разные observables.

---

# Часть V. Как квантовая геометрия получает внутреннюю структуру

# Глава 24. Qubit одновременно содержит distinguishability geometry и phase

Нормированный two-component state живёт на `S3` внутри `C2`. Physical ray quotient даёт

```text
CP1 ~ S2
```

и Hopf fibration

$$
U(1) -> S^3 -> S^2.
$$

Обе структуры объединяет quantum geometric tensor

$$
Q_ab=<partial_a psi | (1-|psi><psi|) | partial_b psi>.
$$

Для Bloch spinor его real part даёт Fubini-Study metric

$$
ds_FS^2=(dtheta^2+sin^2(theta)dphi^2)/4,
$$

а imaginary part — Berry curvature

$$
F=(sin(theta)/2) dtheta wedge dphi.
$$

Схематически:

```text
Re Q -> quantum distinguishability / geometry
Im Q -> phase curvature / U(1)
```

Поэтому light-phase branch и geometry branch не надо вставлять как два совершенно чужих объекта: они имеют общий q=2 ray origin. Но превращение phase carrier в physical photon остаётся dynamical question.

---

# Глава 25. Один q=2 carrier открывает SU(2) и compact U(1)

Bloch/flux branch естественно несёт canonical spatial `SU(2)` geometry.

Pancharatnam link

$$
U_vw=<psi_v|psi_w>/|<psi_v|psi_w>|
$$

transformируется как compact lattice `U(1)` connection.

Closed product даёт Berry/Pancharatnam holonomy.

Kinematically:

```text
q=2 -> SU(2) geometry carrier
q=2 -> compact U(1) phase carrier
```

Но:

```text
U(1) phase carrier != proven Maxwell photon
SU(2) spatial geometry != automatically electroweak SU(2)
```

Эти ограничения сохраняются во всём репозитории.

---

# Глава 26. Unique collective spin-2 существует отдельно от geometry qubit

**[EXACT REPRESENTATION THEORY]**

Снова используем

$$
(1/2)^4=2 x j=0 + 3 x j=1 + 1 x j=2.
$$

В decomposition есть ровно один `j=2` irrep.

Это означает existence unique collective spin-2 carrier внутри four-qubit Hilbert space.

Но это ещё не физический graviton. Чтобы стать graviton sector, carrier должен пройти:

```text
geometric identification
 -> correct kinetic structure
 -> constraints
 -> TT physical quotient
 -> physical history pole
```

Massless TT reduction в соответствующем continuum sector оставляет две helicities.

---

# Глава 27. Logical shape превращается в metric

**[EXACT LOCAL BRIDGE]**

В singlet geometry-qubit sector:

```text
X, Z -> intrinsic shape
Y    -> orientation pseudoscalar
```

Для regular tetrahedron background

```text
g0 = [[2,1,1],
      [1,2,1],
      [1,1,2]]
```

Exact Jacobian tangents `M_X,M_Z` trace-free и имеют Gram

$$
Tr(g0^-1 M_A g0^-1 M_B)=(3/2) delta_AB.
$$

То есть две logical shape directions map’ятся в orthogonal equal-norm metric tangents.

Старая стрелка

```text
logical qubit -> ??? -> metric
```

закрыта конкретным operator map.

---

# Глава 28. Пять traceless metric modes и первый 8.43% precursor

**[FINITE PASS + EXACT S4 REDUCTION]**

Six-edge carrier decomposition:

$$
6=A1 + E + T2.
$$

Trace part `A1` отделяется, а physical local traceless metric space имеет dimension five:

$$
5=E+T2.
$$

First refined q4 metric compression дала

```text
lambda_E  = 1.1111917875584736
lambda_T2 = 1.0220278507464782
Delta_ET  = 0.08916393681199541
kappa_5   = 1.0576934254712764
```

и relative split

$$
Delta_ET/kappa_5=0.08430036026012608.
$$

То есть `8.43%` — настоящий local Euclidean tetrahedral spin-2 anisotropy precursor.

Но он **не** равен автоматически:

```text
physical zeta4
speed anisotropy
particle mass ratio
observable Lorentz violation
```

---

# Глава 29. Почему 8.43% нельзя превратить в массы частиц

**[EXACT NO-GO]**

На traceless space

$$
5=E+T2.
$$

Для normalized tetrahedral splitter

$$
Q_tet=(3/5)P_E-(2/5)P_T2
$$

внутри `T2`

$$
Q_tet|T2=-(2/5)I_3.
$$

Если три generations образуют irreducible `T2`, любой `S4`-invariant mass operator по Schur lemma пропорционален identity:

$$
M=m I_3.
$$

Поэтому

```text
8.43% -> electron/muon/tau hierarchy
```

невозможно без independently derived flavor representation, symmetry-breaking spurion и Yukawa map.

---

# Часть VI. Constraint dynamics и дорога к GR

# Глава 30. Peter-Weyl идёт на следующий shell

**[FINITE PASS]**

Spin parity даёт

```text
P H_E P = 0.
```

Определим

$$
K=P H_E^2 P
$$

и normalized second-shell constraint object

$$
Lambda=K^-1/2 (P H_E^4 P-K^2) K^-1/2.
$$

Exact 32D finite result:

```text
rank(K)=32
lambda_min=10.635759878291307
lambda_max=15.059927665966466
mean=12.860443113390883
distance from scalar identity=0.09440461833276048
```

Это nontrivial finite **constraint spectral data**. Это не physical frequencies и не particle masses.

---

# Глава 31. Geometry-only blocking не создаёт нужный RG flow

**[EXACT CONTROL]**

Для recursive PL geometry

$$
P^T L_(g+1) P=(1/4)L_g.
$$

Если geometry и internal kernel factorize, все internal couplings получают один и тот же scale factor, поэтому normalized anisotropy не течёт.

Следовательно genuine flow обязан приходить из

```text
Peter-Weyl recoupling
nonseparable quantum blocking
interblock transport
history dynamics
```

а не из скрытого geometric rescaling.

---

# Глава 32. Euclidean Hamiltonian получает Lorentzian половину

Для real Ashtekar-Barbero variables

$$
A=Gamma+beta K.
$$

Derivative-free kinetic controls дают

$$
H_E^kin=-beta^2 Q_DW,
$$

$$
H_L^corr=(1+beta^2)Q_DW,
$$

и потому

$$
H_E^kin+H_L^corr=Q_DW.
$$

Это exact classical consistency control DeWitt kinetic structure.

Он не является доказательством quantum beta-independence.

---

# Глава 33. Hamiltonian constraints должны научиться двигать пространство

Главная structural gravity equation:

$$
[H[N],H[M]] -> i*hbar*D[sharp(N dM-M dN)].
$$

RHS строится независимо через cochain/Hodge/flux map и route rerouting.

Fixed-cutoff scaling:

```text
C_cross / D = O(epsilon)
C_GG    / D = O(epsilon^2)
```

с conservative simultaneous family

$$
Jmax=o(epsilon^(-2/13)).
$$

В declared ADM family closure выбирает

```text
c = 1/2
A*B = 1
```

но HDA не выводит numeric Newton constant, а cosmological term cancels из bracket.

---

# Глава 34. Plebanski и Regge независимо сходятся к Einstein structure

Две downstream дороги:

```text
B-field -> simplicity -> Urbantke metric -> connection -> curvature -> Einstein control
```

и

```text
metric -> Regge Hessian -> Fierz-Pauli -> Einstein-Hilbert / Ward controls
```

работают как independent cross-checks.

Held-out Regge finite-size rule

$$
Z_L=1/8+C/L^2+D/L^4
$$

предсказал

```text
Z6_pred = 0.11876923193907167
Z6_obs  = 0.11876075461190198
relative error ~ 0.00714%
```

Это internal held-out numerical control, не experimental confirmation quantum gravity.

---

# Глава 35. Первый reduced TT propagator

**[EXACT REDUCED CONTROL]**

Reduced kernel:

$$
G_TT(omega,k)=I_TT / { Z_T [4 sin^2(omega/2) - (1/3) sum_i 4 sin^2(k_i/2) + i0] }.
$$

Он имеет massless pole в reduced model.

Bare lattice controls:

```text
eta2_bare  = -1/45
zeta4_bare = -1/12
```

Equal-time Gaussian covariance:

$$
P_TT(k) proportional to k^-1.
$$

Это regulator positive control, не final interacting physical prediction.

---

# Глава 36. Почему R_aniso -> zeta4 было неправильной стрелкой

Logical higher-shell ratio

```text
R_aniso ~ 0.08975326618
```

— internal Peter-Weyl RG diagnostic.

Он не physical cubic-dispersion coefficient.

Легальная chain:

```text
shape dynamics
 -> exact shape-to-metric map
 -> metric effective kernel
 -> TT physical kernel
 -> physical pole coefficients
```

---

# Часть VII. Momentum, Wilson space и физические observables

# Глава 37. Onsite kernel сжимается до трёх numbers — только onsite

**[EXACT S4 AT k=0]**

Для одного tetrahedral coarse block

$$
C6^(0)=a0 I+b0 A_adj+c0 O_opp.
$$

Irrep eigenvalues:

```text
lambda_A1 = a0 + 4 b0 + c0
lambda_E  = a0 - 2 b0 + c0
lambda_T2 = a0 - c0
```

Это правильная onsite symmetry compression. Generic directed momentum несёт собственную representation и требует большего space.

---

# Глава 38. Momentum сам трансформируется

Correct covariance law:

$$
C6(omega,g*k)=U_g C6(omega,k) U_g^-1.
$$

До TT constraints representation count даёт 13 quartic S4 singlets.

После

```text
tr(h)=0
h_ij k_j=0
```

exact polynomial quotient имеет dimension

$$
dim W_TT,S4^(4)=6.
$$

Это полный parity-even quartic physical pole space в declared symmetry class.

---

# Глава 39. Шесть Wilson coefficients и frozen extractor

Один complete Reynolds basis содержит шесть structures `W1...W6`, поэтому

$$
delta K_TT^(4)=Z_T c_T^2 a_*^2 sum_(r=1)^6 c_r W_r.
$$

Настоящая generic dimensionless prediction — six-vector

```text
c_IR = (c1,c2,c3,c4,c5,c6).
```

High-symmetry `100/110/111` дают rank five. Добавление preregistered generic direction `120` закрывает rank six.

Exact extraction determinant:

$$
det(A)=1/699840000 != 0.
$$

`A^-1` frozen до открытия microscopic coefficients.

---

# Глава 40. Momentum рождается из interblock transport

Onsite return не знает, куда распространяется волна.

Для face-sharing tetrahedra shared-face stabilizer — `S3`.

Six-edge carrier decomposes under it как

```text
6=(A1+E)_apex + (A1+E)_face.
```

Reciprocal nearest-neighbour transfer задаётся двумя symmetric `2x2` multiplicity matrices — всего шестью real transfer functions.

Regular tetrahedral moments:

$$
sum_a n_a^i n_a^j=(4/3)delta_ij,
$$

$$
sum_a (k dot n_a)^4=(4/5)(k^2)^2-(8/9)Q4_cub(k).
$$

Поэтому leading `k^2` может стать isotropic, тогда как tetrahedral memory впервые появляется at quartic order.

---

# Глава 41. eta2 и zeta4 теперь только nested hypothesis

Старый compact ansatz

$$
e4(n)=eta2+zeta4 Q4_cub(n)
$$

не выброшен, но является только двумерной subspace внутри general six-dimensional answer.

Если frozen result сам туда попадает:

```text
zeta4 = 2(e100-e110)
eta2  = (e100+4e110)/5
```

и held-out relation

$$
e100-4e110+3e111=0
$$

должна выполниться без tuning.

---

# Глава 42. Tetrahedral polarization fingerprint

Для single-Q_tet nested model exact TT projection даёт spectra

```text
100: { 3/5,  -2/5 }
110: { 7/20, -2/5 }
111: {-1/15, -1/15}
```

и parameter-free splitting ratio

$$
Delta e_100 : Delta e_110 : Delta e_111 = 4:3:0.
$$

Это strong blind fingerprint только если full six-vector сначала independently выбирает эту nested submodel.

---

# Глава 43. On-shell Wilson space переживает local field redefinitions

Leading Einstein TT kernel

$$
K0=Z_T(-omega^2+c_T^2 k^2)I_TT.
$$

Local field redefinition добавляет quartic terms, пропорциональные `K0`. На leading massless pole `K0=0`, поэтому эти pieces vanish.

Следовательно six-dimensional quotient является space genuine quartic **pole** observables, хотя off-shell action может иметь больше basis-dependent coefficients.

---

# Часть VIII. Constraint spectrum ещё не физическая частота

# Глава 44. Самая важная концептуальная коррекция: constraint z != physical omega

Peter-Weyl `H[N]` — Hamiltonian constraint.

Поэтому spectral resolvent

```text
(z-H)^-1
```

нельзя автоматически назвать physical propagator

```text
G(omega,k).
```

Constraint spectral parameter `z` — не physical frequency `omega`.

Легальная chain:

```text
constraints H[N]
 -> physical projector / rigging map
 -> history or boundary amplitude
 -> Z[J]
 -> W[J]
 -> 1PI Gamma
 -> physical quadratic kernel
 -> poles in physical omega,k
```

Finite Peter-Weyl `K/A/B/Lambda` остаются ценными constraint-dynamics data, но не переименовываются в graviton self-energy.

---

# Глава 45. Physical projector перестал быть словом

**[EXACT FINITE + CI PASS]**

Для constraints `C_A` и positive metric `G^AB` define master constraint

$$
M_G=C_A^dagger G^AB C_B.
$$

Тогда exactly

$$
ker(M_G)=intersection_A ker(C_A).
$$

Finite physical projector

$$
P0=chi_{0}(M_G).
$$

CI control:

```text
max ||C_A P0||                 ~ 1.35e-15
max ||P0(G_i)-P0(G_j)||        ~ 2.82e-15
```

и heat-kernel convergence совпадает с spectral prediction на machine precision.

Открыт theory-specific refinement/rigging limit

$$
delta_P(g)=||P_(g+1) I_g-I_g P_g|| / ||I_g P_g|| -> 0.
$$

---

# Глава 46. Время появляется после physical conditioning

Minimal parametrized-system positive control показывает

$$
2 <T_out|P_phys|T_in> = exp[-i H_s (T_out-T_in)].
$$

То есть обычная unitary time evolution восстанавливается **после** projection и conditioning на relational clock states.

Для gravity candidate natural clock — не искусственный внешний параметр, а physical boundary proper separation `tau`, задаваемый semiclassical geometry/extrinsic-curvature data. Тогда physical `omega` — Fourier conjugate именно к `tau`.

---

# Глава 47. Настоящая физика живёт в 1PI effective action

После physical projector/history measure нужны generating functional

$$
Z[J_g,J_A,...]
$$

и 1PI effective action

$$
Gamma[g,A,...].
$$

Physical quadratic kernels:

$$
K_g=delta^2 Gamma / delta h_TT^2,
$$

$$
K_A=delta^2 Gamma / delta A_T^2.
$$

Только здесь разрешено говорить о physical poles, residues, propagation, group velocity и phase.

Это нынешний главный conceptual physical bottleneck.

---

# Часть IX. Теория может предсказать не dispersion, а её отсутствие

# Глава 48. Шесть coefficients могут законно сжаться в один, а потом в ноль

Для isotropic coefficient vector

```text
v_iso=(6,24,6,36,-9,18)^T
```

frozen extractor даёт exactly

```text
A v_iso=(1,1,1,1,1,1)^T.
```

Поэтому observable symmetry ladder:

```text
S4:      six independent observables
SO(3):   y1=y2=...=y6
Lorentz metric-only massless vacuum: y1=...=y6=0
```

Или короче:

$$
6 -> 1 -> 0.
$$

Пять contrasts проверяют restoration spatial isotropy. Шестая common amplitude проверяет, остаётся ли preferred-foliation quartic pole shift.

---

# Глава 49. Почему Lorentz-invariant metric-only vacuum защищает massless cone

Если IR vacuum Lorentz invariant, diffeomorphism unbroken и low-energy helicity-2 field — обычный metric graviton, inverse propagator имеет form

$$
K_TT(s)=P_TT s F(a_*^2 s),
$$

где

$$
s=-omega^2+c^2 k^2.
$$

Massless root

$$
s=0
$$

не сдвигается local analytic higher derivatives. Они могут менять off-shell form factor или добавлять heavy roots `F=0`, но не обязаны давать vacuum `k^4,k^6,...` shift исходному massless graviton.

Значит Planck-suppressed vacuum dispersion **не является обязательной сигнатурой quantum gravity**.

---

# Глава 50. Если tetrahedral anisotropy физична, у неё должен быть physical order tensor

Regular tetrahedron normals define quartic tensor

$$
S_ijkl=sum_a n_ai n_aj n_ak n_al.
$$

Trace-free tetrahedral order parameter

$$
T4_ijkl=S_ijkl-(4/5)delta_(ij delta_kl).
$$

Он удовлетворяет

```text
T4_iikl = 0
||T4||^2 = 128/135
```

и contraction даёт cubic harmonic

$$
T4_ijkl k_i k_j k_k k_l=-(8/9)Q4_cub(k).
$$

Если anisotropic physical pole выживает, тот же order parameter должен существовать в state/history/EFT. Иначе direction likely принадлежит regulator frame.

---

# Часть X. Световая ветвь

# Глава 51. Compact U(1) получает canonical Maxwell-like dynamics

На seed S3 complex:

```text
V=8, E=24, F=32, T=16
rank d0=7
rank d1=17
d1 d0=0
b1=0
```

Если blocked Pancharatnam phase sector даёт positive local quadratic action

$$
L_A=(Z_A/2)(dot(theta)-d0 A0)^T M1 (dot(theta)-d0 A0)
    -(Z_A/2)(d1 theta)^T M2(d1 theta),
$$

то canonical momentum

$$
p=Z_A M1(dot(theta)-d0 A0)
$$

и variation по `A0` автоматически даёт Gauss law

$$
d0^T p=0.
$$

Transverse dynamics:

$$
ddot(theta)=-M1^-1 d1^T M2 d1 theta.
$$

Важно: `Z_A` cancels from linear dispersion. Он задаёт normalization/coupling, но не light speed.

---

# Глава 52. Почему Hopf topology не может одна выдать 137

Compactness фиксирует phase period и integer charge lattice.

Но family

$$
Gamma_A[Z_A]=-(Z_A/4) integral F^2
$$

имеет ту же gauge symmetry, compactness, Chern class и massless cone для любого positive `Z_A`.

Поэтому

```text
Hopf topology + gauge symmetry + Maxwell form
  does NOT determine alpha.
```

В unit-charge convention

$$
alpha=1/(4*pi*Z_A).
$$

Значит `alpha` требует microscopic phase-history/RG calculation `Z_A`. Случайный Peter-Weyl eigenvalue нельзя переименовывать в `137`.

---

# Глава 53. Почему 3+1 особенно важно для compact U(1)

Независимые branches дают

```text
q=2 -> d_space=3
q=2 -> compact U(1) phase carrier
```

вместе — `3+1-dimensional compact U(1)`.

Эта dimensionality допускает deconfined/Coulomb phase. Это compatibility result, а не proof того, что microscopic `Z_A` нашей модели уже лежит в deconfined basin.

Deconfinement остаётся dynamic question.

---

# Глава 54. Гравитация и свет могут иметь один principal cone

Если physical IR action приходит к одной emergent metric,

$$
Gamma_IR[g,A]=integral sqrt(-g)[(R-2 Lambda)/(16 pi G) -(Z_A/4)F^2]+...
$$

то principal scalar

$$
s=g^munu k_mu k_nu
$$

общий.

В Lorentz-invariant vacuum

```text
K_g     = s F_g(s)
K_gamma = s F_gamma(s)
```

и исходные massless photon и graviton имеют один cone

$$
s=0.
$$

`G`, `Z_A` и `alpha` не используются как ручки для tuning скорости.

Conditional massless-spin-2 consistency дополнительно ведёт к universal gravitational coupling, тогда как U(1) требует charge conservation/quantization, но не одинакового charge у всех species.

---

# Часть XI. Три фундаментальных constants — три разных microscopic questions

# Глава 55. Newton constant

После geometric normalization metric physical 1PI action должна иметь

$$
Gamma[g] contains C_R integral sqrt(-g) R.
$$

Только тогда

$$
G=1/(16*pi*C_R).
$$

В internal units первым вычисляется dimensionless `G/a_*^2`.

Graviton residue без фиксированной geometric field normalization нельзя автоматически называть Newton constant.

---

# Глава 56. Cosmological constant

`Lambda` не выводится HDA bracket.

Она должна определяться background saddle physical effective action:

$$
delta Gamma/delta g |_(g_bar)=0.
$$

Curvature этого vacuum solution определяет effective cosmological constant.

Поэтому unit-radius S4 control `Lambda approximately 3` — reconstruction test supplied geometry, а не prediction observed dark energy.

---

# Глава 57. Fine-structure constant

После microscopic calculation Maxwell stiffness

$$
Z_A
$$

получаем в chosen unit-charge convention

$$
alpha=1/(4*pi*Z_A).
$$

Итак:

```text
C_R   -> G
vacuum saddle -> Lambda
Z_A   -> alpha
```

Это три different microscopic estimators.

---

# Глава 58. Zero dispersion не означает zero quantum geometry

Даже если physical six-vector

```text
c1=...=c6=0,
```

connected metric covariance

$$
C_h(x,y)=<h(x)h(y)>_connected
$$

может быть nonzero.

Optical phase map

$$
delta phi=(k ell/2) J h
$$

даёт

$$
C_phi=(k ell/2)^2 J C_h J^T.
$$

Поэтому experimental programme разделяется:

```text
1. pole / dispersion test
2. connected fluctuation / interference test
```

и zero Lorentz violation не означает, что quantum geometry observationally empty.

---

# Часть XII. Matter и cosmology: что topology уже разрешает, но dynamics ещё не вывела

# Глава 59. S3 не запрещает fermions

`S3` parallelizable, поэтому

$$
w2(S3)=0.
$$

Кроме того

$$
H1(S3,Z2)=0.
$$

Следовательно на S3 существует ровно одна spin structure.

Seed 16-cell over Z2 даёт

```text
(b0,b1,b2,b3)=(1,0,0,1).
```

Это topological prerequisite для spin-1/2 fields.

Но это не derivation Standard Model, chirality, generations или Yukawa sector. Geometric `Spin(3)~SU(2)` нельзя автоматически переименовывать в electroweak `SU(2)`.

---

# Глава 60. Global S3 имеет cosmological falsifiers

Если physical continuum сохраняет closed S3 spatial slices, FRW curvature sign

$$
k=+1.
$$

Это не требует, чтобы observable curvature сегодня была большой.

Scalar harmonics на S3 radius `a` имеют discrete spectrum

$$
-nabla^2 Y_n=[n(n+2)/a^2]Y_n,
$$

с degeneracy `(n+1)^2`.

Это conditional global-topology test: physical history dynamics ещё должна показать, что microscopic canonical S3 survives в cosmological continuum.

---

# Часть XIII. Где тяжёлая микрофизика упирается сейчас

# Глава 61. j=1 representation RG

Canonical `j=1 S4[2,2]` carrier и finite master-projector preflight прошли gates.

Exact ordered Peter-Weyl paths реально вычислялись, но часть paths превысила hosted-runner wall, поэтому full

```text
Lambda(j=1)
R_aniso(j=1)
```

ещё не frozen.

Следующая exact computational factorization:

$$
H_s H_r=sum_(alpha,beta) H_(s,beta) H_(r,alpha).
$$

Это sharding identity, не physics approximation.

---

# Глава 62. full-H_E L1 block

Active-cone backend — representation optimization, которая должна быть exactly equivalent reference implementation.

Reference-vs-local certificate упёрся в CI time wall до numerical guard, поэтому 72 L1 production shards нельзя объявлять завершёнными.

Правильный следующий шаг — shard’ить сам equivalence certificate, не ослабляя support/amplitude tolerances.

То есть bottleneck сейчас computational granularity, а не найденный physical contradiction.

---

# Глава 63. Truth table на сегодня

| Arrow / observable | Status |
|---|---|
| binary local alternatives | **MODEL STARTING ASSUMPTION** |
| `q+2=2^q -> q=2` | **EXACT** |
| q=2 Hamming `C4` | **EXACT** |
| octahedral local `S2` link | **EXACT** |
| `Z2^2 -> Walsh tetrahedral normals` | **EXACT** |
| face-qubit flux closure | **EXACT / FINITE** |
| four-face singlet geometry qubit | **EXACT REPRESENTATION** |
| canonical PL `S3` completion | **EXACT / FINITE STABILITY** |
| minimal 8-vertex flag uniqueness | **EXACT IN DECLARED SEMANTICS** |
| causal-volume fixed point `d*=3` | **EXACT** |
| `d_H/z~3.00439`, history `~4.00439` | **FROZEN / DERIVED** |
| observer resolution map | **DECLARED COARSE-GRAINING MAP** |
| `delta g~b^-2`, gradient `~b^-3`, curvature `~b^-4` | **FINITE PASS** |
| smoothing alone derives 4D | **NO — NEGATIVE CONTROL** |
| smoothing exponent = TT vacuum spectrum | **REJECTED SHORTCUT** |
| quantum geometric tensor `ReQ/ImQ` | **EXACT KINEMATIC** |
| logical shape -> metric | **EXACT** |
| L1 `E/T2` split 8.43% | **FINITE PASS** |
| `8.43% -> particle masses` | **NO-GO** |
| 32D higher-shell constraint Lambda | **FINITE PASS** |
| geometry-only anisotropy flow | **NO-FLOW CONTROL** |
| HDA/ADM declared closure | **STRUCTURAL PASS** |
| Regge held-out Z6 | **HELD-OUT PASS** |
| reduced massless TT propagator | **EXACT REDUCED CONTROL** |
| generic quartic TT S4 dimension = 6 | **EXACT** |
| six-observable extractor | **EXACT** |
| on-shell field-redefinition invariance | **EXACT** |
| finite master projector | **EXACT + CI PASS** |
| constraint spectral z = physical omega | **REJECTED SHORTCUT** |
| `6 -> 1 -> 0` ladder | **EXACT / CONDITIONAL IR** |
| compact Hopf U(1) carrier | **EXACT KINEMATIC** |
| Maxwell form from positive phase action | **CONDITIONAL THEOREM** |
| `Hopf topology -> alpha` | **NO-GO** |
| unique spin structure on S3 | **EXACT TOPOLOGICAL** |
| physical projector continuum/rigging limit | **OPEN PHYSICAL** |
| microscopic physical Gamma[g,A] | **OPEN PHYSICAL** |
| frozen physical six-vector | **OPEN PHYSICAL** |
| microscopic G, Lambda, Z_A | **OPEN PHYSICAL** |
| realistic gauge/chiral/Yukawa matter | **OPEN** |
| experimental confirmation | **OPEN / DATA** |

---

# Пять драконов, которых нельзя обмануть

### Dragon I — наблюдатель не является новой динамикой

Расстояние до объекта не перестраивает microscopic spacetime. Меняется resolution/coarse-graining map. Аналогия со стеной допустима только в этом смысле.

### Dragon II — constraint is not time

Нельзя переименовать spectral variable constraint в physical frequency. Сначала projector/history, затем Gamma, затем pole.

### Dragon III — regulator is not nature

Если tetrahedral anisotropy не сопровождается physical order parameter или не stabilizes under refinement, она regulator memory.

### Dragon IV — common scale is common

Нельзя отдельно калибровать directions, polarizations, events и sectors. Один derived scale или один заранее объявленный calibration datum.

### Dragon V — blind data

После freeze нельзя менять basis, удалять неудобный coefficient или выбирать nested submodel потому, что posterior красивее.

У природы всегда должно оставаться право сказать `FAIL`.

---

# Воспроизводимые gates

```bash
python scripts/verify_theory_gates.py
python bcqg_bit_to_gravity_final.py --strict
python bcqg_observer_smoothing_unified.py
python bcqg_global_manifold_gate.py
python scripts/q2_dimension3_fixed_point_gate.py --max-generation 10
python scripts/micro_walsh_qgeom_gate.py
python scripts/q2_global_face_qubit_gluing_gate.py
python scripts/logical_shape_metric_jacobian_gate.py
python scripts/peter_weyl_j1_s4_block_gate.py
python scripts/tt_propagator_first_pass.py
python scripts/tt_vacuum_two_point_gate.py
python scripts/s4_tt_quartic_complete_basis_gate.py
python scripts/s4_tt_six_wilson_predictor.py --selftest
python scripts/nearest_block_s3_transfer_gate.py
python scripts/c6_tt_wilson_extractor.py
python scripts/tetrahedral_tt_birefringence_gate.py
```

---

# Канонические входы

| Layer | Entry point |
|---|---|
| Full evidence index | `CANONICAL_THEORY_PACKAGE.md` |
| Human status | `THEORY_STATUS.md` |
| Machine ledger | `theory_gates.json` |
| Binary -> smooth spacetime | `BIT_TO_SPACETIME_CENTRAL_EQUATION.md` |
| Observer-scale smoothing | `OBSERVER_SCALE_SMOOTHING.md` |
| Global q=2 manifold | `GLOBAL_MANIFOLD_Q2_COMPLETION.md` |
| q=2 fixed point | `Q2_DIMENSION3_FIXED_POINT_CLOSURE.md` |
| q=2 Walsh geometry | `MICRO_WALSH_QGEOM_BRIDGE.md` |
| Shape -> metric | `LOGICAL_SHAPE_METRIC_JACOBIAN.md` |
| Mass no-go | `S4_MASS_SPLITTING_NO_GO.md` |
| Higher shell | `PETER_WEYL_HIGHER_SHELL_LAMBDA_RESULT.md` |
| HDA | `THREE_NODE_GRAPH_HDA_RESULT.md`, `JOINT_REGULATOR_LIMIT.md` |
| Regge control | `TT_REGGE_ZT_L6_RESULT.md` |
| Quartic TT space | `S4_TT_QUARTIC_COMPLETE_BASIS.md` |
| Observable dictionary | `TT_TO_REAL_PHYSICS_OBSERVABLES.md` |
| External tests | `PREDICTIONS_AND_EXPERIMENTAL_TESTS.md` |
| Detailed 14 Aug lesson archive | `docs/archive/README_LESSON_2026-08-14.md` |
| Original 17 Aug story | `docs/archive/README_STORY_2026-08-17.md` |
| Previous 21 Aug v42 story | `docs/archive/README_STORY_2026-08-21_v42.md` |

---

# Эпилог. Что именно мы теперь имеем в виду под «битами пространства-времени»

Мы начали не с lattice spacing и не с metric tensor.

Мы начали с binary distinction.

Локальная однородность выбрала

$$
q=2.
$$

Четыре route labels образовали `C4`.

Два causal poles превратили его в octahedral `S2` link.

Три Walsh characters превратили те же binary labels в четыре exact tetrahedral normals.

Face qubits получили flux closure.

Gauss projection создал gauge-invariant geometry qubit.

Global gluing дал canonical `S3` spatial phase.

Recursive causal growth дал exact volume fixed point

$$
d_*=3.
$$

Dynamical exponent пришёл к

$$
z approximately 1,
$$

и history стала 3+1-like.

Но microscopic world всё ещё discrete.

И вот здесь появляется наблюдатель.

Не потому, что его взгляд «магически меняет физику», а потому, что любой observable имеет finite resolution.

Вблизи стены видна песчинка.

Издалека одна visual cell содержит тысячи песчинок.

Вблизи microscopic spacetime наблюдатель различал бы отдельные binary quantum-geometric degrees of freedom.

На macroscopic scale один effective cell содержит огромное число этих degrees of freedom.

Если unresolved contributions self-average,

```text
metric roughness ~ b^-2
slope roughness  ~ b^-3
curvature noise  ~ b^-4.
```

Поэтому **дискретность может быть fundamental, а гладкость — emergent и observer-resolution dependent**, не противореча друг другу.

Это и есть самая точная версия метафоры «шероховатая стена становится гладкой, когда мы отходим»:

> стена не меняется; меняется масштаб, на котором её можно различить.

Так же и здесь:

> microscopic spacetime не обязано становиться continuous. Continuous metric может быть эффективным языком, которым coarse observer описывает огромное число unresolved quantum bits.

Но на этом сказка не заканчивается.

Smooth geometry ещё должна obey correct gravity constraints.

Constraint spectrum ещё не physical time.

Physical projector ещё должен иметь continuum limit.

Physical history должна породить `Gamma[g,A,...]`.

Из неё должны независимо выйти graviton kernel, Maxwell kernel, Newton constant, cosmological background и electromagnetic stiffness.

И уже после этого — blind experiment.

Современная конечная машина поэтому выглядит так:

```text
binary distinction
 -> route combinatorics
 -> local topology
 -> tetrahedral quantum geometry
 -> global spatial phase
 -> dimension
 -> causal/history scaling
 -> observer coarse graining
 -> smooth effective metric
 -> quantum constraints
 -> physical projector
 -> history / boundary amplitudes
 -> 1PI effective action
 -> physical graviton + photon kernels
 -> constants and correlations
 -> blind data
```

Если microscopic history calculation проходит эти gates, candidate theory получает настоящую physical prediction.

Если нет — соответствующая ветка должна быть отвергнута.

Так и должна заканчиваться научная сказка для взрослых: **не обещанием, что герой обязательно победит, а экспериментом, которому позволено решить финал.**