from test.routes.base import TestApiParent, TestCachedApiParent, TestWeightedApiParent


class TestTrieGet(TestApiParent):

    def test_suffix_in_trie(self) -> None:
        response = self.client.get("/api/trie?suffix=dog")
        self.assertEqual(response.status_code, 200)


    def test_suffix_in_trie_with_spaces(self) -> None:
        response = self.client.get("/api/trie?suffix=apple%20orchard")
        self.assertEqual(response.status_code, 200)


    def test_suffix_not_in_trie(self) -> None:
        response = self.client.get("/api/trie?suffix=cat")
        self.assertEqual(response.status_code, 404)


    def test_no_suffix(self) -> None:
        response = self.client.get("/api/trie")
        self.assertEqual(response.status_code, 400)


class TestWeightedTrieGet(TestWeightedApiParent):

    def test_suffix_in_trie(self) -> None:
        response = self.client.get("/api/weighted-trie?suffix=dog")
        self.assertEqual(response.status_code, 200)


    def test_suffix_in_trie_with_spaces(self) -> None:
        response = self.client.get("/api/weighted-trie?suffix=apple%20orchard")
        self.assertEqual(response.status_code, 200)


    def test_suffix_not_in_trie(self) -> None:
        response = self.client.get("/api/weighted-trie?suffix=cat")
        self.assertEqual(response.status_code, 404)


    def test_no_suffix(self) -> None:
        response = self.client.get("/api/weighted-trie")
        self.assertEqual(response.status_code, 400)


class TestCachedTrieGet(TestCachedApiParent):

    def test_suffix_in_trie(self) -> None:
        response = self.client.get("/api/cached-trie?suffix=dog")
        self.assertEqual(response.status_code, 200)


    def test_suffix_in_trie_with_spaces(self) -> None:
        response = self.client.get("/api/cached-trie?suffix=apple%20orchard")
        self.assertEqual(response.status_code, 200)


    def test_suffix_not_in_trie(self) -> None:
        response = self.client.get("/api/cached-trie?suffix=cat")
        self.assertEqual(response.status_code, 404)


    def test_no_suffix(self) -> None:
        response = self.client.get("/api/cached-trie")
        self.assertEqual(response.status_code, 400)