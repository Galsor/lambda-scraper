import logging
from enum import Enum
from lambda_scraper.utils.plugins import load_plugins

from lambda_scraper.utils.paths import PLUGINS_DIRS
from lambda_scraper.recipe.interface import *

logger = logging.getLogger("Initialize plugins")

PLUGINS = load_plugins(PLUGINS_DIRS)

# List all available scraping plugins
Tasks = Enum("Task", PLUGINS)  # Auto enum with plugins names

logger.debug(f"Available plugins: {[e.name for e in Tasks]}")
