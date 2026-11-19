# Progress data

`progress.json` is the human-editable source of truth for demonstrated skill and session status. `PROGRESS.md` is generated; do not edit it by hand.

## Update workflow

1. Finish or pause a session and save its observable artefacts in the repository (or use a durable external URL).
2. Set that session’s `status` to `in_progress` or `completed` and add evidence paths/links.
3. For each genuinely demonstrated skill milestone, add one or more evidence paths/links to its array:
   - `explain`: your own explanation applied to trade-offs;
   - `guided`: a working application completed with scaffolding or help;
   - `independent`: an application in another context with materially less guidance;
   - `diagnose`: a failure diagnosis or meaningful edge-case validation.
4. Set `blocked` independently when progress is blocked and use `note` to say why. Blocked does not change RAG colour.
5. Update the session’s detailed reflection in `sessions/Sxx.md`.
6. Regenerate and validate:

   ```bash
   python3 scripts/render_progress.py
   ```

The renderer rejects unknown/missing topics, sessions, milestones, statuses, empty evidence strings, and an invalid start date. Set `start_date` to the ISO date of the Week 1 Monday when known, for example `2027-01-11`; leave it `null` otherwise.

## Calculation

- Topic progress = milestone arrays with at least one evidence link / 4.
- Category progress = completed milestones across its five topics / 20.
- Overall skill progress = completed milestones across all 25 topics / 100.
- Session progress = sessions marked `completed` / 36 and is shown separately.
- 🔴 Red = zero milestones; 🟠 Amber = one to three; 🟢 Green = all four with evidence.
- “Awaiting consolidation” means the topic has begun but still lacks independent application or diagnosis/edge-case evidence.

Existing experience starts at zero intentionally. Add it through the same evidence-backed assessment rather than changing a percentage directly.

