import unittest

from trie.abstract_trie import AbstractTrie
from trie.standard_trie import StandardTrie
from trie.trie_node import TrieNode


class TestStandardTrieParent(unittest.TestCase):

    def setUp(self) -> None:
        self.trie = StandardTrie(20)


class TestStandardTrieParentWithSuffixes(TestStandardTrieParent):

    def setUp(self) -> None:
        super().setUp()
        self.test_suffixes = ["app", "apple", "apple orchard", "dog"]

        for suffix in self.test_suffixes:
            self.trie.insert(suffix)
            

class TestStandardTrieCreation(TestStandardTrieParent):

    def test_inherits_from_abstract_trie(self) -> None:
        self.assertTrue(issubclass(StandardTrie, AbstractTrie))


    # will raise error from instantion if abstract methods are not implemented
    def test_implements_abstract_methods(self) -> None:
        StandardTrie()


    def test_instantiation_creates_root_node(self) -> None:
        self.assertTrue(isinstance(self.trie._root, TrieNode))


    def test_creation_with_negative_max_depth_throws_error(self) -> None:
        with self.assertRaises(ValueError):
            StandardTrie(-1)