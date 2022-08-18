from typing import List
from test.trie.standard_trie.test_creation import TestStandardTrieParent, TestStandardTrieParentWithSuffixes
from trie.standard_trie import StandardTrie


class TestGetSuffixes(TestStandardTrieParentWithSuffixes):

    def test_empty_trie(self) -> None:
        self.assertEqual(StandardTrie().get_suffixes("a"), [])


    def test_not_in_trie(self) -> None:
        self.assertEqual(StandardTrie().get_suffixes("zebra"), [])


    def test_empty_string(self) -> None:
        test_arr = self.test_suffixes
        self.assertEqual(self.trie.get_suffixes(""), test_arr)


    def test_multiple_from_input(self) -> None:
        test_arr = ["pp", "pple", "pple orchard"]
        self.assertEqual(self.trie.get_suffixes("a"), test_arr)


    def test_longer_overlapping_not_in_trie(self) -> None:
        self.assertEqual(self.trie.get_suffixes("dogg"), [])


    def test_multiple_overlapping(self) -> None:
        test_arr = ["", "le", "le orchard"]
        self.assertEqual(self.trie.get_suffixes("app"), test_arr)


    def test_illegal_char(self) -> None:
        self.assertEqual(self.trie.get_suffixes("&~&"), [])


    def test_default_input_root(self) -> None:
        test_arr = self.test_suffixes
        self.assertEqual(self.trie.get_suffixes(), test_arr)


class TestGetSuffixesFromNode(TestStandardTrieParent):
    
    def setUp(self) -> None:
        super().setUp()
        self.node = self.trie._root


    def add_suffixes(self, suffixes: List[str]) -> None:
        for suffix in suffixes:
            self.trie.insert(suffix)


    def test_empty_node(self) -> None:
        self.assertEqual(self.trie._get_suffixes_from_node(self.node), [])


    def test_single_suffix(self) -> None:
        suffixes = ["dog"]
        self.add_suffixes(suffixes)
        self.assertEqual(self.trie._get_suffixes_from_node(self.node), suffixes)


    def test_multiple_overlapping_suffixes(self) -> None:
        suffixes = ["app", "apple", "apple orchard"]
        self.add_suffixes(suffixes)
        self.assertEqual(self.trie._get_suffixes_from_node(self.node), suffixes)


    def test_multiple_suffixes_from_root(self) -> None:
        suffixes =  ["apple orchard", "dog"]
        self.add_suffixes(suffixes)
        self.assertEqual(self.trie._get_suffixes_from_node(self.node), suffixes)


    def test_gets_empty_str_from_start_node_when_suffix(self) -> None:
        suffixes = ["app", "apple"]
        self.add_suffixes(suffixes)
        node = self.trie._get_node_from_str("app")
        self.assertEqual(self.trie._get_suffixes_from_node(node), ["", "le"])


    def test_does_not_get_empty_str_from_root(self) -> None:
        self.assertEqual(self.trie._get_suffixes_from_node(self.node), [])