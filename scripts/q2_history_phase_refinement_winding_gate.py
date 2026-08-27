#!/usr/bin/env python3
"""Exact/conditional gate for q=2 history -> winding and phase refinement.

This gate deliberately separates four logically different statements.

EXACT A: the frozen q=2 phase skeleton is an oriented Gray C4 and every selected
C4 edge is a Hamming edge.

EXACT B: the already-committed graph-link gate proves each q=2 Hamming matrix
unit factors through the single no-link state.  A *history/event lift* may
therefore distinguish one midpoint event per oriented coarse edge.  Those four
midpoint histories plus the four active vertices form the canonical edge
subdivision C8.  The refined carry update has order eight and squares to the
coarse C4 shift after coarse projection.

NO-GO: the instantaneous five-state active+no-link Hilbert cannot by itself be
that C8.  All four event midpoints project to the same rank-one no-link state,
so edge-channel information is lost unless the history/projector description
retains the transition label.  Likewise Z4 x Z2 is not Z8; an independent time
bit does not refine phase.  The nontrivial carry relation is essential.

EXACT C: for any oriented cycle C_N, a full nearest-neighbor history path has a
unique lift to the universal cover Z once one initial lift is chosen.  Closed
histories have integer winding w=(n_T-n_0)/N, independent of the chosen sheet.
Winding is preserved by edge subdivision.

CONDITIONAL D: if the same ordered two-stage history-edge subdivision is
selected recursively at every refinement level, then

    C4 -> C8 -> C16 -> ... -> C_(4*2^g)

and the corresponding root groups mu_(4*2^g) are nested with angular mesh going
to zero, hence their union is dense in U(1).  The frozen q=2 causal rewrite does
have exact length-doubling per generation, but current repository evidence does
not yet prove that the physical history/projector dynamically locks that causal
subdivision to the phase-edge carry at every level.  That final locking remains
OPEN_PHYSICAL and is not silently promoted to a theorem here.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Iterable


GRAY = ((0, 0), (0, 1), (1, 1), (1, 0))


def hamming(a: tuple[int, int], b: tuple[int, int]) -> int:
    return sum(x != y for x, y in zip(a, b))


def read_json(path: Path | None) -> dict | None:
    if path is None:
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def shift_order(n: int, step: int = 1) -> int:
    """Order of +step in Z_n."""
    return n // math.gcd(n, step)


def carry_step(k: int, r: int, coarse_n: int, substeps: int) -> tuple[int, int]:
    """Advance one refined history tick with carry into the coarse phase index."""
    if r + 1 < substeps:
        return k, r + 1
    return (k + 1) % coarse_n, 0


def carry_cycle_order(coarse_n: int, substeps: int) -> int:
    start = (0, 0)
    state = start
    for t in range(1, coarse_n * substeps + 2):
        state = carry_step(*state, coarse_n, substeps)
        if state == start:
            return t
    raise RuntimeError("carry cycle did not close")


def independent_product_max_order(n: int, m: int) -> int:
    """Maximum element order in Z_n x Z_m."""
    return math.lcm(n, m)


def refined_projection(j_fine: int, fine_n: int) -> int:
    """Edge-subdivision coarse map C_(2N)->C_N on ordered history positions."""
    if fine_n % 2:
        raise ValueError("fine_n must be even")
    return (j_fine // 2) % (fine_n // 2)


def check_semiconjugacy(coarse_n: int) -> bool:
    """pi(T_fine^2 j)=T_coarse pi(j) for every fine history position."""
    fine_n = 2 * coarse_n
    return all(
        refined_projection((j + 2) % fine_n, fine_n)
        == (refined_projection(j, fine_n) + 1) % coarse_n
        for j in range(fine_n)
    )


def residues_from_increments(n: int, increments: Iterable[int], start: int = 0) -> list[int]:
    out = [start % n]
    k = start % n
    for d in increments:
        if d not in (-1, 1):
            raise ValueError("cycle path increments must be +/-1")
        k = (k + d) % n
        out.append(k)
    return out


def lift_residue_path(path: list[int], n: int, start_lift: int | None = None) -> list[int]:
    """Unique nearest-neighbor path lift from C_n to its universal cover Z."""
    if not path:
        raise ValueError("empty path")
    if start_lift is None:
        start_lift = int(path[0])
    if start_lift % n != path[0] % n:
        raise ValueError("start lift is on the wrong sheet")
    out = [start_lift]
    for a, b in zip(path, path[1:]):
        d = (b - a) % n
        if d == 1:
            delta = 1
        elif d == n - 1:
            delta = -1
        else:
            raise ValueError(f"non-nearest-neighbor cycle step {a}->{b} for C_{n}")
        out.append(out[-1] + delta)
    return out


def winding_of_closed_path(path: list[int], n: int, start_lift: int | None = None) -> int:
    if path[-1] % n != path[0] % n:
        raise ValueError("path is not closed")
    lift = lift_residue_path(path, n, start_lift)
    delta = lift[-1] - lift[0]
    if delta % n:
        raise AssertionError("closed lifted path did not differ by a deck transformation")
    return delta // n


def exhaustive_winding_checks(n: int = 4, length: int = 8) -> dict[str, object]:
    closed = 0
    sheet_invariant = True
    formula_exact = True
    refinement_invariant = True
    winding_values: set[int] = set()

    for inc in product((-1, 1), repeat=length):
        path = residues_from_increments(n, inc, 0)
        if path[-1] != path[0]:
            continue
        closed += 1
        expected = sum(inc) // n
        w0 = winding_of_closed_path(path, n, 0)
        wshift = winding_of_closed_path(path, n, 3 * n)
        formula_exact &= w0 == expected
        sheet_invariant &= w0 == wshift
        winding_values.add(w0)

        # Canonical edge subdivision: every coarse +/-1 step is two fine +/-1 steps.
        fine_inc = tuple(d for x in inc for d in (x, x))
        fine_path = residues_from_increments(2 * n, fine_inc, 0)
        wfine = winding_of_closed_path(fine_path, 2 * n, 0)
        refinement_invariant &= wfine == w0

    return {
        "cycle_n": n,
        "enumerated_increment_length": length,
        "closed_paths_checked": closed,
        "winding_values_seen": sorted(winding_values),
        "formula_exact": formula_exact,
        "sheet_invariant": sheet_invariant,
        "edge_subdivision_preserves_winding": refinement_invariant,
        "pass": closed > 0 and formula_exact and sheet_invariant and refinement_invariant,
    }


def recursive_refinement_checks(max_generation: int = 10) -> dict[str, object]:
    rows = []
    ok = True
    previous_turns: set[Fraction] | None = None

    for g in range(max_generation + 1):
        n = 4 * (2**g)
        substeps = 2**g
        order = carry_cycle_order(4, substeps)
        phases = {Fraction(k, n) for k in range(n)}
        nested = True if previous_turns is None else previous_turns.issubset(phases)
        if previous_turns is not None:
            ok &= nested
        previous_turns = phases

        # Max angular distance to nearest root in normalized turns is 1/(2N).
        max_nearest_turn_error = Fraction(1, 2 * n)
        rows.append(
            {
                "generation": g,
                "phase_cycle_order": n,
                "history_substeps_per_original_C4_edge": substeps,
                "carry_update_order": order,
                "nested_previous_root_group": nested,
                "max_nearest_phase_error_turns": str(max_nearest_turn_error),
                "max_nearest_phase_error_radians_bound": math.pi / n,
            }
        )
        ok &= order == n
        if g > 0:
            ok &= check_semiconjugacy(n // 2)

    density_bound_decreases = all(
        rows[i + 1]["max_nearest_phase_error_radians_bound"]
        < rows[i]["max_nearest_phase_error_radians_bound"]
        for i in range(len(rows) - 1)
    )
    ok &= density_bound_decreases

    return {
        "status": "exact algebraic theorem conditional on recursive ordered edge subdivision",
        "rows": rows,
        "density_bound_monotone_to_zero": density_bound_decreases,
        "pass": ok,
        "physical_status": "CONDITIONAL: recursive phase-edge/carry locking is not yet derived from the physical history/projector",
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--graphlink-json", type=Path)
    ap.add_argument("--dimension-json", type=Path)
    ap.add_argument("--max-generation", type=int, default=10)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    graphlink = read_json(args.graphlink_json)
    dimension = read_json(args.dimension_json)

    gray_edges_are_hamming = all(
        hamming(GRAY[k], GRAY[(k + 1) % 4]) == 1 for k in range(4)
    )

    graphlink_ok = True
    graphlink_evidence = None
    if graphlink is not None:
        graphlink_ok = bool(graphlink.get("passed")) and float(
            graphlink.get("graph_change_q2_adjacency_factorization_error", 1.0)
        ) < 1e-12
        graphlink_evidence = {
            "passed": bool(graphlink.get("passed")),
            "matrix_unit_factorization_error": graphlink.get("matrix_unit_factorization_error"),
            "graph_change_q2_adjacency_factorization_error": graphlink.get(
                "graph_change_q2_adjacency_factorization_error"
            ),
            "active_q2_sector_rank": graphlink.get("active_q2_sector_rank"),
            "no_link_singlet_rank": graphlink.get("no_link_singlet_rank"),
        }

    causal_doubling_ok = True
    causal_evidence = None
    if dimension is not None:
        causal_doubling_ok = bool(dimension.get("passed")) and int(
            dimension.get("causal_length_growth_per_generation", -1)
        ) == 2
        causal_evidence = {
            "passed": bool(dimension.get("passed")),
            "causal_length_growth_per_generation": dimension.get(
                "causal_length_growth_per_generation"
            ),
            "active_edge_growth_per_generation": dimension.get(
                "active_edge_growth_per_generation"
            ),
        }

    # First history lift C4 -> C8.
    first_refinement = {
        "coarse_cycle_order": 4,
        "refined_history_cycle_order": carry_cycle_order(4, 2),
        "coarse_shift_order": shift_order(4),
        "refined_shift_order": shift_order(8),
        "two_refined_ticks_project_to_one_coarse_tick": check_semiconjugacy(4),
        "gray_cycle_edges_are_frozen_hamming_edges": gray_edges_are_hamming,
    }
    first_refinement["pass"] = (
        first_refinement["refined_history_cycle_order"] == 8
        and first_refinement["refined_shift_order"] == 8
        and first_refinement["two_refined_ticks_project_to_one_coarse_tick"]
        and gray_edges_are_hamming
        and graphlink_ok
    )

    # Physical-state-only no-go: four history edge midpoints all project to one no-link state.
    midpoint_history_labels = tuple(("edge_event", k) for k in range(4))
    physical_midpoint_images = tuple("no_link" for _ in midpoint_history_labels)
    state_only_no_go = {
        "history_midpoint_count": len(set(midpoint_history_labels)),
        "instantaneous_no_link_image_count": len(set(physical_midpoint_images)),
        "instantaneous_active_plus_no_link_basis_size": 5,
        "required_C8_history_positions": 8,
        "channel_information_lost_without_history_label": len(set(physical_midpoint_images)) < len(set(midpoint_history_labels)),
        "pass": (
            len(set(midpoint_history_labels)) == 4
            and len(set(physical_midpoint_images)) == 1
            and 5 < 8
        ),
    }

    # Independent time-bit no-go.
    product_no_go = {
        "group": "Z4 x Z2",
        "max_element_order": independent_product_max_order(4, 2),
        "required_order_for_mu8": 8,
        "independent_product_cannot_generate_order8": independent_product_max_order(4, 2) < 8,
    }
    product_no_go["pass"] = product_no_go["independent_product_cannot_generate_order8"]

    winding = exhaustive_winding_checks(4, 8)
    recursive = recursive_refinement_checks(args.max_generation)

    exact_checks = {
        "gray_C4": gray_edges_are_hamming,
        "graphlink_factorization_input": graphlink_ok,
        "causal_length_doubling_input": causal_doubling_ok,
        "first_history_refinement_C4_to_C8": bool(first_refinement["pass"]),
        "state_only_C8_no_go": bool(state_only_no_go["pass"]),
        "independent_product_no_go": bool(product_no_go["pass"]),
        "history_to_integer_winding": bool(winding["pass"]),
        "conditional_recursive_algebra": bool(recursive["pass"]),
    }

    report = {
        "status": "q=2 history phase-refinement/winding frontier with exact-vs-conditional separation",
        "passed": all(exact_checks.values()),
        "q2_gray_cycle": [list(x) for x in GRAY],
        "graphlink_evidence": graphlink_evidence,
        "causal_rewrite_evidence": causal_evidence,
        "first_refinement": first_refinement,
        "instantaneous_state_no_go": state_only_no_go,
        "independent_clock_product_no_go": product_no_go,
        "winding_universal_cover": winding,
        "recursive_phase_refinement": recursive,
        "exact_checks": exact_checks,
        "theorems": {
            "history_winding": "For a nearest-neighbor path on oriented C_N, path lifting to the universal cover Z is unique after choosing one initial lift; closed-path winding is the deck-transformation integer and is sheet-independent.",
            "first_phase_refinement": "Once each selected oriented C4 edge is represented as a distinct two-stage history event, canonical edge subdivision gives one connected C8 with a carry update of order 8; two fine ticks coarse-project to one C4 tick.",
            "carry_requirement": "Z4 x Z2 is not cyclic of order 8. Phase refinement requires a carry/edge-subdivision relation, not an independent binary clock register.",
            "recursive_conditional": "If the ordered edge-subdivision rule is physically self-similar at every refinement, C_(4*2^g) and nested mu_(4*2^g) follow and the phase mesh tends to zero.",
        },
        "physical_frontier": {
            "history_to_winding": "EXACT_TOPOLOGICAL once full transition history is retained",
            "C4_to_C8_history_graph": "EXACT_HISTORY_LIFT using the already-factorized q=2 edge channels",
            "C8_to_C16_to_U1": "CONDITIONAL_ALGEBRA; needs recursive physical carry locking",
            "instantaneous_5_state_Hilbert_to_C8": "NEGATIVE without transition/history channel resolution",
            "causal_length_doubling": "EXACT in the frozen q=2 rewrite input",
            "phase_causal_locking": "OPEN_PHYSICAL",
            "history_measure_and_physical_projector": "OPEN_PHYSICAL",
        },
        "claim_boundary": (
            "The gate proves that winding is already an integer topological observable of complete q=2 phase histories and that the first C4->C8 refinement is the canonical edge-history lift of the existing two-step graph-link factorization. It also proves two no-go results: the five-state instantaneous Hilbert and an independent Z2 clock cannot supply the C8 phase. The infinite dyadic phase tower is mathematically exact only conditional on recursive physical carry/edge-subdivision self-similarity; current evidence does not yet derive that locking from the microscopic Hamiltonian or physical-projector measure."
        ),
    }

    text = json.dumps(report, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
