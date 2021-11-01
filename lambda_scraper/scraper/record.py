from functools import wraps
from typing import Dict


def record_result(func):
    @wraps
    def wrapper(func, *args, **kwargs):
        task: Dict = func(*args, **kwargs)
        # TODO:
        # - Remove task from queue
        # - Update record in database
        return task

    return wrapper
