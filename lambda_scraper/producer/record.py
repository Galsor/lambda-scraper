from functools import wraps
from typing import Dict


def record_task(func):
    @wraps
    def wrapper(func, *args, **kwargs):
        task: Dict = func(*args, **kwargs)
        # TODO:
        # - Save task in queue
        # - Open record in database
        return task

    return wrapper
