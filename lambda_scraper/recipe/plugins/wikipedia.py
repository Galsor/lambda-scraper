import json

from lambda_scraper.recipe.interface import produce, scrap, context
from lambda_scraper.utils.types import TaskType
from lambda_scraper.utils.paths import DATA_DIR


_context_filepath = DATA_DIR / "wikipedia" / "context.json"


@produce.register
def _(
    task_type: TaskType,
):
    pass


@scrap.register
def _(
    task_type: TaskType,
):
    pass


@context.register
def _(
    task_type: TaskType,
    ):
    with open(context_filepath) as f:
            context = json.load(f)
    return context 