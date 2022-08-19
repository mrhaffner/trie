from test.routes.base import TestApiParent, TestCachedApiParent, TestWeightedApiParent


class TestTrieDelete(TestApiParent):

    def test_delete_word_in_trie(self) -> None:
        delete_data = {"suffix": "dog"}
        delete_response = self.client.delete("/api/trie", data = delete_data)
        self.assertEqual(delete_response.status_code, 204)
        
        get_response = self.client.get("/api/trie/?suffix=cat")
        self.assertEqual(get_response.status_code, 404)


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


class TestWeightedTrieDelete(TestWeightedApiParent):

    def test_delete_word_in_trie(self) -> None:
        delete_data = {"suffix": "dog"}
        delete_response = self.client.delete("/api/weighted-trie", data = delete_data)
        self.assertEqual(delete_response.status_code, 204)
        
        get_response = self.client.get("/api/weighted-trie/?suffix=cat")
        self.assertEqual(get_response.status_code, 404)


    def test_delete_invalid_suffix(self) -> None:
        delete_data = {"suffix": "&~&"}
        delete_response = self.client.delete("/api/weighted-trie", data = delete_data)
        self.assertEqual(delete_response.status_code, 422)


    def test_delete_suffix_not_in_trie(self) -> None:
        delete_data = {"suffix": "bee"}
        delete_response = self.client.delete("/api/weighted-trie", data = delete_data)
        self.assertEqual(delete_response.status_code, 422)


    def test_no_suffix(self) -> None:
        delete_response = self.client.delete("/api/weighted-trie")
        self.assertEqual(delete_response.status_code, 400)


class TestCachedTrieDelete(TestCachedApiParent):

    def test_delete_word_in_trie(self) -> None:
        delete_data = {"suffix": "dog"}
        delete_response = self.client.delete("/api/cached-trie", data = delete_data)
        self.assertEqual(delete_response.status_code, 204)
        
        get_response = self.client.get("/api/cached-trie/?suffix=cat")
        self.assertEqual(get_response.status_code, 404)


    def test_delete_invalid_suffix(self) -> None:
        delete_data = {"suffix": "&~&"}
        delete_response = self.client.delete("/api/cached-trie", data = delete_data)
        self.assertEqual(delete_response.status_code, 422)


    def test_delete_suffix_not_in_trie(self) -> None:
        delete_data = {"suffix": "bee"}
        delete_response = self.client.delete("/api/cached-trie", data = delete_data)
        self.assertEqual(delete_response.status_code, 422)


    def test_no_suffix(self) -> None:
        delete_response = self.client.delete("/api/cached-trie")
        self.assertEqual(delete_response.status_code, 400)