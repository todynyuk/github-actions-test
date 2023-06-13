import re

from locators.page_locators import OverviewPageLocators
from pages.cart_page import CartPage


class OverviewPage(CartPage):
    overview = OverviewPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    """ Get overview page title """
    def get_overview_page_title(self) -> str:
        return self.action_get_text(self.overview.PAGE_TITLE)

    """ Get all overview items prices """
    def get_list_of_overview_item_prices(self) -> list[float]:
        item_prices = self.elements_are_visible(self.overview.ITEM_PRICE)
        return [float(price.text.replace("$", "")) for price in item_prices]

    """ Calculate overview item total price """
    def calc_overview_item_total_price(self) -> float:
        item_prices = self.get_list_of_overview_item_prices()
        return sum(item_prices)

    """ Calculate overview tax price """
    def calc_overview_tax_price(self) -> float:
        item_total_price = self.calc_overview_item_total_price()
        tax_price = (item_total_price * 8) / 100
        return round(tax_price, 2)

    """ Calculate overview total price """
    def calc_overview_total_price(self) -> float:
        item_total_price = self.calc_overview_item_total_price()
        tax_price = self.calc_overview_tax_price()
        total_price = item_total_price + tax_price
        return total_price

    """ Get overview list of calculated prices """
    def get_list_of_overview_calc_prices(self) -> list[float]:
        item_total_price = self.calc_overview_item_total_price()
        tax_price = self.calc_overview_tax_price()
        total_price = self.calc_overview_total_price()
        prices = [item_total_price, tax_price, total_price]
        return sorted(prices)

    """ Get overview item total price """
    def get_overview_item_total_price(self) -> float:
        get_item_total_price = self.action_get_text(self.overview.ITEM_TOTAL_PRICE)
        item_total_price = re.findall(r'\d+\.\d+', get_item_total_price)[0]
        return float(item_total_price)

    """ Get overview tax price """
    def get_overview_tax_price(self) -> float:
        get_tax_price = self.action_get_text(self.overview.TAX_PRICE)
        tax_price = re.findall(r'\d+\.\d+', get_tax_price)[0]
        return float(tax_price)

    """ Get overview total price """
    def get_overview_total_price(self) -> float:
        get_total_price = self.action_get_text(self.overview.TOTAL_PRICE)
        total_price = re.findall(r'\d+\.\d+', get_total_price)[0]
        return float(total_price)

    """ Get overview list of total prices """
    def get_list_of_overview_total_prices(self) -> list[float]:
        item_total_price = self.get_overview_item_total_price()
        tax_price = self.get_overview_tax_price()
        total_price = self.get_overview_total_price()
        prices = [item_total_price, tax_price, total_price]
        return sorted(prices)

    """ Click cancel button """
    def click_cancel_overview(self) -> None:
        self.action_left_click(self.element_is_visible(self.overview.CANCEL_BUTTON))

    """ Click finish button """
    def click_finish_overview(self) -> None:
        self.action_left_click(self.element_is_visible(self.overview.FINISH_BUTTON))