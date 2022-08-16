import time

from selenium.webdriver.common.by import By
from test.functional.base import FunctionalTest


class TestMobile(FunctionalTest):

    def get_suggestions(self):
        return self.browser.find_elements(By.CLASS_NAME, "mobile-suggestion")

    def test_search_bar(self):
        # Marge visits the webpage on her iPhone 12
        self.browser.get(self.base_url)
        self.browser.set_window_size(390, 844)
        content_wrapper = self.browser.find_element(By.ID, "content-wrapper")

        # She notices that the dimensions of the webpage have changed for mobile
        self.assertEqual(content_wrapper.value_of_css_property("max-width"), "none")
