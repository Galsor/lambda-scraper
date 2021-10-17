from dataclasses import dataclass
from enum import Enum


@dataclass
class CrawlerConfig:
    max_iter: int = 100


@dataclass
class RandomCrawlerConfig(CrawlerConfig):
    name: str = "random_crawler"
    delay_min: float = 0.2
    delay_max: float = 1.5


@dataclass
class FastCrawlerConfig(CrawlerConfig):
    name: str = "fast_crawler"


@dataclass
class LinearCrawlerConfig(CrawlerConfig):
    name: str = "linear_crawler"
    delay: float = 1


# TODO see how to integrate dep_config. (Config Store ?)
class Crawler:
    """Takes a URL and navigate through its childs to extract related URLs"""

    def __init__(self):
        pass

    def run(self):
        pass
