from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "data" / "output"


def save_partitioned_sales(df: pd.DataFrame):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for country, group in df.groupby("Country"):
        safe_country = str(country).replace(" ", "_")
        path = OUTPUT_DIR / f"sales_country={safe_country}.parquet"
        group.to_parquet(path, index=False)


def save_returns(df: pd.DataFrame):
    path = OUTPUT_DIR / "returns.parquet"
    df.to_parquet(path, index=False)


def save_metrics(df: pd.DataFrame):
    path = OUTPUT_DIR / "metrics.parquet"
    df.to_parquet(path, index=False)