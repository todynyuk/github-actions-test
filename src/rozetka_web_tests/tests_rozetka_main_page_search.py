import pytest
from selenium.webdriver.common.by import By
import time,os,shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import sys
import logging
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def setup():
    test_url = "https://rozetka.com.ua/ua/"
    global driver
    driver = uc.Chrome(use_subprocess=True)
    driver.get(test_url)
    time.sleep(2)
    driver.implicitly_wait(10)
    yield
    driver.quit()

@pytest.mark.maintainer("todynyuk")
@pytest.mark.label("Correct search")
def test_correct_search(setup):
    print(str(driver.title), flush=True)
    print('Without headless and use_subprocess=True instead False', flush=True)
    logging.warning(str(driver.title))
    verify_title = str(driver.title).lower().__contains__("rozetka")
    assert verify_title, " Title not contains |rozetka| "
    search_text = "Agm A9"
    driver.find_element(By.CSS_SELECTOR, "input[name='search']").send_keys(search_text)
    #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class*='button_color_green']"))).click()
    driver.find_element(By.CSS_SELECTOR, "button[class*='button_color_green']").click()
    counter = 0
    WebDriverWait(driver, 3).until(EC.visibility_of_all_elements_located((By.XPATH, "//span[@class='goods-tile__title']")))    
    goods_title = driver.find_elements(By.XPATH, "//span[@class='goods-tile__title']")
    for x in range(1, 6):
        if goods_title[x].text.lower().__contains__(search_text.lower()):
            counter += 1
        else:
            counter += 0 
    assert counter == 5, "Search text not contains in all goods title texts"
    LOGGER.info("This is standard logging after test")
    print("This is standard print test")
    time.sleep(5)
    driver.get_screenshot_as_file('screen.png')
    driver.save_screenshot('output/screen.png')
    if os.path.exists(os.path.join(os.getcwd(), 'output')):
        shutil.rmtree(os.path.join(os.getcwd(), 'output'))
    os.mkdir('output')
    driver.get_screenshot_as_file('output/screen.png')
    driver.save_screenshot('output/screen.png')
    driver.get_screenshot_as_file('screen.png')
    time.sleep(2)
    driver.close()

@pytest.mark.maintainer("todynyuk")
@pytest.mark.label("Incorrect search")
def test_incorrect_search():
    assert str(driver.title).lower().__contains__("rozetka"), " Title not contains |rozetka| "
    search_text = "hgvhvg"
    driver.find_element(By.CSS_SELECTOR, "input[name='search']").send_keys(search_text)
    driver.find_element(By.CSS_SELECTOR, "button[class*='button_color_green']").click()
    assert driver.find_element(By.XPATH, "//span[@class='ng-star-inserted']").is_displayed(), "Wrong request text isn`t presented"
    logging.INFO('Test was successful')
