from selenium import webdriver
from omegaconf import DictConfig
from selenium.webdriver.chrome.options import Options as ChromeOptions

from .driver import Driver


class ChromeDriver(Driver, webdriver.Chrome):

    def __init__(self, cfg: DictConfig):
        self.options = ChromeOptions()
        for key, value in cfg.driver.items():
            if value == True:
                self.options.add_argument(f"--{key}")
        super().__init__(options=self.options)


