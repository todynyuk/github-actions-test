import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os, re, shutil
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup():
    test_url = "https://rozetka.com.ua/ua/"
    global driver
    driver = uc.Chrome(headless=True, use_subprocess=False)
    driver.get(test_url)
    time.sleep(2)
    driver.implicitly_wait(10)
    yield
    driver.quit()


def testUsualPriceItemAndInBasket(self, driver):
    print(str(driver.title), flush=True)
    logging.warning('It is test logging.warning')
    verify_title = str(driver.title).lower().__contains__("rozetka")
    assert verify_title, " Title not contains |rozetka| "
    driver.find_element(By.XPATH, "//a[@class='menu-categories__link' and contains(.,'Смартфони')]").click() 
    time.sleep(2)
    print("Page smartphones is opened")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(@class,'tile-cats__heading') and contains(.,'Мобільні')]"))).click()
    time.sleep(2)
    print("Mobile page smartphones is opened") 
    driver.execute_script("window.scrollTo(0, 220)")
    smartphone_price = int(re.sub(r'\D', '', driver.find_element(By.XPATH, "(//span[@class='goods-tile__price-value'])[1]").text))
    short_characteristics = driver.find_element(By.XPATH, "(//span[@class='goods-tile__title'])[1]").text
    driver.execute_script("window.scrollTo(0, 250)")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(@class,'buy-button')][1]").click() 
    time.sleep(2)
    driver.find_element(By.XPATH, "//li[contains(@class,'cart')]/*/button[contains(@class,'header__button')]").click()
    time.sleep(3)
    item_card_description_text = driver.find_element(By.XPATH, "//a[@data-testid='title'][1]").text
    assert str(short_characteristics).__contains__(item_card_description_text), "Device short characteristics not equals"
    shopping_basket_item_price = int(re.sub(r'\D', '', driver.find_element(By.XPATH, "//p[@data-testid='cost'][1]").text))
    assert smartphone_price == shopping_basket_item_price, "Prices are not equals"
    driver.find_element(By.XPATH,"//input[@data-testid='cart-counter-input']").clear()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@data-testid='cart-counter-input']").send_keys(3)
    smartphone_price_multiply = (smartphone_price * 3)
    time.sleep(2)
    sum_price_text = int(re.sub(r'\D', '', driver.find_element(By.XPATH, "//div[@class='cart-receipt__sum-price']//span").text))
    assert smartphone_price_multiply == sum_price_text, "Prices are not equals"
    print('testUsualPriceItemAndInBasket was successful', flush=True)


def testAddGoodsInBasketAndCheckItEmpty(setup):
    print(str(driver.title), flush=True)
    logging.warning('It is test logging.warning')
    verify_title = str(driver.title).lower().__contains__("rozetka")
    assert verify_title, " Title not contains |rozetka| "
    driver.find_element(By.XPATH, "//a[@class='menu-categories__link' and contains(.,'Смартфони')]").click() 
    time.sleep(2)
    print("Page smartphones is opened")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(@class,'tile-cats__heading') and contains(.,'Мобільні')]"))).click()
    time.sleep(2)
    print("Mobile page smartphones is opened")
    driver.execute_script("window.scrollTo(0, 250)")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(@class,'buy-button')][1]").click() 
    time.sleep(2)
    driver.find_element(By.XPATH, "//li[contains(@class,'cart')]/*/button[contains(@class,'header__button')]").click()
    time.sleep(3)
    assert not WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h4[@class='cart-dummy__heading']"))), "Basket empty status text is presented"
    assert int(driver.find_elements(By.XPATH, "//p[@data-testid='cost']").__len__()) > 0, "Basket is empty"
    print('testAddGoodsInBasketAndCheckItEmpty was successful', flush=True)
