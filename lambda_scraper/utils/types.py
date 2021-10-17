from enum import Enum, auto
from abc import ABC
from lambda_scraper.recipe import PLUGINS


class Executor(ABC):
    pass


class Producer(Executor):
    pass


class Scraper(Executor):
    pass


ExecutorMode = {
    "PRODUCER": Producer(),
    "SCRAPER": Scraper()
}

TaskType = Enum("Task", zip(PLUGINS, PLUGINS))  # Auto enum with plugins names
