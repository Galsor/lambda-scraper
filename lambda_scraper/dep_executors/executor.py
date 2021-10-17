from abc import ABC, abstractmethod

from hydra.core.singleton import Singleton
from omegaconf import DictConfig

from lambda_scraper.utils.types import ExecutorMode


class BaseExecutor(ABC, metaclass=Singleton):
    mode: ExecutorMode
    config: DictConfig

    @abstractmethod
    def run(self) -> None:
        """Run the dep_recipes loaded"""
        ...
