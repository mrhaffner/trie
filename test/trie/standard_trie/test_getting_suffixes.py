from typing import List
from test.trie.standard_trie.test_creation import TestStandardTrieParent
from trie.standard_trie import StandardTrie


class TestGetSuffixes(TestStandardTrieParent):
    
    SUFFIXES = ["dog", "apple", "app", "apple orchard"]

    def setUp(self) -> None:
        super().setUp()

        for suffix in TestGetSuffixes.SUFFIXES:
            self.trie.insert(suffix)


    # def test_empty_trie(self) -> None:
    #     self.assertEquals(StandardTrie().get_suffixes("a"), [""])

    
    # def test_empty_string(self) -> None:
    #     test_arr = ["apple", "app", "apple orchard"]
    #     self.assertEquals(self.trie.get_suffixes(""), test_arr)









class TestGetSuffixesFromNode(TestStandardTrieParent):
    
    SUFFIXES = ["app", "apple", "apple orchard", "dog"]

    def setUp(self) -> None:
        super().setUp()
        self.node = self.trie._root


    def add_suffixes(self, suffixes: List[str]) -> None:
        for suffix in suffixes:
            self.trie.insert(suffix)


    def test_empty_node(self) -> None:
        self.assertEqual(self.trie._get_suffixes_from_node(self.node), [""])


    def test_single_suffix(self) -> None:
        suffixes = [TestGetSuffixesFromNode.SUFFIXES[-1]]
        self.add_suffixes(suffixes)
        self.assertEqual(self.trie._get_suffixes_from_node(self.node), [""] + suffixes)


    def test_multiple_overlapping_suffixes(self) -> None:
        suffixes = TestGetSuffixesFromNode.SUFFIXES[0:3]
        self.add_suffixes(suffixes)
        self.assertEqual(self.trie._get_suffixes_from_node(self.node), [""] + suffixes)


    def test_multiple_suffixes_from_root(self) -> None:
        suffixes = TestGetSuffixesFromNode.SUFFIXES[2:]
        self.add_suffixes(suffixes)
        self.assertEqual(self.trie._get_suffixes_from_node(self.node), [""] + suffixes)


    
