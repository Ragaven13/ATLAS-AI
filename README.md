# ATLAS AI — Enterprise Intelligence Platform

A production-oriented portfolio project combining enterprise data engineering, intelligent document processing, advanced retrieval, knowledge graphs, agent orchestration, and predictive machine learning.

**Current milestone:** Stage 1 — Enterprise Data Foundation.

> This starter contains **documentation and dependency declarations only**. Implementation is intentionally left to the developer.

## Business scenario

ATLAS AI serves a fictional enterprise, **Atlas Commerce**, that needs trustworthy answers across orders, customers, products, sellers, payments, shipping events, and internal documents. The initial structured-data domain uses the public **Olist Brazilian E-Commerce** dataset. Any other public business dataset must remain a separate tenant/domain unless a defensible join exists.

Example future question:

> Why did revenue decline in a particular region last quarter? Examine delivery performance, customer feedback, product categories, and supporting documents, and recommend evidence-backed actions.

## Stage 1 goals

1. Understand source files, business meaning, primary keys, and relationships.
2. Define data contracts, data-quality rules, and privacy boundaries.
3. Profile data for missingness, duplicates, invalid values, and outliers.
4. Design repeatable ingestion and Bronze / Silver / Gold transformations.
5. Plan incremental updates, lineage, and quality reporting.
6. Document decisions and measurable acceptance criteria.

No implementation is supplied: write all processing logic yourself.

## Planned technologies

- **Python 3.12+** with **uv** for environments and dependencies
- **Polars, PyArrow, DuckDB, pandas** for analysis and transformation
- **Pandera, Pydantic** for contracts and schema checks
- **Delta Lake (`deltalake`)** for lakehouse table storage
- **Docling and Presidio** for document extraction and sensitive-data detection in a later Stage 1 extension
- **pytest, Ruff, mypy** for developer-quality checks after you add your own code

Dependencies are grouped into optional feature sets so the first installation stays manageable.

## Getting started with uv

From the extracted project folder:

- Install the base data-engineering environment: `uv sync`
- Include development tooling: `uv sync --extra dev`
- Include document processing later: `uv sync --extra documents`
- Include orchestration later: `uv sync --extra orchestration`
- Select several feature sets: `uv sync --extra dev --extra documents`

`uv` may generate a `uv.lock` when it resolves packages. This starter intentionally does not contain a precomputed lockfile because resolution was not run here.

## Documentation map

| File | Purpose |
| --- | --- |
| `docs/architecture.md` | Boundaries, data flow, layers, and planned services |
| `docs/dataset_strategy.md` | Source systems, domain separation, and acquisition plan |
| `docs/data_contracts.md` | Table-level contracts, keys, and integrity considerations |
| `docs/data_quality.md` | Profiling, validation, quarantine, and acceptance criteria |
| `docs/stage1_roadmap.md` | Step-by-step Stage 1 learning and implementation milestones |
| `docs/decisions.md` | Architecture decision record template |

## Non-goals of this starter

No Python source code, example functions, notebooks, tests, Git files, GitHub Actions, infrastructure configuration, generated data, or prewritten ingestion pipeline.

## Dataset reference

Olist Brazilian E-Commerce Public Dataset (Kaggle): https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Respect the dataset's published license/terms and avoid committing raw customer identifiers or other sensitive files publicly.
