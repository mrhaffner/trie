from test.routes.base import TestApiParent, TestWeightedApiParent


class TestTriePost(TestApiParent):

    def test_valid_suffix(self) -> None:
        post_data = {"suffix": "cat"}
        post_response = self.client.post("/api/trie", data = post_data)
        self.assertEqual(post_response.status_code, 200)
        self.assertEqual(post_response.json["suffix"], "cat")
        
        get_response = self.client.get("/api/trie?suffix=cat")
        self.assertEqual(get_response.status_code, 200)


    def test_invalid_suffix(self) -> None:
        post_data = {"suffix": "&~&"}
        post_response = self.client.post("/api/trie", data = post_data)
        self.assertEqual(post_response.status_code, 422)


    def test_no_suffix(self) -> None:
        post_response = self.client.post("/api/trie")
        self.assertEqual(post_response.status_code, 400)


class TestWeightedTriePost(TestWeightedApiParent):

    def test_valid_suffix(self) -> None:
        post_data = {"suffix": "cat", "weight": 1}
        post_response = self.client.post("/api/weighted-trie", data = post_data)
        self.assertEqual(post_response.status_code, 200)
        self.assertEqual(post_response.json["suffix"], "cat")
        
        get_response = self.client.get("/api/weighted-trie?suffix=cat")
        self.assertEqual(get_response.status_code, 200)


    def test_invalid_suffix(self) -> None:
        post_data = {"suffix": "&~&", "weight": 1}
        post_response = self.client.post("/api/weighted-trie", data = post_data)
        self.assertEqual(post_response.status_code, 422)


    def test_invalid_weight(self) -> None:
        post_data = {"suffix": "cat", "weight": "apple"}
        post_response = self.client.post("/api/weighted-trie", data = post_data)
        self.assertEqual(post_response.status_code, 400)


    def test_no_suffix(self) -> None:
        post_data = {"weight": 1}
        post_response = self.client.post("/api/weighted-trie", data = post_data)
        self.assertEqual(post_response.status_code, 400)


    def test_no_weight(self) -> None:
        post_data = {"suffix": "cat"}
        post_response = self.client.post("/api/weighted-trie", data = post_data)
        self.assertEqual(post_response.status_code, 400)


    def test_no_data(self) -> None:
        post_response = self.client.post("/api/weighted-trie")
        self.assertEqual(post_response.status_code, 400)