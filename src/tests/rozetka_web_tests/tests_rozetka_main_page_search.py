import pytest
from selenium.webdriver.common.by import By
import time,os,shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import sys
import logging

@pytest.mark.label("Search", "correct")
def test_correct_search(self, driver):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    search_text = "Agm A9"
    main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
    main_page.open()
    time.sleep(2)
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, "input[name='search']").send_keys(search_text)
    driver.find_element(By.CSS_SELECTOR, "button[class*='button_color_green']").click()
    button = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='goods-tile__title']"))).text
    assert search_text.lower() in str(button).lower(), "Search text not contains in all goods title texts"
    logging.info("This is standard logging after test")
    print("This is standard print test")
    time.sleep(5)
    if os.path.exists(os.path.join(os.getcwd(), 'output')):
        shutil.rmtree(os.path.join(os.getcwd(), 'output'))
    os.mkdir('output')
    driver.save_screenshot('output/screen.png')
    driver.close()
