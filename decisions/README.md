# Decision log

Keep decisions brief and append-only. Record choices that would otherwise be mysterious later; routine session notes belong in `sessions/` or `journal/`.

| ID | Date | Decision | Why | Revisit when |
|---|---|---|---|---|
| D-001 | 2026-11-19 | Use a 12-week, 36-session first pass with relative week/day labels. | The cadence is known but the start date is not; relative scheduling avoids false precision. | A start Monday is chosen. |
| D-002 | 2026-11-19 | Use Terraform as primary IaC and introduce CI/CD in the foundation. | Both need repeated use across architectures, not a single late module. | Evidence suggests a second IaC tool is needed. |
| D-003 | 2026-11-19 | Separate demonstrated skill progress from session completion. | Attendance and exposure are not mastery. | Never, unless the evidence model fails in practice. |
| D-004 | 2026-11-19 | Let each subproject own dependencies and infrastructure. | Independent builds should be reproducible without forcing a monorepo-wide stack. | A stable dependency is genuinely shared by multiple projects. |
| D-005 | 2026-11-19 | Pin implementation versions per subproject when work begins, not in this roadmap. | The roadmap should survive software changes; implementation evidence must remain reproducible. | At the start of each build. |
| D-006 | 2026-11-19 | Correct the requested Atwal reading title to the publisher-verified title in `READING.md`. | The authoritative catalogue lists *Practical DataOps*, not the supplied title. | A primary source shows another edition/title. |

For a new decision, add one row with the next ID and link any supporting session artefact.

