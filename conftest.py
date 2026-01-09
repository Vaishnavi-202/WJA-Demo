import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--headed", action="store_true", default=False, help="Run tests with browser UI")


@pytest.fixture
def driver(request):
    headed = request.config.getoption("--headed")

    options = Options()
    if not headed:
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1280,800")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(2)

    yield driver

    driver.quit()
