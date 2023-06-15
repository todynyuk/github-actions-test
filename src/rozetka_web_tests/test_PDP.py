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
    test_url = "https://demoqa.com"
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
        if os.path.exists(os.path.join(os.getcwd(), 'output')):
            shutil.rmtree(os.path.join(os.getcwd(), 'output'))
        os.mkdir('output')
        driver.save_screenshot('output/screen.png')
        print("This is standard print test")
        time.sleep(2)
        button_card = driver.find_element(By.CSS_SELECTOR, "div[class='card-body']") 
        driver.execute_script("arguments[0].click();", button_card)
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[.='Buttons']").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "button[id='E54Ia']").click() 
        time.sleep(2)
        driver.save_screenshot('output/screen1.png')
        print("BUTTON Click Me is clicked")
        assert driver.find_element(By.ID, "dynamicClickMessage").is_displayed(),"Message not displayed"
        message = driver.find_element(By.ID, "dynamicClickMessage").text
        assert str(message) == "You have done a dynamic click", "Prices are not equals"
        print("Test was successful")
        webdriver.Chrome.save_screenshot('output/screen3.png')
        webdriver.Chrome.quit()
