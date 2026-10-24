# ATLAS AI — Technical Documentation

**Project:** ATLAS AI — Enterprise Knowledge Intelligence Platform  
**Current Stage:** 1.1 — Bronze Data Ingestion  
**Technologies:** Python, Polars, Apache Parquet  
**Dataset:** Olist Brazilian E-Commerce

---

# 1. Introduction to Data Ingestion

## What is data ingestion?

Data ingestion is the process of collecting data from external sources and loading it into a storage system for further processing.

Data can originate from:

- CSV and JSON files
- Relational databases
- REST APIs
- Cloud storage
- Streaming events

### Example in ATLAS AI

We downloaded nine CSV files from the Olist Brazilian E-Commerce dataset.

Our first pipeline will read these files and store their contents in Apache Parquet format.

**Pipeline:**

Olist CSV Files → Polars → Bronze Parquet Files

At this stage, we are not cleaning or transforming business data.

## Why is ingestion necessary?

An enterprise may receive data from hundreds of different sources. A standardized ingestion layer allows engineers to preserve source records, track processing, and prepare data for downstream pipelines.

Our first pipeline is a **batch ingestion pipeline**, meaning it processes an existing collection of files rather than a continuous stream of events.

---

# 2. Medallion Architecture

Medallion Architecture organizes data into layers according to its processing stage.

## Bronze — Raw ingested data

Bronze stores source records with minimal transformation.

For ATLAS AI:

Input: `olist_orders_dataset.csv`

Output: `orders.parquet`

Bronze should preserve original record values and provide source traceability.

We will not remove duplicates, fill missing values, or calculate business metrics in this layer.

## Silver — Cleaned data

Silver contains validated and standardized data.

Future operations may include:

- Checking duplicate business keys
- Validating data types
- Standardizing timestamps
- Handling invalid records
- Checking relationships between tables

## Gold — Business-ready data

Gold contains curated information for analytics and machine learning.

Examples include monthly revenue, product performance, and customer purchasing features.

### Why separate these layers?

Suppose we discover that a cleaning rule was incorrect.

Because Bronze preserves the original data, we can rebuild Silver and Gold without downloading the source dataset again.

This makes the system easier to audit, debug, and reproduce.

---

# 3. CSV vs Apache Parquet

## What is CSV?

CSV stands for Comma-Separated Values.

It is a text-based file format where records are typically stored as rows and fields are separated by commas.

Example:

```text
order_id,order_status
A001,delivered
A002,canceled
```

CSV is simple and widely supported, but it does not inherently preserve rich data types.

## What is Apache Parquet?

Apache Parquet is a columnar storage format designed for efficient analytical processing.

Instead of storing all fields together as text rows, Parquet organizes data by columns within row groups.

### Conceptual example

CSV:

```text
1,25,50000
2,30,60000
3,28,55000
```

Parquet organizes values conceptually as:

```text
ID:     [1, 2, 3]
Age:    [25, 30, 28]
Salary: [50000, 60000, 55000]
```

Actual Parquet files also contain metadata, encoded pages, and column chunks.

## Why use Parquet?

**Columnar storage:** Analytical engines can read selected columns instead of processing every column.

**Compression:** Values of similar types often compress efficiently.

**Data types:** Parquet preserves typed columns, including integers, floating-point values, strings, and timestamps.

**Performance:** Analytical queries can benefit from column pruning and predicate pushdown.

### CSV vs Parquet comparison

| Feature | CSV | Parquet |
|---|---|---|
| Storage | Text-based rows | Columnar binary |
| Compression | External or none | Built-in encoding/compression |
| Data types | Inferred when reading | Stored in schema |
| Human-readable | Yes | No |
| Analytical efficiency | Often lower | Often higher |
| Common usage | Data exchange | Analytical storage |

Parquet is not guaranteed to be faster for every operation, especially for very small files.

---

# 4. Why We Use Polars

Polars is a DataFrame processing library for Python.

It is designed for efficient analytical operations and supports parallel execution.

In ATLAS AI, Polars will be responsible for reading CSV files, inspecting their structure, and writing Parquet files.

## Important Polars concepts

**DataFrame:** A two-dimensional table containing rows and columns.

**Schema:** The names and data types of columns.

**Shape:** The number of rows and columns.

**Null count:** The number of missing values in each column.

**Eager execution:** Operations are executed immediately.

**Lazy execution:** Operations are represented as a query plan and executed when results are requested.

We will begin with eager execution because the Olist dataset is manageable locally.

Later, we can compare eager and lazy processing.

---

# 5. Our First Bronze Ingestion Pipeline

## Input

Directory:

`data/raw/olist/`

Contains nine CSV files covering customers, orders, order items, payments, reviews, products, sellers, geolocation, and product category translations.

## Processing

The ingestion script will:

1. Discover all CSV files.
2. Read each file using Polars.
3. Inspect its shape and schema.
4. Count null values.
5. Identify exact duplicate rows without deleting them.
6. Write the dataset in Parquet format.
7. Report whether ingestion succeeded.

## Output

Directory:

`data/bronze/olist/`

Expected outputs include:

- `customers.parquet`
- `orders.parquet`
- `order_items.parquet`
- `payments.parquet`
- `reviews.parquet`
- `products.parquet`
- `sellers.parquet`
- `geolocation.parquet`
- `category_translation.parquet`

## Important engineering rules

**Preserve source data:** Do not modify original CSV files.

**Avoid accidental data loss:** Verify that input and output row counts match.

**Preserve identifiers:** Some identifiers must remain strings even if they contain digits.

**Handle failures:** Missing files and parsing errors should produce useful error messages.

**Make ingestion repeatable:** Running the pipeline twice should not duplicate records.

**Record metadata:** Track filenames, ingestion timestamps, and processing results.

---

# 6. Current Stage Checklist

- [x] Create ATLAS AI project structure.
- [x] Initialize Git and connect GitHub.
- [x] Download and locate all nine Olist CSV files.
- [ ] Implement CSV discovery.
- [ ] Implement Polars CSV loading.
- [ ] Inspect schemas and row counts.
- [ ] Generate basic data profiling results.
- [ ] Convert CSV files to Parquet.
- [ ] Validate Bronze outputs.
- [ ] Commit the ingestion pipeline.

---

# 7. Current Technical Decisions

| Decision | Choice | Reason |
|---|---|---|
| Initial ingestion | Batch | Source is a static CSV dataset |
| Processing library | Polars | Efficient DataFrame operations |
| Storage format | Parquet | Typed, compressed analytical storage |
| Data architecture | Medallion | Separation of ingestion and cleaning |
| Dependency management | uv | Reproducible Python environment |
| Version control | GitHub | Track source code and documentation |

**Next documentation update:** After implementing the ingestion pipeline, add explanations of Python `pathlib`, CSV schema inference, Parquet writing, duplicate detection, and ingestion metadata.

---

*End of Stage 1.1 documentation — initial version.*

# ATLAS AI — Technical Documentation

**Project:** ATLAS AI — Enterprise Knowledge Intelligence Platform  
**Current Stage:** 1.1 Completed — Initial Data Discovery and Profiling  
**Next Stage:** 1.2 — Bronze Data Ingestion  
**Technologies:** Python, Polars, pathlib, Apache Parquet (planned)  
**Dataset:** Olist Brazilian E-Commerce

---

# 6. Current Stage Checklist

- [x] Create ATLAS AI project structure.
- [x] Initialize Git and connect GitHub.
- [x] Download and locate all nine Olist CSV files.
- [x] Implement CSV discovery using pathlib.
- [x] Load the orders CSV using Polars.
- [x] Inspect schema, shape, and column types.
- [x] Count missing values.
- [x] Validate uniqueness of order IDs.
- [x] Analyze order-status distribution.
- [x] Investigate missing delivery timestamps by status.
- [x] Determine purchase timestamp range.
- [x] Convert timestamp strings to Datetime.
- [x] Verify timestamp parsing.
- [x] Check deliveries occurring before purchases.
- [x] Validate empty and whitespace-only strings.
- [ ] Implement Bronze Parquet writing.
- [ ] Validate Bronze row counts and schema.
- [ ] Add ingestion metadata and repeatability checks.

---

# 7. Current Technical Decisions

| Decision | Choice | Reason |
|---|---|---|
| Initial ingestion | Batch | Static CSV data |
| Processing | Polars | Efficient DataFrame operations |
| Path management | pathlib | Portable filesystem references |
| Initial storage | Apache Parquet | Efficient columnar storage |
| Architecture | Medallion | Separation of raw and curated data |
| Dependencies | uv | Reproducible environments |
| Source preservation | Immutable raw CSVs | Reprocessing and auditability |
| Timestamp parsing | Explicit format | Predictable type conversion |
| Data anomalies | Investigate before modifying | Avoid unnecessary data loss |

---

# 8. Python pathlib and Dataset Discovery

## 8.1 What is pathlib?

`pathlib` is a Python standard-library module that provides an object-oriented interface for interacting with filesystem paths.

It supports operations such as locating directories, checking file existence, joining paths, and discovering files.

## 8.2 Project Root

ATLAS AI determines the project root relative to the location of the ingestion script.

The `__file__` variable references the script's location.

The `resolve()` method creates a resolved absolute path.

The `parents` property provides access to the directories above the file.

In our existing folder structure, `parents[2]` points to the ATLAS AI repository root.

This depends on the script's location and is not automatic project-root discovery.

## 8.3 File Discovery

The `glob()` method identifies files matching a specified pattern.

For example, the pattern `*.csv` identifies files with the CSV extension in the selected directory.

The `sorted()` function provides deterministic ordering.

**ATLAS AI result:** All nine Olist CSV files were successfully discovered.

---

# 9. Polars Data Profiling

## 9.1 What is data profiling?

Data profiling is the process of examining data to understand its structure, completeness, uniqueness, distributions, and potential inconsistencies.

It helps establish data-quality expectations before transformation.

## 9.2 DataFrame inspection

The following Polars operations were used:

| Operation | Purpose |
|---|---|
| `head()` | Preview records |
| `shape` | Return row and column counts |
| `height` | Return row count |
| `columns` | Return column names |
| `schema` | Inspect column types |
| `null_count()` | Count missing values |
| `n_unique()` | Count distinct values |
| `group_by()` | Group records |
| `agg()` | Calculate aggregated metrics |
| `filter()` | Select records matching conditions |

## 9.3 Orders Dataset Profile

| Metric | Actual result |
|---|---:|
| Rows | 99,441 |
| Columns | 8 |
| Unique order IDs | 99,441 |
| Duplicate order IDs | 0 |
| Empty or whitespace-only strings | 0 |

The observed order IDs satisfy the initial uniqueness constraint.

However, uniqueness does not guarantee correctness of the remaining business attributes.

---

# 10. Missing Data and Aggregation

## 10.1 Null values

Null values represent missing or unavailable information.

They should not automatically be classified as errors.

For example, an order that has not been delivered may legitimately have a missing customer-delivery timestamp.

## 10.2 Missing-value results

| Column | Missing values |
|---|---:|
| order_approved_at | 160 |
| order_delivered_carrier_date | 1,783 |
| order_delivered_customer_date | 2,965 |
| Other columns | 0 |

## 10.3 Understanding group_by and agg

`group_by()` divides a dataset into groups based on one or more attributes.

`agg()` computes statistics separately for those groups.

In ATLAS AI, we grouped orders by their status and calculated their total counts and missing delivery timestamps.

## 10.4 Order Status Distribution

| Status | Orders |
|---|---:|
| delivered | 96,478 |
| shipped | 1,107 |
| canceled | 625 |
| unavailable | 609 |
| invoiced | 314 |
| processing | 301 |
| created | 5 |
| approved | 2 |

The dataset is heavily dominated by delivered orders.

This imbalance will be important when defining ML training datasets and evaluation metrics.

## 10.5 Missing Delivery Dates by Status

| Status | Missing dates |
|---|---:|
| shipped | 1,107 |
| canceled | 619 |
| unavailable | 609 |
| invoiced | 314 |
| processing | 301 |
| delivered | 8 |
| created | 5 |
| approved | 2 |

**Key findings:**

- Eight delivered orders have missing customer-delivery timestamps.
- Six canceled orders have recorded customer-delivery timestamps.
- These records require investigation rather than automatic deletion.

---

# 11. Timestamp Parsing and Validation

## 11.1 Why data types matter

CSV files commonly represent timestamp fields as strings.

Strings are suitable for text storage but do not provide native datetime arithmetic.

Converting timestamps to appropriate types enables duration calculations, time-based aggregation, chronological validation, and forecasting features.

## 11.2 Timestamp conversion

ATLAS AI uses Polars to convert five timestamp columns from String to Datetime.

The expected source format is `YYYY-MM-DD HH:MM:SS`.

The `str.strptime()` operation parses a string according to a specified format.

The `with_columns()` operation adds or replaces DataFrame columns.

## 11.3 strict=False

When `strict=False` is used, timestamps that cannot be parsed become null rather than immediately raising an exception.

Therefore, we compare original and converted null counts to identify additional null values introduced by parsing.

**Actual results:**

| Validation | Result |
|---|---:|
| Timestamp parsing failures | 0 |
| Deliveries before purchase | 0 |
| Earliest purchase | 2016-09-04 21:15:19 |
| Latest purchase | 2018-10-17 17:30:18 |

All non-null timestamp strings were parsed successfully.

The datetime fields currently have microsecond precision and no attached timezone.

Chronological validation remains incomplete for other event relationships, such as payment approval and carrier handoff.

---

# 12. Data Quality Engineering Principles

The first profiling stage establishes several engineering principles.

**Completeness:** Identify missing values and determine whether they are expected or anomalous.

**Uniqueness:** Ensure identifiers meet the expected uniqueness constraints.

**Validity:** Verify data types, accepted values, and formatting.

**Consistency:** Check whether related fields agree with business rules.

**Timeliness:** Evaluate date ranges and chronological relationships.

**Traceability:** Preserve source records and record where processed data originated.

For the Bronze layer, anomalies should normally be recorded without changing the source records. Cleaning and standardization belong in the Silver layer.

---

# 13. Next Implementation — Bronze Layer

The next implementation will convert the source CSV datasets into Parquet while preserving their original business records.

The initial workflow will be:

**Raw Olist CSV → Polars ingestion → Bronze Parquet**

The upcoming work includes:

1. Designing the Bronze storage directories.
2. Establishing ingestion metadata.
3. Writing records to Apache Parquet.
4. Verifying input and output row counts.
5. Validating source fidelity.
6. Making ingestion repeatable.
7. Recording ingestion successes and failures.

We will document the actual implementation decisions and results after completing these tasks.

---

**Documentation status:** Updated through Stage 1.1. Bronze persistence has not yet been implemented.