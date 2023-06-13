from selenium.webdriver.remote.webelement import WebElement

from locators.page_locators import CartPageLocators
from pages.inventory_page import InventoryPage


class CartPage(InventoryPage):
    cart = CartPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    """ Get cart page title """
    def get_cart_page_title(self) -> str:
        return self.action_get_text(self.cart.PAGE_TITLE)

    """ Get cart items count """
    def get_item_count(self) -> int:
        return len(self.elements_are_visible(self.cart.CART_ITEM))

    """ Get all cart items """
    def get_all_cart_item_elements(self) -> list[WebElement]:
        return self.elements_are_visible(self.cart.CART_ITEM)

    """ Get all cart items names """
    def get_list_of_cart_item_names(self) -> list[str]:
        item_names = self.elements_are_visible(self.cart.CART_ITEM_NAME)
        return self.action_get_text_from_elements(item_names)

    """ Get all cart items descriptions """
    def get_list_of_cart_item_descs(self) -> list[str]:
        item_descs = self.elements_are_visible(self.cart.CART_ITEM_DESC)
        return self.action_get_text_from_elements(item_descs)

    """ Get all cart items prices """
    def get_list_of_cart_item_prices(self) -> list[float]:
        item_prices = self.elements_are_visible(self.cart.CART_ITEM_PRICE)
        return [float(price.text.replace("$", "")) for price in item_prices]

    """ Get all remove buttons on cart page """
    def get_list_of_remove_buttons(self) -> list[WebElement]:
        return self.elements_are_visible(self.cart.REMOVE_BUTTON)

    """ Remove all products from cart """
    def remove_all_from_cart(self) -> None:
        remove_buttons = self.get_list_of_remove_buttons()
        self.action_left_click_on_elements(remove_buttons)

    """ Calculate cart item total price """
    def calc_cart_item_total_price(self) -> float:
        item_prices = self.get_list_of_cart_item_prices()
        return sum(item_prices)

    """ Calculate cart tax price """
    def calc_cart_tax_price(self) -> float:
        item_total_price = self.calc_cart_item_total_price()
        tax_price = (item_total_price * 8) / 100
        return round(tax_price, 2)

    """ Calculate cart total price """
    def calc_cart_total_price(self) -> float:
        item_total_price = self.calc_cart_item_total_price()
        tax_price = self.calc_cart_tax_price()
        total_price = item_total_price + tax_price
        return total_price

    """ Get cart list of prices """
    def get_list_of_cart_calc_prices(self) -> list[float]:
        item_total_price = self.calc_cart_item_total_price()
        tax_price = self.calc_cart_tax_price()
        total_price = self.calc_cart_total_price()
        prices = [item_total_price, tax_price, total_price]
        return sorted(prices)

    """ Check cart is empty """
    def check_cart_is_empty(self) -> bool:
        cart_item = self.element_is_not_visible(self.cart.CART_ITEM)
        return cart_item

    """ Click continue shopping button """
    def click_continue_shopping(self) -> None:
        self.action_left_click(self.element_is_visible(self.cart.CONTINUE_SHOPPING_BUTTON))

    """ Click checkout button """
    def click_checkout(self) -> None:
        self.action_left_click(self.element_is_visible(self.cart.CHECKOUT_BUTTON))