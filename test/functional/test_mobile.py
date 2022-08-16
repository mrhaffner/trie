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
        search_overlay = self.browser.find_element(By.ID, "mobile-search-overlay")
        searchbar = self.browser.find_element(By.ID, "trie-search-bar")
        input = self.browser.find_element(By.ID, "mobile-search-input")
        close_search_button = self.browser.find_element(By.ID, "close-mobile-search-button")

        # She notices that the search bar is is smaller to accomodate her screen size
        self.assertEqual(searchbar.size["width"], 350)

        # When Marge clicks on the searchbar, she notices a search interface takes over
        # the entire screen
        searchbar.click()
        time.sleep(1)
        self.assertFalse(search_overlay.get_attribute("hidden"))
        self.assertTrue(search_overlay.is_displayed())

        # Marge decides to type in a word and notices a list of good suggestions appear.
        input.send_keys("a")
        time.sleep(1)
        suggestions = self.get_suggestions()
        suggestions_text = [suggestion.text for suggestion in suggestions]
        self.assertEqual(["app", "apple", "apple orchard"], suggestions_text)

        # Marge deletes the word she entered and notices the suggestions disappear.
        input.send_keys("p")
        input.clear()
        time.sleep(1)
        suggestions = self.get_suggestions()
        self.assertTrue(len(suggestions) == 0)


        # She is done with searching, so she clicks the "x" to close the search interface.
        close_search_button.click()
        time.sleep(1)
        self.assertTrue(search_overlay.get_attribute("hidden"))
        self.assertFalse(search_overlay.is_displayed())

        # non-mobile searchbar isn't focused?
