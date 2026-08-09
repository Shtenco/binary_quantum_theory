# Статус теории — актуальный frontier

## Что уже действительно получено

1. Точное дискретное спектральное ядро: $B$, $L=B^\dagger B\ge0$, синусовый символ и massless lattice pole.
2. Симплектическая свободная динамика и два TT-компонента в линейном reduced/Regge sector.
3. Off-shell local-frame invariance конечного SU(2) plaquette; PR17 расширил проверку до двух склеенных plaquettes с общей connection/frames.
4. Finite geometric-cell gate проверяет closure, diagonal simplicity, cross-simplicity и nondegeneracy. После аудита добавлены два adversarial controls: exact closure + individually simple faces с нарушенной cross-simplicity и exact closure + nonsimple bivector с нарушенной diagonal simplicity. Положительный tetrahedron всё ещё edge-generated, поэтому это algebraic/reconstruction gate, не доказательство dynamical simplicity emergence.
5. Dimension-blind control убивает минимальный binary reconvergent diamond как механизм 4D: он стремится к approximately two-dimensional geometry.
6. Conditional qubit-isotropy chain выделяет spatial $D=3$: только для qubit полная adjoint frame freedom $PSU(2)$ совпадает с полным rotation group $SO(3)$; для $q>2$ adjoint $PSU(q)$ не покрывает $SO(q^2-1)$.
7. Four spin-$1/2$ face carriers имеют двухмерный SU(2) singlet/intertwiner sector; logical Pauli operators являются exact tetrahedral shape/oriented-volume observables.
8. Absolute-volume theorem: любой two-dimensional four-valent intertwiner sector имеет $V\propto I$; $j=1$ — первый equal-spin sector, где volume различает zero/nonzero geometry; несколько различных ненулевых volume scales требуют intertwiner dimension $\ge4$.
9. Finite Peter--Weyl link
   $$\mathcal H_{link}^{J_{max}}=\bigoplus_{j\le J_{max}}V_j^L\otimes V_j^R$$
   сохраняет exact left/right SU(2) covariance. Holonomy word с $r$ hits на одном link cutoff-exact при $j_{in}+r/2\le J_{max}$; vacuum Wilson staircase проверяет это через $J_{max}=5/2$.
10. На $K_5$ vector-link truncation $5^{10}$ сжимается Gauss law до 140 states; fully-active five-tetrahedron sector имеет dimension 32. Четыре loop moves — минимальная distance от empty geometry до fully-active $K_5$.
11. Exact five-tetrahedron $j=1/2$ vertex tensor и link-level geometrogenesis почти совпадают: $P_{full}W^4|0\rangle$ имеет fidelity squared $90/91$ к independently contracted vertex. Pure Wilson/scalar volume не закрывают missing $1/91$, tensorial shape — закрывает.
12. Старые orientation-covariant finite normal constraints имеют robust BF-like physical-state kernel: на 32D sector constraints трёх nodes дают rank 31 и unique null state $V_5$.
13. Но старый $J_{max}=1/2$ model не проходит quantum HDA. После правильных geometric orientation signs все 10 HH pairs permutation-covariant, но graph-changing norm fraction squared равен
   $$\boxed{37/69}.$$
   Graph-preserving $Q_{ij}=-iP[H_i,H_j]P$ span содержит projected $SO(5)$-like skeleton, однако higher-body Lie anomaly остаётся огромной.
14. Tangential/normal finite Dirac hierarchy старого model: common kernel всех десяти $Q_{ij}$ двумерен,
   $$\operatorname{span}\{V_5,Y^{\otimes5}V_5\},$$
   а normal constraints выбирают только $V_5$. Это finite BF-like result, не HDA proof.
15. Для regulator-safe Euclidean HH из all-$j=1/2$ $K_5$ per-link wall требует $J_{max}=5/2$. Reachable Gauss basis имеет только 4193 admissible spin assignments / 24364 spin-network states. Среди них лишь 163 distinct local spin quartets, intertwiner multiplicity $\le3$.
16. **Первый настоящий regulator-safe $J_{max}=5/2$ HH-column теперь вычислен с genuine volume**
   $$V=\sqrt{|J_1\cdot(J_2\times J_3)|}.$$
   Для all-$j=1/2$, all-$K=0$ input:
   $$\boxed{\|[H_0,H_1]\psi\|=1.681559985798016},$$
   а fraction norm-squared вне исходного 32D all-$j=1/2$ sector равна
   $$\boxed{0.7020983368626005}.$$
   При этом реально достигнут только $j_{max}=3/2<5/2$: representation wall этот результат не объясняет. Поэтому повышение cutoff само по себе **не восстанавливает HDA**.
17. Тот же safe genuine-volume Hamiltonian не сохраняет старый BF vertex:
   $$\boxed{\|H_0^{safe}V_5\|=1.4002194669856702},$$
   а component результата в исходном 32D sector равна нулю. Следовательно старое $H_vV_5=0$ не универсально и не должно использоваться как tuning target будущей Lorentzian theory.
18. Plebański/Urbantke route проверен отдельно: simple nondegenerate $B^i$ reconstructs metric; compatible connection from $D_AB=0$ и anti-self-dual curvature block отличают Einstein $S^4$ от smooth non-Einstein control.
19. Covariant EPRL simplicity projector
   $$P_{simp}=F(F^\dagger F)^{-1}F^\dagger$$
   normalization-independent. EPRL coherent geometric rays сохраняются, а preregistered single-power extrapolation raw-vs-isometrized ambiguity на $j=15/2$ честно FAIL. Это **отдельная covariant BF/spinfoam ветвь**, а не preprocessing operator внутри real-SU(2) canonical Hamiltonian.
20. Fixed 4D Regge scaffold independently approaches Fierz--Pauli / Einstein--Hilbert / cubic Ward. A law frozen on $L=5..8$ predicted four defects at held-out $L=9,10$: **8/8 preregistered checks passed**, all relative defect errors below 0.5%.
21. Flux-to-metric pullback of the DeWitt supermetric has inertia
   $$\boxed{(5+,1-,3\,0)}$$
   on 100/100 random nondegenerate tetrahedra; the three zeros are Gauss/frame rotations and the unique negative mode is common radial flux scaling.
22. Independent classical HDA controls pass in two formulations: spectral ADM grid and finite 4-simplex deformation algebra, both to approximately $10^{-10}$ in safe windows.
23. Within the local two-derivative ADM ansatz, generic HH closure fixes
   $$\boxed{c_{DW}=1/2,\qquad AB=1}$$
   while leaving Newton scale and $\Lambda$ free. The same closure gives the leading tensor cone $c_T^2=AB=1$ and, with first-class Dirac counting in $D=3$, two physical configuration modes.
24. Real Ashtekar--Barbero classical kinetic sector obeys exact cancellation
   $$H_E^{kin}+H_L^{corr}=H_{DW}$$
   for any real $\beta$; the finite canonical quantum theory must reproduce this after appropriate Gauss/diffeomorphism projection.
25. For the stated nested-commutator Lorentzian regularization, conservative exact per-link support counting gives
   $$r_e(H_E)=2,\qquad r_e(H_L)=6,\qquad r_e(HH)=12.$$
   Therefore all-$j=1/2$ **full Lorentzian HH** is guaranteed Peter--Weyl-safe at
   $$\boxed{J_{max}=13/2}.$$
   This is sufficient, not necessarily minimal: the actual dynamically reached spin must be measured, exactly as it was for the Euclidean safe calculation.

## Что означают новые PR16/17

Последние PR добавили полезные tier-1 finite precursors: glued frame/connection covariance и geometric-cell invariant checks. Они усиливают local kinematics, но не закрывают continuum/HDA gates. PR17 временно перезаписал status и machine ledger старой укороченной версией; актуальный ledger восстановлен без отката новых W1/SIMP1 tests. Сам SIMP1 после аудита усилен closure-preserving adversarial controls, чтобы closure, diagonal simplicity и cross-simplicity проверялись независимо.

## Две ветви теперь разделены строго

### Canonical route

$$
\boxed{
\text{Peter--Weyl }SU(2)
\to H_E+H_L^{(\beta)}
\to \Delta_\beta
\to \Delta_{HH}^{Q}
\to \text{DeWitt/HDA IR}
}
$$

Это текущий главный frontier. EPRL simplicity сюда механически не вставляется.

### Covariant route

$$
\boxed{
BF/Spin(4)\text{ or Lorentzian bivectors}
\xrightarrow{\;simplicity\;}
\text{EPRL/FK-like gravity amplitudes}
}
$$

Она остаётся независимым cross-check того же semiclassical GR limit.

## Главный незакрытый переход

Euclidean safe-cutoff hypothesis уже не является главным вопросом: один safe column её отверг. Центральный killer-gate теперь

$$
\boxed{
\text{full real-}SU(2)\text{ Lorentzian Peter--Weyl Hamiltonian}
\longrightarrow
[H_k,H_l]\simeq i\,D_{kl}/(3V)
}
$$

в simultaneous spin-safe and momentum-safe window, без coefficient tuning.

Правильная реализация должна использовать cached Gauss/recoupling blocks, а не magnetic brute force. Для Euclidean HH уже доказано, что gauge-reduced problem имеет размер всего 24364 states; для Lorentzian nested operator сначала следует построить reachable-spin enumeration и определить actual wall относительно conservative $J_{max}=13/2$.

## Joint canonical pass condition

Теория продвигается к GR только если в одном scaling window одновременно

$$
\boxed{
\Delta_{HH}^{Q}\to0,
\qquad
\Delta_\beta\to0,
\qquad
\operatorname{inertia}K_E\to(5+,1-,3\,0),
\qquad
z\to1.
}
$$

После first-class closure microscopic system должен дать семь constraints $(3G+3D+1H)$ и поэтому ровно две physical configuration degrees of freedom без manual TT projection.

Открыты также frozen microscopic measure/rules, dynamical emergence of one common continuum window, matter/chirality/anomalies, physical scale setting and independent empirical replication.
