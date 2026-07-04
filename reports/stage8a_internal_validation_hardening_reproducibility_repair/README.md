# Stage 8A internal validation hardening and reproducibility repair

This package records the internal-validation hardening work required before strong manuscript claims.

## Scope

Stage 8A is a repair and hardening gate. It does not rerun model training in this repository state because the raw donor embeddings and row-level prediction artifacts are not committed.

## Why this stage exists

Stage 6 produced strong internal summary metrics, but manuscript-readiness requires stronger reproducibility and stability evidence before any Q1-style claim.

Open concerns:

1. severe class imbalance: 14 FLARE donors versus 148 managed-SLE donors;
2. fold-level instability because each 5-fold test split contains only about 2 to 3 FLARE donors;
3. inconsistent repeated-CV protocols reported across outputs;
4. missing row-level prediction table and raw embedding artifact manifest in the repository;
5. missing direct raw-count or pseudobulk baseline comparison.

## Stage 8A goal

Convert those concerns into explicit repair requirements:

- one canonical validation protocol;
- row-level prediction table requirements;
- reproducibility artifact requirements;
- baseline comparison requirements;
- manuscript claim gate.

## Final expected outcome

Stage 8A should end with a clear decision about whether the current Stage 6 result is manuscript-ready or blocked pending additional execution.
