from lambda_scraper.executors.executor import Executor
from omegaconf import DictConfig
from .plugins import Plugins

class SimpleExecutor(Executor):
    def __init__(self, cfg: DictConfig):
        self.config = cfg
        self.mode = cfg.app_mode.name
        self.plugins = Plugins()
    
    def run(self):
        pass
    

