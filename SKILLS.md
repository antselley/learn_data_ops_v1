# Skills map

The catalogue has five fixed categories and five topics per category. IDs are stable: do not rename them when tools change. The topic description defines the capability; the session links show planned exposure and assessment opportunities, not automatic milestone credit.

## 1. IaC, DevOps & DataOps

| ID | Topic | Capability boundary | Planned sessions |
|---|---|---|---|
| DEV-01 | Terraform and remote state | Bootstrap state infrastructure; use remote state and locking; separate environments; detect drift; recreate and safely tear down infrastructure while protecting state and persistent data. | [S01](sessions/S01.md), [S03](sessions/S03.md), [S06](sessions/S06.md), [S33](sessions/S33.md) |
| DEV-02 | Azure identity and secrets | Explain control/data-plane access; use least privilege, managed identities or workload federation for CI; keep credentials out of code; reason about permissions across storage, network, compute, and serving. | [S03](sessions/S03.md), [S04](sessions/S04.md), [S05](sessions/S05.md), [S17](sessions/S17.md), [S33](sessions/S33.md) |
| DEV-03 | Local tooling and automated tests | Reproduce dependencies; use containers where valuable; provide useful developer commands, automated tests, and synthetic data; link code, configuration, and dependencies to evidence. | [S02](sessions/S02.md), [S27](sessions/S27.md), [S33](sessions/S33.md) |
| DEV-04 | CI/CD and environment promotion | Validate code and Terraform early; authenticate without long-lived secrets; promote versioned artefacts and data safely across environments; gate releases and practise independent deployment. | [S05](sessions/S05.md), [S06](sessions/S06.md), [S18](sessions/S18.md), [S28](sessions/S28.md), [S33](sessions/S33.md) |
| DEV-05 | Monitoring, recovery, and rollback | Observe freshness, volume, failures, cost, and service behaviour; recover partial publication; roll back deployments/models; define recovery evidence and operational ownership. | [S09](sessions/S09.md), [S18](sessions/S18.md), [S22](sessions/S22.md), [S30](sessions/S30.md), [S35](sessions/S35.md) |

## 2. Azure Architecture & Compute

| ID | Topic | Capability boundary | Planned sessions |
|---|---|---|---|
| ARC-01 | Storage, networking, and access | Translate freshness, volume, concurrency, sensitivity, recovery, and cost needs into storage/network boundaries, access paths, and supported reporting or serving paths. | [S01](sessions/S01.md), [S04](sessions/S04.md), [S17](sessions/S17.md), [S32](sessions/S32.md) |
| ARC-02 | DuckDB and Parquet | Build and assess a low-cost analytical path using portable files, efficient layout, local/server execution, and a supported reporting interface. | [S10](sessions/S10.md), [S11](sessions/S11.md), [S21](sessions/S21.md) |
| ARC-03 | Azure batch compute and serving | Choose and operate affordable Azure batch compute and data-serving paths, including scheduling, identity, networking, concurrency, recovery, and scale-to-zero trade-offs. | [S17](sessions/S17.md), [S18](sessions/S18.md), [S32](sessions/S32.md) |
| ARC-04 | Standalone Spark and performance tuning | Run PySpark locally and with `spark-submit`; relate local and distributed execution; inspect plans/UI; diagnose shuffles, skew, partitioning, and join strategies. | [S19](sessions/S19.md), [S20](sessions/S20.md), [S21](sessions/S21.md), [S35](sessions/S35.md) |
| ARC-05 | Azure Databricks and cost trade-offs | Compare managed and self-managed capabilities, performance, developer experience, managed-feature dependencies, licensing/compute cost, and maintenance effort. | [S21](sessions/S21.md), [S22](sessions/S22.md), [S32](sessions/S32.md) |

## 3. Ingestion & Analytics Engineering

| ID | Topic | Capability boundary | Planned sessions |
|---|---|---|---|
| ING-01 | Source discovery and data contracts | Discover source semantics and ownership; document freshness, volume, deletes, schema evolution, sensitivity, consumers, and contract/reconciliation expectations. | [S01](sessions/S01.md), [S07](sessions/S07.md), [S23](sessions/S23.md), [S32](sessions/S32.md) |
| ING-02 | Incremental loads and CDC | Choose keys/watermarks or log-based change capture; handle updates/deletes/schema changes; make loads idempotent; support replay, backfill, and reconciliation. | [S08](sessions/S08.md), [S09](sessions/S09.md), [S23](sessions/S23.md), [S35](sessions/S35.md) |
| ING-03 | Fivetran, Airbyte, and dlt | Compare managed connectors, self-managed connector platforms, and Python-native ingestion by source coverage, incremental semantics, operations, licensing, and maintenance. | [S08](sessions/S08.md), [S23](sessions/S23.md), [S32](sessions/S32.md) |
| ING-04 | SQL modelling and dbt | Compare plain SQL with dbt for testing, documentation, dependencies, environments, collaboration, and total complexity; choose deliberately. | [S10](sessions/S10.md), [S11](sessions/S11.md), [S12](sessions/S12.md), [S21](sessions/S21.md) |
| ING-05 | Data quality, replay, and backfills | Define actionable quality controls; quarantine or publish safely; diagnose partial failure; replay deterministically; backfill without corrupting current results. | [S09](sessions/S09.md), [S12](sessions/S12.md), [S35](sessions/S35.md) |

## 4. Mission Outcomes & Experimentation

| ID | Topic | Capability boundary | Planned sessions |
|---|---|---|---|
| OUT-01 | Decision discovery and metric design | Start from a decision and action; distinguish activity, outcome, prediction, and causal impact; define ownership, grain, denominators, missingness, and decision latency. | [S01](sessions/S01.md), [S07](sessions/S07.md), [S13](sessions/S13.md), [S32](sessions/S32.md) |
| OUT-02 | Reach, outcomes, and equity | Measure who is reached and who benefits; expose missing outcomes and appropriate denominators; segment carefully without overstating small samples. | [S13](sessions/S13.md), [S16](sessions/S16.md), [S34](sessions/S34.md) |
| OUT-03 | Funnels, cohorts, and segmentation | Define journeys and cohorts; measure engagement/retention; select useful segments; recognise bias, unstable slices, and unsupported conclusions. | [S14](sessions/S14.md), [S34](sessions/S34.md) |
| OUT-04 | Capacity and unit economics | Connect demand, service delivery, capacity, cost, and financial sustainability; make resource-allocation trade-offs visible. | [S15](sessions/S15.md), [S31](sessions/S31.md), [S32](sessions/S32.md) |
| OUT-05 | Experiment design and causal evaluation | Define hypotheses, assignment, guardrails, estimands, power limits, and analysis; distinguish experiments from observational evaluation and prediction. | [S16](sessions/S16.md), [S34](sessions/S34.md), [S36](sessions/S36.md) |

## 5. Applied ML & MLOps

| ID | Topic | Capability boundary | Planned sessions |
|---|---|---|---|
| ML-01 | Regression, classification, and forecasting | Refresh core models through action-oriented problems; establish simple baselines first; choose a problem form that matches the operational decision. | [S25](sessions/S25.md), [S31](sessions/S31.md), [S34](sessions/S34.md) |
| ML-02 | Validation, leakage, and baselines | Match metrics to action; use time/entity-aware validation; build point-in-time-correct features; detect leakage; reject conclusions unsupported by data or sample size. | [S25](sessions/S25.md), [S26](sessions/S26.md), [S31](sessions/S31.md), [S34](sessions/S34.md) |
| ML-03 | MLflow tracking and model registry | Reproduce training from linked data, code, configuration, and dependencies; track experiments; version and compare models with meaningful lineage. | [S27](sessions/S27.md), [S30](sessions/S30.md), [S33](sessions/S33.md) |
| ML-04 | Batch scoring and model promotion | Produce versioned batch predictions; gate promotion on evaluation; deploy safely; retain rollback paths; describe what online inference would change. | [S28](sessions/S28.md), [S30](sessions/S30.md), [S33](sessions/S33.md) |
| ML-05 | Drift, performance, and retraining | Join predictions to eventual outcomes; distinguish data drift, prediction drift, and measured degradation; set investigation, retraining, and retirement criteria. | [S29](sessions/S29.md), [S30](sessions/S30.md), [S35](sessions/S35.md), [S36](sessions/S36.md) |

## Coverage interpretation

The roadmap offers multiple encounters for every topic, including independent repetition and failure/edge-case work. Actual milestone status lives in `progress/progress.json`. A planned diagnostic session does not earn a diagnostic milestone until the evidence shows that the failure was understood or the edge case meaningfully validated.

