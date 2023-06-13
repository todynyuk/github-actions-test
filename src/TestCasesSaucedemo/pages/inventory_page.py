import random

from selenium.webdriver.remote.webelement import WebElement

from locators.page_locators import InventoryPageLocators
from pages.login_page import LoginPage


class InventoryPage(LoginPage):
    inventory = InventoryPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    """ Get products page title """
    def get_products_page_title(self) -> str:
        return self.action_get_text(self.inventory.PAGE_TITLE)

    """ Open hamburger menu """
    def open_hamburger_menu(self) -> None:
        self.action_left_click(self.element_is_visible(self.inventory.HAMBURGER_ICON))

    """ Click logout button """
    def click_logout_button(self) -> None:
        self.action_left_click(self.element_is_visible(self.inventory.LOGOUT_BUTTON))

    """ Logout from app """
    def logout(self) -> None:
        self.open_hamburger_menu()
        self.click_logout_button()

    """ Get menu links """
    def get_menu_links(self) -> list[WebElement]:
        return self.elements_are_visible(self.inventory.HAMBURGER_MENU)

    """ Get all menu links text """
    def get_menu_links_text(self) -> list[str]:
        menu_links = self.get_menu_links()
        menu_links_text = self.action_get_text_from_elements(menu_links)
        return menu_links_text

    """ Open cart page """
    def open_cart_page(self) -> None:
        self.action_left_click(self.element_is_visible(self.inventory.CART_ICON))

    """ Check cart count exists """
    def check_cart_count_exists(self) -> bool:
        cart_count = self.element_is_present(self.inventory.CART_COUNT)
        return cart_count is not None

    """ Check cart count not-exist """
    def check_cart_count_not_exist(self) -> bool:
        cart_count = self.element_is_not_visible(self.inventory.CART_COUNT)
        return cart_count

    """ Get count of items in cart """
    def get_cart_item_count(self) -> int:
        cart_count = self.check_cart_count_exists()
        if cart_count:
            return int(self.action_get_text(self.inventory.CART_COUNT))
        else:
            return 0

    """ Get products count """
    def get_products_count(self) -> int:
        return len(self.elements_are_visible(self.inventory.INVENTORY_ITEM))

    """ Get all products """
    def get_all_product_elements(self) -> list[WebElement]:
        return self.elements_are_visible(self.inventory.INVENTORY_ITEM)

    """ Get all product urls """
    def get_list_of_product_urls(self) -> list[str]:
        product_links = self.elements_are_present(self.inventory.INVENTORY_ITEM_URL)
        urls = self.action_get_attr_from_elements(product_links, "href")
        urls_with_id = []
        for url in urls:
            url_index = random.randrange(0, len(urls))
            url = url.replace("inventory.html#", "inventory-item.html")
            url = f"{url}?id={url_index}"
            urls_with_id.append(url)
        return urls_with_id

    """ Get all product names """
    def get_list_of_product_names(self) -> list[str]:
        product_names = self.elements_are_visible(self.inventory.INVENTORY_ITEM_NAME)
        return self.action_get_text_from_elements(product_names)

    """ Get all product descriptions """
    def get_list_of_product_descs(self) -> list[str]:
        product_descs = self.elements_are_visible(self.inventory.INVENTORY_ITEM_DESC)
        return self.action_get_text_from_elements(product_descs)

    """ Get all product prices """
    def get_list_of_product_prices(self) -> list[float]:
        product_prices = self.elements_are_visible(self.inventory.INVENTORY_ITEM_PRICE)
        return [float(price.text.replace("$", "")) for price in product_prices]

    """ Get all product add to cart buttons """
    def get_list_of_add_to_cart_buttons(self) -> list[WebElement]:
        return self.elements_are_visible(self.inventory.ADD_TO_CART_BUTTON)

    """ Get all product remove from cart buttons """
    def get_list_of_remove_from_cart_buttons(self) -> list[WebElement]:
        return self.elements_are_visible(self.inventory.REMOVE_BUTTON)

    """ Add all products to cart """
    def add_all_to_cart(self) -> None:
        add_to_cart_buttons = self.get_list_of_add_to_cart_buttons()
        self.action_left_click_on_elements(add_to_cart_buttons)

    """ Remove all products from cart """
    def remove_all_from_cart(self) -> None:
        remove_from_cart_buttons = self.get_list_of_remove_from_cart_buttons()
        self.action_left_click_on_elements(remove_from_cart_buttons)

    """ Open random product """
    def open_random_product(self) -> None:
        product_urls_list = self.get_list_of_product_urls()
        url_index = random.randrange(0, len(product_urls_list))
        product_url = product_urls_list[url_index]
        self.open_url(product_url)

    """ Open products sort menu """
    def open_products_sort_menu(self) -> None:
        self.action_left_click(self.element_is_visible(self.inventory.SORT_MENU))

    """ Sort products A to Z """
    def sort_products_a_to_z(self) -> None:
        self.open_products_sort_menu()
        sort_option = self.element_is_present(self.inventory.SORT_A_Z)
        sort_option.click()

    """ Sort products Z to A """
    def sort_products_z_to_a(self) -> None:
        self.open_products_sort_menu()
        sort_option = self.element_is_present(self.inventory.SORT_Z_A)
        sort_option.click()

    """ Sort products low to high """
    def sort_products_low_to_high(self) -> None:
        self.open_products_sort_menu()
        sort_option = self.element_is_present(self.inventory.SORT_LOW_HIGH)
        sort_option.click()

    """ Sort products high to low """
    def sort_products_high_to_low(self) -> None:
        self.open_products_sort_menu()
        sort_option = self.element_is_present(self.inventory.SORT_HIGH_LOW)
        sort_option.click()