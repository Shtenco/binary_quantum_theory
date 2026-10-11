# Настоящий двухшаговый Euclidean расчёт

Выполнены H0H1ψ и H1H0ψ для original source column0 (all-half spins и k2=0 на пяти узлах), canonical sine и zero-aware volume. Все37 промежуточных состояний каждого порядка сохранены. Doubled-spin cutoff7; максимальный финальный spin2=3. Оба порядка содержат1004 состояний, commutator514 выше pruning threshold1e−10. Норма commutator2.8794538147.

Проверены74 обратных матричных элемента, возвращающих в выбранное исходное состояние; symmetry error≤2.7756e−16. Это конечная проверка, не доказательство общего selfadjoint domain. Projection настоящего commutator на original32 code совпала с предыдущей antisymmetric cross-Gram column до5.87475e−16. Одна mixed-spin промежуточная ветвь независимо совпала с direct реализации с error0.

Original code projection norm0.5503455637; outside code norm2.8263711772. Доля squared norm вне code96.3469913%. Поэтому исходное сжатие отбрасывает основную измеренную динамику. Ненулевой коммутатор сам по себе не anomaly: правая часть HDA обычно ненулевая.

Сопоставление с D не выполнено: источники D в проекте имеют иной carrier/habitat, отсутствуют общий inverse metric, lapse interpolation и independently defined microscopic D на этих two-hit states. Файл diffeomorphism_scope.md описывает источники. Определять D самим измеренным commutator было бы circular.

Не проверены другие31 исходные колонны, остальные node pairs, full Lorentzian family и total numerical pruning/roundoff bounds. Scientific statuses не меняются.
