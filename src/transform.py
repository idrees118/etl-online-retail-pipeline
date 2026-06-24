import pandas as pd

def transform_data(df: pd.DataFrame):
    df_clean = df.copy()

    # 1. Fix datatypes
    df_clean['InvoiceDate'] = pd.to_datetime(df_clean['InvoiceDate'])
    # Fix customer ID
    df_clean['CustomerID'] = df_clean["CustomerID"].astype('Int64')

    # 2. Handle missing values

    df_clean["Description"] = df_clean["Description"].fillna("Unknown")
    
    # 3. Remove invalid prices
    df_clean = df_clean[df_clean['UnitPrice'] >=0]

    # 4. Split business logic
    sales_df = df_clean[df_clean["Quantity"] > 0].copy()
    return_df = df_clean[df_clean["Quantity"] < 0].copy()

    # 5. Feature Engineering
    sales_df["Revenue"] = sales_df["Quantity"] * sales_df['UnitPrice']

    return sales_df, return_df

if __name__ == "__main__":
    from extract import df # temporary import (we’ll improve later)
    sales, returns = transform_data(df)

    print(sales.head())
    print(returns.head())