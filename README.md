# Affordable Data Platforms Learning Journey

This repository is a 12-week practice system for becoming excellent at building useful, affordable data platforms for mission-driven organisations. It assumes strong data engineering foundations and concentrates on the harder surrounding work: infrastructure, delivery, identity, architecture, operations, experimentation, and MLOps.

The aim is not to collect tools. It is to develop judgement: what a small organisation needs now, what can wait, what will cost money or attention, and how to leave behind a platform that another engineer can understand and operate.

## First pass at a glance

- 12 relative weeks; Monday, Wednesday, and Friday mornings
- 36 active sessions of 2–3 hours
- Terraform from the start, then reused across architectures
- CI/CD, recovery, cost, and teardown practised repeatedly
- five skill categories and 25 evidence-based topics
- optional reading in two short blocks per week
- independent repetition, failure diagnosis, consolidation, and catch-up

No start date is required. When useful, set `start_date` in [`progress/progress.json`](progress/progress.json) to an ISO date; the roadmap remains expressed as relative weeks and weekdays.

## Start here

1. Read the [`journey overview`](JOURNEY.md) and [`skills map`](SKILLS.md).
2. Open the [`36-session roadmap`](ROADMAP.md).
3. Begin with [`S01 — Define the platform target`](sessions/S01.md).
4. After a session, add links or paths to evidence in [`progress/progress.json`](progress/progress.json), update the session note, then regenerate the tracker:

   ```bash
   python3 scripts/render_progress.py
   ```

5. Review the generated [`progress tracker`](PROGRESS.md) before choosing the next session.

Progress is based on demonstrated evidence, not time spent or repeated exposure. Existing experience can be credited later when it is connected to evidence.

## Repository map

| Path | Purpose |
|---|---|
| [`JOURNEY.md`](JOURNEY.md) | Learning principles, cadence, architecture thread, and first-pass shape |
| [`SKILLS.md`](SKILLS.md) | Stable 25-topic catalogue and session traceability |
| [`ROADMAP.md`](ROADMAP.md) | 12-week sequence and links to all 36 session records |
| [`sessions/`](sessions/) | Outcomes, evidence, stopping points, status, and reflections |
| [`READING.md`](READING.md) | Optional, stage-relevant reading in manageable blocks |
| [`progress/progress.json`](progress/progress.json) | Human-editable source of truth for progress |
| [`PROGRESS.md`](PROGRESS.md) | Generated visual tracker |
| [`decisions/`](decisions/) | Brief architecture and learning decisions |
| [`journal/`](journal/) | Cross-session retrospectives and learning notes |
| [`projects/`](projects/) | Future independent subprojects and their conventions |
| [`scripts/`](scripts/) | Small repository maintenance scripts |

## Boundaries

This setup provisions nothing and installs nothing. Cloud deployments, paid services, credentials, and remote repositories are deliberately deferred. Each future subproject may own its dependencies, infrastructure, tests, and documentation; shared resources should only be introduced after two or more projects have a genuine common need.

