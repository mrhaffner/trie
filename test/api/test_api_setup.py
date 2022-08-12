from app import app, trie
from flask import Flask
from flask_testing import TestCase


class TestApiParent(TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.starting_suffixes = ["app", "apple", "apple orchard", "dog"]
        for suffix in self.starting_suffixes:
            trie.insert(suffix)
        

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

class TestSetup(TestApiParent):

    def test_api_base_route(self):
        response = self.client.get("/api")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, "Welcome to the API.")