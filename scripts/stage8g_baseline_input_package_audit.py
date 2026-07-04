#!/usr/bin/env python3
"""Stage 8G baseline input package audit.

This script checks whether the expected Stage 8G baseline input files exist.
It does not create predictions, compute metrics, or run external scoring.
"""

from __future__ import annotations

import csv
from pathlib import Path

INPUT_DIR = Path("artifacts/stage8g/baseline_inputs")
REPORT_DIR = Path("reports/stage8g_baseline_data_acquisition_construction/audit")

REQUIRED = [
    "pseudobulk_matrix.csv.gz",
    "labels.csv",
    "fold_assignments.csv",
    "donor_inventory.csv",
    "preprocessing_config.yaml",
    "file_hashes.csv",
    "environment.json",
]


def main() -> int:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    missing = []
    for name in REQUIRED:
        path = INPUT_DIR / name
        status = "present" if path.exists() else "missing"
        if status == "missing":
            missing.append(name)
        rows.append((name, str(path), status))

    with (REPORT_DIR / "stage8g_input_audit.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["file_name", "path", "status"])
        writer.writerows(rows)

    with (REPORT_DIR / "execution_decision.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["field", "value"])
        writer.writerow(["stage", "8G"])
        writer.writerow(["status", "blocked_missing_inputs" if missing else "ready_for_stage8h_review"])
        writer.writerow(["predictions_created", "false"])
        writer.writerow(["metrics_created", "false"])
        writer.writerow(["external_scoring", "false"])

    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
