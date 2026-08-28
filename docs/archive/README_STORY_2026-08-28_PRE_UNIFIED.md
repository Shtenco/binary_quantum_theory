# От бита пространства-времени к геометрии, гравитации, свету и эксперименту

## Большая научная сказка для детей-учёных — всё по шагам, на пальцах, но без обмана

> **Канонический статус: 23 августа 2026. Candidate theory.**
>
> Это не объявление «теории всего». Это исследовательская программа, которая пытается пройти очень длинный путь: от минимальных бинарных различий до пространства, времени, гравитации, света и реальных наблюдаемых. Там, где мост уже доказан, мы так и пишем. Там, где есть только finite calculation или дополнительная гипотеза, мы тоже говорим об этом прямо.

---

## Самая короткая версия всей истории

Представь, что мы не имеем права начать с готового пространства.

Нам нельзя заранее сказать:

```text
вот ось X
вот ось Y
вот ось Z
вот время T
```

Нельзя заранее нарисовать решётку.

Нельзя заранее положить на стол метрическую линейку.

Можно начать только с очень простой идеи:

```text
есть различие
0 или 1
```

И задать вопрос:

> Может ли огромное количество таких бинарных различий, если они связаны одним и тем же локальным правилом, коллективно начать выглядеть как пространство-время?

В нашей кандидатной конструкции путь выглядит так:

```text
бинарное различие
→ q = 2
→ четыре route-состояния
→ локальная сфера S²
→ тетраэдральная геометрия
→ квантовые грани
→ geometry qubit
→ склейка клеток
→ глобальное S³
→ размерность стремится к 3
→ z ≈ 1
→ 3+1-like history
→ coarse-graining наблюдателя
→ дискретная микрогеометрия выглядит гладкой
→ SU(2)/Peter–Weyl quantum geometry
→ spin-2 сектор
→ метрика
→ Hamiltonian constraints
→ physical projector
→ физическое время
→ 1PI effective action
→ гравитон и свет
→ эксперимент
```

Теперь разберём каждую стрелку медленно.

---

# Как читать этот README

У каждой важной главы будет три уровня.

### На пальцах

Что происходит простыми словами.

### Чуть строже

Минимальная математика, которая не даёт нам превратить красивую историю в фантазию.

### Что здесь реально доказано

Один из статусов:

- **EXACT** — точное алгебраическое или комбинаторное утверждение в заявленных предпосылках;
- **FINITE PASS** — воспроизводимый конечный расчёт;
- **HELD-OUT PASS** — проверка на заранее отложенных данных;
- **CONDITIONAL** — верно, если выполняется явно указанная дополнительная гипотеза;
- **OPEN** — мост пока не закрыт;
- **NO-GO** — показано, что красивый короткий путь не работает.

Главные строгие документы лежат отдельно:

- [`CANONICAL_THEORY_PACKAGE.md`](CANONICAL_THEORY_PACKAGE.md) — сухой evidence index;
- [`BIT_TO_SPACETIME_CENTRAL_EQUATION.md`](BIT_TO_SPACETIME_CENTRAL_EQUATION.md) — техническая цепь «binary microstructure → smooth spacetime»;
- [`OBSERVER_SCALE_SMOOTHING.md`](OBSERVER_SCALE_SMOOTHING.md) — observer/coarse-graining;
- [`GLOBAL_MANIFOLD_Q2_COMPLETION.md`](GLOBAL_MANIFOLD_Q2_COMPLETION.md) — локальная S² и глобальная S³ completion;
- [`MICRO_WALSH_QGEOM_BRIDGE.md`](MICRO_WALSH_QGEOM_BRIDGE.md) — binary labels → tetrahedral geometry;
- [`LOGICAL_SHAPE_METRIC_JACOBIAN.md`](LOGICAL_SHAPE_METRIC_JACOBIAN.md) — shape → metric;
- [`THEORY_STATUS.md`](THEORY_STATUS.md) — текущий human-readable status;
- [`theory_gates.json`](theory_gates.json) — machine-readable gates.

Исторические версии тоже сохранены:

- [`README_LESSON_2026-08-14.md`](docs/archive/README_LESSON_2026-08-14.md);
- [`README_STORY_2026-08-17.md`](docs/archive/README_STORY_2026-08-17.md);
- [`README_STORY_2026-08-21_v42.md`](docs/archive/README_STORY_2026-08-21_v42.md);
- [`README_STORY_2026-08-23_PRE_CHILDREN.md`](docs/archive/README_STORY_2026-08-23_PRE_CHILDREN.md).

---

# Часть I. Что такое «бит пространства-времени»

## Глава 1. Бит — это не маленький кубик

### На пальцах

Очень легко представить фундаментальное пространство так:

```text
[0][1][1][0][1]
```

будто Вселенная состоит из крошечных клеточек-пикселей.

Но это было бы ловушкой.

Если мы уже нарисовали клеточки в ряд или в кубе, то мы **заранее вставили пространство**.

Поэтому здесь слово «бит» означает не маленький кусочек готового пространства.

Бит означает минимальную **различимость**:

```text
вариант A
или
вариант B
```

То есть на самом глубоком уровне мы начинаем не с длины, а с ответа на вопрос:

> Можно ли отличить одно состояние от другого?

### Чуть строже

Минимальный classical label:

```text
0 или 1
```

Минимальный quantum carrier:

```text
|ψ> = α|0> + β|1>
```

при условии

```text
|α|² + |β|² = 1.
```

Но даже qubit сам по себе ещё не является пространством.

Нужно вывести геометрические отношения между большим количеством таких объектов.

### Что здесь реально доказано

**STARTING ANSATZ.** Бинарная локальная степень различимости — выбранная минимальная гипотеза модели, а не экспериментально установленный «атом пространства».

---

## Глава 2. Почему одного бита недостаточно

Один бинарный выбор знает только две альтернативы.

Он не знает:

```text
лево / право
вверх / вниз
угол
площадь
объём
соседство
```

Поэтому вводим число `q` — сколько независимых бинарных различий участвуют в одном локальном causal событии.

Если независимых битов `q`, то различных binary route labels существует

```text
2^q.
```

Например:

```text
q = 1 → 0, 1
q = 2 → 00, 01, 10, 11
q = 3 → 000 ... 111
```

Пока это просто набор состояний.

Следующий вопрос:

> Какое q позволяет локальной структуре быть максимально однородной без ручной подгонки?

---

## Глава 3. Простое уравнение выбирает q = 2

### На пальцах

Представь локальный причинный «ромб».

Есть два специальных конца:

```text
вход
выход
```

и между ними есть `2^q` возможных route states.

Каждый route state:

- связан с двумя causal концами;
- отличается одним битом от `q` соседних route states.

Поэтому у него

```text
q + 2
```

связей.

А каждый causal конец связан со всеми

```text
2^q
```

маршрутами.

Если хотим, чтобы эти два типа вершин имели одинаковую valence, получаем

```text
q + 2 = 2^q.
```

Проверяем:

```text
q=1: 3 != 2
q=2: 4  = 4
q=3: 5 != 8
q=4: 6 != 16
```

Единственный целый ответ:

```text
q = 2.
```

### Что это значит

Модель не говорит «возьмём два бита, потому что так удобно».

Два бита появляются как решение локального условия однородности.

### Что здесь реально доказано

**EXACT:** в объявленном binary-route family уравнение `q+2=2^q` имеет единственное целое решение `q=2` для `q>=1`.

---

# Часть II. Как из четырёх бинарных маршрутов рождается локальная геометрия

## Глава 4. Четыре состояния образуют квадрат

При `q=2` есть четыре labels:

```text
00
01
10
11
```

Соединяем два labels, если они отличаются ровно одним битом.

Получаем цикл:

```text
00 —— 01
|       |
10 —— 11
```

Топологически это квадрат `C4`.

Сам по себе квадрат всё ещё не трёхмерное пространство.

Но теперь добавим два causal полюса.

---

## Глава 5. Квадрат плюс два полюса превращается в октаэдр

Каждый из двух causal poles соединяем со всеми четырьмя route states.

Получается граф октаэдра.

Его поверхность имеет:

```text
6 вершин
12 рёбер
8 треугольных граней
```

и Euler characteristic

```text
χ = 6 - 12 + 8 = 2.
```

Это поверхность двумерной сферы:

```text
S².
```

### Почему это важно

Если мы стоим внутри обычного трёхмерного пространства и возьмём очень маленькую сферу вокруг обычной точки, её поверхность будет S².

В combinatorial 3-manifold говорят:

```text
link внутренней вершины = S².
```

То есть наш binary object получил именно тот тип локальной оболочки, который нужен обычной точке трёхмерного пространства.

### Что здесь реально доказано

**EXACT:** при q=2 suspension Hamming-cycle `C4` даёт octahedral simplicial S².

Это ещё не доказывает глобальное трёхмерное пространство.

---

## Глава 6. Второй сюрприз: те же четыре labels сами строят тетраэдр

Вот одна из самых красивых частей модели.

Четыре labels

```text
00, 01, 10, 11
```

можно рассматривать как элементы группы

```text
Z₂².
```

У неё есть три нетривиальных real Walsh characters.

Из этих трёх функций строим трёхкомпонентный вектор для каждого label.

Получаются четыре unit vectors с очень специальным свойством:

```text
каждый имеет длину 1
сумма всех четырёх = 0
скалярное произведение любых разных = -1/3
```

### На пальцах

Положи четыре одинаковые стрелки из центра правильного тетраэдра к центрам его четырёх граней.

Именно так они и расположены:

```text
каждая стрелка одинаковой длины
между любой парой одинаковый угол
все четыре вместе взаимно уравновешиваются
```

То есть binary labels сами дают **нормали правильного тетраэдра**.

### Почему это важно

Мы не нарисовали тетраэдр руками после того, как увидели q=2.

Тетраэдральный frame получается из character algebra самих binary labels.

### Что здесь реально доказано

**EXACT:** `Z₂²` через три nontrivial Walsh characters отображается в четыре вершины regular simplex в R³, то есть в tetrahedral frame. Подробности: [`MICRO_WALSH_QGEOM_BRIDGE.md`](MICRO_WALSH_QGEOM_BRIDGE.md).

---

## Глава 7. Что такое face qubit

Теперь у нас есть четыре derived направления `n_f` — по одному на каждую грань будущего тетраэдра.

Каждому направлению можно сопоставить qubit state, у которого Bloch vector указывает вдоль `n_f`.

На пальцах:

```text
binary label
→ направление
→ квантовая стрелка-нормаль к грани
```

То есть qubit начинает нести геометрический смысл.

Но четыре независимые стрелки ещё могут не образовывать замкнутую клетку.

Нужно условие closure.

---

## Глава 8. Почему сумма четырёх face fluxes должна быть нулём

У замкнутого тетраэдра outward face normals, взвешенные площадями, уравновешиваются.

На пальцах это похоже на четыре силы, которые тянут замкнутую клетку наружу, но в сумме не уносят её никуда.

Для regular tetrahedral frame:

```text
E₁ + E₂ + E₃ + E₄ = 0.
```

В gauge language это Gauss closure.

Finite gate для binary-derived tetrahedral state даёт closure norm, равную нулю в точной конструкции.

### Что здесь реально доказано

**EXACT/FINITE:** derived q=2 frame имеет exact flux closure и nonzero support в gauge-invariant singlet sector.

---

## Глава 9. Четыре face qubits превращаются в один geometry qubit

Четыре spin-1/2 объекта вместе содержат несколько collective spin sectors.

Разложение:

```text
(1/2)^4 = 2×j=0 + 3×j=1 + 1×j=2.
```

Нас сейчас интересует gauge-invariant `j=0` sector.

У него dimension 2.

А двухмерное quantum space — это снова qubit.

Поэтому:

```text
4 face qubits
→ Gauss-invariant sector
→ 1 logical geometry qubit.
```

### Что хранит geometry qubit

Не «0 или 1 в пространстве».

Его logical coordinates кодируют свойства формы тетраэдра:

```text
X_L → одна shape-комбинация
Z_L → другая shape-комбинация
Y_L → orientation / oriented volume
```

Oriented-volume eigenvalues в выбранной нормировке:

```text
+sqrt(3)/4
-sqrt(3)/4.
```

То есть два состояния могут различать левую и правую orientation клетки.

### Важное предупреждение

Этот `j=0` geometry qubit не надо путать с unique collective `j=2` sector, который позже будет кандидатом на spin-2 carrier.

---

## Глава 10. Из face fluxes можно восстановить обычную геометрию тетраэдра

Пусть из одной вершины тетраэдра выходят три edge vectors:

```text
a, b, c.
```

Три face-area vectors можно записать как

```text
E1 = (b × c)/2
E2 = (c × a)/2
E3 = (a × b)/2.
```

И наоборот, если мы знаем эти fluxes, можно восстановить edge geometry.

Это очень важно.

Мы получили не просто абстрактные qubit labels, а quantities, из которых можно вернуться к обычным длинам, углам и shape.

### Что здесь реально доказано

**EXACT/FINITE:** для non-degenerate tetrahedron flux reconstruction работает до machine precision в соответствующем gate.

---

# Часть III. Почему один тетраэдр ещё не пространство

## Глава 11. Пространство начинается со склейки

Один идеальный LEGO-кирпич — не дом.

Один тетраэдр — не пространство.

Нужно соединить много клеток так, чтобы общая грань для двух соседей действительно была **одной и той же геометрической гранью**.

Только совпадения площади недостаточно.

Два треугольника могут иметь:

```text
одинаковую площадь
одинаковую нормаль
```

но разную внутреннюю форму.

Это один из вариантов twisted geometry.

Поэтому нужны как минимум два условия:

```text
closure defect → 0
shape mismatch → 0.
```

Если shape mismatch не исчезает, мы имеем набор хороших клеток, но ещё не одну гладкую геометрию.

---

## Глава 12. Почему соседние orientation должны быть противоположны

Если два тетраэдра имеют общую грань, outward normal первого смотрит через грань в сторону второго.

А outward normal второго смотрит в обратную сторону.

Поэтому правильная склейка требует:

```text
intrinsic face shape совпадает
outward orientation меняет знак.
```

Старый Bell-gluing control именно это и проверял на logical geometry qubits:

```text
shape correlations совпадают
orientation correlation имеет противоположный знак.
```

В современной q=2 global gluing ветке outward Walsh fluxes сокращаются на shared faces.

---

## Глава 13. Локальные S² можно сложить в глобальное S³

Canonical minimal completion использует boundary четырёхмерного cross-polytope — 16-cell.

У seed complex:

```text
V = 8
E = 24
F = 32
T = 16 tetrahedra
```

Betti numbers:

```text
(1,0,0,1)
```

как у S³.

У него:

```text
vertex link   = S²
edge link     = S¹
triangle link = S⁰.
```

Каждый triangle принадлежит ровно двум tetrahedra.

Complex orientable.

Boundary-of-boundary равна нулю.

### На пальцах

Мы проверяем не только «красивая ли картинка».

Мы проверяем, нет ли:

```text
дырявого шва
висячей грани
неправильной окрестности точки
перевёрнутой ориентации
```

### Что здесь реально доказано

**EXACT/FINITE:** natural canonical PL completion совместима с closed orientable S³ и сохраняет manifold properties на проверенных refinements.

Не доказано, что любой imaginable bare-causal gluing обязан быть именно этим S³.

---

## Глава 14. Почему появляется именно 16-cell

При дополнительной declared semantics:

```text
минимум 8 вершин
каждая vertex link = octahedral S²
flag/clique closure
```

у каждой вершины есть 6 соседей среди остальных 7.

Значит есть ровно один antipode, с которым edge отсутствует.

Восемь вершин разбиваются на четыре antipodal pairs.

Чтобы построить tetrahedron, берём по одной вершине из каждой пары.

Выборов:

```text
2×2×2×2 = 16.
```

Отсюда 16 tetrahedra.

Это и есть boundary 16-cell.

### Статус

**EXACT в minimal+flag semantics.** Не uniqueness theorem для любого nonflag microscopic rule.

---

## Глава 15. Пространство не ломается при увеличении детализации

Barycentric refinement:

```text
16 tetrahedra
→ 384
→ 9216
```

На проверенных уровнях:

```text
bad vertex links = 0
bad edge links = 0
bad face links = 0
orientable = yes
all faces two-sided = yes
```

То есть при subdivision пространственная фаза сохраняет topology.

---

# Часть IV. Почему это пространство оказывается трёхмерным

## Глава 16. Топология и размерность — разные вопросы

S³ уже говорит нам о topological type выбранной spatial completion.

Но ещё хочется независимо увидеть, как растёт количество доступных состояний с масштабом.

Для обычного трёхмерного пространства volume растёт примерно как

```text
R³.
```

Поэтому ищем exponent, который стремится к 3.

---

## Глава 17. Exact causal-volume sequence идёт к 3

Для q=2 каждый active causal edge порождает восемь child edges, а линейный causal scale удваивается.

Exact count:

```text
N_g = (4*8^g + 10)/7.
```

One-step exponent:

```text
d_g = log2(N_g/N_{g-1}).
```

Последовательность:

```text
g=2 → 2.662965...
g=3 → 2.951744...
g=4 → 2.993853...
g=5 → 2.999229...
g=6 → 2.999903...
g=7 → 2.999987...
g=8 → 2.999998...
```

Она:

```text
всегда ниже 3
монотонно растёт
стремится к 3.
```

Поэтому fixed point:

```text
d* = 3.
```

### Что это значит

Старая цифра `2.999229...` оказалась не случайным «почти три».

Это просто g=5 point exact sequence, которая аналитически идёт к тройке.

### Статус

**EXACT** для объявленного recursive q=2 causal-volume family.

---

## Глава 18. Почему одного числа 3 всё равно мало

Хорошая теория не должна зависеть от одного удачного индикатора.

Поэтому здесь есть несколько свидетелей:

```text
local vertex link = S²
canonical global phase = S³
causal-volume exponent → 3
held-out d_H ≈ 2.99923
```

А dynamics даёт ещё один важный exponent `z`.

---

# Часть V. Откуда появляется время

## Глава 19. Пространство должно не только существовать, но и меняться

Представь фильм.

Один кадр — spatial slice.

История — последовательность кадров.

Если spatial scale увеличился в `λ` раз, characteristic time scale может измениться как

```text
τ → λ^z τ.
```

Для relativistic scaling нам нужен

```text
z → 1.
```

Frozen finite result:

```text
z ≈ 0.998281.
```

То есть пространственный и causal-time масштабы растут почти одинаково.

---

## Глава 20. Почему получается 3+1-like history

Историческое effective slice value:

```text
d_eff(slice) = d_H / z ≈ 3.004393867.
```

К нему добавляем одно causal/history направление:

```text
d_eff(history) = 1 + d_H/z ≈ 4.004393867.
```

Поэтому candidate scaling выглядит как

```text
3 spatial-like directions
+ 1 causal-time direction.
```

### Очень важное предупреждение

Это ещё **не** означает, что любой eigenvalue Hamiltonian constraint уже является физической частотой ω.

К этой проблеме мы вернёмся позже.

---

# Часть VI. Почему дискретное пространство может казаться гладким

## Глава 21. Самая важная аналогия: штукатурная стена

Подойди очень близко к стене.

Ты увидишь:

```text
песчинки
поры
царапины
микротрещины
шероховатости
```

Теперь отойди на десять метров.

Стена выглядит гладкой.

Но произошло ли чудо?

Нет.

Стена не перестроилась.

Ты просто перестал разрешать отдельные микронеровности.

### То же самое в нашей spacetime picture

Microscopic geometry может оставаться дискретной.

Но один observable pixel макроскопического наблюдателя содержит огромное количество microscopic degrees of freedom.

Он видит не каждый отдельный bit, а их collective average.

Поэтому корректная фраза:

> не «пространство физически становится гладким, когда мы отходим», а «при более грубом разрешении его дискретная микроструктура становится неразрешимой и coarse observables выглядят гладкими».

---

## Глава 22. Что именно меняется при удалении наблюдателя

Пусть microscopic cutoff равен `ell_*`.

Мы **не обязаны** сразу называть его Planck length.

Это отдельный scale-setting вопрос.

Для наблюдателя с characteristic angular/causal resolution `theta` и separation `r` можно использовать resolution map:

```text
ell_obs(r) = sqrt(ell_*² + (theta*r)²).
```

### Очень близко

Если

```text
theta*r << ell_*
```

то

```text
ell_obs ≈ ell_*.
```

Можно различать microscopic structure.

### Далеко

Если

```text
theta*r >> ell_*
```

то

```text
ell_obs ≈ theta*r.
```

Один pixel уже покрывает много microscopic cells.

---

## Глава 23. Что такое block size b

Вводим coarse factor:

```text
b ≈ ell_obs / ell_*.
```

В dyadic implementation берутся powers of two:

```text
b = 1, 2, 4, 8, ...
```

`b=1` — почти microscopic view.

Большое `b` — один observable cell включает много microcells.

---

## Глава 24. Почему шум падает как 1/sqrt(N)

Представь тысячу монет.

Одна монета даёт очень грубый результат:

```text
0 или 1.
```

Если усреднить тысячи независимых бросков, относительная случайная ошибка становится намного меньше.

Для `N` weakly correlated contributions typical fluctuation:

```text
noise_RMS ~ 1/sqrt(N).
```

Если history block effectively содержит

```text
N ~ b^4
```

microscopic contributions, тогда

```text
noise_RMS ~ 1/sqrt(b^4) = b^-2.
```

Вот математическая версия нашей стены.

---

## Глава 25. Почему slope и curvature становятся гладкими ещё быстрее

Если metric roughness

```text
delta g ~ b^-2,
```

то spatial derivative добавляет ещё один inverse length:

```text
grad(delta g) ~ b^-3.
```

А curvature roughly содержит две derivatives:

```text
delta R ~ b^-4.
```

То есть по мере coarse-graining:

```text
сама поверхность сглаживается
её slope fluctuations сглаживаются быстрее
curvature fluctuations — ещё быстрее.
```

---

## Глава 26. Что реально показал finite observer gate

В q=2 control измерено примерно:

```text
delta g       ~ b^-2.001707
grad(delta g) ~ b^-3.001458
delta R       ~ b^-4.000524
```

А в two-form / reconstructed-metric sector:

```text
simplicity defect ~ b^-1.994838
metric error      ~ b^-2.019746.
```

То есть несколько разных measures рассказывают одну и ту же историю:

```text
микроскопическая шероховатость
→ blocking
→ rapidly falling reconstruction defects
→ smooth IR description.
```

### Статус

**FINITE PASS / CONDITIONAL INTERPRETATION.** Это сильный continuumisation control, но universal exponent theorem потребовал бы полноценного RG и контроля correlations.

---

## Глава 27. Очень важный отрицательный контроль: averaging не создаёт измерения

Можно было бы обмануть себя так:

```text
много битов усредняются
→ значит автоматически получается 4D.
```

Это неверно.

Старый dimension-blind binary-diamond control после coarse-graining оставался около spectral dimension

```text
2.07,
```

а не превращался магически в 4.

Значит есть две разные задачи:

```text
binary rule / topology / growth → dimension
coarse-graining → smoothness.
```

Нельзя заменять одну другой.

---

## Глава 28. Гладкая средняя геометрия не означает отсутствие квантовой пены

Можно иметь одновременно:

```text
средняя fluctuation = 0
variance fluctuation > 0.
```

На пальцах:

поверхность озера может иметь средний уровень воды, но при этом на ней есть волны.

Так же smooth mean geometry может сосуществовать с microscopic quantum fluctuations.

Это позже важно для interferometric tests: даже если средняя propagation law полностью Lorentz-invariant, connected phase noise может оставаться ненулевым.

---

# Часть VII. Qubit открывает две двери: геометрию и фазу

## Глава 29. Bloch sphere — это уже геометрический объект

Normalized qubit имеет состояние

```text
|ψ> = cos(theta/2)|0> + exp(i phi) sin(theta/2)|1>.
```

После удаления общей phase физические ray states образуют sphere S².

Но важнее другое: один и тот же quantum geometric tensor содержит две части.

### Real part

Измеряет distinguishability соседних states — information geometry.

### Imaginary part

Даёт Berry curvature — phase geometry.

То есть один qubit ray одновременно несёт:

```text
геометрическую distinguishability
и
U(1)-подобную phase structure.
```

Это будущие две ветви:

```text
Re Q → geometry
Im Q → compact phase / light candidate.
```

### Статус

**EXACT KINEMATIC.** Динамика, превращающая phase carrier в реальный photon, ещё отдельный шаг.

---

# Часть VIII. Как появляется spin-2 и метрическая гравитация

## Глава 30. Где прячется collective spin-2

Вернёмся к четырём spin-1/2.

Их decomposition содержит unique `j=2` representation.

Это важно потому, что massless graviton в 3+1D имеет helicity ±2.

Но надо быть аккуратными.

Фраза

```text
«четыре qubits = graviton»
```

неверна.

Правильнее:

```text
четыре spin-1/2
→ содержат unique collective spin-2 carrier
→ carrier ещё должен получить правильную metric meaning
→ dynamics
→ constraints
→ physical pole.
```

### Статус

**EXACT REPRESENTATION-THEORY EXISTENCE**, не derivation physical graviton.

---

## Глава 31. Shape qubit действительно двигает метрику

В logical geometry sector два coordinates отвечают intrinsic shape deformations.

Exact Jacobian показывает, что они отображаются в два independent trace-free tangent directions metric space.

На пальцах:

```text
повернули logical shape coordinate
→ изменились dihedral relations
→ изменились edge scalar products
→ изменилась metric.
```

То есть между «qubit shape» и `g_ij` построен явный differential bridge.

### Статус

**EXACT** в declared tetrahedral geometry sector.

---

## Глава 32. Почему metric modes распадаются как 1 + 2 + 3

У symmetric 3×3 metric perturbation шесть components.

Tetrahedral/cubic symmetry S4 разлагает их как:

```text
A1  → 1 trace-like mode
E   → 2 modes
T2  → 3 modes.
```

Trace-free sector имеет 5 modes:

```text
E + T2.
```

Первый refined q4 finite kernel дал разные eigenvalues для E и T2.

Normalized split:

```text
примерно 8.430036%.
```

### Очень важное предупреждение

Это не означает:

```text
скорость гравитона отличается на 8.43%
или
массы частиц связаны как 8.43%.
```

Это локальный Euclidean spin-2 anisotropy precursor.

---

## Глава 33. Почему 8.43% нельзя превращать в массы электронов и мюонов

Это хороший пример того, как theory сама запрещает красивую numerology.

Если три generation-like states образуют irreducible T2 representation, любой S4-invariant mass operator на этом triplet пропорционален identity:

```text
M = m I₃.
```

То есть сам по себе tetrahedral splitting не может создать hierarchy

```text
electron
muon
tau.
```

Нужны отдельно выведенные:

```text
matter representations
flavor symmetry
symmetry-breaking spurion
Yukawa map.
```

### Статус

**NO-GO:** shortcut `8.43% → particle mass hierarchy` отвергнут.

---

# Часть IX. Peter–Weyl: клетка начинает жить квантовой динамикой

## Глава 34. Что такое Peter–Weyl здесь

SU(2) holonomies можно разложить по irreducible spins `j`.

Это похоже на разложение музыкального звука по гармоникам.

Вместо одной ноты мы имеем набор representation channels.

Hamiltonian действует между ними, меняет intermediate spins и создаёт nontrivial recoupling.

Именно здесь появляется настоящее quantum geometry dynamics, которой не было в одной static tetrahedral picture.

---

## Глава 35. Почему higher-shell spectrum ещё не физические частоты

Finite Peter–Weyl calculation даёт nontrivial 32D constraint spectral data.

Это полезно: оно показывает, что Hamiltonian не сводится к trivial scalar operator.

Но очень важно не сделать незаконный скачок:

```text
constraint eigenvalue
!=
physical frequency omega.
```

К этому мы скоро вернёмся.

### Статус

**FINITE PASS:** nontrivial constraint spectral structure есть.

**OPEN:** physical propagator ещё требует projector/history bridge.

---

## Глава 36. Почему простое геометрическое subdivision не создаёт нужный RG flow

Для separable geometry-only kernel blocking даёт общий scale factor всем internal modes.

Поэтому normalized anisotropy сама по себе не течёт.

На пальцах:

если увеличить фотографию одинаково по всем каналам, отношение красного к синему не изменится.

Чтобы internal anisotropy реально renormalize, нужна nonseparable dynamics:

```text
Peter–Weyl recoupling
interblock transfer
history dynamics.
```

### Статус

**NO-FLOW CONTROL** для geometry-only separable blocking.

---

# Часть X. От квантовой геометрии к общей относительности

## Глава 37. Почему Euclidean Hamiltonian недостаточен

Canonical real-SU(2) gravity использует connection

```text
A = Gamma + beta K.
```

Здесь `Gamma` — intrinsic spin connection, а `K` связан с extrinsic curvature.

Euclidean и Lorentzian pieces по отдельности зависят от Immirzi parameter beta.

В классическом kinetic combination beta dependence сокращается нужным образом.

### Статус

**EXACT CLASSICAL CONSISTENCY CONTROL.** Это не доказательство полной quantum beta-independence.

---

## Глава 38. Что такое HDA на пальцах

Общая относительность должна позволять по-разному нарезать spacetime на spatial slices и при этом описывать одну и ту же физику.

Hamiltonian constraint говорит примерно:

> сдвинь slice немного «в нормальном направлении».

Diffeomorphism constraint говорит:

> перетащи точки вдоль самого slice.

Если сначала сделать один normal deformation, потом другой и вычесть обратный порядок, должен получиться tangential shift.

Символически:

```text
[H[N], H[M]]
→ D[q^{-1}(N dM - M dN)].
```

Это один из главных тестов, отличающих настоящую gravity-like dynamics от красивого spin system.

---

## Глава 39. Почему старый factorized Hamiltonian был недостаточен

Если Hamiltonian действует на geometry, но совсем не умеет работать с path/rerouting sector, commutator не может породить нужную spatial diffeomorphism action.

Это был полезный negative result.

После него был построен route-normal generator, у которого principal symbol reproduces нужную HDA structure function в заявленном semiclassical scope.

### Статус

**STRUCTURAL/FINITE PASS** в declared route-normal sector; full physical history still requires projector/refinement completion.

---

## Глава 40. Plebanski и Regge — два независимых моста к Einstein geometry

Проект использует два разных downstream контроля.

### Ветка 1

```text
B-fields
→ simplicity
→ Urbantke metric
→ connection
→ curvature.
```

### Ветка 2

```text
metric simplices
→ Regge action
→ Hessian
→ Fierz–Pauli / Einstein-Hilbert behaviour.
```

Когда две независимые дороги приходят к совместимой IR structure, это сильнее одной удачной формулы.

### Но

Это всё ещё не означает, что microscopic binary dynamics уже полностью вывела continuum GR measure.

---

# Часть XI. Graviton propagator и почему всё оказалось сложнее

## Глава 41. Reduced TT model имеет правильный massless pole

В reduced positive-control model TT propagator имеет lattice sine form.

При малых momenta:

```text
sin(x/2) ≈ x/2,
```

поэтому leading dispersion становится relativistic:

```text
omega² ≈ c² k².
```

И equal-time TT vacuum power в этом reduced control ведёт себя как

```text
P_TT(k) ~ k^-1.
```

### Статус

**EXACT REDUCED CONTROL**, но не final interacting physical prediction.

---

## Глава 42. Почему generic quartic correction имеет не два, а шесть coefficients

Раньше было очень соблазнительно описать всё двумя числами:

```text
isotropic eta₂
cubic zeta₄.
```

Но generic momentum сам трансформируется под S4.

После точного TT quotient оказывается:

```text
physical parity-even quartic pole space dimension = 6.
```

То есть в общем случае нужны шесть Wilson coefficients.

### Зачем это важно

Если бы мы заранее оставили только два удобных параметра, мы могли бы получить красивый fit просто потому, что выбрали слишком узкую модель.

Теперь extractor заморожен до microscopic data.

### Статус

**EXACT:** six-dimensional quartic TT on-shell observable space в declared S4 setting.

---

## Глава 43. Шесть специальных измерений позволяют восстановить все шесть coefficients

Три красивые high-symmetry directions `100`, `110`, `111` дают только rank 5.

Поэтому заранее добавлена generic direction `120`.

И selected six observables дают invertible extraction matrix.

То есть:

```text
6 измеряемых directional/polarization numbers
↔
6 Wilson coefficients.
```

Нельзя после просмотра результата поменять basis на более удобный.

### Статус

**EXACT / PREREGISTERED EXTRACTOR.**

---

# Часть XII. Большая поправка: constraint spectrum — это ещё не физическое время

## Глава 44. Почему нельзя просто назвать z частотой omega

В обычной quantum mechanics Hamiltonian генерирует physical time evolution.

В generally covariant gravity Hamiltonian в canonical form в значительной степени является **constraint**.

Поэтому объект

```text
(z - H)^-1
```

не имеет права автоматически называться

```text
G(omega,k).
```

Это была важная conceptual correction проекта.

Правильная дорога:

```text
constraints
→ physical projector
→ physical history amplitude
→ generating functional
→ effective action Gamma
→ quadratic metric kernel
→ physical poles.
```

---

## Глава 45. Что такое physical projector на пальцах

Представь большую quantum Hilbert space комнату.

Не все states в ней физически допустимы.

Constraints говорят:

```text
вот эти направления являются gauge / unphysical
вот kernel, где constraints выполнены.
```

Physical projector — это оператор, который оставляет только допустимую часть state.

Finite master-constraint construction использует positive operator

```text
M = sum constraints²
```

с positive metric в constraint space.

Kernel `M` совпадает с общим kernel constraints.

Finite CI checks дали residuals порядка `10^-15`.

### Статус

**EXACT FINITE + CI PASS.**

Открыт настоящий refinement/rigging limit между масштабами.

---

## Глава 46. Как после projector появляется физическое время

Есть простой constrained toy model, где после projection и conditioning на clock states получается обычный unitary propagator.

На пальцах:

```text
сначала выбираем physical states
потом спрашиваем амплитуду между двумя показаниями relational clock
только тогда появляется физическое время между ними.
```

Для gravity естественный кандидат — boundary geometry, где proper separation задаётся самой semiclassical metric/extrinsic-curvature data.

Тогда физическая `omega` conjugate не к arbitrary label, а к physical separation.

### Статус

**EXACT POSITIVE CONTROL** для constrained toy model.

**OPEN PHYSICAL** для full microscopic gravity history.

---

## Глава 47. Настоящая физика живёт в effective action Gamma

После physical history construction вводим generating functional `Z[J]`.

Из него effective action `Gamma`.

И уже из second derivatives `Gamma` получаем physical kernels:

```text
K_gravity
K_photon
```

Только здесь можно честно говорить о:

```text
physical pole
speed
residue
dispersion
phase shift.
```

Это сейчас один из главных открытых microscopic bridges.

---

# Часть XIII. Шесть коэффициентов могут исчезнуть — и это нормально

## Глава 48. Лестница 6 → 1 → 0

Generic tetrahedral S4 environment разрешает шесть quartic TT observables.

Если при RG восстанавливается full spatial isotropy SO(3), все six observable values должны схлопнуться на одну common line:

```text
y1 = y2 = ... = y6.
```

А если дополнительно vacuum Lorentz-invariant, diffeomorphism unbroken и low-energy field — обычный metric graviton, massless branch может остаться exactly на

```text
s = -omega² + c²k² = 0.
```

Тогда common quartic pole shift тоже исчезает.

Получаем hierarchy:

```text
S4       → 6 numbers
SO(3)    → 1 number
Lorentz  → 0 vacuum massless-pole shift.
```

### Почему это красиво

Theory заранее допускает результат «ничего не нашли в vacuum dispersion».

Это не провал.

Это может быть правильным universality outcome.

---

## Глава 49. Если anisotropy остаётся, она обязана иметь физический источник

Нельзя позволить regulator grid незаметно превратиться в «new physics».

Если directional quartic pole реально survives, должен существовать physical order parameter, который тоже выбирает эти направления.

Например tetrahedral rank-4 tensor order.

Если tensor order under refinement исчезает, а pole anisotropy почему-то остаётся, это сильный признак regulator contamination.

---

# Часть XIV. Как из phase branch может появиться свет

## Глава 50. Откуда берётся compact U(1)

Normalized qubit живёт на S³ в C².

Но physical ray не зависит от общей phase.

Получается Hopf fibration:

```text
U(1) → S³ → S².
```

Phase between neighboring states даёт link variable.

Closed loop даёт Berry/Pancharatnam holonomy.

То есть q=2 quantum carrier естественно содержит compact phase structure.

### Статус

**EXACT KINEMATIC.** Это ещё не доказанный photon.

---

## Глава 51. Что нужно, чтобы phase стала Maxwell field

Нужна dynamics.

Если blocked phase sector получает positive local quadratic action, variation по temporal component автоматически даёт discrete Gauss law.

Transverse sector then obeys Maxwell-like wave equation.

На seed S³ complex:

```text
V=8
E=24
F=32
rank d0=7
rank d1=17
b1=0.
```

Нулевые modes соответствуют gauge image, без лишнего flat physical mode в unit-Hodge control.

### Статус

**CONDITIONAL THEOREM:** если microscopic phase-history генерирует нужный positive local quadratic action, canonical Maxwell structure следует.

Deconfinement и actual stiffness ещё надо вывести динамически.

---

## Глава 52. Почему число 137 нельзя достать из красивой топологии

Compact U(1) фиксирует:

```text
phase periodicity
integer charge lattice.
```

Но Maxwell action может иметь любой positive stiffness `Z_A`:

```text
Gamma_A ~ -(Z_A/4) F².
```

Одна и та же topology допускает разные `Z_A`.

Следовательно topology сама не фиксирует fine-structure constant.

В standard unit-charge convention:

```text
alpha = 1/(4*pi*Z_A).
```

Чтобы получить реальное число, надо вычислить `Z_A` из microscopic dynamics.

### Статус

**NO-GO:** `Hopf topology → 1/137` без dynamics запрещено.

---

## Глава 53. Почему 3+1 dimensions помогают compact U(1)

Это не derivation photon, но важная compatibility story.

В pure compact gauge theories dimensionality сильно влияет на confinement physics.

Наша независимая spatial branch даёт three-dimensional slice, а causal branch — one time-like history direction.

Поэтому compact U(1) живёт именно в 3+1-like setting, где Coulomb/deconfined phase вообще может существовать.

### Статус

**CONDITIONAL COMPATIBILITY**, не proof того, что microscopic phase находится в deconfined basin.

---

# Часть XV. Почему свет и гравитация могут видеть одну и ту же геометрию

## Глава 54. Один metric cone

Если physical IR action имеет одну emergent metric `g`, и к ней минимально подключены gravity и Maxwell sectors, их principal propagation condition использует один и тот же scalar:

```text
s = g^{mu nu} k_mu k_nu.
```

Massless photon и graviton тогда имеют common leading cone:

```text
s = 0.
```

Важно: ни Newton constant `G`, ни electromagnetic stiffness `Z_A` не являются ручками для настройки скорости.

Они задают strengths, а не causal cone.

---

## Глава 55. Почему gravity universal, а electric charge может быть разным

Massless spin-2 consistency в Lorentz-invariant IR требует universal coupling к conserved energy-momentum.

А U(1) gauge consistency требует conservation charge, но не одинакового charge у всех species.

На пальцах:

```text
gravity спрашивает: сколько у тебя энергии и импульса?
photon спрашивает: какой у тебя U(1) charge?
```

Первый coupling universal.

Второй может быть species-dependent.

### Статус

**CONDITIONAL IR THEOREM** при assumptions обычного massless spin-2 Lorentz-invariant sector.

---

# Часть XVI. Где живут G, Lambda и alpha

## Глава 56. Почему нельзя вытащить все константы из одного красивого eigenvalue

Это ещё одна защита от numerology.

Три numbers возникают из трёх разных physical questions.

### Newton constant G

Нужен coefficient перед curvature term в properly normalized physical effective action.

### Cosmological constant Lambda

Нужно найти physical vacuum/background saddle `Gamma` и его curvature.

### Fine-structure constant alpha

Нужен phase stiffness `Z_A`.

То есть:

```text
G      ← gravitational kinetic normalization
Lambda ← vacuum/background saddle
alpha  ← U(1) stiffness.
```

Один Peter–Weyl spectral number не имеет права одновременно быть всеми тремя.

---

# Часть XVII. Даже если vacuum dispersion нулевая, quantum geometry может быть видна

## Глава 57. Нулевой systematic shift не означает нулевые fluctuations

Представь идеально ровную среднюю поверхность воды.

Средний наклон может быть нулём.

Но waves всё равно существуют.

Так же можно иметь:

```text
physical massless pole exactly Lorentz-invariant
но
connected metric fluctuations nonzero.
```

Тогда light interferometer может видеть phase correlations/noise, даже если average time-of-flight dispersion отсутствует.

Это важная вторая experimental branch.

---

## Глава 58. Как metric fluctuation превращается в optical phase

Если небольшая metric perturbation меняет optical path, phase shift примерно linear in metric perturbation:

```text
delta_phi ~ (k*ell/2) J h.
```

Тогда phase covariance связана с metric covariance:

```text
C_phi ~ (k*ell/2)^2 J C_h J^T.
```

То есть quantum geometry можно искать не только как systematic speed anomaly, но и как structured correlated phase fluctuations.

---

# Часть XVIII. Может ли в таком пространстве жить материя?

## Глава 59. S³ допускает spin-1/2 fields

Chosen global spatial topology S³ parallelizable.

У неё существует spin structure.

Более того, поскольку

```text
H¹(S³,Z₂)=0,
```

spin structure единственна.

### Что это значит

Topology выбранного spatial manifold не запрещает fermions и не создаёт много inequivalent spin sectors.

### Что это НЕ значит

Мы пока не вывели:

```text
Standard Model
chirality
SU(3)
electroweak SU(2)
3 generations
Yukawa couplings
particle masses.
```

Geometric `Spin(3) ~ SU(2)` нельзя автоматически объявлять electroweak SU(2).

---

# Часть XIX. Может ли глобальное S³ когда-нибудь проверяться космологически?

## Глава 60. Если S³ survives в continuum cosmology

Тогда spatial FRW curvature sign соответствует closed slicing:

```text
k = +1.
```

Но это не означает, что curvature обязана быть большой сегодня.

Большой curvature radius может сделать observable `Omega_k` очень маленьким.

На S³ также discrete global harmonic spectrum.

То есть global topology потенциально даёт low-k cosmological signatures.

### Статус

**CONDITIONAL:** microscopic/history dynamics ещё должна показать survival global S³ в realistic cosmological state.

---

# Часть XX. Что сегодня уже закрыто, а что ещё нет

## Глава 61. Лестница доказательств

| Вопрос | Статус |
|---|---|
| Почему q=2? | **EXACT** |
| Возникает ли local S² shell? | **EXACT** |
| Дают ли q=2 labels tetrahedral frame? | **EXACT** |
| Можно ли получить face qubits и geometry qubit? | **EXACT / FINITE** |
| Есть ли natural global S³ completion? | **EXACT / FINITE STABILITY** |
| Идёт ли causal-volume exponent к 3? | **EXACT** |
| Есть ли z≈1 finite branch? | **FINITE / FROZEN** |
| Получается ли 3+1-like scaling? | **DERIVED IN DECLARED MODEL** |
| Сглаживается ли coarse geometry как b^-2/-3/-4? | **FINITE PASS** |
| Создаёт ли coarse-graining сам по себе 4D? | **NO — NEGATIVE CONTROL** |
| Есть ли exact shape→metric bridge? | **EXACT** |
| Есть ли local E/T2 split ~8.43%? | **FINITE PASS** |
| Можно ли из 8.43% вывести particle masses? | **NO-GO** |
| Есть ли nontrivial Peter–Weyl higher-shell data? | **FINITE PASS** |
| Closed ли HDA structure в declared control sectors? | **STRUCTURAL/FINITE PASS** |
| Есть ли reduced massless TT positive control? | **EXACT REDUCED** |
| Сколько generic quartic S4 TT observables? | **6 — EXACT** |
| Frozen ли six-observable extractor? | **YES — EXACT** |
| Constraint eigenvalue = physical omega? | **NO — REJECTED SHORTCUT** |
| Есть ли finite master projector? | **EXACT + CI PASS** |
| Есть ли full refinement/rigging projector limit? | **OPEN** |
| Есть ли microscopic physical Gamma[g,A]? | **OPEN** |
| Frozen ли interacting physical six-vector? | **OPEN** |
| Есть ли compact U(1) phase carrier? | **EXACT KINEMATIC** |
| Доказан ли physical Maxwell photon? | **CONDITIONAL / OPEN DYNAMICS** |
| Выведена ли alpha? | **NO** |
| Выведены ли G и Lambda? | **NO** |
| Выведена ли realistic matter sector? | **NO** |
| Есть ли external experimental confirmation? | **NO** |

---

## Глава 62. Четыре дракона, которых нельзя обмануть

### Дракон 1. «Красивое число»

Нельзя взять число из одного sector и назвать его mass, alpha или cosmological constant только потому, что оно похоже.

### Дракон 2. «Regulator — это природа»

Нельзя принять orientation lattice/tetrahedron за physical preferred direction без independent order parameter и refinement stability.

### Дракон 3. «Constraint — это время»

Нельзя назвать constraint spectral variable физической omega без projector/history construction.

### Дракон 4. «Подгоним после данных»

Нельзя менять basis, directions, calibration или submodel после того, как увидели experimental result.

У природы должно оставаться право сказать:

```text
FAIL.
```

---

# Часть XXI. Что сейчас считается главным следующим шагом

## Глава 63. Самая важная незакрытая стрелка

У нас уже есть много structural bridges.

Но настоящая physical prediction требует пройти:

```text
microscopic constraints
→ physical projector / refinement limit
→ physical history or relational boundary amplitude
→ Gamma[g,A,...]
→ physical TT / Maxwell kernels
→ freeze observables
→ one common scale setting
→ blind experiment.
```

Именно здесь theory должна либо действительно стать physics, либо честно провалить gate.

---

# Эпилог. Стена, пиксели и Вселенная

Вернёмся к стене.

Вблизи она шероховатая.

Издалека — гладкая.

Но неровности не исчезли.

Они просто стали меньше одного observable pixel.

Кандидатная идея этого проекта устроена похожим образом.

На самом глубоком уровне может не существовать привычной гладкой координатной ткани.

Есть бинарные distinctions и quantum relations.

Из их combinatorics появляется local S².

Из character algebra появляется tetrahedral geometry.

Из many cells появляется global S³ phase.

Из recursive growth появляется dimension 3.

Из dynamics — z≈1 и 3+1-like history.

Из coarse-graining огромное количество microscopic distinctions перестаёт быть разрешимым по отдельности.

И effective geometry становится гладкой примерно так же, как становится гладкой далёкая штукатурная стена.

Но история на этом не заканчивается.

Smooth geometry ещё должна научиться obey Einstein constraints.

Constraint states ещё должны стать physical histories.

Physical histories ещё должны породить effective action.

Из него ещё должны появиться реальные photon/graviton kernels и measurable numbers.

Поэтому самая честная формула всего проекта сегодня такая:

```text
BIT
→ RELATION
→ LOCAL GEOMETRY
→ SPACE
→ DIMENSION
→ HISTORY
→ COARSE SMOOTHNESS
→ QUANTUM GEOMETRY
→ CONSTRAINTS
→ PHYSICAL PROJECTOR
→ PHYSICAL TIME
→ EFFECTIVE ACTION
→ OBSERVABLES
→ EXPERIMENT.
```

Именно поэтому это научная сказка, а не миф.

В мифе герой обязан победить.

В науке последнюю главу пишет эксперимент.