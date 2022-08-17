from test.routes.base import TestApiParent


class TestSetup(TestApiParent):

    def test_api_base_route(self):
        response = self.client.get("/api")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, "Welcome to the API.")