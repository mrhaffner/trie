from test.unittests.trie.standard_trie.test_creation import TestStandardTrieParent


class TestStandardTrieInsertAndContains(TestStandardTrieParent):

    def test_inserts_valid_suffix(self) -> None:
        self.assertTrue(self.trie.insert("Hello Matt"))
        self.assertTrue(self.trie.contains("Hello Matt"))


    def test_inserts_empty_suffix(self) -> None:
        self.assertTrue(self.trie.insert(""))
        self.assertTrue(self.trie.contains(""))


    # use patch for tests that depend on other functions?
    def test_does_not_add_too_long_suffix(self) -> None:
        self.assertFalse(self.trie.insert("h" * (self.trie._max_depth + 1)))
        self.assertFalse(self.trie.contains("h" * (self.trie._max_depth + 1)))


    def test_does_not_add_suffix_with_bad_chars(self) -> None:
        self.assertFalse(self.trie.insert("&%$"))
        self.assertFalse(self.trie.contains("&%$"))
        

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