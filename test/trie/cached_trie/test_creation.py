import unittest

from trie.abstract_trie import AbstractTrie
from trie.cached_trie import CachedTrie
from trie.cached_trie_node import CachedTrieNode


class TestCachedTrieParent(unittest.TestCase):

    def setUp(self) -> None:
        self.trie = CachedTrie(4, max_depth = 20)


class TestCachedTrieParentWithSuffixes(TestCachedTrieParent):

    def setUp(self) -> None:
        super().setUp()
        self.test_suffixes = [{"suffix": "app", "weight": 1}, {"suffix": "apple", "weight": 4}, 
                              {"suffix": "apple orchard", "weight": 1}, {"suffix": "dog", "weight": 5}]

        for suffix in self.test_suffixes:
            self.trie.insert(suffix)
            

class TestCachedTrieCreation(TestCachedTrieParent):

    def test_inherits_from_abstract_trie(self) -> None:
        self.assertTrue(issubclass(CachedTrie, AbstractTrie))


    # will raise error from instantion if abstract methods are not implemented
    def test_implements_abstract_methods(self) -> None:
        CachedTrie(3)


    def test_instantiation_creates_root_node(self) -> None:
        self.assertTrue(isinstance(self.trie._root, CachedTrieNode))


    def test_creation_with_negative_max_depth_throws_error(self) -> None:
        with self.assertRaises(ValueError):
            CachedTrie(3, max_depth = -1)


    def test_creation_with_limit_less_than_one_throws_error(self) -> None:
        with self.assertRaises(ValueError):
            CachedTrie(0)