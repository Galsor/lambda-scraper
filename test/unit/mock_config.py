from omegaconf import DictConfig
from hydra import compose, initialize_config_dir, initialize
from lambda_scraper.utils.types import ExecutorMode
import pytest
import logging
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
CONFIG_FILENAME = 'test_config.yaml'
logger = logging.getLogger(__name__)


#TODO: Fix config upload.
# might be due to python version (Hydra suffers issues with 3.10)
def load_config(app_mode):

    with initialize(config_path="../../config"):
        cfg = compose(config_name="config", overrides=[f"app_mode={app_mode}"])
        return cfg

    return cfg


def mock_config():
    logger.warning("You are using default config. This dep_config is based on Scraper app_mode")
    return load_config("SCRAPER")


def mock_config_scraper():
    return load_config("SCRAPER")


def mock_config_producer():
    return load_config("PRODUCER")
