# От одного различия к пространству, времени, гравитации, свету и эксперименту

## Большая научная сказка-путешествие для взрослых учёных детей

> **Канонический обзор: 28 августа 2026. Candidate theory.**
>
> Это не заявление «мы доказали теорию всего». Это подробная карта исследовательского путешествия: что в репозитории уже доказано точно, что прошло конечные вычислительные проверки, что выдержало held-out тест, что зависит от дополнительной гипотезы, что оказалось тупиком, а где дорога пока действительно обрывается.
>
> Главный закон этой книги прост: **красивая формула не становится физикой, пока между её символами и наблюдаемым миром нет выведенного моста.**

---

# Самая короткая версия сказки

Представьте, что нам запретили начинать с готовой Вселенной.

Нельзя заранее написать:

```text
x, y, z, t
```

Нельзя нарисовать решётку.

Нельзя положить на стол линейку.

Нельзя сказать: «вот маленький кубик пространства».

Можно начать только с минимального различия:

```text
0 или 1
```

А потом спросить:

> Может ли огромное количество таких различий, если они связаны одним простым правилом, коллективно начать вести себя как геометрия, пространство, время и поле?

В текущей кандидатной конструкции дорога выглядит так:

```text
РАЗЛИЧИЕ
→ binary q
→ q = 2
→ четыре route labels
→ C4
→ локальная S²
→ Walsh-тетраэдр
→ face qubits
→ Gauss closure
→ geometry qubit
→ shape + orientation
→ gluing
→ глобальная PL S³
→ exact d* = 3
→ z ≈ 1
→ 3+1-like history
→ observer coarse-graining
→ гладкая effective geometry
→ SU(2) / Peter–Weyl
→ metric / B / Urbantke / Regge
→ Hamiltonian constraints
→ HDA / ADM
→ TT spin-2 sector
→ шесть quartic Wilson observables
→ physical projector / relational history
→ source functional
→ Γ^(2)
→ physical pole
→ experiment
```

Но в 2026 году у сказки появилась ещё одна ветка:

```text
q=2 oriented C4
→ quarter-turn J, J²=-I
→ modular / integer arithmetic
→ winding
→ Z → Q → R
→ complex phase как real rotation
→ U(1)
→ |z|² precursor
→ relational projector
```

И эти две ветви теперь начинают встречаться в одном месте: **ориентация геометрии, направление истории и комплексное сопряжение**.

---

# Как читать эту книгу

Каждая важная ступень имеет один из семи статусов.

| Ярлык | Что он означает |
|---|---|
| **EXACT** | точное алгебраическое или комбинаторное утверждение в явно заявленных предпосылках |
| **FINITE PASS** | воспроизводимый конечный численный/матричный расчёт |
| **HELD-OUT PASS** | правило было заморожено до открытия проверочного результата |
| **CONDITIONAL** | результат верен при явно названной дополнительной гипотезе |
| **OPEN PHYSICAL** | математика вокруг моста есть, но сам физический мост или число ещё не получены |
| **NO-GO** | показано, что короткая красивая дорога не работает |
| **EXPERIMENT** | внешний тест природы; отсутствие такого теста не равно внутреннему доказательству |

Есть ещё одно важное разделение.

### Этаж 1 — структурный candidate core

В заявленных finite scopes репозиторий уже содержит непрерывную математическую архитектуру:

```text
binary rule → geometry → dimension → quantum geometry → constraints
→ GR/HDA controls → TT observable dictionary.
```

В этом смысле старые документы говорят `core_theory_closed_declared = true`.

### Этаж 2 — физикализация

Чтобы назвать эту архитектуру физической теорией природы, ещё нужны:

```text
настоящий physical history / rigging map
→ физический inner product
→ connected interblock history amplitude
→ Γ[g]
→ physical TT pole
→ frozen six-Wilson vector
→ один общий scale
→ blind external experiment.
```

Этот этаж **ещё не закрыт**.

Поэтому фразы

```text
структурный candidate core закрыт в объявленном scope
```

и

```text
физическая теория ещё не подтверждена и первый interacting six-vector не frozen
```

не противоречат друг другу.

---

# Карта строгих документов

README — это путешествие. Сухие доказательные книги остаются рядом:

- [`CANONICAL_THEORY_PACKAGE.md`](CANONICAL_THEORY_PACKAGE.md) — индекс внутреннего candidate package;
- [`BIT_TO_SPACETIME_CENTRAL_EQUATION.md`](BIT_TO_SPACETIME_CENTRAL_EQUATION.md) — техническая цепь micro → smooth spacetime;
- [`OBSERVER_SCALE_SMOOTHING.md`](OBSERVER_SCALE_SMOOTHING.md) — масштаб наблюдателя и coarse-graining;
- [`MICRO_WALSH_QGEOM_BRIDGE.md`](MICRO_WALSH_QGEOM_BRIDGE.md) — q=2 → Walsh tetrahedron;
- [`SPATIAL_QUBIT_GEOMETRY_BRIDGE.md`](SPATIAL_QUBIT_GEOMETRY_BRIDGE.md) — face qubits → geometry qubit → gluing;
- [`GLOBAL_MANIFOLD_Q2_COMPLETION.md`](GLOBAL_MANIFOLD_Q2_COMPLETION.md) — локальная S² → canonical global S³;
- [`Q2_DIMENSION3_FIXED_POINT_CLOSURE.md`](Q2_DIMENSION3_FIXED_POINT_CLOSURE.md) — exact d* = 3;
- [`PETER_WEYL_HIGHER_SHELL_LAMBDA_RESULT.md`](PETER_WEYL_HIGHER_SHELL_LAMBDA_RESULT.md) — тяжёлая finite Peter–Weyl динамика;
- [`S4_TT_QUARTIC_COMPLETE_BASIS.md`](S4_TT_QUARTIC_COMPLETE_BASIS.md) — complete six-dimensional quartic TT space;
- [`TT_TO_REAL_PHYSICS_OBSERVABLES.md`](TT_TO_REAL_PHYSICS_OBSERVABLES.md) — перевод frozen TT pole в реальные observables;
- [`THEORY_STATUS.md`](THEORY_STATUS.md) и [`theory_gates.json`](theory_gates.json) — старший ledger main-ветки.

История README тоже не стирается. Она лежит в [`docs/archive`](docs/archive/).

---

# ЧАСТЬ I. До пространства ещё очень далеко

## Глава 1. Бит — не маленький кирпичик Вселенной

### На пальцах

Когда говорят «пространство может быть дискретным», мозг сразу рисует Minecraft:

```text
[куб][куб][куб]
[куб][куб][куб]
```

Но это нечестный старт.

Чтобы нарисовать куб, мы уже должны знать:

- что такое три направления;
- что такое длина;
- что такое угол;
- что значит «рядом»;
- как сравнивать размеры.

То есть геометрия уже тайком присутствует.

В этой модели фундаментальный bit означает гораздо меньше:

> есть минимальное различие между двумя альтернативами.

Classical label:

```text
0 / 1
```

Quantum carrier:

```text
|ψ> = α|0> + β|1>,   |α|² + |β|² = 1.
```

Но qubit пока не знает, где он находится. У него ещё нет координат.

**Статус:** STARTING ANSATZ. Бинарная различимость — минимальная гипотеза модели, не экспериментально найденный «атом пространства».

---

## Глава 2. Пространство должно родиться из отношений

Одна нота не образует мелодию.

Одна точка не образует геометрию.

Нужны отношения:

```text
кто с кем связан
какие переходы разрешены
какие пути эквивалентны
как связи повторяются
```

Поэтому microscopic object в route-family беднее готового пространства:

```text
binary labels
+ causal endpoints
+ adjacency
+ recursive rewrite.
```

Только после этого мы спрашиваем, можно ли из коллективных observables восстановить площади, объёмы, метрику и кривизну.

---

## Глава 3. Сколько бинарных различий должно жить в одной локальной клетке?

Пусть их `q`.

Тогда число возможных binary routes:

```text
2^q.
```

Каждый route отличается одним битом от `q` Hamming-neighbours и связан ещё с двумя causal endpoints.

Его degree:

```text
q + 2.
```

Каждый endpoint видит все routes:

```text
2^q.
```

Если потребовать локальную valence-homogeneity:

```text
q + 2 = 2^q.
```

Проверяем целые q ≥ 1:

```text
q=1: 3 != 2
q=2: 4  = 4
q=3: 5 != 8
q=4: 6 != 16
...
```

Получаем единственное решение:

$$
q=2.
$$

**EXACT:** уникальность q=2 верна внутри объявленного binary-route family.

Это не утверждение, что любая мыслимая квантовая гравитация обязана начинаться с двух битов.

---

# ЧАСТЬ II. Четыре labels находят геометрию

## Глава 4. Четыре состояния сначала строят квадрат

При q=2:

```text
00, 01, 10, 11.
```

Соединяем labels Hamming distance one.

Получаем C4:

```text
00 —— 01
|       |
10 —— 11
```

Это ещё не пространство. Это только relational skeleton.

Но у него уже есть циклическая структура, к которой мы вернёмся намного позже — когда будем выводить complex phase.

---

## Глава 5. Квадрат получает два causal полюса и превращается в S²

Добавим два endpoints, каждый соединён со всеми четырьмя route states.

Поверхность полученного octahedron имеет:

```text
V=6, E=12, F=8,
χ = 6-12+8 = 2.
```

Это simplicial sphere S².

Почему это важно?

У внутренней вершины обычного combinatorial 3-manifold link должен быть S².

Поэтому впервые появляется геометрическая стрелка:

```text
binary homogeneity
→ q=2
→ octahedral S² local link.
```

**EXACT:** локальная оболочка q=2 имеет правильный topology type для вершины 3D PL-space.

Но локальная сфера ещё не доказывает глобальное пространство.

---

## Глава 6. Те же четыре labels неожиданно рисуют правильный тетраэдр

Четыре labels являются элементами:

```text
Z₂² = {00,01,10,11}.
```

У этой группы есть три нетривиальных real Walsh characters.

Строим:

$$
Phi(g) = (χ01(g), χ10(g), χ11(g))/sqrt(3).
$$

Character orthogonality даёт точно:

```text
Σ_g Phi(g) = 0
|Phi(g)| = 1
Phi(g)·Phi(h) = -1/3   при g != h.
```

А это ровно Gram geometry четырёх одинаковых нормалей правильного тетраэдра.

### На пальцах

Представьте правильный тетраэдр и четыре стрелки из центра к центрам граней.

Они:

- одинаковой длины;
- одинаково наклонены друг к другу;
- в сумме дают ноль.

Именно такой набор произвели binary characters.

То есть тетраэдр здесь не был нарисован после ответа. Он выпал из algebra q=2 labels.

**EXACT:** `Z₂² → 3 Walsh characters → regular tetrahedral frame`.

---

## Глава 7. Из нормалей появляются face qubits

Для каждой derived unit normal `n_f` вводим:

$$
rho_f = (I + n_f·sigma)/2.
$$

Теперь Bloch direction не fitted continuum arrow. Она пришла из binary label.

Gate проверяет:

```text
flux closure norm                  = 0
regular tetrahedron Gram error     < 1e-14
Gauss-singlet weight               = 2/9
logical oriented volume            = sqrt(3)/4
reconstructed edge spread          = 0.
```

Получается первая длинная цепочка без готовой метрики на входе:

```text
binary label
→ Walsh direction
→ face flux
→ face qubit
→ gauge-invariant geometry support.
```

---

## Глава 8. Четыре face qubits прячут один geometry qubit

Four spin-1/2 decompose as:

```text
(1/2)^⊗4 = 2×j=0 ⊕ 3×j=1 ⊕ 1×j=2.
```

Gauss law требует total spin zero.

Singlet sector имеет dimension 2.

А двумерное Hilbert space — это один logical qubit:

```text
4 face qubits
→ Gauss projection
→ 1 geometry qubit.
```

Gauss penalty

```text
H_G = λ J_tot²
```

даёт exact spectrum:

```text
0          ×2
2λ         ×9
6λ         ×5.
```

Geometry sector отделён gap `2λ` от gauge-violating states.

**EXACT:** dimension и spectrum этого finite carrier.

---

## Глава 9. У geometry qubit три оси, но они означают разные вещи

В natural singlet basis:

```text
X_L, Z_L  → intrinsic shape / dihedral data
Y_L       → orientation pseudoscalar.
```

Например:

$$
J_1·J_2 = -I/4 - Z_L/2,
$$

$$
J_1·J_3 = -I/4 + Z_L/4 - sqrt(3) X_L/4.
$$

А oriented triple product:

$$
Q_or = J_1·(J_2×J_3) = sqrt(3) Y_L/4.
$$

Поэтому eigenvalues signed volume:

$$
±sqrt(3)/4.
$$

Это важнейшая развилка всей книги:

```text
X,Z меняют intrinsic geometry;
Y меняет ориентацию mirror branch.
```

Позже это спасёт нас от ошибки «ориентация = обычная metric perturbation».

---

## Глава 10. Из fluxes можно восстановить настоящий тетраэдр

Пусть `a,b,c` — три edge vectors из одной вершины.

Oriented area vectors:

```text
E1 = (b×c)/2
E2 = (c×a)/2
E3 = (a×b)/2.
```

Соберём `C=(2E1,2E2,2E3)`.

Тогда:

```text
C = det(A) A^(-T)
```

и поэтому:

$$
A = sqrt(|det C|) C^(-T).
$$

Это уже literal bridge:

```text
flux observables
→ edge geometry.
```

Finite controls восстанавливают nondegenerate tetrahedra до machine precision.

---

## Глава 11. Первый дракон: одинаковые площадь и normal ещё не означают одинаковую грань

Две triangles могут иметь:

```text
same area
same normal
```

и всё равно различную intrinsic shape.

Это twisted-geometry problem.

Negative control специально строит две equal-area triangles и получает:

```text
area mismatch = 0
shape defect ≈ 0.2593.
```

Поэтому smooth gluing требует одновременно:

```text
closure defect → 0
shape mismatch → 0.
```

**NO-GO:** «совпали площади и normals, значит уже получилась Regge geometry» — неверно.

---

## Глава 12. Как две клетки договариваются о общей грани

Для соседних geometry qubits Bell state

```text
|Phi+> = (|00>+|11>)/sqrt(2)
```

имеет:

```text
<XX> = +1
<ZZ> = +1
<YY> = -1.
```

То есть intrinsic shapes согласованы, а outward orientation разворачивается на общей face.

Минимальный gluing Hamiltonian:

```text
H_glue = -J (XX - YY + ZZ)
```

имеет spectrum:

```text
-3J, +J, +J, +J
```

и unique Bell-glued ground state с gap `4J`.

Это не доказательство, что именно этот Hamiltonian фундаментален. Это exact local positive control правильного gluing pattern.

---

# ЧАСТЬ III. Одна клетка становится пространством

## Глава 13. LEGO-кирпич ещё не дом

Один тетраэдр может иметь прекрасную геометрию и всё равно не давать manifold.

Нужны:

- shared faces;
- two-sided incidence;
- согласованная orientation;
- правильные links;
- глобальная topology.

В candidate construction берётся наиболее экономичный canonical completion локальной q=2 shell.

---

## Глава 14. Каноническая глобализация — boundary 16-cell

Boundary 4D cross-polytope имеет:

```text
V=8
E=24
F=32
T=16.
```

Именно здесь:

```text
vertex link   = S²
edge link     = S¹
triangle link = S⁰
каждая triangle принадлежит двум tetrahedra.
```

Homology over F₂:

```text
β = (1,0,0,1).
```

Это ожидаемая homology S³.

Complex orientable.

Поэтому в объявленной completion:

$$
M^3 ≅ S^3.
$$

**EXACT / FINITE PL:** existence и incidence проверены.

**OPEN:** bare causal graph сам по себе пока не доказан как единственный механизм, который обязан выбрать именно эту global face pairing.

---

## Глава 15. Почему именно 16 tetrahedra выглядят естественно

У seed cross-polytope восемь vertices образуют четыре antipodal pairs.

Flag tetrahedron выбирает по одной вершине из каждой пары.

Количество choices:

```text
2^4 = 16.
```

Получается 16 tetrahedral cells без ручного списка.

Dual graph этих cells — Q4.

На shared faces q=2 carrier labels совпадают, orientation alternates, outward Walsh fluxes cancel pairwise.

---

## Глава 16. Пространство можно дробить, не разрушая manifold

Barycentric subdivision даёт:

```text
g=0: 16 tetrahedra
g=1: 384
g=2: 9216.
```

Полные counts:

| уровень | V | E | F | T | bad links |
|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 24 | 32 | 16 | 0 |
| 1 | 80 | 464 | 768 | 384 | 0 |
| 2 | 1696 | 10912 | 18432 | 9216 | 0 |

На каждом проверенном уровне:

```text
∂² = 0
faces two-sided
orientation consistent
χ(M³)=0.
```

Это important stability test: continuum refinement не разваливает topology случайно.

---

# ЧАСТЬ IV. Почему пространство получает размерность три

## Глава 17. Размерность нельзя просто объявить

Можно построить graph с красивым S²-link и всё равно ошибиться в effective growth.

Поэтому topology и scaling проверяются независимо.

В q-route rewrite один causal length step удваивается, а число active causal descendants растёт как `2^(q+1)`.

Для declared family fixed-point exponent:

```text
d* = q + 1.
```

При q=2:

$$
d* = 3.
$$

---

## Глава 18. Тройка теперь не extrapolation, а exact sequence

Для frozen q=2:

$$
N_g = (4·8^g + 10)/7.
$$

Finite-step exponent:

$$
d_g = log_2(N_g/N_(g-1)).
$$

Его можно переписать:

$$
d_g = 3 + log_2(1 - 35/(16·8^(g-1)+40)).
$$

Отсюда точно:

```text
d_g < 3
 d_(g+1) > d_g
lim d_g = 3.
```

Числа:

```text
g=2  2.6629650127
g=3  2.9517448314
g=4  2.9938530157
g=5  2.9992297821
g=6  2.9999036938
g=7  2.9999879613
g=8  2.9999984952
```

Историческое `2.999229782...` оказалось просто g=5 этой exact ladder.

**EXACT:** fixed point `d*=3` внутри frozen rewrite family.

---

## Глава 19. У трёхмерности есть несколько независимых свидетелей

Мы имеем:

```text
local link topology      → S², значит 3D PL-neighbourhood
canonical global complex → S³
causal-volume growth     → d* = 3
finite d_H               → 2.999229782...
```

Они не являются одним и тем же test, поэтому их согласие сильнее одного красивого числа.

---

## Глава 20. Где появляется время

Spatial slice сама по себе — один кадр фильма.

Чтобы появился history, нужны последовательные causal rewrites.

Frozen finite dynamics дала:

```text
z ≈ 0.998281156.
```

Исправленная notation:

```text
d_eff(slice) = d_H / z ≈ 3.004393867
```

и для одной causal-history direction:

```text
d_eff(history) = 1 + d_H/z ≈ 4.004393867.
```

То есть в этом finite scaling sense:

```text
space ≈ 3
history ≈ 3+1.
```

**FINITE PASS:** `z≈1` — измеренная dynamical scaling property candidate, а не доказательство physical Lorentz invariance.

---

# ЧАСТЬ V. Почему микроскопическая шероховатость может выглядеть гладкой

## Глава 21. Стена

Подойдите к штукатурной стене вплотную.

Вы увидите:

```text
песчинки
поры
микротрещины
царапины
неровности.
```

Отойдите далеко — получите почти идеальную плоскость.

Но стена не перестроилась, когда вы отступили.

Изменилось только отношение:

```text
размер микродетали / resolution наблюдения.
```

Так же надо читать фразу:

> «дискретное пространство-время на больших масштабах становится гладким».

Microscopic state не меняется из-за расстояния до наблюдателя. Меняется effective resolution.

---

## Глава 22. Формула наблюдателя

Обозначим microscopic cutoff:

```text
ell_*.
```

Мы **не** объявляем автоматически `ell_* = Planck length`.

Для angular/causal resolution `theta` и separation `r` используем model map:

$$
ell_obs(r) = sqrt(ell_*² + (theta r)²).
$$

Dyadic coarse factor:

$$
b(r) = 2^{floor(log_2(ell_obs/ell_*))}.
$$

Если `theta r << ell_*`, observer может различать microscopic structure.

Если `theta r >> ell_*`, один observable cell содержит много microscopic cells.

---

## Глава 23. Почему roughness падает примерно как b^-2

В 3+1-like history block число microscopic contributions примерно:

```text
N(b) ~ b^(d_H+z) ≈ b^4.
```

Если relevant fluctuations zero-mean и достаточно weakly correlated:

```text
RMS noise ~ 1/sqrt(N).
```

Поэтому:

$$
delta g_RMS ~ b^-2.
$$

Это математическая версия стены: всё больше песчинок усредняются внутри одного pixel.

---

## Глава 24. Производные сглаживаются ещё быстрее

Одна derivative на block scale добавляет примерно `b^-1`:

```text
δg        ~ b^-2
∇δg       ~ b^-3
δR_proxy  ~ b^-4.
```

Measured candidate controls:

```text
δg        ~ b^-2.001707
∇δg       ~ b^-3.001458
δR        ~ b^-4.000524
simplicity defect ~ b^-1.994838
Urbantke defect   ~ b^-2.019746.
```

**FINITE PASS:** сильная согласованность declared control.

**Не universal theorem:** long-range correlations могут менять exponents.

---

## Глава 25. Второй дракон: coarse-graining не создаёт размерность

Старый dimension-blind binary diamond при coarse-graining оставался около spectral dimension:

```text
d_s ≈ 2.07.
```

То есть усреднение само по себе не превращает любую сеть в 4D spacetime.

Правильное разделение:

```text
topology + rewrite growth → dimension
coarse-graining            → smoothness.
```

**NO-GO:** «мы отошли далеко, значит автоматически появились четыре измерения».

---

## Глава 26. Гладкое не означает классическое и пустое

Coarse mean field может быть smooth, а quantum correlations оставаться ненулевыми.

Это как спокойная поверхность моря: средняя высота почти гладкая, но волновой correlation function не исчезает.

Поэтому IR smoothness не разрешает нам выбросить quantum two-point functions.

Именно эти correlations позже важны для TT vacuum и optical phase visibility.

---

# ЧАСТЬ VI. Геометрия учится говорить на языке SU(2)

## Глава 27. Почему SU(2), но не «готовая Lorentz group»

Один qubit естественно несёт SU(2) algebra через Pauli observables.

Это хороший carrier для spatial Ashtekar-Barbero geometry.

Но finite SU(2) qubit **не равен** full Lorentzian SL(2,C) spacetime connection.

Поэтому architecture честно разделяет:

```text
spatial SU(2) quantum geometry
+ causal/history dynamics
+ Lorentzian/HDA tests.
```

Lorentzian physics должна появиться динамически, а не из переименования SU(2).

---

## Глава 28. Graph-change добавляет «пустое состояние»

Четыре active q=2 states сами по себе не дают весь нужный endpoint representation.

Добавим no-link / j=0 state.

Получается exact decomposition:

```text
(2,2) + (1,1)
```

в SO(5)-vector language.

Самое важное transporter identity:

```text
P_g U_a P_0 U_b P_g = |a><b|.
```

То есть Hamming transition между active states можно факторизовать как:

```text
active
→ no-link
→ active.
```

Позже именно этот двухтактный history даст первый C4→C8 reversible lift.

---

## Глава 29. Peter–Weyl tower появляется при symmetric blocking

Если occupancy n блокируется полностью симметрично:

```text
Sym^n(C²) → j=n/2.
```

Dimension:

```text
(2j+1)² = (n+1)²
```

для diagonal left/right Peter–Weyl block.

Поэтому occupancies `n=0..N` дают tower:

```text
j=0, 1/2, 1, 3/2, ... N/2.
```

**CONDITIONAL EXACT:** representation identity точна при declared symmetric blocking; динамический выбор именно этого blocking measure остаётся более сильным вопросом.

---

## Глава 30. Geometry qubit превращается в metric tangent

У regular tetrahedron background:

```text
g0 = [[2,1,1],
      [1,2,1],
      [1,1,2]].
```

Exact Jacobians `M_X`, `M_Z` имеют:

```text
rank 2
trace-free
orthogonal
same norm.
```

DeWitt inner product:

$$
Tr(g0^-1 M_A g0^-1 M_B) = (3/2) delta_AB.
$$

Это literal bridge:

```text
logical shape X,Z
→ metric perturbation.
```

---

## Глава 31. Но orientation Y не является линейной intrinsic metric perturbation

У двух mirror regular branches:

```text
(X,Z,Y)=(0,0,+1)
(X,Z,Y)=(0,0,-1)
```

intrinsic metric одна и та же.

Exact:

$$
partial g / partial Y = 0.
$$

Full XYZ Gram matrices:

```text
Frobenius: diag(9/2, 0, 9/2)
DeWitt:    diag(3/2, 0, 3/2).
```

**NO-GO:** будущий orientation/history coupling нельзя просто засунуть в linear intrinsic metric Γ^(2) как ещё один TT coefficient.

Orientation-sensitive physics должна сохранять triad/frame/connection/extrinsic-curvature/history information либо появляться nonlinear.

---

# ЧАСТЬ VII. Пять spin-2 metric modes и первое 8-процентное число

## Глава 32. Traceless metric — пять компонентов

В tetrahedral symmetry traceless metric sector decomposes:

```text
5 = E(2) ⊕ T2(3).
```

На first refined q4 metric compression получено:

```text
lambda_E  = 1.1111917875584736
lambda_T2 = 1.0220278507464782
Delta_ET  = 0.08916393681199541.
```

Если нормировать с учётом degeneracy 2+3:

```text
kappa = (2 lambda_E + 3 lambda_T2)/5
      = 1.0576934254712764

Delta_ET/kappa = 0.08430036026012608
                ≈ 8.430036%.
```

В старом package встречается simple two-eigenvalue mean normalization, дающая около 8.36%. Это **другая normalization convention**, не физическое расхождение.

---

## Глава 33. Что означает 8.43%, а чего оно не означает

Оно означает:

> finite local Euclidean tetrahedral split между E и T2 spin-2 metric channels.

Оно **не означает автоматически**:

```text
zeta4 = 0.0843
скорость гравитона отличается на 8.43%
масса частицы = 8.43% другой массы
Lorentz violation = 8.43%.
```

Чтобы получить physical dispersion, нужен momentum/history/RG/TT bridge.

---

## Глава 34. Третий дракон: из 8.43% нельзя сделать lepton masses

Для irreducible S4 triplet Schur lemma говорит:

```text
S4-invariant mass matrix = m I_3.
```

Даже scalar term, построенный из tetrahedral Q_tet на irreducible T2, остаётся пропорциональным identity в generation triplet.

Поэтому:

```text
8.43%
≠ electron/muon/tau hierarchy.
```

Нужны отдельно выведенные:

- matter representations;
- chirality;
- flavor representation;
- symmetry-breaking spurion/operator;
- Yukawa normalization.

**NO-GO:** нумерологический поиск степеней `0.0843` для известных масс запрещён самим representation theorem.

---

## Глава 35. Geometry-only blocking не умеет тайком лечить anisotropy

Для recursive PL Laplacian:

$$
P^T L_(g+1) P = L_g/4
$$

с machine-level residual.

Если internal dynamics factorizes как `L ⊗ J`, все internal couplings масштабируются одинаково.

Их ratio не течёт.

Значит настоящий RG flow E/T2 должен приходить из:

```text
Peter–Weyl recoupling
nonseparable blocking
interblock dynamics,
```

а не из геометрического resize.

**NO-GO:** «refinement само собой сделает локальную anisotropy нулевой».

---

# ЧАСТЬ VIII. Две дороги к Einstein geometry

## Глава 36. Дорога B-field → Urbantke metric

Одна end-to-end control chain:

```text
face qubits
→ B two-forms
→ simplicity
→ Urbantke metric
→ compatible connection
→ curvature
→ Einstein test.
```

Positive S4 control восстанавливает:

```text
Lambda_rec ≈ 2.9999998973
Lambda_input = 3
relative error ≈ 3.42e-8.
```

Но это **не prediction cosmological Lambda=3**.

Input geometry уже имела эту curvature. Тест проверяет reconstruction pipeline.

Independent non-Einstein control проходит metric stage, но проваливает Einstein-curvature gate — значит pipeline не просто всегда отвечает «Einstein».

---

## Глава 37. Дорога Regge → Einstein-Hilbert

Вторая независимая ветка начинает с discrete edge geometry.

Regge Hessian на refinement должен приближаться к Fierz–Pauli / Einstein-Hilbert tensor structure.

Leading finite-spacing errors ведут себя примерно как:

```text
O(a²).
```

Особенно важен held-out residue test.

---

## Глава 38. Held-out L=6 — редкий момент, когда теория заранее подписала ответ

Frozen rule:

```text
Z_L = 1/8 + C/L² + D/L⁴
```

fit только по:

```text
L=3,4,5.
```

До открытия L=6 prediction:

```text
Z6_pred = 0.11876923193907167.
```

Independent result:

```text
Z6_obs  = 0.11876075461190198.
```

Relative error:

```text
≈ 0.00714%.
```

**HELD-OUT PASS:** внутренний numerical continuation test без refit на L=6.

Это не external confirmation природы, но это гораздо сильнее post-hoc fit.

---

# ЧАСТЬ IX. Hamiltonian constraint входит в историю

## Глава 39. Гравитация — не обычная система с внешними часами

В школьной quantum mechanics можно написать:

```text
i dψ/dt = H ψ.
```

В generally covariant gravity время не должно быть внешней сценой, на которой играет сама spacetime.

Canonical theory содержит constraints:

```text
H[N] |Psi_phys> ≈ 0
D[N^a] |Psi_phys> ≈ 0.
```

Это принципиально меняет физический смысл спектра H.

---

## Глава 40. Euclidean и Lorentzian половины

Ashtekar–Barbero connection:

```text
A = Gamma + beta K.
```

Classical derivative-free kinetic pieces satisfy:

```text
H_E^kin = -beta² Q_DW
H_L^corr = (1+beta²) Q_DW
```

и вместе:

```text
H_E^kin + H_L^corr = Q_DW.
```

Это exact classical beta-cancellation control правильного DeWitt kinetic structure.

**Не доказано:** full quantum beta-independence.

---

## Глава 41. Что такое HDA — на пальцах

Представьте мягкий лист.

Сначала чуть толкнём его «вперёд по normal» функцией N(x), потом M(x).

Затем поменяем порядок.

В General Relativity разница не должна создавать новую физику из воздуха. Она должна быть эквивалентна tangential deformation самого slice.

Symbolically:

$$
[H[N],H[M]]/(i hbar)
→ D[q^(ab)(N d_b M - M d_b N)].
$$

Поэтому HDA — очень сильный test: правильный spectrum без правильной deformation algebra ещё не GR.

---

## Глава 42. Теория встречает дракона cutoff

Старый oriented K5 finite model при `Jmax=1/2` сделал полезную вещь: **провалил физический HDA test**.

Orientation correction восстановила permutation covariance, но graph-changing anomaly осталась большой:

```text
epsilon_graph = sqrt(37/69) ≈ 0.7323.
```

Fixed-sector commutators показали красивый projected SO(5) skeleton, но огромный orthogonal remainder:

```text
epsilon_Lie ≈ 0.998315.
```

Это могло бы выглядеть катастрофой.

Но reachability theorem показал:

```text
safe Euclidean HH wall = Jmax 5/2.
```

А расчёт использовал `Jmax=1/2` — слишком низкий cutoff.

Урок:

> finite truncation может создавать anomaly; сначала докажи support-safe wall, потом суди физику.

**FINITE FAIL как physical HDA at Jmax=1/2; не failure всей Peter–Weyl architecture.**

---

## Глава 43. Safe windows и scaling

В более зрелых two-/three-node gates:

```text
route channel          ~ epsilon
cross channel          ~ epsilon
pure geometry channel  ~ epsilon²
joint defect            decreases approximately ~ epsilon.
```

Для fixed-cutoff habitat theorem:

```text
C_cross / D = O(epsilon)
C_GG    / D = O(epsilon²).
```

Conservative joint family также записана, но это **не uniform theorem для любого графа и любого regulator path**.

ADM local family selects:

```text
c = 1/2
A B = 1.
```

Она не выбирает absolute Newton G и не вычисляет cosmological Lambda.

---

# ЧАСТЬ X. Peter–Weyl поднимается на второй этаж

## Глава 44. Почему первый return не вся история

Пусть P — logical coarse sector, H — finite Peter–Weyl constraint.

Parity даёт:

```text
P H P = 0.
```

Первый ненулевой возврат:

```text
K = P H² P.
```

Но после него есть следующий shell.

Определим:

```text
M = P H⁴ P - K²
Lambda = K^(-1/2) M K^(-1/2).
```

Это denominator-free next-shell observable.

---

## Глава 45. Тяжёлый 32D calculation оказался не scalar

На safe second-hit wall `Jmax=5/2`:

```text
rank K = 32
lambda_min(K) = 4.3060759870
lambda_max(K) = 13.3527813527
cond(K) = 3.1009163315.
```

`M` positive:

```text
lambda_min(M) = 47.9777767497
lambda_max(M) = 186.9023442232.
```

For Lambda:

```text
min = 10.6357598783
max = 15.0599276660
mean = 12.8604431134
std = 1.2195317610
relative distance from scalar I = 0.0944046183.
```

Block-Lanczos reconstructions close at ~`1e-13`.

**FINITE PASS:** genuine non-scalar finite constraint dynamics.

---

## Глава 46. Orientation survived normalization

After environment trace/canonical pair frame:

```text
shape coupling       = -0.3629900151
orientation coupling = +0.7912767589
Delta                = +1.1542667740.
```

Largest nonidentity pair coefficient is orientation-like `IIIYY`.

Это означает: higher-shell dynamics не стирает structure в scalar identity.

Но это **не** particle mass spectrum и **не** physical Lorentz violation.

---

## Глава 47. Четвёртый дракон: constraint spectrum — не physical frequency

Можно построить exact Feshbach/Block-Lanczos resolvent:

```text
G_constraint(z) = Q0† (z-H)^(-1) Q0.
```

И exact K/A/B identities.

Но `z` здесь — spectral variable constraint operator.

Мы **не имеем права** просто переименовать:

```text
z → omega.
```

Правильный путь:

```text
constraint
→ physical projector / rigging map / relational clock
→ history amplitude
→ source functional Z[J]
→ W[J]
→ Γ[g]
→ Γ^(2)_metric
→ TT pole K_TT(omega,k).
```

**NO-GO:** `constraint resolvent = physical graviton propagator` без history/clock bridge.

---

# ЧАСТЬ XI. Первый настоящий TT язык

## Глава 48. Reduced TT positive control

В reduced lattice model:

$$
G_TT(omega,k)
= 1 / { Z_T [4 sin²(omega/2) - (1/3) Σ_i 4 sin²(k_i/2) + i0] }.
$$

В polarization basis numerator — `delta_AB`.

Leading pole massless.

Small-k bare directional quartic controls:

```text
(100): -1/18
(110): -1/72
(111):  0.
```

Restricted cubic decomposition:

```text
eta2_bare  = -1/45
zeta4_bare = -1/12.
```

**Важно:** это bare/reduced positive-control coefficients, не final interacting physical prediction.

---

## Глава 49. Vacuum two-point function исправил старую красивую ошибку

Прямой equal-time Gaussian calculation даёт:

```text
P_TT(k) ~ k^-1
```

с slope практически `-1`.

Раньше smoothing exponent был слишком быстро интерпретирован как другой TT spectrum.

Прямой propagator calculation эту интерпретацию отверг.

Так и должна жить теория: более прямой observable имеет приоритет над красивой аналогией.

---

# ЧАСТЬ XII. Почему физическому гравитону нужны шесть ручек

## Глава 50. Onsite symmetry проще, чем momentum symmetry

На одном tetrahedral block при `k=0` six-edge kernel действительно имеет три orbit numbers:

```text
C6^(0) = a I + b A_adj + c O_opp.
```

Но generic directed momentum сам трансформируется.

Правильная covariance:

$$
C(g k) = U_g C(k) U_g^-1.
$$

Нельзя требовать `C(gk)=C(k)` для фиксированного generic direction.

---

## Глава 51. До TT constraints существует 13 quartic structures

Traceless metric carrier:

```text
H5 = E ⊕ T2.
```

Representation theory:

```text
Sym²(H5)   = 2A1 ⊕ 2E ⊕ T1 ⊕ 2T2
Sym⁴(T2_k) = 2A1 ⊕ 2E ⊕ T1 ⊕ 2T2.
```

Number of singlet pairings:

```text
2² + 2² + 1² + 2² = 13.
```

То есть одна `Q_tet` или два eta/zeta параметра — только restricted hypotheses.

---

## Глава 52. TT quotient сокращает 13 до шести

Physical tensor constraints:

```text
tr(h)=0
h_ij k_j=0.
```

Exact polynomial/Reynolds computation:

```text
TT ideal rank          = 222
invariant + ideal rank = 228
quotient dimension     = 6.
```

Поэтому:

$$
dim W_TT,S4^(4) = 6.
$$

Это один из главных exact observability results репозитория.

---

## Глава 53. Шесть Wilson coefficients — это не шесть fitted knobs

Choose canonical Reynolds basis `W1...W6`.

General parity-even quartic physical response:

```text
delta K_TT^(4) = Z_T c_T² a_*² Σ_r c_r W_r.
```

Six `c_r` — complete coordinates в заявленном symmetry class.

Их надо frozen extraction protocol определить **до** открытия microscopic data, иначе basis selection превратится в fit.

---

## Глава 54. Три красивых directions почти хватили — но только почти

Directions:

```text
(100), (110), (111)
```

дают только rank 5.

Одна quartic TT direction остаётся невидимой.

Добавляем заранее выбранную generic:

```text
(120).
```

И extraction matrix становится full rank:

$$
det A = 1/699840000 != 0.
$$

Теперь six-vector uniquely reconstructible.

**EXACT:** extractor frozen до будущих physical microscopic data.

---

## Глава 55. Старые eta/zeta не выброшены — они стали nested hypothesis

Restricted ansatz:

```text
e4(n) = eta2 + zeta4 Q4_cub(n).
```

Если microscopic six-vector действительно лежит в этом subspace:

```text
zeta4 = 2(e100-e110)
eta2  = (e100+4e110)/5
```

и held-out relation:

```text
e100 - 4 e110 + 3 e111 = 0.
```

Если relation не проходит — мы не подгоняем eta/zeta. Просто публикуем full six-vector.

---

## Глава 56. Тетраэдральная birefringence тоже только nested test

For single-Q_tet submodel TT eigenvalues:

```text
(100): { 3/5, -2/5 }
(110): { 7/20, -2/5 }
(111): { -1/15, -1/15 }.
```

Если coefficient `gamma4` этого одного operator действительно selected:

```text
zeta4 = gamma4/4
polarization splitting ratio = 4 : 3 : 0.
```

Это сильный zero-fit fingerprint, **если** nested submodel проходит.

---

## Глава 57. Field redefinitions не увеличивают physical pole space

Off-shell action может содержать больше `omega⁴`, `omega²k²` bookkeeping terms.

Но local field redefinition shifts quartic kernel pieces proportional to leading equation of motion.

На massless leading pole они исчезают.

Поэтому six-dimensional **on-shell pole quotient** остаётся правильным physical target.

---

# ЧАСТЬ XIII. Как six-vector однажды станет измеряемым

## Глава 58. Если physical pole frozen, перевод в observables уже готов

Suppose future physical TT branches:

```text
omega_sigma² = c² k² [1 + a_*² k² e4_sigma(n) + ...].
```

Then:

```text
(v_g,sigma - c)/c = (3/2) a_*² k² e4_sigma(n)
```

и accumulated phase:

```text
delta_phi_sigma = -(1/2) L a_*² (omega/c)³ e4_sigma(n).
```

В modified-dispersion notation:

```text
E² = (pc)² + A_alpha (pc)^alpha
```

quartic correction соответствует:

```text
alpha = 4.
```

Translator code уже существует. Он не fitting engine.

---

## Глава 59. Почему остаётся ровно один общий scale

Microscopic counting даёт dimensionless numbers.

Чтобы превратить integer/additive count `N` в dimensionful quantity `Q`, additivity:

```text
Q(N+M)=Q(N)+Q(M)
```

на integers заставляет:

```text
Q(N)=s N.
```

Остаётся один slope `s`.

В gravity scale language:

```text
a_*² = 8 pi lambda_R_eff ell_P².
```

Correct protocol:

1. сначала frozen dimensionless six-vector;
2. потом либо derive scale из microscopic principle;
3. либо ровно один declared physical datum calibrates общий scale;
4. остальные observables становятся held-out.

**NO-GO:** отдельный scale fitting для каждого эффекта.

---

# ЧАСТЬ XIV. Свет появляется как фаза, но ещё не как готовый фотон

## Глава 60. Qubit ray носит U(1) fiber

Normalized two-component state lives on S³.

Physical ray quotient:

```text
S³ / U(1) = CP¹ ≅ S².
```

Это Hopf fibration:

```text
U(1) → S³ → S².
```

Link phase:

```text
U_vw = <psi_v|psi_w> / |<psi_v|psi_w>|.
```

Under local phase changes it transforms как compact lattice U(1) connection.

Closed loop gives Pancharatnam/Berry holonomy.

**EXACT KINEMATIC:** compact phase carrier есть.

---

## Глава 61. Пятый дракон: U(1) topology ещё не Maxwell photon

Чтобы получить physical electromagnetism, нужны:

```text
dynamical action
Gauss law in the correct physical Hilbert
propagating deconfined transverse modes
Maxwell stiffness Z_A
common spacetime light cone.
```

Topology alone не даёт coupling strength.

В effective action convention:

```text
Gamma_A = - (Z_A/4) ∫ F².
```

If unit compact charge convention:

```text
e = 1/sqrt(Z_A)
alpha = 1/(4 pi Z_A).
```

Значит `1/137` появляется только после microscopic derivation `Z_A`.

**NO-GO:** Hopf U(1) → alpha by numerology.

---

## Глава 62. Optical phase — хороший bridge к quantum geometry

Если geometry perturbation меняет optical path:

```text
delta_phi ~ k ell_* × geometry observable.
```

Single-photon interferometer gives probabilities:

```text
P_± = (1 ± cos Delta_phi)/2.
```

Если geometry quantum:

```text
visibility = |<exp(i Delta_phi_hat)>|.
```

То есть даже когда mean metric smooth, quantum geometry correlations могут проявляться в phase noise/visibility.

Это будущая experimental dictionary, не текущая detection.

---

# ЧАСТЬ XV. Неожиданная арифметическая пещера

> Следующие главы — свежий frontier 27–28 августа. Они живут в research PR #40 и последующих stacked branches. Exact statements имеют зелёные CI, но пока не все merged в `main`.

## Глава 63. А если complex numbers — не fundamental datatype?

Возьмём Gaussian modular number:

```text
a + b i   (mod N).
```

Его можно заменить обычной 2×2 matrix целых residues:

```text
[a  -b]
[b   a]
```

mod N.

Addition и multiplication сохраняются точно.

Determinant:

```text
a²+b².
```

Transpose реализует conjugation.

То есть complex arithmetic может быть representation ordinary arithmetic on a two-dimensional real/integer plane.

**EXACT:** ring embedding for every N.

---

## Глава 64. Иногда даже i распадается на два обычных modular channels

If prime:

```text
p = 1 mod 4,
```

существует root:

```text
r² = -1 mod p.
```

Then:

```text
a+bi → (a+rb, a-rb)
```

и:

```text
F_p[i] ≅ F_p × F_p.
```

If `p=3 mod4`, root нет и получается genuine quadratic field `F_(p²)`.

At p=2:

```text
(1+i)² = 0 mod2
```

— ramified nilpotent case.

Это чистая algebra, пока без physical claim о preferred modulus.

---

## Глава 65. Наш q=2 уже содержит real operator, который ведёт себя как i

Remember oriented C4.

One-step cyclic shift decomposes over reals into trivial/sign blocks and:

```text
J = [[0,-1],
     [1, 0]].
```

Exact:

```text
J² = -I.
```

То есть `i` можно читать не как магический symbol, а как:

> «поверни real phase-plane на четверть оборота».

Это очень естественный geometric meaning complex structure.

---

## Глава 66. Но Z₂² — не Z₄

Здесь легко сделать красивую ошибку.

Labels form group:

```text
Z₂ × Z₂.
```

Она **не** cyclic Z₄.

C4 возникает как adjacency graph и oriented automorphism cycle, а не как label addition group.

Правильное разделение:

```text
Z₂² character algebra → tetrahedral geometry
oriented C4 shift      → phase complex structure J.
```

**NO-GO:** отождествлять Z₂² и Z₄.

---

## Глава 67. Один reflection одновременно делает conjugation и переворачивает tetrahedron

Take C4 reversal:

```text
k → -k mod4.
```

На phase-plane:

```text
R J R^-1 = -J.
```

То есть:

```text
i → -i.
```

На тех же q=2 Walsh labels этот reflection меняет sign oriented tetrahedral determinant.

А geometry qubit:

```text
Q_or = sqrt(3) Y_L/4
```

тоже меняет sign.

Так один label reflection реализует совместно:

```text
J → -J
complex conjugation
Q_or → -Q_or
Y_L → -Y_L.
```

**EXACT compatibility.** Dynamical locking этих sectors — отдельный physical question.

---

# ЧАСТЬ XVI. Как modulo начинает вспоминать обычные числа

## Глава 68. Residue сам не знает, сколько кругов мы прошли

Residue:

```text
r mod M
```

может означать:

```text
r, r+M, r+2M, ...
```

Но полная history может хранить winding `w`.

Тогда:

```text
N = r + w M.
```

И ordinary integer восстановлен.

---

## Глава 69. History сама содержит winding

Nearest-neighbor oriented path on C_N имеет universal cover:

```text
Z → C_N.
```

После выбора initial sheet полный ordered path поднимается uniquely.

For closed path:

```text
n_T - n_0 = N w,
w ∈ Z.
```

Winding не зависит от выбора initial sheet.

**EXACT TOPOLOGICAL:** если transition history сохраняется, integer winding не надо прикручивать дополнительным counter.

---

## Глава 70. CRT собирает обычную arithmetic из нескольких modular views

Если integer bounded и известны residues по coprime moduli, Chinese Remainder Theorem восстанавливает его exactly.

То же работает componentwise для Gaussian integers.

Это показывает:

```text
many finite modular views
+ bound
→ ordinary exact integer arithmetic.
```

Rational reconstruction затем поднимает bounded residue к `a/b`, если modulus достаточно велик относительно numerator/denominator bounds.

Получаем честную лестницу:

```text
modular residues
→ Z
→ Q.
```

---

## Глава 71. Почему обычная real line требует ещё одного выбора

Finite modular arithmetic cyclic. У неё нет обычного Archimedean total order, совместимого со сложением.

После Q возникают разные notions of distance.

Congruence refinement ведёт к p-adic directions.

Обычный physical continuum получается при Archimedean absolute value:

```text
Q + |.|_infinity + Cauchy completion → R.
```

**NO-GO:** никакой один finite modulus сам по себе не содержит привычную ordered real line.

Это важный physical frontier: почему macroscopic rods/clocks выбирают именно Archimedean place, ещё надо объяснить динамически.

---

## Глава 72. После R complex numbers возвращаются как geometry

Когда real numbers уже доступны, а J²=-I уже derived:

```text
R[J] ≅ C.
```

Complex number:

```text
a+ib
```

становится real operator:

```text
a I + b J.
```

То есть complex arithmetic можно интерпретировать как real plane + orientation/quarter-turn structure.

---

# ЧАСТЬ XVII. Почему U(1) не требует бесконечно вручную добавлять корни

## Глава 73. Первый C4→C8 появляется из graph-changing history

Existing Hamming transporter уже two-stage:

```text
active → no-link → active.
```

Если различать intermediate transition events на oriented C4 edges:

```text
0 → m0 → 1 → m1 → 2 → m2 → 3 → m3 → 0
```

получаем C8 history cycle.

Но есть subtlety: один common no-link instantaneous state не хранит, из какого edge мы пришли.

---

## Глава 74. Reversibility сама требует четыре transition channels

Если reversible map:

```text
|k> → |no-link> |e_k>,
```

isometry требует:

```text
<e_k|e_l> = delta_kl.
```

Значит минимум четыре orthogonal transition channels.

Minimal reversible history dimension:

```text
4 active + 4 transition = 8.
```

**EXACT:** C8 — минимальный reversible dilation в declared class.

---

## Глава 75. Шестой дракон: independent time bit не даёт C8

Можно было бы написать:

```text
phase Z4 × clock Z2
```

и надеяться получить Z8.

Но максимальный element order в `Z4×Z2` равен 4.

Нужен linked carry:

```text
(k,0) → (k,1) → (k+1,0).
```

**NO-GO:** независимый binary clock сам по себе не удваивает phase order.

---

## Глава 76. Infinite root tower красива, но не обязательна

Если recursive edge subdivision selected на всех уровнях, можно получить:

```text
C4 → C8 → C16 → ...
```

и roots become dense in U(1).

Но all-level physical locking этого rule пока **CONDITIONAL**.

К счастью, есть короче путь.

С J²=-I и rational coefficients unit elements:

```text
a I + b J,
a²+b²=1,
a,b ∈ Q
```

уже образуют dense subgroup circle.

Pythagorean parametrization:

```text
a=(q²-p²)/(p²+q²)
b=2pq/(p²+q²).
```

Therefore:

```text
C4 + Q → dense U(1)
C4 + R → SO(2) ≅ U(1) exactly.
```

---

## Глава 77. Winding и phase оказываются dual

Closed history sectors add:

```text
w(γ1∘γ2)=w(γ1)+w(γ2).
```

Если unit-norm phase weight respects composition:

```text
Omega(w1+w2)=Omega(w1) Omega(w2),
Omega(0)=1,
```

то necessarily:

```text
Omega(w)=u^w,   u∈U(1).
```

Это character group statement:

```text
Z^ = U(1).
```

Orientation reversal:

```text
w → -w
Omega → Omega^-1 = conjugate(Omega).
```

Так winding, U(1) и conjugation оказываются одной algebraic family.

---

# ЧАСТЬ XVIII. Геометрическая ориентация выбирает направление истории

## Глава 78. Minimal orientation-resolved step

Define:

```text
P_± = (I ± Y_L)/2.
```

В narrow class deterministic nearest-neighbor, Y-conserving, simultaneous-reflection-covariant reversible lifts единственные choices — global reversals друг друга:

```text
+ orientation → U8
- orientation → U8^-1
```

или наоборот.

Therefore:

```text
W = P_+⊗U8 + P_-⊗U8^-1.
```

**EXACT under stated minimal assumptions.**

---

## Глава 79. Even и odd части W раскрывают смысл coarse Hamming dynamics

Exactly:

```text
(W+W†)/2
= I ⊗ (U8+U8^-1)/2
```

и:

```text
(W-W†)/(2i)
= Y_L ⊗ C_h,
C_h=(U8-U8^-1)/(2i).
```

То есть orientation-unresolved dynamics видит только even cosine-like part.

Orientation-resolved dynamics содержит directed sine/current part.

После двух ticks и забывания orientation возвращается исходная q=2 Hamming adjacency.

Coefficient ladder:

```text
g_YC^Hamming       = 0       EXACT after orientation quotient
|g_YC^minimal|     = 1       EXACT kinematic normalization
g_YC^gravity       = OPEN    physical.
```

Не путайте вторую единицу с gravitational coupling.

---

## Глава 80. Complex phase и real history rotation оказались одним объектом

Take history character:

```text
U|theta> = exp(i theta)|theta>.
```

Then:

```text
W(theta)
= P_+ e^(i theta) + P_- e^(-i theta)
= cos(theta) I + i sin(theta) Y_L.
```

Define:

```text
J = -i Y_L
  = [[0,-1],[1,0]],
J²=-I.
```

Then:

$$
W(theta)=exp(-theta J).
$$

Это ordinary real SO(2) rotation.

Complex history phase и real quarter-turn complex structure — один group element в двух representations.

**EXACT.** `theta` пока не называется physical frequency.

---

## Глава 81. Directed difference точно факторизует graph Laplacian

Вместо pure current берём полный one-step difference:

```text
Delta_W = W - I.
```

Exact:

```text
Delta_W† Delta_W
= I_geom ⊗ (2I-U-U†).
```

В Fourier character:

```text
Delta(theta)
= (cos theta - 1) I - sin theta J
```

и:

```text
Delta(theta)^T Delta(theta)
= 4 sin²(theta/2) I.
```

Это exact graph-Laplacian eigenvalue.

---

## Глава 82. Седьмой дракон: pure sine current имеет лишний zero

Pure current spectrum:

```text
sin(theta)
```

на C8 имеет zeros:

```text
m=0 и m=4.
```

Это lattice doubler-like phenomenon.

Но full directed difference содержит even piece:

```text
cos(theta)-1
```

автоматически и оставляет только trivial zero `m=0` в positive square.

Это algebraically Wilson-like correction, но репозиторий **не** объявляет отсюда physical fermion или Dirac equation.

---

## Глава 83. Один J проходит через все арифметические и quantum layers

Cross-layer CI проверил один и тот же exact matrix J в:

```text
q=2 C4 phase
history Fourier rotation
modular complex representation
unique quadratic phase weight
realification Hermitian dynamics
directed history Laplacian.
```

Standard realification convention:

```text
e^(+i theta) ↔ exp(+theta J)
```

current history-forward convention:

```text
W(theta)=exp(-theta J) ↔ e^(-i theta).
```

Разница — orientation convention. History reversal меняет sign theta, carrier J остаётся тем же.

---

# ЧАСТЬ XIX. Почему появляется именно |z|² — но ещё не весь Born rule

## Глава 84. Пусть weight quadratic и phase-invariant

For real phase vector `v=(a,b)`:

```text
Q(v)=v^T A v,
A=A^T.
```

Require quarter-turn invariance:

```text
J^T A J = A.
```

Это forces:

```text
A = lambda I.
```

Positivity:

```text
lambda ≥ 0.
```

Normalization `Q(1,0)=1` gives:

```text
lambda=1.
```

Thus:

$$
Q(z)=a²+b²=|z|².
$$

И interference term comes from polarization identity:

```text
|z+w|² = |z|²+|w|²+2 Re(z conjugate(w)).
```

**EXACT precursor under quadraticity/positivity/normalization assumptions.**

**Не full Born rule:** outcomes, measurement composition and physical probability measure still need derivation.

---

## Глава 85. Schrödinger equation можно полностью realify

For Hermitian:

```text
H = A + i B
```

define:

```text
R(H) = [[A,-B],
        [B, A]].
```

Hermiticity becomes real symmetry:

```text
R(H)^T = R(H).
```

And:

```text
i dψ/dt = H ψ
```

is equivalent to:

```text
dv/dt = -J R(H) v.
```

Generator real skew-symmetric → norm preserved.

Complex unitary evolution can therefore be represented as ordinary real orthogonal/symplectic flow with complex structure J.

**Representation theorem only.** It does not derive physical H or physical t.

---

# ЧАСТЬ XX. Constraint наконец получает правильную relational history

## Глава 86. Восьмой дракон: обычное group averaging убивает phase

На C8:

```text
P_avg = (1/8) Σ_t U^t.
```

Это projector на trivial character.

Все nontrivial characters уничтожаются.

На universal cover Z continuous characters вообще generalized spectral states, а не normalizable l²(Z) vectors.

Поэтому нельзя одновременно говорить:

```text
history shift — pure gauge
```

и ожидать, что ordinary untwisted averaging сохранит nontrivial phase.

**NO-GO:** physical phase требует character-resolved/relational/boundary rigging construction.

---

## Глава 87. Combined relational projector показывает правильный принцип

Finite positive control вводит отдельный C8 clock shift S и system rotation R=J.

Combined constraint:

```text
G = S_clock ⊗ R_geom.
```

Relational history state:

```text
|Psi> = (1/sqrt8) Σ_t |t> ⊗ R^t |psi0>.
```

Exactly:

```text
G|Psi> = |Psi>.
```

Combined group average:

```text
P_rel = (1/8) Σ_tau G^tau
```

Hermitian, idempotent and projects an orbit seed onto relational history.

Conditioning on clock t recovers:

```text
|psi(t)> = R^t |psi0>.
```

---

## Глава 88. Старый no-go при этом остаётся правильным

Clock-only average:

```text
P_clock = [(1/8)Σ S^tau] ⊗ I
```

для same nontrivial relational state даёт:

```text
P_clock |Psi> = 0.
```

То есть difference не в «усреднять или не усреднять».

Difference в том, **что является constraint**:

```text
clock alone             → phase erased
clock + correlated system → relational evolution survives.
```

Это finite Page–Wootters/rigging-map positive control, не full gravity physical projector.

---

# ЧАСТЬ XXI. От projector к source functional — впервые в правильном порядке

## Глава 89. Physical-history isometry

Define:

```text
V|psi>
= (1/sqrt8) Σ_t |t>⊗R^t|psi>.
```

Exact:

```text
V†V = I
VV† = P_rel.
```

То есть finite geometry Hilbert isometrically embedded в physical relational subspace.

---

## Глава 90. Relational observables commute with combined constraint

For geometry operator O:

```text
O_rel = Σ_t |t><t| ⊗ R^t O R^-t.
```

Then:

```text
[O_rel,G]=0
O_rel V = V O
V† O_rel V = O.
```

Это точный способ вставлять source **после** physical projection, не до него.

---

## Глава 91. Finite generating functional

For q=2 shape source:

```text
K = jx X + jz Z.
```

Because:

```text
K²=(jx²+jz²) I,
```

normalized physical trace:

```text
Z(jx,jz)=cosh(sqrt(jx²+jz²))
W=log Z.
```

Zero-source connected shape Hessian:

```text
C_shape = I₂.
```

Push through exact shape→metric Jacobian B:

```text
B^T B = (9/2) I₂.
```

Metric response has rank 2 and nonzero eigenvalues `9/2`.

Moore–Penrose inverse:

```text
C_metric^+ = (4/81) C_metric.
```

Inverse-response eigenvalue on tangent:

```text
2/9.
```

**FINITE EXACT POSITIVE CONTROL:** legal chain `projector → sources → W → finite Γ²` now executable.

**Не physical graviton Γ².** R=J и C8 clock пока positive-control choices.

---

# ЧАСТЬ XXII. Orientation получает настоящий microscopic witness

## Глава 92. Pauli Y перестаёт быть просто абстрактным label

На four-spin-1/2 Hilbert define gauge-scalar oriented flux triple:

$$
Q_or = epsilon_abc J_1^a J_2^b J_3^c.
$$

Projection на two-dimensional singlet carrier gives exactly:

```text
Q_or = (sqrt3/4) Y_L.
```

It commutes with total SU(2) generators and flips sign under odd face permutation.

So:

```text
Y_L = (4/sqrt3) Q_or.
```

Теперь orientation observable имеет microscopic gauge-invariant geometry meaning.

Latest exact CI on research branch: **SUCCESS**.

---

## Глава 93. History current можно переписать через oriented volume

Minimal history odd part:

```text
(W-W†)/(2i)
= Y_L ⊗ C_h
= (4/sqrt3) Q_or ⊗ C_h.
```

Это важнее notation convenience: future microscopic amplitude можно тестировать against gauge-scalar flux pseudoscalar, а не «против одной Pauli matrix по имени Y».

---

## Глава 94. 24 Lorentzian permutations сжимаются в один sign channel

Exact combinatorics of tetrahedral frame:

```text
epsilon_coeff(p) = -sgn(p)
```

for all 24 permutations.

If genuine canonical logical ordered triple O obeys required S4 covariance:

```text
T_p = U_p O U_p†,
```

then full epsilon node:

```text
L_epsilon
= -Σ_p sgn(p) U_p O U_p†.
```

On logical [2,2] carrier sign irrep one-dimensional:

```text
L_epsilon = -12 Tr(Y_L O) Y_L.
```

Using oriented flux:

```text
L_epsilon
= -64 Tr(Q_or O) Q_or.
```

**EXACT REDUCTION conditional on microscopic covariance.**

It can reduce 24 heavy calculations to one logical matrix + covariance audit.

---

## Глава 95. А настоящий Peter–Weyl orientation amplitude пока не успел досчитаться

Preregistered test in PR #42 was deliberately allowed two scientific outcomes:

```text
relative reversal difference < 1e-9 → ZERO
relative reversal difference > 1e-6 → NONZERO
middle band → numerical ambiguity / fail.
```

Two genuine safe sine-ordered triples at `Jmax=7/2` started independently:

```text
T_123
T_213.
```

Both spent the full 120-minute workflow wall inside the actual amplitude computation and were cancelled at timeout before artifact upload.

Therefore current result is:

```text
ZERO?        UNKNOWN
NONZERO?     UNKNOWN
g_YC gravity OPEN
reason: computational no-result / timeout.
```

**Очень важно:** timeout не является physical zero и не является evidence for nonzero.

Следующий implementation task — exact runtime reduction/caching, а не изменение thresholds или operator definition.

---

# ЧАСТЬ XXIII. Кладбище красивых коротких дорог

Эта часть — не список поражений. Это список мест, где теория стала сильнее, потому что запретила себе самообман.

## Дракон A. «Bit — это Planck voxel»

Нет.

`ell_*` — microscopic cutoff candidate. `ell_* = ell_P` требует отдельного physical scale bridge.

---

## Дракон B. «Coarse-graining создаёт четыре измерения»

Нет.

Dimension-blind control остаётся около 2.07. Dimension must come from topology/growth; smoothing only hides roughness.

---

## Дракон C. «Local S² автоматически uniquely forces global S³»

Нет.

16-cell gives canonical economical completion with exact stability, not uniqueness theorem of bare graph dynamics.

---

## Дракон D. «SU(2) qubit уже есть Lorentzian SL(2,C) spacetime»

Нет.

SU(2) is spatial gauge carrier. Lorentzian physics needs causal dynamics/extrinsic curvature/HDA.

---

## Дракон E. «8.43% = zeta4»

Нет.

Это local Euclidean E/T2 precursor. Physical quartic TT has six-dimensional observable space and needs momentum/RG/history bridge.

---

## Дракон F. «8.43% = particle mass ratio»

Нет.

Schur lemma forbids splitting one irreducible S4 triplet with invariant scalar term.

---

## Дракон G. «Higher-shell eigenvalues = masses»

Нет.

Это finite constraint spectral data с dynamic range ~1.416, not matter mass matrix.

---

## Дракон H. «Constraint z = physical omega»

Нет.

Need projector/history/source/Γ bridge first.

---

## Дракон I. «Три high-symmetry directions определяют generic quartic TT»

Нет.

Rank only five; direction `(120)` необходима для full rank six.

---

## Дракон J. «Hopf U(1) автоматически даёт photon и 1/137»

Нет.

Need Maxwell dynamics/deconfinement/stiffness `Z_A`.

---

## Дракон K. «Finite modular arithmetic сама содержит real number line»

Нет.

Need Archimedean completion after rational lift.

---

## Дракон L. «Z₂² = Z₄»

Нет.

Geometry group и adjacency cycle играют разные роли.

---

## Дракон M. «Z₄×Z₂ = Z₈»

Нет.

Independent time bit не даёт order-eight generator; carry coupling essential.

---

## Дракон N. «Pure gauge averaging сохранит phase»

Нет.

Untwisted average selects trivial character. Relational phase survives only when constraint correlates clock and system.

---

## Дракон O. «Orientation Y — ещё одна linear metric direction»

Нет.

`partial g / partial Y = 0` exactly. Use oriented flux/triad/connection/history observables instead.

---

## Дракон P. «Timeout тяжёлого расчёта означает ноль»

Нет.

No artifact = no measured amplitude.

---

# ЧАСТЬ XXIV. Что сейчас действительно закрыто

## Структурная геометрия

**EXACT / FINITE:**

```text
q+2=2^q → q=2
C4 + endpoints → local S²
Walsh(q=2) → regular tetrahedral frame
face qubits → Gauss geometry qubit
flux → tetrahedral geometry
canonical 16-cell completion → S³-like PL manifold
recursive barycentric stability
d_g → 3 exactly.
```

---

## Coarse observer

**FINITE PASS:**

```text
z≈1
3+1-like history scaling
δg ~ b^-2.001707
∇δg ~ b^-3.001458
δR ~ b^-4.000524.
```

Scope: declared q=2 control, not universal critical theorem.

---

## Quantum geometry / gravity structure

**EXACT / FINITE:**

```text
geometry qubit X/Z/Y interpretation
shape→metric Jacobian
Plebanski/Urbantke controls
Regge/EH controls
DeWitt/ADM selection
support-safe HDA scaling hierarchy
Peter–Weyl higher-shell non-scalarity
held-out L=6 residue.
```

---

## Observable dictionary

**EXACT:**

```text
generic parity-even quartic TT dimension = 6
full-rank six-observable extractor
on-shell field-redefinition quotient
six-vector → TT eigenbranches → A4/velocity/phase translator.
```

---

## Arithmetic/history representation layer

**EXACT mathematics / green frontier CI:**

```text
modular complex decomplexification
C4 quarter-turn J²=-I
orientation reversal ↔ conjugation
history → integer winding
minimal reversible C8 dilation
C4+Q dense in U(1)
C4+R = U(1)
unique positive quadratic C4-invariant |z|² precursor
realification of Hermitian dynamics
orientation-resolved history W(theta)=exp(-theta J)
directed difference square → graph Laplacian
same J across all these representations.
```

---

## Projector/source positive controls

**FINITE EXACT POSITIVE CONTROLS:**

```text
clock-only averaging kills phase
combined clock-system relational projector preserves correlations
V†V=I, VV†=P_rel
relational sources commute with combined constraint
projector → Z[J] → W[J] → finite metric Γ² chain
Y is null in linear intrinsic metric
Q_or=(sqrt3/4)Y is microscopic orientation witness.
```

These are architectural positive controls, not yet the full gravity physical inner product.

---

# ЧАСТЬ XXV. Что всё ещё открыто физически

## 1. Physical history / rigging map полного gravitational constraint

Нужно заменить toy/positive-control relational clock на derived gravitational/boundary-history construction.

Target:

```text
H[N]
→ P_phys / rigging map
→ physical inner product
→ boundary/history amplitudes.
```

---

## 2. Genuine orientation-odd Lorentzian amplitude

PR #42 timed out without result.

Нужно exact acceleration, которое не меняет physics:

- shared caches;
- safe recoupling reductions;
- symmetry transport only after genuine covariance proof;
- checkpoint/artifact sharding.

После этого preregistered ZERO/NONZERO thresholds остаются прежними.

---

## 3. Connected interblock history kernel

Local constraint spectral data insufficient.

Нужно connected spatial/history calculation across blocks/refinement levels.

---

## 4. Physical Γ^(2)_metric

Finite positive-control chain уже существует.

Теперь надо заменить positive-control R/ensemble genuine gravity rigging/boundary amplitude и только затем TT-project.

---

## 5. Первый interacting six-Wilson vector

Нужно получить:

```text
c_IR = (c1,c2,c3,c4,c5,c6)
```

из genuine physical pole, **до** scale fitting и external data.

Сначала full six-vector. Только потом тестировать nested eta/zeta и Q_tet submodels.

---

## 6. Regulator/refinement convergence

Нужна устойчивость six-vector по cutoff/refinement и explicit uncertainty.

Local PL rescaling alone не решает эту задачу.

---

## 7. Один physical scale

Либо derive microscopic scale, либо calibrate ровно один declared datum.

Никаких разных scale для разных predictions.

---

## 8. Maxwell stiffness

Hopf/U(1) carrier есть.

Physical photon требует derived `Z_A`, propagating modes и common causal cone.

Только после этого можно говорить о derived `alpha`.

---

## 9. Matter / chirality / flavor

Gravity carrier не выводит автоматически Standard Model.

Нужны отдельные matter representations, chirality, anomaly structure, flavor-breaking dynamics, Yukawa sector.

---

## 10. Blind external experiment

После freezing theory commit, six-vector, scale rule и likelihood:

```text
→ held-out GW dispersion/birefringence data
→ optical/phase tests if applicable
→ no post-hoc retuning.
```

Именно внешний эксперимент решит, является ли candidate природой, а не только красивой математической машиной.

---

# ЧАСТЬ XXVI. Современная правильная цепь физикализации

После всех исправлений самая строгая дорога выглядит так:

```text
binary microscopic relation
↓
q=2 local route structure
↓
Walsh tetrahedral geometry
↓
Gauss / gluing / PL spatial carrier
↓
causal history + d*=3 + z≈1
↓
coarse smooth geometry
↓
Peter–Weyl quantum constraint dynamics
↓
HDA / ADM consistency
↓
physical projector / rigging map
↓
relational or boundary history
↓
metric / connection sources
↓
Z[J]
↓
W[J] = log Z
↓
Γ[g,A,...]
↓
Γ^(2)
↓
physical TT pole
↓
(c1,...,c6)_IR
↓
one common scale
↓
velocity / phase / birefringence observables
↓
blind experiment.
```

Ни одну стрелку после `constraint` нельзя заменить фразой «ну это, наверное, просто omega».

---

# ЧАСТЬ XXVII. Где искать исходники каждого этапа

## Geometrogenesis

```text
BINARY_TO_GEOMETRY_GATE.md
BIT_TO_SPACETIME_CENTRAL_EQUATION.md
MICRO_WALSH_QGEOM_BRIDGE.md
SPATIAL_QUBIT_GEOMETRY_BRIDGE.md
GLOBAL_MANIFOLD_Q2_COMPLETION.md
Q2_DIMENSION3_FIXED_POINT_CLOSURE.md
OBSERVER_SCALE_SMOOTHING.md
```

## Metric / continuum gravity

```text
LOGICAL_SHAPE_METRIC_JACOBIAN.md
FACE_QUBIT_BFIELD.md
SIMPLICITY_PROJECTOR_THEOREM.md
PLEBANSKI_URBANTKE_BRIDGE.md
PLEBANSKI_CONNECTION_EINSTEIN_GATE.md
REGGE_EH_CUBIC_BRIDGE.md
DEWITT_HDA_UNIQUENESS.md
FLUX_DEWITT_SIGNATURE_THEOREM.md
```

## Constraint / HDA / Peter–Weyl

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

## TT / physical observables

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
PREDICTIONS_AND_EXPERIMENTAL_TESTS.md
```

## Current arithmetic/history frontier

Research stack:

```text
PR #40 modular-complex → ordinary arithmetic
PR #41 history → winding / minimal C8 / U(1)
PR #42 genuine Peter-Weyl reversal amplitude — timeout/no-result
PR #43 Lorentzian epsilon sign-twirl reduction
PR #44 history Fourier → real complex structure
PR #45 directed-history Laplacian factorization
PR #46 unified J cross-layer audit
PR #47 relational-history projector
PR #48 relational metric sources / finite Γ²
PR #49 orientation intrinsic-metric no-go
research/q2-oriented-flux-history-observable — Q_or witness, CI SUCCESS.
```

Эти ветки должны считаться **frontier evidence**, пока не сведены в один canonical merge.

---

# ЧАСТЬ XXVIII. Как воспроизводить, а не верить README

Главная идея репозитория — каждое важное число должно иметь executable gate.

Canonical main workflow:

```text
.github/workflows/core-regression.yml
```

В `scripts/` лежат отдельные gates:

```text
q2_dimension3_fixed_point_gate.py
micro_walsh_qgeom_gate.py
logical_shape_metric_jacobian_gate.py
collective_l1_q4_s4_metric_compression.py
plebanski_urbantke_gate.py
regge_eh_cubic_bridge.py
peter_weyl_* gates
s4_tt_quartic_complete_basis_gate.py
s4_tt_six_wilson_predictor.py
...
```

Green internal CI означает:

```text
этот declared mathematical/computational result reproduced = YES
природа экспериментально подтвердила theory              = NO.
```

Это различие нельзя стирать.

---

# ЧАСТЬ XXIX. Таблица истины на 28 августа 2026

| Утверждение | Статус |
|---|---|
| `q+2=2^q` uniquely selects q=2 in route family | **EXACT** |
| q=2 local shell is octahedral S² | **EXACT** |
| Walsh q=2 labels form regular tetrahedral normals | **EXACT** |
| four face qubits contain 2D Gauss geometry sector | **EXACT** |
| `Q_or=(sqrt3/4)Y_L` | **EXACT** |
| selected 16-cell completion is stable PL S³-like manifold | **EXACT / FINITE** |
| exact rewrite fixed point `d*=3` | **EXACT** |
| observer smoothing exponents near -2/-3/-4 | **FINITE PASS** |
| q=2 geometry is uniquely selected dynamically from every generic state | **OPEN / EXTENSION** |
| shape X/Z maps to rank-two metric tangent | **EXACT** |
| Y is linear intrinsic-metric direction | **NO-GO** |
| first q4 E/T2 split exists | **FINITE PASS** |
| 8.43% is physical Lorentz violation | **NOT CLAIMED** |
| Regge L6 continuation | **HELD-OUT PASS** |
| finite Peter–Weyl higher shell is non-scalar | **FINITE PASS** |
| constraint spectral z is physical omega | **NO-GO** |
| quartic physical S4 TT space has dimension six | **EXACT** |
| six-observable extractor has full rank | **EXACT** |
| final interacting six-Wilson vector frozen | **OPEN PHYSICAL** |
| Hopf U(1) carrier exists | **EXACT KINEMATIC** |
| Maxwell stiffness / alpha derived | **OPEN PHYSICAL** |
| modular complex arithmetic realifies to integer matrices | **EXACT** |
| history winding lifts to Z | **EXACT TOPOLOGICAL** |
| q=2 history supplies real `J²=-I` phase structure | **EXACT in minimal lift** |
| C4+Q is dense in U(1) | **EXACT MATHEMATICS** |
| `|z|²` unique normalized positive quadratic C4 invariant | **EXACT PRECURSOR** |
| full Born measurement rule derived | **OPEN PHYSICAL** |
| combined relational projector positive control works | **FINITE EXACT** |
| finite projector→sources→Γ² bridge works | **FINITE EXACT** |
| genuine gravitational `g_YC` measured | **OPEN — heavy run timed out** |
| Standard-Model masses derived | **NO** |
| theory externally confirmed | **NO** |

---

# Эпилог. Как заканчивается научная сказка

В обычной сказке автор заранее знает, что герой победит дракона.

В научной сказке это запрещено.

Мы можем построить красивую цепь:

```text
bit
→ relation
→ geometry
→ space
→ history
→ smoothness
→ quantum geometry
→ constraint
→ projector
→ observable
→ experiment.
```

Мы можем доказать сотни промежуточных identities.

Можем заранее заморозить extraction matrix.

Можем построить no-go, который разрушит нашу любимую идею.

Можем потратить два часа CI и получить не число, а timeout — и честно написать `UNKNOWN`.

Но последнюю страницу всё равно пишет не README.

Её пишет природа.

Поэтому самый сильный корректный итог проекта сегодня звучит так:

> **В репозитории существует необычно длинная и воспроизводимая структурно-математическая candidate architecture от binary relations до геометрии, GR/HDA controls и полного six-dimensional TT observable dictionary. Новая arithmetic/history ветка показывает точные способы появления real complex structure, winding, U(1)-phase и relational-projector positive controls из q=2 architecture. Но full gravitational physical history/inner product, genuine interacting six-Wilson pole vector, common physical scale и blind experimental validation ещё не закрыты.**

И это не слабость сказки.

Это место, где сказка наконец становится экспериментальной физикой.
