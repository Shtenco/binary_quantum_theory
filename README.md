# Information-Graph / CIMFIG Gravity Programme

**Актуальный статус:** 2026-08-13  
**Класс результата:** вычислимая кандидатная архитектура; фундаментальная физическая теория **не заявлена**.

> Главный принцип репозитория: конечное тождество, regression test и continuum/physics claim — разные уровни доказательности. Ни один численный PASS внутри выбранной модели не считается экспериментальным подтверждением природы.

## Текущий frontier

Наиболее сильная canonical ветвь сейчас формулируется как

$$
\boxed{
\text{Peter--Weyl }SU(2)
\longrightarrow H_E+H_L^{(\beta)}
\longrightarrow \text{graph-changing off-shell domain}
\longrightarrow \text{HDA/DeWitt continuum}
}
$$

Правый член hypersurface-deformation algebra больше не подбирается после расчёта. Он собирается независимо:

$$
N,M
\xrightarrow{\ d\ }
\omega=N\,dM-M\,dN
\xrightarrow{\ \sharp_{E,q}\ }
\beta
\xrightarrow{\ \text{path rerouting}\ }
D_{\rm path}[\beta].
$$

Центральный открытый тест:

$$
\boxed{
[\hat H[N],\hat H[M]]
\stackrel{?}{\longrightarrow}
i\hbar\,\hat D_{\rm path}
\!\left[\sharp_{E,q}(N\,dM-M\,dN)\right]
}
$$

на **nontrivial off-shell domain**, одновременно с

$$
\Delta_\beta\to0,
\qquad
\operatorname{inertia}K_E\to(5+,1-,3\,0),
\qquad
z\to1,
$$

и first-class rank должен идти к $3G+3D+1H$, а не к топологическому BF-flatness rank.

Полный подробный ledger: **[`THEORY_STATUS.md`](THEORY_STATUS.md)**  
Machine-readable gates: **[`theory_gates.json`](theory_gates.json)**

## Что уже воспроизводимо

- exact periodic sine/Laplacian identities для $L=B^\dagger B$;
- finite SU(2) frame/connection Ward checks и algebraic geometric-cell controls;
- finite Peter--Weyl links с exact left/right gauge covariance и cutoff-wall theorem;
- $K_5$ five-tetrahedron/Gauss laboratories и отдельный BF/15j negative control;
- regulator-safe $J_{\max}=5/2$ genuine-volume HH support diagnostic;
- generic dual-cell Hodge/RT0 `sharp` reconstruction from flux geometry;
- refined path-register Lie algebra с quadratic continuum convergence;
- DeWitt flux pullback inertia $(5+,1-,3\,0)$;
- independent classical ADM/simplex HDA controls;
- fixed-4D Regge $\to$ Fierz--Pauli / Einstein--Hilbert / cubic Ward scaling;
- preregistered Regge continuation $L=9,10$: **8/8 held-out checks PASS**, все relative defect errors < 0.5%;
- отдельная covariant EPRL/simplicity ветвь с честно сохранённым blind extrapolation FAIL.

Это сильные **finite/conditional** результаты. Они не заменяют вывод одной Lorentzian microscopic theory, общего RG-окна и экспериментальную проверку.

## Что принципиально не считается доказательством GR

1. Две TT-моды после ручной TT-проекции.
2. `EEF`-подобный оператор сам по себе.
3. 15j/BF kernel или flatness constraints.
4. Нулевой commutator только после group averaging.
5. Выход Hamiltonian из fixed $K_5$ sector: graph/spin change разрешён canonical LQG dynamics.
6. Совпадение заранее известных констант или post-hoc fitting.

BF/GR discriminator зафиксирован отдельно в [`BF_GR_DIRAC_COUNT_DISCRIMINATOR.md`](BF_GR_DIRAC_COUNT_DISCRIMINATOR.md).

## Две gravity-ветви не смешиваются

### Canonical real-$SU(2)$

Peter--Weyl holonomy/flux variables, Euclidean + Lorentzian Hamiltonian, graph-changing/off-shell HDA, Immirzi cancellation, DeWitt signature.

Ключевые файлы:

- [`CANONICAL_MICRO_ARCHITECTURE_V1.md`](CANONICAL_MICRO_ARCHITECTURE_V1.md)
- [`FLUX_DRIVEN_PATH_HDA_TARGET.md`](FLUX_DRIVEN_PATH_HDA_TARGET.md)
- [`OFF_SHELL_HDA_HABITAT_TARGET.md`](OFF_SHELL_HDA_HABITAT_TARGET.md)
- [`DENSITIZED_QUANTUM_HDA_TARGET.md`](DENSITIZED_QUANTUM_HDA_TARGET.md)
- [`LORENTZIAN_BETA_CANCELLATION.md`](LORENTZIAN_BETA_CANCELLATION.md)
- [`LORENTZIAN_HH_REACHABLE_SPACE.md`](LORENTZIAN_HH_REACHABLE_SPACE.md)

### Covariant BF / spin foam

Simplicity constraints select a gravity sector from BF/Spin(4) data. Эта ветвь служит independent semiclassical cross-check и **не вставляется механически** как preprocessing в real-$SU(2)$ canonical Hamiltonian.

Ключевые файлы:

- [`SIMPLICITY_PROJECTOR_THEOREM.md`](SIMPLICITY_PROJECTOR_THEOREM.md)
- [`EPRL_COHERENT_FUSION_SCALING.md`](EPRL_COHERENT_FUSION_SCALING.md)
- [`K5_DUAL_BF_CONTROL.md`](K5_DUAL_BF_CONTROL.md)

## Быстрый regression run

```bash
python -m pip install -r requirements.txt
python scripts/verify_theory_gates.py
python scripts/validate_github_latex.py
python scripts/verify_sine_bridge.py
python scripts/verify_connection_ward.py
python scripts/verify_geometric_cell.py
python scripts/dual_k5_lapse_cochain_gate.py
python scripts/dual_cell_sharp_rt0_gate.py
python scripts/path_rerouting_diffeo_gate.py
python scripts/path_diffeo_lie_gate.py
python scripts/path_vector_diffeo_gate.py
python scripts/lorentzian_hit_depth_bound.py
```

GitHub Actions запускает этот core regression автоматически на `push` в `main` и на pull request.

## Правило изменения теории

Любой PR, который меняет физический claim, обязан одновременно:

1. обновить `THEORY_STATUS.md`;
2. обновить соответствующий gate в `theory_gates.json`;
3. добавить/обновить воспроизводимый evidence-файл;
4. сохранить отрицательные и blind FAIL результаты;
5. не повышать `tested_finite`/`conditional` до `proved` без нового доказательства;
6. быть основанным на актуальном `main`, чтобы старые Codex-ветки не откатывали frontier.

См. [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Навигация

- **Текущий статус:** [`THEORY_STATUS.md`](THEORY_STATUS.md)
- **Machine ledger:** [`theory_gates.json`](theory_gates.json)
- **Кандидатная теория:** [`CIMFIG_V18_CANDIDATE_THEORY.md`](CIMFIG_V18_CANDIDATE_THEORY.md)
- **Canonical architecture:** [`CANONICAL_MICRO_ARCHITECTURE_V1.md`](CANONICAL_MICRO_ARCHITECTURE_V1.md)
- **Regge bridge:** [`GRAVITY_BRIDGE_SCALING.md`](GRAVITY_BRIDGE_SCALING.md), [`REGGE_EH_CUBIC_BRIDGE.md`](REGGE_EH_CUBIC_BRIDGE.md), [`CUBIC_WARD_SCALING.md`](CUBIC_WARD_SCALING.md)
- **Held-out predictions:** [`HELDOUT_L9_L10_PREREGISTRATION.md`](HELDOUT_L9_L10_PREREGISTRATION.md), [`HELDOUT_L9_L10_RESULTS.md`](HELDOUT_L9_L10_RESULTS.md)
- **Old long-form README snapshot:** [`docs/LEGACY_README_2026-07-28.md`](docs/LEGACY_README_2026-07-28.md)

## Remaining scientific gates

Главные незакрытые задачи:

- один frozen microscopic Lorentzian rule/measure без post-hoc tuning;
- full off-shell quantum HDA на общем graph-changing domain;
- simultaneous RG window: dimension/topology, large spin, Lorentzian DeWitt, $z=1$, GR constraint rank;
- matter/chirality/anomaly cancellation;
- physical scale setting;
- новые preregistered predictions и независимая экспериментальная replication.

До закрытия этих gates правильная формулировка результата остаётся:

$$
\boxed{\text{сильная вычислимая программа квантовой геометрии, а не подтверждённая теория природы}.}
$$
