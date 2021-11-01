from abc import ABC, abstractmethod
from enum import Enum

from omegaconf import DictConfig


class BaseTask(ABC):
    pass


class BaseExecutor(ABC):
    """Abstract class for runnable application such as Producer and Scraper"""

    cfg: DictConfig

    @abstractmethod
    def run(self, cfg: DictConfig, context):
        ...
