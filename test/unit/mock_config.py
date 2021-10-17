from omegaconf import DictConfig
from hydra import compose, initialize_config_dir
from lambda_scraper.utils.types import ExecutorMode
import pytest
import logging
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
logger = logging.getLogger(__name__)

def load_config(app_mode):
    config_path = ROOT_DIR / "config"
    if (config_path / "config.yaml").is_file():
        with initialize_config_dir(config_dir=str(config_path), job_name="test_app"):
            cfg = compose(config_name="config", overrides=[f"app_mode={app_mode}"])
            return cfg
    else:
        raise FileNotFoundError(f"No config file found to create MockConfig. Expected file: {config_path}")


def mock_config():
    logger.warning("You are using default config. This dep_config is based on Scraper app_mode")
    return load_config(ExecutorMode.SCRAPER)

def mock_config_scraper():
    return load_config(ExecutorMode.SCRAPER)

def mock_config_producer():
    return load_config(ExecutorMode.PRODUCER)