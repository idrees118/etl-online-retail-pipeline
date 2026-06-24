import pandas as pd


def validate_sales_data(df: pd.DataFrame):

    # 1. Empty check
    if df.empty:
        raise ValueError("Sales dataset is empty")

    # 2. Required columns check
    required_cols = ["InvoiceNo", "Quantity", "UnitPrice", "Revenue", "Country"]

    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    # 3. Negative revenue check
    if (df["Revenue"] < 0).any():
        raise ValueError("Negative revenue detected")

    # 4. Null country check
    if df["Country"].isnull().any():
        raise ValueError("Null Country values found")

    print("Sales data validation passed")
    return True


def validate_returns_data(df: pd.DataFrame):

    if df.empty:
        print("Warning: Returns dataset is empty")

    if "Quantity" in df.columns:
        if (df["Quantity"] >= 0).any():
            raise ValueError("Returns dataset contains non-negative quantities")

    print("Returns data validation passed")
    return True