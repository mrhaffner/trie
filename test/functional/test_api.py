from selenium.webdriver.common.by import By
from test.functional.base import FunctionalTest


class TestApi(FunctionalTest):

    def test_api_loads(self):
        self.browser.get(self.base_url + "api")
        element = self.browser.find_element(By.TAG_NAME, "pre")
        self.assertEqual(element.text, "\"Welcome to the API.\"")