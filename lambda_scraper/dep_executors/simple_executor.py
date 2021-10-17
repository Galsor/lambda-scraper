from omegaconf import DictConfig

from lambda_scraper.dep_executors.executor import Executor

from .plugins import Plugins


class SimpleExecutor(Executor):
    def __init__(self, cfg: DictConfig):
        self.config = cfg
        self.mode = cfg.app_mode.name
        self.plugins = Plugins()

    def run(self):
        pass
