from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from test.functional.base import FunctionalTest


class TestWebpageLayout(FunctionalTest):        

    def test_layout_and_styling(self):
        # Marge visits the webpage and notices a nice centered search bar.
        self.browser.get(self.base_url)
        self.browser.set_window_size(1024, 768)
        searchbar = self.browser.find_element(By.ID, "trie-search-bar")
        self.assertAlmostEqual(
            searchbar.location["x"] + searchbar.size["width"] / 2,
            1008 / 2, # screen actual width / 2
            delta=10
        )

        # Interested, she moves her mouse over it. Marge notices the search
        # bar appears to come to life!
        ActionChains(self.browser).move_to_element(searchbar).perform()
        self.assertFalse(searchbar.value_of_css_property("box-shadow") is None)


    def test_mobile_search_bar(self):
        # Marge visits the webpage on her iPhone 12
        self.browser.get(self.base_url)
        self.browser.set_window_size(390, 844)
        content_wrapper = self.browser.find_element(By.ID, "content-wrapper")

        # She notices that the dimensions of the webpage have changed for mobile
        self.assertEqual(content_wrapper.value_of_css_property("max-width"), "none")