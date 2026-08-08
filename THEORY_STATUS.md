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
10. Нелинейный тест на generic three-wave metric field: отдельно quadratic и
    cubic коэффициенты конечного Regge action сходятся к прямому численному
    $\int\sqrt g R$ с ожидаемой нормировкой
    $S_{Regge}/S_{EH}\to1/2$. На $L=5..8$ ошибки $c_2$, $c_3$ и $c_3/c_2$
    убывают примерно как $L^{-1.87}$, $L^{-1.82}$ и $L^{-1.91}$;
    экстраполяции дают $0.497924$ и $0.491859$ для $c_2$ и $c_3$.
    Подробности: `REGGE_EH_CUBIC_BRIDGE.md`.

Это доказанное или конечномерно проверенное **кинематическое/геометрическое ядро**, а не полная
квантовая гравитация. Пункты 9--10 относятся к 4D Regge scaffold и сами по себе не
доказывают ни возникновение четырёхмерности, ни RG-переход из binary edge-bit
ensemble, ни нелинейную gauge closure.

## Какие инварианты ещё нужны

| Инвариант | Требуемый предел |
|:--|:--|
| Causal/channel | $\delta_D(\ell)\to0$ |
| Размерность | $d_s(\ell)\to4$ |
| Лоренц-инвариантность | $z(\ell)\to1$, угловая анизотропия $\to0$ |
| Spin-2 | ровно две gapless TT-моды без ручной проекции |
| Ghost gap | $m_{\rm unwanted}/m_{\rm TT}\to\infty$ |
| Нелинейная ОТО | замыкание hypersurface-deformation algebra и cubic Ward identity |
| Универсальность | коэффициенты не зависят от blocking/regulator |
| Материя | ненулевой chiral index и сокращение gauge/gravity anomalies |
| Эксперимент | одно preregistered blind prediction и независимая репликация |

## Один следующий расчёт

Для gravity gate следующий минимальный удар — не ещё один TT-fit и не ещё один
scalar action coefficient, а **cubic gauge-closure test**. На independent
connection/frame variables либо на явно выведенном nonlinear gauge map нужно
вычислить на momentum-conserving triads

$$
W_3(\ell)=
\frac{\|\delta_0S_3+\delta_1S_2\|}
{\|S_3\|+\|S_2\|}
$$

и потребовать $W_3(\ell)\to0$ одновременно с уже измеряемыми quadratic
Fierz--Pauli residual, cubic Regge/EH residual и angular anisotropy.

Для полного microscopic gate по-прежнему нужно зафиксировать один малый EML
rule set; без TT-проекции выполнить blocking на последовательности размеров и
на каждом масштабе совместно измерить

$$
(\delta_D,d_s,z,\operatorname{spec}H,
\lVert\{H,H\}-D\rVert,\operatorname{index}D_{\rm chiral}).
$$

Если все первые восемь инвариантов стремятся к требуемым пределам в одном
масштабном окне, математический кандидат на континуальную квантовую гравитацию
получен. Физически подтверждённой теорией он станет только после последнего,
экспериментального инварианта.
