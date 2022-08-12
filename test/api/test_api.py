from app import app, starting_suffixes
from flask import Flask
from flask_testing import TestCase


class TestApi(TestCase):

    def setUp(self):
        self.client = app.test_client()
        

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app


    def test_api_base_route(self):
        response = self.client.get("/api")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, "Welcome to the API.")


    def test_trie_get_all(self):
        response = self.client.get("/api/trie")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, starting_suffixes)


    def test_trie_get_from_prefix(self):
        expected_reponse = ["pp", "pple", "pple orchard"]
        response = self.client.get("/api/trie?prefix=a")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_reponse)


    def test_trie_get_from_prefix_with_space(self):
        expected_reponse = ["rchard"]
        response = self.client.get("/api/trie?prefix=apple%20o")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_reponse)


    def test_get_with_shorter_limit(self):
        expected_reponse = ["pp"]
        response = self.client.get("/api/trie?prefix=a&limit=1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_reponse)


    def test_get_with_equal_limit(self):
        expected_reponse = ["pp", "pple", "pple orchard"]
        response = self.client.get("/api/trie?prefix=a&limit=3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_reponse)


    def test_get_with_longer_limit(self):
        expected_reponse = ["pp", "pple", "pple orchard"]
        response = self.client.get("/api/trie?prefix=a&limit=10")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_reponse)
