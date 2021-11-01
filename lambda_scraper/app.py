import logging

import hydra
from omegaconf import DictConfig, OmegaConf

from lambda_scraper.producer.executor import Producer
from lambda_scraper.scraper.executor import Scraper
from lambda_scraper import recipe

logger = logging.getLogger(__name__)

AppMode = {"PRODUCER": Producer, "SCRAPER": Scraper}


def format_config(cfg: DictConfig) -> DictConfig:
    """ Clean field possibly overriden by user"""
    cfg.app_mode = cfg.app_mode.upper()
    cfg.task = cfg.task.lower()
    return cfg


@hydra.main(config_path="../config", config_name="config")
def run_app(cfg: DictConfig):
    logger.debug("Debug is printed")
    logger.info(OmegaConf.to_yaml(cfg))
    
    cfg = format_config(cfg)
    executor = AppMode[cfg.app_mode.upper()](cfg)
    print(list(recipe.Tasks))
    ctx = recipe.context(recipe.Tasks[cfg.task].value)
    executor.run(ctx)


if __name__ == "__main__":
    run_app()
