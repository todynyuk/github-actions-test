from locators.page_locators import CheckoutPageLocators
from pages.cart_page import CartPage


class CheckoutPage(CartPage):
    checkout = CheckoutPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    """ Get checkout page title """
    def get_checkout_page_title(self) -> str:
        return self.action_get_text(self.checkout.PAGE_TITLE)

    """ Enter a first name in checkout form """
    def enter_first_name(self, first_name) -> None:
        self.action_fill_text(self.element_is_visible(self.checkout.FIRST_NAME), first_name)

    """ Enter a last name in checkout form """
    def enter_last_name(self, last_name) -> None:
        self.action_fill_text(self.element_is_visible(self.checkout.LAST_NAME), last_name)

    """ Enter a zip code in checkout form """
    def enter_zip_code(self, zip_code) -> None:
        self.action_fill_text(self.element_is_visible(self.checkout.ZIP_CODE), zip_code)

    """ Filing checkout form fields """
    def fill_checkout_form(self, first_name: str, last_name: str, zip_code: int) -> None:
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_zip_code(zip_code)

    """ Check checkout fields """
    def check_checkout_form(self) -> bool:
        first_name = self.element_is_visible(self.checkout.FIRST_NAME)
        last_name = self.element_is_visible(self.checkout.LAST_NAME)
        zip_code = self.element_is_visible(self.checkout.ZIP_CODE)
        return first_name is not None and last_name is not None and zip_code is not None

    """ Get first name """
    def get_first_name(self) -> str:
        return self.action_get_attr(self.checkout.FIRST_NAME, "value")

    """ Get last name """
    def get_last_name(self) -> str:
        return self.action_get_attr(self.checkout.LAST_NAME, "value")

    """ Get zip code """
    def get_zip_code(self) -> str:
        return self.action_get_attr(self.checkout.ZIP_CODE, "value")

    """ Clear first name field """
    def clear_first_name(self) -> None:
        self.action_clear_text(self.element_is_visible(self.checkout.FIRST_NAME))

    """ Clear last name field """
    def clear_last_name(self) -> None:
        self.action_clear_text(self.element_is_visible(self.checkout.LAST_NAME))

    """ Clear zip code field """
    def clear_zip_code(self) -> None:
        self.action_clear_text(self.element_is_visible(self.checkout.ZIP_CODE))

    """ Clear all checkout form fields """
    def clear_checkout_form(self) -> None:
        self.clear_first_name()
        self.clear_last_name()
        self.clear_zip_code()

    """ Check error message exists """
    def error_checkout_message_exists(self) -> bool:
        error_message = self.element_is_visible(self.checkout.ERROR_MESSAGE)
        return error_message is not None

    """ Check error message not-exist """
    def error_checkout_message_not_exist(self) -> bool:
        error_message = self.element_is_not_visible(self.checkout.ERROR_MESSAGE)
        return error_message

    """ Get error message text """
    def get_checkout_error_message(self) -> str | None:
        if self.error_checkout_message_exists():
            return self.action_get_text(self.checkout.ERROR_MESSAGE)
        else:
            return None

    """ Click error button """
    def click_checkout_error_button(self) -> None:
        self.action_left_click(self.element_is_visible(self.checkout.ERROR_BUTTON))

    """ Click cancel button """
    def click_cancel_checkout(self) -> None:
        self.action_left_click(self.element_is_visible(self.checkout.CANCEL_BUTTON))

    """ Click continue button """
    def click_continue_checkout(self) -> None:
        self.action_left_click(self.element_is_visible(self.checkout.CONTINUE_BUTTON))