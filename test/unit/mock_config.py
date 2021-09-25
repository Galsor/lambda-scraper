from omegaconf import DictConfig
from hydra import compose, initialize_config_dir

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]


class MockConfig(DictConfig):
    def __new__(cls):
        config_path = ROOT_DIR / "config"
        if (config_path / "config.yaml").is_file():
            with initialize_config_dir(config_dir=str(config_path), job_name="test_app"):
                cfg = compose(config_name="config")
                return cfg
        else:
            raise FileNotFoundError(f"No config file found to create MockConfig. Expected file: {config_path}")
