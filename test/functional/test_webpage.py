import time
import unittest

from app import trie
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWebapge(unittest.TestCase):

    def setUp(self):
        self.starting_suffixes = ["app", "apple", "apple orchard", "dog"]
        for suffix in self.starting_suffixes:
            trie.insert(suffix)

        self.browser = webdriver.Chrome()
        self.base_url = "http://127.0.0.1:5000/"

    
    def tearDown(self):
        self.browser.quit()


    def test_api_loads(self):
        self.browser.get(self.base_url + "api")
        element = self.browser.find_element(By.TAG_NAME, "pre")
        self.assertEqual(element.text, "\"Welcome to the API.\"")


    def test_layout_and_styling(self):
        self.browser.get(self.base_url)
        self.browser.set_window_size(1024, 768)
        searchbar = self.browser.find_element(By.ID, "search-input")
        self.assertAlmostEqual(
            searchbar.location["x"] + searchbar.size["width"] / 2,
            1008 / 2,
            delta=10
        )


    def test_search_yields_correct_suggestions(self):
        self.browser.get(self.base_url)
        searchbar = self.browser.find_element(By.ID, "search-input")
        searchbar.send_keys("ap")
        # wait for
        time.sleep(1)
        suggestions = self.browser.find_elements(By.CLASS_NAME, "auto-suggetion")
        suggestions_text = [suggestion.text for suggestion in suggestions]
        self.assertEqual(["app", "apple", "apple_orchard"], suggestions_text)