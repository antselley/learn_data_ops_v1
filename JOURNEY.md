# Journey overview

## North star

Build the judgement and repeatable habits needed to help a technically capable, mission-driven startup establish its first useful data platform: inexpensive enough to sustain, pleasant to develop, safe to change, and directly connected to decisions and outcomes.

Excellence here means being able to explain a choice, implement it, repeat it independently, and diagnose its failure modes. It also means recognising when the available data, sample size, organisational capacity, or likely benefit cannot justify a more complex system.

## Cadence

- Active sessions: Monday, Wednesday, Friday mornings
- Time box: 2–3 hours, including notes and cleanup
- Optional reading: roughly two 20–30 minute blocks per week
- First pass: 12 weeks / 36 sessions
- Dates: relative by default; optional `start_date` in `progress/progress.json`
- Beyond week 12: add sessions only in response to evidence, gaps, or a purposeful project

Every session has a defensible stopping point. Unfinished work is recorded, not silently expanded into the next time box. Consolidation sessions can absorb catch-up, but their first purpose is retrieval, repetition, and diagnosis.

## How the sequence works

1. **Foundation (weeks 1–2):** requirements, Terraform, reproducible local tooling, remote state design, identity, CI, teardown, and a first independent repeat.
2. **Reliable data delivery (weeks 3–4):** contracts, incremental ingestion, connector choices, replay, reconciliation, DuckDB/Parquet, SQL/dbt, and quality.
3. **Mission decisions and Azure serving (weeks 5–6):** outcomes, equity, funnels, capacity, unit economics, experiments, batch serving, promotion, recovery, and total cost.
4. **Compute and architecture choice (weeks 7–8):** standalone Spark, execution behaviour, cross-engine comparison, Databricks trade-offs, connectors, and consolidation.
5. **Applied ML and MLOps (weeks 9–10):** baselines, action-aligned metrics, validation, leakage, reproducibility, MLflow, batch promotion, drift, rollback, and retraining criteria.
6. **Synthesis (weeks 11–12):** forecasting judgement, an end-to-end platform design, an independent rebuild, causal evaluation, troubleshooting, evidence review, and the next pass.

The roadmap reuses a familiar service-delivery domain where that avoids incidental learning. A later session can select an open or synthetic dataset suited to the specific outcome. Five use-case families recur throughout:

- mission outcomes and reach;
- service delivery and capacity;
- engagement, retention, and segmentation;
- financial sustainability and resource allocation;
- experimentation and evaluation.

## Architecture practice loop

Each architecture should be evaluated through the same lens:

`requirements → provision → authenticate → deploy → observe → recover → cost → teardown`

Requirements include freshness, volume, concurrency, sensitivity, reporting/serving paths, recovery needs, and budget. Cost includes infrastructure, licences, and maintenance effort. Teardown must protect designated persistent data and Terraform state. A managed feature is valuable only when its operational benefit justifies cost, coupling, and loss of portability.

The planned architectures deliberately vary:

- local containerised tooling with synthetic data;
- DuckDB and Parquet as a low-cost analytical platform;
- Azure storage, networking, identity, batch compute, and serving;
- standalone Spark outside Databricks;
- Azure Databricks as a managed alternative;
- connector patterns spanning managed, self-managed, and Python-native tools;
- reproducible batch ML with MLflow and monitored predictions.

## Evidence and mastery

Every topic has four milestones:

1. explain the concept and its trade-offs;
2. apply it with guidance;
3. apply it independently in another context;
4. diagnose a failure or validate a meaningful edge case.

One artefact may support several milestones, but a milestone is recorded only when its evidence genuinely demonstrates it. Repetition alone is exposure, not proof. Green status requires all four milestones with linked evidence. See [`PROGRESS.md`](PROGRESS.md) for the current state and [`progress/README.md`](progress/README.md) for the update workflow.

## Learning-session rhythm

A useful 2–3 hour session normally includes:

- 10 minutes: retrieve the relevant concept and inspect prerequisites;
- 15 minutes: state a hypothesis, design choice, or expected failure mode;
- 80–120 minutes: build, compare, test, or diagnose;
- 20 minutes: capture observable evidence and explain the trade-off;
- 10 minutes: clean up safely and identify the smallest next step.

Future tutoring should preserve active learning: ask for choices and predictions, offer scaffolding and hints, and provide deeper implementation help when requested.

