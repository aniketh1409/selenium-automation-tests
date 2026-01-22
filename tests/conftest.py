import pytest
from selenium import webdriver

BASE_URL = "http://localhost:8000/index.html"  

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)
    yield driver
    driver.quit()