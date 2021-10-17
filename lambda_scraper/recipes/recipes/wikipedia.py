import requests

from .recipe import BSRecipe


class WikipediaRecipe(BSRecipe):
    def __init__(self, activated: bool = True):
        self.name = "Wikipedia Recipe"
        self.activated = activated
        self.entrypoints = [
            "Assurance",
            "Aéronautique",
            "Construction_automobile",
            "Banque",
        ]
        self.base_url = "https://fr.wikipedia.org/wiki/"

    def run_url_parsing(self):
        # TODO
        return super().run_url_parsing()

    def run_scraping(self):
        # TODO
        return super().run_scraping()

    def run_file_making(self):
        # TODO
        return super().run_file_making()
