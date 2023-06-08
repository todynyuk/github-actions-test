import time
from pages.main_page import MainPage
import pytest
import logging

class TestsRozetkaMainPageSearch:

    @pytest.mark.label("Search", "correct")
    def test_correct_search(self, driver):
        main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
        main_page.open()
        search_text = "Agm A9"
        main_page.set_search_input(search_text)
        main_page.click_search_button()
        logging.INFO('Test was successful')
        assert main_page.verify_is_search_brand_present_in_goods_title(search_text), "Search text not" \
                                                                                     " contains in all " \
                                                                                     "goods title texts"

    @pytest.mark.label("Search", "Incorrect")
    def test_incorrect_search(self, driver):
        main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
        main_page.open()
        search_text = "hgvhvg"
        main_page.set_search_input(search_text)
        main_page.click_search_button()
        logging.INFO('Test was successful')
        assert main_page.verify_wrong_search_request(), "Wrong request text isn`t presented"
