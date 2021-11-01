from os import PathLike
from omegaconf import DictConfig
from hydra import compose, initialize
import pytest
import logging
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
CONFIG_FILENAME = 'test_config.yaml'
logger = logging.getLogger(__name__)



def load_config(app_mode:str, tmp_path:PathLike) -> DictConfig:

    with initialize(config_path="../../config"):
        cfg = compose(config_name="config", 
                    overrides=[
                        f"app_mode={app_mode}",
                        f"environment.db.filepath={tmp_path}"
                    ])
    return cfg

@pytest.fixture(scope="session")
def database_path(tmpdir_factory)-> PathLike:
    db_path = tmpdir_factory.mktemp("data").join("database.json")
    print(db_path)
    return db_path


@pytest.fixture(scope="session")
def mock_config_scraper(database_path) -> DictConfig:
    return load_config("SCRAPER", database_path)


@pytest.fixture(scope="session")
def mock_config_producer(database_path) -> DictConfig:
    return load_config("PRODUCER", database_path)
