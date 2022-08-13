import multiprocessing

from app import create_app, trie
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWebapge(LiveServerTestCase):

    def create_app(self):
        # need this on unix, otherwise LiverServerTestCase will not work
        multiprocessing.set_start_method("fork")
        app = create_app()
        app.config['TESTING'] = True
        return app


    def setUp(self):
        self.starting_suffixes = ["app", "apple", "apple orchard", "dog"]
        for suffix in self.starting_suffixes:
            trie.insert(suffix)

        self.browser = webdriver.Chrome()
        self.url = "http://127.0.0.1:5000/api"

    
    def tearDown(self):
        self.browser.quit()


    def test_api_loads(self):
        self.browser.get(self.url)
        element = self.browser.find_element(By.TAG_NAME, "pre")
        self.assertEqual(element.text, "\"Welcome to the API.\"")
