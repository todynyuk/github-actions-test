import pytest

from data.tests_data import Users, Errors, Links
from tests.test_base import BaseTest


class TestLogin(BaseTest):

    """ Login with invalid credentials test """

    @pytest.mark.parametrize(
        "username, password, expected_message",
        [
            (Users.WRONG_USER_NAME, Users.WRONG_USER_PASSWORD, Errors.WRONG_LOGIN_MESSAGE),
        ]
    )
    def test_invalid_login(self, username, password, expected_message):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        actual_error_message = self.pages['login_page'].get_login_error_message()
        expected_error_message = expected_message
        assert expected_error_message == actual_error_message, f"The actual error message '{actual_error_message}' does not match the expected error message '{expected_error_message}'"

    """ Login with valid credentials test """

    @pytest.mark.parametrize(
        "username, password, expected_url",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD, Links.PRODUCTS),
        ]
    )
    def test_valid_login(self, username, password, expected_url):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        actual_url_after_login = self.pages['login_page'].action_get_url()
        expected_url_after_login = expected_url
        assert expected_url_after_login == actual_url_after_login, f"The actual url '{actual_url_after_login}' after logout does not match the expected url '{expected_url_after_login}'"

    """ Login with locked credentials test """

    @pytest.mark.parametrize(
        "username, password, expected_message",
        [
            (Users.LOCKED_USER_NAME, Users.LOCKED_USER_PASSWORD, Errors.LOCKED_LOGIN_MESSAGE),
        ]
    )
    def test_login_by_locked_user(self, username, password, expected_message):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        actual_error_message = self.pages['login_page'].get_login_error_message()
        expected_error_message = expected_message
        assert expected_error_message == actual_error_message, f"The actual error message '{actual_error_message}' does not match the expected error message '{expected_error_message}'"

    """ Logout test """

    @pytest.mark.parametrize(
        "username, password, expected_url",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD, Links.BASE_URL),
        ]
    )
    def test_logout(self, username, password, expected_url):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['inventory_page'].logout()
        check_form = self.pages['login_page'].check_login_form()
        actual_url_after_logout = self.pages['login_page'].action_get_url()
        expected_url_after_logout = expected_url
        assert check_form is True, "The login form does not contain all fields"
        assert expected_url_after_logout == actual_url_after_logout, f"The actual url '{actual_url_after_logout}' after logout does not match the expected url '{expected_url_after_logout}'"

    """ Mandatory password fields test """

    @pytest.mark.parametrize(
        "username, password, expected_message",
        [
            (Users.STANDARD_USER_NAME, Users.EMPTY_STRING, Errors.MANDATORY_PASSWORD),
        ]
    )
    def test_mandatory_password(self, username, password, expected_message):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['login_page'].click_login_button()
        actual_error_message_about_password = self.pages['login_page'].get_login_error_message()
        expected_error_message_about_password = expected_message
        assert expected_error_message_about_password == actual_error_message_about_password, f"The actual error message '{actual_error_message_about_password}' does not match the expected error message '{expected_error_message_about_password}'"

    """ Mandatory username fields test """

    @pytest.mark.parametrize(
        "username, password, expected_message",
        [
            (Users.EMPTY_STRING, Users.STANDARD_USER_PASSWORD, Errors.MANDATORY_USERNAME),
        ]
    )
    def test_mandatory_username(self, username, password, expected_message):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['login_page'].click_login_button()
        actual_error_message_about_username = self.pages['login_page'].get_login_error_message()
        expected_error_message_about_username = expected_message
        assert expected_error_message_about_username == actual_error_message_about_username, f"The actual error message '{actual_error_message_about_username}' does not match the expected error message '{expected_error_message_about_username}'"

    """ Close error message test """

    def test_close_error_message(self):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].click_login_button()
        self.pages['login_page'].click_login_error_button()
        actual_error_message_not_exist = self.pages['login_page'].error_login_message_not_exist()
        expected_error_message_not_exist = True
        assert expected_error_message_not_exist == actual_error_message_not_exist, f"The error message is existed on the page"
