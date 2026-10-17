# Data Quality and Cleaning Plan

## Profiling dimensions

**Completeness:** missing cells by field and group; distinguish legitimately absent timestamps from malformed records.

**Uniqueness:** duplicates by declared grain; distinguish duplicate file ingestion from genuine repeated business events.

**Validity:** types, ranges, status enums, malformed dates, amounts, and inconsistent timezone representations.

**Consistency:** cross-table reconciliations (orders, items, payments), contradictory status/timestamp combinations, location/category inconsistencies.

**Integrity:** missing references, orphan items, unmatched sellers or products, and unexplained join inflation.

**Freshness:** lag from source event to stored table; late arrivals and stale snapshots.

## Cleaning principles

1. Never overwrite the raw source without preserving the original.
2. Profile first; do not impute missing values automatically.
3. For every cleaning rule, log the affected row count and reasoning.
4. Distinguish hard failures, quarantined rows, and warnings.
5. Prefer deterministic, repeatable transformations.
6. Track dataset and transformation versions.
7. Never let a future observation leak into historical ML features.

## Suggested measurable acceptance checks

- All processed rows trace to a source file and processing run.
- No duplicates in tables with declared unique keys.
- Referential integrity checks have documented exceptions.
- Re-running unchanged inputs yields identical curated results.
- Rejected records retain an explainable rejection reason.
- Aggregate metrics have reconciliation checks and clear financial definitions.

**Do not claim specific thresholds or passing results before measuring the data.** Set quality targets after profiling and explicitly record exceptions.
