import logging
from functools import singledispatch
from typing import Dict

import hydra
from omegaconf import DictConfig, OmegaConf

from lambda_scraper.utils.types import ExecutorMode, Scraper, Producer

logger = logging.getLogger(__name__)


@singledispatch
def run(app_mode, cfg: DictConfig):
    raise NotImplementedError(f"Impossible to Run {app_mode}. Please use any of {list(ExecutorMode)}")


@run.register
def _(app_mode: Producer, params: Dict):
    logger.info("Running producer")


@run.register
def _(app_mode: Scraper, params: Dict):
    logger.info("Running scraper")


@hydra.main(config_path="../config", config_name="config")
def run_app(cfg: DictConfig):
    logger.debug("Debug is printed")
    logger.info(OmegaConf.to_yaml(cfg))
    app_mode = ExecutorMode[cfg.app_mode.upper()]
    print(app_mode)
    run(app_mode, cfg)


if __name__ == "__main__":
    run_app()
