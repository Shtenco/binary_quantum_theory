# Depth-6 [3,2] Canonical Recovery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the `[3,2]` numerical recovery path reproducible from canonical `main` without recomputing the frozen depth-6 shell/orbits/multiplicity/Jucys structure, then prepare a ledger-driven keymeta-first retry path that can only advance after complete persisted coverage.

**Architecture:** Canonicalize only the recovery/inventory logic needed on `main`, with a small standalone keymeta coverage module instead of importing research-only proof code. Add a fail-closed verifier for `BQG_DEPTH6_32_RECOVERY_FRONTIER_2026-10-02.json`, a persisted-assignment ledger schema/verifier, and a batch planner that consumes that ledger but never reconstructs assignments. Wire these gates into `core-regression`; keep the expensive numerical master-map engine on the research proof branch until its inputs are frozen and complete.

**Tech Stack:** Python 3.11+, standard library (`json`, `gzip`, `pickle`, `zipfile`, `hashlib`, `urllib`), GitHub Actions YAML, existing repository JSON ledgers.

**Spec:** `docs/superpowers/specs/2026-10-01-depth6-proof-frontier-design.md`

## Global Constraints

- `[3,2].structural_status` remains `CLOSED`; this work must never reopen shell/orbit/Jucys/branch-sum proof.
- Frozen targets are exactly `2755` blocks and `130903` columns.
- No retry code may call `shell(6)`, enumerate S5 orbits, call `exact_mult`, or reconstruct Jucys assignment metadata.
- Partial keymeta coverage is reusable evidence only and must keep `schedule_allowed=false`.
- Global actual-q peeling/SVD is forbidden until complete persisted coverage reaches `2755/2755` blocks and `130903/130903` columns.
- Matching/peeling failure is not an operator kernel; failed numerical candidates stay present for replay.
- Any new canonical ledger or manifest must carry provenance and SHA-256 where file content is persisted.
- The current full finite depth-6 theorem remains `NOT_YET_PROVED` until `[3,2]`, `[3,1,1]`, and `[2,2,1]` have independent finite numerical master witnesses.

## Review Focus

- Duplicate shard/orbit identifiers must fail closed rather than be silently overwritten.
- A complete set of 112 shard IDs with the wrong block/column totals must fail closed.
- Mixed proof-engine hashes in keymeta must fail closed.
- Missing or malformed persisted assignment records must never trigger reconstruction from shell/Jucys code.
- CI must distinguish “frontier ledger is internally consistent” from “`[3,2]` is numerically closed.”

---

### Task 1: Canonical keymeta coverage module and inventory restoration

**Files:**
- Create: `scripts/depth6_keymeta_coverage.py`
- Create: `scripts/inventory_depth6_32_keymeta.py`
- Create: `scripts/test_depth6_keymeta_coverage.py`
- Create: `scripts/test_inventory_depth6_32_keymeta.py`

**Interfaces:**
- Consumes: persisted `BQG_MIXED_MASTER_KEY_METADATA` payloads only.
- Produces: `validate_keymeta_coverage(records, *, irrep, expected_shards, target_blocks, target_columns) -> dict`, plus inventory helpers `is_candidate_keymeta_artifact_name`, `load_payloads_from_zip`, `choose_latest_payloads`.

- [ ] **Step 1: Write failing tests** for incomplete coverage, duplicate shard, duplicate orbit, mixed engine hash, wrong full totals, multi-shard salvage ZIP, and single-vs-salvage artifact-name recognition.
- [ ] **Step 2: Run the focused tests and confirm failure** because canonical modules are absent.
- [ ] **Step 3: Implement the standalone coverage module** by extracting only the persisted-keymeta validation logic from the research proof branch; no import from `mixed_parallel`.
- [ ] **Step 4: Restore/adapt the inventory script** so it can ingest both one-shard artifacts and multi-shard salvage artifacts, deduplicate by shard using artifact freshness, and validate every loaded payload against its shard ID.
- [ ] **Step 5: Run focused tests and compile checks**; expected result is PASS with no proof-branch dependency.
- [ ] **Step 6: Commit** the canonical recovery inventory restoration.

### Task 2: Fail-closed `[3,2]` recovery-frontier verifier

**Files:**
- Create: `scripts/verify_depth6_32_recovery_frontier.py`
- Create: `scripts/test_verify_depth6_32_recovery_frontier.py`
- Modify: `.github/workflows/core-regression.yml`

**Interfaces:**
- Consumes: `BQG_DEPTH6_32_RECOVERY_FRONTIER_2026-10-02.json`, `depth6_frontier.json`, canonical script paths.
- Produces: exit `0` only when the recovery ledger preserves the exact scientific boundary and all declared canonical implementation files are present.

- [ ] **Step 1: Write failing verifier tests** covering exact targets/status, 15 preserved shards, quarantined targeted retry, `schedule_allowed=false`, no structural recompute, and required canonical implementation files.
- [ ] **Step 2: Run tests and confirm RED** on the pre-restoration state.
- [ ] **Step 3: Implement verifier** with explicit assertions for the frozen numbers and claim boundary; do not check Git history ancestry as proof, check the canonical files and immutable identifiers actually needed for reproduction.
- [ ] **Step 4: Wire verifier and focused unit tests into `core-regression`** before expensive structural jobs.
- [ ] **Step 5: Run verifier/tests and compile checks**; expected result is PASS while `[3,2].numerical_status` remains `RECOVER_OR_FINISH`.
- [ ] **Step 6: Commit** the recovery frontier gate.

### Task 3: Persisted assignment ledger schema and fail-closed collector

**Files:**
- Create: `scripts/depth6_assignment_ledger.py`
- Create: `scripts/test_depth6_assignment_ledger.py`
- Create: `BQG_DEPTH6_32_ASSIGNMENT_LEDGER_2026-10-02.json`

**Interfaces:**
- Consumes: already persisted keymeta/raw-summary assignment records containing `orbit_index`, `rep`, `m`, and optional `coord_dim`/cost provenance.
- Produces: canonical ledger records keyed by `orbit_id` plus `coverage` and `ledger_sha256`; never synthesizes missing records.

- [ ] **Step 1: Write failing tests** for duplicate orbit IDs, inconsistent reps/multiplicities, missing provenance, stable canonical serialization/hash, and incomplete coverage staying `INCOMPLETE_PERSISTED_ASSIGNMENT_LEDGER`.
- [ ] **Step 2: Implement `normalize_assignment_record`, `merge_assignment_records`, `build_assignment_ledger`, and `verify_assignment_ledger`** without any shell/Jucys imports.
- [ ] **Step 3: Build the current canonical ledger only from persisted records already present in repository recovery ledgers.** If only the known 15 assignments can be proven, record that incompleteness explicitly; do not manufacture the other 2740.
- [ ] **Step 4: Add the assignment-ledger verifier to the recovery-frontier verifier** so retry scheduling remains forbidden until the persisted ledger is complete.
- [ ] **Step 5: Run tests and compile checks**; expected result is PASS for ledger integrity but `retry_allowed=false` while incomplete.
- [ ] **Step 6: Commit** the persisted assignment boundary.

### Task 4: Ledger-driven cost-balanced batch planner

**Files:**
- Create: `scripts/plan_depth6_32_batches.py`
- Create: `scripts/test_plan_depth6_32_batches.py`

**Interfaces:**
- Consumes: `BQG_DEPTH6_32_ASSIGNMENT_LEDGER_2026-10-02.json` only.
- Produces: deterministic batches of immutable orbit records and a manifest hash; refuses incomplete ledgers unless invoked in explicit diagnostic mode.

- [ ] **Step 1: Write failing tests** for deterministic greedy cost balancing, no record mutation, full union/no overlap, and refusal to plan canonical compute from incomplete coverage.
- [ ] **Step 2: Implement planner** using persisted `cost_proxy` when present, otherwise a declared deterministic fallback based only on persisted fields (for diagnostics only unless the ledger is complete).
- [ ] **Step 3: Run tests and compile checks**; expected result is PASS and no call path to shell/orbit/Jucys reconstruction.
- [ ] **Step 4: Commit** the batch planner.

### Task 5: Keymeta-first retry contract and workflow skeleton

**Files:**
- Create: `scripts/run_depth6_32_ledger_batch.py`
- Create: `scripts/test_run_depth6_32_ledger_batch.py`
- Create: `.github/workflows/bqg-depth6-32-ledger-keymeta-first.yml`

**Interfaces:**
- Consumes: a complete frozen assignment ledger, one deterministic batch manifest, and the existing proof bundle/engine functions needed to calculate the actual master map for an already-specified `rep`/`m` record.
- Produces: small per-batch keymeta artifacts first; optional raw matrices are retained only for blocks later selected for numerical rank certification.

- [ ] **Step 1: Write failing contract tests** proving the runner accepts explicit persisted assignments and has no shell/orbit/exact-mult/Jucys-assignment bootstrap path.
- [ ] **Step 2: Implement runner adapter** that computes from explicit frozen records and emits keymeta immediately after each successful block, with provenance and manifest hash.
- [ ] **Step 3: Create workflow skeleton** guarded by assignment-ledger completeness; canonical execution must fail before compute if the ledger is incomplete.
- [ ] **Step 4: Run unit/compile checks**. Do not launch expensive `[3,2]` Actions from an incomplete ledger.
- [ ] **Step 5: Commit** the keymeta-first compute contract.

### Task 6: Branch-wide verification

**Files:**
- Verify all files above plus `.github/workflows/core-regression.yml`.

**Interfaces:**
- Consumes: completed Tasks 1-5.
- Produces: a branch that is safe to merge without changing any numerical closure claim.

- [ ] **Step 1: Run all new unit tests.**
- [ ] **Step 2: Run `python -m compileall -q scripts`.**
- [ ] **Step 3: Run `python scripts/verify_depth6_frontier.py` and `python scripts/verify_depth6_32_recovery_frontier.py`.**
- [ ] **Step 4: Confirm the canonical state still says `[3,2] = RECOVER_OR_FINISH` and full depth-6 theorem `NOT_YET_PROVED`.**
- [ ] **Step 5: Review branch diff for accidental structural recomputation imports/calls (`shell`, `exact_mult`, Jucys assignment generation).**
- [ ] **Step 6: Commit any final verification-only adjustments and open a PR against `main`.**
