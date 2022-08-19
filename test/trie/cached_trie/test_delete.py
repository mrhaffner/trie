from test.trie.cached_trie.test_creation import TestCachedTrieParentWithSuffixes


class TestWeightedDelete(TestCachedTrieParentWithSuffixes):

    def test_delete_suffix(self):
        test_word = "dog"
        self.assertTrue(self.trie.delete(test_word))
        for suffix_dict in self.test_suffixes:
            suffix = suffix_dict["suffix"]
            if suffix == test_word:
                self.assertFalse(self.trie.contains(suffix))
            else:
                self.assertTrue(self.trie.contains(suffix))


    def test_deletes_shorter_overlapping_suffix(self) -> None:
        test_word = "app"
        self.assertTrue(self.trie.delete(test_word))
        for suffix_dict in self.test_suffixes:
            suffix = suffix_dict["suffix"]
            if suffix == test_word:
                self.assertFalse(self.trie.contains(suffix))
            else:
                self.assertTrue(self.trie.contains(suffix))


    def test_delete_longer_overlapping_suffix(self) -> None:
        test_word = "apple orchard"
        self.assertTrue(self.trie.delete(test_word))
        for suffix_dict in self.test_suffixes:
            suffix = suffix_dict["suffix"]
            if suffix == test_word:
                self.assertFalse(self.trie.contains(suffix))
            else:
                self.assertTrue(self.trie.contains(suffix))


    def test_delete_suffix_not_in_trie(self) -> None:
        test_word = "bat"
        self.assertFalse(self.trie.delete(test_word))
        for suffix_dict in self.test_suffixes:
            suffix = suffix_dict["suffix"]
            self.assertTrue(self.trie.contains(suffix))


    def test_cannot_delete_empty_string(self) -> None:
        test_word = ""
        self.assertFalse(self.trie.delete(test_word))
        self.assertTrue(self.trie.contains(test_word))
        for suffix_dict in self.test_suffixes:
            suffix = suffix_dict["suffix"]
            self.assertTrue(self.trie.contains(suffix))


    def test_handles_too_long_suffix(self) -> None:
        test_word = "h" * (self.trie._max_depth + 1)
        self.assertFalse(self.trie.delete(test_word))
        self.assertFalse(self.trie.contains(test_word))
        for suffix_dict in self.test_suffixes:
            suffix = suffix_dict["suffix"]
            self.assertTrue(self.trie.contains(suffix))
        

    def test_handles_suffix_with_bad_chars(self) -> None:
        test_word = "&~"
        self.assertFalse(self.trie.delete(test_word))
        self.assertFalse(self.trie.contains(test_word))
        for suffix_dict in self.test_suffixes:
            suffix = suffix_dict["suffix"]
            self.assertTrue(self.trie.contains(suffix))


    def test_updates_cache(self) -> None:
        self.trie.delete("apple")
        expected = ["dog", "app", "apple orchard"]
        self.assertEqual(self.trie.get_suffixes(), expected)