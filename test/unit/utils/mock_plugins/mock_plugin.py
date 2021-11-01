
from lambda_scraper.utils.types import BaseTask


TYPE= type(__name__, (BaseTask,), {})


def _context(task_type: TYPE,):
    return  True
    

def _produce(task_type: TYPE,):
    return True


def _scrap(task_type: TYPE,):
    return True

