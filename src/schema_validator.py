from schema import REQUIRED_COLUMNS


def validate_schema(df):
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]

    if missing:
        raise ValueError(f"Missing columns: {missing}")

    print("Schema validation passed")