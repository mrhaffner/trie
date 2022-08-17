import unittest

from trie.abstract_trie import AbstractTrie
from trie.weighted_trie import WeightedTrie
from trie.weighted_trie_node import WeightedTrieNode


class TestWeightedTrieParent(unittest.TestCase):

    def setUp(self) -> None:
        self.trie = WeightedTrie(20)


class TestWeightedTrieParentWithSuffixes(TestWeightedTrieParent):

    def setUp(self) -> None:
        super().setUp()
        self.test_suffixes = [{"suffix": "app", "weight": 1}, {"suffix": "apple", "weight": 4}, 
                              {"suffix": "apple orchard", "weight": 1}, {"suffix": "dog", "weight": 5}]

        for suffix in self.test_suffixes:
            self.trie.insert(suffix)
            

class TestWeightedTrieCreation(TestWeightedTrieParent):

    # or is it a sublcass of standard trie?
    def test_inherits_from_abstract_trie(self) -> None:
        self.assertTrue(issubclass(WeightedTrie, AbstractTrie))


    # or is it a sublcass of standard trie?
    # will raise error from instantion if abstract methods are not implemented
    def test_implements_abstract_methods(self) -> None:
        WeightedTrie()


    def test_instantiation_creates_root_node(self) -> None:
        self.assertTrue(isinstance(self.trie._root, WeightedTrieNode))


    def test_creation_with_negative_max_depth_throws_error(self) -> None:
        with self.assertRaises(ValueError):
            WeightedTrie(-1)