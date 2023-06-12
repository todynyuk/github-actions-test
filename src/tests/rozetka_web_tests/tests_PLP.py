import time
from pages.device_page import DevicePage
from pages.devices_category_page import DeviceCategory
from pages.main_page import MainPage
from pages.sub_category_page import SubCategory
import pytest
import logging

class TestDevicesCategoryPage:

    @pytest.mark.skip(reason="Rozetka have problem with sorting by price")
    def testFilterByBrandNameMaxCustomPriceAndAvailable(self, driver):
        main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
        main_page.open()
        main_page.click_universal_category_link(driver, "Смартфони")
        time.sleep(2)
        SubCategory.click_universal_subcategory_menu_link(self, "Мобільні", driver)
        assert str(driver.title).lower().__contains__(("Мобільні").lower())
        DeviceCategory.clear_and_set_sorting_price(self, driver, "max", 4000)
        DeviceCategory.click_ok_button(self, driver)
        assert DeviceCategory.check_is_all_goods_prices_less_than_choosen(self, driver, 4000), \
            "One or more things have price more than choosen"
        DeviceCategory.click_check_box_filter(self, driver, "Sigma")
        assert DeviceCategory.verify_is_search_think_present_in_goods_title(self, driver, "Sigma"), \
            "Search result don`t contains chosen brand"
        DeviceCategory.click_check_box_filter(self, driver, "Є в наявності")
        length = DeviceCategory.check_is_all_goods_available(self, driver, "Немає в наявності")
        assert length == 0, "One or more goods are not available"
        logging.INFO('Test was successful')

    def testVerifyItemRamMatrixTypeAndProcessor(self, driver):
        main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
        main_page.open()
        main_page.click_universal_category_link(driver, "Ноутбуки")
        SubCategory.click_universal_subcategory_menu_link(self, "моноблоки", driver)
        DeviceCategory.click_check_box_filter(self, driver, "Intel Core i5")
        DeviceCategory.click_check_box_filter(self, driver, "Моноблок")
        DeviceCategory.click_check_box_filter(self, driver, "8 ГБ")
        DeviceCategory.clickUniversalShowCheckBoxButton(self, driver, "Тип матриці")
        DeviceCategory.click_check_box_filter(self, driver, "IPS")
        DeviceCategory.click_check_box_filter(self, driver, "Новий")
        DeviceCategory.click_check_box_filter(self, driver, "Є в наявності")
        length = DeviceCategory.check_is_all_goods_available(self, driver,
                                                             "Немає в наявності")
        assert length == 0, "One or more goods are not available"
        DeviceCategory.clickLinkMoreAboutDevice(self, driver, 1)
        assert DevicePage.verifyChosenParameterInShortCharacteristics(self, driver, "Intel Core i5"), \
            "Processor name text not contains in about device text"
        assert DevicePage.verifyChosenParameterInShortCharacteristics(self, driver, "8 ГБ"), \
            "Ram text not contains in about device text"
        assert DevicePage.verifyChosenParameterInShortCharacteristics(self, driver, "IPS"), \
            "Matrix type text not contains in about device text"
        assert DevicePage.verifyChosenParamInAllCharacteristics(self, driver,
                                                                "Моноблок"), "Computer type text not contains in description device text"
        logging.INFO('Test was successful')

    @pytest.mark.skip(reason="Rozetka have problem with sorting by price")
    def testVerifySortByPrice(self, driver):
        main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
        main_page.open()
        main_page.click_universal_category_link(driver, "Смартфони")
        SubCategory.click_universal_subcategory_menu_link(self, "Мобільні", driver)
        DeviceCategory.clickDropdownOption(self, driver, "Від дешевих до дорогих")
        is_good_prices_low_to_hight = DeviceCategory.isAllGoodsSortedFromLowToHighPrice(self, driver)
        assert is_good_prices_low_to_hight, "One or more prices not sorted from low to high price"
        DeviceCategory.clickDropdownOption(self, driver, "Від дорогих до дешевих")
        is_good_prices_hight_to_low = DeviceCategory.isAllGoodsSortedFromHighToLowPrice(self, driver)
        assert is_good_prices_hight_to_low, "One or more prices not sorted from high to low price"
        attach_logs(logging.INFO, 'Test was successful')

    def testAddingAndCountGoodsInBasket(self, driver):
        main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
        main_page.open()
        main_page.click_universal_category_link(driver, "Смартфони")
        SubCategory.click_universal_subcategory_menu_link(self, "Мобільні", driver)
        assert DeviceCategory.isAddedToCartGoodsCounterTextPresent(self, driver) == False, \
            "Cart Goods Counter Text isn't presented"

        DeviceCategory.clickBuyButtonByIndex(self, driver, 1)
        assert DeviceCategory.isAddedToCartGoodsCounterTextPresent(self, driver) != False, \
            "Cart Goods Counter Text isn't presented"
        logging.INFO('Test was successful')

    def test_choose_brands_and_check(self, driver):
        main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
        main_page.open()
        main_page.click_universal_category_link(driver, "Смартфони")
        SubCategory.click_universal_subcategory_menu_link(self, "Мобільні", driver)
        DeviceCategory.click_check_box_filter(self, driver, "Huawei")
        DeviceCategory.click_check_box_filter(self, driver, "Infinix")
        DeviceCategory.click_check_box_filter(self, driver, "Motorola")
        assert DeviceCategory.check_chosen_filters_contains_chosen_brands(self, driver, "Huawei"), \
            "List chosen parameters not contains this parameter"
        assert DeviceCategory.check_chosen_filters_contains_chosen_brands(self, driver, "Infinix"), \
            "List chosen parameters not contains this parameter"
        assert DeviceCategory.check_chosen_filters_contains_chosen_brands(self, driver, "Motorola"), \
            "List chosen parameters not contains this parameter"
        logging.INFO('Test was successful')
