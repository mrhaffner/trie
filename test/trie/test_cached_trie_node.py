import unittest

from trie.cached_trie_node import CachedTrieNode


class TestTrieNode(unittest.TestCase):

    def setUp(self) -> None:
        self.edges_length = 3
        self.node = CachedTrieNode(self.edges_length)


    def test_edges_has_length_of_input(self) -> None:
        self.assertEqual(len(self.node.edges), self.edges_length)


    def test_edges_contains_only_nones(self) -> None:
        for node in self.node.edges:
            self.assertEqual(node, None)


    def test_default_weight_is_zero(self) -> None:
        self.assertTrue(self.node.weight == 0)


    def test_edges_cannot_be_negative(self) -> None:
        with self.assertRaises(ValueError):
            CachedTrieNode(-1)


    def test_cache_starts_empty(self) -> None:
        self.assertEqual(len(self.node.cache), 0)