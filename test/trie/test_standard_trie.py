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


class TestStandardTrieHashChar(TestStandardTrieParent):

    def test_converts_letter_to_0_index_alphabetical_num(self) -> None:
        self.assertEquals(self.trie._hash_char("a"), 0)
        self.assertEquals(self.trie._hash_char("z"), 25)


    def test_converts_space(self) -> None:
        self.assertEquals(self.trie._hash_char(" "), 26)
    

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
        self.assertEquals(self.trie._hash_char("A"), 0)
        self.assertEquals(self.trie._hash_char("Z"), 25)


class TestStandardTrieIsValidSuffix(TestStandardTrieParent):

    def test_suffix_longer_than_max_depth_is_invalid(self):
        self.assertFalse(self.trie._is_valid_suffix("h" * (self.trie._max_depth + 1)))


    def test_valid_suffix_returns_true(self):
        self.assertTrue(self.trie._is_valid_suffix("Hello"))


    # use patch for tests that depend on other functions?
    def test_non_hashable_suffix_is_invalid(self):
        self.assertFalse(self.trie._is_valid_suffix("&%$")) 


class TestStandardTrieInsert(TestStandardTrieParent):

    # contains?
    def test_inserts_valid_suffix(self) -> None:
        self.assertTrue(self.trie.insert("Hello"))
        self.assertTrue(self.trie.insert("Hello Matt"))
        self.assertTrue(self.trie.insert("He"))
        self.assertTrue(self.trie.insert(""))


    # use patch for tests that depend on other functions?
    def test_does_not_add_invalid_suffix(self) -> None:
        self.assertFalse(self.trie.insert("&%$"))
        self.assertFalse(self.trie.insert("h" * (self.trie._max_depth + 1)))
        

    def test_inserts_duplicate(self) -> None:
        pass


    def test_inserts_shorter_overlapping_suffix(self) -> None:
        pass


    def test_inserts_longer_overlapping_suffix(self) -> None:
        pass



        