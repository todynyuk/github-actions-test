import pytest
import time,os,re,shutil
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

@pytest.fixture()
def setup():
    test_url = "https://rozetka.com.ua/"
    global driver
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get(test_url)
    driver.implicitly_wait(10)
    yield
    driver.quit()

@pytest.mark.maintainer("todynyuk")
@pytest.mark.label("ItemFilter", "RamAndPrice")
def testItemRamAndPrice(setup):
        driver.maximize_window()
        time.sleep(2)
        title_text="Интернет-магазин ROZETKA™: официальный сайт самого популярного онлайн-гипермаркета в Украине"
        verify_title = str(driver.title).lower().__contains__(title_text)
        assert verify_title, "Titles are not equals"
        print("Test was successful")
        driver.quit()
