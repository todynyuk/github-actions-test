import pytest
import time,os,re,shutil
import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import undetected_chromedriver as uc

@pytest.fixture()
def setup():
    test_url = "https://rozetka.com.ua/ua/"
    global driver
    options = webdriver.ChromeOptions() 
    options.headless = True
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = uc.Chrome(options=options)
    driver.get(test_url)
   # driver = uc.Chrome(headless=True,use_subprocess=False)
   # driver.get(test_url)
    driver.implicitly_wait(10)
    yield
    driver.quit()

@pytest.mark.maintainer("todynyuk")
@pytest.mark.label("ItemFilter", "RamAndPrice")
def testItemRamAndPrice(setup):
        print(str(driver.title))
        logging.warning(str(driver.title))
        verify_title = str(driver.title).lower().__contains__("rozetka")
        assert verify_title, " Title not contains |rozetka| "
        print("Test was successful")
        driver.save_screenshot('output/screen.png')
        driver.quit()
        
@pytest.mark.skip
def test_loginPage(setup):
    pass

'''Test xfail in pytest'''
@pytest.mark.xfail
def test_xfail(setup):
    assert False
