<div align="center">

# 🛒 ETL Pipeline — Online Retail Data

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/Parquet-Output%20Format-009CAB?style=for-the-badge&logo=apache&logoColor=white"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge"/>
</p>

<p>
A production-style, modular ETL pipeline that ingests messy raw retail transaction data,<br/>
enforces schema, validates quality, separates sales from returns, computes country-level metrics,<br/>
and writes partitioned Parquet output — <strong>one file per country across 38 countries.</strong>
</p>

</div>

---

## 🔄 Pipeline Flow

```
┌─────────────┐    ┌───────────────┐    ┌──────────────────┐    ┌─────────────┐    ┌─────────────┐
│   EXTRACT   │ →  │   TRANSFORM   │ →  │ VALIDATE/QUALITY │ →  │  ANALYTICS  │ →  │    LOAD     │
│             │    │               │    │                  │    │             │    │             │
│ Read raw    │    │ Fix types     │    │ Schema check     │    │ Aggregate   │    │ Write       │
│ CSV into    │    │ Compute       │    │ Row-level rules  │    │ by country  │    │ Parquet     │
│ DataFrame   │    │ Revenue col   │    │ Dataset checks   │    │ Revenue     │    │ Partitioned │
│             │    │ Split Sales/  │    │ Log bad rows     │    │ Orders      │    │ by country  │
│             │    │ Returns       │    │                  │    │ Quantity    │    │             │
└─────────────┘    └───────────────┘    └──────────────────┘    └─────────────┘    └─────────────┘
```

---

## 📂 Project Structure

```
etl-online-retail-pipeline/
│
├── 📁 config/
│   └── config.yaml              # All file paths and settings (nothing hardcoded)
│
├── 📁 data/
│   ├── raw/
│   │   └── OnlineRetail.csv     # Raw input — 541,909 transactions
│   └── output/
│       ├── sales.parquet            # All clean sales
│       ├── returns.parquet          # Isolated returns
│       ├── metrics.parquet          # Aggregated metrics
│       ├── sales_metrics.parquet    # Country-level business metrics
│       └── sales_country=*.parquet  # 38 country-partitioned files
│
├── 📁 logs/
│   └── pipeline.log             # Full execution log with timestamps
│
└── 📁 src/
    ├── main.py                  # Orchestrates the full pipeline
    ├── extract.py               # Ingestion layer
    ├── transform.py             # Core transformation logic
    ├── schema.py                # Column and type definitions
    ├── schema_validator.py      # Schema enforcement
    ├── validate.py              # Row-level validation
    ├── quality_checks.py        # Dataset-level quality checks
    ├── analytics.py             # Business metric aggregations
    ├── load.py                  # Parquet writer with partitioning
    ├── config.py                # Config loader
    ├── logger.py                # Centralized logging
    └── check_output.py          # Output verification
```

---

## 🔍 What Each Module Does

### 📥 `extract.py` — Ingestion
Reads `OnlineRetail.csv` into a Pandas DataFrame with proper encoding handling. Zero transformation at this stage — raw data only.

---

### ⚙️ `transform.py` — Core Logic
The most important module in the pipeline. It:
- Converts `InvoiceDate` from raw string → proper `datetime`
- Drops rows where both `CustomerID` and `Description` are missing
- Computes a new column: **`Revenue = Quantity × UnitPrice`**
- Splits the dataset into two clean DataFrames:
  - ✅ **Sales** — positive quantities, valid invoices
  - 🔁 **Returns** — negative quantities or invoice codes starting with `C`

---

### 🧱 `schema.py` + `schema_validator.py` — Schema Layer
`schema.py` defines the expected columns and their data types.  
`schema_validator.py` enforces them — if a required column is missing or has the wrong type, the pipeline catches it before the data goes any further.

---

### ✅ `validate.py` — Row-Level Validation
Checks every row before it reaches output:
- `UnitPrice` must be greater than zero
- `Quantity` must be a valid positive integer (for sales)
- Rows with missing `CustomerID` are **flagged and logged**, not silently dropped

---

### 🔎 `quality_checks.py` — Dataset-Level Checks
Runs after transformation across the full dataset:
- No duplicate invoice records
- All revenue values are non-negative
- Sales and returns split is clean with no overlap

---

### 📊 `analytics.py` — Business Metrics
Aggregates the clean sales data by country and computes:
- 💰 Total Revenue
- 📦 Total Orders
- 🔢 Total Quantity Sold

Covers **38 countries** from the UK to Australia, Japan, Brazil, and beyond.

---

### 💾 `load.py` — Output Writer
Saves all results as **Parquet** (not CSV) because:
- Columnar format — much faster to query
- Preserves data types — no re-parsing on load
- Industry standard in Spark, Athena, BigQuery, Databricks

Sales data is written **partitioned by country**, so downstream tools can query a single country without scanning the full file.

---

### 🛠️ Supporting Modules

| Module | Role |
|---|---|
| `main.py` | Runs the full pipeline in order: extract → transform → validate → analytics → load |
| `logger.py` | Centralized logger — writes to both console and `logs/pipeline.log` |
| `config.py` | Loads `config.yaml` so paths and settings are never hardcoded |
| `check_output.py` | Reads output Parquet files post-run and prints summary to verify correctness |

---

## 📤 Output Files

| File | Description |
|---|---|
| `sales.parquet` | Clean, validated sales transactions |
| `returns.parquet` | Isolated return transactions |
| `sales_metrics.parquet` | Country-level revenue, orders, quantity |
| `sales_country=X.parquet` | Sales partitioned per country — 38 files total |

---

## 🗃️ Dataset

**UCI Online Retail Dataset**  
541,909 transactions from a UK-based non-store online retailer between December 2010 and December 2011.  
🔗 https://archive.ics.uci.edu/ml/datasets/online+retail

---

## 🧰 Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.12 | Core language |
| Pandas | Data loading, cleaning, transformation |
| PyArrow | Parquet read/write |
| PyYAML | Config file parsing |
| Logging | Execution tracking |

---

<div align="center">

## 👤 Author

**Muhammad Idrees**  
Aspiring Data Engineer  
🔗 [github.com/idrees118](https://github.com/idrees118)

</div>
