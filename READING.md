# Optional reading guide

Reading supports active work; it does not replace it. Aim for two short blocks of roughly 20–30 minutes per week. Skim for the question shown, stop when the time box ends, and record only insights that change a design or experiment.

## Verified books and title note

- *[The DevOps Handbook, Second Edition](https://itrevolution.com/product/the-devops-handbook-second-edition/)*, Gene Kim, Jez Humble, Patrick Debois, John Willis, and Nicole Forsgren (IT Revolution, 2021). The publisher confirms the edition, authors, and six-part structure; its [official excerpt and contents](https://itrevolution.com/wp-content/uploads/2022/06/DOHB2_Excerpt.pdf) can be used to check chapter/part names.
- The requested “*DataOps: A Modern Approach to Data Analytics*, by Harvinder Atwal” does not match the title in the publisher catalogue. The verified book is *[Practical DataOps: Delivering Agile Data Science at Scale](https://link.springer.com/book/10.1007/978-1-4842-5104-1)*, Harvinder Atwal (Apress, 2020; first published December 2019). This guide uses the publisher-listed section names: “The Problem with Data Science,” “Data Strategy,” “Lean Thinking,” “Agile Collaboration,” “Build Feedback and Measurement,” “Building Trust,” “DevOps for DataOps,” “Organizing for DataOps,” “DataOps Technology,” and “The DataOps Factory.”

Do not rely on chapter numbers from another edition. The named parts/sections below were checked against those publisher sources on 2026-11-19.

## Version-resilient documentation rule

Links favour official landing or concept pages. At implementation time, record the selected tool/runtime version and date in the relevant subproject, then use that version’s documentation. Re-check changing connector features, Azure service capabilities, Databricks runtimes, authentication guidance, and prices when making a real decision.

<a id="week-01"></a>
## Week 1 — Flow, IaC, and reproducibility

**Block A:** *The DevOps Handbook*, Part I, “The Three Ways.” Ask: how do flow, feedback, and continual learning alter the design of a one-person or small-team platform?

**Block B:** [Terraform on Azure overview](https://developer.hashicorp.com/terraform/tutorials/azure-get-started), [AzureRM backend](https://developer.hashicorp.com/terraform/language/backend/azurerm), and a skim of [Python dependency-management guidance](https://packaging.python.org/en/latest/tutorials/managing-dependencies/). Ask: what is needed to reproduce both infrastructure and the local toolchain, and what creates the bootstrap dependency?

<a id="week-02"></a>
## Week 2 — Identity and delivery

**Block A:** *The DevOps Handbook*, Part III, especially the named themes “Create the Foundations of Our Deployment Pipeline,” “Enable Fast and Reliable Automated Testing,” and “Enable and Practice Continuous Integration.” Ask: what is the smallest useful feedback path?

**Block B:** Microsoft’s [workload identity federation concepts](https://learn.microsoft.com/entra/workload-id/workload-identity-federation), [Azure RBAC overview](https://learn.microsoft.com/azure/role-based-access-control/overview), and [network security for Azure Storage](https://learn.microsoft.com/azure/storage/common/storage-network-security). Ask: which trust, role, scope, and network condition must all be true for access?

<a id="week-03"></a>
## Week 3 — Contracts, increments, and feedback

**Block A:** *Practical DataOps*, “Build Feedback and Measurement” and “Building Trust.” Ask: what feedback proves a data product is both correct enough and useful?

**Block B:** Skim official concepts for [Fivetran syncs](https://fivetran.com/docs/core-concepts/sync-overview), [Airbyte incremental append](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/incremental-append), and [dlt incremental loading](https://dlthub.com/docs/general-usage/incremental-loading). Ask: what state is stored, and what happens to updates, deletes, late records, and retries? Verify the exact source connector later.

<a id="week-04"></a>
## Week 4 — Local analytics and modelling discipline

**Block A:** [DuckDB’s Parquet overview](https://duckdb.org/docs/stable/data/parquet/overview) and [dbt project best practices](https://docs.getdbt.com/best-practices). Ask: which file/model organisation improves real work, and which is ceremony at this scale?

**Block B:** *Practical DataOps*, “DataOps Technology.” Ask: how should technology selection support feedback, flow, trust, and self-service rather than become the strategy?

<a id="week-05"></a>
## Week 5 — Value and mission measures

**Block A:** *Practical DataOps*, “Data Strategy” and “Lean Thinking.” Ask: what is the shortest value path from data to an improved mission decision?

**Block B:** *The DevOps Handbook*, Part II, “Where to Start,” especially its value-stream and visible-work themes. Apply the reading to service activity, outcomes, equity, capacity, and unit cost—not only software delivery.

<a id="week-06"></a>
## Week 6 — Experiments, batch architecture, and low-risk change

**Block A:** *The DevOps Handbook*, Part III’s low-risk release themes, plus the Azure Well-Architected Framework’s [cost optimisation principles](https://learn.microsoft.com/azure/well-architected/cost-optimization/principles). Ask: how do reversibility and total cost change the architecture?

**Block B:** [Statsmodels power and sample-size tools](https://www.statsmodels.org/stable/stats.html#power-and-sample-size-calculations) and Azure Architecture Center’s [batch processing guidance](https://learn.microsoft.com/azure/architecture/data-guide/technology-choices/batch-processing). Ask: what cannot the proposed sample or platform support, and what smaller learning objective remains useful?

<a id="week-07"></a>
## Week 7 — Spark outside the managed notebook

**Block A:** Select the implementation version from the [Apache Spark documentation index](https://spark.apache.org/documentation), then read its Quick Start and [submitting applications](https://spark.apache.org/docs/latest/submitting-applications.html) guidance. Ask: what runs in the driver, what is packaged, and what changes outside local mode?

**Block B:** The selected version’s [Spark web UI](https://spark.apache.org/docs/latest/web-ui.html) and [SQL performance tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html) sections. Ask: what observation would support a shuffle, skew, partition, or join hypothesis?

<a id="week-08"></a>
## Week 8 — Managed platforms and connector ownership

**Block A:** Azure Databricks [architecture overview](https://learn.microsoft.com/azure/databricks/getting-started/overview) and the [pricing system table reference](https://learn.microsoft.com/azure/databricks/administration-guide/system-tables/pricing). Ask: which managed capability removes work the team would otherwise own? Refresh actual Azure prices separately before spending.

**Block B:** Revisit the exact Fivetran, Airbyte, and dlt connector pages selected in S23; use their navigation from the official sources in week 3. Ask: how do historical sync, delete capture, schema change, retry, and maintenance differ for this source rather than for the product in general?

<a id="week-09"></a>
## Week 9 — Valid ML and reproducible experiments

**Block A:** Scikit-learn’s [model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html), [grouped cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators-for-grouped-data), and [time-series split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html). Ask: which split and metric reproduce the future decision setting?

**Block B:** MLflow’s [tracking](https://mlflow.org/docs/latest/ml/tracking/) and [model registry](https://mlflow.org/docs/latest/registry/) documentation. Ask: what must be recorded to recreate the evaluation, not merely reload a model object?

<a id="week-10"></a>
## Week 10 — Promotion, feedback, and recovery

**Block A:** MLflow’s [model registry workflow](https://mlflow.org/docs/latest/ml/model-registry/workflow/) and [model evaluation](https://mlflow.org/docs/latest/ml/evaluation) guidance. Ask: which measurable gates allow promotion, rejection, and rollback?

**Block B:** *The DevOps Handbook*, Part IV, “The Second Way: The Technical Practices of Feedback.” Apply production telemetry and feedback ideas to batch predictions, delayed outcomes, partial publication, and degraded models.

<a id="week-11"></a>
## Week 11 — Forecasts and platform synthesis

**Block A:** Revisit scikit-learn’s [time-series split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html) and the Azure Architecture Center [data architecture guide](https://learn.microsoft.com/azure/architecture/data-guide/). Ask: what forecast horizon, service level, and serving path correspond to the operational decision?

**Block B:** *Practical DataOps*, “DevOps for DataOps” and “The DataOps Factory.” Ask: how should reproducibility, delivery, self-service, and operating ownership appear in the end-to-end design?

<a id="week-12"></a>
## Week 12 — Learning system and next pass

**Block A:** *The DevOps Handbook*, Part V, “The Third Way: The Technical Practices of Continual Learning and Experimentation.” Ask: how will incidents and independent repetitions change shared practice rather than remain private lessons?

**Block B:** *Practical DataOps*, “Organizing for DataOps.” Ask: what is the smallest ownership model a mission-driven startup can sustain, and which capabilities should remain deliberately absent for now?

## How to record useful reading

Put a short note in the relevant session reflection or a journal entry:

- the source and named section;
- one idea that changed a choice;
- one disagreement or contextual limit;
- one experiment or check prompted by the reading.

Do not mark a skill milestone from reading alone. Reading can support the “explain” evidence only when accompanied by your own trade-off explanation applied to a concrete context.

