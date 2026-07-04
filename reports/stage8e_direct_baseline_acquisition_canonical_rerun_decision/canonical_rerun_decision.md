# Canonical rerun decision

## Decision

A new canonical rerun is not approved yet.

## Reason

The project has primary-model result artifacts, but the direct baseline package is still missing.

## Required before rerun

Before a canonical rerun, the following must exist:

- matched sample label table;
- seed list;
- fold table;
- primary model row-level predictions or executable primary rerun path;
- direct baseline input package;
- direct baseline execution path;
- output manifest and hashes.

## Rerun rule

The rerun must produce one final matched comparison table rather than mixing old protocol variants.

## Output required after rerun

- final primary metrics;
- final direct baseline metrics;
- row-level predictions for both models;
- fold-level stability table;
- confidence intervals;
- final claim-safe summary.
