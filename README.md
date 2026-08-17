# Information Graph Theory: от бинарной квантовой микроструктуры к гладкому пространству-времени

Этот репозиторий исследует **кандидатную математико-вычислительную схему квантовой гравитации**, в которой микроскопические степени свободы дискретны и бинарны, а гладкая геометрия общей теории относительности должна возникать только в крупномасштабном пределе.

Главная задача проекта теперь формулируется узко:

```text
binary / qubit degrees of freedom
        ↓
quantum state and quantum operators
        ↓
discrete geometric observables
        ↓
coarse-graining / refinement
        ↓
smooth metric and curvature
        ↓
Einstein / ADM / HDA continuum limit
```

Это **не экспериментально подтверждённая теория природы**. Репозиторий содержит точные конечномерные результаты, численные регрессии, контролируемые toy-модели и явно отмеченные открытые переходы.

---

## 1. Что значит «пространство-время состоит из битов»

В модели фундаментальный объект — не заранее заданная гладкая координатная сетка, а конечный набор локальных двухуровневых квантовых степеней свободы. Классический бит имеет состояния `0/1`; квантовый двухуровневый объект имеет состояние

$$
|\psi\rangle=\alpha|0\rangle+\beta|1\rangle,
\qquad
|\alpha|^2+|\beta|^2=1.
$$

Для многих локальных двухуровневых систем пространство состояний является тензорным произведением

$$
\mathcal H=\bigotimes_e \mathcal H_e,
\qquad
\dim\mathcal H_e=2
$$

в минимальной бинарной модели. Геометрия должна быть не входным фоном, а набором наблюдаемых или эффективных переменных, построенных из состояния на $\mathcal H$.

Микроскопический cutoff обозначим $\ell_*$. Отождествление $\ell_*$ с планковской длиной является **дополнительной физической гипотезой модели**, а не результатом конечных вычислений в этом репозитории.

---

## 2. Квантовая механика: динамика микросостояний

Для обычной квантовой системы динамика задаётся

$$
i\hbar\frac{\partial}{\partial t}|\Psi\rangle
=\hat H|\Psi\rangle.
$$

В канонической гравитации ситуация тоньше: lapse и shift выступают множителями ограничений, а физическая теория должна согласовать гамильтоново и диффеоморфное ограничения. Поэтому ключевой объект проекта — не попытка просто подставить метрику в обычное уравнение Шрёдингера, а построение квантовых операторов геометрии и ограничений на общем пространстве состояний.

Схематически:

$$
\hat H[N]|\Psi\rangle\approx0,
\qquad
\hat D[\vec N]|\Psi\rangle\approx0,
$$

а в semiclassical/continuum режиме коммутаторы должны воспроизводить классическую алгебру деформаций гиперповерхности.

---

## 3. ОТО: целевой гладкий предел

Классическая целевая динамика — уравнения Эйнштейна

$$
G_{\mu\nu}+\Lambda g_{\mu\nu}
=\frac{8\pi G}{c^4}T_{\mu\nu},
$$

получаемые из действия Эйнштейна–Гильберта

$$
S_{EH}
=\frac{c^3}{16\pi G}
\int d^4x\,\sqrt{-g}\,(R-2\Lambda)+S_{matter}.
$$

Дискретная теория не считается связанной с ОТО только потому, что в ней есть граф или кванты площади. Нужны проверяемые мосты:

1. квантовые данные $\to$ геометрические наблюдаемые;
2. дискретная метрика/кривизна $\to$ гладкая метрика/кривизна;
3. дискретное гравитационное действие $\to S_{EH}$ при refinement;
4. гамильтоновы ограничения $\to$ правильная HDA;
5. результаты должны быть устойчивы к увеличению cutoff и размерности вычислительного пространства.

---

## 4. Центральный мост: qubit → two-form → metric → Einstein test

Один из самых чистых конечномерных тестов проекта начинается непосредственно с qubit density matrices на ориентированных 2-faces:

$$
\rho_{\mu\nu}
\longrightarrow
B^i_{\mu\nu}
\longrightarrow
\Delta_{simp}
\longrightarrow
g_U
\longrightarrow
A_B
\longrightarrow
F(A_B).
$$

В `scripts/qubit_to_einstein_end_to_end.py` исходная гладкая метрика не передаётся в реконструктор. Downstream-геометрия восстанавливается через Pauli expectations, simplicity и Urbantke construction.

Положительный $S^4$-control восстанавливает

```text
Lambda_rec = 2.9999998973
Lambda_exact = 3
relative error ≈ 3.42e-8
```

для **искусственно заданного Euclidean control dataset**. Это проверка composability математических стрелок, а не предсказание наблюдаемой космологической постоянной.

Отдельный non-Einstein negative control проходит ранние metric-стрелки и затем проваливает Einstein-curvature test. Поэтому тест различает «получилась гладкая метрика» и «получилась Einstein geometry».

Подробно: `QUBIT_TO_EINSTEIN_END_TO_END.md`.

---

## 5. Дискретность и гладкость: правильная интерпретация масштаба

Не расстояние до объекта физически делает пространство-время более гладким. Меняется **доступное разрешение наблюдателя**.

Аналогия со стеной полезна в таком виде: вблизи видна структура краски, издалека при конечном угловом разрешении множество микродеталей попадает в один разрешаемый элемент. Стена не изменилась — изменился coarse-graining.

В модели это записывается как

$$
\mathcal G_{micro}
\xrightarrow{\;\mathcal C_b\;}
\mathcal G_{eff}(b),
$$

где $b$ — размер coarse block в единицах микроскопического cutoff.

Для frozen binary-route rule семейства $R_q$ один spatial rewrite удваивает линейный масштаб, а число causal child links растёт как $2^{q+1}$. Поэтому асимптотически

$$
d_H=q+1.
$$

В объявленном train/held-out протоколе среди $q=1,2,3$ был выбран $q=2$, а held-out transition дал

```text
d_H        = 2.999229782
z          = 0.998281156
d_s(slice) = 3.004393867
```

При добавлении одной causal-time scaling direction получается 4D-like history scaling.

Для слабокоррелированных unbiased microscopic fluctuations стандартное self-averaging даёт

$$
\delta g_{RMS}\sim N(b)^{-1/2}.
$$

В текущем finite stochastic control измерены законы

```text
metric fluctuation   ~ b^-2.001707
gradient fluctuation ~ b^-3.001458
curvature proxy      ~ b^-4.000524
```

Эти числа являются характеристиками конкретного вычислительного control, а не доказательством универсального закона природы.

Подробно: `BIT_TO_SPACETIME_CENTRAL_EQUATION.md`, `OBSERVER_SCALE_SMOOTHING.md`.

---

## 6. Локальная и глобальная геометрия

Для frozen $q=2$ route states образуют $Q_2=C_4$. Добавление двух causal endpoints даёт suspension $\Sigma C_4$, то есть октаэдральную $S^2$-оболочку.

`bcqg_global_manifold_gate.py` проверяет естественное минимальное PL-завершение — boundary 4D cross-polytope — и его barycentric refinements. Для выбранного completion проверяются vertex/edge/face links, orientability, $\partial^2=0$ и homology.

Это доказывает **существование и стабильность выбранного PL completion**. Это не доказывает, что bare microscopic rewrite единственным образом динамически выбирает именно это глобальное склеивание.

---

## 7. Regge → Einstein–Hilbert

В дискретной геометрии curvature кодируется deficit angles на simplices/hinges. Проект содержит отдельные gates, проверяющие дискретный Regge/EH bridge и continuum scaling:

- `REGGE_EH_CUBIC_BRIDGE.md`
- `scripts/regge_eh_cubic_bridge.py`
- `scripts/verify_geometric_cell.py`
- `scripts/verify_connection_ward.py`

Критерий здесь принципиальный: при refinement дискретное действие и вариационные identities должны стремиться к соответствующим continuum quantities без перенастройки параметров после просмотра результата.

---

## 8. HDA — главный тест ковариантной динамики

В ADM/canonical GR ограничения удовлетворяют hypersurface-deformation algebra. Центральная скобка имеет структуру

$$
\{H[N],H[M]\}
=
D\!\left[q^{ab}(N\partial_bM-M\partial_bN)\right].
$$

Квантовый целевой предел:

$$
\frac{1}{i\hbar}
[\hat H[N],\hat H[M]]
\longrightarrow
\hat D\!\left[q^{ab}(N\partial_bM-M\partial_bN)\right].
$$

Репозиторий уже содержит несколько разных уровней этого теста:

- path-vector / rerouting diffeomorphism algebra;
- route-normal principal-symbol HDA;
- two-node Peter–Weyl × route finite regression;
- fixed-cutoff Lorentzian composition bound;
- graph-changing HDA target, где fixed-sector leakage не отождествляется автоматически с anomaly.

Важно различать уровни доказательства. `bcqg_quantum_hda_killer.py` прямо возвращает

```text
full_quantum_HDA_closed = false
```

для полного microscopic operator problem, хотя route-sector principal-symbol gate проходит. Поэтому multi-node, graph-changing, regulator-independent off-shell closure остаётся центральной задачей, а не уже установленным фактом.

---

## 9. Что сейчас действительно проверено

Machine-readable статус хранится в `theory_gates.json`.

Основные finite/exact компоненты:

- frozen binary-route dimensional/smoothing test;
- выбранное recursive PL 3-manifold completion;
- finite Peter–Weyl/SU(2) geometry operators;
- qubit → $B$ → Urbantke metric → Einstein curvature control;
- Regge/EH continuum bridge controls;
- route/diffeomorphism HDA controls;
- preregistered two-node Euclidean Peter–Weyl × route scaling test;
- fixed-cutoff Lorentzian support/composition result.

Сильнейшие утверждения относятся к **конкретным конечным моделям, cutoff и объявленным scaling limits**. Они не автоматически переносятся на природу.

---

## 10. Что остаётся открытым

Ключевые незакрытые физические стрелки:

1. вывести нужный geometric qubit/two-form sector из одной и той же microscopic binary dynamics, а не кодировать его oracle-control данными;
2. доказать динамический выбор глобальной 3-manifold фазы;
3. получить полноценную graph-changing off-shell quantum HDA на многоузловом habitat;
4. контролировать совместный предел refinement/cutoff, а не только фиксированный безопасный cutoff;
5. построить Lorentzian quantum measure и доказать физическую unitary/causal consistency;
6. вывести $G$, $\Lambda$ и другие размерные физические масштабы из microscopic observables;
7. зарегистрировать **слепые физические предсказания до сравнения с экспериментом**, затем проверить их на независимых данных.

Пока пункт 7 не выполнен для конкретной наблюдаемой величины с заранее frozen protocol, совпадение внутреннего dimensionless control с известной константой нельзя называть предсказанием этой константы.

---

## 11. Фальсифицируемость

Архитектура должна считаться опровергнутой или требующей пересмотра, если хотя бы один обязательный bridge систематически не проходит при заранее фиксированном протоколе:

```text
binary rule
  → wrong dimension/topology
  → no stable geometric sector
  → no Regge/EH continuum convergence
  → wrong Einstein curvature test
  → HDA anomaly / wrong structure function
  → regulator dependence that does not vanish
  → blind observable disagrees with experiment
```

Особенно важны held-out/refinement tests: параметры фиксируются **до** запуска следующего масштаба или физической выборки.

---

## 12. Воспроизведение ядра

```bash
python -m pip install -r requirements.txt

python bcqg_observer_smoothing_unified.py
python bcqg_global_manifold_gate.py
python scripts/qubit_to_einstein_end_to_end.py
python scripts/regge_eh_cubic_bridge.py
python scripts/path_normal_hda_gate.py
python scripts/peter_weyl_two_node_euclidean_joint_gate.py
python bcqg_quantum_hda_killer.py
python bcqg_bit_to_gravity_final.py --strict
```

Полная machine-readable карта обязательств:

```bash
python scripts/verify_theory_gates.py
```

GitHub Actions запускает тот же canonical regression subset.

---

## 13. Карта ключевых файлов

| Задача | Файл |
|---|---|
| Центральная binary → continuum постановка | `BIT_TO_SPACETIME_CENTRAL_EQUATION.md` |
| Observer coarse-graining | `OBSERVER_SCALE_SMOOTHING.md` |
| Global PL completion | `GLOBAL_MANIFOLD_Q2_COMPLETION.md` |
| Qubit → Einstein single-path control | `QUBIT_TO_EINSTEIN_END_TO_END.md` |
| Regge → EH | `REGGE_EH_CUBIC_BRIDGE.md` |
| Plebanski/Urbantke bridge | `PLEBANSKI_URBANTKE_BRIDGE.md` |
| HDA structural target | `QUANTUM_HDA_KILLER_RESULT.md` |
| Graph-changing HDA | `GRAPH_CHANGING_HDA_TARGET.md` |
| Fixed-cutoff composition | `FIXED_CUTOFF_COMPOSITION_BOUND.md` |
| Текущий статус | `THEORY_STATUS.md` |
| Открытые задачи | `OPEN_PROBLEMS.md` |

---

## 14. Научная дисциплина проекта

Для каждого результата репозиторий должен явно указывать один из уровней:

```text
proved          — точное математическое утверждение в объявленной модели
tested_finite   — воспроизводимый конечномерный/численный тест
conditional     — следствие при явно записанной дополнительной гипотезе
open            — обязательный переход ещё не закрыт
```

Никакой finite PASS сам по себе не повышается до «экспериментально подтверждённой квантовой гравитации».

Цель проекта — не максимальная громкость формулировок, а одна проверяемая цепь:

$$
\boxed{
\text{quantum binary microstructure}
\to
\text{discrete quantum geometry}
\to
\text{coarse-grained smooth geometry}
\to
\text{GR dynamics in the continuum limit}
}
$$