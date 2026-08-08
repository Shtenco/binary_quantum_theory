# Статус теории — кратко

## Что уже получено

1. Дискретная производная $B$ и лапласиан $L=B^\dagger B\geq0$.
2. Точный синусовый символ
   $\widehat L(k)=4\sum_i\sin^2(k_i/2)$.
3. Симплектическая свободная динамика и две TT-компоненты линейного сектора.
4. Квантовый язык boundary density operators и channels, совместимый с Bell/CHSH.
5. Уравнение Гейзенберга для динамики наблюдаемых.
6. Локальное удаление чистой connection и сохранение loop holonomy.
7. Кинематический bit-to-smooth crossover и слабополевой предел
   $\ddot x\to-\nabla\Phi$.
8. Условная абсолютная сходимость регуляризованных спектральных сумм.
9. Тест без TT-проекции: полный 10-компонентный metric Hessian плоской
   4D Regge-решётки на $L=3,4,5$ приближается к квадратичной структуре
   Fierz--Pauli; full-matrix residual, ошибка отношений коэффициентов и
   generic gauge-to-metric leakage убывают приблизительно как $O(L^{-2})$.
   Подробности: `GRAVITY_BRIDGE_SCALING.md`.
10. Нелинейный generic three-wave test: отдельно quadratic и cubic
    коэффициенты конечного Regge action сходятся к прямому численному
    $\int\sqrt g R$ с ожидаемой нормировкой $S_{Regge}/S_{EH}\to1/2$.
    На $L=5..8$ ошибки $c_2$, $c_3$ и $c_3/c_2$ убывают примерно как
    $L^{-1.87}$, $L^{-1.82}$ и $L^{-1.91}$; экстраполяции дают $0.497924$
    и $0.491859$ для $c_2$ и $c_3$. Подробности: `REGGE_EH_CUBIC_BRIDGE.md`.
11. Прямой cubic Ward test без TT-проекции: для
    $g=\eta+\lambda h$ отдельно извлечены $\delta_0S_3$ и $\delta_1S_2$.
    Continuum EH control даёт $W_3\sim10^{-9}$, а finite Regge defect
    монотонно падает
    $0.1552\to0.05955\to0.03444\to0.02267\to0.01614\to0.01210$
    на $L=3..8$; на $L=5..8$ $W_3\sim L^{-2.23}$.
    Подробности: `CUBIC_WARD_SCALING.md`.
12. Dimension-blind falsifier: минимальный coordinate-free binary diamond
    `edge -> two alternative two-step paths -> reconvergence` **не** рождает
    4D. Его effective volume dimension идёт
    $1.874\to1.967\to1.992$, а полный heat-kernel test на поколении 5 даёт
    $d_s=2.0698\pm0.0181$. Контрольный estimator независимо различает
    1D/2D/3D/4D тори. Подробности: `BINARY_TO_GEOMETRY_GATE.md`.
13. Добавлен coordinate-free local topology gate: по homology vertex links
    без embedding coordinates корректно восстанавливаются 2D, 3D и 4D
    контрольные periodic complexes; это готовый falsifier для frozen hypergraph.
    Подробности: `MANIFOLD_DIMENSION_GATE.md`.
14. Сформулирован новый условный dimension-selector: если microscopic
    connection/holonomy algebra **сама** генерирует локальную Hodge duality,
    то closure curvature 2-forms внутри того же 2-form sector требует полного
    spacetime dimension $d=4$; в canonical split edge/face duality требует
    spatial $D=3$. Это гипотеза, пока duality map не выведена из frozen rules.
    Подробности: `HODGE_DIMENSION_SELECTOR.md`.

Это доказанное, условно выведенное или конечномерно проверенное
**кинематическое/геометрическое ядро**, а не полная квантовая гравитация.
Пункты 9--11 существенно усиливают подмост

$$
\text{smooth 4D Regge}\longrightarrow\text{Fierz--Pauli / Einstein--Hilbert},
$$

но стартуют с заранее заданного 4D Regge scaffold. Пункты 12--14 теперь
отдельно атакуют более ранний и главный разрыв — возникновение самой геометрии.

## Какие инварианты ещё нужны

| Инвариант | Требуемый предел |
|:--|:--|
| Frozen microscopic dynamics | один опубликованный rule/measure hash, не меняемый после held-out run |
| Causal/channel | $\delta_D(\ell)\to0$ |
| Local manifold topology | на spatial slices $D_{\rm link}\to3$ или на full history complex $D_{\rm link}\to4$; defect fraction $\to0$ |
| Diffusion dimension | соответственно $d_s^{\rm slice}\to3$ или $d_s^{\rm history}\to4$ |
| Space-time consistency | $z\to1$ и, для slice interpretation, $\Delta_{3+1}=|d_s^{history}-(1+d_s^{slice}/z)|\to0$ |
| Hodge/connection duality | если dimension-selector используется: локальные edge/face или 2-form duality defects $\to0$ без post-hoc fit |
| Lorentz invariance | угловая анизотропия $\to0$ и единый light cone |
| Spin-2 | ровно две gapless TT-моды без ручной проекции в microscopic ensemble |
| Ghost gap | $m_{\rm unwanted}/m_{\rm TT}\to\infty$ |
| Нелинейная ОТО | Ward/HDA closure должна возникнуть после microscopic blocking, а не только на Regge scaffold |
| Универсальность | коэффициенты не зависят от blocking/regulator |
| Материя | ненулевой chiral index и сокращение gauge/gravity anomalies |
| Эксперимент | одно preregistered blind prediction и независимая репликация |

## Главный незакрытый переход

После Regge quadratic/cubic/Ward tests ещё один тест чистого Regge уже не является
главным бутылочным горлышком. Главная стрелка:

$$
\boxed{
\text{frozen binary causal/frame + loop rule}
\dashrightarrow
\text{3+1 / 4D manifold-like metric phase}
}
$$

Причём теперь запрещено засчитывать одно число $d_s\approx4$ как доказательство.
Размерность должна одновременно появиться в **независимых** структурах:

1. local topology через vertex links;
2. diffusion / heat kernel;
3. dynamical scaling $z$;
4. при использовании нового selector — Hodge edge/loop duality.

Для canonical slice interpretation требуется одно scaling window

$$
D_{\rm link}\to3,
\qquad
d_s^{\rm slice}\to3,
\qquad
z\to1,
\qquad
\Delta_{3+1}\to0.
$$

После этого на том же coarse ensemble без ручной TT-проекции должны пройти

$$
\operatorname{spec}H:\;N_{\rm gapless}=2,
\qquad
m_{\rm unwanted}/m_{\rm TT}\to\infty,
\qquad
W_3\to0.
$$

Если frozen microscopic rule не даёт **одно общее scaling window** для этих
условий, конкретная версия CIMFIG отвергается независимо от того, насколько
хорошо отдельно заданный Regge scaffold воспроизводит Einstein--Hilbert.

Физически подтверждённой теорией кандидат станет только после blind prediction
и независимой экспериментальной репликации.
