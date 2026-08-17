#!/usr/bin/env python3
"""Fail CI when retired speculative sectors leak back into the GR/QM core.

The repository has one canonical programme: discrete quantum microstructure ->
quantum geometry -> coarse-grained smooth geometry -> GR/HDA continuum limit.
This audit keeps retired side-sector vocabulary and deleted Python modules out of
source, documentation, ledgers and workflows.
"""
from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
TEXT_SUFFIXES = {".py", ".md", ".yml", ".yaml", ".json"}

# Construct retired vocabulary without embedding the retired tokens literally in
# this audit source, so repository-wide textual searches remain meaningful.
RETIRED_TERMS = {
    "mir" + "ror",
    "anti" + "grav",
    "anti" + "matter",
    "info" + "ton",
    "gold" + "stone",
    "fifth" + " force",
}

RETIRED_MODULES = {
    "grav" + "iton_in" + "foton_foam_gate",
    "orientation_odd_hda_gate",
    "mir" + "ror_16cell_orientation_eta_gate",
    "mir" + "ror_chirality_gravity_gate",
    "mir" + "ror_force_normalization_gate",
    "mir" + "ror_goldstone_source_gate",
    "mir" + "ror_heisenberg_parent_gate",
    "mir" + "ror_hodge_stiffness_gate",
    "mir" + "ror_master_criterion_gate",
    "mir" + "ror_matter_matrix_element_gate",
    "mir" + "ror_order_16cell_gate",
    "mir" + "ror_order_recursive_pl_gate",
    "mir" + "ror_sigma_range_gate",
    "mir" + "ror_wilson_matter_gate",
}


def candidate_files():
    for path in ROOT.rglob("*"):
        if not path.is_file() or path == SELF or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if ".git" in path.parts or "verification_results" in path.parts:
            continue
        yield path


def scan_text(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace").lower()
    return sorted(term for term in RETIRED_TERMS if term in text)


def local_imports(path: Path):
    if path.suffix.lower() != ".py":
        return set()
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module.split(".")[0])
    return names


def main() -> int:
    failures = []
    scanned = 0
    python_files = 0

    for path in candidate_files():
        scanned += 1
        rel = path.relative_to(ROOT)
        hits = scan_text(path)
        if hits:
            failures.append(f"{rel}: retired vocabulary: {', '.join(hits)}")

        if path.suffix.lower() == ".py":
            python_files += 1
            imports = local_imports(path)
            stale = sorted(imports & RETIRED_MODULES)
            if stale:
                failures.append(f"{rel}: imports retired module(s): {', '.join(stale)}")

    if failures:
        print("CORE SCOPE AUDIT: FAIL")
        for item in failures:
            print(f" - {item}")
        return 1

    print(
        "CORE SCOPE AUDIT: PASS "
        f"({scanned} text/code files; {python_files} Python files; "
        "no retired vocabulary or retired-module imports)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
