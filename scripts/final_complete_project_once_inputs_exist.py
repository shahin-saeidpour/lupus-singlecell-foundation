#!/usr/bin/env python3
"""Final completion gate for the lupus project.

This is the single remaining task controller. It stops the stage-loop and
reports whether the project can be considered complete.

It does not invent data. If real local baseline artifacts are missing, it
fails closed with a clear report.
"""

from __future__ import annotations

import csv
import json
import platform
from datetime import datetime, timezone
from pathlib import Path

REPORT_DIR = Path("reports/final_remaining_task")
BASELINE_DIR = Path("artifacts/stage8g/baseline_inputs")
REGISTRY = Path("artifacts/stage9a/local_source_registry.csv")

REQUIRED_BASELINE_FILES = [
    BASELINE_DIR / "pseudobulk_matrix.csv.gz",
    BASELINE_DIR / "labels.csv",
    BASELINE_DIR / "fold_assignments.csv",
    BASELINE_DIR / "donor_inventory.csv",
    BASELINE_DIR / "preprocessing_config.yaml",
    BASELINE_DIR / "file_hashes.csv",
    BASELINE_DIR / "environment.json",
]


def write_csv(path: Path, header: list[str], rows: list[list[str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)


def main() -> int:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    rows = []
    missing = []
    for path in REQUIRED_BASELINE_FILES:
        status = "present" if path.exists() else "missing"
        rows.append([str(path), status])
        if status == "missing":
            missing.append(str(path))

    registry_status = "present" if REGISTRY.exists() else "missing"
    rows.append([str(REGISTRY), registry_status])

    if missing:
        project_status = "blocked_missing_real_local_baseline_artifact"
        completion_status = "incomplete"
        next_action = "place_required_baseline_files_or_register_real_local_source"
        exit_code = 1
    else:
        project_status = "all_required_baseline_inputs_present"
        completion_status = "complete"
        next_action = "ready_for_matched_rerun_or_final_archive"
        exit_code = 0

    write_csv(REPORT_DIR / "required_file_audit.csv", ["path", "status"], rows)

    final_rows = [
        ["project_completion_status", completion_status],
        ["project_status", project_status],
        ["required_missing_count", str(len(missing))],
        ["numeric_execution", "not_run_by_this_gate"],
        ["predictions_created", "false"],
        ["metrics_created", "false"],
        ["next_action", next_action],
    ]
    write_csv(REPORT_DIR / "final_task_status.csv", ["field", "value"], final_rows)

    environment = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "script": "scripts/final_complete_project_once_inputs_exist.py",
    }
    (REPORT_DIR / "final_task_environment.json").write_text(
        json.dumps(environment, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
