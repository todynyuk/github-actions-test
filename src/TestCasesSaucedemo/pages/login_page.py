from locators.page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    login_page = LoginPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    """ Open login page """
    def open_login_page(self) -> None:
        self.init_site()

    """ Enter a password in login form """
    def enter_password(self, password) -> None:
        self.action_fill_text(self.element_is_visible(self.login_page.PASSWORD), password)

    """ Enter a username in login form """
    def enter_username(self, username) -> None:
        self.action_fill_text(self.element_is_visible(self.login_page.USERNAME), username)

    """ Click login button """
    def click_login_button(self) -> None:
        self.action_left_click(self.element_is_visible(self.login_page.LOGIN_BUTTON))

    """ Login in app """
    def login(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    """ Clear username field """
    def clear_username(self) -> None:
        self.action_clear_text(self.element_is_visible(self.login_page.USERNAME))

    """ Clear password field """
    def clear_password(self) -> None:
        self.action_clear_text(self.element_is_visible(self.login_page.PASSWORD))

    """ Clear all login form fields """
    def clear_login_form(self) -> None:
        self.clear_username()
        self.clear_password()

    """ Check login form fields """
    def check_login_form(self) -> bool:
        username = self.element_is_visible(self.login_page.USERNAME)
        password = self.element_is_visible(self.login_page.PASSWORD)
        login_button = self.element_is_visible(self.login_page.LOGIN_BUTTON)
        return username is not None and password is not None and login_button is not None

    """ Check error message exists """
    def error_login_message_exists(self) -> bool:
        error_message = self.element_is_visible(self.login_page.ERROR_MESSAGE)
        return error_message is not None

    """ Check error message not-exist """
    def error_login_message_not_exist(self) -> bool:
        error_message = self.element_is_not_visible(self.login_page.ERROR_MESSAGE)
        return error_message

    """ Get error message text """
    def get_login_error_message(self) -> str | None:
        if self.error_login_message_exists():
            return self.action_get_text(self.login_page.ERROR_MESSAGE)
        else:
            return None

    """ Click error button """
    def click_login_error_button(self) -> None:
        self.action_left_click(self.element_is_visible(self.login_page.ERROR_BUTTON))