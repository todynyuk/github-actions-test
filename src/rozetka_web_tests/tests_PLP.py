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

@pytest.mark.skip(reason="Rozetka have problem with sorting by price")
def testFilterByBrandNameMaxCustomPriceAndAvailable(setup):
    verify_title = str(driver.title).lower().__contains__("rozetka")
    assert verify_title, " Title not contains |rozetka| "
    driver.find_element(By.XPATH, "//a[@class='menu-categories__link' and contains(.,'Смартфони')]").click()
    time.sleep(2)
    print("Page smartphones is opened", flush=True)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(@class,'tile-cats__heading') and contains(.,'Мобільні')]"))).click()
    time.sleep(2)
    print("Mobile page smartphones is opened", flush=True)
    assert str(driver.title).lower().__contains__(("Мобільні").lower())
    driver.find_element(By.XPATH, "//input[@formcontrolname='max']").clear()
    driver.find_element(By.XPATH, "//input[@formcontrolname='max']").send_keys(4000)
    driver.find_element(By.XPATH, "//button[contains(@class,'slider-filter__button')]").click()
    counter = 0
    device_prices = driver.find_elements(By.XPATH, "//span[@class='goods-tile__price-value']")
    for x in range(1, 6):
        if int(device_prices[x].text) <= 4000:
            counter += 1
        else:
            counter += 0
    assert counter == 5, "One or more things have price more than choosen"
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.XPATH, "//a[contains(@data-id,'Sigma')]")).perform()
    driver.find_element(By.XPATH, "//a[contains(@data-id,'Sigma')]").click()
    time.sleep(3)
    goods_title = driver.find_elements(By.XPATH, "//span[@class='goods-tile__title']")
    for x in range(1, 6):
        if goods_title[x].text.lower().__contains__("Sigma".lower()):
            counter += 1
        else:
            counter += 0
    assert counter == 5, "Search result don`t contains chosen brand"
    action.move_to_element(driver.find_element(By.XPATH, "//a[contains(@data-id,'Є в наявності')]")).perform()
    driver.find_element(By.XPATH, "//a[contains(@data-id,'Є в наявності')]").click()
    time.sleep(3)
    length = driver.find_elements(By.XPATH,
                                  "//div[contains(@class,'goods-tile__availability') and contains(text(),'Немає в наявності')]").__len__()
    assert length == 0, "One or more goods are not available"
    print("Test FilterByBrandNameMaxCustomPriceAndAvailable was successful", flush=True)


def testVerifyItemRamMatrixTypeAndProcessor(setup):
    verify_title = str(driver.title).lower().__contains__("rozetka")
    assert verify_title, " Title not contains |rozetka| "
    driver.find_element(By.XPATH, "//a[@class='menu-categories__link' and contains(.,'Ноутбуки')]").click()
    time.sleep(2)
    print("Page laptops is opened", flush=True)
    time.sleep(10)
    driver.find_element(By.XPATH, "//a[contains(@class,'tile-cats__heading') and contains(.,'моноблоки')]").click()
    time.sleep(3)
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.XPATH, "//a[contains(@data-id,'Intel Core i5')]")).perform()
    driver.find_element(By.XPATH, "//a[contains(@data-id,'Intel Core i5')]").click()
    time.sleep(3)
    action.move_to_element(driver.find_element(By.XPATH, "//a[contains(@data-id,'Моноблок')]")).perform()
    driver.find_element(By.XPATH, "//a[contains(@data-id,'Моноблок')]").click()
    time.sleep(3)
    action.move_to_element(driver.find_element(By.XPATH, "//a[contains(@data-id,'8 ГБ')]")).perform()
    driver.find_element(By.XPATH, "//a[contains(@data-id,'8 ГБ')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,
                        "//span[@class='sidebar-block__toggle-title' and contains (., 'Тип матриці')]").click()
    action.move_to_element(driver.find_element(By.XPATH, "//a[contains(@data-id,'IPS')]")).perform()
    driver.find_element(By.XPATH, "//a[contains(@data-id,'IPS')]").click()
    time.sleep(3)
    action.move_to_element(driver.find_element(By.XPATH, "//a[contains(@data-id,'Новий')]")).perform()
    driver.find_element(By.XPATH, "//a[contains(@data-id,'Новий')]").click()
    time.sleep(3)
    action.move_to_element(driver.find_element(By.XPATH, "//a[contains(@data-id,'Є в наявності')]")).perform()
    driver.find_element(By.XPATH, "//a[contains(@data-id,'Є в наявності')]").click()
    time.sleep(3)
    length = driver.find_elements(By.XPATH,
                                  "//div[contains(@class,'goods-tile__availability') and contains(text(),'Немає в наявності')]").__len__()
    assert length == 0, "One or more goods are not available"
    driver.execute_script("window.scrollTo(0, 220)")
    driver.find_element(By.XPATH, "//a[@class='goods-tile__heading ng-star-inserted'][1]").click()
    driver.execute_script("arguments[0].scrollIntoView();",
                          driver.find_element(By.XPATH, "//p[@class='product-about__brief ng-star-inserted']"))
    assert driver.find_element(By.XPATH, "//p[@class='product-about__brief ng-star-inserted']").text.__contains__(
        "Intel Core i5"), "Processor name text not contains in about device text"
    assert driver.find_element(By.XPATH, "//p[@class='product-about__brief ng-star-inserted']").text.__contains__(
        "8 ГБ"), "Ram text not contains in about device text"
    assert driver.find_element(By.XPATH, "//p[@class='product-about__brief ng-star-inserted']").text.__contains__(
        "IPS"), "Matrix type text not contains in about device text"
    assert driver.find_element(By.XPATH,
                               "//h3[@class='product-tabs__heading']//span[contains(@class,'heading_color_gray')]").text.__contains__(
        "Моноблок"), "Computer type text not contains in description device text"
    print("Test FilterByBrandNameMaxCustomPriceAndAvailable was successful", flush=True)

def testVerifySortByPrice(setup):
    verify_title = str(driver.title).lower().__contains__("rozetka")
    assert verify_title, " Title not contains |rozetka| "
    driver.find_element(By.XPATH, "//a[@class='menu-categories__link' and contains(.,'Смартфони')]").click()
    time.sleep(2)
    print("Page smartphones is opened", flush=True)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(@class,'tile-cats__heading') and contains(.,'Мобільні')]"))).click()
    time.sleep(2)
    print("Mobile page smartphones is opened", flush=True)
    driver.find_element(By.XPATH,
                        "//select[contains(@class,'select-css')]/option[contains(text(),'Від дешевих до дорогих')]")
    counter_low_hight = 0
    priceItemText = driver.find_elements(By.XPATH, "//span[@class='goods-tile__price-value']")
    for x in range(1, 6):
        if (re.sub(r'\D', '', priceItemText[x].text)) <= (re.sub(r'\D', '', priceItemText[x + 1].text)):
            counter_low_hight += 1
        else:
            counter_low_hight += 0
    assert counter_low_hight == 5, "One or more prices not sorted from low to high price"
    driver.find_element(By.XPATH,
                        "//select[contains(@class,'select-css')]/option[contains(text(),'Від дорогих до дешевих')]")
    counter_hight_to_low = 0
    is_good_prices_hight_to_low = driver.find_elements(By.XPATH, "//span[@class='goods-tile__price-value']")
    for x in range(1, 6):
        if (re.sub(r'\D', '', priceItemText[x].text)) >= (re.sub(r'\D', '', priceItemText[x + 1].text)):
            counter_hight_to_low += 1
        else:
            counter_hight_to_low += 0
        assert counter_hight_to_low == 5, "One or more prices not sorted from high to low price"
    print("Test VerifySortByPrice was successful", flush=True)

def testAddingAndCountGoodsInBasket(setup):
    verify_title = str(driver.title).lower().__contains__("rozetka")
    assert verify_title, " Title not contains |rozetka| "
    driver.find_element(By.XPATH, "//a[@class='menu-categories__link' and contains(.,'Смартфони')]").click()
    time.sleep(2)
    print("Page smartphones is opened", flush=True)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(@class,'tile-cats__heading') and contains(.,'Мобільні')]"))).click()
    time.sleep(2)
    print("Mobile page smartphones is opened", flush=True)
    assert not WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.XPATH, "//span[contains(@class,'badge--green')]"))), "Cart Goods Counter Text is presented"
    driver.execute_script("window.scrollTo(0, 250)")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(@class,'buy-button')][1]").click()
    time.sleep(2)
    assert driver.find_element(By.XPATH,
                               "//span[contains(@class,'badge--green')]").is_displayed(), "Cart Goods Counter Text isn't presented"
    print("Test AddingAndCountGoodsInBasket was successful", flush=True)

def test_choose_brands_and_check(setup):
    verify_title = str(driver.title).lower().__contains__("rozetka")
    assert verify_title, " Title not contains |rozetka| "
    driver.find_element(By.XPATH, "//a[@class='menu-categories__link' and contains(.,'Смартфони')]").click()
    time.sleep(2)
    print("Page smartphones is opened", flush=True)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(@class,'tile-cats__heading') and contains(.,'Мобільні')]"))).click()
    time.sleep(2)
    print("Mobile page smartphones is opened", flush=True)
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.XPATH, "//a[contains(@data-id,'Huawei')]")).perform()
    driver.find_element(By.XPATH, "//a[contains(@data-id,'Huawei')]").click()
    time.sleep(3)
    action.move_to_element(driver.find_element(By.XPATH, "//a[contains(@data-id,'Infinix')]")).perform()
    driver.find_element(By.XPATH, "//a[contains(@data-id,'Infinix')]").click()
    time.sleep(3)
    action.move_to_element(driver.find_element(By.XPATH, "//a[contains(@data-id,'Motorola')]")).perform()
    driver.find_element(By.XPATH, "//a[contains(@data-id,'Motorola')]").click()
    time.sleep(3)
    chosen_filters = []
    chosen_filtersText = driver.find_elements(By.XPATH,
                                              "//li[contains(@class,'selection')]//a[contains(@class,'link')]")
    for i in chosen_filtersText:
        chosen_filters.append(str(i.text).replace(' ', ''))
    assert "Huawei" in chosen_filters, "List chosen parameters not contains Huawei"
    assert "Infinix" in chosen_filters, "List chosen parameters not contains Infinix"
    assert "Motorola", "List chosen parameters not contains Motorola"
    print("Test choose brands and check was successful", flush=True)
