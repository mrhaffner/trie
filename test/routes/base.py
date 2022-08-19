from app import cached_trie, create_app, trie, weighted_trie
from flask import Flask
from flask_testing import TestCase


class TestApiParent(TestCase):


    def setUp(self):
        self.client = create_app(False).test_client()
        self.starting_suffixes = ["app", "apple", "apple orchard", "dog"]
        for suffix in self.starting_suffixes:
            trie.insert(suffix)
        

    def create_app(self):
        for suffix in trie.get_suffixes():
            trie.delete(suffix)
        app = Flask(__name__)
        app.config["TESTING"] = True
        return app


class TestWeightedApiParent(TestApiParent):

    def setUp(self):
        self.client = create_app(False).test_client()
        self.starting_suffixes = [{"suffix": "app", "weight": 1}, {"suffix": "apple", "weight": 4}, 
                              {"suffix": "apple orchard", "weight": 1}, {"suffix": "dog", "weight": 5}]
        for suffix in self.starting_suffixes:
            weighted_trie.insert(suffix)
        

class TestCachedApiParent(TestApiParent):

    def setUp(self):
        self.client = create_app(False).test_client()
        self.starting_suffixes = [{"suffix": "app", "weight": 1}, {"suffix": "apple", "weight": 4}, 
                              {"suffix": "apple orchard", "weight": 1}, {"suffix": "dog", "weight": 5}]
        for suffix in self.starting_suffixes:
            cached_trie.insert(suffix)