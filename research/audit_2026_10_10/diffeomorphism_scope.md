# Доступность правой части HDA

На срезе a55c77b найденные D живут на разных носителях:
- classical_hda_safe_window_gate.py:D_smear — классические канонические поля q,p на пространственной сетке;
- flux_habitat_diffeo_gate.py — производная по положениям вершин tetrahedron, D(k,l)f=−E_l·∂_(x_k)f;
- path_vector_diffeo_gate.py и path_normal_hda_gate.py — дополнительные path registers;
- k5_oriented_quantum_hda_gate.py — regulator-unsafe jmax1/2 finite diagnostic и fitting Pauli action span, не independently derived D на полном Peter–Weyl двухшаговом образе.

Текущий расчёт использует lapse vectors N=(1,0,0,0,0), M=(0,1,0,0,0). Формальная правая часть D[q^{ab}(N∂_bM−M∂_bN)] требует отдельно заданных spatial interpolation, metric observable/inverse, habitat and domain; Gauss reduction также требует определить возможный Gauss term согласно conventions. Эти элементы не задаются самим выбором двух узлов.

Поэтому нельзя объявить отсутствующую правую часть нулём или определить D=commutator: это сделало бы closure тождеством по определению. Настоящее сравнение открыто до общей microscopic D construction.
