#!/usr/bin/env python3
"""Stage 8F direct baseline readiness scaffold.

Header-only checker for future Stage 8G input files. It writes a decision file
and intentionally performs no numerical analysis.
"""

from __future__ import annotations

import csv
from pathlib import Path

REQUIRED_FILES = [
    "pseudobulk_matrix.csv.gz",
    "labels.csv",
    "fold_assignments.csv",
    "donor_inventory.csv",
    "preprocessing_config.yaml",
    "file_hashes.csv",
    "environment.json",
]


def write_decision(output_dir: Path, status: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "execution_decision.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["field", "value"])
        writer.writerow(["stage", "8F"])
        writer.writerow(["status", status])
        writer.writerow(["numerical_analysis", "not_run"])


def main() -> int:
    input_dir = Path("artifacts/stage8g/baseline_inputs")
    output_dir = Path("reports/stage8f_baseline_construction_plan_execution_scaffold/readiness_check")
    missing = [name for name in REQUIRED_FILES if not (input_dir / name).exists()]
    status = "blocked_missing_inputs" if missing else "ready_for_stage8g_review"
    write_decision(output_dir, status)
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
