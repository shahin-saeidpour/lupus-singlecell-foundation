#!/usr/bin/env python3
"""Stage 9C pseudobulk construction gate.

This gate checks readiness before any donor-level pseudobulk construction. It
intentionally performs no construction when required inputs are missing.
"""

from __future__ import annotations

import csv
from pathlib import Path

REPORT_DIR = Path("reports/stage9c_pseudobulk_baseline_construction/audit")
REQUIRED = [
    Path("artifacts/stage9a/local_source_registry.csv"),
    Path("artifacts/stage8g/baseline_inputs/labels.csv"),
    Path("artifacts/stage8g/baseline_inputs/fold_assignments.csv"),
    Path("artifacts/stage8g/baseline_inputs/donor_inventory.csv"),
]
DIRECT_PSEUDOBULK = Path("artifacts/stage8g/baseline_inputs/pseudobulk_matrix.csv.gz")


def main() -> int:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    missing = []
    rows = []
    for path in REQUIRED:
        status = "present" if path.exists() else "missing"
        rows.append([str(path), status])
        if status == "missing":
            missing.append(str(path))

    direct_status = "present" if DIRECT_PSEUDOBULK.exists() else "missing"
    rows.append([str(DIRECT_PSEUDOBULK), direct_status])
    if direct_status == "missing":
        missing.append(str(DIRECT_PSEUDOBULK))

    status = "blocked_missing_inputs" if missing else "ready_for_controlled_construction"

    with (REPORT_DIR / "stage9c_construction_gate.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["path", "status"])
        writer.writerows(rows)

    with (REPORT_DIR / "execution_decision.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["field", "value"])
        writer.writerow(["stage", "9C"])
        writer.writerow(["status", status])
        writer.writerow(["pseudobulk_constructed", "false"])
        writer.writerow(["numeric_execution", "false"])
        writer.writerow(["predictions_created", "false"])
        writer.writerow(["scores_created", "false"])

    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
