from dataclasses import dataclass
from ..executors.plugins import Plugin
from abc import abstractmethod

@dataclass
class Recipe(Plugin):
    
    @abstractmethod
    def run_url_parsing(self):
        ...
    
    @abstractmethod
    def run_scraping(self):
        ...

    @abstractmethod
    def run_file_making(self):
        ...

@dataclass
class BSRecipe(Recipe):
    """Dedicated to static html scraping with beautiful soup"""
    ...

@dataclass
class APIRecipe(Recipe):
    """Dedicated to API response scraping"""
    ...

@dataclass
class SeleniumRecipe(Recipe):
    """Dedicated dynamic web page scraping including javascript, navigation or form filling tasks"""
    ...