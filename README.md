# ETL Pipeline – Online Retail Data

A modular ETL pipeline built in Python that processes raw retail transaction data, validates it against a schema, separates sales from returns, computes country-level metrics, and writes partitioned Parquet output — one file per country.

---

## Project Structure

```
etl-online-retail-pipeline/
├── config/
│   └── config.yaml          # Paths and pipeline settings
├── data/
│   ├── raw/
│   │   └── OnlineRetail.csv # Raw input dataset
│   └── output/
│       ├── sales.parquet
│       ├── returns.parquet
│       ├── metrics.parquet
│       ├── sales_metrics.parquet
│       └── sales_country=*.parquet  # Partitioned by country (38 countries)
├── logs/
│   └── pipeline.log         # Full execution log
└── src/
    ├── main.py              # Pipeline entry point
    ├── extract.py           # Load raw CSV
    ├── transform.py         # Clean and engineer features
    ├── validate.py          # Row-level validation
    ├── quality_checks.py    # Dataset-level quality checks
    ├── schema.py            # Column schema definitions
    ├── schema_validator.py  # Schema enforcement
    ├── analytics.py         # Country-level aggregations
    ├── load.py              # Write Parquet output
    ├── config.py            # Config loader
    ├── logger.py            # Logging setup
    └── check_output.py      # Verify output files
```

---

## How the Pipeline Works

**1. Extract** (`extract.py`) — Reads `OnlineRetail.csv` into a Pandas DataFrame. No changes at this stage.

**2. Transform** (`transform.py`) — Fixes date types, handles missing `CustomerID` and `Description`, computes `Revenue = Quantity × UnitPrice`, and splits the data into sales and returns.

**3. Validate** (`validate.py`, `quality_checks.py`, `schema_validator.py`) — Enforces schema, checks that prices are positive, quantities are valid, and flags bad rows before anything is saved. This is the layer that prevents bad data from reaching the output.

**4. Analytics** (`analytics.py`) — Aggregates clean sales data by country: total revenue, total orders, total quantity sold.

**5. Load** (`load.py`) — Saves output as Parquet. Sales data is partitioned by country, so each country gets its own file — 38 countries total. This mirrors how real data lakes store data for efficient querying.

---

## Output Files

| File | Contents |
|---|---|
| `sales.parquet` | All clean sales transactions |
| `returns.parquet` | Isolated return transactions |
| `metrics.parquet` / `sales_metrics.parquet` | Country-level aggregated metrics |
| `sales_country=X.parquet` | Sales partitioned per country (38 files) |

---

## How to Run

```bash
git clone https://github.com/idrees118/etl-online-retail-pipeline.git
cd etl-online-retail-pipeline
pip install -r requirements.txt
python src/main.py
```

Raw data goes in `data/raw/`. Output lands in `data/output/`. Logs are written to `logs/pipeline.log`.

---

## Tech Stack

Python · Pandas · PyArrow · PyYAML · Logging

---

## Dataset

UCI Online Retail Dataset — transactions from a UK-based online retailer (Dec 2010 – Dec 2011).  
Source: https://archive.ics.uci.edu/ml/datasets/online+retail

---

## Author

**Muhammad Idrees** — Aspiring Data Engineer  
GitHub: https://github.com/idrees118
