from pathlib import Path
import yaml


BASE_DIR = Path(__file__).resolve().parent.parent


def load_config():

    config_path = BASE_DIR / "config" / "config.yaml"

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    return config