# Центральная цепь: binary quantum microstructure → smooth spacetime

## 1. Физическая постановка

Репозиторий рассматривает гипотезу, что фундаментальные локальные степени свободы могут быть дискретными и в минимальной модели двухуровневыми, а гладкая геометрия возникает как эффективное описание большого числа таких квантовых степеней свободы.

Обозначим микроскопический cutoff через

$$
\ell_*.
$$

Возможное отождествление $\ell_*\sim\ell_P$ с планковским масштабом является **гипотезой физической интерпретации**, а не установленным здесь фактом. Современная физика не требует, чтобы планковская длина была буквально доказанной минимальной длиной или чтобы один планковский объём был классическим битом.

Минимальный quantum-bit объект записывается как

$$
|\psi_e\rangle
=\alpha_e|0\rangle+\beta_e|1\rangle,
\qquad
|\alpha_e|^2+|\beta_e|^2=1,
$$

а многоузловое состояние — как состояние на тензорном произведении локальных пространств

$$
\mathcal H_\Gamma=\bigotimes_{e\in\Gamma}\mathcal H_e.
$$

Ключевая задача — не объявить граф пространством-временем, а вывести из квантового состояния геометрические наблюдаемые и показать их переход к ОТО.

---

## 2. Центральный мост

На уровне архитектуры проверяется цепь

$$
\boxed{
\rho_{micro}
\xrightarrow{\text{quantum dynamics}}
\rho_{\Gamma}
\xrightarrow{\text{geometric observables}}
\mathcal G_{discrete}
\xrightarrow{\mathcal C_b}
(g_{ab}^{(b)},K_{ab}^{(b)})
\xrightarrow[b\to\infty]{\ell_*/L\to0}
(g_{ab},K_{ab})
\xrightarrow{\text{constraints}}
\text{GR}
}
$$

где:

- $\rho_{micro}$ — microscopic quantum state;
- $\mathcal G_{discrete}$ — набор дискретных геометрических наблюдаемых;
- $\mathcal C_b$ — coarse-graining map;
- $g_{ab}^{(b)}$ и $K_{ab}^{(b)}$ — effective spatial metric и extrinsic-curvature data на масштабе блока $b$;
- continuum limit должен удовлетворять Einstein/ADM dynamics и hypersurface-deformation algebra.

Именно последние две стрелки отличают квантовую гравитацию от произвольной дискретной модели.

---

## 3. Квантовая динамика и гравитационные ограничения

Для обычной квантовой системы

$$
i\hbar\partial_t|\Psi\rangle=\hat H|\Psi\rangle.
$$

В generally covariant канонической гравитации lapse и shift умножают ограничения. Поэтому целевой quantum-gravity объект имеет структуру

$$
\hat H[N]|\Psi_{phys}\rangle\approx0,
\qquad
\hat D[\vec N]|\Psi_{phys}\rangle\approx0,
$$

а их коммутаторы должны воспроизводить правильную деформационную алгебру в semiclassical/continuum режиме:

$$
\boxed{
\frac{1}{i\hbar}
[\hat H[N],\hat H[M]]
\longrightarrow
\hat D\!\left[q^{ab}(N\partial_bM-M\partial_bN)\right].
}
$$

Поэтому в проекте HDA является более сильным тестом, чем простое совпадение спектра или размерности.

---

## 4. Не расстояние делает пространство-время гладким — coarse-graining делает микроструктуру неразрешимой

Корректная версия аналогии со стеной:

```text
микроскопически: отдельные неровности / дискретные элементы
макроскопически: один разрешаемый элемент содержит очень много микродеталей
```

Стена не становится физически гладкой от удаления наблюдателя. Аналогично microscopic spacetime не меняется от расстояния до наблюдателя. Меняется resolution scale.

Вводим

$$
\ell_{obs}\gg\ell_*
$$

и coarse factor

$$
b\sim\frac{\ell_{obs}}{\ell_*}.
$$

Тогда effective geometry определяется не отдельными microscopic labels, а coarse observables:

$$
\boxed{
\mathcal G_{eff}(b)=\mathcal C_b[\rho_\Gamma,\mathcal G_{micro}].
}
$$

В infrared limit требуется, чтобы различия между соседними coarse descriptions стремились к нулю после физической нормировки:

$$
\|\mathcal G_{eff}(2b)-\mathcal G_{eff}(b)\|
\to0.
$$

Это и есть математически проверяемая версия появления гладкости.

---

## 5. Frozen binary-route family и emergent spatial dimension

В текущем toy family $R_q$:

1. causal link заменяется всеми $2^q$ двухшаговыми маршрутами;
2. маршрут имеет $q$ binary labels;
3. route states соединяются intra-cell link при Hamming distance one;
4. рекурсивно переписываются causal child links.

Один rewrite удваивает линейный масштаб:

$$
\lambda_\ell=2,
$$

а число causal child links растёт как

$$
\lambda_V=2^{q+1}.
$$

Поэтому для этого конкретного family

$$
\boxed{
d_H
=\frac{\log\lambda_V}{\log\lambda_\ell}
=q+1.
}
$$

Это combinatorial result внутри объявленного family, а не универсальная теорема о природе.

Для frozen candidates $q=1,2,3$ train protocol выбрал $q=2$ до held-out generation. Held-out transition дал

$$
\boxed{d_H=2.999229782},
\qquad
\boxed{z=0.998281156},
$$

и

$$
\boxed{d_s^{slice}=3.004393867}.
$$

При добавлении одной causal-time scaling direction получается 4D-like history scaling

$$
d_{history}\approx4.004393867.
$$

Это finite train/held-out result данной модели.

---

## 6. Локальный topology precursor

Route labels $q=2$ образуют

$$
Q_2=C_4.
$$

Suspension двух causal endpoints над $C_4$ даёт octahedral $S^2$ local shell. Это согласуется с link structure локального трёхмерного PL-комплекса.

Репозиторий отдельно проверяет выбранное глобальное completion через boundary 4D cross-polytope и barycentric refinements.

Важно:

```text
local S2 link + one valid global S3 completion
!=
proof that microscopic dynamics uniquely selects that global topology.
```

Динамический выбор topology остаётся отдельной задачей.

---

## 7. Почему coarse fluctuations могут выглядеть гладкими

Если coarse block содержит

$$
N(b)\sim b^{d_H+z}\approx b^4
$$

слабо коррелированных unbiased microscopic contributions, стандартное self-averaging даёт

$$
\delta g_{RMS}\sim N^{-1/2}\sim b^{-2}.
$$

В текущем stochastic control измерено

$$
\delta g\sim b^{-2.001707},
$$

$$
\nabla\delta g\sim b^{-3.001458},
$$

$$
\delta R_{proxy}\sim b^{-4.000524}.
$$

Эти показатели являются finite diagnostics конкретного control. Они не должны называться универсальными critical exponents без доказательства universality и контроля корреляций.

---

## 8. От qubit observables к метрике

Отдельная end-to-end Euclidean ветка реализует

$$
\boxed{
\rho_f
\to
B^i_{\mu\nu}
\to
\Delta_{simp}
\to
g_U
\to
A_B
\to
F(A_B)
\to
\text{Einstein-curvature test}.
}
$$

Здесь $g_U$ — Urbantke metric, реконструируемая из two-form data.

Положительный искусственный $S^4$ control восстанавливает

```text
Lambda_rec = 2.9999998973
Lambda_exact = 3
relative error ≈ 3.42e-8
```

но этот результат **не является предсказанием физической космологической постоянной**: target curvature задан входным control geometry. Ценность теста в том, что downstream reconstruction не получает метрику напрямую и отдельный non-Einstein control проваливает финальный curvature gate.

Главная открытая стрелка:

$$
\boxed{
\text{same frozen microscopic binary dynamics}
\dashrightarrow
\text{required geometric qubit/two-form state}
}
$$

без oracle encoding target geometry.

---

## 9. Дискретная кривизна → гладкая ОТО

Для геометрического continuum bridge проект использует Regge-type discrete curvature и независимые Plebanski/Urbantke controls.

Целевой предел действия:

$$
\boxed{
S_{discrete}[\Gamma_n]
\longrightarrow
S_{EH}[g]
=\frac{c^3}{16\pi G}
\int d^4x\sqrt{-g}(R-2\Lambda).
}
$$

Недостаточно получить smooth metric. Нужно также получить правильную динамику:

$$
G_{\mu\nu}+\Lambda g_{\mu\nu}
=\frac{8\pi G}{c^4}T_{\mu\nu}
$$

или эквивалентную каноническую constraint structure в заявленном секторе.

---

## 10. Почему в классическом пределе у гравитации две локальные поляризации

Если continuum limit действительно даёт 3+1-dimensional GR с first-class Hamiltonian и diffeomorphism constraints, стандартный Dirac degree counting оставляет две локальные конфигурационные степени свободы метрического гравитационного поля. В линейном vacuum limit они соответствуют двум helicities массового spin-2 гравитона.

Это свойство **ОТО и её корректного квантового/семиклассического предела**. Оно не выводится из одного факта, что microscopic objects бинарны.

---

## 11. Текущий статус центральной цепи

```text
binary/qubit microscopic degrees        candidate ansatz
q=2 finite dimension/smoothing gate     tested_finite
selected PL completion                  tested_finite
qubit -> B -> Urbantke -> Einstein      tested_finite oracle control
Regge/EH finite bridge                  tested_finite
route-normal HDA principal symbol       tested_finite
two-node Peter-Weyl x route regression  tested_finite
fixed-cutoff composition bound          proved under stated assumptions

micro dynamics -> geometric qubit phase OPEN
global topology dynamical selection     OPEN
multi-node graph-changing off-shell HDA OPEN
uniform regulator removal               OPEN
physical scale setting                  OPEN
blind external physical prediction      OPEN
```

Поэтому корректный итог сейчас:

$$
\boxed{
\text{discrete quantum microstructure}
\;
\overset{\text{finite bridges}}{\Longrightarrow}
\;
\text{a coherent candidate route to smooth GR},
}
$$

но не доказательство завершённой квантовой теории гравитации.
