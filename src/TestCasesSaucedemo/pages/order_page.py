from locators.page_locators import OrderPageLocators
from pages.cart_page import CartPage


class OrderPage(CartPage):
    order = OrderPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    """ Get order page title """
    def get_order_page_title(self) -> str:
        return self.action_get_text(self.order.PAGE_TITLE)

    """ Get order page subtitle """
    def get_order_page_subtitle(self) -> str:
        return self.action_get_text(self.order.PAGE_SUBTITLE)

    """ Get order page text """
    def get_order_page_text(self) -> str:
        return self.action_get_text(self.order.PAGE_TEXT)

    """ Click order back button """
    def click_order_back_button(self) -> None:
        self.action_left_click(self.element_is_visible(self.order.BACK_BUTTON))
