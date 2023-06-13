import pytest

from data.tests_data import Links, Users, Errors, CheckoutPage, CartPage, OverviewPage
from tests.test_base import BaseTest


class TestCheckout(BaseTest):

    """ Open checkout page test """

    @pytest.mark.parametrize(
        "username, password, expected_title, expected_url",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD, CheckoutPage.CHECKOUT_TITLE, Links.CHECKOUT)
        ]
    )
    def test_open_checkout(self, username, password, expected_title, expected_url):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['inventory_page'].open_cart_page()
        self.pages['cart_page'].click_checkout()
        actual_checkout_title = self.pages['checkout_page'].get_checkout_page_title()
        expected_checkout_title = expected_title
        actual_checkout_url = self.pages['checkout_page'].action_get_url()
        expected_checkout_url = expected_url
        assert expected_checkout_title == actual_checkout_title, f"The actual title '{actual_checkout_title}' does not match the expected title '{expected_checkout_title}'"
        assert expected_checkout_url == actual_checkout_url, f"The actual url '{actual_checkout_url}' does not match the expected url '{expected_checkout_url}'"

    """ Back from checkout page test """

    @pytest.mark.parametrize(
        "username, password, expected_title, expected_url",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD, CartPage.CART_TITLE, Links.CART)
        ]
    )
    def test_cancel_checkout(self, username, password, expected_title, expected_url):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['inventory_page'].open_cart_page()
        self.pages['cart_page'].click_checkout()
        self.pages['checkout_page'].click_cancel_checkout()
        actual_title_after_cancel_checkout = self.pages['cart_page'].get_cart_page_title()
        expected_title_after_cancel_checkout = expected_title
        actual_url_after_cancel_checkout = self.pages['cart_page'].action_get_url()
        expected_url_after_cancel_checkout = expected_url
        assert expected_title_after_cancel_checkout == actual_title_after_cancel_checkout, f"The actual title '{actual_title_after_cancel_checkout}' does not match the expected title '{expected_title_after_cancel_checkout}'"
        assert expected_url_after_cancel_checkout == actual_url_after_cancel_checkout, f"The actual url '{expected_url_after_cancel_checkout}' does not match the expected url '{actual_url_after_cancel_checkout}'"

    """ Fill checkout form test """

    @pytest.mark.parametrize(
        "username, password, expected_title, expected_url",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD, OverviewPage.OVERVIEW_TITLE, Links.OVERVIEW)
        ]
    )
    def test_fill_checkout(self, username, password, expected_title, expected_url):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['inventory_page'].open_cart_page()
        self.pages['cart_page'].click_checkout()
        check_form = self.pages['checkout_page'].check_checkout_form()
        assert check_form is True, "The checkout form does not contain all fields"
        first_name = self.data['generator'].first_name()
        last_name = self.data['generator'].last_name()
        zip_code = self.data['generator'].zip_code()
        self.pages['checkout_page'].fill_checkout_form(first_name, last_name, zip_code)
        assert self.pages[
                   'checkout_page'].get_first_name() == first_name, f"The first name field does not contain value"
        assert self.pages['checkout_page'].get_last_name() == last_name, f"The last name field does not contain value"
        assert self.pages['checkout_page'].get_zip_code() == zip_code, f"The zip code field does not contain value"
        self.pages['checkout_page'].click_continue_checkout()
        actual_title_after_continue_checkout = self.pages['overview_page'].get_overview_page_title()
        expected_title_after_continue_checkout = expected_title
        actual_url_after_continue_checkout = self.pages['overview_page'].action_get_url()
        expected_url_after_continue_checkout = expected_url
        assert actual_title_after_continue_checkout == expected_title_after_continue_checkout, f"The actual title '{actual_title_after_continue_checkout}' does not match the expected title '{expected_title_after_continue_checkout}'"
        assert actual_url_after_continue_checkout == expected_url_after_continue_checkout, f"The actual url '{actual_url_after_continue_checkout}' does not match the expected url '{expected_url_after_continue_checkout}'"

    """ Mandatory first name fields test """

    @pytest.mark.parametrize(
        "username, password, expected_message",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD, Errors.MANDATORY_FIRSTNAME)
        ]
    )
    def test_mandatory_first_name(self, username, password, expected_message):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['inventory_page'].open_cart_page()
        self.pages['cart_page'].click_checkout()
        last_name = self.data['generator'].last_name()
        zip_code = self.data['generator'].zip_code()
        self.pages['checkout_page'].enter_last_name(last_name)
        self.pages['checkout_page'].enter_zip_code(zip_code)
        self.pages['checkout_page'].click_continue_checkout()
        actual_error_message_about_first_name = self.pages['checkout_page'].get_checkout_error_message()
        expected_error_message_about_first_name = expected_message
        assert expected_error_message_about_first_name == actual_error_message_about_first_name, f"The actual error message '{actual_error_message_about_first_name}' does not match the expected error message '{expected_error_message_about_first_name}'"

    """ Mandatory last name fields test """

    @pytest.mark.parametrize(
        "username, password, expected_message",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD, Errors.MANDATORY_LASTNAME)
        ]
    )
    def test_mandatory_last_name(self, username, password, expected_message):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['inventory_page'].open_cart_page()
        self.pages['cart_page'].click_checkout()
        first_name = self.data['generator'].first_name()
        zip_code = self.data['generator'].zip_code()
        self.pages['checkout_page'].enter_first_name(first_name)
        self.pages['checkout_page'].enter_zip_code(zip_code)
        self.pages['checkout_page'].click_continue_checkout()
        actual_error_message_about_last_name = self.pages['checkout_page'].get_checkout_error_message()
        expected_error_message_about_last_name = expected_message
        assert expected_error_message_about_last_name == actual_error_message_about_last_name, f"The actual error message '{actual_error_message_about_last_name}' does not match the expected error message '{expected_error_message_about_last_name}'"

    """ Mandatory zip code fields test """

    @pytest.mark.parametrize(
        "username, password, expected_message",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD, Errors.MANDATORY_ZIP)
        ]
    )
    def test_mandatory_zip_code(self, username, password, expected_message):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['inventory_page'].open_cart_page()
        self.pages['cart_page'].click_checkout()
        first_name = self.data['generator'].first_name()
        last_name = self.data['generator'].last_name()
        self.pages['checkout_page'].enter_first_name(first_name)
        self.pages['checkout_page'].enter_last_name(last_name)
        self.pages['checkout_page'].click_continue_checkout()
        actual_error_message_about_zip_code = self.pages['checkout_page'].get_checkout_error_message()
        expected_error_message_about_zip_code = expected_message
        assert expected_error_message_about_zip_code == actual_error_message_about_zip_code, f"The actual error message '{actual_error_message_about_zip_code}' does not match the expected error message '{expected_error_message_about_zip_code}'"

    """ Close error message test """

    @pytest.mark.parametrize(
        "username, password",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD)
        ]
    )
    def test_close_error_message(self, username, password):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['inventory_page'].open_cart_page()
        self.pages['cart_page'].click_checkout()
        self.pages['checkout_page'].click_continue_checkout()
        self.pages['checkout_page'].click_checkout_error_button()
        actual_error_message_not_exist = self.pages['checkout_page'].error_checkout_message_not_exist()
        expected_error_message_not_exist = True
        assert expected_error_message_not_exist == actual_error_message_not_exist, f"The error message is existed on the page"
