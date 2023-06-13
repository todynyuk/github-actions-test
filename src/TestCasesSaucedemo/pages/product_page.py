from locators.page_locators import ProductPageLocators
from pages.inventory_page import InventoryPage


class ProductPage(InventoryPage):
    product = ProductPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    """ Get product name """
    def get_product_name(self) -> str:
        return self.action_get_text(self.product.NAME)

    """ Get product desc """
    def get_product_desc(self) -> str:
        return self.action_get_text(self.product.DESC)

    """ Get product price """
    def get_product_price(self) -> float:
        product_price = self.action_get_text(self.product.PRICE)
        return float(product_price.replace("$", ""))

    """ Click add product button to cart """
    def click_add_product_to_cart(self) -> None:
        self.action_left_click(self.element_is_visible(self.product.ADD_TO_CART_BUTTON))

    """ Click remove product button from cart """
    def click_remove_product_from_cart(self) -> None:
        self.action_left_click(self.element_is_visible(self.product.REMOVE_BUTTON))

    """ Click back to products button """
    def click_back_to_products_button(self) -> None:
        self.action_left_click(self.element_is_visible(self.product.BACK_BUTTON))