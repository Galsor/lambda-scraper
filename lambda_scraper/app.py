import logging

import hydra
from omegaconf import DictConfig, OmegaConf

from lambda_scraper.scraper.executor import Scraper
from lambda_scraper.producer.executor import Producer

logger = logging.getLogger(__name__)

AppMode = {"PRODUCER": Producer, "SCRAPER": Scraper}

def format_config(cfg:DictConfig) -> DictConfig:
    cfg.app_mode=cfg.app_mode.upper()
    return cfg


@hydra.main(config_path="../config", config_name="config")
def run_app(cfg: DictConfig):
    logger.debug("Debug is printed")
    logger.info(OmegaConf.to_yaml(cfg))
    
    cfg = format_config(cfg)

    executor = AppMode[cfg.app_mode.upper()](cfg)
    executor.run()


if __name__ == "__main__":
    run_app()
