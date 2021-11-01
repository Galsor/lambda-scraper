import json
import logging
from typing import Type

from lambda_scraper.recipe.interface import context, produce, scrap
from lambda_scraper.utils.paths import DATA_DIR
from lambda_scraper.utils.types import BaseTask

TYPE= type(__name__, (BaseTask,), {})
logger = logging.getLogger(__name__)

_context_filepath = DATA_DIR / "wikipedia" / "context.json"

def _context(
    task_type: TYPE,
):
    with open(_context_filepath) as f:
        context = json.load(f)
    return context
    

def _produce(
    task_type: TYPE,
):
    pass


def _scrap(
    task_type: TYPE,
):
    pass


