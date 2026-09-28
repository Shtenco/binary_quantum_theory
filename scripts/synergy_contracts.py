from __future__ import annotations
from typing import Any

from bell_chsh_qubit_gate import run

CONTRACT_ID = "synergy.science.quantum-reference-control/v1"
AUTHORITY = "quantum_reference_research"


def quantum_reference_payload(*, benchmark_id: str, seed: int = 260830, trials: int = 16) -> dict[str, Any]:
    if not benchmark_id.strip() or trials <= 0:
        raise ValueError("benchmark_id and positive trials required")
    result = run(seed=seed, random_trials=trials, rotation_trials=max(4, trials // 2))
    if not result["passed"]:
        raise ValueError("standard quantum reference control failed")
    return {
        "benchmark_id": benchmark_id,
        "science_status": result["science_status"],
        "seed": seed,
        "random_trials": trials,
        "chsh_absolute_value": float(result["CHSH_absolute_value"]),
        "tsirelson_bound": float(result["Tsirelson_bound"]),
        "max_reference_error": max(
            float(result["Pauli_commutator_error"]),
            float(result["Pauli_anticommutator_error"]),
            float(result["singlet_correlation_tensor_error"]),
            float(result["Tsirelson_square_identity_error"]),
        ),
        "passed": True,
        "experimental_result": False,
        "novel_physics_claim": False,
    }
