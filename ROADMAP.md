# 12-week roadmap

This is the navigation view. Each linked session record contains prerequisites, concrete outcomes, evidence, reading, stopping point, status, and reflection. Prerequisites always refer to earlier sessions; “complete or explicitly defer” allows a catch-up decision without pretending the missing evidence exists.

## Weeks 1–4 — foundations and reliable data delivery

| ID | When | Title | Skills | Prerequisites | Outcome summary |
|---|---|---|---|---|---|
| [S01](sessions/S01.md) | W01 Mon | Define the platform target | DEV-01, ARC-01, ING-01, OUT-01 | None | Turn a mission decision into bounded platform requirements and an IaC-first learning target. |
| [S02](sessions/S02.md) | W01 Wed | Reproducible local developer loop | DEV-03 | S01 | Specify a reproducible environment, commands, tests, container boundary, and synthetic data strategy. |
| [S03](sessions/S03.md) | W01 Fri | Terraform bootstrap and state | DEV-01, DEV-02 | S01 | Explain and design bootstrap, remote state, locking, permissions, environments, drift, and protected teardown. |
| [S04](sessions/S04.md) | W02 Mon | Azure boundaries and access | DEV-02, ARC-01 | S01, S03 | Explain why identities can or cannot traverse storage, network, and control/data-plane boundaries. |
| [S05](sessions/S05.md) | W02 Wed | CI and workload identity | DEV-02, DEV-04 | S02–S04 | Design fast checks and secretless CI authentication with scoped promotion. |
| [S06](sessions/S06.md) | W02 Fri | Independent sandbox repetition | DEV-01, DEV-04 | S03, S05 | Recreate and tear down a sandbox from version-controlled infrastructure with less guidance. |
| [S07](sessions/S07.md) | W03 Mon | Discover sources and decisions | ING-01, OUT-01 | S01 | Produce a source/decision contract covering semantics, ownership, sensitivity, deletes, and consumers. |
| [S08](sessions/S08.md) | W03 Wed | Incremental ingestion choices | ING-02, ING-03 | S07 | Compare incremental/CDC semantics and select a managed, self-managed, or Python-native approach. |
| [S09](sessions/S09.md) | W03 Fri | Partial-failure recovery lab | DEV-05, ING-02, ING-05 | S08 | Diagnose an introduced failure and demonstrate idempotent replay and reconciliation. |
| [S10](sessions/S10.md) | W04 Mon | DuckDB and Parquet path | ARC-02, ING-04 | S02, S07 | Define a low-cost transformation and reporting path with observable performance evidence. |
| [S11](sessions/S11.md) | W04 Wed | Plain SQL versus dbt | ARC-02, ING-04 | S10 | Compare equivalent modelling workflows and justify whether dbt’s structure earns its cost. |
| [S12](sessions/S12.md) | W04 Fri | Quality, replay, and backfill | ING-04, ING-05 | S09–S11 | Add quality gates and plan a safe historical backfill; consolidate weeks 3–4 or catch up. |

## Weeks 5–8 — mission judgement and architecture choice

| ID | When | Title | Skills | Prerequisites | Outcome summary |
|---|---|---|---|---|---|
| [S13](sessions/S13.md) | W05 Mon | Reach, outcomes, and equity | OUT-01, OUT-02 | S07 | Define honest mission measures with denominators, missing outcomes, and equity slices. |
| [S14](sessions/S14.md) | W05 Wed | Funnels, cohorts, and segments | OUT-03 | S13 | Build defensible engagement/retention definitions and identify unsupported segment claims. |
| [S15](sessions/S15.md) | W05 Fri | Capacity and unit economics | OUT-04 | S13 | Connect demand, throughput, constraints, cost, and resource allocation in a decision model. |
| [S16](sessions/S16.md) | W06 Mon | Experiments and causal limits | OUT-02, OUT-05 | S13–S15 | Design an evaluation and state what sample size, missingness, or assignment cannot support. |
| [S17](sessions/S17.md) | W06 Wed | Azure batch and serving design | DEV-02, ARC-01, ARC-03 | S04, S10 | Choose an identity-aware batch compute and reporting/serving path against requirements. |
| [S18](sessions/S18.md) | W06 Fri | Promote, recover, and cost | DEV-04, DEV-05, ARC-03 | S05, S09, S17 | Rehearse promotion/recovery and compare infrastructure, licence, and maintenance cost. |
| [S19](sessions/S19.md) | W07 Mon | PySpark beyond Databricks | ARC-04 | S02, S10 | Run the same PySpark job in local mode and via `spark-submit`; explain distributed differences. |
| [S20](sessions/S20.md) | W07 Wed | Spark plans and bottlenecks | ARC-04 | S19 | Use plans and the Spark UI to investigate shuffles, skew, partitioning, and joins. |
| [S21](sessions/S21.md) | W07 Fri | Cross-engine comparison | ARC-02, ARC-04, ARC-05, ING-04 | S11, S19, S20 | Compare one workload in DuckDB, standalone Spark, and Databricks; identify portable and managed parts. |
| [S22](sessions/S22.md) | W08 Mon | Databricks value and lock-in | DEV-05, ARC-05 | S18, S21 | Evaluate managed features, operability, performance, portability, and total cost under two scenarios. |
| [S23](sessions/S23.md) | W08 Wed | Connector decision lab | ING-01, ING-02, ING-03 | S08, S12 | Compare Fivetran, Airbyte, and dlt for increments, deletes, schema change, cost, and ownership. |
| [S24](sessions/S24.md) | W08 Fri | Architecture consolidation | DEV-05, ARC-01, ING-05 | S18, S20, S23 | Retrieve and troubleshoot a prior architecture; use remaining time for explicit catch-up. |

## Weeks 9–12 — applied ML, operations, and synthesis

| ID | When | Title | Skills | Prerequisites | Outcome summary |
|---|---|---|---|---|---|
| [S25](sessions/S25.md) | W09 Mon | Baselines before models | ML-01, ML-02 | S13 | Frame an actionable regression/classification problem and beat—or retain—a simple baseline honestly. |
| [S26](sessions/S26.md) | W09 Wed | Validation and leakage | ML-02 | S25 | Build time/entity-aware validation and point-in-time features; expose a leakage path. |
| [S27](sessions/S27.md) | W09 Fri | Reproducible MLflow runs | DEV-03, ML-03 | S02, S26 | Reproduce evaluation from recorded data, code, configuration, dependencies, and tracked runs. |
| [S28](sessions/S28.md) | W10 Mon | Batch scoring and promotion | DEV-04, ML-04 | S05, S27 | Create versioned batch predictions and a measurable promotion gate with a rollback target. |
| [S29](sessions/S29.md) | W10 Wed | Outcomes and drift | ML-05 | S26, S28 | Join predictions to eventual outcomes and distinguish data, prediction, and performance change. |
| [S30](sessions/S30.md) | W10 Fri | ML failure and rollback | DEV-05, ML-03, ML-04, ML-05 | S27–S29 | Independently diagnose a failed model release, roll back, and set retrain/retire criteria. |
| [S31](sessions/S31.md) | W11 Mon | Forecasting with constraints | OUT-04, ML-01, ML-02 | S15, S25, S26 | Evaluate a forecast against a capacity action, baseline, uncertainty, and data limitations. |
| [S32](sessions/S32.md) | W11 Wed | End-to-end platform design | ARC-01, ARC-03, ARC-05, ING-01, ING-03, OUT-01, OUT-04 | S17, S22, S23, S31 | Produce a costed, operable platform design with supported serving paths and explicit non-goals. |
| [S33](sessions/S33.md) | W11 Fri | Independent rebuild | DEV-01, DEV-02, DEV-03, DEV-04, ML-03, ML-04 | S06, S28, S32 | Rebuild and promote a bounded path with less guidance, preserving reproducibility and teardown safety. |
| [S34](sessions/S34.md) | W12 Mon | Evaluation synthesis | OUT-02, OUT-03, OUT-05, ML-01, ML-02 | S16, S26, S31 | Choose among reporting, prediction, experiment, or causal evaluation for a mission decision. |
| [S35](sessions/S35.md) | W12 Wed | Troubleshooting consolidation | DEV-05, ARC-04, ING-02, ING-05, ML-05 | S24, S30 | Diagnose a cross-layer incident and validate recovery; use remaining time for evidence gaps. |
| [S36](sessions/S36.md) | W12 Fri | Evidence review and next pass | OUT-05, ML-05 | S33–S35 | Audit evidence, avoid unearned milestones, identify consolidation needs, and shape the next sessions. |

## After the first pass

Keep the stable skill IDs and evidence model. Add sessions after S36 only to close a demonstrated gap, deepen a mission/scientific use case, or build a deliberately different architecture. Likely neuroscience or mental-health extensions should first address governance, sensitivity, missing outcomes, repeated measures, entity-aware validation, and the difference between prediction and causal or clinical claims.

