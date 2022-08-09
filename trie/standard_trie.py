import math

from trie.abstract_trie import AbstractTrie
from trie.trie_node import TrieNode
from typing import List


class StandardTrie(AbstractTrie):
    """A Trie (Suffix Tree)"""

    SIZE_CHAR_SET = 27

    # note about max.inf being a float
    # do we need to test this default max_depth behavior?
    def __init__(self, max_depth: int = math.inf) -> None:
        if max_depth < 0:
            raise ValueError("max_depth must be a positive integer")

        self._root = self._create_node()
        # automatically includes the empty string
        self._root.is_suffix_end = True
        self._max_depth = max_depth

    
    def _create_node(self) -> TrieNode:
        return TrieNode(StandardTrie.SIZE_CHAR_SET)


    def insert(self, suffix: str) -> bool:
        if not self._is_valid_suffix(suffix):
            return False
        
        cur_node = self._root

        for char in suffix:
            hash_code = self._hash_char(char)

            if not cur_node.edges[hash_code]:
                cur_node.edges[hash_code] = self._create_node()

            cur_node = cur_node.edges[hash_code]

        cur_node.is_suffix_end = True

        return True


    def _is_valid_suffix(self, suffix: str) -> bool:
        """
        A valid suffix may contain only english letters and/or spaces
        Returns True if the given suffix may be inserted into this Trie
        """
        if len(suffix) > self._max_depth:
            return False

        try:
            for char in suffix:
                self._hash_char(char)
        except TypeError:
            return False
        except ValueError:
            return False
        
        return True


    def _hash_char(self, char: str) -> int:
        """
        Converts and returns a single character to a hashcode
        Upper case letters are converted to lower case

        Example hash codes:
            a = 0
            z = 25
            space = 26

        Raises ValueError if char is not an english letter or a space
        Raises TypeError if the length of char is not 1
        """
        if char == " ":
            return 26
        else:
            hash_code = ord(char.lower()) - ord("a")
            if hash_code < 0 or hash_code > 26:
                raise ValueError("Only accepts english letters or a space")

            return hash_code


    def contains(self, suffix: str) -> bool:
        cur_node = self._root

        for char in suffix:
            if not self._is_valid_suffix(char):
                return False

            hash_code = self._hash_char(char)
            cur_node = cur_node.edges[hash_code]

            if cur_node is None:
                return False
            
        if cur_node.is_suffix_end:
            return True
        else:
            return False


    def delete(self, suffix: str) -> bool:
        pass


    def get_all_suffixes(self) -> List[str]:
        pass


    def get_suffixes(self, prefix: str) -> List[str]:
        pass


