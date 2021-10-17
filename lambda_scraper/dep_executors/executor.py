from abc import ABC, abstractmethod

from hydra.core.singleton import Singleton
from omegaconf import DictConfig

from ..utils.types import ExecutorMode
from .plugins import Plugins


class Executor(ABC, metaclass=Singleton):
    mode: ExecutorMode
    plugins: Plugins
    config: DictConfig

    @abstractmethod
    def load_plugins(self) -> None:
        """Abstract method in charge of loading scraping plugins"""
        ...

    def run(self) -> None:
        """Run the recipes loaded"""
        ...
