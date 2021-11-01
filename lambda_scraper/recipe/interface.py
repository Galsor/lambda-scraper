from functools import singledispatch

from lambda_scraper.producer.record import record_task
from lambda_scraper.scraper.record import record_result
from lambda_scraper.utils.types import TaskType


@record_task
@singledispatch
def produce(task_type: TaskType):
    """Generic method to produce scraping tasks.
    This methodes requires to be supercharged with @produce.register to provide actions."""
    raise NotImplementedError(
        f"Producer function is not implemented for {type(task_type)}"
    )


@record_result
@singledispatch
def scrap(task_type: TaskType):
    """Generic method to produce scraping tasks.
    This methodes requires to be supercharged with @produce.register to provide actions."""
    raise NotImplementedError(
        f"Scraper function is not implemented for {type(task_type)}"
    )


@singledispatch
def context(task_type: TaskType):
    """Generic method for loading the context of a tasks.
    This methodes requires to be supercharged with @context.register to provide actions."""
    raise NotImplementedError(
        f"Context function is not implemented for {type(task_type)}"
    )