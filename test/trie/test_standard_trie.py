import unittest

from trie.abstract_trie import AbstractTrie
from trie.standard_trie import StandardTrie
from trie.trie_node import TrieNode


class TestStandardTrieParent(unittest.TestCase):

    def setUp(self) -> None:
        self.trie = StandardTrie(20)


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


class TestStandardTrieInsertAndContains(TestStandardTrieParent):

    # contains?
    def test_inserts_valid_suffix(self) -> None:
        self.assertTrue(self.trie.insert("Hello Matt"))
        self.assertTrue(self.trie.insert(""))
        self.assertTrue(self.trie.contains("Hello Matt"))
        self.assertTrue(self.trie.contains(""))


    # use patch for tests that depend on other functions?
    def test_does_not_add_invalid_suffix(self) -> None:
        self.assertFalse(self.trie.insert("&%$"))
        self.assertFalse(self.trie.insert("h" * (self.trie._max_depth + 1)))
        self.assertFalse(self.trie.contains("&%$"))
        self.assertFalse(self.trie.contains("h" * (self.trie._max_depth + 1)))
        

    def test_inserts_duplicate(self) -> None:
        self.assertTrue(self.trie.insert("Hello"))
        self.assertTrue(self.trie.insert("Hello"))
        self.assertTrue(self.trie.contains("Hello"))


    def test_inserts_shorter_overlapping_suffix(self) -> None:
        self.assertTrue(self.trie.insert("Hello"))
        self.assertTrue(self.trie.insert("He"))
        self.assertTrue(self.trie.contains("Hello"))
        self.assertTrue(self.trie.contains("He"))


    def test_inserts_longer_overlapping_suffix(self) -> None:
        self.assertTrue(self.trie.insert("He"))
        self.assertTrue(self.trie.insert("Hello"))
        self.assertTrue(self.trie.contains("He"))
        self.assertTrue(self.trie.contains("Hello"))



        