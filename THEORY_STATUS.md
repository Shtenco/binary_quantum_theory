# Статус теории — актуальный frontier

## Что уже действительно получено

1. Точное дискретное спектральное ядро: $B$, $L=B^\dagger B\ge0$, синусовый символ и massless lattice pole.
2. Симплектическая свободная динамика и два TT-компонента в линейном reduced/Regge sector.
3. Off-shell local-frame invariance конечного SU(2) plaquette; PR17 расширил проверку до двух склеенных plaquettes с общей connection/frames.
4. Finite geometric-cell gate проверяет closure, diagonal simplicity, cross-simplicity и nondegeneracy. После аудита добавлены два closure-preserving adversarial controls, независимо ломающие cross и diagonal simplicity. Положительный tetrahedron edge-generated, поэтому это algebraic/reconstruction gate, не доказательство dynamical simplicity emergence.
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
13. После geometric orientation signs все 10 старых $J_{max}=1/2$ HH pairs permutation-covariant. Projection на fixed all-$j=1/2$ sector оставляет structured weight-3 $Q_{ij}$ и projected SO(5)-like skeleton. Но **fixed-sector leakage больше не называется HDA anomaly**: Thiemann/QSD Hamiltonian graph-changing, поэтому истинный HDA test должен проводиться на enlarged cylindrical/habitat space.
14. Tangential/normal finite hierarchy старого model: common kernel всех десяти projected $Q_{ij}$ двумерен,
   $$\operatorname{span}\{V_5,Y^{\otimes5}V_5\},$$
   а old normal constraints выбирают только $V_5$. Это finite BF-like result, не off-shell HDA proof.
15. Bonzom's 4-simplex construction даёт **точный литературный BF control на том же dual $K_5$ graph**:
   $$H^a_{bc}=E_{ab}\cdot E_{ac}-E_{ab}\cdot\operatorname{Ad}(g_{abc})E_{ac}.$$
   При малой кривизне $H^a_{bc}\sim(E_{ab}\times E_{ac})\cdot F$, то есть выглядит как $EEF$, но полный набор constraints enforces Ooguri/BF flatness и приводит к 15j recursions. Поэтому `EEF-looking + 15j kernel` не идентифицирует GR.
16. Для regulator-safe Euclidean HH из all-$j=1/2$ $K_5$ per-link wall требует $J_{max}=5/2$. Reachable Gauss basis имеет 4193 admissible spin assignments / 24364 spin-network states, 163 distinct local spin quartets, intertwiner multiplicity $\le3$.
17. Первый regulator-safe $J_{max}=5/2$ HH-column с genuine volume
   $$V=\sqrt{|J_1\cdot(J_2\times J_3)|}$$
   даёт
   $$\boxed{\|[H_0,H_1]\psi\|=1.681559985798016}.$$
   Его norm-squared split:
   $$\boxed{0.2979016631}$$
   остаётся в исходном all-$j=1/2$ sector,
   $$\boxed{0.2580651764}$$
   остаётся на том же ten-edge K5 с изменёнными nonzero spins,
   и только
   $$\boxed{0.4440331605}$$
   содержит хотя бы один $j=0$ link. То есть прежние 70.21% outside-32D были mixture spin dynamics + cylindrical graph change, а не HDA anomaly.
18. Те же 510 outputs содержат 305 distinct spin assignments, но всего
   $$\boxed{26}$$
   orbits после quotient по всем 120 automorphisms K5. Это label-removal control, не полный diffeomorphism quotient.
19. Safe genuine-volume Hamiltonian не сохраняет old BF vertex:
   $$\boxed{\|H_0^{safe}V_5\|=1.4002194669856702},$$
   а component результата в исходном 32D sector равна нулю. Поэтому old $V_5$ kernel не должен использоваться как tuning target canonical GR.
20. Graph-changing HDA target исправлен по QSD/QSD III и Lewandowski--Marolf: group-averaged/on-shell vanishing слишком слаб; требуется **nontrivial off-shell habitat/dual action** reproducing the diffeomorphism structure function rather than merely zero commutator.
21. Exact relational bridge для этого target:
   $$\boxed{E_l=3V\nabla\lambda_l},$$
   поэтому на tetrahedral vertex-smooth functional
   $$\boxed{D(k,l)f=-E_l\cdot\partial_{x_k}f}.$$
   100 random tetrahedra подтверждают face-area identity до $6.2\times10^{-16}$, flux closure до $1.2\times10^{-15}$ и finite-difference derivative до $2.6\times10^{-8}$.
22. Это позволяет использовать inverse-volume-free densitized quantum target
   $$\boxed{\frac32\{V,-i[H_k,H_l]\}\to\hbar(D_{lk}-D_{kl})}$$
   на nondegenerate off-shell habitat channels.
23. Для unit regular tetrahedron заранее preregistered five habitat channels pair $(1,2)$:
   $$(-1,\ 2\sqrt3/3,\ -\sqrt6/6,\ \sqrt3/3,\ 0),$$
   но их статус **reference-simplex benchmark**: Bonzom--Dittrich formula fixes one primal spatial tetrahedron, whereas generic node-local K5 Hamiltonians use dual tetrahedral nodes/local volumes. Generic primal-to-dual HDA mapping remains OPEN.
24. Plebański/Urbantke route проверен отдельно: simple nondegenerate $B^i$ reconstructs metric; compatible connection from $D_AB=0$ и anti-self-dual curvature block отличают Einstein $S^4$ от smooth non-Einstein control.
25. Covariant EPRL simplicity projector
   $$P_{simp}=F(F^\dagger F)^{-1}F^\dagger$$
   normalization-independent. Coherent geometric rays сохраняются; preregistered single-power extrapolation on $j=15/2$ honestly FAIL. Это отдельная covariant BF/spinfoam ветвь, не preprocessing внутри real-SU(2) canonical Hamiltonian.
26. Fixed 4D Regge scaffold independently approaches Fierz--Pauli / Einstein--Hilbert / cubic Ward. Law frozen on $L=5..8$ predicted four defects at held-out $L=9,10$: **8/8 preregistered checks passed**, all relative defect errors below 0.5%.
27. Flux-to-metric pullback DeWitt supermetric имеет inertia
   $$\boxed{(5+,1-,3\,0)}$$
   on 100/100 random nondegenerate tetrahedra; three zeros are Gauss/frame rotations, unique negative mode is common radial flux scaling.
28. Independent classical HDA controls pass in spectral ADM and finite 4-simplex formulations to approximately $10^{-10}$ in safe windows.
29. Within local two-derivative ADM ansatz, generic HH closure fixes
   $$\boxed{c_{DW}=1/2,\qquad AB=1}$$
   while leaving Newton scale and $\Lambda$ free. Then $c_T^2=AB=1$ and first-class Dirac counting in $D=3$ leaves two physical configuration modes.
30. BF-vs-GR Dirac discriminator: on the same 18D canonical phase space, SU(2) BF has $3$ Gauss + $6$ independent flatness directions and therefore zero local physical DOF; GR has $3G+3D+1H$ and therefore two configuration DOF. A closed constraint algebra with BF rank is a **topological FAIL**, even if it is anomaly-free and Regge/15j-like.
31. Real Ashtekar--Barbero classical kinetic sector obeys exact cancellation
   $$H_E^{kin}+H_L^{corr}=H_{DW}$$
   for any real $\beta$; finite canonical quantum theory must reproduce this after appropriate Gauss/diffeomorphism handling.
32. For the stated nested-commutator Lorentzian support:
   $$r_e(H_E)=2,\qquad r_e(H_L)=6,\qquad r_e(HH)=12.$$
   All-$j=1/2$ full Lorentzian HH is guaranteed transient-cutoff-safe at
   $$\boxed{J_{max}=13/2}.$$
33. Full Lorentzian support-only reachability is large but finite and highly local. After one $H_E+H_L$:
   $$\boxed{1843\ \text{Gauss spin assignments},\quad9750\ \text{spin-network states}}.$$
   After one HH pair:
   $$\boxed{615884\ \text{assignments},\quad11314085\ \text{spin-network states}},$$
   with maximum final spin $11/2$. The whole upper-bound support is assembled from only
   $$\boxed{2850}$$
   distinct local intertwiner blocks of size at most $7\times7$.

## Что означают новые PR16/17

PR16/17 added useful tier-1 local precursors: glued frame/connection covariance and geometric-cell invariant checks. They do not close continuum/HDA gates. PR17 temporarily overwrote the project status/ledger with an older reduced version; the current ledger was restored without reverting the new tests. SIMP1 was strengthened with closure-preserving adversarial controls.

## Две gravity-ветви разделены строго

### Canonical real-SU(2) route

$$
\boxed{
\text{Peter--Weyl }SU(2)
\to H_E+H_L^{(\beta)}
\to \text{graph-changing off-shell habitat}
\to \Delta_\beta,\ \Delta_{HH}^{off}
\to \text{DeWitt/HDA IR}
}
$$

EPRL simplicity сюда механически не вставляется.

### Covariant route

$$
\boxed{
BF/Spin(4)\text{ or Lorentzian bivectors}
\xrightarrow{\;simplicity\;}
\text{EPRL/FK-like gravity amplitudes}
}
$$

Она остаётся independent cross-check того же semiclassical GR limit.

## Главный незакрытый переход

Главный вопрос больше **не** `does HH stay inside fixed K5?`. Graph change is allowed.

Настоящий killer-gate:

$$
\boxed{
([H[N],H[M]]'-i\hbar D[\beta]')F_f
\longrightarrow0
}
$$

на preregistered nonconstant relational/vertex-smooth functionals, в simultaneous Peter--Weyl-safe and momentum-safe window. Group-averaged zero alone не считается PASS, потому что известен ultralocal/zero-commutator failure mode.

Для finite implementation preferred inverse-volume-free version:

$$
\boxed{
\frac32\{V,-i[H_k,H_l]\}F_f
\longrightarrow
\hbar(D_{lk}-D_{kl})F_f.
}
$$

Перед generic K5 claim необходимо отдельно вывести **dual-cell classical structure functions** matching node-local K5 Hamiltonians; current regular-tetrahedron preregistration is only a symmetric/reference-simplex benchmark.

## Joint canonical pass condition

В одном scaling window одновременно должны выполняться

$$
\boxed{
\Delta_{HH}^{off}\to0,
\qquad
\Delta_\beta\to0,
\qquad
\operatorname{inertia}K_E\to(5+,1-,3\,0),
\qquad
z\to1,
}
$$

и independent first-class rank должен идти к $3G+3D+1H$, а не к BF flatness rank.

Открыты также frozen microscopic measure/rules, dynamical emergence of one common continuum window, generic dual-K5 HDA mapping, matter/chirality/anomalies, physical scale setting and independent empirical replication.
