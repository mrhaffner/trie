import unittest

from app import trie
from selenium import webdriver


class FunctionalTest(unittest.TestCase):

    def setUp(self):
        self.starting_suffixes = ["app", "apple", "apple orchard", "dog"] 
        self.starting_suffixes += ["z" * i for i in range(2, 16)]
        for suffix in self.starting_suffixes:
            trie.insert(suffix)

        self.browser = webdriver.Chrome()
        self.base_url = "http://127.0.0.1:5000/"

    
    def tearDown(self):
        self.browser.quit()