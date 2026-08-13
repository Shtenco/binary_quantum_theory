# Центральное уравнение: binary Planck rule -> observer-accessible spacetime

## 1. Не расстояние меняет геометрию — меняется разрешение

Основная effective-map формулировка:

$$
\boxed{
\mathcal G_{\rm Planck}^{\rm binary}
\xrightarrow{\;\mathcal C_{b(r)}\;}
\mathcal G_{\rm eff}(r)
}
$$

с

$$
\ell_{\rm obs}(r)=\sqrt{\ell_P^2+(\theta r)^2},
\qquad
b(r)=2^{\lfloor\log_2(\ell_{\rm obs}/\ell_P)\rfloor}.
$$

Расстояние само по себе не изменяет microscopic spacetime. При фиксированном
угловом/каузальном разрешении более далёкий объект соответствует большему
physical coarse-graining block, поэтому отдельные планковские binary degrees of
freedom становятся operationally unresolved.

## 2. Frozen binary-route rule family

Локальное правило $R_q$ не содержит координатной размерности:

1. causal link заменяется всеми $2^q$ двухшаговыми маршрутами;
2. каждый маршрут помечен $q$ binary bits;
3. два route states соединяются intra-cell frame link тогда и только тогда,
   когда их labels имеют Hamming distance one;
4. рекурсивно переписываются только causal child links.

Линейный масштаб при одном rewrite удваивается:

$$
\lambda_\ell=2.
$$

Число causal child links умножается на

$$
\lambda_V=2\,2^q=2^{q+1}.
$$

Следовательно асимптотическая volume dimension этого rule family равна

$$
\boxed{
d_H
=
\frac{\log\lambda_V}{\log\lambda_\ell}
=
q+1.
}
$$

Это следствие rule combinatorics, а не подстановка $D=3$.

## 3. Независимый topology selector

Route labels образуют Hamming graph $Q_q$. Два causal endpoints дают suspension
этого графа как local route shell.

Для связного hypercube graph

$$
V(Q_q)=2^q,
\qquad
E(Q_q)=q2^{q-1},
$$

поэтому при $q\ge2$

$$
\beta_1(Q_q)
=E-V+1
=2^{q-1}(q-2)+1.
$$

Suspension сдвигает reduced homology на одну степень, следовательно

$$
\boxed{
\beta_2(\Sigma Q_q)
=2^{q-1}(q-2)+1.
}
$$

Для трёх заранее объявленных binary candidates:

$$
q=1:\quad \beta=(1,0,0),
$$

$$
\boxed{q=2:\quad \beta=(1,0,1)},
$$

$$
q=3:\quad \beta=(1,0,5).
$$

Таким образом $q=2$ одновременно даёт

$$
\boxed{d_H=3}
$$

и single homology-$S^2$ route shell, допускающую natural local 3-cell
completion. Topology shell не использовалась в numerical rule-selection score.

Это **локальный manifold precursor**. Он ещё не доказывает, что все links
рекурсивно склеенного global complex имеют topology $S^2$.

## 4. Frozen train -> held-out result

Train generations $g=2,3,4$ использовали только proximity к
$D_{slice}=3$ и $z=1$ и выбрали

$$
\boxed{q_*=2}
$$

до просмотра generation $g=5$.

Held-out transition $4\to5$ дал

$$
\boxed{d_H=2.999229782},
\qquad
\boxed{z=0.998281156}.
$$

Из independent volume/gap scaling:

$$
\boxed{d_s^{slice}=\frac{d_H}{z}=3.004393867},
$$

а при одной ordinary causal-time direction

$$
\boxed{d_s^{history}\approx4.004393867}.
$$

## 5. Почему появляется закон гладкости $b^{-2}$

Для frozen $q=2$ spatial rule один dyadic spatial coarse step содержит
асимптотически

$$
N_{space}(b)\sim b^{d_H}\approx b^3
$$

microscopic events. Один causal-time window при $z\simeq1$ даёт ещё factor
$b$, поэтому observer spacetime block содержит

$$
N_{obs}(b)\sim b^{d_H+z}\approx b^4.
$$

Для unbiased weakly correlated binary fluctuations central-limit scaling даёт

$$
\delta g_{\rm rms}
\sim N_{obs}^{-1/2}
\sim b^{-(d_H+z)/2}
\approx b^{-2}.
$$

Каждая physical derivative добавляет inverse coarse length:

$$
\boxed{
\delta g\sim b^{-2},
\qquad
\nabla\delta g\sim b^{-3},
\qquad
\delta R\sim b^{-4}.
}
$$

В unified Python run измерено

$$
\delta g\sim b^{-2.001707},
$$

$$
\nabla\delta g\sim b^{-3.001458},
$$

$$
\delta R\sim b^{-4.000524}.
$$

То есть прежний smoothing law больше не требует заранее заданного 4D torus: он
следует из discovered spatial scaling плюс одной causal-time direction.

## 6. Two-form metric sector

Те же observer-cell multiplicities, применённые к binary perturbations simple
self-dual $B^i$, дают

$$
\boxed{
\Delta_{simp}\sim b^{-1.994838},
\qquad
\Delta_{g_U}\sim b^{-2.019746}.
}
$$

Это self-averaging вокруг simple metric sector. Оно не является dynamical proof
того, что произвольная microscopic state сама войдёт в Plebański simplicity
surface.

## 7. Diffeomorphism kinematics

У frozen rule ровно два route bits. В refined description они дают две local
transverse rerouting coordinates. Независимый path-vector calculation даёт

$$
\boxed{
[D_\beta,D_\gamma]
\to
D_{[\beta,\gamma]},
\qquad
\Delta_{Lie}\sim L^{-1.981810}.
}
$$

Это nontrivial continuum diffeomorphism kinematics, но ещё не полный
Hamiltonian-constraint algebra.

## 8. Почему две graviton polarizations пока conditional

Если held-out $D_{slice}\simeq3$ и full constraints действительно становятся
first class, HDA выбирает

$$
c_{DW}=\frac1{D-1}=\frac12,
$$

а Dirac counting даёт

$$
\boxed{N_{grav}=2}
$$

local metric configuration degrees of freedom.

Но это следствие **условия first-class HDA**, а не доказательство того, что
microscopic Hamiltonian уже его выполняет.

## 9. Настоящий оставшийся killer gate

Теперь переход больше не формулируется как `4D discrete -> 4D smooth`.
Проверяемая цепь стала

$$
\boxed{
\text{binary route bits}
\to q_*=2
\to S^2\text{ local shell}
\to d_s^{slice}\approx3
\to z\approx1
\to \mathcal C_{b(r)}
\to \text{smooth IR candidate}.
}
$$

Остаются две обязательные стрелки:

1. global recursive complex должен сам пройти 3-manifold vertex-link gate;
2. на том же graph-changing Hilbert space необходимо получить

$$
\boxed{
[\hat H[N],\hat H[M]]
\longrightarrow
i\hbar\hat D[\sharp(NdM-MdN)]
}
$$

в regulator-safe collective limit.

Только после этого finite `bit -> spacetime candidate` можно повышать до claims
о microscopic quantum general relativity.
