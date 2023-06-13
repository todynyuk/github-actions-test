from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as expected

from data.tests_data import Links


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Links.BASE_URL
        self.wait = wait(self.driver, 15, 0.3)

    """ Init a site """
    def init_site(self) -> None:
        self.driver.get(self.url)

    """ Open a site """
    def open_url(self, url) -> None:
        self.driver.get(url)

    """ Find a visible element """
    def element_is_visible(self, element) -> WebElement:
        self.go_to_element(self.element_is_present(element))
        return self.wait.until(expected.visibility_of_element_located(element))

    """ Find visible elements """
    def elements_are_visible(self, element) -> list[WebElement]:
        return self.wait.until(expected.visibility_of_all_elements_located(element))

    """ Find a present element """
    def element_is_present(self, element) -> WebElement:
        return self.wait.until(expected.presence_of_element_located(element))

    """ Find present elements """
    def elements_are_present(self, element) -> list[WebElement]:
        return self.wait.until(expected.presence_of_all_elements_located(element))

    """ Find a not visible element """
    def element_is_not_visible(self, element) -> bool:
        return self.wait.until(expected.invisibility_of_element_located(element))

    """ Find clickable elements """
    def element_is_clickable(self, element) -> WebElement:
        return self.wait.until(expected.element_to_be_clickable(element))

    """ Scroll to bottom """
    def scroll_to_bottom(self) -> None:
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    """ Go to specified element """
    def go_to_element(self, element) -> None:
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    """ Double click """
    def action_double_click(self, element) -> None:
        action = ActionChains(self.driver)
        self.highlight_element(element, "green")
        action.double_click(element)
        action.perform()

    """ Right click """
    def action_right_click(self, element) -> None:
        action = ActionChains(self.driver)
        self.highlight_element(element, "green")
        action.context_click(element)
        action.perform()

    """ Left click """
    def action_left_click(self, element) -> None:
        action = ActionChains(self.driver)
        self.highlight_element(element, "green")
        action.click(element)
        action.perform()

    """ Click on items in list """
    def action_left_click_on_elements(self, elements: list) -> None:
        for element in elements:
            self.action_left_click(element)

    """ Fill text """
    def action_fill_text(self, element, txt: str) -> None:
        element: WebElement = self.wait.until(expected.element_to_be_clickable(element))
        element.clear()
        self.highlight_element(element, "green")
        element.send_keys(txt)

    """ Clear text """
    def action_clear_text(self, element) -> None:
        element: WebElement = self.wait.until(expected.element_to_be_clickable(element))
        self.highlight_element(element, "green")
        element.clear()

    """ Get text """
    def action_get_text(self, element) -> str:
        element: WebElement = self.wait.until(expected.visibility_of_element_located(element))
        self.highlight_element(element, "green")
        return element.text

    """ Get text from elements """
    def action_get_text_from_elements(self, elements: list[WebElement]) -> list[str]:
        return [element.text for element in elements]

    """ Get element by text """
    def get_element_by_text(self, elements: list[WebElement], name: str) -> WebElement:
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]

    """ Get attribute """
    def action_get_attr(self, element, attribute) -> str:
        element: WebElement = self.wait.until(expected.visibility_of_element_located(element))
        self.highlight_element(element, "green")
        return element.get_attribute(attribute)

    """ Get attribute from elements """
    def action_get_attr_from_elements(self, elements: list[WebElement], attribute) -> list[str]:
        return [element.get_attribute(attribute) for element in elements]

    """ Get page url """
    def action_get_url(self) -> str:
        pages_url = self.driver.current_url
        return pages_url

    """ Drag and drop by offset """
    def action_drag_and_drop_by_offset(self, element, x_coords, y_coords) -> None:
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.perform()

    """ Drag and drop element to element """
    def action_drag_and_drop_to_element(self, what, where) -> None:
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()

    """ Move cursor to element """
    def action_move_to_element(self, element) -> None:
        action = ActionChains(self.driver)
        self.wait.until(expected.visibility_of(element))
        action.move_to_element(element)
        action.perform()

    """ Highlight element """
    def highlight_element(self, element, color: str) -> None:
        original_style = element.get_attribute("style")
        new_style = f"background-color: {color}; border: 1px solid #000; {original_style}"
        self.driver.execute_script(
            "var tmpArguments = arguments;setTimeout(function () {tmpArguments[0].setAttribute('style', '"
            + new_style + "');},0);", element)
        self.driver.execute_script(
            "var tmpArguments = arguments;setTimeout(function () {tmpArguments[0].setAttribute('style', '"
            + original_style + "');},400);", element)

    """ Find value in data """
    def find_value_in_data(self, value, data: list) -> bool:
        if value in data:
            return True
        else:
            return False
