import pytest

class BaseTest:
    @pytest.fixture(autouse=True)
    def injector(self, pages, data):
        self.pages = pages
        self.data = data