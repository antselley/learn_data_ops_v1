#!/usr/bin/env python3
"""Run structural checks for the learning-journey repository."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SESSION_IDS = [f"S{number:02d}" for number in range(1, 37)]
EXPECTED_PREFIXES = {"DEV", "ARC", "ING", "OUT", "ML"}
REQUIRED_SESSION_HEADINGS = (
    "## Desired outcomes",
    "## Observable evidence",
    "## Optional preparation",
    "## Stopping point",
    "## Reflection",
    "## Next step",
)


def check(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def section(text: str, heading: str) -> str:
    match = re.search(
        rf"^{re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)", text, flags=re.MULTILINE | re.DOTALL
    )
    return match.group(1) if match else ""


def main() -> int:
    errors: list[str] = []
    skills_text = (ROOT / "SKILLS.md").read_text(encoding="utf-8")
    category_headings = re.findall(r"^## \d+\. (.+)$", skills_text, re.MULTILINE)
    check(len(category_headings) == 5, f"Expected 5 skill categories, found {len(category_headings)}", errors)

    skill_rows = re.findall(r"^\| ((?:DEV|ARC|ING|OUT|ML)-\d{2}) \|", skills_text, re.MULTILINE)
    skill_counts = Counter(skill_rows)
    check(len(skill_counts) == 25, f"Expected 25 unique skill topics, found {len(skill_counts)}", errors)
    check(all(count == 1 for count in skill_counts.values()), "A skill row appears more than once", errors)
    prefix_counts = Counter(skill_id.split("-")[0] for skill_id in skill_counts)
    check(set(prefix_counts) == EXPECTED_PREFIXES, f"Unexpected skill prefixes: {prefix_counts}", errors)
    check(all(prefix_counts[prefix] == 5 for prefix in EXPECTED_PREFIXES), f"Expected 5 topics per category: {prefix_counts}", errors)

    session_files = sorted((ROOT / "sessions").glob("S??.md"))
    check([path.stem for path in session_files] == SESSION_IDS, "Expected session files S01 through S36", errors)
    mapped_skills: Counter[str] = Counter()
    declared_session_skills: dict[str, set[str]] = {}
    days_by_week: dict[int, set[str]] = {week: set() for week in range(1, 13)}

    for index, session_id in enumerate(SESSION_IDS):
        path = ROOT / "sessions" / f"{session_id}.md"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for heading in REQUIRED_SESSION_HEADINGS:
            check(heading in text, f"{session_id} missing {heading}", errors)
        check("- **Status:** Not started" in text, f"{session_id} initial status is not Not started", errors)

        when = re.search(r"^- \*\*When:\*\* Week (\d{2}), (Monday|Wednesday|Friday)$", text, re.MULTILINE)
        check(bool(when), f"{session_id} has invalid When field", errors)
        if when:
            week = int(when.group(1))
            day = when.group(2)
            expected_week = index // 3 + 1
            expected_day = ("Monday", "Wednesday", "Friday")[index % 3]
            check((week, day) == (expected_week, expected_day), f"{session_id} should be Week {expected_week:02d}, {expected_day}", errors)
            if week in days_by_week:
                days_by_week[week].add(day)

        skill_line = re.search(r"^- \*\*Skills:\*\* (.+)$", text, re.MULTILINE)
        check(bool(skill_line), f"{session_id} missing Skills field", errors)
        declared: set[str] = set()
        if skill_line:
            declared = set(re.findall(r"(?:DEV|ARC|ING|OUT|ML)-\d{2}", skill_line.group(1)))
            check(bool(declared), f"{session_id} declares no recognised skills", errors)
            check(declared <= set(skill_counts), f"{session_id} declares unknown skills {sorted(declared - set(skill_counts))}", errors)
            mapped_skills.update(declared)
        declared_session_skills[session_id] = declared

        prerequisite_line = re.search(r"^- \*\*Prerequisites:\*\* (.+)$", text, re.MULTILINE)
        check(bool(prerequisite_line), f"{session_id} missing Prerequisites field", errors)
        if prerequisite_line:
            for prior in re.findall(r"S\d{2}", prerequisite_line.group(1)):
                check(int(prior[1:]) < int(session_id[1:]), f"{session_id} prerequisite {prior} is not earlier", errors)

        outcome_lines = re.findall(r"^\d+\. ", section(text, "## Desired outcomes"), re.MULTILINE)
        check(1 <= len(outcome_lines) <= 3, f"{session_id} should have 1–3 outcomes, found {len(outcome_lines)}", errors)
        evidence_lines = re.findall(r"^- ", section(text, "## Observable evidence"), re.MULTILINE)
        check(bool(evidence_lines), f"{session_id} has no observable evidence bullets", errors)
        check(bool(section(text, "## Stopping point").strip()), f"{session_id} has no stopping point", errors)
        check(bool(section(text, "## Reflection").strip()), f"{session_id} has no reflection field", errors)
        check(bool(section(text, "## Next step").strip()), f"{session_id} has no next-step field", errors)

    for week, days in days_by_week.items():
        check(days == {"Monday", "Wednesday", "Friday"}, f"Week {week:02d} does not contain Monday, Wednesday, Friday", errors)
    check(set(mapped_skills) == set(skill_counts), f"Unmapped topics: {sorted(set(skill_counts) - set(mapped_skills))}", errors)

    for row in skills_text.splitlines():
        row_match = re.match(r"^\| ((?:DEV|ARC|ING|OUT|ML)-\d{2}) \|.*\| (\[S\d{2}.*) \|$", row)
        if not row_match:
            continue
        skill_id = row_match.group(1)
        linked_sessions = re.findall(r"\[(S\d{2})\]", row_match.group(2))
        check(bool(linked_sessions), f"{skill_id} has no planned session links", errors)
        for session_id in linked_sessions:
            check(skill_id in declared_session_skills.get(session_id, set()), f"SKILLS.md maps {skill_id} to {session_id}, but the session does not declare it", errors)

    progress = json.loads((ROOT / "progress" / "progress.json").read_text(encoding="utf-8"))
    check(progress.get("start_date") is None, "Initial start_date must be null", errors)
    check(set(progress.get("skills", {})) == set(skill_counts), "Progress skill IDs differ from SKILLS.md", errors)
    check(set(progress.get("sessions", {})) == set(SESSION_IDS), "Progress sessions differ from S01–S36", errors)
    for skill_id, value in progress.get("skills", {}).items():
        check(value.get("blocked") is False, f"{skill_id} must initially be unblocked", errors)
        check(all(not evidence for evidence in value.get("milestones", {}).values()), f"{skill_id} must initially have no milestone evidence", errors)
    for session_id, value in progress.get("sessions", {}).items():
        check(value.get("status") == "not_started", f"{session_id} must initially be not_started", errors)
        check(not value.get("evidence"), f"{session_id} must initially have no evidence", errors)

    reading = (ROOT / "READING.md").read_text(encoding="utf-8")
    anchors = re.findall(r'<a id="week-(\d{2})"></a>', reading)
    check(anchors == [f"{week:02d}" for week in range(1, 13)], "READING.md must have week-01 through week-12 anchors", errors)
    check(reading.count("**Block A:**") == 12, "READING.md must have 12 Block A entries", errors)
    check(reading.count("**Block B:**") == 12, "READING.md must have 12 Block B entries", errors)

    markdown_files = list(ROOT.glob("*.md")) + list(ROOT.glob("*/*.md"))
    link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall(text):
            target = raw_target.strip().strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target_path = unquote(target.split("#", 1)[0])
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            check(resolved.exists(), f"Broken relative link in {path.relative_to(ROOT)}: {raw_target}", errors)

    check((ROOT / "projects" / "README.md").exists(), "Missing subprojects parent/conventions", errors)
    check((ROOT / "AGENTS.md").exists(), "Missing AGENTS.md", errors)

    if errors:
        print("Repository validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Repository validation passed:")
    print("- 5 categories and 25 topics (5 per category)")
    print("- 36 sessions across 12 Monday/Wednesday/Friday weeks")
    print("- all topics mapped; all prerequisites point backward")
    print("- every session has 1–3 outcomes, evidence, stopping point, status, reflection, and next step")
    print("- initial progress is honest and all relative Markdown links resolve")
    print("- 12 weeks each have two optional reading blocks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

