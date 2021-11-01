import importlib
import logging
from os import PathLike
from typing import List
from lambda_scraper.recipe.interface import context, produce, scrap
from lambda_scraper.utils.paths import PLUGINS_DIRS
from lambda_scraper.utils.types import BaseTask

logger = logging.getLogger(__name__)


def load_plugins(path_list: List[PathLike]=PLUGINS_DIRS):
    PLUGINS = []
    for path in path_list:
        for file in path.glob("*.py"):
            if file.name != "__init__.py":
                #module = import_module(f"lambda_scraper.recipe.plugins.{file.stem}")
                logger.debug(f"loading plugin in file: {file}")
                spec = importlib.util.spec_from_file_location(file.stem, file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                task_type = type(file.stem, (BaseTask,), {})
                
                # ex: ("wikipedia", <class wikipedia>)
                PLUGINS.append((file.stem, task_type()))
                
                # Register related functions
                context.register(task_type, module._context)
                produce.register(task_type, module._produce)
                scrap.register(task_type, module._scrap)
    logger.debug(f"Plugins successfully loaded: {PLUGINS}")
    return PLUGINS
