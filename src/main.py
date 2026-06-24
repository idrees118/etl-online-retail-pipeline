from extract import load_data
from transform import transform_data
from analytics import create_sales_metric
from schema_validator import validate_schema
from quality_checks import validate_sales_data, validate_returns_data
from load import save_partitioned_sales, save_returns, save_metrics
from logger import get_logger


logger = get_logger("main")


def run_pipeline():

    logger.info("Pipeline started")

    df = load_data()

    validate_schema(df)

    sales_df, return_df = transform_data(df)

    validate_sales_data(sales_df)
    validate_returns_data(return_df)

    metrics_df = create_sales_metric(sales_df)

    save_partitioned_sales(sales_df)
    save_returns(return_df)
    save_metrics(metrics_df)

    logger.info("Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()