import time
from pages.device_page import DevicePage
from pages.devices_category_page import DeviceCategory
from pages.main_page import MainPage
from pages.shopping_basket import ShoppingBasket
from pages.sub_category_page import SubCategory
import pytest
import logging

class TestShoppingBasket:
    def testUsualPriceItemAndInBasket(self, driver):
        main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
        main_page.open()
        main_page.click_universal_category_link(driver, "Смартфони")
        SubCategory.click_universal_subcategory_menu_link(self, "Мобільні", driver)
        smartphone_price = DeviceCategory.getSmartphonePriceText(self, driver, 1)
        short_characteristics = DeviceCategory.get_goods_title_text_by_index(self, driver, 1)
        DeviceCategory.clickBuyButtonByIndex(self, driver, 1)
        DeviceCategory.clickOnShoppingBasketButton(self, driver)
        item_card_description_text = ShoppingBasket.get_goods_description_text_by_index(self, driver, 1)
        assert str(short_characteristics).__contains__(
            item_card_description_text), "Device Short_characteristics not equals"
        shopping_basket_item_price = ShoppingBasket.getDevicePriceText(self, driver, 1)
        assert smartphone_price == shopping_basket_item_price, "Prices are not equals"
        ShoppingBasket.set_goods_count_value(self, driver, 3)
        smartphone_price_multiply = (smartphone_price * 3)
        time.sleep(2)
        assert smartphone_price_multiply == ShoppingBasket.getSumPriceText(self, driver), "Prices are not equals"
        logging.INFO('Test was successful')

    def testAddGoodsInBasketAndCheckItEmpty(self, driver):
        main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
        main_page.open()
        main_page.click_universal_category_link(driver, "Смартфони")
        SubCategory.click_universal_subcategory_menu_link(self, "Мобільні", driver)
        DeviceCategory.clickBuyButtonByIndex(self, driver, 1)
        DeviceCategory.clickOnShoppingBasketButton(self, driver)
        assert ShoppingBasket.isBasketEmptyStatusTextPresent(self, driver) == False, \
            "Basket empty status text is presented"
        goods_in_shopping_basket_count = ShoppingBasket.getGoodsInCartListSize(self, driver)
        assert goods_in_shopping_basket_count > 0, "Basket is empty"
        logging.INFO('Test was successful')
