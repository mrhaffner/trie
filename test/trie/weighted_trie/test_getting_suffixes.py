from typing import List
from test.trie.weighted_trie.test_creation import TestWeightedTrieParent, TestWeightedTrieParentWithSuffixes
from trie.weighted_trie import WeightedTrie


class TestWeightedGetSuffixes(TestWeightedTrieParentWithSuffixes):

    def test_empty_trie(self) -> None:
        self.assertEqual(WeightedTrie().get_suffixes("a"), [])


    def test_not_in_trie(self) -> None:
        self.assertEqual(WeightedTrie().get_suffixes("zebra"), [])


    def test_empty_string(self) -> None:
        expected = ["dog", "apple", "app", "apple orchard"]
        self.assertEqual(self.trie.get_suffixes(""), expected)


    def test_multiple_from_input(self) -> None:
        expected = ["pple", "pp", "pple orchard"]
        self.assertEqual(self.trie.get_suffixes("a"), expected)


    def test_longer_overlapping_not_in_trie(self) -> None:
        self.assertEqual(self.trie.get_suffixes("dogg"), [])


    def test_multiple_overlapping(self) -> None:
        test_arr = ["le", "", "le orchard"]
        self.assertEqual(self.trie.get_suffixes("app"), test_arr)


    def test_illegal_char(self) -> None:
        self.assertEqual(self.trie.get_suffixes("&~&"), [])


    def test_default_input_root(self) -> None:
        test_arr = ["dog", "apple", "app", "apple orchard"]
        self.assertEqual(self.trie.get_suffixes(), test_arr)


class TestGetSuffixesFromNode(TestWeightedTrieParent):
    
    def setUp(self) -> None:
        super().setUp()
        self.node = self.trie._root


    def add_suffixes(self, suffixes: List[str]) -> None:
        for suffix in suffixes:
            self.trie.insert(suffix)


    def test_empty_node(self) -> None:
        self.assertEqual(self.trie._get_suffixes_from_node(self.node), [])


    def test_single_suffix(self) -> None:
        suffixes = [{"suffix": "dog", "weight": 5}]
        self.add_suffixes(suffixes)
        self.assertEqual(self.trie._get_suffixes_from_node(self.node), suffixes)


    def test_multiple_overlapping_suffixes(self) -> None:
        suffixes = [{"suffix": "app", "weight": 1}, {"suffix": "apple", "weight": 4}, 
                    {"suffix": "apple orchard", "weight": 1}]
        self.add_suffixes(suffixes)
        self.assertEqual(self.trie._get_suffixes_from_node(self.node), suffixes)


    def test_multiple_suffixes_from_root(self) -> None:
        suffixes = [{"suffix": "app", "weight": 5}, {"suffix": "dog", "weight": 4}]
        self.add_suffixes(suffixes)
        self.assertEqual(self.trie._get_suffixes_from_node(self.node), suffixes)


    def test_does_not_get_empty_str_from_root(self) -> None:
        self.assertEqual(self.trie._get_suffixes_from_node(self.node), [])