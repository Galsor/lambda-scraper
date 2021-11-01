
from lambda_scraper.recipe.interface import produce, scrap
from lambda_scraper.utils.types import TaskType


@produce.register
def _(task_type: TaskType, ):
    pass

@scrap.register
def _(task_type: TaskType,):
    pass