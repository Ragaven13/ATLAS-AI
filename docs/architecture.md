# Stage 1 Architecture — Enterprise Data Foundation

## Scope

Build an auditable data foundation for Atlas Commerce. Stage 1 feeds future RAG, GraphRAG, analytics agents, and predictive models but does **not** implement those systems yet.

## Logical flow

Source files and events → Source inventory and metadata → Ingestion → Bronze (immutable raw snapshots) → Profiling and validation → Silver (typed, standardized, deduplicated records) → Gold (business-oriented analytical tables and metrics) → downstream consumers.

Quarantine invalid records with clear reasons; record quality metrics and transformations in a run-level audit trail.

## Layers

**Bronze**: Preserve input payloads, source filenames, ingestion timestamps, and batch IDs. Ensure replayability and idempotent ingestion.

**Silver**: Type conversions, normalized timestamps, primary/foreign-key checks, explicit duplicate rules, missing-value policies, and currency conventions. Keep rejected records auditable rather than silently dropping them.

**Gold**: Carefully defined metrics and dimensional tables. For example, orders by day/region, delivery-delay summaries, seller performance, and product-category reporting. Document metric grain, eligible statuses, and refund handling.

## Interfaces to later stages

- Search/document pipelines consume permissions and canonical document metadata.
- Agents query approved Gold models, not arbitrary operational tables.
- Graph construction consumes stable entity IDs and documented relationship edges.
- ML consumes point-in-time-correct features and versioned training snapshots.

## Design questions to resolve

1. Which file is authoritative for each field?
2. What uniquely identifies a record across repeated runs?
3. How do changes, deletes, and late-arriving events propagate downstream?
4. Which columns identify people or businesses, and who may access them?
5. Which business metrics require returns, cancellations, or refunds to be handled explicitly?
6. How will a downstream answer trace back to source rows and processing runs?

## Out of scope (for now)

Kafka, Airflow, Azure deployment, Qdrant, Neo4j, agents, and predictive model serving are later milestones. Avoid premature service complexity.
