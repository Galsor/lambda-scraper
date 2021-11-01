import logging

from omegaconf import DictConfig

from lambda_scraper.utils.types import BaseExecutor

logger = logging.getLogger(__name__)

class Producer(BaseExecutor):
    def __init__(self, cfg: DictConfig):
        self.cfg = cfg

    def run(self, context):
        logger.debug(context)
