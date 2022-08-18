from test.routes.base import TestApiParent, TestWeightedApiParent


class TestTrieGet(TestApiParent):

    BASE_URL = "/api/trie/suggestions"

    def test_trie_get_all(self) -> None:
        response = self.client.get(TestTrieGet.BASE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, self.starting_suffixes)


    def test_trie_get_from_prefix(self) -> None:
        expected_reponse = ["pp", "pple", "pple orchard"]
        response = self.client.get(TestTrieGet.BASE_URL + "?prefix=a")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_reponse)


    def test_trie_get_from_prefix_with_space(self) -> None:
        expected_reponse = ["rchard"]
        response = self.client.get(TestTrieGet.BASE_URL + "?prefix=apple%20o")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_reponse)


    def test_trie_get_with_valid_prefix(self) -> None:
        expected_reponse = ["", " orchard"]
        response = self.client.get(TestTrieGet.BASE_URL + "?prefix=apple")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_reponse)


    def test_get_with_shorter_limit(self) -> None:
        expected_reponse = ["pp"]
        response = self.client.get(TestTrieGet.BASE_URL + "?prefix=a&limit=1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_reponse)


    def test_get_with_equal_limit(self) -> None:
        expected_reponse = ["pp", "pple", "pple orchard"]
        response = self.client.get(TestTrieGet.BASE_URL + "?prefix=a&limit=3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_reponse)


    def test_get_with_longer_limit(self) -> None:
        expected_reponse = ["pp", "pple", "pple orchard"]
        response = self.client.get(TestTrieGet.BASE_URL + "?prefix=a&limit=10")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_reponse)


    def test_get_empty_reponse(self) -> None:
        expected_reponse = []
        response = self.client.get(TestTrieGet.BASE_URL + "?prefix=bee")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_reponse)


class TestWeightedTrieGet(TestWeightedApiParent):

    BASE_URL = "/api/weighted-trie/suggestions"

    def test_trie_get_all(self) -> None:
        expected = ["dog", "apple", "app", "apple orchard"]
        expected += ["z" * i for i in range(2, 16)]
        response = self.client.get(TestWeightedTrieGet.BASE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)


    def test_trie_get_from_prefix(self) -> None:
        expected_reponse = ["pple", "pp", "pple orchard"]
        response = self.client.get(TestWeightedTrieGet.BASE_URL + "?prefix=a")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_reponse)


    def test_trie_get_from_prefix_with_space(self) -> None:
        expected_reponse = ["rchard"]
        response = self.client.get(TestWeightedTrieGet.BASE_URL + "?prefix=apple%20o")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_reponse)


    def test_get_with_shorter_limit(self) -> None:
        expected_reponse = ["pple"]
        response = self.client.get(TestWeightedTrieGet.BASE_URL + "?prefix=a&limit=1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_reponse)


    def test_get_with_equal_limit(self) -> None:
        expected_reponse = ["pple", "pp", "pple orchard"]
        response = self.client.get(TestWeightedTrieGet.BASE_URL + "?prefix=a&limit=3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_reponse)


    def test_get_with_longer_limit(self) -> None:
        expected_reponse = ["pple", "pp", "pple orchard"]
        response = self.client.get(TestWeightedTrieGet.BASE_URL + "?prefix=a&limit=10")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_reponse)


    def test_get_empty_reponse(self) -> None:
        expected_reponse = []
        response = self.client.get(TestWeightedTrieGet.BASE_URL + "?prefix=bee")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_reponse)