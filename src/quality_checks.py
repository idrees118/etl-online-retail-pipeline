def validate_sales_data(df):

    # 1. No negative price
    if (df["UnitPrice"] < 0).any():
        raise ValueError("Negative UnitPrice found")

    # 2. No zero or negative quantity
    if (df["Quantity"] <= 0).any():
        raise ValueError("Invalid Quantity found")

    # 3. Missing CustomerID (soft warning)
    if df["CustomerID"].isna().any():
        print("WARNING: Missing CustomerID values exist")

    print("Sales data validation passed")

def validate_returns_data(df):

    # returns must always be negative
    if (df["Quantity"] >= 0).any():
        raise ValueError("Returns dataset contains invalid non-negative quantities")

    print("Returns data validation passed")    