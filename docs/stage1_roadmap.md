# Stage 1 Implementation Roadmap (No Code Provided)

## Milestone 1 — Source understanding

Review the Olist dataset, record each source file and business grain, sketch primary/foreign keys, and capture observed row counts and null patterns.

**Deliverable:** source inventory and initial entity relationship diagram.

## Milestone 2 — Contracts and profiling

Write schema expectations and data-quality rules; profile nulls, duplicates, dates, and monetary distributions. Decide which exceptions are acceptable.

**Deliverable:** data contracts and baseline quality report.

## Milestone 3 — Ingestion design

Choose ingestion interfaces and naming conventions. Track input checksums, ingest timestamps, run IDs, and source versions. Decide retry/idempotency behavior.

**Deliverable:** repeatable raw ingestion, written and implemented independently.

## Milestone 4 — Bronze and Silver

Store replayable raw copies; build explicit type conversions and deterministic cleaning steps; quarantine invalid rows.

**Deliverable:** curated tables and auditable exception outputs.

## Milestone 5 — Gold models

Define safe order-level and seller-level metrics. Avoid double-counting due to one-to-many joins. Verify totals against sources.

**Deliverable:** documented analytical tables and business queries.

## Milestone 6 — Incremental and operational quality

Implement change detection, late-arrival handling, observability, test coverage, and lineage. Compare incremental results with a full refresh.

**Deliverable:** reproducible Stage 1 pipeline with measured data-quality outcomes.

## Definition of done

- New developer can reproduce the pipeline from documented source data.
- Each curated field and business metric has a clear definition.
- Invalid data and partial failures are visible, not silently ignored.
- Full and incremental processing are consistent.
- Execution and validation results are recorded and reviewable.
