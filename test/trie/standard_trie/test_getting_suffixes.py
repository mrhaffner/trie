from test.trie.standard_trie.test_creation import TestStandardTrieParent
from trie.standard_trie import StandardTrie


class TestGetSuffixes(TestStandardTrieParent):
    
    SUFFIXES = ["dog", "apple", "app", "apple orchard"]

    def setUp(self) -> None:
        super().setUp()

        for suffix in TestGetSuffixes.SUFFIXES:
            self.trie.insert(suffix)


    def test_empty_trie(self) -> None:
        self.assertEquals(StandardTrie().get_suffixes("a"), [""])

    
    def test_empty_string(self) -> None:
        test_arr = ["apple", "app", "apple orchard"]
        self.assertEquals(self.trie.get_suffixes(""), test_arr)


class TestGetSuffixesFromNode(TestStandardTrieParent):
    
    SUFFIXES = ["dog", "apple", "app", "apple orchard"]

    def setUp(self) -> None:
        super().setUp()

        for suffix in TestGetSuffixes.SUFFIXES:
            self.trie.insert(suffix)

        self.parent_node = self.trie._get_node_from_str("ap")


    def test_gets_multiple_suffixes(self) -> None:
        pass