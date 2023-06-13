import pytest

from data.tests_data import Users, InventoryPage
from tests.test_base import BaseTest


class TestInventory(BaseTest):

    """ Check list of menu links """

    @pytest.mark.parametrize(
        "username, password, expected_links",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD, InventoryPage.HAMBURGER_MENU_LIST),
        ]
    )
    def test_check_menu_links(self, username, password, expected_links):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['inventory_page'].open_hamburger_menu()
        actual_menu_links = self.pages['inventory_page'].get_menu_links_text()
        expected_menu_links = expected_links
        assert actual_menu_links == expected_menu_links, f"List of menu links {actual_menu_links} does not match the expected {expected_menu_links}"

    """ Purchase one item test """

    @pytest.mark.parametrize(
        "username, password",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD)
        ]
    )
    def test_purchase_one_item(self, username, password):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['inventory_page'].open_random_product()
        actual_product_price = self.pages['product_page'].get_product_price()
        self.pages['product_page'].click_add_product_to_cart()
        self.pages['inventory_page'].open_cart_page()
        all_cart_item_prices = self.pages['cart_page'].get_list_of_cart_item_prices()
        assert self.pages['cart_page'].find_value_in_data(actual_product_price, all_cart_item_prices) is True, f"The product price does not match to item price from cart page"
        expected_cart_calc_prices = self.pages['cart_page'].get_list_of_cart_calc_prices()
        self.pages['cart_page'].click_checkout()
        first_name = self.data['generator'].first_name()
        last_name = self.data['generator'].last_name()
        zip_code = self.data['generator'].zip_code()
        self.pages['checkout_page'].fill_checkout_form(first_name, last_name, zip_code)
        self.pages['checkout_page'].click_continue_checkout()
        actual_overview_total_prices = self.pages['overview_page'].get_list_of_overview_total_prices()
        expected_overview_calc_prices = self.pages['overview_page'].get_list_of_overview_calc_prices()
        assert expected_cart_calc_prices == actual_overview_total_prices, f"The item prices from cart page does not match to item price from overview page"
        assert expected_overview_calc_prices == actual_overview_total_prices, f"The item prices from overview page does not match to total_prices from overview page"
        self.pages['overview_page'].click_finish_overview()
        expected_cart_item_count_not_exist = self.pages['order_page'].check_cart_count_not_exist()
        assert expected_cart_item_count_not_exist is True, f"The cart contains items"

    """ Purchase all items test """

    @pytest.mark.parametrize(
        "username, password",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD)
        ]
    )
    def test_purchase_all_item(self, username, password):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        all_product_names = self.pages['inventory_page'].get_list_of_product_names()
        all_product_prices = self.pages['inventory_page'].get_list_of_product_prices()
        assert len(all_product_names) > 0, "No products found on inventory page"
        self.pages['inventory_page'].add_all_to_cart()
        self.pages['inventory_page'].open_cart_page()
        all_cart_item_names = self.pages['cart_page'].get_list_of_cart_item_names()
        all_cart_item_prices = self.pages['cart_page'].get_list_of_cart_item_prices()
        assert all_product_names == all_cart_item_names, f"The product names in inventory do not match to item names from cart page"
        assert all_product_prices == all_cart_item_prices, f"The product prices in inventory do not match to item prices from cart page"
        expected_cart_calc_prices = self.pages['cart_page'].get_list_of_cart_calc_prices()
        self.pages['cart_page'].click_checkout()
        first_name = self.data['generator'].first_name()
        last_name = self.data['generator'].last_name()
        zip_code = self.data['generator'].zip_code()
        self.pages['checkout_page'].fill_checkout_form(first_name, last_name, zip_code)
        self.pages['checkout_page'].click_continue_checkout()
        actual_overview_total_prices = self.pages['overview_page'].get_list_of_overview_total_prices()
        expected_overview_calc_prices = self.pages['overview_page'].get_list_of_overview_calc_prices()
        assert expected_cart_calc_prices == actual_overview_total_prices, f"The item prices from cart page does not match to item price from overview page"
        assert expected_overview_calc_prices == actual_overview_total_prices, f"The item prices from overview page does not match to total_prices from overview page"
        self.pages['overview_page'].click_finish_overview()
        expected_cart_item_count_not_exist = self.pages['order_page'].check_cart_count_not_exist()
        assert expected_cart_item_count_not_exist is True, f"The cart contains items"

    """ Add products to cart and then remove them from cart test """

    @pytest.mark.parametrize(
        "username, password",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD)
        ]
    )
    def test_add_to_cart(self, username, password):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        all_product_elements = self.pages['inventory_page'].get_all_product_elements()
        self.pages['inventory_page'].add_all_to_cart()
        actual_cart_item_count = self.pages['inventory_page'].get_cart_item_count()
        expected_cart_item_count = len(all_product_elements)
        assert expected_cart_item_count == actual_cart_item_count, f"The cart does not contain all products"
        self.pages['inventory_page'].remove_all_from_cart()
        expected_cart_item_count_not_exist = self.pages['inventory_page'].check_cart_count_not_exist()
        assert expected_cart_item_count_not_exist is True, f"The cart contains items"

    """ Sorting products in alphabetical order test """

    @pytest.mark.parametrize(
        "username, password",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD)
        ]
    )
    def test_sort_a_to_z(self, username, password):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['inventory_page'].sort_products_a_to_z()
        all_product_names = self.pages['inventory_page'].get_list_of_product_names()
        for i in range(len(all_product_names) - 1):
            assert all_product_names[i] <= all_product_names[i + 1], "Products {0} and {1} are not ordered correctly.".format(all_product_names[i], all_product_names[i + 1])

    """ Sorting products in reverse alphabetical order test """

    @pytest.mark.parametrize(
        "username, password",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD)
        ]
    )
    def test_sort_z_to_a(self, username, password):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['inventory_page'].sort_products_z_to_a()
        all_product_names = self.pages['inventory_page'].get_list_of_product_names()
        for i in range(len(all_product_names) - 1):
            assert all_product_names[i] >= all_product_names[i + 1], "Products {0} and {1} are not ordered correctly.".format(all_product_names[i], all_product_names[i + 1])

    """ Sorting products by price in ascending order test """

    @pytest.mark.parametrize(
        "username, password",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD)
        ]
    )
    def test_sort_low_to_high(self, username, password):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['inventory_page'].sort_products_low_to_high()
        all_product_prices = self.pages['inventory_page'].get_list_of_product_prices()
        for i in range(len(all_product_prices) - 1):
            assert all_product_prices[i] <= all_product_prices[i + 1], "Products {0} and {1} are not ordered correctly.".format(all_product_prices[i], all_product_prices[i + 1])

    """ Sorting products by price in descending order test """

    @pytest.mark.parametrize(
        "username, password",
        [
            (Users.STANDARD_USER_NAME, Users.STANDARD_USER_PASSWORD)
        ]
    )
    def test_sort_high_to_low(self, username, password):
        self.pages['login_page'].open_login_page()
        self.pages['login_page'].login(username, password)
        self.pages['inventory_page'].sort_products_high_to_low()
        all_product_prices = self.pages['inventory_page'].get_list_of_product_prices()
        for i in range(len(all_product_prices) - 1):
            assert all_product_prices[i] >= all_product_prices[i + 1], "Products {0} and {1} are not ordered correctly.".format(all_product_prices[i], all_product_prices[i + 1])
