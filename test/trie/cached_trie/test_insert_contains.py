from test.trie.cached_trie.test_creation import TestCachedTrieParent
from trie.cached_trie import CachedTrie


class TestStandardTrieInsertAndContains(TestCachedTrieParent):

    def test_inserts_valid_suffix(self) -> None:
        self.assertTrue(self.trie.insert({"suffix": "Hello Matt", "weight": 1}))
        self.assertTrue(self.trie.contains("Hello Matt"))


    def test_inserts_empty_suffix(self) -> None:
        self.assertTrue(self.trie.insert({"suffix": "", "weight": 1}))
        self.assertTrue(self.trie.contains(""))


    # use patch for tests that depend on other functions?
    def test_does_not_add_too_long_suffix(self) -> None:
        self.assertFalse(self.trie.insert({"suffix": "h" * (self.trie._max_depth + 1), "weight": 1}))
        self.assertFalse(self.trie.contains("h" * (self.trie._max_depth + 1)))


    def test_does_not_add_suffix_with_bad_chars(self) -> None:
        self.assertFalse(self.trie.insert({"suffix": "&%$", "weight": 1}))
        self.assertFalse(self.trie.contains("&%$"))
        

    def test_inserts_duplicate(self) -> None:
        self.assertTrue(self.trie.insert({"suffix": "Hello", "weight": 1}))
        self.assertTrue(self.trie.insert({"suffix": "Hello", "weight": 1}))
        self.assertTrue(self.trie.contains("Hello"))


    def test_inserts_duplicate_updates_weight(self) -> None:
        self.assertTrue(self.trie.insert({"suffix": "Hello", "weight": 1}))
        self.assertTrue(self.trie.insert({"suffix": "Hello", "weight": 2}))
        node = self.trie._get_node_from_str("Hello")
        self.assertTrue(node.weight == 2)


    def test_inserts_shorter_overlapping_suffix(self) -> None:
        self.assertTrue(self.trie.insert({"suffix": "Hello", "weight": 1}))
        self.assertTrue(self.trie.insert({"suffix": "He", "weight": 1}))
        self.assertTrue(self.trie.contains("Hello"))
        self.assertTrue(self.trie.contains("He"))


    def test_inserts_longer_overlapping_suffix(self) -> None:
        self.assertTrue(self.trie.insert({"suffix": "He", "weight": 1}))
        self.assertTrue(self.trie.insert({"suffix": "Hello", "weight": 1}))
        self.assertTrue(self.trie.contains("He"))
        self.assertTrue(self.trie.contains("Hello"))


    def test_adjusts_cache_past_limit(self) -> None:
        trie = CachedTrie(2)
        suffix_dicts = [{"suffix": "a", "weight": 1}, {"suffix": "b", "weight": 2}, 
                        {"suffix": "c", "weight": 3}]
        for entry in suffix_dicts:
            trie.insert(entry)
        self.assertEqual(trie.get_suffixes(), ["c", "b"])


    def test_updates_cache_on_duplicate_insert(self) -> None:
        trie = CachedTrie(3)
        suffix_dicts = [{"suffix": "a", "weight": 1}, {"suffix": "b", "weight": 2}, 
                        {"suffix": "a", "weight": 3}]
        for entry in suffix_dicts:
            trie.insert(entry)
        self.assertEqual(trie.get_suffixes(), ["a", "b"])