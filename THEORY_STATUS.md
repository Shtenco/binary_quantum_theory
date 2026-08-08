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

Это доказанное или конечномерно проверенное **кинематическое/геометрическое ядро**, а не полная
квантовая гравитация. Пункты 9--11 существенно усиливают именно подмост

$$
\text{smooth 4D Regge}\longrightarrow\text{Fierz--Pauli / Einstein--Hilbert},
$$

но все они стартуют с заранее заданного 4D Regge scaffold. Они не доказывают
возникновение Regge/metric phase из binary edge-bit/frame rewrite ensemble.

## Какие инварианты ещё нужны

| Инвариант | Требуемый предел |
|:--|:--|
| Causal/channel | $\delta_D(\ell)\to0$ |
| Размерность | $d_s(\ell)\to4$ без заранее заданного 4D scaffold |
| Лоренц-инвариантность | $z(\ell)\to1$, угловая анизотропия $\to0$ |
| Spin-2 | ровно две gapless TT-моды без ручной проекции в microscopic ensemble |
| Ghost gap | $m_{\rm unwanted}/m_{\rm TT}\to\infty$ |
| Нелинейная ОТО | Ward/HDA closure должна возникнуть после microscopic blocking, а не только на Regge scaffold |
| Универсальность | коэффициенты не зависят от blocking/regulator |
| Материя | ненулевой chiral index и сокращение gauge/gravity anomalies |
| Эксперимент | одно preregistered blind prediction и независимая репликация |

## Один следующий расчёт

После пунктов 9--11 **ещё один тест чистого Regge уже не является главным
бутылочным горлышком**. Главный незакрытый переход теперь:

$$
\boxed{
\text{binary causal/frame rules}
\dashrightarrow
\text{4D Regge/metric critical phase}
}
$$

Нужно зафиксировать **один** малый EML/rewrite rule set и не менять его после
просмотра результатов. Затем без TT-проекции выполнить blocking на
последовательности размеров и на каждом масштабе совместно измерить

$$
(\delta_D,d_s,z,\operatorname{spec}H,
W_3,\operatorname{index}D_{\rm chiral}).
$$

Ключевой falsifier: первые пять gravity-инвариантов должны входить в одно и то
же scaling window, причём 4D и spin-2 не должны быть встроены в coarse basis.
Если для frozen microscopic rule этого не происходит, конкретная версия
CIMFIG отвергается, независимо от того, насколько хорошо отдельный Regge
scaffold воспроизводит Einstein--Hilbert.

Если все первые восемь инвариантов стремятся к требуемым пределам в одном
масштабном окне, математический кандидат на континуальную квантовую гравитацию
получен. Физически подтверждённой теорией он станет только после последнего,
экспериментального инварианта.
