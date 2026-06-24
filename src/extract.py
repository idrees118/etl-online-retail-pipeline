from pathlib import Path
import pandas as pd
from config import load_config


BASE_DIR = Path(__file__).resolve().parent.parent


def load_data():

    config = load_config()

    file_path = BASE_DIR / config["paths"]["raw_data"]

    df = pd.read_csv(
        file_path,
        encoding="ISO-8859-1"
    )

    return df