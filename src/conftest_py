import os
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    options = webdriver.FirefoxOptions()
    options.platform_name = "linux"
    options.browser_version = "108.0"
    options.set_capability("enableVideo", "true")

    driver = webdriver.Remote(
        options=options
    )
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
