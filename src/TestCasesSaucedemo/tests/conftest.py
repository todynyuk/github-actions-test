import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from pages.order_page import OrderPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.overview_page import OverviewPage
from pages.product_page import ProductPage
from utils.generator import DataGenerator


@pytest.fixture(scope='function')
def driver():
    options = chrome_options()
    options.add_argument("chrome")  # Use headless if you do not need a browser UI
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def pages(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    overview_page = OverviewPage(driver)
    order_page = OrderPage(driver)
    return locals()


@pytest.fixture(scope='function')
def data():
    generator = DataGenerator()
    return locals()
