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
14. Сформулирован условный dimension-selector: если microscopic
    connection/holonomy algebra сама генерирует локальную 2-form duality, либо
    metric-free coarse action строится только из $B\in\Omega^2$ и
    $F(A)\in\Omega^2$ без дополнительного degree-completing field, то
    form-degree closure выделяет $d=4$. Это гипотеза, пока соответствующий
    сектор не возник из frozen rules. Подробности:
    `HODGE_DIMENSION_SELECTOR.md`, `TWO_FORM_DIMENSION_PRINCIPLE.md`.
15. Найден более естественный microscopic carrier: **один qubit на oriented
    2-cell** даёт три Pauli/Bloch компоненты
    $b_f^i={\rm Tr}(\rho_f\sigma^i)$, которые под $SU(2)$ frame rotation
    преобразуются как adjoint $SO(3)$ triplet. С edge $SU(2)$ parallel
    transport такой face-qubit ensemble допускает gauge-covariant blocking в
    adjoint-valued discrete 2-form $B^i$. Random finite test даёт covariance
    errors $\lesssim3\times10^{-15}$. Подробности: `FACE_QUBIT_BFIELD.md`.
16. Plebański/Urbantke gate: для 8 случайных невырожденных tetrad простые
    self-dual 2-forms дают $\Delta_{simp}<4.3\times10^{-16}$ и восстанавливают
    metric через cubic Urbantke tensor с error $<1.8\times10^{-15}$;
    непосредственно проверено $U_{\mu\nu}=12\det(e)g_{\mu\nu}$.
    Важный negative control: volume-preserving $GL(3)$ internal distortion
    оставляет conformal Urbantke metric неизменной до $10^{-15}$, но увеличивает
    simplicity defect до $0.06..0.59$. Поэтому `metric exists` не означает
    `GR metricity`. Подробности: `PLEBANSKI_URBANTKE_BRIDGE.md`.
17. Connection-first Einstein gate: из $B^i$ численно решается
    $D_AB^i=0$ без подачи Levi-Civita connection. Для stereographic $S^4$
    reconstructed curvature имеет anti-self-dual defect $<8.3\times10^{-9}$
    и self-dual matrix $F^{ij}\simeq-\delta^{ij}$. Специальный non-Einstein
    conformally-flat negative control при идеальной metricity даёт
    $\Delta_{ASD}\simeq0.737$, то есть уверенно отвергается.
    Подробности: `PLEBANSKI_CONNECTION_EINSTEIN_GATE.md`.
18. Internal-isotropy null model показывает возможный, но пока только
    условный механизм emergence simplicity без явного penalty:
    для независимых isotropic Bloch vectors traceless covariance defect
    масштабируется как $N^{-0.49914}$; при anisotropic distribution остаётся
    конечным. Это **не** заменяет настоящий $B^i\wedge B^j$ gate.
    Подробности: `scripts/internal_isotropy_proxy.py`.

Это доказанное, условно выведенное или конечномерно проверенное
**кинематическое/геометрическое ядро**, а не полная квантовая гравитация.
Пункты 9--11 усиливают подмост

$$
\text{smooth 4D Regge}\longrightarrow\text{Fierz--Pauli / Einstein--Hilbert},
$$

а пункты 12--18 заменяют прежний расплывчатый `binary -> metric` на более
конкретную connection-first программу

$$
\boxed{
\text{face qubits + edge transport}
\to B^i
\to \text{4D/manifold gates}
\to \Delta_{simp}
\to g_U
\to A_B
\to \Delta_{ASD}
\to \text{Regge/FP/EH/Ward cross-check}.
}
$$

Критически важно: пока эта цепочка проверена по частям на контрольных данных,
но **не получена из одного frozen microscopic dynamics**.

## Какие инварианты ещё нужны

| Инвариант | Требуемый предел |
|:--|:--|
| Frozen microscopic dynamics | один опубликованный local rule/measure hash для $(K_2,\rho_f,U_e)$, не меняемый после held-out run |
| Causal/channel | $\delta_D(\ell)\to0$ |
| Local manifold topology | на spatial slices $D_{link}\to3$ или на full history complex $D_{link}\to4$; defect fraction $\to0$ |
| Diffusion dimension | соответственно $d_s^{slice}\to3$ или $d_s^{history}\to4$ |
| Space-time consistency | $z\to1$ и, для slice interpretation, $\Delta_{3+1}=|d_s^{history}-(1+d_s^{slice}/z)|\to0$ |
| Two-form / Hodge structure | local $B,F$ 2-form sector и duality/top-form defects $\to0$ без dimensional scaffold |
| Plebański metricity | $\Delta_{simp}(b)\to0$ и wedge matrix остаётся невырожденной без whitening/projection |
| Compatible connection | $\Delta_{D_AB}(b)\to0$ с локальным scale-stable $A_B$ |
| Einstein curvature | $\Delta_{ASD}(b)\to0$ (с appropriate matter source после включения материи) |
| Lorentz invariance | угловая анизотропия $\to0$ и единый light cone |
| Spin-2 | ровно две gapless физические моды без ручной TT-проекции в microscopic ensemble |
| Ghost gap | $m_{unwanted}/m_{TT}\to\infty$ |
| Нелинейная ОТО | Ward/HDA closure должна возникнуть после microscopic blocking, а не только на Regge scaffold |
| Универсальность | коэффициенты не зависят от blocking/regulator |
| Материя | ненулевой chiral index и сокращение gauge/gravity anomalies |
| Эксперимент | одно preregistered blind prediction и независимая репликация |

## Главный незакрытый переход

Теперь bottleneck можно записать гораздо точнее:

$$
\boxed{
(K_2,\rho_f,U_e)_{micro}
\xrightarrow{\text{ONE FROZEN LOCAL RULE}}
B^i_b
\text{ with }
D_{link}\to4,
\ d_s\to4,
\ \Delta_{simp}\to0,
\ \Delta_{ASD}\to0.
}
$$

Для canonical slice interpretation вместо full-history `$4$` используются
`$3$` на slice плюс `$z\to1$` и consistency defect `$\Delta_{3+1}\to0$`.

После этого на **том же ensemble и том же scaling window** без ручной
TT-проекции должны пройти

$$
N_{gapless}=2,
\qquad
m_{unwanted}/m_{TT}\to\infty,
\qquad
W_3\to0.
$$

Если один frozen rule не даёт эту совместную сходимость, конкретная версия
CIMFIG отвергается независимо от качества отдельно заданного Regge scaffold.

Физически подтверждённой теорией кандидат станет только после blind prediction
и независимой экспериментальной репликации.
