import pytest
from lambda_scraper.dep_drivers.selenium_chrome import ChromeDriver
from test.unit.mock_config import mock_config_scraper

@pytest.fixture(scope="module")
def driver(mock_config = mock_config_scraper()):
    driver = ChromeDriver(mock_config)
    return driver
    
def test_get(driver):
    driver.get("https://www.python.org/")
    assert "Python" in driver.title
