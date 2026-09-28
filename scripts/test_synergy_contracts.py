from synergy_contracts import CONTRACT_ID, quantum_reference_payload

def test_quantum_reference_is_standard_control_only():
    p=quantum_reference_payload(benchmark_id="chsh-ref",trials=4)
    assert CONTRACT_ID=="synergy.science.quantum-reference-control/v1"
    assert p["passed"] is True
    assert p["experimental_result"] is False
    assert p["novel_physics_claim"] is False
