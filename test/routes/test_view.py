from app import create_app
from flask import Flask
from flask_testing import TestCase


class TestView(TestCase):

    def setUp(self):
        self.client = create_app(False).test_client()
        

    def create_app(self):
        app = Flask(__name__)
        app.config["TESTING"] = True
        return app


    def test_webpage_runs(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


    def test_template_used(self):
        self.client.get("/")
        self.assert_template_used("index.html")