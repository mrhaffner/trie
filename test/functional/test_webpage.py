import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from test.functional.base import FunctionalTest


class TestWebpage(FunctionalTest):

    def get_suggestions(self):
        return self.browser.find_elements(By.CLASS_NAME, "suggestion")


    def test_api_loads(self):
        self.browser.get(self.base_url + "api")
        element = self.browser.find_element(By.TAG_NAME, "pre")
        self.assertEqual(element.text, "\"Welcome to the API.\"")


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


    def test_search_bar_behavior(self):
        # Marge visits the webpage exited to try out the search bar.
        self.browser.get(self.base_url)
        searchbar = self.browser.find_element(By.ID, "trie-search-bar")
        h1 = self.browser.find_element(By.TAG_NAME, "h1")
        input = self.browser.find_element(By.ID, "search-input")
        suggestions_list = self.browser.find_element(By.ID, "suggestions")

        # Marge decides to click on the searchbar, notices it comes to life, but there 
        # are no search suggestions yet.
        searchbar.click()
        self.assertIn("search-bar-active", searchbar.get_attribute("class"))
        suggestions = self.get_suggestions()
        self.assertTrue(len(suggestions) == 0)

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