from test.api.test_api_setup import TestApiParent


class TestTrieDelete(TestApiParent):

    def test_delete_word_in_trie(self) -> None:
        delete_data = {"suffix": "dog"}
        delete_response = self.client.delete("/api/trie", data = delete_data)
        self.assertEqual(delete_response.status_code, 204)
        
        get_response = self.client.get("/api/trie/suggestions?prefix=ca")
        self.assertEqual(get_response.json, [])


    def test_delete_invalid_suffix(self) -> None:
        delete_data = {"suffix": "&~&"}
        delete_response = self.client.delete("/api/trie", data = delete_data)
        self.assertEqual(delete_response.status_code, 422)


    def test_delete_suffix_not_in_trie(self) -> None:
        delete_data = {"suffix": "bee"}
        delete_response = self.client.delete("/api/trie", data = delete_data)
        self.assertEqual(delete_response.status_code, 422)


    def test_no_suffix(self) -> None:
        delete_response = self.client.delete("/api/trie")
        self.assertEqual(delete_response.status_code, 400)