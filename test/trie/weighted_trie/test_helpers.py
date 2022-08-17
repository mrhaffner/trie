from test.trie.weighted_trie.test_creation import TestWeightedTrieParent, TestWeightedTrieParentWithSuffixes
from trie.weighted_trie import WeightedTrie


class TestWeightedCreateNode(TestWeightedTrieParent):

    def setUp(self) -> None:
        super().setUp()
        self.node = self.trie._create_node()


    def test_edges_have_correct_length(self) -> None:
        self.assertEqual(len(self.node.edges), WeightedTrie.SIZE_CHAR_SET)


    def test_edges_are_none(self) -> None:
        for edge in self.node.edges:
            self.assertEqual(edge, None)


    def test_is_not_suffix_end(self) -> None:
        self.assertTrue(self.node.weight == 0)


class TestStandardTrieHashChar(TestWeightedTrieParent):

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


    def test_uppercase_letter_converts_to_lower(self) -> None:
        self.assertEqual(self.trie._hash_char("A"), 0)
        self.assertEqual(self.trie._hash_char("Z"), 25)


class TestStandardTrieIsValidSuffix(TestWeightedTrieParent):

    def test_suffix_longer_than_max_depth_is_invalid(self):
        self.assertFalse(self.trie._is_valid_suffix("h" * (self.trie._max_depth + 1)))


    def test_valid_suffix_returns_true(self):
        self.assertTrue(self.trie._is_valid_suffix("Hello"))


    def test_non_hashable_suffix_is_invalid(self):
        self.assertFalse(self.trie._is_valid_suffix("&%$")) 


class TestGetNodeFromStr(TestWeightedTrieParentWithSuffixes):

    def test_empty_str(self) -> None:
        self.assertEqual(self.trie._get_node_from_str(""), self.trie._root)


    def test_invalid_word(self) -> None:
        self.assertIsNone(self.trie._get_node_from_str("&!&"))


    def test_word_not_in_trie(self) -> None:
        self.assertIsNone(self.trie._get_node_from_str("bee"))

    
    def test_longer_overlapping(self) -> None:
        self.assertIsNone(self.trie._get_node_from_str("apple orchards"))


    def test_equal_word_non_overlapping(self) -> None:
        node = self.trie._get_node_from_str("dog")
        
        for edge in node.edges:
            self.assertIsNone(edge)


    def test_shorter_overlapping(self) -> None:
        node = self.trie._get_node_from_str("app")
        l_hash = self.trie._hash_char("l")

        for i, edge in enumerate(node.edges):
            if i == l_hash:
                self.assertIsNotNone(edge)
            else:
                self.assertIsNone(edge)


class TestReverseHashChar(TestWeightedTrieParent):

    def test_converts_index_to_letter(self) -> None:
        self.assertEqual("a", self.trie._reverse_hash_char(0))
        self.assertEqual("z", self.trie._reverse_hash_char(25))


    def test_converts_space(self) -> None:
        self.assertEqual(" ", self.trie._reverse_hash_char(26))


    def test_raises_error_if_invalid_index(self) -> None:
        with self.assertRaises(ValueError):
            self.trie._reverse_hash_char(-1)
        with self.assertRaises(ValueError):
            self.trie._reverse_hash_char(27)