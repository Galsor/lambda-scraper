from unittest import TestCase
from lambda_scraper.drivers.selenium_chrome import ChromeDriver
from test.unit.mock_config import MockConfig

class TestChromeDriver(TestCase):
    def setUp(self):
        self.mock_cfg = MockConfig()
        print(self.mock_cfg)
        self.driver = ChromeDriver(self.mock_cfg)
    
    def test_get(self):
        self.driver.get("https://www.python.org/")
        assert "Python" in self.driver.title
