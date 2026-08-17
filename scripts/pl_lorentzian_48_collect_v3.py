#!/usr/bin/env python3
"""Final collector for exact V3 pairing-stabilizer-reduced Lorentzian terms."""
from __future__ import annotations

import argparse
import json
import traceback
from pathlib import Path

import pl_lorentzian_48_collect as BASE
import pl_lorentzian_48_collect_v2 as V2

VERSION = "tetrahedral-charged-volume-v2"
EXEC_DIRECT = "direct-corrected-v2"
EXEC_RECON = "pairing-stabilizer-reconstructed-v3"


def provenance_preflight(root: Path, cert_path: Path):
    cert = json.loads(cert_path.read_text(encoding="utf-8"))
    if not cert.get("passed"):
        raise RuntimeError("orbit reconstruction certificate did not pass")
    if not cert.get("checks", {}).get("all_six_heldout_pairs_pass"):
        raise RuntimeError("six held-out covariance pairs were not all validated")
    pairs = cert.get("validation_pairs", [])
    if len(pairs) != 6 or not all(x.get("passed") for x in pairs):
        raise RuntimeError("orbit validation pair ledger is incomplete")

    rows = []
    for p in root.rglob("term_*.json"):
        d = json.loads(p.read_text(encoding="utf-8"))
        rows.append((p, d))
    if len(rows) != 48:
        raise RuntimeError(f"need exactly 48 materialized terms, got {len(rows)}")

    if any(d.get("operator_version") != VERSION for _, d in rows):
        raise RuntimeError("non-V2 physical operator provenance found in V3 materialized orbit")

    direct = [(p, d) for p, d in rows if d.get("execution_version") == EXEC_DIRECT]
    recon = [(p, d) for p, d in rows if d.get("execution_version") == EXEC_RECON]
    other = [str(p) for p, d in rows if d.get("execution_version") not in (EXEC_DIRECT, EXEC_RECON)]
    if other:
        raise RuntimeError(f"unknown V3 execution provenance: {other[:8]}")
    if len(direct) != 12 or len(recon) != 36:
        raise RuntimeError(f"expected 12 direct + 36 reconstructed, got {len(direct)} + {len(recon)}")

    direct_ids = {(d["mode"], int(d["index"])) for _, d in direct}
    expected_direct = {
        *(('forward', i) for i in [0, 2, 6, 8, 12, 14]),
        *(('adjoint', i) for i in [0, 1, 14, 15, 20, 21]),
    }
    if direct_ids != expected_direct:
        raise RuntimeError(f"direct held-out ledger changed: {sorted(direct_ids)}")

    return cert, rows, len(direct), len(recon)


def run(root: Path, cert_path: Path):
    cert, rows, ndirect, nrecon = provenance_preflight(root, cert_path)

    # Reuse the complete 48-index V2 physical collector and all original hard thresholds.
    L, Ld, S, out = V2.run(root)

    extra_checks = {
        "orbit_certificate_passed": bool(cert.get("passed")),
        "six_direct_pair_validations_passed": len(cert.get("validation_pairs", [])) == 6
        and all(x.get("passed") for x in cert.get("validation_pairs", [])),
        "direct_count_12": ndirect == 12,
        "reconstructed_count_36": nrecon == 36,
        "complete_materialized_count_48": len(rows) == 48,
    }
    out["checks"].update(extra_checks)
    out["passed"] = bool(out.get("passed") and all(extra_checks.values()))
    out["science_status"] = "AMPLITUDE_PRECURSOR_S_NODE0_V3_ORBIT_EXACT"
    out["operator_version"] = VERSION
    out["execution_version"] = "v3-direct-heldout-plus-exact-H-reconstruction"
    out["direct_heavy_term_count"] = ndirect
    out["symmetry_reconstructed_term_count"] = nrecon
    out["heldout_covariance_pair_count"] = len(cert.get("validation_pairs", []))
    out["max_heldout_pair_relative_amplitude_error"] = cert.get(
        "max_pair_relative_amplitude_error"
    )
    out["pairing_stabilizer_orbits"] = cert.get("orbits")
    out["definition"] = (
        "S=-i(L_raw-L_raw^dagger)/2 over the complete 24 forward + 24 adjoint "
        "worker index orbit. Twelve corrected-V2 terms are evaluated directly; the "
        "remaining 36 are materialized by exact order-8 pairing-stabilizer Peter-Weyl "
        "unitary transport only after six preregistered direct held-out covariance pairs pass."
    )
    out["interpretation"] = (
        "Exact symmetry-reduced execution of the same tetrahedral-volume V2 physical operator; "
        "not a 48-direct-worker claim and not a model approximation."
    )
    out["v3_preregistration"] = "PL_16CELL_HERMITIAN_LORENTZIAN_PREREGISTRATION_V3_ORBIT.md"
    return L, Ld, S, out


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, required=True)
    p.add_argument("--orbit-certificate", type=Path, required=True)
    p.add_argument("--json-output", type=Path, required=True)
    p.add_argument("--state-output", type=Path, required=True)
    a = p.parse_args()
    try:
        L, Ld, S, out = run(a.root, a.orbit_certificate)
        code = 0 if out["passed"] else 1
    except Exception as exc:
        L = Ld = S = {}
        out = {
            "status": "V3 collector exception",
            "passed": False,
            "science_status": "INFRASTRUCTURE_DIAGNOSTIC",
            "operator_version": VERSION,
            "error_type": type(exc).__name__,
            "error": str(exc),
            "traceback": traceback.format_exc(),
        }
        code = 1
    a.json_output.parent.mkdir(parents=True, exist_ok=True)
    a.json_output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    BASE.save_bundle(a.state_output, L, Ld, S)
    print(json.dumps(out, indent=2, sort_keys=True))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
