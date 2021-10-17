from enum import Enum, auto


# TODO: sync enum value with names from the configs
# or use dep_config store and dataclass
class ExecutorMode(str, Enum):
    PRODUCER = auto()
    SCRAPER = auto()
