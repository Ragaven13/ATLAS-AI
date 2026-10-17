# Architecture Decision Log

Record important implementation choices here as you make them. The entries below are **questions**, not pre-made decisions.

## ADR template

- **ID / Date:**
- **Decision title:**
- **Context / problem:**
- **Options considered:**
- **Chosen approach:**
- **Rationale and trade-offs:**
- **Consequences / risks:**
- **How to revisit the decision:**

## Decisions to consider first

1. Local filesystem vs object storage for initial Bronze datasets.
2. Parquet vs Delta Lake at each stage of the prototype.
3. Polars vs SQL/DuckDB responsibilities.
4. How to define canonical order revenue without double counting.
5. Handling of duplicates, nulls, and invalid timestamps.
6. Required freshness and when streaming is justified.
