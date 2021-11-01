from importlib import import_module
from pathlib import Path
from enum import Enum
import logging
from lambda_scraper.utils.types import BaseTask

logger = logging.getLogger("Initialize plugins")

plugin_dir = (Path(__file__).parent / "plugins").resolve()
assert plugin_dir.is_dir()

import_module(f"lambda_scraper.recipe.plugins")

PLUGINS = []

for file in plugin_dir.glob("*.py"):
    if file.name != "__init__.py":
        # ex: ("wikipedia", <class wikipedia>)
        PLUGINS.append((file.stem, type(__name__, (BaseTask,), {})))

# List all available scraping plugins
Tasks = Enum("Task", PLUGINS)  # Auto enum with plugins names

logger.debug(f"Available plugins: {[e.name for e in Tasks]}")