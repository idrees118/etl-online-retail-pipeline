import pandas as pd
def create_sales_metric(sales_df:pd.DataFrame):
    country_sales = (
        sales_df.groupby("Country").agg(
            total_revenue =('Revenue', 'sum'),
            total_orders =('InvoiceNo', 'nunique'),
            total_quantity=('Quantity', 'sum')

        )
        .reset_index()
    )
    return country_sales