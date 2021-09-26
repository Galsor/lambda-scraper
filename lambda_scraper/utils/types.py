from enum import Enum


# TODO: sync enum value with names from the configs
# or use config store and dataclass
class ExecutorMode(str, Enum):
    URL_PARSER = "url_parser"
    SCRAPER = "scraper"
    FILE_MAKER = "file_maker"
