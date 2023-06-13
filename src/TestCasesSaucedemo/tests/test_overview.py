import pytest

from data.tests_data import Links, Users, OverviewPage, InventoryPage, OrderPage
from tests.test_base import BaseTest


class TestOverview(BaseTest):

    """ Open overview page test """

    @pytest.mark.parametrize(
        "username, password, expected_title, expected_url",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD, OverviewPage.OVERVIEW_TITLE, Links.OVERVIEW),
        ]
    )
    def test_open_overview(self, username, password, expected_title, expected_url):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['inventory_page'].open_cart_page()
        self.pages['cart_page'].click_checkout()
        first_name = self.data['generator'].first_name()
        last_name = self.data['generator'].last_name()
        zip_code = self.data['generator'].zip_code()
        self.pages['checkout_page'].fill_checkout_form(first_name, last_name, zip_code)
        self.pages['checkout_page'].click_continue_checkout()
        actual_overview_title = self.pages['overview_page'].get_overview_page_title()
        expected_overview_title = expected_title
        actual_overview_url = self.pages['overview_page'].action_get_url()
        expected_overview_url = expected_url
        assert expected_overview_title == actual_overview_title, f"The actual title '{actual_overview_title}' does not match the expected title '{expected_overview_title}'"
        assert expected_overview_url == actual_overview_url, f"The actual url '{actual_overview_url}' does not match the expected url '{expected_overview_url}'"

    """ Back from overview page test """

    @pytest.mark.parametrize(
        "username, password, expected_title, expected_url",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD, InventoryPage.PRODUCTS_TITLE, Links.PRODUCTS),
        ]
    )
    def test_cancel_overview(self, username, password, expected_title, expected_url):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['inventory_page'].open_cart_page()
        self.pages['cart_page'].click_checkout()
        first_name = self.data['generator'].first_name()
        last_name = self.data['generator'].last_name()
        zip_code = self.data['generator'].zip_code()
        self.pages['checkout_page'].fill_checkout_form(first_name, last_name, zip_code)
        self.pages['checkout_page'].click_continue_checkout()
        self.pages['overview_page'].click_cancel_overview()
        actual_title_after_cancel_overview = self.pages['inventory_page'].get_products_page_title()
        expected_title_after_cancel_overview = expected_title
        actual_url_after_cancel_overview = self.pages['inventory_page'].action_get_url()
        expected_url_after_cancel_overview = expected_url
        assert expected_title_after_cancel_overview == actual_title_after_cancel_overview, f"The actual title '{actual_title_after_cancel_overview}' does not match the expected title '{expected_title_after_cancel_overview}'"
        assert expected_url_after_cancel_overview == actual_url_after_cancel_overview, f"The actual url '{expected_url_after_cancel_overview}' does not match the expected url '{actual_url_after_cancel_overview}'"

    """ Finish overview test """

    @pytest.mark.parametrize(
        "username, password, expected_title, expected_url",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD, OrderPage.ORDER_TITLE, Links.ORDER),
        ]
    )
    def test_finish_overview(self, username, password, expected_title, expected_url):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['inventory_page'].open_cart_page()
        self.pages['cart_page'].click_checkout()
        first_name = self.data['generator'].first_name()
        last_name = self.data['generator'].last_name()
        zip_code = self.data['generator'].zip_code()
        self.pages['checkout_page'].fill_checkout_form(first_name, last_name, zip_code)
        self.pages['checkout_page'].click_continue_checkout()
        self.pages['overview_page'].click_finish_overview()
        actual_title_after_finish_overview = self.pages['order_page'].get_order_page_title()
        expected_title_after_finish_overview = expected_title
        actual_url_after_finish_overview = self.pages['order_page'].action_get_url()
        expected_url_after_finish_overview = expected_url
        assert expected_title_after_finish_overview == actual_title_after_finish_overview, f"The actual title '{actual_title_after_finish_overview}' does not match the expected title '{expected_title_after_finish_overview}'"
        assert expected_url_after_finish_overview == actual_url_after_finish_overview, f"The actual url '{expected_url_after_finish_overview}' does not match the expected url '{actual_url_after_finish_overview}'"
