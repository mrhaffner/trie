from test.trie.standard_trie.test_creation import TestStandardTrieParent
from trie.standard_trie import StandardTrie


class TestCreateNode(TestStandardTrieParent):

    def setUp(self) -> None:
        super().setUp()
        self.node = self.trie._create_node()


    def test_edges_have_correct_length(self) -> None:
        self.assertEqual(len(self.node.edges), StandardTrie.SIZE_CHAR_SET)


    def test_edges_are_none(self) -> None:
        for edge in self.node.edges:
            self.assertEqual(edge, None)


    def test_is_not_suffix_end(self) -> None:
        self.assertFalse(self.node.is_suffix_end)


class TestStandardTrieHashChar(TestStandardTrieParent):

    def test_converts_letter_to_0_index_alphabetical_num(self) -> None:
        self.assertEqual(self.trie._hash_char("a"), 0)
        self.assertEqual(self.trie._hash_char("z"), 25)


    def test_converts_space(self) -> None:
        self.assertEqual(self.trie._hash_char(" "), 26)
    

    def test_raises_error_if_length_not_one(self) -> None:
        with self.assertRaises(TypeError):
            self.trie._hash_char("")
        with self.assertRaises(TypeError):
            self.trie._hash_char("22")


    def test_raises_error_if_invalid_char(self) -> None:
        # value less than ord(a) which is 0 
        with self.assertRaises(ValueError):
            self.trie._hash_char("&")
        # value greater than ord(z) + 1 which is 26
        with self.assertRaises(ValueError):
            self.trie._hash_char("~")


    def test_uppcase_letter_converts_to_lower(self) -> None:
        self.assertEqual(self.trie._hash_char("A"), 0)
        self.assertEqual(self.trie._hash_char("Z"), 25)


class TestStandardTrieIsValidSuffix(TestStandardTrieParent):

    def test_suffix_longer_than_max_depth_is_invalid(self):
        self.assertFalse(self.trie._is_valid_suffix("h" * (self.trie._max_depth + 1)))


    def test_valid_suffix_returns_true(self):
        self.assertTrue(self.trie._is_valid_suffix("Hello"))


    # use patch for tests that depend on other functions?
    def test_non_hashable_suffix_is_invalid(self):
        self.assertFalse(self.trie._is_valid_suffix("&%$")) 