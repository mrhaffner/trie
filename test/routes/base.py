from app import create_app, trie
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