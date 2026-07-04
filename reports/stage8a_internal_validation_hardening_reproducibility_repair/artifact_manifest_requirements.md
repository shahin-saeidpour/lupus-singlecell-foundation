# Artifact manifest requirements

## Purpose

A manuscript-facing result must be reproducible from versioned artifacts, not only summary tables.

## Required artifacts

The final internal-validation package must include or reference:

1. donor embedding artifact archive;
2. row-level prediction table;
3. fold assignment table;
4. canonical metric table;
5. environment manifest;
6. command log or run script;
7. SHA256 hashes for all large external artifacts.

## Large files policy

Large embeddings do not need to be committed directly to Git.

Acceptable options:

- Git LFS;
- Zenodo;
- OSF;
- institutional storage;
- release asset with SHA256 recorded in the repository.

## Minimum manifest fields

Each external artifact must record:

- artifact name;
- file path or URL;
- file size;
- SHA256 hash;
- creation command;
- creation date;
- source commit;
- expected consumer script;
- notes about privacy or redistribution limits.

## Blocking rule

If the donor embeddings and prediction table cannot be reproduced or verified from recorded artifacts, manuscript claims must be downgraded to exploratory internal evidence.
