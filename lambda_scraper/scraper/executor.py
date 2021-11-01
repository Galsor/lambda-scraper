from omegaconf import DictConfig

from lambda_scraper.utils.types import BaseExecutor

class Scraper(BaseExecutor):

    def __init__(self, cfg:DictConfig):
        self.cfg = cfg
        
    def run(self, context):
        pass


