import unittest

from abc import ABCMeta
from unittest.mock import patch
from trie.abstract_trie import AbstractTrie


class TestAbstractTrie(unittest.TestCase):
    
    @patch("trie.abstract_trie.AbstractTrie.__abstractmethods__", set())
    def setUp(self) -> None:
        self.trie = AbstractTrie()


    def test_is_abstract(self) -> None:
        self.assertTrue(isinstance(AbstractTrie, ABCMeta))


    def test_cannot_instantiate(self) -> None:
        with self.assertRaises(TypeError):
            AbstractTrie()


    def test_has_abstract_insert(self) -> None:
        with self.assertRaises(NotImplementedError):
            self.trie.insert("w")


    def test_has_abstract_delete(self) -> None:
        with self.assertRaises(NotImplementedError):
            self.trie.delete("w")


    def test_has_abstract_contains(self) -> None:
        with self.assertRaises(NotImplementedError):
            self.trie.contains("w")

    
    def test_has_abstract_get_all(self) -> None:
        with self.assertRaises(NotImplementedError):
            self.trie.get_all()


    def test_has_abstract_get_suggestions(self) -> None:
        with self.assertRaises(NotImplementedError):
            self.trie.get_suggestions("w")