#!/usr/bin/env python3
"""Validate progress/progress.json and render the Markdown progress tracker."""

from __future__ import annotations

import argparse
import json
import sys
from collections import OrderedDict
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "progress" / "progress.json"
OUTPUT = ROOT / "PROGRESS.md"

MILESTONES = OrderedDict(
    [
        ("explain", "Explain trade-offs"),
        ("guided", "Apply with guidance"),
        ("independent", "Apply independently"),
        ("diagnose", "Diagnose / edge case"),
    ]
)

CATEGORIES = OrderedDict(
    [
        (
            "IaC, DevOps & DataOps",
            OrderedDict(
                [
                    ("DEV-01", "Terraform and remote state"),
                    ("DEV-02", "Azure identity and secrets"),
                    ("DEV-03", "Local tooling and automated tests"),
                    ("DEV-04", "CI/CD and environment promotion"),
                    ("DEV-05", "Monitoring, recovery, and rollback"),
                ]
            ),
        ),
        (
            "Azure Architecture & Compute",
            OrderedDict(
                [
                    ("ARC-01", "Storage, networking, and access"),
                    ("ARC-02", "DuckDB and Parquet"),
                    ("ARC-03", "Azure batch compute and serving"),
                    ("ARC-04", "Standalone Spark and performance tuning"),
                    ("ARC-05", "Azure Databricks and cost trade-offs"),
                ]
            ),
        ),
        (
            "Ingestion & Analytics Engineering",
            OrderedDict(
                [
                    ("ING-01", "Source discovery and data contracts"),
                    ("ING-02", "Incremental loads and CDC"),
                    ("ING-03", "Fivetran, Airbyte, and dlt"),
                    ("ING-04", "SQL modelling and dbt"),
                    ("ING-05", "Data quality, replay, and backfills"),
                ]
            ),
        ),
        (
            "Mission Outcomes & Experimentation",
            OrderedDict(
                [
                    ("OUT-01", "Decision discovery and metric design"),
                    ("OUT-02", "Reach, outcomes, and equity"),
                    ("OUT-03", "Funnels, cohorts, and segmentation"),
                    ("OUT-04", "Capacity and unit economics"),
                    ("OUT-05", "Experiment design and causal evaluation"),
                ]
            ),
        ),
        (
            "Applied ML & MLOps",
            OrderedDict(
                [
                    ("ML-01", "Regression, classification, and forecasting"),
                    ("ML-02", "Validation, leakage, and baselines"),
                    ("ML-03", "MLflow tracking and model registry"),
                    ("ML-04", "Batch scoring and model promotion"),
                    ("ML-05", "Drift, performance, and retraining"),
                ]
            ),
        ),
    ]
)

SESSION_TITLES = [
    "Define the platform target",
    "Reproducible local developer loop",
    "Terraform bootstrap and state",
    "Azure boundaries and access",
    "CI and workload identity",
    "Independent sandbox repetition",
    "Discover sources and decisions",
    "Incremental ingestion choices",
    "Partial-failure recovery lab",
    "DuckDB and Parquet path",
    "Plain SQL versus dbt",
    "Quality, replay, and backfill",
    "Reach, outcomes, and equity",
    "Funnels, cohorts, and segments",
    "Capacity and unit economics",
    "Experiments and causal limits",
    "Azure batch and serving design",
    "Promote, recover, and cost",
    "PySpark beyond Databricks",
    "Spark plans and bottlenecks",
    "Cross-engine comparison",
    "Databricks value and lock-in",
    "Connector decision lab",
    "Architecture consolidation",
    "Baselines before models",
    "Validation and leakage",
    "Reproducible MLflow runs",
    "Batch scoring and promotion",
    "Outcomes and drift",
    "ML failure and rollback",
    "Forecasting with constraints",
    "End-to-end platform design",
    "Independent rebuild",
    "Evaluation synthesis",
    "Troubleshooting consolidation",
    "Evidence review and next pass",
]
SESSION_IDS = [f"S{number:02d}" for number in range(1, 37)]
SESSION_STATUS = {
    "not_started": "Not started",
    "in_progress": "In progress",
    "completed": "Completed",
}
DAY_NAMES = ("Monday", "Wednesday", "Friday")
DAY_OFFSETS = (0, 2, 4)


def fail(message: str) -> None:
    raise ValueError(message)


def load_and_validate() -> dict:
    try:
        data = json.loads(SOURCE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"Cannot read {SOURCE.relative_to(ROOT)}: {exc}")

    if data.get("schema_version") != 1:
        fail("schema_version must be 1")

    start_date = data.get("start_date")
    if start_date is not None:
        try:
            parsed = date.fromisoformat(start_date)
        except (TypeError, ValueError):
            fail("start_date must be null or an ISO date (YYYY-MM-DD)")
        if parsed.weekday() != 0:
            fail("start_date must be the Monday of Week 1")

    expected_skills = {
        skill_id for topics in CATEGORIES.values() for skill_id in topics
    }
    skills = data.get("skills")
    if not isinstance(skills, dict) or set(skills) != expected_skills:
        missing = sorted(expected_skills - set(skills or {}))
        extra = sorted(set(skills or {}) - expected_skills)
        fail(f"skills must contain exactly 25 known IDs; missing={missing}, extra={extra}")

    for skill_id, skill in skills.items():
        if not isinstance(skill.get("blocked"), bool):
            fail(f"{skill_id}.blocked must be true or false")
        if not isinstance(skill.get("note"), str):
            fail(f"{skill_id}.note must be a string")
        milestone_data = skill.get("milestones")
        if not isinstance(milestone_data, dict) or set(milestone_data) != set(MILESTONES):
            fail(f"{skill_id}.milestones must contain exactly {list(MILESTONES)}")
        for milestone, evidence in milestone_data.items():
            if not isinstance(evidence, list) or not all(
                isinstance(item, str) and item.strip() for item in evidence
            ):
                fail(f"{skill_id}.{milestone} must be a list of non-empty evidence links")

    sessions = data.get("sessions")
    if not isinstance(sessions, dict) or set(sessions) != set(SESSION_IDS):
        missing = sorted(set(SESSION_IDS) - set(sessions or {}))
        extra = sorted(set(sessions or {}) - set(SESSION_IDS))
        fail(f"sessions must contain exactly S01–S36; missing={missing}, extra={extra}")
    for session_id, session in sessions.items():
        if session.get("status") not in SESSION_STATUS:
            fail(f"{session_id}.status must be one of {list(SESSION_STATUS)}")
        evidence = session.get("evidence")
        if not isinstance(evidence, list) or not all(
            isinstance(item, str) and item.strip() for item in evidence
        ):
            fail(f"{session_id}.evidence must be a list of non-empty links")

    return data


def milestone_count(skill: dict) -> int:
    return sum(bool(skill["milestones"][name]) for name in MILESTONES)


def percent(completed: int, total: int) -> int:
    return round(100 * completed / total)


def progress_bar(completed: int, total: int) -> str:
    value = percent(completed, total)
    filled = min(10, (value + 5) // 10)
    return f"[{'█' * filled}{'░' * (10 - filled)}] {value}%"


def rag(completed: int, total: int) -> str:
    if completed == 0:
        return "🔴 Red — not started"
    if completed == total:
        return "🟢 Green — independently demonstrated"
    return "🟠 Amber — learning or needs reinforcement"


def session_position(index: int) -> tuple[int, str, int]:
    return index // 3 + 1, DAY_NAMES[index % 3], DAY_OFFSETS[index % 3]


def session_date(start: date | None, index: int) -> str:
    if start is None:
        return ""
    week, _, offset = session_position(index)
    return (start + timedelta(days=(week - 1) * 7 + offset)).isoformat()


def render(data: dict) -> str:
    skills = data["skills"]
    sessions = data["sessions"]
    parsed_start = date.fromisoformat(data["start_date"]) if data["start_date"] else None
    total_skill_milestones = sum(milestone_count(skill) for skill in skills.values())
    completed_sessions = sum(
        session["status"] == "completed" for session in sessions.values()
    )

    lines = [
        "# Learning progress",
        "",
        "> Generated from `progress/progress.json` by `python3 scripts/render_progress.py`. Do not edit this file directly.",
        "",
        "## Overall",
        "",
        f"- **Demonstrated skill progress:** {progress_bar(total_skill_milestones, 100)} ({total_skill_milestones}/100 milestones)",
        f"- **Session completion:** {progress_bar(completed_sessions, 36)} ({completed_sessions}/36 sessions)",
        f"- **Configured start:** {data['start_date'] or 'Not set — roadmap uses relative weeks'}",
        "",
        "RAG status: 🔴 Red — not started · 🟠 Amber — learning or needs reinforcement · 🟢 Green — independently demonstrated. **Blocked is tracked separately.**",
        "",
        "## Next session",
        "",
    ]

    next_index = next(
        (index for index, session_id in enumerate(SESSION_IDS) if sessions[session_id]["status"] != "completed"),
        None,
    )
    if next_index is None:
        lines.append("The 36-session first pass is complete. Review S36 evidence before adding sessions.")
    else:
        session_id = SESSION_IDS[next_index]
        week, day_name, _ = session_position(next_index)
        date_text = session_date(parsed_start, next_index)
        suffix = f" · {date_text}" if date_text else ""
        status = SESSION_STATUS[sessions[session_id]["status"]]
        lines.append(
            f"**[{session_id} — {SESSION_TITLES[next_index]}](sessions/{session_id}.md)** · Week {week:02d}, {day_name}{suffix} · {status}"
        )

    lines.extend(
        [
            "",
            "## Category progress",
            "",
            "| Category | Progress | RAG status | Blocked topics |",
            "|---|---:|---|---:|",
        ]
    )
    for category, topics in CATEGORIES.items():
        count = sum(milestone_count(skills[skill_id]) for skill_id in topics)
        blocked = sum(skills[skill_id]["blocked"] for skill_id in topics)
        lines.append(
            f"| {category} | {progress_bar(count, 20)} ({count}/20) | {rag(count, 20)} | {blocked} |"
        )

    lines.extend(["", "## Topic progress", ""])
    for category, topics in CATEGORIES.items():
        lines.extend(
            [
                f"### {category}",
                "",
                "| Topic | Progress | RAG status | E | G | I | D | Blocked |",
                "|---|---:|---|:---:|:---:|:---:|:---:|---|",
            ]
        )
        for skill_id, name in topics.items():
            skill = skills[skill_id]
            count = milestone_count(skill)
            marks = ["✓" if skill["milestones"][key] else "—" for key in MILESTONES]
            blocked = "Yes" if skill["blocked"] else "No"
            lines.append(
                f"| [{skill_id}](SKILLS.md) {name} | {progress_bar(count, 4)} ({count}/4) | {rag(count, 4)} | {' | '.join(marks)} | {blocked} |"
            )
        lines.extend(
            [
                "",
                "E = explain trade-offs · G = apply with guidance · I = apply independently · D = diagnose a failure or validate an edge case.",
                "",
            ]
        )

    lines.extend(
        [
            "## Session completion",
            "",
            "| Week | Monday | Wednesday | Friday |",
            "|---:|---|---|---|",
        ]
    )
    session_symbols = {"not_started": "⬜", "in_progress": "◐", "completed": "✅"}
    for week in range(1, 13):
        cells = []
        for day_index in range(3):
            index = (week - 1) * 3 + day_index
            session_id = SESSION_IDS[index]
            status_key = sessions[session_id]["status"]
            date_text = session_date(parsed_start, index)
            date_suffix = f" ({date_text})" if date_text else ""
            cells.append(
                f"{session_symbols[status_key]} [{session_id}](sessions/{session_id}.md){date_suffix} — {SESSION_STATUS[status_key]}"
            )
        lines.append(f"| {week:02d} | {' | '.join(cells)} |")

    awaiting = []
    for category, topics in CATEGORIES.items():
        for skill_id, name in topics.items():
            skill = skills[skill_id]
            count = milestone_count(skill)
            missing_consolidation = not skill["milestones"]["independent"] or not skill["milestones"]["diagnose"]
            if count and missing_consolidation:
                missing = [
                    label
                    for key, label in MILESTONES.items()
                    if not skill["milestones"][key] and key in {"independent", "diagnose"}
                ]
                awaiting.append((skill_id, name, ", ".join(missing)))

    lines.extend(["", "## Topics awaiting consolidation", ""])
    if not awaiting:
        lines.append("None yet — all topics are not started, so there is no partial evidence to consolidate.")
    else:
        for skill_id, name, missing in awaiting:
            lines.append(f"- **{skill_id} — {name}:** missing {missing} evidence.")

    lines.extend(
        [
            "",
            "## Updating this tracker",
            "",
            "Edit `progress/progress.json` using the evidence rules in `progress/README.md`, then run:",
            "",
            "```bash",
            "python3 scripts/render_progress.py",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="validate and fail if PROGRESS.md is not up to date",
    )
    args = parser.parse_args()

    try:
        rendered = render(load_and_validate())
    except ValueError as exc:
        print(f"progress error: {exc}", file=sys.stderr)
        return 1

    if args.check:
        current = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else ""
        if current != rendered:
            print("PROGRESS.md is out of date; run python3 scripts/render_progress.py", file=sys.stderr)
            return 1
        print("Progress data and PROGRESS.md are valid.")
        return 0

    OUTPUT.write_text(rendered, encoding="utf-8")
    print(f"Rendered {OUTPUT.relative_to(ROOT)} from {SOURCE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

