import pytest

from data.tests_data import Links, Users, CartPage, InventoryPage
from tests.test_base import BaseTest


class TestCart(BaseTest):

    """ Open cart page test """

    @pytest.mark.parametrize(
        "username, password, expected_title, expected_url",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD, CartPage.CART_TITLE, Links.CART),
        ],
    )
    def test_open_cart(self, username, password, expected_title, expected_url):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['inventory_page'].open_cart_page()
        actual_cart_title = self.pages['cart_page'].get_cart_page_title()
        expected_cart_title = expected_title
        actual_cart_url = self.pages['cart_page'].action_get_url()
        expected_cart_url = expected_url
        assert expected_cart_title == actual_cart_title, f"The actual title '{actual_cart_title}' does not match the expected title '{expected_cart_title}'"
        assert expected_cart_url == actual_cart_url, f"The actual url '{actual_cart_url}' does not match the expected url '{expected_cart_url}'"

    """ Back from cart page test """

    @pytest.mark.parametrize(
        "username, password, expected_title, expected_url",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD, InventoryPage.PRODUCTS_TITLE, Links.PRODUCTS),
        ],
    )
    def test_click_continue_shopping(self, username, password, expected_title, expected_url):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['inventory_page'].open_cart_page()
        self.pages['cart_page'].click_continue_shopping()
        actual_title_after_back_from_cart = self.pages['inventory_page'].get_products_page_title()
        expected_title_after_back_from_cart = expected_title
        actual_url_after_back_from_cart = self.pages['inventory_page'].action_get_url()
        expected_url_after_back_from_cart = expected_url
        assert expected_title_after_back_from_cart == actual_title_after_back_from_cart, f"The actual title '{actual_title_after_back_from_cart}' does not match the expected title '{expected_title_after_back_from_cart}'"
        assert expected_url_after_back_from_cart == actual_url_after_back_from_cart, f"The actual url '{expected_url_after_back_from_cart}' does not match the expected url '{actual_url_after_back_from_cart}'"

    """ Remove all from cart test """

    @pytest.mark.parametrize(
        "username, password",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD),
        ],
    )
    def test_remove_all_from_cart(self, username, password):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['inventory_page'].add_all_to_cart()
        actual_product_count = self.pages['inventory_page'].get_products_count()
        expected_cart_item_count = self.pages['inventory_page'].get_cart_item_count()
        assert expected_cart_item_count == actual_product_count, f"The actual product count '{actual_product_count}' does not match the expected cart item count '{expected_cart_item_count}'"
        self.pages['inventory_page'].open_cart_page()
        self.pages['cart_page'].remove_all_from_cart()
        expected_cart_is_empty = self.pages['cart_page'].check_cart_is_empty()
        expected_cart_item_count_not_exist = self.pages['cart_page'].check_cart_count_not_exist()
        assert expected_cart_is_empty is True, f"The cart contains items"
        assert expected_cart_item_count_not_exist is True, f"The cart contains items"

