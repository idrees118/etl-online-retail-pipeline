import pandas as pd


sales = pd.read_parquet("data/output/sales.parquet")
returns = pd.read_parquet("data/output/returns.parquet")
metrics = pd.read_parquet("data/output/sales_metrics.parquet")


print("SALES")
print(sales.head())

print("\nRETURNS")
print(returns.head())

print("\nMETRICS")
print(metrics.head())