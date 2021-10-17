from enum import Enum, auto

from lambda_scraper.recipe import PLUGINS


# TODO: sync enum value with names from the configs
# or use dep_config store and dataclass
class ExecutorMode(str, Enum):
    PRODUCER = auto()
    SCRAPER = auto()


TaskType = Enum("Task", zip(PLUGINS, PLUGINS)) #Auto enum with plugins names