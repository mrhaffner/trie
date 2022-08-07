import unittest

from trie.abstract_trie import AbstractTrie
from trie.standard_trie import StandardTrie


class TestStandardTrie(unittest.TestCase):

    # def setUp(self) -> None:
    #     self.trie = StandardTrie()


    def test_inherits_from_abstract_trie(self) -> None:
        self.assertTrue(issubclass(StandardTrie, AbstractTrie))


    def test_implements_abstract_methods(self) -> None:
        # will raise error from instantion if abstract methods are not implemented
        StandardTrie()