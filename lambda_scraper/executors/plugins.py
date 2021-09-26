import logging
from abc import ABC
from dataclasses import dataclass
from typing import Dict, List, Optional, Type

from hydra.core.singleton import Singleton
from omegaconf import DictConfig

logger = logging.getLogger(__name__)


@dataclass
class Plugin(ABC):
    name: str
    activated: bool


class Plugins(metaclass=Singleton):
    def __init__(self, cfg: DictConfig, initialized: bool = True) -> None:
        self.name_to_plugin: Dict[str, Type[Plugin]] = {}
        if initialized:
            self._initialize(only_active=cfg.plugins.only_active)

    def __getitem__(self, plugin_name: str) -> Plugin:
        return self.name_to_plugin[plugin_name]

    def __len__(self) -> int:
        return len(self.name_to_plugin)

    def _initialize(
        self, only_active: bool = True, plugin_type: Optional[Plugin] = None
    ) -> None:
        """Load plugins from configs"""
        discovered_plugins = self._discover(plugin_type)
        if only_active:
            self.load_active_plugins(discovered_plugins)
        else:
            self.load_all_plugins(discovered_plugins)

    def _discover(self, plugin_type: Optional[Type[Plugin]] = None) -> List[Plugin]:
        discovered_plugins: List[Type[Plugin]] = []
        if plugin_type is None:
            plugin_type = Plugin
        assert issubclass(plugin_type, Plugin)
        # TODO Look for plugins where they are

        return discovered_plugins

    def load_active_plugins(self, discovered_plugins: List[Plugin]) -> None:
        for plugin in discovered_plugins:
            if plugin.activated:
                self.name_to_plugin[plugin.name] = plugin

    def load_all_plugins(self, discovered_plugins: List[Plugin]) -> None:
        for plugin in discovered_plugins:
            self.name_to_plugin[plugin.name] = plugin

    def reset(
        self, reinitialize=True, only_active=True, plugin_type: Optional[Plugin] = None
    ):
        self.name_to_plugin: Dict[str, Type[Plugin]] = {}
        if reinitialize:
            self._initialize(only_active, plugin_type)
