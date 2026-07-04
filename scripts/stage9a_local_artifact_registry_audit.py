#!/usr/bin/env python3
"""Stage 9A local artifact registry audit.

This script checks whether the local source registry exists and whether listed
paths are present. It records status only. It does not load matrices, compute
scores, train models, or generate predictions.
"""

from __future__ import annotations

import csv
from pathlib import Path

REGISTRY = Path("artifacts/stage9a/local_source_registry.csv")
TEMPLATE = Path("artifacts/stage9a/local_source_registry_template.csv")
REPORT_DIR = Path("reports/stage9a_direct_baseline_artifact_intake/audit")


def main() -> int:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    source = REGISTRY if REGISTRY.exists() else TEMPLATE
    rows = []
    blocked = not REGISTRY.exists()

    if source.exists():
        with source.open("r", newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                local_path = row.get("local_path", "")
                required = row.get("required", "").lower() == "true"
                exists = bool(local_path and local_path != "TODO" and Path(local_path).exists())
                status = "present" if exists else "missing"
                if required and not exists:
                    blocked = True
                rows.append([
                    row.get("artifact_id", ""),
                    row.get("artifact_role", ""),
                    local_path,
                    str(required).lower(),
                    status,
                ])
    else:
        blocked = True

    with (REPORT_DIR / "stage9a_registry_audit.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["artifact_id", "artifact_role", "local_path", "required", "status"])
        writer.writerows(rows)

    with (REPORT_DIR / "execution_decision.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["field", "value"])
        writer.writerow(["stage", "9A"])
        writer.writerow(["status", "blocked_missing_local_artifacts" if blocked else "ready_for_stage9b_audit"])
        writer.writerow(["registry_exists", str(REGISTRY.exists()).lower()])
        writer.writerow(["numeric_execution", "false"])
        writer.writerow(["predictions_created", "false"])
        writer.writerow(["metrics_created", "false"])

    return 1 if blocked else 0


if __name__ == "__main__":
    raise SystemExit(main())
