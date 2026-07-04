#!/usr/bin/env python3
"""Stage 9B local baseline input audit.

This script audits whether the files required for direct baseline construction
exist. It does not build pseudobulk matrices, fit models, make predictions, or
compute metrics.
"""

from __future__ import annotations

import csv
from pathlib import Path

REPORT_DIR = Path("reports/stage9b_local_baseline_input_audit/audit")
REQUIRED_FILES = [
    Path("artifacts/stage9a/local_source_registry.csv"),
    Path("artifacts/stage8g/baseline_inputs/labels.csv"),
    Path("artifacts/stage8g/baseline_inputs/fold_assignments.csv"),
    Path("artifacts/stage8g/baseline_inputs/donor_inventory.csv"),
    Path("artifacts/stage8g/baseline_inputs/preprocessing_config.yaml"),
    Path("artifacts/stage8g/baseline_inputs/file_hashes.csv"),
    Path("artifacts/stage8g/baseline_inputs/environment.json"),
]
PSEUDOBULK = Path("artifacts/stage8g/baseline_inputs/pseudobulk_matrix.csv.gz")


def main() -> int:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    missing = []

    for path in REQUIRED_FILES:
        status = "present" if path.exists() else "missing"
        if status == "missing":
            missing.append(str(path))
        rows.append([str(path), status])

    pseudobulk_status = "present" if PSEUDOBULK.exists() else "missing"
    if pseudobulk_status == "missing":
        missing.append(str(PSEUDOBULK))
    rows.append([str(PSEUDOBULK), pseudobulk_status])

    decision = "ready_for_stage9c_construction" if not missing else "blocked_missing_baseline_inputs"

    with (REPORT_DIR / "stage9b_file_audit.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["path", "status"])
        writer.writerows(rows)

    with (REPORT_DIR / "execution_decision.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["field", "value"])
        writer.writerow(["stage", "9B"])
        writer.writerow(["status", decision])
        writer.writerow(["pseudobulk_construction", "not_run"])
        writer.writerow(["numeric_execution", "false"])
        writer.writerow(["predictions_created", "false"])
        writer.writerow(["metrics_created", "false"])

    return 0 if not missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
