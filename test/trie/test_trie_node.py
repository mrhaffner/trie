import unittest

from trie.trie_node import TrieNode


class TestTrieNode(unittest.TestCase):

    def setUp(self) -> None:
        self.edges_length = 3
        self.node = TrieNode(self.edges_length)


    def test_edges_has_length_of_input(self) -> None:
        self.assertEqual(len(self.node.edges), self.edges_length)


    def test_edges_contains_only_nones(self) -> None:
        for node in self.node.edges:
            self.assertEqual(node, None)


    def test_is_suffix_end_starts_false(self) -> None:
        self.assertFalse(self.node.is_suffix_end)


    def test_edges_cannot_be_negative(self) -> None:
        with self.assertRaises(ValueError):
            TrieNode(-1)