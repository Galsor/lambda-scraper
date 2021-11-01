import logging
from enum import Enum
from importlib import import_module
from pathlib import Path

from lambda_scraper.utils.types import BaseTask
from lambda_scraper.recipe.interface import *

logger = logging.getLogger("Initialize plugins")

plugin_dir = (Path(__file__).parent / "plugins").resolve()
assert plugin_dir.is_dir()

#import_module(f"lambda_scraper.recipe.plugins")

PLUGINS = []

for file in plugin_dir.glob("*.py"):
    if file.name != "__init__.py":
        module = import_module(f"lambda_scraper.recipe.plugins.{file.stem}")
        task_type = type(file.stem, (object,), {})
        
        # ex: ("wikipedia", <class wikipedia>)
        PLUGINS.append((file.stem, task_type()))
        
        # Register related functions
        context.register(task_type, module._context)
        produce.register(task_type, module._produce)
        scrap.register(task_type, module._scrap)


# List all available scraping plugins
Tasks = Enum("Task", PLUGINS)  # Auto enum with plugins names

logger.debug(f"Available plugins: {[e.name for e in Tasks]}")
