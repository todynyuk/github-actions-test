from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME = (By.XPATH, "//input[@id='user-name']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")
    ERROR_BUTTON = (By.XPATH, "//div[@id='login_button_container']/div/form/div[3]/h3/button")


class InventoryPageLocators:
    PAGE_TITLE = (By.XPATH, "//div[@id='header_container']/div[2]/span")
    HAMBURGER_ICON = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    HAMBURGER_MENU = (By.XPATH, "//div[@id='menu_button_container']/div/div[2]/div[1]/nav/a")
    LOGOUT_BUTTON = (By.XPATH, "//a[@id='logout_sidebar_link']")
    CART_ICON = (By.XPATH, "//div[@id='shopping_cart_container']//a")
    CART_COUNT = (By.XPATH, "//div[@id='shopping_cart_container']/a/span")
    SORT_MENU = (By.XPATH, "//div[@id='header_container']/div[2]/div/span/select")
    SORT_A_Z = (By.XPATH, "//div[@id='header_container']/div[2]/div/span/select/option[1]")
    SORT_Z_A = (By.XPATH, "//div[@id='header_container']/div[2]/div/span/select/option[2]")
    SORT_LOW_HIGH = (By.XPATH, "//div[@id='header_container']/div[2]/div/span/select/option[3]")
    SORT_HIGH_LOW = (By.XPATH, "//div[@id='header_container']/div[2]/div/span/select/option[4]")
    INVENTORY_ITEM = (By.XPATH, "//div[@class='inventory_item']")
    INVENTORY_ITEM_URL = (By.XPATH, "//div[@class='inventory_list']//div[@class='inventory_item']//div[@class='inventory_item_label']//a")
    INVENTORY_ITEM_NAME = (By.XPATH, "//div[@class='inventory_list']//div[@class='inventory_item']//div[@class='inventory_item_label']//div[@class='inventory_item_name']")
    INVENTORY_ITEM_DESC = (By.XPATH, "//div[@class='inventory_list']//div[@class='inventory_item']//div[@class='inventory_item_label']//div[@class='inventory_item_desc']")
    INVENTORY_ITEM_PRICE = (By.XPATH, "//div[@class='inventory_list']//div[@class='inventory_item']//div[@class='inventory_item_description']//div[@class='pricebar']//div[@class='inventory_item_price']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//div[@class='inventory_list']//div[@class='inventory_item']//div[@class='pricebar']//button")
    REMOVE_BUTTON = (By.XPATH, "//div[@class='inventory_list']//div[@class='inventory_item']//div[@class='pricebar']//button")


class ProductPageLocators:
    NAME = (By.XPATH, "//div[@id='inventory_item_container']/div/div/div[2]/div[1]")
    DESC = (By.XPATH, "//div[@id='inventory_item_container']/div/div/div[2]/div[2]")
    PRICE = (By.XPATH, "//div[@id='inventory_item_container']/div/div/div[2]/div[3]")
    ADD_TO_CART_BUTTON = (By.XPATH, "//div[@id='inventory_item_container']/div/div/div[2]/button")
    CART_COUNT = (By.XPATH, "//div[@id='shopping_cart_container']/a/span")
    REMOVE_BUTTON = (By.XPATH, "//div[@id='inventory_item_container']/div/div/div[2]/button")
    BACK_BUTTON = (By.XPATH, "//button[@id='back-to-products']")


class CartPageLocators:
    PAGE_TITLE = (By.XPATH, "//div[@id='header_container']/div[2]/span")
    CART_ITEM = (By.XPATH, "//div[@class='cart_item']")
    CART_ITEM_NAME = (By.XPATH, "//div[@class='cart_list']//div[@class='cart_item']//div[@class='cart_item_label']//div[@class='inventory_item_name']")
    CART_ITEM_DESC = (By.XPATH, "//div[@class='cart_list']//div[@class='cart_item']//div[@class='cart_item_label']//div[@class='inventory_item_desc']")
    CART_ITEM_PRICE = (By.XPATH, "//div[@class='cart_list']//div[@class='cart_item']//div[@class='cart_item_label']//div[@class='item_pricebar']//div[@class='inventory_item_price']")
    REMOVE_BUTTON = (By.XPATH, "//div[@class='cart_list']//div[@class='cart_item']//div[@class='item_pricebar']//button")
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//button[@id='continue-shopping']")
    CHECKOUT_BUTTON = (By.XPATH, "//button[@id='checkout']")


class CheckoutPageLocators:
    PAGE_TITLE = (By.XPATH, "//div[@id='header_container']/div[2]/span")
    FIRST_NAME = (By.XPATH, "//input[@id='first-name']")
    LAST_NAME = (By.XPATH, "//input[@id='last-name']")
    ZIP_CODE = (By.XPATH, "//input[@id='postal-code']")
    CANCEL_BUTTON = (By.XPATH, "//button[@id='cancel']")
    CONTINUE_BUTTON = (By.XPATH, "//input[@id='continue']")
    ERROR_MESSAGE = (By.XPATH, "//div[@id='checkout_info_container']/div/form/div[1]/div[4]/h3")
    ERROR_BUTTON = (By.XPATH, "//div[@id='checkout_info_container']/div/form/div[1]/div[4]/h3/button")


class OverviewPageLocators:
    PAGE_TITLE = (By.XPATH, "//div[@id='header_container']/div[2]/span")
    ITEM_PRICE = (By.XPATH, "//div[@class='cart_list']//div[@class='cart_item']//div[@class='cart_item_label']//div[@class='item_pricebar']//div[@class='inventory_item_price']")
    ITEM_TOTAL_PRICE = (By.XPATH, "//div[@id='checkout_summary_container']/div/div[2]/div[@class='summary_subtotal_label']")
    TOTAL_PRICE = (By.XPATH, "//div[@id='checkout_summary_container']/div/div[2]/div[@class='summary_tax_label']")
    TAX_PRICE = (By.XPATH, "//div[@id='checkout_summary_container']/div/div[2]/div[@class='summary_info_label summary_total_label']")
    CANCEL_BUTTON = (By.XPATH, "//button[@id='cancel']")
    FINISH_BUTTON = (By.XPATH, "//button[@id='finish']")


class OrderPageLocators:
    PAGE_TITLE = (By.XPATH, "//div[@id='header_container']/div[2]/span")
    PAGE_SUBTITLE = (By.XPATH, "//div[@id='checkout_complete_container']/h2")
    PAGE_TEXT = (By.XPATH, "//div[@id='checkout_complete_container']/div")
    BACK_BUTTON = (By.XPATH, "//button[@id='back-to-products']")
