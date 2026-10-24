# BQG depth-6 [3,2] recovery status snapshot — 2026-10-24 20:18 UTC

## Scope and claim boundary

This is an operational snapshot of GitHub Actions run [39743112374](https://github.com/Shtenco/binary_quantum_theory/actions/runs/39743112374), attempt 2, on branch `bqg/depth6-32-canonical-recovery`. It is not a numerical closure or rank certificate.

The frozen target remains 2,755 orbit blocks / 130,903 columns. The authorized source replay is run `39708640090`. The recovery plan partitions the missing frozen orbit IDs into 195 chunks, with the 63 already-durable chunks excluded from recomputation.

## Current attempt status

At 2026-10-24 20:18 UTC, the jobs API returned 196 jobs with the following states:

- 64 completed successfully (the prepare job plus 63 previously durable recovery chunks).
- 84 recovery jobs completed with failure.
- 4 recovery jobs in progress.
- 44 recovery jobs queued.

Thus, 128 of the 132 jobs needing retry had not produced a successful completion at this snapshot (84 failed, 4 running, 44 queued). Do not interpret the run-level API's `queued` status as the complete state: the per-job endpoint simultaneously reported active jobs. Treat this as an API status inconsistency and use the per-job results for this snapshot.

The run artifact listing contained 65 artifacts: 63 recovery chunk artifacts, one frozen source snapshot, and one recovery plan. No full 2,755-block union or numerical closure certificate was present.

## Failure evidence

Logs for multiple failed recovery jobs were retrievable. For example:

- Job 120757762041, chunk 0 (oversize singleton orbit 2744), ran from 02:46:56 to 04:30:36 UTC. The numerical replay step did not emit a Python exception in the available log tail; the runner reported a shutdown signal and cancellation.
- Job 120757770053, chunk 146, ran from 19:45:54 to 20:11:34 UTC. The same runner-shutdown/cancellation message appeared after the replay step began.

The logs show cancellation at the runner/process level, not a demonstrated mathematical assertion failure. The root cause of runner shutdown is **not established**. Resource exhaustion or hosted-runner termination are hypotheses only; this snapshot does not prove either.

## Integrity and coverage baseline

The previous independent archive audit found:

- 63 recovery archives and 20 original source-shard archives inspected.
- ZIP CRC errors: 0.
- Recovery manifest mismatches: 0.
- Recovery payload SHA-256 mismatches: 0.
- Duplicate recovery orbit IDs: 0.
- Overlap between original source and recovery orbit IDs: 0.
- Combined durable union: 216 / 2,755 blocks and 34,700 / 130,903 columns.
- Coverage: 7.84% by blocks and 26.51% by columns.
- Detected integrity errors in inspected archives: 0.

This coverage figure is based on the durable artifacts already audited; it must not be increased based on queued or running jobs. Re-audit artifacts after additional jobs actually upload results.

## Next safe steps

1. Allow the currently running jobs to finish before triggering another retry, to avoid overlapping work.
2. Poll the per-job API, not only the run-level status field.
3. For newly completed jobs, inspect the failed step and log tail; distinguish Python exceptions, timeouts, cancellations, and runner shutdown.
4. Re-fetch the artifact listing and audit any genuinely new archives by CRC, manifest status, identity, and payload SHA-256.
5. Do not claim full [3,2] closure, rank, or a kernel result until the complete frozen union is present and the downstream global calculation and validation pass.

## Scientific status

`rank_certified=false` and `numerical_closure_claimed=false` remain the correct claim boundary. Complete KEYMETA persistence is a prerequisite for global peeling/SVD, not a rank certificate by itself.
