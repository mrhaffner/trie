from test.api.test_api_setup import TestApi


class TestTriePost(TestApi):

    def test_valid_suffix(self) -> None:
        post_data = {"suffix": "cat"}
        post_response = self.client.post("/api/trie", data = post_data)
        self.assertEqual(post_response.status_code, 200)
        self.assertEqual(post_response.json["suffix"], "cat")
        
        get_response = self.client.get("api/trie?prefix=ca")
        self.assertIn("t", get_response.json)


    def test_invalid_suffix(self) -> None:
        post_data = {"suffix": "&~&"}
        post_response = self.client.post("/api/trie", data = post_data)
        self.assertEqual(post_response.status_code, 422)
        
        get_response = self.client.get("api/trie?prefix=&")
        self.assertNotIn("~&", get_response.json)


    def test_no_suffix(self) -> None:
        post_response = self.client.post("/api/trie")
        self.assertEqual(post_response.status_code, 400)