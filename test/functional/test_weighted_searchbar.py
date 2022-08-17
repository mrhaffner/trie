import time
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from test.functional.base import FunctionalTest


class TestWeightedTrieSearchBar(FunctionalTest):

    def get_suggestions(self) -> List[WebElement]:
        container = self.browser.find_element(By.ID, "weighted-suggestions")
        parent = container.find_elements(By.TAG_NAME, "ul")
        return parent[0].find_elements(By.CLASS_NAME, "suggestion")  if parent else []


    def test_weighted_search_bar_behavior(self) -> None:
        # Marge visits the webpage exited to try out the search bar.
        self.browser.get(self.base_url)
        searchbar = self.browser.find_element(By.ID, "weighted-trie-search-bar")
        h1 = self.browser.find_element(By.TAG_NAME, "h1")
        input = self.browser.find_element(By.ID, "weighted-search-input")
        suggestions_list = self.browser.find_element(By.ID, "weighted-suggestions")

        # Marge decides to click on the searchbar, notices it comes to life, but there 
        # are no search suggestions yet.
        searchbar.click()
        self.assertIn("search-bar-active", searchbar.get_attribute("class"))
        suggestions = self.get_suggestions()
        self.assertTrue(len(suggestions) == 0)

        # Marge decides to type in a word and notices a list of good suggestions appear 
        # this time sorted by weight.
        input.send_keys("a")
        time.sleep(1)
        suggestions = self.get_suggestions()
        suggestions_text = [suggestion.text for suggestion in suggestions]
        self.assertEqual(["apple", "app", "apple orchard"], suggestions_text)

        # Marge deletes the word she entered and notices the suggestions disappear.
        input.send_keys("p")
        input.clear()
        time.sleep(1)
        suggestions = self.get_suggestions()
        self.assertTrue(suggestions_list.get_attribute("hidden"))

        # Marge trie a new search and notices the list of suggestions never grows beyond 10.
        input.send_keys("z")
        time.sleep(1)
        suggestions = self.get_suggestions()
        self.assertTrue(len(suggestions) == 10)

        # Marge clicks outside the searchbar and notices here search suggestions dissappeared
        # and the search bar itself goes back to normal.
        h1.click()
        time.sleep(1)
        suggestions = self.get_suggestions()
        self.assertTrue(suggestions_list.get_attribute("hidden"))
        self.assertNotIn("search-bar-active", searchbar.get_attribute("class"))

        # Panicked, Marge clicks back on the searchbar. She is relieved to find her
        # suggestions have returned.
        searchbar.click()
        time.sleep(1)
        suggestions = self.get_suggestions()
        self.assertTrue(len(suggestions) == 10)

        # She adds another letter to her search making a typo and notices the 
        # suggestions disappear.
        input.send_keys("zb")
        time.sleep(1)
        suggestions = self.get_suggestions()
        self.assertTrue(suggestions_list.get_attribute("hidden"))