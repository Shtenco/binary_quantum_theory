# Условная цепочка refinement → physical space → connected history → Einstein IR

Это математическая достаточная теорема и диагностические модели, не утверждение о выполнении её предпосылок BQG. Исходные gates не переводятся в proved. Источник проекта a55c77b.

## I. Уточнения и физический предел: достаточная теорема

Пусть Phi — общее линейное тестовое пространство с фиксированной нормой; I_n:Phi→H_n — совместимые изометрические вложения, например I_(n+1)=J_n I_n. На H_n задано ПОЛНОЕ семейство C_(i,n) на общих нужных доменах. Замкнутая положительная master-форма M_n удовлетворяет q_(M_n)[u]≥κ Σ_i ||C_(i,n)u||² с κ>0 независимо от n. Зафиксировать окно E_n=1_(0,δ_n](M_n), δ_n→0, и a_n>0. Если нуль имеет атом, выбор окна с атомом либо без атома должен обосновываться отдельно; здесь атом исключён.

Обозначим η_n(ψ,φ)=<E_n I_nψ,E_n I_nφ>/a_n. Предположить:
(a) для любых ψ,φ последовательность η_n сходится и диагонали ограничены;
(b) есть Ω с η_n(Ω,Ω)=1 для всех n;
(c) на Phi определены C_i с C_i Phi⊂Phi и
r_(i,n)(ψ)=||E_n I_n C_iψ−C_(i,n)E_n I_nψ||/sqrt(a_n)→0.

Тогда η=lim η_n положительна и ненулевая. Прямой расчёт даёт
|η_n(C_iψ,φ)|≤sqrt(δ_n/κ) sqrt(η_n(ψ,ψ)η_n(φ,φ)) + r_(i,n)(ψ)sqrt(η_n(φ,φ))→0.
Следовательно, C_i Phi входит в null η. Completion(Phi/null η) — ненулевое физическое Hilbert space, все исходные C_i действуют нулём на спущенном тестовом пространстве. Неравенство использует только form bound и указанные домены: самосопряжённость master следует из замкнутой формы, свойства каждого constraint задаются отдельно.

Удобное достаточное условие для(a):
|η_(n+1)(ψ,φ)−η_n(ψ,φ)|≤ε_n ||ψ||||φ||, Σ_n ε_n<∞.
Телескопическая оценка хвоста доказывает Cauchy. Например ε_n=2^-n даёт tail с n8 равный1/128. Предел единствен для этой последовательности, но независимость от ДРУГОЙ схемы уточнений/пути δ_n требует отдельных cofinal comparisons.

Это слабее требования точного переноса каждого H, но сильнее ненормированной малости ошибки. Даже если абсолютный defect→0, его деление на sqrt(a_n) может расходиться. Не следует выводить близость резких проекторов из одного малого intertwining defect без spectral separation/resolvent estimates. Все эти оценки должны учитывать full leakage, все nodes и Lorentzian terms.

## II. Почему доказательства I недостаточно

Точная модель: H=L²(0,1), C=sqrt(x), M=x, Eδ=1_(0,δ], aδ=δ, Phi=span{x^(k/2): k≥0}. C сохраняет Phi, коммутатор нулевой, I_n identity. Для непрерывных тестовых функций η(f,g)=conj(f(0))g(0). Физическое пространство одномерно и ненулевое, η(Cf,g)=0. Если задать spatial q_ab=δ_ab I, det q=1, все connected metric fluctuations равны нулю. Никакого TT propagator нет.

Таким образом, даже ненулевая нормированная rigging форма и невырожденная spatial metric не доказывают spacetime, evolution, connected histories или spin2. Модель не имеет BQG полных ограничений и не является её контрпримером; она опровергает общий логический переход, лишённый дополнительных предпосылок.

## III. Мост к connected истории — отдельные условия

Нужны физические metric observables с определённой spacetime localization/clock или корректной boundary interpretation, и один derived history functional Z[J], поддержанный конструкцией I. Его source insertions должны быть совместимы с quotient и refinement. В Lorentzian formalism W[J]=−iℏ log Z[J] удаляет disconnected pieces, а δ²W/δJδJ даёт connected response с соответствующими conventional factors. Log identity сама не доказывает существования history measure. Нельзя из projector автоматически получить physical time.

При подходящей invertibility после gauge fixing Legendre transform W даёт Γ[g]. Нужно независимо установить anomaly-free diffeomorphism Ward identity, правильные contact/ghost contributions, continuum convergence и физическую TT spectral positivity. Для flat phase TT response должен иметь два helicities, positive residue Z>0 и massless pole, не подменённый parameter resolvent. Для curved vacuum flat momentum pole formulation неприменима без local/WKB prescription. В асимптотически плоском вакууме renormalized Λ=0.

## IV. Условная Einstein IR теорема

Предположить результат I и III, а дополнительно: в четырёх измерениях существует regular Lorentzian nondegenerate metric phase; pure gravitational leading action является локальным diffeomorphism-invariant функционалом только g; through two derivatives применима derivative expansion; нет дополнительных light gravitational fields или несупрессированных nonlocal terms этого порядка; physical TT kinetic coefficient nonzero positive. Высшие производные/quantum nonlocalities допускаются в контролируемом remainder, их малость должна быть доказана на заявленном диапазоне физических масштабов.

Тогда локальные scalars из одной metric через две derivatives — constant и R modulo boundary. В normal coordinates first derivatives g исчезают в точке, second derivatives входят в curvature; единственное линейное scalar contraction Riemann — R. Diffeomorphism invariance запрещает самостоятельную polynomial metric potential и preferred-frame kinetic coefficients. Поэтому
Γ_leading = B ∫d⁴x sqrt(−g)(R−2Λ), B>0,
где положительность B соответствует positive TT kinetic residue в conventional signature(−+++). Определение B=1/(16πG_eff) в units c=ℏ=1 калибрует G_eff, не предсказывает его численное значение. Полный Γ содержит remainder и matter functional, если он отдельно выведен.

Вариация с корректным boundary term:
δΓ_leading=B ∫sqrt(−g)(G_ab+Λg_ab) δg^ab.
С T_ab=−2/sqrt(−g) δS_m/δg^ab получаем
G_ab+Λg_ab=8πG_eff T_ab + Δ_ab,
Δ_ab=−(1/(B sqrt(−g)))δΓ_remainder/δg^ab.
В physical units matter coefficient8πG_eff/c⁴. Для leading truncation Δ=0: это уравнения Эйнштейна. Для полной теории утверждается controlled IR approximation, а не exact Einstein equation at every scale. Предпосылка suppression remainder должна дать численный bound; её нельзя заменить словом IR.

Ward/Bianchi обеспечивает covariant conservation on matter equations. Символьная проверка линейного Einstein symbol на pure gauge h_ab=k_a ξ_b+k_b ξ_a даёт ровно0. Это consistency identity известного endpoint, не вывод микроскопического Ward.

## V. Роль soft spin2 аргумента

Factorization ведущего soft pole и decoupling longitudinal polarization дают Σ_i η_i g_i p_i=0. В общих взаимодействующих каналах это требует универсальной связи; выбранный точный generic2→2 контроль route5 имеет rank3 и kernel(1,1,1,1). Вырожденные каналы недостаточны, disconnected sectors не связываются автоматически. Этот аргумент поддерживает universal leading coupling, но не сам по себе локальность Γ, отсутствие extra fields или suppression higher derivatives. Нелинейный endpoint IV следует из явно перечисленных дополнительных условий.

## VI. Что закрыто и что не закрыто

Закрыты условно: достаточный refinement/spectral theorem I; Einstein leading-action classification и вариация IV; exact toy diagnostic II и gauge-symbol check; ранее exact generic soft-Ward algebra.
Не выведены для BQG: полный Lorentzian constraint family и общий domain, normalized refinement errors и ненулевой path-independent limit, физическое spacetime/history measure, connected Γ, interacting positive TT pole, microscopic Ward и local IR bounds. Вносить их как hypotheses допустимо для conditional theorem, но не как proved gates. Фундаментальные константы эти hypotheses не заменяют. Выбор EH в качестве целевой microscopic dynamics был бы новой completion/model, не доказательством исходной BQG.
