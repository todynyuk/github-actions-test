import pytest
import time,os,re,shutil
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

@pytest.fixture()
def setup():
    test_url = "https://rozetka.com.ua/ua/"
    global driver
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.get(test_url)
    driver.implicitly_wait(10)
    yield
    driver.quit()

@pytest.mark.maintainer("todynyuk")
@pytest.mark.label("ItemFilter", "RamAndPrice")
def testItemRamAndPrice(setup):
        time.sleep(2)
        print("This is standard print test")
        driver.find_element(By.XPATH, "//a[@class='menu-categories__link' and contains(.,'Смартфони')]").click()
        time.sleep(2)
        print("Page Smartphones is opened")
        driver.find_element(By.XPATH,
                            "//a[contains(@class,'tile-cats__heading') and contains(.,'Мобільні')]").click()
        time.sleep(2)
        print("Mobile Page Smartphones is opened")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@class,'tile-filter__link') and contains(text(),'12')]"))).click()
        time.sleep(2)
        element = driver.find_element(By.XPATH, "//a[contains(@data-id,'Синій')]")
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        element.click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 220)")
        smartphone_price = int(re.sub(r'\D', '', driver.find_element(By.XPATH, "//span[@class='goods-tile__price-value'][1]").text))
        driver.execute_script("window.scrollTo(0, 220)")
        driver.find_element(By.XPATH, "//a[@class='goods-tile__heading ng-star-inserted'][1]").click()
        time.sleep(2)
        print("MoreAboutDevice Page Smartphones is opened")
        short_characteristics = driver.find_element(By.XPATH, "//h1[@class='product__title']").text.__contains__(str(12))
        chosen_device_price = re.sub(r'\D', '', driver.find_element(By.XPATH, "//p[contains(@class,'product-price__big')]").text)
        assert short_characteristics, "Short_characteristics don't contains chosen ram capacity"
        assert str(smartphone_price) == chosen_device_price, "Prices are not equals"
        print("Test was successful")
        if os.path.exists(os.path.join(os.getcwd(), 'output')):
            shutil.rmtree(os.path.join(os.getcwd(), 'output'))
        os.mkdir('output')
        webdriver.Chrome.save_screenshot('output/screen.png')
        webdriver.Chrome.quit()
