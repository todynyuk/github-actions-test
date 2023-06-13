import pytest

from data.tests_data import Links, Users, OrderPage, InventoryPage
from tests.test_base import BaseTest


class TestOrder(BaseTest):

    """ Open order page test """

    @pytest.mark.parametrize(
        "username, password, expected_title, expected_subtitle, expected_text, expected_url",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD, OrderPage.ORDER_TITLE, OrderPage.ORDER_SUBTITLE, OrderPage.ORDER_TEXT, Links.ORDER),
        ]
    )
    def test_open_order(self, username, password, expected_title, expected_subtitle, expected_text, expected_url):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['inventory_page'].open_random_product()
        self.pages['product_page'].click_add_product_to_cart()
        self.pages['product_page'].open_cart_page()
        self.pages['cart_page'].click_checkout()
        first_name = self.data['generator'].first_name()
        last_name = self.data['generator'].last_name()
        zip_code = self.data['generator'].zip_code()
        self.pages['checkout_page'].fill_checkout_form(first_name, last_name, zip_code)
        self.pages['checkout_page'].click_continue_checkout()
        self.pages['overview_page'].click_finish_overview()
        expected_cart_item_count_not_exist = self.pages['order_page'].check_cart_count_not_exist()
        actual_order_title = self.pages['order_page'].get_order_page_title()
        expected_order_title = expected_title
        actual_order_url = self.pages['order_page'].action_get_url()
        expected_order_url = expected_url
        actual_order_subtitle = self.pages['order_page'].get_order_page_subtitle()
        expected_order_subtitle = expected_subtitle
        actual_order_text = self.pages['order_page'].get_order_page_text()
        expected_order_text = expected_text
        assert expected_cart_item_count_not_exist is True, f"The cart contains items"
        assert expected_order_title == actual_order_title, f"The actual title '{actual_order_title}' does not match the expected title '{expected_order_title}'"
        assert expected_order_url == actual_order_url, f"The actual url '{actual_order_url}' does not match the expected url '{expected_order_url}'"
        assert expected_order_subtitle == actual_order_subtitle, f"The actual subtitle '{actual_order_subtitle}' does not match the expected subtitle '{expected_order_subtitle}'"
        assert expected_order_text == actual_order_text, f"The actual text '{actual_order_text}' does not match the expected text '{expected_order_text}'"

    """ Back from order page test """

    @pytest.mark.parametrize(
        "username, password, expected_title, expected_url",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD, InventoryPage.PRODUCTS_TITLE, Links.PRODUCTS),
        ]
    )
    def test_back_from_order(self, username, password, expected_title, expected_url):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['inventory_page'].open_random_product()
        self.pages['product_page'].click_add_product_to_cart()
        self.pages['product_page'].open_cart_page()
        self.pages['cart_page'].click_checkout()
        first_name = self.data['generator'].first_name()
        last_name = self.data['generator'].last_name()
        zip_code = self.data['generator'].zip_code()
        self.pages['checkout_page'].fill_checkout_form(first_name, last_name, zip_code)
        self.pages['checkout_page'].click_continue_checkout()
        self.pages['overview_page'].click_finish_overview()
        self.pages['order_page'].click_order_back_button()
        actual_title_after_back_from_order = self.pages['inventory_page'].get_products_page_title()
        expected_title_after_back_from_order = expected_title
        actual_url_after_back_from_order = self.pages['inventory_page'].action_get_url()
        expected_url_after_back_from_order = expected_url
        assert expected_title_after_back_from_order == actual_title_after_back_from_order, f"The actual title '{actual_title_after_back_from_order}' does not match the expected title '{expected_title_after_back_from_order}'"
        assert expected_url_after_back_from_order == actual_url_after_back_from_order, f"The actual url '{expected_url_after_back_from_order}' does not match the expected url '{actual_url_after_back_from_order}'"