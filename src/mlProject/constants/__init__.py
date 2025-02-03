from pathlib import Path
from mlProject import logger

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
SCHEMA_FILE_PATH = Path("schema.yaml")

logger.info(f"Loaded constants. CONFIG_FILE_PATH={CONFIG_FILE_PATH}")
